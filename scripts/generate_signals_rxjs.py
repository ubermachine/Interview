#!/usr/bin/env python3
"""
Generator for 03_Angular_Signals_RxJS.md adhering strictly to SSE-1.
"""
import os, sys

def format_q(num, title, companies, one_line, spoken, terms, hook, code, follow_up_q, follow_up_a, comparison=None, hood=None):
    comp_str = ", ".join(companies)
    lines = [
        f"## Q{num}: {title}",
        f"*Commonly asked at: {comp_str}*",
        "",
        "**⚡ One-line answer**",
        one_line.strip(),
        "",
        "**🗣️ Spoken answer (30–45 seconds)**",
        spoken.strip(),
        "",
        "**🎯 Terms the interviewer listens for**"
    ]
    for term, gloss, starred in terms:
        star = " ⭐" if starred else ""
        lines.append(f"- **{term}**: {gloss}{star}")
    lines.append("")
    lines.append("**🧠 Memory hook**")
    lines.append(hook.strip())
    lines.append("")
    lines.append("**💻 Code**")
    lines.append("```typescript")
    lines.append(code.strip())
    lines.append("```")
    lines.append("")
    lines.append("**⚠️ Likely follow-up**")
    lines.append(f"*Question:* {follow_up_q.strip()}")
    lines.append(f"*Answer:* {follow_up_a.strip()}")
    
    if comparison:
        lines.append("")
        lines.append("**📊 Quick comparison**")
        lines.append(comparison.strip())
        
    if hood:
        lines.append("")
        lines.append("**🔬 Under the hood (optional)**")
        lines.append(hood.strip())
        
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)

