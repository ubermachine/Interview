#!/usr/bin/env python3
"""
Deep Dive Part 4: Module 17 (Q44 to Q51 converted from Case Studies)
plus 4 clean Architecture References.
"""
from generate_deep_dive import format_q

def get_part4_questions():
    qs = []

    # Q44: Standalone Migration (Case Study 1)
    qs.append(format_q(
        44,
        "How do you migrate enterprise Angular applications from NgModules to Standalone Components and Control Flow?",
        ["TCS", "Infosys", "Cognizant", "Capgemini"],
        "Migrate by setting standalone true, replacing SharedModule with explicit imports, and converting structural directives to compiler control flow.",
        "Migrating legacy Angular applications to modern architecture requires a systematic approach. First, mark components as standalone and declare explicit dependencies inside their `imports` array. This eliminates monolithic SharedModule dumping grounds and unlocks aggressive tree-shaking in esbuild. Next, convert structural directives (`*ngIf`, `*ngFor`) to compiler-native control flow (`@if`, `@for`). In one of my projects, migrating to standalone components reduced initial bundle size by sixty-five percent. For the complete runnable implementation, see [01-standalone-migration.ts](file:///home/ubermensch/Desktop/interview/examples/angular/01-standalone-migration.ts).",
        [
            ("standalone: true", "decouples components from NgModule compilation containers", True),
            ("Dead-code elimination", "bundler strips unreferenced exports from production bundles", True),
            ("Compiler control flow", "native template branching instructions like ɵɵconditional", True),
            ("SharedModule elimination", "removing bloated central module dumping grounds", False),
            ("provideRouter", "functional router configuration replacing RouterModule", False)
        ],
        "Demolishing a massive shared warehouse where everyone stored everything, replacing it with private modular storage units.",
        """// ❌ Bad: monolithic SharedModule dumping ground
@NgModule({ imports: [CommonModule, MatTableModule, MatButtonModule] })
export class SharedModule {}

// ✅ Good: standalone component with laser-focused imports
@Component({
  standalone: true,
  imports: [CurrencyPipe],
  template: `@if (loading()) { <p>Loading...</p> }`
})
export class ModernPortfolioComponent {}""",
        "How does the automated Angular CLI migration command help migrate to standalone components?",
        "Running `ng generate @angular/core:standalone` automates converting component declarations, removing NgModules, and switching to `bootstrapApplication()`.",
        """| Migration Step | Legacy Pattern | Modern Senior Pattern |
| :--- | :--- | :--- |
| **Component Model** | `NgModule.declarations` | `standalone: true` |
| **Imports** | Monolithic `SharedModule` | Explicit `imports: [...]` |
| **Template Loops** | `*ngFor` with `trackBy` | `@for (...; track id)` |
| **Bootstrap** | `platformBrowserDynamic` | `bootstrapApplication()` |""",
        "Standalone components allow the compiler to build a Directed Acyclic Graph of dependencies, enabling tree-shaking of unreferenced directives."
    ))

    # Q45: Signal Cart & Live Pricing (Case Study 2)
    qs.append(format_q(
        45,
        "How do you build a high-throughput e-commerce cart and live pricing engine using Angular Signals?",
        ["Walmart", "Flipkart", "Amazon", "Target"],
        "Model cart items as writable signals, derive pricing via computed signals, and update state using immutable transformations.",
        "High-throughput checkout engines require fine-grained reactivity to avoid full-tree change detection passes. Model cart items as a writable `signal<CartItem[]>`. Derive subtotals, tax, and shipping using `computed()` signals. When users modify item quantities, call `.update()` with the spread operator to produce fresh references. In one of my projects, this push-pull architecture handled rapid quantity updates without UI frame drops. For the complete runnable implementation, see [02-signal-cart-pricing.ts](file:///home/ubermensch/Desktop/interview/examples/angular/02-signal-cart-pricing.ts).",
        [
            ("Push-pull graph", "reactive graph architecture powering signals", True),
            ("computed() derivation", "lazily evaluated memoized calculation signal", True),
            ("Immutable update", "producing new references without in-place mutation", True),
            ("Microtask batching", "coalescing multiple rapid signal changes into one repaint", False),
            ("Zoneless change detection", "change detection without Zone.js overhead", False)
        ],
        "An Excel spreadsheet where changing item quantity automatically recalculates taxes and totals through pre-wired formula cells.",
        """// ❌ Bad: mutating object in place skips signal notifications
this.items()[0].quantity++; // UI fails to update!

// ✅ Good: immutable update producing new object references
this.items.update(list => list.map(item =>
  item.id === id ? { ...item, quantity: item.quantity + 1 } : item
));""",
        "Why is computed() superior to calling calculation methods directly in templates?",
        "Template methods execute during every change detection cycle, whereas `computed()` caches results, recomputing only when dependencies change.",
        """| Metric | Template Method | computed() Signal |
| :--- | :--- | :--- |
| **Execution Count** | Every change pass | Only on dependency change |
| **Memoization** | None | Automatic cached result |
| **Zoneless Support** | Requires manual trigger | Native automatic update |""",
        "The signals graph evaluates dependencies via topological sort, ensuring that grandTotal reads pristine, updated subtotal and tax values."
    ))

    # Q46: Typeahead Catalog Search (Case Study 3)
    qs.append(format_q(
        46,
        "How do you implement a typeahead search catalog preventing race conditions and stream termination?",
        ["Google", "Microsoft", "Swiggy", "Zomato"],
        "Use switchMap to cancel stale in-flight requests, debounce user keystrokes, and isolate error handling inside the inner stream.",
        "A reliable typeahead search must handle rapid keystrokes, out-of-order network responses, and transient API failures. Apply `debounceTime(300)` to throttle typing, followed by `distinctUntilChanged()` to ignore duplicate inputs. Use `switchMap` to cancel pending in-flight requests when new queries arrive. Place `catchError` inside the inner switchMap observable to keep the outer stream alive on errors. In one of my projects, this architecture prevented search race conditions. For the complete runnable implementation, see [03-typeahead-search.ts](file:///home/ubermensch/Desktop/interview/examples/angular/03-typeahead-search.ts).",
        [
            ("switchMap", "cancels stale in-flight requests on new input", True),
            ("debounceTime", "delays emission until typing pauses for duration", True),
            ("Inner catchError", "recovers from network failures without stream termination", True),
            ("distinctUntilChanged", "ignores consecutive identical search terms", False),
            ("takeUntilDestroyed", "cleans subscription on component destruction", False)
        ],
        "A restaurant order counter that cancels previous kitchen tickets when a customer changes their order before cooking begins.",
        """// ❌ Bad: outer catchError permanently breaks input listener
search$.pipe(
  switchMap(q => this.http.get(`/search?q=${q}`)),
  catchError(() => of([])) // outer stream dies!
).subscribe();

// ✅ Good: inner catchError keeps search listener alive
search$.pipe(
  switchMap(q => this.http.get(`/search?q=${q}`).pipe(catchError(() => of([]))))
).subscribe();""",
        "What happens if network latency causes response B to arrive before response A in a mergeMap search?",
        "mergeMap does not cancel pending requests; response A can overwrite newer response B, displaying stale search results to users.",
        """| Operator | In-Flight Handling | Concurrency Result |
| :--- | :--- | :--- |
| `mergeMap` | Keeps all active | Race condition bug |
| `switchMap` | Aborts previous | Pristine latest results |""",
        "switchMap calls unsubscribe() on the active inner subscriber before subscribing to the new observable, triggering XMLHttpRequest abort()."
    ))

    # Q47: High-Frequency Modal Dialogs (Case Study 4)
    qs.append(format_q(
        47,
        "How do you prevent detached DOM tree memory leaks when displaying high-frequency data in dialogs?",
        ["Morgan Stanley", "JPMorgan", "Wells Fargo", "Barclays"],
        "Prevent detached DOM leaks by tying subscriptions to injection context with takeUntilDestroyed or bridging streams to signals.",
        "Dynamic modals displaying high-frequency market data often cause detached DOM tree memory leaks. When components subscribe to singleton streaming services without uninsubscribing, closures retain component references and their entire DOM subtree in memory. Modern Angular prevents this by using `takeUntilDestroyed()` within the constructor or converting streams using `toSignal()`. In one of my projects, adding automatic teardown eliminated three gigabytes of retained heap allocations. For the complete runnable implementation, see [04-leak-proof-modal.ts](file:///home/ubermensch/Desktop/interview/examples/angular/04-leak-proof-modal.ts).",
        [
            ("takeUntilDestroyed()", "unsubscribes automatically when component destroys", True),
            ("toSignal()", "bridges observable streams to signals with cleanup", True),
            ("Detached DOM tree", "DOM nodes retained in memory by active closures", True),
            ("DestroyRef", "functional teardown hook replacing ngOnDestroy", False),
            ("Heap snapshot", "diagnostic snapshot of memory objects in DevTools", False)
        ],
        "Moving out of an apartment and remembering to cancel the high-speed broadband contract so bills do not pile up.",
        """// ❌ Bad: singleton stream retains destroyed component closure
ngOnInit(): void {
  this.ratesService.stream$.subscribe(r => this.rate = r);
}

// ✅ Good: automatic teardown tied to injection context
readonly liveRate = toSignal(this.ratesService.stream$);""",
        "How can you verify that a modal component was successfully garbage collected?",
        "Take a heap snapshot in Chrome DevTools, open and close the modal, trigger manual garbage collection, and assert the component count is zero.",
        """| Teardown Method | Context Required | Risk of Leak |
| :--- | :--- | :--- |
| `toSignal()` | Injection context | Zero (built-in teardown) |
| `takeUntilDestroyed()` | Injection context | Zero (built-in teardown) |
| Manual `ngOnDestroy` | Class hook | High (forgotten cleanup) |""",
        "When an outer observable retains an inner subscriber callback referencing this, the V8 engine marks the entire component closure reachable."
    ))

    # Q48: 60 FPS Real-Time Canvas Rendering (Case Study 5)
    qs.append(format_q(
        48,
        "How do you achieve 60 FPS performance for high-frequency real-time updates without triggering change detection?",
        ["TCS", "Accenture", "Cognizant", "Persistent"],
        "Achieve 60 FPS by executing high-frequency event listeners outside Angular using NgZone.runOutsideAngular and applying direct DOM transforms.",
        "High-frequency events like canvas drawing, mouse moves, and WebSockets can trigger hundreds of change detection cycles per second, causing UI stutter. To achieve smooth 60 FPS rendering, run event listeners outside Angular using `NgZone.runOutsideAngular()`. Mutate canvas contexts and element transforms directly via standard DOM APIs without invoking change detection passes. When discrete user interactions require state updates, re-enter the zone using `NgZone.run()`. In one of my projects, this technique restored smooth 60 FPS animations. For the complete runnable implementation, see [05-high-fps-ngzone.ts](file:///home/ubermensch/Desktop/interview/examples/angular/05-high-fps-ngzone.ts).",
        [
            ("NgZone.runOutsideAngular()", "runs code without triggering change detection", True),
            ("60 FPS rendering", "smooth animation frame rate requiring sixteen millisecond frames", True),
            ("OnPush change detection", "prunes component subtrees from change passes", True),
            ("Direct DOM transform", "updating styles without Angular change detection overhead", False),
            ("AbortController", "cancels event listeners cleanly on component destruction", False)
        ],
        "A train conductor letting passengers move freely inside carriages without stopping the train at every seat movement.",
        """// ❌ Bad: mousemove inside zone triggers frequent detection
canvas.addEventListener('mousemove', () => this.draw());

// ✅ Good: runOutsideAngular bypasses change detection completely
this.ngZone.runOutsideAngular(() => {
  canvas.addEventListener('mousemove', (e) => this.drawDirect(e));
});""",
        "How do you clean up DOM event listeners added via runOutsideAngular?",
        "Use an `AbortController` signal option in `addEventListener`, calling `abortController.abort()` inside `ngOnDestroy` or `DestroyRef`.",
        """| Strategy | Execution Scope | Change Detection Fired | Frame Rate |
| :--- | :--- | :--- | :--- |
| **Standard Binding** | Inside Angular Zone | Every mousemove event | Drops to < 20 FPS |
| **NgZone Escaping** | Outside Angular Zone | Zero ticks fired | Solid 60 FPS |""",
        "Zone.js monkey-patches addEventListener. runOutsideAngular switches the active zone to root zone, bypassing tick() invocation."
    ))

    # Q49: Silent JWT Token Refresh & Atomic Route Guard (Case Study 6)
    qs.append(format_q(
        49,
        "How do you implement silent JWT token refresh and atomic route guarding in modern Angular?",
        ["Barclays", "Morgan Stanley", "Deloitte", "Capgemini"],
        "Implement a functional interceptor with a concurrency lock and queue, paired with functional guards returning atomic UrlTrees.",
        "Enterprise authentication requires seamless token renewal and secure routing. A functional HTTP interceptor [HttpInterceptorFn] catches 401 Unauthorized errors, using a concurrency lock and BehaviorSubject queue during token renewal. Once refreshed, queued requests resume execution with updated authorization headers. Route protection uses a functional guard returning an atomic `UrlTree` for unauthorized access. In one of my projects, this pattern prevented multi-request token refresh storms. For the complete runnable implementation, see [06-jwt-refresh-interceptor.ts](file:///home/ubermensch/Desktop/interview/examples/angular/06-jwt-refresh-interceptor.ts).",
        [
            ("HttpInterceptorFn", "functional middleware intercepting HTTP traffic", True),
            ("Silent refresh", "renewing expired access tokens without user interruption", True),
            ("Concurrency lock", "flag preventing duplicate concurrent refresh requests", True),
            ("UrlTree", "atomic router redirect target representation", False),
            ("BehaviorSubject queue", "buffers waiting requests until token refresh completes", False)
        ],
        "A group entering a secured room: when the keycard expires, one member gets a new key while others wait outside.",
        """// ❌ Bad: duplicate concurrent refresh calls on token expiry
catchError(err => this.authService.refreshToken());

// ✅ Good: concurrency lock with BehaviorSubject queue
if (!isRefreshing) {
  isRefreshing = true;
  return auth.refreshToken().pipe(
    switchMap(token => { isRefreshing = false; return next(clone(req, token)); })
  );
}""",
        "Why is returning a UrlTree preferred over router.navigate() in modern route guards?",
        "Returning a UrlTree executes an atomic redirect within the current navigation cycle, avoiding competing navigations and broken history states.",
        """| Component | Responsibility | Modern API |
| :--- | :--- | :--- |
| **Interceptor** | Token injection & 401 refresh | `HttpInterceptorFn` |
| **Route Guard** | Security validation & redirect | `CanActivateFn` with `UrlTree` |""",
        "Waiting requests subscribe to a BehaviorSubject with filter(token => token !== null) and take(1), resuming execution when the new token emits."
    ))

    # Q50: Enterprise NgRx SignalStore Architecture (Case Study 7)
    qs.append(format_q(
        50,
        "How do you design an enterprise state management architecture using NgRx SignalStore and custom features?",
        ["TCS", "Accenture", "Cognizant", "Infosys"],
        "Design SignalStore using withState for state slices, withComputed for derivations, and withMethods with rxMethod for side effects.",
        "NgRx SignalStore provides a lightweight, composable alternative to traditional Redux. We define state using `withState(initialState)`, where each state slice is a signal and `computed` caches results until inputs change. Derived calculations are declared using `withComputed()` for memoization. Business methods and asynchronous side effects are encapsulated inside `withMethods()` using `patchState()` and `rxMethod`. In one of my projects, SignalStore reduced state boilerplate by sixty percent. For the complete runnable implementation, see [07-ngrx-signal-store.ts](file:///home/ubermensch/Desktop/interview/examples/angular/07-ngrx-signal-store.ts).",
        [
            ("signalStore()", "factory function creating a composable store", True),
            ("withState()", "defines reactive state slices as signals", True),
            ("withComputed()", "adds memoized computed signals to the store", True),
            ("withMethods()", "defines state mutation and async methods", False),
            ("patchState()", "atomic state update utility function", False)
        ],
        "A modular hi-fi audio system: plug in amplifier modules for power, tuner modules for stations, and speakers for output.",
        """// ❌ Bad: classic Redux actions, reducers, and selectors boilerplate
export const loadItems = createAction('[Cart] Load');
export const cartReducer = createReducer(...);

// ✅ Good: concise composable NgRx SignalStore
export const CartStore = signalStore(
  withState({ items: [], loading: false }),
  withComputed(({ items }) => ({ total: computed(() => items().length) }))
);""",
        "How do you implement reusable custom store features in NgRx SignalStore?",
        "Create custom functions using `signalStoreFeature` to package reusable behaviors like local storage sync, logging, or entity management.",
        """| Feature | Primary Function | Output Property |
| :--- | :--- | :--- |
| `withState` | Declares reactive state | Read-only Signals |
| `withComputed` | Derives memoized state | Computed Signals |
| `withMethods` | Updates state & side effects | Store methods |
| `withHooks` | Lifecycle initialization | onInit, onDestroy |""",
        "SignalStore builds an object whose properties map directly to signals; patchState evaluates state updaters and sets signals cleanly."
    ))

    # Q51: Real-Time Polling Dashboard Widget (Case Study 8)
    qs.append(format_q(
        51,
        "How do you build a real-time polling dashboard widget with clean teardown, error recovery, and backoff?",
        ["Capgemini", "Infosys", "Deloitte", "Wipro"],
        "Combine timer and manual refresh triggers using switchMap, isolate error boundaries, and manage teardown via takeUntilDestroyed.",
        "A resilient polling widget must coordinate periodic updates, handle manual refresh requests, and survive network errors. Combine `timer(0, interval)` and a manual refresh `Subject` using `merge()`, piping into `switchMap` to cancel pending in-flight requests. Critically, isolate error handling using `catchError` inside the inner switchMap observable to prevent stream termination. Discard subscriptions automatically using `takeUntilDestroyed()`. In one of my projects, this architecture ensured continuous telemetry display. For the complete runnable implementation, see [08-polling-dashboard.ts](file:///home/ubermensch/Desktop/interview/examples/angular/08-polling-dashboard.ts).",
        [
            ("timer()", "observable emitting on initial delay and periodic intervals", True),
            ("switchMap", "cancels stale in-flight requests on new polling ticks", True),
            ("takeUntilDestroyed()", "unsubscribes automatically when component destroys", True),
            ("Inner catchError", "recovers from network failures without stream termination", False),
            ("merge()", "combines periodic timer with manual refresh triggers", False)
        ],
        "A security guard patrolling rounds every ten minutes, who also checks doors immediately when a sensor alarm chimes.",
        """// ❌ Bad: setInterval with unmanaged subscribe leaks on destroy
ngOnInit(): void {
  setInterval(() => this.http.get('/metrics').subscribe(), 5000);
}

// ✅ Good: resilient pipeline with automatic teardown
merge(timer(0, 10000), this.manualRefresh$).pipe(
  switchMap(() => this.http.get('/metrics').pipe(catchError(() => of(null)))),
  takeUntilDestroyed()
).subscribe(data => this.stats.set(data));""",
        "What happens if an API call takes longer than the polling interval when using mergeMap?",
        "mergeMap will trigger overlapping concurrent requests, piling up network load and causing out-of-order state overwrites.",
        """| Step | Operator | Primary Responsibility |
| :--- | :--- | :--- |
| **1. Schedule** | `timer(0, interval)` | Periodic polling clock |
| **2. Combine** | `merge(manual$)` | Immediate manual refresh |
| **3. Cancel Stale** | `switchMap()` | Aborts slow pending requests |
| **4. Error Recovery** | Inner `catchError()` | Prevents polling stream death |
| **5. Cleanup** | `takeUntilDestroyed()` | Disposes on component destroy |""",
        "switchMap maintains an active subscription reference. When timer emits, it calls unsubscribe() on the active inner subscriber before fetching."
    ))

    return qs

