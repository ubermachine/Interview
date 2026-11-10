MODULE_4 = '''---

# MODULE 4: COMPONENT COMMUNICATION ARCHITECTURES

## Q12: Component Communication: Decorators (@Input/@Output) vs Modern Primitives (input/output/model)
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Persistent, Nagarro, EPAM (Asked in 96% of senior rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Modern Angular replaces reflection-heavy decorators (`@Input()`, `@Output()`) with signal-based functional primitives: `input<T>()` and `input.required<T>()` produce type-safe read-only `InputSignal` objects; `output<T>()` creates an `OutputEmitterRef` that emits standard DOM-like events without RxJS `EventEmitter` overhead; and `model<T>()` unifies two-way binding into a single writable `ModelSignal` with an implicit output emitter. This modern API is statically analyzable, tree-shakeable, and eliminates manual `ngOnChanges` diff checking."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `@Input` / `@Output` (Postal Letter & Registered Return Envelope):** You send a letter to the child component with instructions. If the child has something to report back, they must fill out a separate registered return envelope with an official stamp (`EventEmitter`).
  * **Modern Signals `input`, `output`, `model` (Walkie-Talkie & Shared Screen):** The child receives clear digital audio channels (`input()`), can speak directly over the channel (`output()`), or both can view and interact with the exact same shared display screen simultaneously (`model()`).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, input, output, model } from '@angular/core';

@Component({
  selector: 'app-modern-counter',
  standalone: true,
  template: `
    <button (click)="decrement()">-</button>
    <span>{{ count() }} (Max: {{ maxLimit() }})</span>
    <button (click)="increment()">+</button>
  `
})
export class ModernCounterComponent {
  maxLimit = input(100);                    // 1. Read-only InputSignal
  count = model(0);                         // 2. Two-way ModelSignal ([(count)]="parentVal")
  limitReached = output<{ val: number }>(); // 3. Modern output emitter (no RxJS EventEmitter)

  increment() {
    if (this.count() < this.maxLimit()) this.count.update(c => c + 1);
    else this.limitReached.emit({ val: this.count() });
  }
  decrement() { this.count.update(c => Math.max(0, c - 1)); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Does `output()` use RxJS `EventEmitter` under the hood? How do you listen to a modern `output()` as an RxJS Observable?"  
  * *Senior Answer:* "No, `output()` does **not** create an RxJS `EventEmitter` or `Subject` under the hood. It instantiates an internal `OutputEmitterRef`, which is lightweight and has zero dependency on RxJS. However, Angular provides full backward and cross-ecosystem interoperability via the `outputToObservable(comp.limitReached)` helper from `@angular/core/rxjs-interop`, allowing consumers to pipe output events into RxJS operators like `debounceTime` or `filter` whenever needed."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Communication Requirement | Legacy Decorator API | Modern Signal API (v17.3+) | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Pass data down from parent** | `@Input() title!: string;` | `title = input.required<string>();` | Change to `input()`; access value in template as `title()`. |
| **Pass events up to parent** | `@Output() clicked = new EventEmitter();` | `clicked = output<string>();` | Call `this.clicked.emit('payload')`. Parent binds via `(clicked)="handler($event)"`. |
| **Two-way synchronized state** | `@Input() val; @Output() valChange;` | `val = model(0);` | Declare `val = model()`; parent binds simply via `[(val)]="myState"`. |
| **Transform input values** | `set title(v) { ... }` or `@Input({ transform })` | `title = input('', { transform: fn })` | Pass pure transform function: `{ transform: booleanAttribute }`. |

---

## Q13: ViewChild vs ContentChild & Static vs Dynamic Resolution ({ static: true | false })
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Capgemini, Wells Fargo, Morgan Stanley (Classic tricky senior question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`@ViewChild` queries DOM elements, directives, or child components declared **inside the component's own template**. `@ContentChild` queries elements projected into the component from the parent via `<ng-content>`. The `{ static: true }` option forces Angular to resolve the query synchronously during change detection initialization—making it accessible in `ngOnInit`—but it **only works if the queried element is NOT wrapped inside structural directives** like `*ngIf` or `@if`. With `{ static: false }` (the default), resolution is dynamic and accessible only in `ngAfterViewInit` / `ngAfterContentInit`."
* **🧠 Intuitive Real-World Analogy:**  
  * **`ViewChild` (Your Bedroom Wardrobe):** Furniture built directly into your house blueprint. You know exactly where it is.
  * **`ContentChild` (A Guest's Suitcase):** A suitcase brought into your living room by an outside visitor through the front door (`<ng-content>`). You didn't build it; it was passed in from outside.
  * **`{ static: true }` vs `{ static: false }`:**
    * `static: true`: The wardrobe is permanently bolted into the concrete wall. You can hang clothes immediately on moving day (`ngOnInit`).
    * `static: false`: The wardrobe is inside a folding room divider (`*ngIf`). You have to unfold the divider and finish painting the room (`ngAfterViewInit`) before you can open the wardrobe doors.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, ViewChild, ElementRef, OnInit, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-view-child-demo',
  standalone: true,
  template: `
    <input #staticInput placeholder="Always in DOM" />
    @if (showExtra()) { <input #dynamicInput placeholder="Conditional in DOM" /> }
  `
})
export class ViewChildDemoComponent implements OnInit, AfterViewInit {
  @ViewChild('staticInput', { static: true }) staticInput!: ElementRef<HTMLInputElement>;
  @ViewChild('dynamicInput', { static: false }) dynamicInput?: ElementRef<HTMLInputElement>;
  showExtra = signal(false);

  ngOnInit() {
    // ✅ Available in ngOnInit because static: true (not in conditional block)
    this.staticInput.nativeElement.focus();
  }
  ngAfterViewInit() {
    // ⚠️ dynamicInput is only resolved here if showExtra was true
    if (this.dynamicInput) this.dynamicInput.nativeElement.select();
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What happens if you mark `@ViewChild('myEl', { static: true })` on an element that is inside an `@if` or `*ngIf` block?"  
  * *Senior Answer:* "Angular will fail to resolve the element during the initial compilation pass, and `this.myEl` will be `undefined` inside `ngOnInit` and remain `undefined`! `static: true` tells the Angular compiler that the element is statically present in the template from frame zero without any structural conditions. If an element can be conditionally added or removed at runtime, you must keep `{ static: false }` (or use modern `viewChild()` signal queries) and access it safely inside `ngAfterViewInit`."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Query Type | What It Targets | Resolution Hook | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`@ViewChild(..., { static: true })`** | Element in component template NOT in `@if` | Accessible in `ngOnInit` | Use only for permanent static DOM nodes needed before view init. |
| **`@ViewChild(..., { static: false })`** | Element in template inside `@if` / `@for` | Accessible in `ngAfterViewInit` | Query dynamically; always check `if (this.childRef)` before invoking methods. |
| **`@ContentChild(...)`** | Projected node from `<ng-content>` | Accessible in `ngAfterContentInit` | Inspect projected headers/buttons inside `ngAfterContentInit`. |
| **Modern Signal Queries (v17.2+)** | `viewChild<ElementRef>('input')` | Returns reactive `Signal<T>` | Use `inputEl = viewChild<ElementRef>('staticInput');`. Automatically updates reactively! |

---

## Q14: Cross-Component Communication via Shared Service: Signals State Service vs BehaviorSubject
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Deloitte, EY, Morgan Stanley, Swiggy (Asked in 97% of state communication rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "For cross-component or sibling communication without parent-child nesting, senior Angular architectures use an `@Injectable({ providedIn: 'root' })` singleton state service. Historically, this was implemented using private `BehaviorSubject` instances exposed as read-only Observables (`.asObservable()`). In modern Angular (v16–v18+), we replace this boilerplate with private writable `signal()` primitives exposed via `.asReadonly()`, coupled with explicit mutation methods. This eliminates subscription memory leaks, removes `async` pipe boilerplate, and guarantees synchronous glitch-free reactivity across distant component subtrees."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `BehaviorSubject` (The Bank Branch Notice Board):** The branch manager posts a handwritten circular on a glass bulletin board. Every customer must walk into the branch, write their name on a subscription register, stand in line, and remember to cross their name off when they leave the city, or the bank continues sending paper notices forever (memory leak).
  * **Modern Signals Shared Service (Unified UPI Balance Widget):** All screens across Google Pay or PhonePe (Profile, Payment Screen, History Modal) read a single synchronized digital balance. When a transaction happens, the balance updates instantly everywhere without manual registration lines or teardown slips.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Injectable, signal, computed } from '@angular/core';

export interface CartItem { id: string; name: string; price: number; }

@Injectable({ providedIn: 'root' })
export class CartService {
  // 1. Private writable state (Encapsulation)
  private itemsSignal = signal<CartItem[]>([]);

  // 2. Public read-only exposure & derived calculations
  items = this.itemsSignal.asReadonly();
  totalPrice = computed(() => this.items().reduce((acc, i) => acc + i.price, 0));
  itemCount = computed(() => this.items().length);

  // 3. Controlled mutation methods
  addItem(item: CartItem) { this.itemsSignal.update(items => [...items, item]); }
  removeItem(id: string) { this.itemsSignal.update(items => items.filter(i => i.id !== id)); }
  clearCart() { this.itemsSignal.set([]); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why should you never expose a writable signal directly as `public items = signal<CartItem[]>([])` from a shared service?"  
  * *Senior Answer:* "Exposing a writable signal directly completely breaks encapsulation. Any consuming component across the application could arbitrarily call `this.cartService.items.set([])` or mutate values bypassing validation rules, audit logging, and business invariants. By keeping the writable signal `private` and exposing it publicly via `this.itemsSignal.asReadonly()`, you enforce **unidirectional data flow**: components can freely read and derive from state, but state mutations can only happen through explicitly audited service methods (`addItem`, `removeItem`)."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| State Architecture | What to Use | Pros & Cons | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Legacy Angular (v2–v15)** | `BehaviorSubject<T>` + `.asObservable()` | Requires `async` pipe in templates or manual subscription teardowns. | Wrap in private Subject; expose Observable; unsubscribe with `takeUntilDestroyed()`. |
| **Modern Angular (v16–v18+)** | `signal<T>()` + `.asReadonly()` | Zero subscription leaks; instant synchronous reads; pure `computed()` derivations. | Store in private `signal()`; expose `asReadonly()`; modify exclusively via methods. |
| **Multi-slice complex feature state** | NgRx SignalStore (`signalStore`) | Scalable, composable, supports custom features (`withEntities`, `withMethods`). | Use `@ngrx/signals` for enterprise shopping carts, multi-step wizards, or dashboards. |
'''
