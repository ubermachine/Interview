MODULE_14 = '''---

# MODULE 14: STATE MANAGEMENT: LOCAL VS NGRX SIGNALSTORE

## Q36: State Management Decision Matrix: Local Signals vs Service Signals vs NgRx SignalStore vs NgRx Redux Store
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Swiggy (The high-stakes architectural strategy question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "State management in enterprise Angular follows a 4-tier architectural spectrum based on scope and complexity: **Tier 1 (Local Component Signals)** handles ephemeral UI state (modals, toggles); **Tier 2 (Service with Signals)** handles feature-scoped or shared cross-component state with zero external dependencies; **Tier 3 (NgRx SignalStore)** provides modular, functional, tree-shakeable state with out-of-the-box computed signals, entity adapters, and asynchronous effects without Redux ceremony; and **Tier 4 (Classic NgRx Global Redux Store)** is reserved strictly for massive multi-team enterprise apps that require strict immutable action log auditing and time-travel debugging."
* **🧠 Intuitive Real-World Analogy:**  
  * **Tier 1 (Local Signal):** Sticky note on your personal desk monitor reminding you to buy milk.
  * **Tier 2 (Service with Signals):** Shared white-board in your team's conference room.
  * **Tier 3 (NgRx SignalStore):** An organized digital Kanban board (Trello / Jira) with automated swimlanes, custom filters, and instant notifications.
  * **Tier 4 (Classic NgRx Redux):** An official government registry office requiring you to fill out 4 notarized action slips, stamp them with reducers, hand them to an effects courier, and wait for the state ledger to update.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
// Tier 2 Example: Lightweight, dependency-free Signal Service for 80% of applications
import { Injectable, signal, computed } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class FeatureStateService {
  private countSignal = signal(0);
  count = this.countSignal.asReadonly();
  doubleCount = computed(() => this.count() * 2);

  increment() { this.countSignal.update(c => c + 1); }
  reset() { this.countSignal.set(0); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:** "Why are enterprise teams increasingly abandoning classic NgRx (@ngrx/store with Actions, Reducers, Effects, Selectors) in favor of NgRx SignalStore?"  
  * *Senior Answer:** "Classic NgRx introduces massive **indirection fatigue and boilerplate overhead**: a simple counter or CRUD slice requires creating 4 to 5 separate files (`actions.ts`, `reducer.ts`, `effects.ts`, `selectors.ts`, `state.ts`), producing over 200 lines of ceremony for a simple API call. Navigating code requires jumping through 5 files to trace a single event. NgRx SignalStore (`@ngrx/signals`) unifies state, derived computeds, and async methods into a single, highly readable, composable functional API that compiles to 70% less code, is 100% tree-shakeable, and natively aligns with Angular's push-pull Signal architecture."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Complexity Tier | State Solution | Pros & Cons | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Tier 1: Ephemeral UI** | Local Component `signal()` | Instant, zero boilerplate, destroyed with component. | Use `isOpen = signal(false);` inside component. |
| **Tier 2: Medium Shared State** | `@Injectable()` Service with Signals | No 3rd-party libs, clean encapsulation, readable. | Use private `signal()`, public `asReadonly()`, service methods. |
| **Tier 3: Complex Feature State** | NgRx SignalStore (`@ngrx/signals`) | Functional, extensible (`withEntities`), signals native. | Run `npm i @ngrx/signals`; define `signalStore(withState(...))`. |
| **Tier 4: Enterprise Audit Monolith** | Classic NgRx Global Redux Store | Extreme boilerplate; strict action log traceability. | Use only if mandatory compliance requires centralized action history logs. |

---

## Q37: Modern NgRx SignalStore Architecture: signalStore(), withState(), withComputed(), and withMethods()
* **Asked At:** Wells Fargo, Morgan Stanley, Walmart Global Tech, Swiggy, Persistent, EPAM (The cutting-edge NgRx interview topic).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "NgRx SignalStore is a functional, composable state management library built on Angular Signals. A store is declared via the **`signalStore()`** builder function and customized using modular extension features: **`withState()`** declares reactive state slices; **`withComputed()`** adds lazy, memoized derived signals that have access to all state slices; and **`withMethods()`** adds synchronous or asynchronous updater methods utilizing **`patchState()`** for safe immutable state updates. SignalStores can be provided globally (`providedIn: 'root'`) or locally at the component level for automatic lifecycle destruction."
* **🧠 Intuitive Real-World Analogy:**  
  * Think of assembling a custom gaming PC at a computer shop:
    * **`signalStore()`:** The motherboard chassis.
    * **`withState()`:** Plugging in the RAM and SSD storage drives (holding raw data).
    * **`withComputed()`:** Attaching the GPU display card (instantly computing graphics from memory).
    * **`withMethods()`:** Connecting the keyboard and game controller (the only authorized inputs that can send signals to modify storage).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { signalStore, withState, withComputed, withMethods, patchState } from '@ngrx/signals';
import { computed, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { rxMethod } from '@ngrx/signals/rxjs-interop';
import { pipe, switchMap, tap } from 'rxjs';

interface TodoState { items: string[]; loading: boolean; }
const initialState: TodoState = { items: [], loading: false };

export const TodoStore = signalStore(
  { providedIn: 'root' },
  withState(initialState),
  withComputed(({ items }) => ({
    count: computed(() => items().length),
    isEmpty: computed(() => items().length === 0)
  })),
  withMethods((store, http = inject(HttpClient)) => ({
    loadTodos: rxMethod<void>(pipe(
      tap(() => patchState(store, { loading: true })),
      switchMap(() => http.get<string[]>('/api/todos')),
      tap(items => patchState(store, { items, loading: false }))
    ))
  }))
);
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "How does `patchState` enforce immutability, and what happens if you mutate nested state objects directly inside a method?"  
  * *Senior Answer:* "`patchState(store, partialStateOrUpdaterFn)` takes the current state slice and shallowly merges the updated fields into a brand-new immutable state object, notifying only the specific signals that changed. If you bypass `patchState` and mutate an array or nested object directly (e.g. `store.items().push('new')`), you violate referential identity; downstream computed signals and templates will not receive invalidation notifications. Furthermore, `patchState` ensures atomic state transitions, preventing intermediate UI rendering glitches."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Store Building Block | Extension Function | Purpose | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **State Declaration** | `withState(initialState)` | Defines reactive state properties | Pass typed initial state object. |
| **Derived Computations** | `withComputed(({ prop }) => ...)` | Adds memoized derived signals | Return dictionary of `computed()` signals. |
| **Synchronous Mutations** | `withMethods(store => ({ ... }))` | Modifies state via `patchState` | Use `patchState(store, { key: value })`. |
| **Async RxJS Pipelines** | `rxMethod<T>(pipe(...))` | Integrates HTTP calls with cancellation | Import `rxMethod` from `@ngrx/signals/rxjs-interop`. |
| **Entity Collection Management** | `withEntities<T>()` | Built-in CRUD for ID-indexed lists | Adds `entities()`, `entityMap()`, and `ids()` automatically. |
'''
