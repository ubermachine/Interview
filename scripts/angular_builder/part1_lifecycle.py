MODULE_1 = '''---

# MODULE 1: COMPONENT LIFECYCLE HOOKS & EXECUTION ORDER

## Q1: Component Lifecycle Sequence & Exact Execution Order
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 98% of Indian senior Angular interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular component lifecycle executes in an exact 8-phase sequence managed by the change detection engine: `constructor` initializes the TypeScript class instance and dependency injection; followed by `ngOnChanges` whenever bound `@Input` properties mutate by reference; `ngOnInit` executes exactly once after initial inputs are verified; `ngDoCheck` runs during every change detection cycle for custom dirty-checking; followed by the projected content hooks `ngAfterContentInit` and `ngAfterContentChecked`; then the view rendering hooks `ngAfterViewInit` and `ngAfterViewChecked`; and finally `ngOnDestroy` for resource disposal right before DOM removal."
* **🧠 Intuitive Real-World Analogy:**  
  * Think of constructing a pre-fabricated modular luxury villa in Bengaluru:
    * **`constructor`:** Laying the concrete foundation and connecting water/electricity lines (Dependency Injection). No interior walls exist yet.
    * **`ngOnChanges` / `ngOnInit`:** The architect inspects delivered blueprints (`@Input` data) and turns on the master electricity switch once.
    * **`ngAfterContentInit`:** The furniture bought by the client arrives and is placed inside (`<ng-content>` content projection).
    * **`ngAfterViewInit`:** The house decorators finish painting the living room walls and fitting smart TV displays (Component's own DOM `@ViewChild`).
    * **`ngOnDestroy`:** The occupant moves out, cancels the broadband connection, and hands the keys back to prevent unpaid utility bills (unsubscribing to prevent memory leaks).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, Input, OnInit, OnChanges, SimpleChanges, AfterViewInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-lifecycle-demo',
  standalone: true,
  template: `<p>User: {{ userName }}</p>`
})
export class LifecycleDemoComponent implements OnChanges, OnInit, AfterViewInit, OnDestroy {
  @Input() userName = '';

  constructor() { console.log('1. Constructor: Class instantiated, DI ready, Inputs NOT ready'); }
  ngOnChanges(c: SimpleChanges) { console.log('2. ngOnChanges: Input bound/changed', c['userName']?.currentValue); }
  ngOnInit() { console.log('3. ngOnInit: Initial inputs validated, ideal for HTTP calls'); }
  ngAfterViewInit() { console.log('4. ngAfterViewInit: Template DOM & ViewChild fully rendered'); }
  ngOnDestroy() { console.log('5. ngOnDestroy: Teardown subscriptions & intervals before DOM detached'); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Is the `constructor` a lifecycle hook? Why shouldn't you make HTTP calls or bind DOM events inside the constructor?"  
  * *Senior Answer:* "No, the `constructor` is a standard JavaScript/TypeScript ES6 class feature, not an Angular lifecycle hook. Inside the constructor, Angular has instantiated the class and injected dependencies, but `@Input` bindings are still `undefined` and the component's template DOM does not yet exist. Making HTTP calls or accessing inputs in the constructor breaks testability, makes unit testing difficult (requires mock inputs before instantiation), and violates Angular's design principle of separating object construction from business initialization. All initialization logic belongs strictly in `ngOnInit`."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Trigger / Requirement / Scenario | What to Use | Why / Trade-offs | What Must Be Done (Action Steps + Exact Code) |
| :--- | :--- | :--- | :--- |
| **Injecting services / setting default state** | `constructor` / `inject()` | Only DI is resolved; input bindings are not yet populated. | Keep body empty or use field-level `inject(ServiceName)` initializers. |
| **Reacting to `@Input()` value mutations** | `ngOnChanges(changes: SimpleChanges)` | Only fires when input reference identity (`!==`) changes. | Check `if (changes['prop'] && !changes['prop'].isFirstChange())` before running logic. |
| **Initial API calls / Subscriptions setup** | `ngOnInit` | Inputs are guaranteed ready; runs exactly once per component lifetime. | Trigger HTTP dispatch: `this.userService.loadProfile().pipe(takeUntilDestroyed(this.destroyRef)).subscribe()`. |
| **Direct DOM manipulation / 3rd-party JS widgets** | `ngAfterViewInit` | Template DOM and `@ViewChild` references are guaranteed fully rendered. | Initialize chart/modal: `new Chart(this.chartCanvas.nativeElement, config);`. Avoid synchronous property mutations. |
| **Cleaning up intervals, WebSockets, EventListeners** | `ngOnDestroy` or `DestroyRef` | Executed immediately before Angular detaches component from DOM. | Teardown: `clearInterval(this.timerId);` or use modern `DestroyRef.onDestroy(() => ...)`. |

---

## Q2: Parent-Child Lifecycle Hook Execution Order
* **Asked At:** Cognizant, Infosys, Capgemini, Accenture, Wells Fargo, Persistent (Asked in 95% of Senior Lead rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular resolves component lifecycles in two distinct phases: Initialization proceeds **Top-Down (Parent -> Child)**, whereas View Rendering completion proceeds **Bottom-Up (Child -> Parent)**. A parent component's `constructor`, `ngOnChanges`, and `ngOnInit` execute first to construct inputs for children; however, the parent's `ngAfterViewInit` cannot fire until all nested children have completed their own `ngAfterViewInit` rendering passes. On destruction, teardown is strictly **Top-Down (Parent -> Child)**."
* **🧠 Intuitive Real-World Analogy:**  
  * Think of manufacturing an electric vehicle at a Tata Motors plant:
    * **Initialization (Top-Down):** The master chassis frame (Parent) is laid out first, and specifications/parts (`@Input()`) are assigned to the battery pack assembly line (Child).
    * **View Assembly (Bottom-Up):** The dashboard display screen (Child View) must be fully built and wired before the master car inspection engineer (Parent `ngAfterViewInit`) can stamp the entire car as ready for delivery!
    * **Scrapping/Teardown (Top-Down):** When dismantling, the master chassis is decommissioned first, cutting power to all internal child sensors.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
// Sequence Demonstration Console Output:
// 1. [Parent] constructor
// 2. [Parent] ngOnChanges -> ngOnInit -> ngDoCheck
// 3. [Parent] ngAfterContentInit -> ngAfterContentChecked
// 4.   [Child] constructor
// 5.   [Child] ngOnChanges -> ngOnInit -> ngDoCheck
// 6.   [Child] ngAfterContentInit -> ngAfterViewInit -> ngAfterViewChecked (Child DOM Ready!)
// 7. [Parent] ngAfterViewInit -> ngAfterViewChecked (Parent DOM Ready!)
// --- DESTRUCTION ---
// 8. [Parent] ngOnDestroy
// 9.   [Child] ngOnDestroy
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why does a Child component's `ngAfterViewInit` execute *before* its Parent's `ngAfterViewInit`, but Parent's `ngOnInit` executes *before* Child's `ngOnInit`?"  
  * *Senior Answer:* "`ngOnInit` is data-driven: a child component cannot initialize its business logic or consume `@Input()` properties until the parent has initialized and bound those properties down the tree. Conversely, `ngAfterViewInit` is DOM-composition-driven: a parent component's view template *contains* the child's DOM. Because a container DOM node cannot be considered completely painted and verified until all of its interior subtree DOM nodes are painted, the child view must finish first (`Child.ngAfterViewInit`), bubbling up to allow `Parent.ngAfterViewInit` to finally resolve."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Phase | Execution Direction | Order of Execution | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Creation & Inputs** | **Top-Down** (Parent to Child) | `Parent.constructor` -> `Parent.ngOnInit` -> `Child.constructor` -> `Child.ngOnInit` | Pass data down from parent. Do not attempt to query child view methods in `Parent.ngOnInit`. |
| **Projected Content (`<ng-content>`)** | **Top-Down** | `Parent.ngAfterContentInit` -> `Child.ngAfterContentInit` | Inspect `<ng-content>` projections safely inside `ngAfterContentInit`. |
| **View Initialization (`@ViewChild`)** | **Bottom-Up** (Child to Parent) | `Child.ngAfterViewInit` -> `Parent.ngAfterViewInit` | Access child `@ViewChild` instances only inside `Parent.ngAfterViewInit`, never in `Parent.ngOnInit`. |
| **Destruction / Disposal** | **Top-Down** | `Parent.ngOnDestroy` -> `Child.ngOnDestroy` | Cancel parent subscriptions so pending async emissions do not push data down to dying children. |

---

## Q3: ngOnChanges vs ngOnInit vs ngDoCheck: Deep Difference & The ngDoCheck Trap
* **Asked At:** TCS, Wipro, HCL, Cognizant, Morgan Stanley, Walmart Global Tech (A favorite differentiation question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`ngOnInit` runs exactly once to handle one-time business initialization after inputs are bound. `ngOnChanges` executes before `ngOnInit` and repeatedly whenever an `@Input()` reference changes by identity (`!==`). `ngDoCheck` executes on every single change detection cycle—regardless of whether inputs changed—allowing custom dirty checking. Placing heavy algorithms, deep object comparisons, or HTTP calls inside `ngDoCheck` is a severe anti-pattern that destroys frame rates and freezes the browser UI."
* **🧠 Intuitive Real-World Analogy:**  
  * **`ngOnInit` (Passport Office Biometrics):** You take your fingerprint and iris scan once when your application opens.
  * **`ngOnChanges` (Courier Delivery Notification):** Your phone buzzes only when a new delivery box actually arrives at your doorstep with a new tracking ID.
  * **`ngDoCheck` (Over-Anxious Security Guard):** A security guard who taps you on the shoulder every 2 seconds asking "Did you buy anything yet? How about now? How about now?" even if you just blinked your eyes!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, Input, OnChanges, OnInit, DoCheck, SimpleChanges } from '@angular/core';

@Component({ selector: 'app-check-trap', standalone: true, template: `<div>{{ user.name }}</div>` })
export class CheckTrapComponent implements OnChanges, OnInit, DoCheck {
  @Input() user!: { id: string; name: string };
  private prevName = '';

  ngOnChanges(c: SimpleChanges) { /* Only fires if 'user' object reference changes! */ }
  ngOnInit() { /* Fires ONCE: Fetch user permissions or setup timers */ }
  ngDoCheck() {
    // ⚠️ FIRES ON EVERY CLICK, TIMER, PROMISE! Keep ultra-lightweight:
    if (this.user?.name !== this.prevName) {
      this.prevName = this.user.name;
      console.log('Custom mutated property detected manually!');
    }
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "If a parent component passes an object `user = { name: 'Amit' }` to a child, and the parent mutates it in-place via `this.user.name = 'Rahul'`, does `ngOnChanges` fire in the child? How do you fix this?"  
  * *Senior Answer:* "No! `ngOnChanges` strictly checks object references using `Object.is()` / `===`. Because the heap address of `user` did not change, `ngOnChanges` is completely blind to in-place property mutations. The senior solution is **never mutate objects in-place**—always produce a new immutable reference in the parent: `this.user = { ...this.user, name: 'Rahul' }`, or migrate to modern Angular Signals (`user = signal({ name: 'Amit' })`) where updates propagate fine-grained reactivity automatically."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Scenario | What to Use | Why / Trade-offs | What Must Be Done (Action Steps) |
| :--- | :--- | :--- | :--- |
| **One-time data fetch on component load** | `ngOnInit` | Guarantees inputs are set; executes exactly once. | Make HTTP calls or dispatch NgRx actions here. |
| **Detecting changes to `@Input()` references** | `ngOnChanges` | Angular automatically compares references and supplies `SimpleChanges`. | Use `changes['prop'].currentValue` and check `!changes['prop'].firstChange`. |
| **Detecting in-place mutations of 3rd party objects** | `ngDoCheck` with `KeyValueDiffers` | Extremely expensive; runs on every microtask tick. | Inject `KeyValueDiffers`, compare diff shallowly, and never call HTTP services inside. |
| **Modern Angular Reactivity (v16+)** | `computed()` or `effect()` | Eliminates `ngOnChanges` and `ngDoCheck` completely. | Use `user = input.required<User>()` and derive state via `computed(() => this.user().name)`. |

---

## Q4: ngAfterViewInit vs ngAfterContentInit & ExpressionChangedAfterItHasBeenCheckedError
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Deloitte, EY, Nagarro, EPAM (Asked in 99% of interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`ngAfterContentInit` executes once projected content (`<ng-content>`) is initialized into the component's slot. `ngAfterViewInit` executes once the component's own template and child views (`@ViewChild`) are completely rendered. If you synchronously modify a template-bound property inside `ngAfterViewInit`, Angular throws the dreaded `ExpressionChangedAfterItHasBeenCheckedError` during development mode because Angular's unidirectional data flow check detects that a view property mutated after the rendering pass had already verified it."
* **🧠 Intuitive Real-World Analogy:**  
  * **Projected Content (`ngAfterContentInit`):** A tenant brings their own refrigerator into an unfurnished apartment. The landlord hooks it up before painting the apartment walls.
  * **View Init (`ngAfterViewInit`):** The landlord finishes installing the glass chandelier in the ceiling.
  * **The Error (Expression Changed Trap):** Imagine a bank cashier counts your ₹10,000 cash deposit and writes ₹10,000 in the verified ledger. While the supervisor is stamping the ledger two seconds later, you sneak in an extra ₹500 note. The supervisor screams: *"Fraud! The verified total changed after I just confirmed it!"*
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, AfterViewInit, signal, ChangeDetectorRef, inject } from '@angular/core';

@Component({
  selector: 'app-expression-fix',
  standalone: true,
  template: `<p>Status: {{ status }}</p>`
})
export class ExpressionFixComponent implements AfterViewInit {
  status = 'Loading...';
  private cdr = inject(ChangeDetectorRef);

  ngAfterViewInit() {
    // ❌ BAD: this.status = 'Ready'; -> Throws ExpressionChangedAfterItHasBeenCheckedError!
    // ✅ SENIOR FIX 1: Defer mutation to the next microtask queue
    queueMicrotask(() => { this.status = 'Ready (Safe Microtask)'; });
    // ✅ SENIOR FIX 2: Or explicitly force CD tick: this.cdr.detectChanges();
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why does `ExpressionChangedAfterItHasBeenCheckedError` only occur in development mode, and why does Angular enforce this rule?"  
  * *Senior Answer:* "In development mode, Angular runs an extra verification change detection cycle (`checkNoChanges()`) immediately after the main change detection pass to guarantee that data flows strictly unidirectionally from parent to child. In production mode, this verification pass is disabled for performance. Angular enforces this strictly to prevent cyclical change cascades, infinite rendering loops, and unpredictable UI glitches where a child component unpredictably mutates parent state during rendering."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Problem / Requirement | What to Use | Why / Trade-offs | What Must Be Done (Exact Code) |
| :--- | :--- | :--- | :--- |
| **DOM query for projected `<ng-content>`** | `ngAfterContentInit` & `@ContentChild` | Projected content is stable before the component's own view finishes rendering. | Query content safe from expression errors. |
| **DOM query for template elements (`<canvas>`, child components)** | `ngAfterViewInit` & `@ViewChild` | Element references are guaranteed resolved in the real DOM. | Use `@ViewChild('chart') chart!: ElementRef;`. Access nativeElement here. |
| **Updating bound state from `ngAfterViewInit`** | `queueMicrotask()` or `Promise.resolve()` | Moves state mutation into the next event loop turn, after current CD finishes. | `queueMicrotask(() => this.isLoading.set(false));` |
| **Immediate synchronous UI sync** | `ChangeDetectorRef.detectChanges()` | Forces immediate synchronous re-check of the view. | Call `this.cdr.detectChanges();` immediately after state mutation. |
| **Modern Architecture Solution** | Angular Signals (`signal()`) | Fine-grained push-pull DAG updates the specific DOM text node directly. | Convert property to `status = signal('Loading')` and update via `status.set('Ready')`. |
'''