def get_architecture_sections():
    return """# ADVANCED ENTERPRISE REFERENCE & PRODUCTION ARCHITECTURE

## 🏛️ Architecture 1: Angular Push-Pull Reactive Graph Architecture & Low-Level Internals

Modern Angular Signals operate as a Directed Acyclic Graph (DAG) connecting state producers to consumers.

### The Push-Pull Reactive Graph

```mermaid
flowchart TD
    subgraph Producers ["State Producers (Writable Signals)"]
        P1["quantity = signal(1)"]
        P2["unitPrice = signal(100)"]
        P3["discount = signal(10)"]
    end

    subgraph Derivations ["Intermediate Nodes (Computed Signals)"]
        D1["subtotal = computed(() => quantity() * unitPrice())"]
        D2["totalDiscount = computed(() => (subtotal() * discount()) / 100)"]
    end

    subgraph Consumers ["Terminal Consumers (Effects & Template Views)"]
        C1["finalPrice = computed(() => subtotal() - totalDiscount())"]
        E1["effect(() => syncCart(finalPrice()))"]
        V1["Component Template View Binding: {{ finalPrice() }}"]
    end

    P1 -->|1. Push Invalidation| D1
    P2 -->|1. Push Invalidation| D1
    D1 -->|1. Push Invalidation| D2
    P3 -->|1. Push Invalidation| D2
    D1 -->|1. Push Invalidation| C1
    D2 -->|1. Push Invalidation| C1
    C1 -->|1. Push Invalidation| E1
    C1 -->|1. Push Invalidation| V1

    V1 -.->|2. Pull Pristine Value| C1
    C1 -.->|2. Pull Pristine Value| D1
    C1 -.->|2. Pull Pristine Value| D2
```

1. **Push Phase (Dirty Flag Notification):** When a writable signal mutates via `.set()` or `.update()`, it does not immediately re-evaluate the entire downstream tree. Instead, it pushes a lightweight `DIRTY` notification down its dependent edges, marking consumers as needing re-evaluation.
2. **Pull Phase (Lazy Memoized Evaluation):** When a consumer (such as an effect or template binding) reads a computed signal, the consumer pulls the value. If the computed signal is marked dirty, it evaluates its upstream producers and caches the result. If clean, it returns its cached value immediately.
3. **Glitch-Free Topological Sorting:** Signals resolve the "diamond dependency problem" using dynamic topological sorting. Downstream nodes never observe intermediate contradictory states.

---

## 🏛️ Architecture 2: Zoneless Microtask Batching & Change Detection Tree Traversal

In Zoneless mode (`provideExperimentalZonelessChangeDetection()`), Angular coordinates view updates without Zone.js monkey-patching.

```mermaid
sequenceDiagram
    autonumber
    participant App as Component State (Signal)
    participant Graph as Signals Reactive DAG
    participant Sched as Zoneless Scheduler
    participant Queue as Microtask Queue (queueMicrotask)
    participant Engine as Change Detection Engine (ApplicationRef)
    participant DOM as Browser DOM

    App->>Graph: signal.set(newValue)
    Graph->>Graph: Propagate DIRTY flags down DAG
    Graph->>Sched: Request ApplicationRef.tick()
    Sched->>Queue: Enqueue tick on microtask queue
    Note over Queue: Coalesces 50 rapid signal updates into 1 turn
    Queue->>Engine: Flush microtask turn -> ApplicationRef.tick()
    Engine->>Engine: Traverse marked component views (depth-first)
    Engine->>DOM: Patch updated text nodes & attributes
```

- When signal state mutates, dirty flags notify the Zoneless scheduler.
- The scheduler enqueues a single tick request onto the browser microtask queue using `queueMicrotask()`.
- Fifty rapid synchronous mutations coalesce into a single DOM repaint cycle.

---

## 🏛️ Architecture 3: RxJS Higher-Order Flattening Execution Strategies

Choosing the right flattening operator dictates how concurrent asynchronous operations execute:

```mermaid
flowchart TD
    subgraph StreamInput ["Outer Stream Emission (e.g. User Keystrokes or Button Clicks)"]
        IN["Event Emission arrives at Flattening Operator"]
    end

    subgraph Strategies ["Concurrency Strategy"]
        direction TB
        SW["switchMap: Unsubscribes from active inner stream; executes newest only"]
        MG["mergeMap: Spawns parallel inner streams; emits all results concurrently"]
        CC["concatMap: Buffers incoming emissions; executes in strict FIFO sequence"]
        EX["exhaustMap: Discards incoming emissions while an inner stream is active"]
    end

    IN --> SW
    IN --> MG
    IN --> CC
    IN --> EX

    SW --> OUT1["Ideal for: Typeahead Search, Route Switching, Tab Navigation"]
    MG --> OUT2["Ideal for: Parallel independent reads, Bulk data processing"]
    CC --> OUT3["Ideal for: Sequential database writes, Financial balance transfers"]
    EX --> OUT4["Ideal for: Form submission, Login authentication, Payment triggers"]
```

---

## 🏛️ Architecture 4: Detached DOM Tree Memory Leak Mechanics

Understanding how uncancelled subscriptions cause retained memory leaks:

```mermaid
flowchart TD
    subgraph RootContext ["Garbage Collection Roots (V8 Engine)"]
        WIN["window / Global Scope"]
        ROOT_SVC["Singleton Service (providedIn: 'root')"]
    end

    subgraph HeapMemory ["Retained Heap Memory (Leak Path)"]
        SUB["RxJS Subscription Reference"]
        CLOSURE["Callback Closure Scope (capturing 'this')"]
        COMP["Destroyed Component Instance"]
        NATIVE_DOM["Detached DOM Nodes & Event Listeners"]
    end

    WIN --> ROOT_SVC
    ROOT_SVC -->|1. Retains active stream| SUB
    SUB -->|2. Retains observer callback| CLOSURE
    CLOSURE -->|3. Captures component pointer| COMP
    COMP -->|4. Retains template DOM references| NATIVE_DOM

    classDef leak fill:#fee2e2,stroke:#ef4444,stroke-width:2px;
    class HeapMemory,SUB,CLOSURE,COMP,NATIVE_DOM leak;
```

When a component is removed from the DOM, if an active subscription remains open in a singleton service, the closure retains the component instance in memory, creating a detached DOM tree leak.
"""
