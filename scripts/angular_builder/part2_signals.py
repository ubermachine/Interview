MODULE_2 = '''---

# MODULE 2: ANGULAR SIGNALS (v16–v18+) REACTIVE PRIMITIVES

## Q5: The Modern Signals Trio: signal(), computed(), and effect() Under the Hood
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Walmart (Asked in 100% of modern Angular interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular Signals operate on a fine-grained, push-pull reactive dependency graph (DAG). `signal()` is a writable reactive state container that pushes dirty notification flags down the graph upon mutation. `computed()` is a lazy, memoized, read-only derivation that pulls dependency values on demand and caches results until upstream dependencies become dirty. `effect()` is a scheduled side-effect runner executed on microtasks that reacts to signal mutations without returning values—ideal for DOM synchronization, logging, or third-party SDK integration."
* **🧠 Intuitive Real-World Analogy:**  
  * **`signal()` (Spreadsheet Cell A1 = 100):** You type a raw number into cell A1.
  * **`computed()` (Formula Cell B1 = `=A1 * 1.18`):** Cell B1 calculates the GST total. If you don't look at Cell B1, it never calculates. If A1 hasn't changed, B1 returns its cached value in O(1) time without re-evaluating.
  * **`effect()` (Automated SMS / UPI Webhook):** Whenever Cell B1 exceeds ₹50,000, an automated SMS alert is fired to the bank manager.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, signal, computed, effect } from '@angular/core';

@Component({
  selector: 'app-signals-trio',
  standalone: true,
  template: `<div>Item: ₹{{ price() }} | Total (with GST): ₹{{ totalWithGst() }}</div>`
})
export class SignalsTrioComponent {
  price = signal(1000); // 1. Writable State
  gstRate = signal(0.18);
  totalWithGst = computed(() => this.price() * (1 + this.gstRate())); // 2. Memoized Derivation

  constructor() {
    // 3. Side-Effect: Runs automatically whenever price or gstRate changes
    effect(() => console.log(`[Audit] Price updated in cart: ₹${this.totalWithGst()}`));
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Can you write to a signal inside an `effect()`? Why does Angular disallow it by default and require `{ allowSignalWrites: true }`?"  
  * *Senior Answer:* "By default, writing to signals inside an `effect()` throws an error (`NG0600: Writing to signals is not allowed in a computed or an effect`) because it violates unidirectional data flow and easily triggers infinite cyclical microtask loops (`Signal A updates -> Effect runs -> Signal A updates`). While `{ allowSignalWrites: true }` permits it, using it to compute derived state is a major architectural anti-pattern. If state derives from other signals, you must use `computed()`. `allowSignalWrites: true` should only be used in rare synchronization bridges (such as setting an error signal in response to an external WebSocket event)."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Primitive | Role / Behavior | Reactivity Type | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`signal(initVal)`** | Primary source of mutable state | Push (Invalidation) | Modify via `.set(val)` for replacement or `.update(fn)` for transformations. |
| **`computed(fn)`** | Derived calculations / filtering | Pull (Memoized) | Keep functions pure with zero side-effects. Never perform HTTP calls inside `computed()`. |
| **`effect(fn)`** | Side-effects outside Angular | Microtask Consumer | Place in `constructor` (Injection Context) or supply `Injector`. Use for logging, canvas, localStorage. |
| **Derived State Trap** | Replacing `effect` with `computed` | Architectural Rule | If you find yourself setting a signal inside an effect, delete the signal and replace it with `computed()`. |

---

## Q6: Array & Object State Mutations: Direct .push() Anti-Pattern vs .set() and .update()
* **Asked At:** Infosys, TCS, Wipro, Capgemini, Persistent, Nagarro, EPAM (High-frequency screening trap).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular Signals rely on strict referential identity comparison (`Object.is`) to notify downstream consumers and mark views dirty. Directly mutating an array using `.push()` or an object via `obj.name = 'X'` mutates the existing heap address in-place without producing a new memory reference. Consequently, the signal runtime detects zero identity change, dirty notifications are never dispatched, and UI templates fail to re-render. State must always be updated immutably using `.set()` or `.update()`."
* **🧠 Intuitive Real-World Analogy:**  
  * Imagine you give your bank passbook to a printer.
  * **Direct `.push()` Mutation:** You take a ballpoint pen and write an extra line yourself on the physical page while the bank teller is not looking. The bank's central database server has no idea any transaction occurred, so your online net-banking balance remains unchanged!
  * **`.update()` Senior Fix:** You deposit money at the teller counter, and the bank issues a newly validated, stamped statement (a brand-new immutable object reference).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, signal } from '@angular/core';

interface CartItem { id: number; name: string; price: number; }

@Component({ selector: 'app-cart-mutation', standalone: true, template: `...` })
export class CartMutationComponent {
  cartItems = signal<CartItem[]>([]);

  addItem(newItem: CartItem) {
    // ❌ ANTI-PATTERN: this.cartItems().push(newItem); -> Fails change detection!
    // ✅ SENIOR PATTERN: Produce a brand-new array reference using .update()
    this.cartItems.update(items => [...items, newItem]);
  }

  updateItemPrice(id: number, newPrice: number) {
    // ✅ SENIOR PATTERN: Immutable map transformation
    this.cartItems.update(items => items.map(item => item.id === id ? { ...item, price: newPrice } : item));
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Can you configure a custom equality function on a Signal to compare object properties instead of default `Object.is`?"  
  * *Senior Answer:* "Yes! `signal<T>(initialValue, { equal: customEqualityFn })` accepts an options object with an `equal` comparator. If you have complex object payloads and only want downstream computations or templates to update when a specific field (like `order.id` or `order.version`) changes, you can pass a custom comparator: `equal: (prev, curr) => prev.id === curr.id`. This prevents unnecessary dirty propagation when other non-UI fields mutate."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Operation | What to Use | Trade-offs | What Must Be Done (Exact Code) |
| :--- | :--- | :--- | :--- |
| **Replacing primitive or whole object** | `.set(newValue)` | Overwrites entire state value | `this.selectedId.set(101);` |
| **Adding item to array** | `.update(arr => [...arr, item])` | Allocates new array reference; triggers CD | `this.items.update(list => [...list, newItem]);` |
| **Updating item inside array** | `.update(arr => arr.map(...))` | Safe immutable transformation | `this.items.update(l => l.map(i => i.id === id ? {...i, done: true} : i));` |
| **Filtering / deleting item** | `.update(arr => arr.filter(...))` | Drops deleted items; creates clean new reference | `this.items.update(l => l.filter(i => i.id !== removeId));` |
| **Preventing dirty flags on same data** | `equal: (a, b) => isEqual(a, b)` | Custom equality check | Pass comparator in `signal(init, { equal: (a, b) => a.id === b.id })`. |

---

## Q7: untracked() Signal Reads & Breaking Circular Dependency Cascades
* **Asked At:** Morgan Stanley, Wells Fargo, Walmart Global Tech, EPAM, Persistent (Senior / Lead Architect Round).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`untracked()` executes a function and reads signal values without registering those signals as reactive dependencies in the current reactive context (such as an `effect()` or `computed()`). This is critical for preventing unnecessary effect re-executions, avoiding cascading reactive update loops, and performing one-off value sampling or non-reactive telemetry logging."
* **🧠 Intuitive Real-World Analogy:**  
  * Imagine a Swiggy food delivery driver tracking your GPS location:
    * **Tracked Signal (`location()`):** Whenever you move to a new apartment, the driver's map re-routes.
    * **`untracked(batteryLevel)`:** When the driver arrives at your door, the app logs your phone's battery level for diagnostics. If your battery drops from 80% to 79%, the delivery driver doesn't cancel and re-route the delivery! It samples the value once without subscribing to future battery fluctuations.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, signal, effect, untracked, inject } from '@angular/core';
import { AnalyticsService } from './analytics.service';

@Component({ selector: 'app-untracked-demo', standalone: true, template: `...` })
export class UntrackedDemoComponent {
  searchQuery = signal('');
  currentUser = signal({ id: 'USR-101', role: 'Trader' });
  private analytics = inject(AnalyticsService);

  constructor() {
    effect(() => {
      const query = this.searchQuery(); // ✅ Tracked dependency: Effect runs when query changes
      // ⚠️ Read user info without subscribing to user mutations:
      const user = untracked(() => this.currentUser()); 
      this.analytics.logSearch(query, user.id);
    });
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What happens if an `effect()` reads `signalA()` directly, and reads `signalB()` inside `untracked()`, but then `signalB` changes 1,000 times? Will the effect execute 1,000 times?"  
  * *Senior Answer:* "No! The effect will execute **zero times** in response to `signalB` mutations. Because `signalB` was evaluated inside `untracked()`, it was never registered in the producer-consumer edge list of the effect's `ReactiveNode`. The effect only re-executes when `signalA` changes. When `signalA` finally does change, the effect runs and will sample whatever the newest current value of `signalB` happens to be at that instant."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Scenario | What to Use | Why / Trade-offs | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Telemetry / Audit Logging** | `untracked(() => this.user())` | Avoids re-logging when non-primary metadata changes. | Wrap the non-triggering signal inside `untracked()`. |
| **Sampling current state on external event** | `untracked(() => this.formState())` | Reads current snapshot without triggering reactive loops. | Evaluate signal inside event handler or `untracked()` block. |
| **Breaking circular dependency loops** | `untracked()` in effect | Prevents Signal A -> Effect -> Signal B -> Effect cyclical crashes. | Audit effect dependencies and wrap secondary reads in `untracked()`. |

---

## Q8: Modern Signal Inputs & Two-Way Binding: input(), input.required(), and model()
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Deloitte, Nagarro (Modern Angular 17.1–18+ core question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular 17.1+ introduced Signal-based component inputs: `input<T>()` and `input.required<T>()` replace legacy `@Input()` decorators with read-only `InputSignal<T>` reactive nodes. They guarantee strict TypeScript typing, eliminate `ngOnChanges` boilerplate via pure `computed()` derivations, and support transform functions. For two-way data binding, `model<T>()` replaces the cumbersome `@Input() + @Output() Change` pattern with a writable `ModelSignal<T>` that automatically manages parent-child synchronization."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `@Input()` + `@Output()`:** A child customer gives a paper token to a restaurant cashier and waits for the cashier to shout their order number over a loudspeaker (`EventEmitter`).
  * **Modern `model()` Two-Way Binding:** A shared digital Google Docs document. When the parent types, the child sees it instantly; when the child edits a paragraph, the parent's view syncs automatically without manual event listeners!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, input, model, computed } from '@angular/core';

@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <h3>{{ fullName() }} (Role: {{ role() }})</h3>
    <input [value]="active()" (change)="active.set(!active())" type="checkbox" />
  `
})
export class UserCardComponent {
  firstName = input.required<string>(); // 1. Mandatory InputSignal
  lastName = input('');                 // 2. Optional InputSignal with default
  role = input('Viewer', { transform: (v: string) => v.toUpperCase() }); // 3. Input with transform
  active = model(false);                // 4. Two-Way ModelSignal ([(active)]="isActive")

  fullName = computed(() => `${this.firstName()} ${this.lastName()}`);
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Can a child component call `this.firstName.set('Amit')` on a signal created via `input()`? How does `model()` differ from `input()`?"  
  * *Senior Answer:* "No! `input()` returns an `InputSignal<T>`, which is strictly read-only; calling `.set()` or `.update()` on an `InputSignal` causes a TypeScript compilation error. If a child component must mutate the input and notify the parent via two-way binding, you must use `model<T>()`. `model()` returns a `ModelSignal<T>`, which is writable by the child via `this.active.set(...)` and automatically emits an implicit output event (`activeChange`) to update the parent's bound state."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Binding Requirement | Modern API (v17.1+) | Directionality | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Optional Parent -> Child Data** | `input<T>(defaultValue)` | One-Way (Read-only Child) | Declare `userId = input<string>('default')`. Read as `this.userId()`. |
| **Mandatory Parent -> Child Data** | `input.required<T>()` | One-Way (Compile-time Enforced) | Declare `token = input.required<string>()`. Parent must pass `[token]`. |
| **Sanitizing / Formatting input values** | `input(val, { transform })` | One-Way with Pipeline | Use `{ transform: booleanAttribute }` for clean boolean inputs (`<comp disabled />`). |
| **Two-Way Parent <-> Child Binding** | `model<T>()` | Two-Way (Read & Write) | Declare `isOpen = model(false);`. Parent binds via `[(isOpen)]="showModal"`. |
'''