def build_signals_rxjs():
    header = """# 03. Modern Angular (v16–v18+), Signals & RxJS Mastery (6+ YOE)

> **Target Audience:** Senior Frontend & Full-Stack Engineers (6+ Years Experience) preparing for Senior and Lead technical rounds at top product firms and GCCs.  
> **Philosophy:** Modern Angular exclusively (v16–v18+). Fine-grained reactivity, Signals graph propagation, Zoneless architecture, advanced RxJS flattening strategies, and leak-proof production design.

---

## Table of Contents
- [Part 1: Modern Angular Architecture & Reactive System Blueprint](#part-1-modern-angular-architecture--reactive-system-blueprint)
  - [1.1 Angular Architectural Evolution (v14 to v18+)](#11-angular-architectural-evolution-v14-to-v18)
  - [1.2 Angular Signals & Zoneless Change Detection](#12-angular-signals--zoneless-change-detection)
  - [1.3 RxJS Concurrency & Flattening Strategies](#13-rxjs-concurrency--flattening-strategies)
  - [1.4 Memory Leak Prevention & Teardown Architecture](#14-memory-leak-prevention--teardown-architecture)
  - [1.5 Change Detection Optimization: OnPush & NgZone Escaping](#15-change-detection-optimization-onpush--ngzone-escaping)
  - [1.6 Functional Interceptors & Modern Route Guards](#16-functional-interceptors--modern-route-guards)
  - [1.7 Enterprise State Management with NgRx SignalStore](#17-enterprise-state-management-with-ngrx-signalstore)
- [Part 2: Top 26 High-Frequency Senior Signals & RxJS Questions](#part-2-top-26-high-frequency-senior-signals--rxjs-questions)
"""

    part1 = """
---

# Part 1: Modern Angular Architecture & Reactive System Blueprint

### 1.1 Angular Architectural Evolution (v14 to v18+)
Modern Angular eliminates NgModule containers and Zone.js dirty-checking overhead. Standalone components declare explicit dependencies in their `imports` array, enabling dead-code elimination [tree-shaking]. Built-in control flow (`@if`, `@for`, `@switch`) compiles directly into native runtime instructions (`ɵɵconditional`, `ɵɵrepeater`). For a complete runnable standalone migration example, see [01-standalone-migration.ts](file:///home/ubermensch/Desktop/interview/examples/angular/01-standalone-migration.ts).

### 1.2 Angular Signals & Zoneless Change Detection
Angular Signals model state as a Directed Acyclic Graph (DAG) connecting producers to consumers. When a signal updates, dirty flags push down the graph, and consumers pull fresh values only on read. In zoneless mode (`provideExperimentalZonelessChangeDetection()`), signal notifications push updates directly to a microtask scheduler, batching DOM repaints without Zone.js. For a full live pricing implementation, see [02-signal-cart-pricing.ts](file:///home/ubermensch/Desktop/interview/examples/angular/02-signal-cart-pricing.ts).

### 1.3 RxJS Concurrency & Flattening Strategies
Flattening operators handle higher-order observables based on specific concurrency requirements:
- `switchMap`: cancels stale in-flight requests, ideal for typeahead search.
- `mergeMap`: runs child streams concurrently in parallel, ideal for independent reads.
- `concatMap`: queues child streams in strict order, ideal for sequential writes.
- `exhaustMap`: ignores new emissions while active, ideal for login and submit buttons.
For a complete typeahead catalog search implementation with local error boundaries, see [03-typeahead-search.ts](file:///home/ubermensch/Desktop/interview/examples/angular/03-typeahead-search.ts).

### 1.4 Memory Leak Prevention & Teardown Architecture
Memory leaks occur when long-lived subscriptions or uncancelled timers retain references to destroyed component instances. Modern Angular cleans them up automatically using `takeUntilDestroyed()` within injection contexts or declarative `toSignal()` bridges. For a leak-proof modal streaming implementation, see [04-leak-proof-modal.ts](file:///home/ubermensch/Desktop/interview/examples/angular/04-leak-proof-modal.ts).

### 1.5 Change Detection Optimization: OnPush & NgZone Escaping
`ChangeDetectionStrategy.OnPush` prunes clean subtrees during change passes, re-checking only when input references change, signals update, or local event handlers fire. For high-frequency DOM events like canvas drawing, `NgZone.runOutsideAngular()` runs listeners outside Zone.js to prevent change detection overhead. For a 60 FPS real-time rendering implementation, see [05-high-fps-ngzone.ts](file:///home/ubermensch/Desktop/interview/examples/angular/05-high-fps-ngzone.ts).

### 1.6 Functional Interceptors & Modern Route Guards
Angular replaces class-based middleware with functional `HttpInterceptorFn` and `CanActivateFn`. Interceptors clone immutable requests to attach authorization headers and coordinate silent JWT token refresh with concurrency locks. Route guards return atomic `UrlTree` redirects to prevent race conditions. For a complete implementation, see [06-jwt-refresh-interceptor.ts](file:///home/ubermensch/Desktop/interview/examples/angular/06-jwt-refresh-interceptor.ts).

### 1.7 Enterprise State Management with NgRx SignalStore
NgRx SignalStore provides lightweight, modular state management. Each state slice is a signal; `computed` caches its result until an input changes. Stores compose cleanly using `withState()`, `withComputed()`, and `withMethods()`. Asynchronous workflows integrate via `rxMethod`. For a complete SignalStore implementation, see [07-ngrx-signal-store.ts](file:///home/ubermensch/Desktop/interview/examples/angular/07-ngrx-signal-store.ts).

---

# Part 2: Top 26 High-Frequency Senior Signals & RxJS Questions

"""

    questions = []

    # Q1: signal, computed, effect
    questions.append(format_q(
        1,
        "What is the exact difference between signal, computed, and effect?",
        ["TCS", "Accenture", "Cognizant", "Infosys"],
        "signal holds writable state, computed derives read-only cached values, and effect executes side effects on state changes.",
        "The signals trio forms Angular's reactive foundation. A `signal()` holds writable state, updated via `.set()` or `.update()`. A `computed()` derives read-only state lazily, recalculating only when read and its dependencies changed. An `effect()` runs side effects like logging or localStorage synchronization, scheduled on browser microtasks. You should never write to signals inside effects to avoid infinite loops. In one of my projects, replacing manual state derivation with computed signals removed twenty state synchronization bugs.",
        [
            ("signal()", "writable reactive state container primitive", True),
            ("computed()", "lazily evaluated memoized derived signal", True),
            ("effect()", "microtask scheduled reactive side effect operation", True),
            ("Push-pull graph", "dirty flag propagation and lazy pulling", False),
            ("Reactive context", "tracks dynamic dependencies during function execution", False)
        ],
        "signal is an Excel number cell; computed is an Excel formula cell; effect is an email alert sent when totals change.",
        """// ❌ Bad: using effect to calculate derived state
effect(() => {
  this.total.set(this.qty() * this.price());
}, { allowSignalWrites: true });

// ✅ Good: pure declarative derived state with computed
readonly total = computed(() => this.qty() * this.price());""",
        "Can a computed signal write to another signal?",
        "No. Computed expressions must remain pure read-only derivations with zero side effects; mutating state inside them throws an error.",
        """| Primitive | Writable | Evaluation | Primary Purpose |
| :--- | :--- | :--- | :--- |
| `signal()` | Yes (`.set`, `.update`) | Immediate | State storage |
| `computed()` | No (Read-only) | Lazy on read | Derived state |
| `effect()` | No (Side effect) | Microtask queue | DOM sync, logging |""",
        "Computed nodes track producer versions. On read, if all upstream producer versions match cached versions, the memoized value returns immediately."
    ))

    # Q2: Mutating array directly with push
    questions.append(format_q(
        2,
        "Why is mutating a Signal array directly with push an anti-pattern?",
        ["Wipro", "TCS", "Capgemini", "Persistent"],
        "Signals check equality using Object.is; in-place array mutation keeps the same reference, so consumers never update.",
        "Signals use reference equality [Object.is] to decide whether consumers need re-evaluation. Calling `items().push(item)` mutates the existing array in place without changing its memory reference. Because the old reference and new reference are identical, the signal drops notifications and dependent templates fail to re-render. You must create a new array reference using `.update()` with the spread operator. In one of my projects, fixing direct mutations resolved missing shopping cart item updates.",
        [
            ("Object.is", "equality algorithm used for signal changes", True),
            ("Immutable update", "producing new references without in-place mutation", True),
            ("update()", "modifies signal value using a pure transformation", True),
            ("Reference equality", "evaluates memory address identity of objects", False),
            ("Dirty marking", "notifies downstream consumers of state changes", False)
        ],
        "Direct array push is writing a note inside an old book; immutable update is publishing a new edition with a fresh cover.",
        """// ❌ Bad: in-place mutation does not change reference
this.items().push(newItem);
// UI fails to update!

// ✅ Good: update returns a brand-new array reference
this.items.update(list => [...list, newItem]);""",
        "How can you supply a custom equality comparison function to a signal?",
        "Pass an options object with an equal function: `signal(value, { equal: (a, b) => customComparison(a, b) })`.",
        """| Mutation Style | Reference Identity | Signal Notification |
| :--- | :--- | :--- |
| `.push()` | Unchanged (`prev === next`) | Dropped (No UI update) |
| `.update([...list])` | New reference (`prev !== next`) | Emitted (UI updates) |""",
        "Signal nodes execute `equal(prevValue, nextValue)`. If true, the node returns without bumping its version or dirtying downstream consumers."
    ))

    # Q3: Purpose of untracked()
    questions.append(format_q(
        3,
        "What is the purpose of untracked inside an effect or computed signal?",
        ["Cognizant", "Accenture", "TCS", "Infosys"],
        "untracked reads a signal value without registering it as a reactive dependency in the current context.",
        "When an effect or computed executes, reading any signal registers that signal as a reactive dependency. Reading a signal inside `untracked()` accesses its current value while excluding it from dependency tracking. Consequently, subsequent mutations to that untracked signal will not trigger re-execution of the effect. This prevents circular dependency cascades and unintended re-runs. In one of my projects, untracked prevented infinite loops when logging analytics events alongside state updates.",
        [
            ("untracked()", "reads signal values without dependency registration", True),
            ("Reactive context", "execution scope tracking accessed signal producers", True),
            ("Circular dependency", "infinite loop caused by reciprocal signal triggers", True),
            ("Dynamic tracking", "registers dependencies accessed during branch execution", False),
            ("Version checking", "determines whether computed signals need re-evaluation", False)
        ],
        "untracked is like glancing at the wall clock while cooking without setting an alarm for every second.",
        """// ❌ Bad: effect re-runs whenever logCounter updates
effect(() => {
  console.log(this.user(), this.logCount());
});

// ✅ Good: reads logCount without tracking dependencies
effect(() => {
  console.log(this.user(), untracked(() => this.logCount()));
});""",
        "What happens if you mutate a signal inside an untracked block?",
        "Mutating signals inside untracked does not prevent notification propagation down the graph; it only excludes reads from the current scope.",
        """| Context | Normal Read | untracked() Read |
| :--- | :--- | :--- |
| `computed()` | Establishes dependency edge | Reads value without edge |
| `effect()` | Re-runs on signal change | Ignores signal change |""",
        "untracked temporarily sets the active reactive node context to null, reads the signal value, and restores the prior reactive context."
    ))

    # Q4: Defer trigger conditions
    questions.append(format_q(
        4,
        "Explain Deferrable Views (@defer) and their trigger conditions.",
        ["Capgemini", "Infosys", "Deloitte", "TCS"],
        "@defer lazily loads template sections on declarative triggers like viewport, interaction, hover, timer, or idle.",
        "Deferrable views allow declarative, template-level code splitting for components, directives, and pipes. The `@defer` block downloads and renders its content only when a configured trigger fires. Common triggers include `on viewport` using IntersectionObserver, `on interaction` on user click, `on hover`, and `on idle`. Companion blocks include `@placeholder`, `@loading`, and `@error` for states. In one of my projects, deferring offscreen comment lists reduced initial load JavaScript by thirty-five percent.",
        [
            ("@defer", "template block for lazy loading markup chunks", True),
            ("on viewport", "loads chunk when placeholder enters viewport", True),
            ("on idle", "loads chunk during browser idle time", True),
            ("@placeholder", "markup displayed before deferred load begins", False),
            ("@loading", "markup shown while the chunk is actively downloading", False)
        ],
        "@defer is ordering dessert only after finishing dinner rather than crowding the table at the start.",
        """// ❌ Bad: heavy chart bundled into main route chunk
<app-heavy-chart [data]="metrics" />

// ✅ Good: heavy chart loaded when visible
@defer (on viewport) {
  <app-heavy-chart [data]="metrics" />
}
@placeholder {
  <div class="h-40">Loading chart...</div>
}""",
        "Why should you always pair @defer with a @placeholder block when using on viewport?",
        "Without a placeholder, there is no rendered DOM element for the browser's IntersectionObserver to target, so viewport triggers fail to fire.",
        """| Trigger | Condition to Load | Best For |
| :--- | :--- | :--- |
| `on viewport` | Enters browser visible area | Below-the-fold content |
| `on interaction` | Click or keydown on target | Modals, dropdown menus |
| `on hover` | Mouse enters target element | Tooltips, popovers |
| `on idle` | Browser thread becomes idle | Analytics, charts |""",
        "The compiler extracts inner components of @defer blocks into separate dynamic chunks, wiring native browser observers to invoke import()."
    ))

    # Q5: forkJoin vs combineLatest
    questions.append(format_q(
        5,
        "How do forkJoin and combineLatest differ in execution and emission rules?",
        ["Cognizant", "Infosys", "Deloitte", "Capgemini"],
        "forkJoin waits for all streams to complete; combineLatest emits on any update once all have emitted at least once.",
        "These combination operators handle multiple streams under different trigger policies. `forkJoin` waits for all source observables to complete and emits their final values in parallel, acting like `Promise.all`. `combineLatest` emits whenever any source emits, provided every source has emitted at least once. Selecting the wrong operator causes stale data or hung streams. In one of my projects, forkJoin parallelized three independent configuration API calls on startup.",
        [
            ("forkJoin", "waits for all source streams to complete", True),
            ("combineLatest", "emits latest values whenever any source updates", True),
            ("Promise.all", "JavaScript promise combination equivalent to forkJoin", True),
            ("Completion rule", "stream must complete before emitting in forkJoin", False),
            ("Cold observable", "stream producing values upon subscription", False)
        ],
        "forkJoin waits for everyone to finish exams before leaving; combineLatest updates scores whenever any player scores.",
        """// ❌ Bad: combineLatest when completion is required
combineLatest([httpA$, httpB$]).subscribe(res => {
  this.handleData(res);
});

// ✅ Good: forkJoin waits for completion
forkJoin({
  users: this.getUsers(),
  roles: this.getRoles()
}).subscribe();""",
        "What happens if one source stream inside forkJoin throws an error?",
        "The entire forkJoin operation aborts immediately and errors out, dropping values from any other completed sibling streams.",
        """| Operator | Trigger Condition | Requires Completion |
| :--- | :--- | :--- |
| `forkJoin` | All sources complete | Yes |
| `combineLatest` | Any source emits new value | No |""",
        "forkJoin buffers the latest emission of each stream. When its completion countdown hits zero, it emits the aggregated array and completes."
    ))

    # Q6: BehaviorSubject vs ReplaySubject(1)
    questions.append(format_q(
        6,
        "What is the difference between BehaviorSubject and ReplaySubject(1)?",
        ["TCS", "Accenture", "LTIMindtree", "Persistent"],
        "BehaviorSubject requires an initial seed value; ReplaySubject(1) replays one past value without requiring an initial value.",
        "Both subjects replay cached data to late subscribers but differ in initialization and completion behavior. `BehaviorSubject` requires an initial seed value upon instantiation and always holds a current value synchronously accessible via `.getValue()`. `ReplaySubject(1)` does not require an initial value, remaining quiet until its first emission. Furthermore, when `BehaviorSubject` completes, late subscribers still receive its last value, whereas `ReplaySubject(1)` replays its buffered value even after completion. In one of my projects, ReplaySubject(1) handled one-shot auth tokens cleanly.",
        [
            ("BehaviorSubject", "stores current value and requires an initial seed", True),
            ("ReplaySubject(1)", "buffers one value without requiring an initial seed", True),
            ("getValue()", "synchronously reads current value of BehaviorSubject", True),
            ("Seed value", "initial value supplied during subject instantiation", False),
            ("Late subscriber", "observer subscribing after initial stream emissions", False)
        ],
        "BehaviorSubject is a clock always showing the current time; ReplaySubject(1) is a voice recorder replaying the latest message.",
        """// ❌ Bad: BehaviorSubject forced to use awkward null initial state
const token$ = new BehaviorSubject<string | null>(null);

// ✅ Good: ReplaySubject(1) emits only when real token arrives
const token$ = new ReplaySubject<string>(1);
token$.next('jwt-token-xyz');""",
        "Can a BehaviorSubject emit without having a value?",
        "No. By definition, a BehaviorSubject must be constructed with an initial value, so it always emits at least that seed value immediately.",
        """| Feature | BehaviorSubject | ReplaySubject(1) |
| :--- | :--- | :--- |
| **Initial Seed** | Mandatory | Not required |
| **Synchronous Read** | `.getValue()` supported | Not supported |
| **Emits on Complete** | Emits last value | Replays buffer |""",
        "BehaviorSubject stores its current value in an internal `_value` field; ReplaySubject buffers values in an internal array queue."
    ))

    # Q7: ExpressionChanged error
    questions.append(format_q(
        7,
        "What causes ExpressionChangedAfterItHasBeenCheckedError and how do you fix it?",
        ["Infosys", "Deloitte", "Cognizant", "TCS"],
        "It happens when property bindings mutate after parent template verification; fix it by moving updates earlier or using signals.",
        "This development-only error enforces unidirectional data flow. In development mode, Angular runs a second verification pass after change detection. If a binding value differs from what was checked in the primary pass, Angular throws this error. It typically occurs when a child component modifies a parent property inside lifecycle hooks like `ngAfterViewInit`. The fix is moving mutations to `ngOnInit` or managing state via signals. In one of my projects, switching to signal inputs eliminated this error.",
        [
            ("Unidirectional data flow", "data flows downward from parent to children", True),
            ("Verification pass", "development-only second check for binding stability", True),
            ("ngAfterViewInit", "hook that frequently triggers late mutation errors", True),
            ("queueMicrotask()", "postpones state mutations to subsequent event cycles", False),
            ("ChangeDetectorRef", "provides manual control over change detection runs", False)
        ],
        "It is like a bill inspector approving your grocery invoice, only for a cashier to add an item immediately after signing.",
        """// ❌ Bad: mutating parent property after view is checked
ngAfterViewInit(): void {
  this.parent.title = 'Updated';
}

// ✅ Good: update state via microtask or signal
ngAfterViewInit(): void {
  queueMicrotask(() => this.parent.title.set('Updated'));
}""",
        "Does ExpressionChangedAfterItHasBeenCheckedError ever throw in production builds?",
        "No. The second verification pass runs only in development mode to catch unstable bindings and race conditions before deployment.",
        """| Environment | Verification Pass | Error Thrown |
| :--- | :--- | :--- |
| **Development** | Runs second check pass | Yes (fails fast) |
| **Production** | Disabled for performance | No (silent inconsistency) |""",
        "In debug mode, `ApplicationRef.tick()` runs `checkAndUpdate()` followed by a second `checkNoChangesNode()` sweep to verify binding equality."
    ))

    # Q8: ViewChild static true vs false
    questions.append(format_q(
        8,
        "What is the difference between ViewChild static true and static false?",
        ["Wipro", "TCS", "Accenture", "HCL"],
        "static true resolves queries before change detection in ngOnInit; static false resolves after template rendering in ngAfterViewInit.",
        "The static flag determines the query resolution phase. When `{ static: true }` is configured, Angular resolves the element before change detection, making it available in `ngOnInit`. This works only if the element is not wrapped in conditional blocks like `@if` or `*ngIf`. When `{ static: false }` is used, the query resolves after view rendering in `ngAfterViewInit`. Modern `viewChild()` signals eliminate this flag completely. In one of my projects, viewChild signals simplified dynamic canvas initialization.",
        [
            ("static: true", "resolves query before change detection in ngOnInit", True),
            ("static: false", "resolves query after template render in ngAfterViewInit", True),
            ("Conditional DOM", "elements inside @if cannot resolve statically", True),
            ("viewChild()", "modern signal-based DOM query primitive", False),
            ("ElementRef", "wrapper around native DOM element instances", False)
        ],
        "static: true is checking your luggage before boarding; static: false is collecting luggage at the arrivals carousel after landing.",
        """// ❌ Bad: static true on conditional element returns undefined
@ViewChild('modal', { static: true })
modal!: ElementRef; // fails if inside @if!

// ✅ Good: modern viewChild signal updates dynamically
readonly modal = viewChild<ElementRef>('modal');""",
        "When should you still use static: true in legacy code?",
        "Use it only when you need to configure form controls or third-party adapters in ngOnInit before view rendering.",
        """| Configuration | Available In | Works Inside @if |
| :--- | :--- | :--- |
| `{ static: true }` | `ngOnInit` | No |
| `{ static: false }` | `ngAfterViewInit` | Yes |
| `viewChild()` signal | Reactively on render | Yes |""",
        "Static queries resolve during component view creation, whereas dynamic queries re-run during embedded view container updates."
    ))

    # Q9: @for vs *ngFor trackBy
    questions.append(format_q(
        9,
        "How does the modern @for block outperform *ngFor with trackBy?",
        ["Cognizant", "Accenture", "TCS", "Persistent"],
        "Built-in @for lowers into native ɵɵrepeater instructions, enforcing tracking keys at compile time and bypassing directive class allocations.",
        "Modern `@for` replaces legacy `*ngFor` structural directives. Because `@for` is compiler-native, it requires zero module imports and generates low-level `ɵɵrepeater` instructions. It enforces a mandatory `track` expression at compile time, eliminating list reconciliation bugs where developers omitted `trackBy`. Furthermore, `@for` includes a native `@empty` block, eliminating companion `*ngIf` checks. In one of my projects, switching to `@for` sped up list rendering by forty percent.",
        [
            ("@for loop", "compiler-native list rendering control flow block", True),
            ("track expression", "mandates unique identity key for list diffing", True),
            ("@empty block", "renders fallback template when collection has zero items", True),
            ("ɵɵrepeater", "compiler instruction for optimized list reconciliation", False),
            ("trackBy function", "legacy class method for identifying array elements", False)
        ],
        "*ngFor was an outside contractor hired to set up a market stall; @for is a built-in automated vending machine.",
        """// ❌ Bad: unkeyed *ngFor recreates entire DOM on every change
<div *ngFor="let item of items">{{ item.name }}</div>

// ✅ Good: modern @for with mandatory compile-time track
@for (item of items(); track item.id) {
  <div>{{ item.name }}</div>
} @empty {
  <p>No items found.</p>
}""",
        "Why is track $index discouraged for dynamic lists?",
        "Using `$index` tracks items by array position rather than data identity, causing incorrect input focus and DOM recycling bugs on sorting or deletion.",
        """| Feature | Legacy `*ngFor` | Modern Built-in `@for` |
| :--- | :--- | :--- |
| **Tracking Key** | Optional `trackBy` class method | Mandatory compile-time `track` |
| **Empty State** | Requires separate `*ngIf` | Integrated `@empty` block |
| **Performance** | Directive allocation overhead | Native ɵɵrepeater instruction |""",
        "The compiler lowers @for into ɵɵrepeaterCreate and ɵɵrepeater instructions, using an optimized diffing algorithm to minimize DOM moves."
    ))

    # Q10: Global error handling
    questions.append(format_q(
        10,
        "How do you implement global error handling in Angular?",
        ["TCS", "Cognizant", "Wipro", "Accenture"],
        "Implement global error handling by providing a custom ErrorHandler class in provideZoneChangeDetection or application config.",
        "Angular routes all unhandled application exceptions through a centralized `ErrorHandler` class. By default, it prints error details to the browser console. To customize handling, create a class implementing `ErrorHandler` and override its `handleError(error: unknown)` method. Register it in `app.config.ts` using `{ provide: ErrorHandler, useClass: GlobalErrorHandler }`. Inside, log errors to external monitoring platforms. In one of my projects, a custom ErrorHandler captured unhandled exceptions and forwarded them to Sentry.",
        [
            ("ErrorHandler", "centralized class catching unhandled errors", True),
            ("handleError()", "method executed when an unhandled exception occurs", True),
            ("Logging service", "forwards error diagnostics to monitoring platforms", True),
            ("Zone.js", "intercepts asynchronous errors and directs them to handler", False),
            ("provideErrorHandler", "configures application-wide error handling", False)
        ],
        "A global ErrorHandler is a central security control room receiving alarms from every sensor across a building.",
        """// ❌ Bad: scattered try-catch blocks with no central logging
try { doWork(); } catch(e) { console.error(e); }

// ✅ Good: centralized global error handler service
@Injectable()
export class AppErrorHandler implements ErrorHandler {
  handleError(err: unknown): void {
    logToService(err);
  }
}""",
        "Why must you use inject() or an Injector manually inside a custom ErrorHandler?",
        "ErrorHandler is instantiated before standard dependencies; injecting services directly in the constructor can cause circular dependency errors.",
        """| Error Mechanism | Scope | Primary Purpose |
| :--- | :--- | :--- |
| `ErrorHandler` | Entire application | Uncaught crash telemetry |
| `HttpInterceptor` | HTTP network layer | 4xx/5xx network retries |
| `catchError()` | Specific RxJS stream | Local fallback values |""",
        "Zone.js catches errors originating in microtasks or DOM events, routing them through `ApplicationRef` to the registered `ErrorHandler` instance."
    ))

    # Q11: Renderer2 vs direct ElementRef.nativeElement
    questions.append(format_q(
        11,
        "Explain the difference between Renderer2 and direct ElementRef.nativeElement access.",
        ["Infosys", "Capgemini", "Deloitte", "TCS"],
        "Renderer2 provides platform-independent DOM abstraction, whereas ElementRef.nativeElement couples code to the browser and risks XSS.",
        "Directly manipulating DOM properties via `ElementRef.nativeElement` couples your application strictly to browser environments. It bypasses Angular security sanitization, introducing cross-site scripting vulnerabilities and breaking server-side rendering [SSR]. `Renderer2` provides a safe abstraction layer across platforms. It coordinates mutations through Angular's rendering engine, supporting Web Workers and server environments safely. In one of my projects, migrating DOM styling to Renderer2 enabled seamless SSR hydration.",
        [
            ("Renderer2", "platform-independent DOM manipulation abstraction layer", True),
            ("ElementRef", "direct wrapper around native browser DOM elements", True),
            ("Server-side rendering", "rendering templates outside browser DOM context", True),
            ("DomSanitizer", "cleans untrusted HTML bindings to block XSS", False),
            ("Native element", "underlying browser HTML DOM node reference", False)
        ],
        "Renderer2 is a universal remote control operating any TV model; nativeElement is rewiring the circuit board directly by hand.",
        """// ❌ Bad: direct DOM access breaks SSR compatibility
setElementColor(): void {
  this.el.nativeElement.style.color = 'red';
}

// ✅ Good: platform-safe mutation through Renderer2
setSafeColor(): void {
  this.renderer.setStyle(this.el.nativeElement, 'color', 'red');
}""",
        "What is the modern preferred alternative to using Renderer2 for host element styling?",
        "Use the modern `host` property on the `@Component` decorator or host directives, avoiding programmatic DOM manipulation altogether.",
        """| Approach | SSR Compatible | XSS Safety | Platform Agnostic |
| :--- | :--- | :--- | :--- |
| `Renderer2` | Yes | High | Yes |
| `nativeElement` | No | Low | No |""",
        "On the server, Angular swaps the browser renderer with a DOM emulation engine, so direct browser DOM references crash the process."
    ))

    # Q12: Tree-Shaking for Angular Services
    questions.append(format_q(
        12,
        "How does Tree-Shaking work for Angular Services?",
        ["TCS", "Accenture", "Cognizant", "Persistent"],
        "Tree-shaking removes unused services from production bundles when declared via providedIn root instead of module provider arrays.",
        "Tree-shaking is a dead-code elimination process performed by bundlers like esbuild. When a service declares `@Injectable({ providedIn: 'root' })`, Angular marks it as tree-shakeable. The bundler examines the application's static dependency graph. If no component or service injects or references that service, the compiler excludes it from the final JavaScript output. Legacy `NgModule` provider arrays forced services into bundles unconditionally. In one of my projects, switching to providedIn root trimmed four hundred kilobytes of unused legacy services.",
        [
            ("providedIn: 'root'", "declares tree-shakeable application-level singleton", True),
            ("Dead-code elimination", "bundler process stripping unreferenced exports", True),
            ("Static analysis", "evaluating code import graphs at compile time", True),
            ("Module provider array", "legacy non-tree-shakeable provider registration", False),
            ("esbuild", "high-performance bundler analyzing dependency graphs", False)
        ],
        "Tree-shaking is like pruning a tree in winter: any branch with zero fruit or leaves is cut away to lighten the trunk.",
        """// ❌ Bad: module provider array bundles service unconditionally
@NgModule({ providers: [AnalyticsService] })
export class AnalyticsModule {}

// ✅ Good: tree-shakeable root provider stripped if unused
@Injectable({ providedIn: 'root' })
export class AnalyticsService {}""",
        "Why are services listed in component providers: [...] arrays not tree-shakeable?",
        "Component decorator metadata creates an explicit runtime reference; bundlers cannot guarantee the component will never be rendered.",
        """| Registration Style | Tree-Shakeable | Scope |
| :--- | :--- | :--- |
| `providedIn: 'root'` | Yes | Application singleton |
| `providedIn: 'platform'` | Yes | Multi-app platform |
| `@NgModule({ providers })` | No | Module-wide |
| `@Component({ providers })` | No | Component subtree |""",
        "Angular compiles providedIn: 'root' into a static ɵprov property on the service class, allowing bundlers to detect unused static properties."
    ))

    # Q13: Content Projection & Multi-Slot Projection
    questions.append(format_q(
        13,
        "What is Content Projection and how does Multi-Slot Projection work?",
        ["Infosys", "Capgemini", "Deloitte", "TCS"],
        "Content projection projects external markup into components using ng-content, using select attributes for multi-slot layouts.",
        "Content projection allows consumers to inject custom HTML fragments into a component template. Single-slot projection uses a plain `<ng-content></ng-content>` tag. Multi-slot projection uses the `select` attribute with CSS selectors like classes, tag names, or attributes to distribute content into distinct designated slots. Projected nodes are instantiated in the parent's context and resolved during `ngAfterContentInit`. In one of my projects, multi-slot projection allowed our modal component to accept separate header, body, and footer content.",
        [
            ("<ng-content>", "transclusion slot rendering external projected DOM", True),
            ("Multi-slot projection", "distributing content via select CSS attributes", True),
            ("ContentChild", "queries projected content elements within components", True),
            ("ngAfterContentInit", "hook where projected content resolves fully", False),
            ("Transclusion", "computer science term for inserting external markup", False)
        ],
        "A multi-slot picture frame with distinct cutouts for the photograph, title plaque, and commemorative seal.",
        """// ❌ Bad: hardcoding content prevents consumer customization
<div class="card-header">Header</div><div class="card-body">Body</div>

// ✅ Good: multi-slot content projection using CSS selectors
<div class="card">
  <ng-content select="[card-header]"></ng-content>
  <ng-content select="[card-body]"></ng-content>
</div>""",
        "What happens if projected content matches none of the select attributes in multi-slot projection?",
        "If a catch-all `<ng-content></ng-content>` tag without select exists, unassigned content renders there; otherwise, unmatched markup is discarded.",
        """| Projection Type | Syntax | Multiple Slots Allowed |
| :--- | :--- | :--- |
| **Single-Slot** | `<ng-content></ng-content>` | No |
| **Multi-Slot** | `<ng-content select="selector">` | Yes |""",
        "Angular tracks projected DOM nodes in the parent view tree, inserting pointers into the child view container at compile time."
    ))

    # Q14: Subject vs BehaviorSubject
    questions.append(format_q(
        14,
        "What is the difference between Subject and BehaviorSubject?",
        ["TCS", "Accenture", "LTIMindtree", "Persistent"],
        "Subject has no initial value; BehaviorSubject requires an initial seed value and always holds its current state.",
        "RxJS subjects act as both observable event emitters and observer consumers. A plain `Subject` emits only future events to subscribers; late subscribers receive nothing. A `BehaviorSubject` requires an initial seed value, holds its current value, and immediately replays it to new subscribers. You can synchronously read the current value of a BehaviorSubject using `.getValue()`. In one of my projects, BehaviorSubject shared authenticated user states across routes.",
        [
            ("Subject", "multicast observable without historical value storage", True),
            ("BehaviorSubject", "stores current value and requires an initial seed", True),
            ("getValue()", "synchronously reads current value of BehaviorSubject", True),
            ("Seed value", "initial value supplied during subject instantiation", False),
            ("Multicasting", "distributing single emission to multiple subscriber observers", False)
        ],
        "Subject is live radio; BehaviorSubject is a digital clock showing current time.",
        """// ❌ Bad: late subscriber misses previous emission
const user$ = new Subject<User>();
user$.next({ name: 'Alex' });

// ✅ Good: BehaviorSubject replays current authenticated user
const user$ = new BehaviorSubject<User | null>(null);
user$.next({ name: 'Alex' });""",
        "Why prefer Signals over BehaviorSubject for component state in modern Angular?",
        "Signals require no manual unsubscription, provide glitch-free computed derivations, and trigger fine-grained zoneless change detection natively.",
        """| Subject Type | Requires Initial Value | Late Subscriber Receives |
| :--- | :--- | :--- |
| `Subject` | No | Future emissions only |
| `BehaviorSubject` | Yes | Most recent value |""",
        "BehaviorSubject overrides `_subscribe` to call `next()` immediately with its internal `_value` buffer before registering the observer."
    ))

    # Q15: Cross-Site Scripting (XSS) & DomSanitizer
    questions.append(format_q(
        15,
        "How does Angular protect against Cross-Site Scripting (XSS) and when should you use DomSanitizer?",
        ["Accenture", "TCS", "Cognizant", "Persistent"],
        "Angular sanitizes untrusted bindings automatically; use DomSanitizer only to explicitly trust verified safe content.",
        "Angular treats all untrusted template values as dangerous by default. During binding compilation, Angular passes values through security contexts, stripping malicious script tags and inline handlers. If you must display safe HTML or trusted external URLs, use `DomSanitizer`. Methods like `bypassSecurityTrustHtml` tell Angular to skip sanitization. You should use it only after thoroughly validating input sources. In one of my projects, sanitizing third-party SVG icons prevented potential script injections.",
        [
            ("DomSanitizer", "service for bypassing Angular security sanitization", True),
            ("Security context", "categorizes bindings like HTML, style, URL", True),
            ("XSS protection", "stripping executable malicious scripts from markup", True),
            ("bypassSecurityTrustHtml", "marks HTML string as safe for rendering", False),
            ("Interpolation escaping", "automatically escapes HTML in template bindings", False)
        ],
        "Angular sanitization is airport luggage screening; DomSanitizer is issuing an express VIP pass to verified diplomatic cargo.",
        """// ❌ Bad: rendering raw HTML directly risks injection
<div [innerHTML]="untrustedContent"></div>

// ✅ Good: sanitize through DomSanitizer after verification
readonly safeHtml = computed(() => {
  return this.sanitizer.bypassSecurityTrustHtml(this.content());
});""",
        "What happens if an attacker injects a <script> tag into a regular {{ value }} binding?",
        "Angular treats it as plain text and escapes it into harmless characters like &lt;script&gt;, so the browser never executes it.",
        """| Binding Type | Default Security | Sanitizer Required |
| :--- | :--- | :--- |
| `{{ value }}` | Encoded as plain text | Never |
| `[innerHTML]` | Sanitized by context | Only for custom trusted markup |
| `[src]` | URL sanitized | Only for trusted dynamic URLs |""",
        "Angular's compiler maps bindings to contexts (HTML, STYLE, SCRIPT, URL, RESOURCE_URL), applying regular expression cleaners per context."
    ))

    # Q16: Non-Destructive Hydration in SSR
    questions.append(format_q(
        16,
        "What is Non-Destructive Hydration in modern Angular Server-Side Rendering?",
        ["Deloitte", "Infosys", "Capgemini", "TCS"],
        "Non-destructive hydration attaches event listeners to server-rendered DOM instead of destroying and re-rendering markup.",
        "In legacy Angular SSR, the browser downloaded server-rendered HTML and immediately destroyed all DOM nodes to re-render client components. This caused noticeable screen flickering and lost form input states. Modern Angular uses non-destructive hydration enabled via `provideClientHydration()`. The client traverses the existing server DOM, matches components to nodes, and attaches event listeners in place. In one of my projects, enabling hydration reduced Largest Contentful Paint [LCP] by forty percent.",
        [
            ("provideClientHydration()", "enables non-destructive hydration in client bootstrap", True),
            ("DOM recycling", "attaches events to existing nodes without recreation", True),
            ("Flickering reduction", "prevents visible page flashes during page load", True),
            ("Largest Contentful Paint", "Core Web Vital metric measuring visual load speed", False),
            ("TransferState", "shares server-fetched data with client bootstrap", False)
        ],
        "Legacy hydration bulldozed a house to rebuild the same house; non-destructive hydration moves furniture into the existing house.",
        """// ❌ Bad: manual SSR bootstrap destroying markup
bootstrapApplication(AppComponent, {
  providers: []
});

// ✅ Good: enable non-destructive hydration in application config
bootstrapApplication(AppComponent, {
  providers: [provideClientHydration()]
});""",
        "What causes hydration mismatch errors in the console?",
        "Hydration mismatches occur when client markup diverges from server HTML, commonly due to reading browser-only globals like window or localStorage.",
        """| Hydration Mode | DOM Destruction | Visual Flash | Performance |
| :--- | :--- | :--- | :--- |
| **Legacy SSR** | Complete wipe and redraw | High flicker | Poor LCP |
| **Non-Destructive** | Reuses server DOM nodes | Zero flicker | Optimal LCP |""",
        "The server annotates DOM nodes with hydration IDs. On the client, Angular reconciles template instructions against these IDs."
    ))

    # Q17: runInInjectionContext
    questions.append(format_q(
        17,
        "What is the purpose of runInInjectionContext in modern Angular?",
        ["Capgemini", "Cognizant", "Persistent", "Accenture"],
        "runInInjectionContext allows executing functions requiring dependency injection outside standard lifecycle windows using an explicit injector.",
        "In modern Angular, `inject()` is legally allowed only during class field initialization, constructor execution, or functional route guards. Calling `inject()` inside asynchronous callbacks like setTimeout or Promise resolutions throws error `NG0203`. `runInInjectionContext` allows you to manually establish an injection frame by passing an `EnvironmentInjector`. This restores the injector stack, allowing functional composables to resolve dependencies safely. In one of my projects, runInInjectionContext allowed asynchronous dialog helpers to inject notification services cleanly.",
        [
            ("runInInjectionContext()", "manually restores injection context for callbacks", True),
            ("EnvironmentInjector", "injector hierarchy for routes and application scope", True),
            ("NG0203 error", "thrown when inject() is called outside context", True),
            ("Injection context", "time window when dependency resolution is legal", False),
            ("Functional composable", "reusable utility resolving dependencies dynamically", False)
        ],
        "A temporary visitor security badge allowing a contractor to use workshop tools after hours.",
        """// ❌ Bad: calling inject() inside async callback throws NG0203
setTimeout(() => { const router = inject(Router); }); // Error!

// ✅ Good: restore injection context using captured injector
const injector = inject(EnvironmentInjector);
setTimeout(() => {
  runInInjectionContext(injector, () => inject(Router).navigate(['/']));
});""",
        "Can runInInjectionContext resolve component-level ElementInjector tokens?",
        "No. If you pass an EnvironmentInjector, it can only resolve environment tokens; to resolve element tokens, capture an ElementInjector reference.",
        """| Execution Timing | Direct inject() Allowed | Requires runInInjectionContext |
| :--- | :--- | :--- |
| **Class Field Init** | Yes | No |
| **Constructor Body** | Yes | No |
| **setTimeout / Promise** | No (Throws NG0203) | Yes |
| **Functional Guard** | Yes | No |""",
        "Angular pushes the provided injector to the top of its internal injector stack, runs the callback, and pops the injector when finished."
    ))

    # Q18: take(1) vs first()
    questions.append(format_q(
        18,
        "What is the difference between take(1) and first() in RxJS?",
        ["TCS", "Wipro", "Cognizant", "Accenture"],
        "take(1) completes on the first emission; first() errors if empty; single() errors if more or less than one value emits.",
        "These three operators take items from observable streams with different completion conditions. `take(1)` emits the first value and completes immediately; if the stream completes empty, it completes without error. `first()` emits the first matching item; if the stream completes without emitting, it throws an `EmptyError`. `single()` asserts that exactly one item matches; if zero or multiple items emit, it throws an error. In one of my projects, take(1) fetched single configuration snapshots cleanly.",
        [
            ("take(1)", "emits first value and completes without empty error", True),
            ("first()", "emits first value but throws EmptyError if empty", True),
            ("single()", "errors if emission count is not exactly one", True),
            ("Predicate function", "conditional callback filtering emitted values", False),
            ("EmptyError", "exception thrown when expected values fail to emit", False)
        ],
        "take(1) takes the first bus leaving; first() demands at least one bus runs; single() insists only one bus exists on the route.",
        """// ❌ Bad: single errors on multiple emitted items
items$.pipe(
  single()
).subscribe();

// ✅ Good: take(1) safely grabs first item
items$.pipe(
  take(1)
).subscribe();""",
        "When would you choose first() over take(1)?",
        "Use first() when an empty stream represents an illegal application state that should fail loudly and trigger error boundaries.",
        """| Operator | Zero Items | One Item | Multiple Items |
| :--- | :--- | :--- | :--- |
| `take(1)` | Completes | Emits & completes | Emits first & completes |
| `first()` | Throws `EmptyError` | Emits & completes | Emits first & completes |""",
        "take(1) decrements an internal counter and unsubscribes from the source observable synchronously upon receiving its first item."
    ))

    # Q19: HostBinding / HostListener vs host property
    questions.append(format_q(
        19,
        "Explain host property bindings vs @HostBinding and @HostListener.",
        ["Capgemini", "Infosys", "Deloitte", "Cognizant"],
        "The component host property declares host bindings cleanly in metadata, eliminating legacy decorator boilerplate.",
        "Angular components and directives often need to bind attributes or listen to events on their host DOM element. The legacy approach used `@HostBinding` and `@HostListener` decorators on class properties and methods. Modern Angular recommends declaring bindings inside the decorator `host` property. This approach centralizes template metadata, improves compiler optimizations, and avoids unnecessary class fields. In one of my projects, migrating to the host property simplified custom tooltip directives.",
        [
            ("host property", "decorator metadata object configuring host element bindings", True),
            ("@HostBinding", "legacy decorator binding host property to class field", True),
            ("@HostListener", "legacy decorator binding host events to class method", True),
            ("Host element", "the DOM node enclosing the component template", False),
            ("Metadata centralization", "keeping component configuration inside decorator", False)
        ],
        "The host property is a component's nameplate on its front door, declaring rules clearly in one visible place.",
        """// ❌ Bad: scattered legacy decorators bloating class
@HostBinding('class.active') isActive = true;
@HostListener('click') onClick() {}

// ✅ Good: clean centralized host metadata property
@Component({
  host: {
    '[class.active]': 'isActive()',
    '(click)': 'onClick()'
  }
})
export class ModernCardComponent {}""",
        "Can you use signal expressions inside the host metadata property?",
        "Yes. Angular evaluates signal calls like `'[class.active]': 'isActive()'` reactively, updating host element classes automatically.",
        """| Approach | Syntax Location | Class Clutter |
| :--- | :--- | :--- |
| **host property** | Inside decorator metadata | Zero extra fields |
| **@HostBinding** | Decorator on class properties | High class boilerplate |
| **@HostListener** | Decorator on class methods | Method wrapper bloat |""",
        "The compiler parses the host metadata object into instruction nodes, applying updates during the component's host binding execution phase."
    ))

    # Q20: Component Inputs with Transforms
    questions.append(format_q(
        20,
        "What are component input transforms like booleanAttribute and numberAttribute?",
        ["TCS", "Accenture", "Wipro", "HCL"],
        "Input transforms automatically parse string attributes into booleans or numbers without manual setter boilerplate.",
        "When HTML attributes are applied without property brackets, browsers pass them as strings. Historically, developers wrote verbose getters and setters to convert empty string flags into true booleans. Angular provides built-in transform functions like `booleanAttribute` and `numberAttribute`. Passing `{ transform: booleanAttribute }` to an input converts `<app-btn disabled />` into a proper boolean. In one of my projects, input transforms removed forty lines of property coercion boilerplate.",
        [
            ("booleanAttribute", "coerces presence or string values to booleans", True),
            ("numberAttribute", "coerces incoming string inputs into numeric types", True),
            ("input() transform", "option configuring automatic value conversion", True),
            ("Coercion boilerplate", "manual getters and setters converting types", False),
            ("HTML attribute binding", "passing unbracketed strings from template markup", False)
        ],
        "An input transform is a universal electrical adapter converting foreign wall plug voltages automatically into your device's voltage.",
        """// ❌ Bad: verbose getter/setter for boolean coercion
private _disabled = false;
@Input() set disabled(v: any) {
  this._disabled = v === '' || !!v;
}

// ✅ Good: built-in transform on modern signal input
readonly disabled = input(false, {
  transform: booleanAttribute
});""",
        "What does booleanAttribute('') return when passing an empty attribute flag?",
        "It returns true, adhering to standard HTML boolean attribute semantics where the mere presence of an attribute implies true.",
        """| Transform Function | Input Value `""` | Input Value `"123"` | Fallback on NaN |
| :--- | :--- | :--- | :--- |
| `booleanAttribute` | `true` | `true` | N/A |
| `numberAttribute` | `NaN` | `123` | Configurable fallback |""",
        "Transforms execute during property binding evaluation, converting raw attribute values before storing them in the signal node."
    ))

    # Q21: router.navigate vs router.navigateByUrl
    questions.append(format_q(
        21,
        "What is the difference between router.navigate and router.navigateByUrl?",
        ["TCS", "Cognizant", "Persistent", "Capgemini"],
        "router.navigate accepts route command arrays for relative path construction, while navigateByUrl requires an absolute URL string.",
        "Angular provides two primary imperative navigation methods. `router.navigate()` accepts a command array, allowing relative navigation from the current `ActivatedRoute` using `./` or `../`. It parses path segments and merges query parameters flexibly. `router.navigateByUrl()` takes a complete absolute URL string starting from the root slash, replacing the entire navigation tree immediately. `navigateByUrl` is faster because it bypasses relative path calculation. In one of my projects, navigateByUrl handled external deep-link redirects efficiently.",
        [
            ("router.navigate()", "navigates based on provided command array parameters", True),
            ("router.navigateByUrl()", "navigates directly using absolute URL string path", True),
            ("Command array", "ordered list of route path segments and parameters", True),
            ("Relative navigation", "resolving target paths relative to active route", False),
            ("UrlTree", "internal data structure representing parsed application URL", False)
        ],
        "navigate() is giving turn-by-turn driving directions from your current spot; navigateByUrl is entering an exact GPS destination address.",
        """// ❌ Bad: using relative command array for absolute deep links
this.router.navigate(['/portal', 'users', id]);

// ✅ Good: navigateByUrl executes immediate absolute navigation
this.router.navigateByUrl(`/portal/users/${id}`);""",
        "Can router.navigateByUrl() perform relative navigation from a child route?",
        "No. navigateByUrl always takes an absolute URL path starting from root `/` and cannot navigate relatively.",
        """| Method | Parameter Type | Supports Relative Path |
| :--- | :--- | :--- |
| `navigate()` | Command array `[...]` | Yes (via `relativeTo`) |
| `navigateByUrl()` | Complete URL string | No (Strictly absolute) |""",
        "navigate() runs createUrlTree() merging relative activated route segments before dispatching transition events."
    ))

    # Q22: shareReplay(1) vs refCount: true
    questions.append(format_q(
        22,
        "Why is shareReplay(1) dangerous without refCount true?",
        ["Cognizant", "Infosys", "Deloitte", "TCS"],
        "shareReplay(1) without refCount keeps the source subscription open forever, causing permanent memory leaks.",
        "The `shareReplay` operator multicasts an observable stream, caching its latest emission for late subscribers. Calling `shareReplay(1)` without `refCount: true` keeps the internal subject subscribed indefinitely. It stays subscribed even after all consumer components unmount. This retains services and HTTP connections in memory permanently. Adding `{ bufferSize: 1, refCount: true }` ensures that when subscribers drop to zero, the source unsubscribes cleanly. In one of my projects, adding refCount fixed memory leaks in our navigation service.",
        [
            ("shareReplay(1)", "multicasts and caches latest emissions for late subscribers", True),
            ("refCount: true", "unsubscribes from source when subscriber count hits zero", True),
            ("Subscription retention", "holding upstream observable connections open indefinitely", True),
            ("Multicast stream", "sharing a single execution among multiple observers", False),
            ("ReplaySubject buffer", "stores historical values to emit to new subscribers", False)
        ],
        "shareReplay without refCount is leaving the garden hose running full blast after everyone has finished watering their plants.",
        """// ❌ Bad: source connection never disconnects after teardown
readonly config$ = this.http.get('/config').pipe(
  shareReplay(1)
);

// ✅ Good: refCount cleans up source when subscribers drop
readonly config$ = this.http.get('/config').pipe(
  shareReplay({ bufferSize: 1, refCount: true })
);""",
        "Why does shareReplay default to refCount false?",
        "It was designed for singleton services where requests should execute exactly once per application lifetime and never re-fetch on component re-mounts.",
        """| Configuration | Unsubscribes on Zero Consumers | Re-Executes on New Consumer |
| :--- | :--- | :--- |
| `shareReplay(1)` | No (Permanent leak risk) | Never (Caches forever) |
| `{ refCount: true }` | Yes (Cleans up source) | Yes (Re-subscribes) |""",
        "When refCount is true, an internal subscriber reference counter tracks active observers, triggering source disposal when the count reaches zero."
    ))

    # Q23: Route Resolvers
    questions.append(format_q(
        23,
        "How do you handle Route Resolvers in modern Angular?",
        ["Infosys", "Capgemini", "TCS", "Wipro"],
        "Use functional ResolveFn for pre-fetching data before route transition, or prefer immediate navigation with signal-driven skeleton loading.",
        "Route resolvers pre-fetch data before a route transition completes. Modern Angular uses functional resolvers via `ResolveFn`. Resolvers prevent blank screens by delaying navigation until data arrives. However, slow network calls delay navigation transitions noticeably, hurting user experience. In modern reactive architecture, senior teams often bypass resolvers. Instead, they navigate immediately, render skeleton screens, and fetch data via Signal services reactively. In one of my projects, switching from resolvers to signal services made page transitions feel instant.",
        [
            ("ResolveFn", "functional route resolver pre-fetching route data", True),
            ("Skeleton screen", "placeholder layout rendered during asynchronous loading", True),
            ("Route transition delay", "delayed navigation caused by slow backend resolvers", True),
            ("withComponentInputBinding", "binds resolved route data to signal inputs", False),
            ("ActivatedRouteSnapshot", "contains route parameter state for resolvers", False)
        ],
        "A resolver is waiting in the restaurant lobby until food is cooked; signal streaming is sitting immediately while chefs prepare dishes.",
        """// ❌ Bad: heavy resolver delays route transition by seconds
export const userResolver: ResolveFn<User> = (route) => {
  return inject(UserService).fetchLargeProfile(route.params['id']);
};

// ✅ Good: immediate navigation with signal-driven skeleton
readonly user = toSignal(this.userService.loadProfile());""",
        "How can resolved data be passed directly into component signal inputs?",
        "Configure `provideRouter(routes, withComponentInputBinding())`; Angular then maps resolved data properties directly to matching `input()` signals.",
        """| Approach | Navigation Speed | User Feedback |
| :--- | :--- | :--- |
| **ResolveFn** | Blocked until API returns | Frozen browser URL |
| **Signal Service** | Instant route transition | Immediate skeleton screen |""",
        "When resolvers execute, the Router pauses the NavigationTransition until all resolved observables complete or emit their first item."
    ))

    # Q24: NgOptimizedImage
    questions.append(format_q(
        24,
        "What is the purpose of NgOptimizedImage (ngSrc) and what optimizations does it enforce?",
        ["Deloitte", "Infosys", "Capgemini", "TCS"],
        "NgOptimizedImage enforces explicit dimensions, generates responsive srcsets, lazy-loads non-priority images, and optimizes Core Web Vitals.",
        "The `NgOptimizedImage` directive replaces raw `<img>` tags to improve visual load performance. It requires developers to declare explicit `width` and `height` attributes to prevent Cumulative Layout Shifts [CLS]. For above-the-fold hero images, the `priority` attribute preloads the image to optimize Largest Contentful Paint [LCP]. It automatically configures lazy loading for offscreen images and warns against broken aspect ratios in development mode. In one of my projects, adopting NgOptimizedImage boosted our Lighthouse performance score significantly.",
        [
            ("NgOptimizedImage", "standalone directive optimizing web image performance", True),
            ("Cumulative Layout Shift", "Core Web Vital measuring unexpected page layout shifts", True),
            ("priority attribute", "preloads critical above-the-fold hero image assets", True),
            ("Largest Contentful Paint", "Core Web Vital metric measuring visual load speed", False),
            ("Image loader", "custom provider formatting image URLs with CDN transforms", False)
        ],
        "An interior designer who reserves wall space before heavy paintings arrive, preventing furniture rearrangement.",
        """// ❌ Bad: raw img tag without dimensions causes layout shifts
<img src="banner.jpg">

// ✅ Good: NgOptimizedImage with dimensions and priority
<img ngSrc="banner.jpg" width="800" height="400" priority>""",
        "What happens if an image using NgOptimizedImage omits width and height?",
        "Angular throws a compile-time or runtime error unless the `fill` attribute is used to fill a styled parent container.",
        """| Feature | Raw `<img>` Tag | `NgOptimizedImage` (`ngSrc`) |
| :--- | :--- | :--- |
| **Dimension Checks** | Optional (Causes CLS) | Mandatory (Prevents CLS) |
| **Preloading** | Manual `<link rel="preload">` | Automated with `priority` |
| **Lazy Loading** | Requires manual attribute | Automatic default |""",
        "NgOptimizedImage dynamically generates preconnect link tags for CDN domains and builds responsive `srcset` breakpoints."
    ))

    # Q25: Circular Dependency Loops in Signals
    questions.append(format_q(
        25,
        "How do Angular Signals handle circular dependency loops?",
        ["Google", "Microsoft", "TCS", "Accenture"],
        "Signals detect circular dependencies dynamically during graph evaluation, throwing an error immediately to prevent infinite browser freezes.",
        "Angular Signals use a Directed Acyclic Graph [DAG] to model reactive dependencies. When a `computed()` signal or `effect()` reads a signal, the runtime registers a dependency edge. If an effect mutates a signal that it directly or indirectly depends upon, Angular detects this circular evaluation loop. The runtime halts execution and throws error `NG0600: Circular dependency detected in Signals`. To prevent circular loops, isolate non-reactive reads using `untracked()`. In one of my projects, untracked broke an accidental circular update between search inputs and analytics logs.",
        [
            ("Circular dependency", "infinite loop caused by reciprocal signal triggers", True),
            ("Directed Acyclic Graph", "graph structure powering signal dependency tracking", True),
            ("NG0600 error", "thrown when circular signal evaluation is detected", True),
            ("untracked()", "reads signal values without dependency registration", False),
            ("Reactive node version", "internal counter verifying freshness of cached states", False)
        ],
        "A circular dependency is two mirrors facing each other reflecting an infinite corridor of light.",
        """// ❌ Bad: effect writes to signal it depends on, causing cycle
effect(() => { this.count.set(this.count() + 1); }); // NG0600!

// ✅ Good: isolate side effects or untrack read dependencies
effect(() => {
  const current = untracked(() => this.count());
  this.analytics.send(current);
});""",
        "Can a computed signal create a circular dependency loop?",
        "Yes. If computed A reads computed B which in turn reads computed A, Angular detects the cycle on read and throws NG0600 immediately.",
        """| Context | Cycle Cause | Runtime Behavior |
| :--- | :--- | :--- |
| `computed()` | Reciprocal reads (A reads B reads A) | Throws `NG0600` |
| `effect()` | Mutates signal that triggers effect | Throws `NG0600` |""",
        "The signals engine marks active nodes as `EVALUATING`. If an evaluating node is visited again during the same pass, a cycle is flagged."
    ))

    # Q26: RxJS Flattening Operators (switchMap, mergeMap, concatMap, exhaustMap)
    questions.append(format_q(
        26,
        "How do switchMap, mergeMap, concatMap, and exhaustMap differ in real-world scenarios?",
        ["TCS", "Cognizant", "Deloitte", "Wipro"],
        "switchMap cancels stale requests; mergeMap runs parallel reads; concatMap queues writes sequentially; exhaustMap ignores concurrent submissions.",
        "Flattening operators handle higher-order observables based on specific concurrency requirements: `switchMap` cancels stale inner requests, making it ideal for typeahead search. `mergeMap` runs inner streams concurrently in parallel, making it ideal for independent reads. `concatMap` queues inner streams in strict order, making it ideal for sequential writes. `exhaustMap` ignores new triggers while an active inner stream runs, making it ideal for login and submit buttons. In one of my projects, exhaustMap eliminated duplicate checkout orders.",
        [
            ("switchMap", "cancels stale in-flight streams for search", True),
            ("mergeMap", "runs parallel independent child requests concurrently", True),
            ("concatMap", "queues streams in sequential FIFO order", True),
            ("exhaustMap", "ignores new inputs until current completes", False),
            ("Higher-order stream", "observable emitting inner observable instances", False)
        ],
        "switchMap is changing TV channels; mergeMap is multi-burner cooking; concatMap is ticket queueing; exhaustMap is an occupied restroom.",
        """// ❌ Bad: mergeMap causes out-of-order search responses
search$.pipe(
  mergeMap(q => this.http.get(`/search?q=${q}`))
).subscribe();

// ✅ Good: switchMap cancels stale search requests
search$.pipe(
  switchMap(q => this.http.get(`/search?q=${q}`))
).subscribe();""",
        "Which flattening operator should you use for financial balance transfers?",
        "Use concatMap to guarantee that debit and credit transactions execute sequentially in strict order without concurrency race conditions.",
        """| Operator | Concurrency Rule | Primary Use Case |
| :--- | :--- | :--- |
| `switchMap` | Cancels active inner stream | Typeahead search |
| `mergeMap` | Runs parallel concurrently | Independent reads |
| `concatMap` | Queues in sequential order | Sequential writes |
| `exhaustMap` | Ignores incoming while busy | Submit & login buttons |""",
        "Higher-order operators manage inner subscription references, handling inner completion signals and outer unsubscriptions according to operator policy."
    ))

    footer = """## Summary Cheatsheet: Signals & RxJS Mastery Anti-Pattern vs Senior Pattern

| Scenario | ❌ Anti-Pattern | ✅ Modern Senior Clean Pattern |
| :--- | :--- | :--- |
| **State management** | BehaviorSubject with manual unsubscriptions | Signal state with `computed` derivations |
| **Component dependencies** | Monolithic `SharedModule` dumping ground | Standalone components with explicit `imports` |
| **Template control flow** | `*ngIf`, `*ngFor` with `trackBy` class methods | `@if`, `@for (...; track id)`, `@defer` |
| **Component communication** | `@Input()` with `ngOnChanges` dirty checking | `input()`, `output()`, and `model()` signals |
| **DOM queries** | `@ViewChild` with static flag ambiguities | Modern `viewChild()` and `contentChild()` signals |
| **Stream cancellation** | Nested subscriptions without teardown | `takeUntilDestroyed()` or `toSignal()` |
| **HTTP Interceptors** | Class-based `HTTP_INTERCEPTORS` multi-token | Composable functional `HttpInterceptorFn` |
| **Route Guards** | Class-based `CanActivate` interfaces | Lightweight functional `CanActivateFn` with `UrlTree` |
"""

    full_text = header + part1 + "\n".join(questions) + "\n" + footer
    with open('/home/ubermensch/Desktop/interview/03_Angular_Signals_RxJS.md', 'w', encoding='utf-8') as f:
        f.write(full_text)
    print("03_Angular_Signals_RxJS.md successfully generated!")

if __name__ == '__main__':
    build_signals_rxjs()
