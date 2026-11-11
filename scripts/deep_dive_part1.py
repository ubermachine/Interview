#!/usr/bin/env python3
"""
Deep Dive Part 1: Modules 1 to 5 (Q1 to Q17)
"""
from generate_deep_dive import format_q

def get_part1_questions():
    qs = []

    # Q1: Lifecycle sequence
    qs.append(format_q(
        1,
        "What is the exact execution sequence of Angular component lifecycle hooks?",
        ["TCS", "Infosys", "Cognizant", "Accenture"],
        "Angular lifecycle hooks execute in a deterministic order from constructor initialization down to final DOM destruction.",
        "Angular manages components through a strict deterministic state sequence. The class constructor runs first for dependency injection. Next, input change detection [ngOnChanges] checks property bindings, followed by ngOnInit for initial business logic. Content projection hooks resolve before view hooks verify the DOM tree. Finally, teardown [ngOnDestroy] frees open subscriptions before element removal. In one of my projects, moving REST calls to ngOnInit prevented premature initialization failures.",
        [
            ("ngOnInit", "executes once after initial inputs are verified", True),
            ("ngOnChanges", "fires whenever input property references mutate", True),
            ("ngOnDestroy", "cleans active subscriptions before DOM removal", True),
            ("ngAfterViewInit", "fires when component template DOM renders", False),
            ("Unidirectional data flow", "prevents binding mutations during render passes", False)
        ],
        "Think of constructing a modular building: lay foundations, verify blueprints, install furniture, inspect lighting, and dismantle cleanly on demolition.",
        """// ❌ Bad: heavy network call in constructor
constructor(private http: HttpClient) {
  this.http.get('/api/data').subscribe();
}

// ✅ Good: dispatch initial calls in ngOnInit
ngOnInit(): void {
  this.userService.loadInitialProfile();
}""",
        "Why must constructors remain lightweight without side effects?",
        "Constructors run before input bindings resolve; placing asynchronous work there violates separation of concerns and complicates unit testing.",
        """| Hook | Trigger Timing | Primary Responsibility |
| :--- | :--- | :--- |
| `ngOnChanges` | Input reference changes | Validates bound data |
| `ngOnInit` | After first changes | Dispatches HTTP requests |
| `ngAfterViewInit` | Template views rendered | Initializes DOM widgets |
| `ngOnDestroy` | Before DOM removal | Cleans active subscriptions |""",
        "Angular's compiler lowers templates into view instructions, executing lifecycle hooks at strict boundary phases during change detection passes."
    ))

    # Q2: Parent-child lifecycle order
    qs.append(format_q(
        2,
        "What is the parent-child lifecycle hook execution order during creation and destruction?",
        ["Cognizant", "Infosys", "Capgemini", "Wells Fargo"],
        "Initialization runs top-down from parent to child, while view resolution runs bottom-up from child to parent.",
        "Component creation proceeds top-down from parent to child. The parent constructor and ngOnInit execute first, enabling child components to initialize their own state. Conversely, view rendering completes bottom-up from child to parent because parent views require rendered children. On destruction, teardown executes top-down to cleanly detach child trees. In one of my projects, understanding this order prevented undefined view query errors.",
        [
            ("Top-down creation", "parents initialize before child instances instantiate", True),
            ("Bottom-up view completion", "children finish view rendering before parents", True),
            ("Top-down teardown", "parents destroy before nested child components", True),
            ("ngAfterViewInit", "hook signaling template view is ready", False),
            ("View encapsulation", "scopes component styles to element boundaries", False)
        ],
        "Assembling a car: the chassis is framed first, then wheels attach, but final inspection happens only after wheels are mounted.",
        """// ❌ Bad: accessing child view in parent ngOnInit
ngOnInit(): void {
  this.childComponent.refresh(); // undefined!
}

// ✅ Good: access child view in ngAfterViewInit
ngAfterViewInit(): void {
  this.childComponent.refresh();
}""",
        "Why does child ngAfterViewInit run before parent ngAfterViewInit?",
        "A parent template view physically contains child views; a container cannot be fully rendered until all interior children complete rendering.",
        """| Phase | Order Direction | Execution Sequence |
| :--- | :--- | :--- |
| **Creation** | Top-down | Parent init then Child init |
| **View Ready** | Bottom-up | Child view then Parent view |
| **Destruction** | Top-down | Parent destroy then Child destroy |""",
        "Angular builds a view hierarchy tree; depth-first traversal evaluates parent initializers, descending to children before returning upward for view completion."
    ))

    # Q3: ngOnChanges vs ngOnInit vs ngDoCheck
    qs.append(format_q(
        3,
        "What is the difference between ngOnChanges, ngOnInit, and ngDoCheck?",
        ["TCS", "Wipro", "HCL", "Walmart"],
        "ngOnInit runs once on initialization; ngOnChanges fires on reference mutations; ngDoCheck runs on every change detection cycle.",
        "These three hooks handle component state tracking at different frequencies. `ngOnInit` executes exactly once when initial inputs are bound. `ngOnChanges` executes before ngOnInit and whenever input references mutate by identity. `ngDoCheck` runs on every single change detection cycle to allow custom dirty checking. Placing heavy algorithms inside ngDoCheck degrades rendering performance. In one of my projects, replacing ngDoCheck with computed signals eliminated unnecessary change detection cycles.",
        [
            ("ngOnInit", "executes once during component initialization", True),
            ("ngOnChanges", "fires when bound input references change", True),
            ("ngDoCheck", "runs during every change detection pass", True),
            ("Reference equality", "checks object pointers via Object.is", False),
            ("KeyValueDiffers", "utility for manual object property tracking", False)
        ],
        "ngOnInit is your morning alarm; ngOnChanges is a doorbell ringing on deliveries; ngDoCheck is a guard asking every minute if anything changed.",
        """// ❌ Bad: heavy calculation inside ngDoCheck
ngDoCheck(): void {
  this.runDeepObjectComparison(); // freezes UI!
}

// ✅ Good: use computed signal for state derivation
readonly total = computed(() => this.items().reduce((a, b) => a + b, 0));""",
        "Does ngOnChanges fire if an object property is mutated in place?",
        "No. ngOnChanges checks reference identity; mutating an object property keeps the same memory pointer, so ngOnChanges ignores it completely.",
        """| Hook | Execution Frequency | Primary Use Case |
| :--- | :--- | :--- |
| `ngOnInit` | Once per lifecycle | Service subscriptions & initial API |
| `ngOnChanges` | On input pointer change | Reacting to parent changes |
| `ngDoCheck` | Every change detection cycle | Custom manual dirty-checking |""",
        "Angular compares current and previous input pointers in the component's view node; if Object.is returns false, SimpleChanges emits."
    ))

    # Q4: ngAfterViewInit vs ngAfterContentInit & ExpressionChanged error
    qs.append(format_q(
        4,
        "What causes ExpressionChangedAfterItHasBeenCheckedError and when does ngAfterViewInit run?",
        ["Infosys", "Deloitte", "Cognizant", "TCS"],
        "It occurs when bindings mutate after verification; fix it by moving updates earlier or using signals.",
        "This error enforces Angular's unidirectional data flow rule in development mode. In development builds, Angular runs a second verification sweep after change detection. If any template binding value changed since the initial pass, it throws this error. It commonly occurs when child components modify parent properties inside `ngAfterViewInit`. The fix is moving logic to `ngOnInit` or managing updates via signals. In one of my projects, switching to signal inputs eliminated this error.",
        [
            ("Unidirectional data flow", "parent properties flow strictly downward to children", True),
            ("Verification sweep", "development check verifying template binding stability", True),
            ("ngAfterViewInit", "hook signaling template view DOM completion", True),
            ("queueMicrotask()", "schedules mutations in the next microtask turn", False),
            ("ChangeDetectorRef", "service controlling change detection execution", False)
        ],
        "A cashier checking your shopping cart totals, but a helper slips an item in after the receipt has printed.",
        """// ❌ Bad: mutating parent state after view check
ngAfterViewInit(): void {
  this.parent.title = 'Updated Title';
}

// ✅ Good: defer mutation to next microtask cycle
ngAfterViewInit(): void {
  queueMicrotask(() => this.parent.title.set('Updated'));
}""",
        "Why does ExpressionChangedAfterItHasBeenCheckedError only appear in development mode?",
        "The verification pass is disabled in production to maximize performance, but leaving the underlying race condition causes UI synchronization glitches.",
        """| Phase | Primary Pass | Verification Pass |
| :--- | :--- | :--- |
| **Check Mode** | Computes bindings | Compares previous values |
| **Action** | Updates DOM nodes | Throws error if mismatched |
| **Production** | Enabled | Stripped for speed |""",
        "ApplicationRef runs tick() with checkAndUpdate(), then runs checkNoChangesNode() in development to assert binding idempotency."
    ))

    # Q5: Signals Trio: signal(), computed(), effect()
    qs.append(format_q(
        5,
        "How do signal, computed, and effect work under the hood in modern Angular?",
        ["Accenture", "TCS", "Cognizant", "Capgemini"],
        "signal stores writable state, computed lazily caches derived values, and effect schedules side effects on microtasks.",
        "Angular Signals form a reactive dependency graph using producers and consumers. A `signal()` is a writable producer holding state that notifies downstream nodes on update. A `computed()` is a memoized derivation that evaluates lazily only when read. An `effect()` is a consumer that schedules side-effect execution on microtasks when dependencies change. Writing to signals inside effects is discouraged to prevent infinite cycles. In one of my projects, computed signals replaced twenty manual subscription calculations.",
        [
            ("signal()", "writable producer node holding reactive state", True),
            ("computed()", "lazily evaluated memoized derived signal", True),
            ("effect()", "microtask scheduled consumer executing side effects", True),
            ("Push-pull graph", "dirty flag propagation and lazy pulling", False),
            ("Reactive context", "execution frame tracking accessed signal producers", False)
        ],
        "signal is an Excel cell with a number; computed is a formula cell; effect is an email triggered when the total changes.",
        """// ❌ Bad: using effect to derive state
effect(() => {
  this.total.set(this.price() * this.qty());
}, { allowSignalWrites: true });

// ✅ Good: declarative derived state using computed
readonly total = computed(() => this.price() * this.qty());""",
        "Can a computed signal produce side effects like HTTP calls?",
        "No. Computed expressions must remain pure read-only functions with zero side effects; mutating state inside them triggers runtime errors.",
        """| Primitive | Node Role | Evaluation | Primary Purpose |
| :--- | :--- | :--- | :--- |
| `signal()` | Producer | Immediate | Holds state |
| `computed()` | Producer & Consumer | Lazy on read | Derived values |
| `effect()` | Consumer | Microtask queue | Side effects |""",
        "When a producer updates, it pushes dirty flags down the DAG. Dependent computed nodes recompute their value only when consumers pull them."
    ))

    # Q6: Array & Object State Mutations: .push() anti-pattern vs .set() and .update()
    qs.append(format_q(
        6,
        "Why is mutating an array with push an anti-pattern in Angular Signals?",
        ["Infosys", "Deloitte", "Wipro", "TCS"],
        "Signals check equality using Object.is; in-place array mutation preserves reference identity, preventing consumers from updating.",
        "Signals rely on equality checks [Object.is] to decide whether downstream consumers need invalidation. Calling `.push()` on an array mutates elements in place without changing the array reference pointer. Because the old and new references are identical, the signal drops notifications and dependent templates fail to re-render. To trigger updates, use `.update()` with the spread operator to return a new reference. In one of my projects, fixing direct mutations resolved missing shopping cart item updates.",
        [
            ("Object.is", "equality algorithm used for signal changes", True),
            ("Immutable update", "producing new references without in-place mutation", True),
            ("update()", "modifies signal value using a pure transformation", True),
            ("Reference equality", "evaluates memory address identity of objects", False),
            ("Consumer invalidation", "marking downstream nodes dirty on state change", False)
        ],
        "Direct push is writing in an old diary; immutable update is publishing a brand-new edition with fresh pages.",
        """// ❌ Bad: in-place mutation keeps old reference
this.items().push(newItem);
// UI never updates!

// ✅ Good: update returns a new array reference
this.items.update(list => [...list, newItem]);""",
        "How can you supply a custom equality comparison function to a signal?",
        "Pass an options object with an equal function: `signal(value, { equal: (a, b) => customComparison(a, b) })`.",
        """| Mutation Style | Reference Identity | Signal Notification |
| :--- | :--- | :--- |
| `.push()` | Identical (`prev === next`) | Dropped (No UI update) |
| `.update([...list])` | New reference (`prev !== next`) | Emitted (UI updates) |""",
        "Signal nodes run `equal(prevValue, nextValue)`. If true, the node returns without bumping its version or invalidating downstream consumers."
    ))

    # Q7: untracked() Signal Reads & Breaking Circular Cascades
    qs.append(format_q(
        7,
        "What is the purpose of untracked inside an effect or computed signal?",
        ["TCS", "Accenture", "Cognizant", "Persistent"],
        "untracked reads a signal value without registering it as a reactive dependency in the current context.",
        "Reading a signal inside a reactive context automatically adds that signal as a dependency edge. The `untracked()` function reads a signal value while preventing that signal from being tracked in the active context. Consequently, updates to the untracked signal will not trigger re-execution of the effect or computed. This breaks circular dependency cascades and prevents infinite loops. In one of my projects, untracked prevented infinite loops when logging analytics events alongside state updates.",
        [
            ("untracked()", "reads signal values without dependency registration", True),
            ("Reactive context", "execution scope tracking accessed signal producers", True),
            ("Circular dependency", "infinite loop caused by reciprocal signal triggers", True),
            ("Dynamic tracking", "registers dependencies accessed during branch execution", False),
            ("Version checking", "determines whether computed signals need re-evaluation", False)
        ],
        "Checking the wall clock while cooking without setting an alarm for every passing second.",
        """// ❌ Bad: effect re-runs when analytics counter updates
effect(() => {
  this.logMetrics(this.user(), this.counter());
});

// ✅ Good: reads counter without registering dependency
effect(() => {
  this.logMetrics(this.user(), untracked(() => this.counter()));
});""",
        "What happens if you mutate a signal inside an untracked block?",
        "Mutating a signal inside untracked still notifies downstream consumers; it only prevents the current context from listening to changes.",
        """| Context | Standard Read | untracked() Read |
| :--- | :--- | :--- |
| `computed()` | Creates dependency edge | Reads without edge |
| `effect()` | Re-runs on update | Ignores signal update |""",
        "untracked temporarily sets the current consumer context to null, reads the producer value, and restores the previous consumer context."
    ))

    # Q8: Modern Signal Inputs & Two-Way Binding: input(), input.required(), model()
    qs.append(format_q(
        8,
        "How do modern signal inputs and two-way model signals work in Angular?",
        ["Capgemini", "Infosys", "Deloitte", "TCS"],
        "input creates a read-only signal property, input.required enforces inputs at compile time, and model enables two-way synchronization.",
        "Modern Angular replaces traditional input decorators with functional signal primitives. The `input()` function creates a read-only signal property with optional transform functions. Using `input.required()` guarantees that parents provide values, failing compilation if missing. For two-way data binding, `model()` creates a writable signal that automatically emits change events back to the parent. In one of my projects, converting to model signals eliminated thirty manual event emitter definitions.",
        [
            ("input()", "read-only signal input property", True),
            ("input.required()", "mandates property at compile time", True),
            ("model()", "two-way synchronized writable signal", True),
            ("InputSignal", "internal type representing read-only signal inputs", False),
            ("Two-way binding", "synchronizes state across component boundaries", False)
        ],
        "input() is a read-only digital billboard; model() is a walkie-talkie connecting parent and child.",
        """// ❌ Bad: verbose decorator with EventEmitter pair
@Input() value = 0;
@Output() valueChange = new EventEmitter<number>();

// ✅ Good: single two-way model signal
readonly value = model(0);""",
        "Can a child component write directly to an input() signal using .set()?",
        "No. InputSignal is strictly read-only; calling .set() produces a compile-time error. Use model() when child mutations are needed.",
        """| Primitive | Direction | Writable by Child |
| :--- | :--- | :--- |
| `input()` | Parent to child | No (Compile error) |
| `input.required()` | Mandatory parent to child | No |
| `model()` | Bidirectional sync | Yes (`.set`, `.update`) |""",
        "The compiler transforms model() into an InputSignal paired with an implicit output emitter named with the 'Change' suffix."
    ))

    # Q9: Signals vs RxJS Observables: When to Use Which (State vs Events)
    qs.append(format_q(
        9,
        "When should you use Angular Signals versus RxJS Observables?",
        ["Accenture", "Cognizant", "TCS", "Wipro"],
        "Use Signals for synchronous state and template presentation; use RxJS for asynchronous events, timing, and stream composition.",
        "Signals and RxJS serve complementary architectural roles. Signals manage synchronous reactive state, powering template bindings and local component derivations with zero subscription boilerplate. RxJS Observables handle asynchronous event streams over time. Use RxJS when you need debounce timing, stream cancellation, or WebSocket coordination. Bridging between them is straightforward using `toSignal()` and `toObservable()`. In one of my projects, using signals for UI state eliminated fifty subscription handlers.",
        [
            ("Synchronous state", "always holds an active current value", True),
            ("Asynchronous stream", "sequence of discrete events over time", True),
            ("toSignal()", "bridges observable streams into reactive signals", True),
            ("toObservable()", "converts signal changes into an observable", False),
            ("Push-pull graph", "reactive graph architecture powering signals", False)
        ],
        "A signal is a gas gauge showing current fuel; an observable is the pump nozzle flowing fuel over time.",
        """// ❌ Bad: manual subscription to manage UI state
items$.subscribe(data => {
  this.items = data;
});

// ✅ Good: declarative signal conversion with automatic teardown
readonly items = toSignal(this.catalogService.items$, { initialValue: [] });""",
        "Can Signals completely replace RxJS in modern Angular applications?",
        "No. Signals lack temporal coordination operators like debounceTime, switchMap, and retry, which are essential for complex event streaming.",
        """| Dimension | Signals | RxJS Observables |
| :--- | :--- | :--- |
| **Value presence** | Always has current value | Emits only when events fire |
| **Timing** | Synchronous | Asynchronous over time |
| **Operators** | `computed`, `effect` | `debounce`, `switchMap`, `retry` |
| **Cleanup** | Automatic garbage collection | Requires unsubscription |""",
        "Signals lack a temporal dimension; they propagate values instantaneously across the graph, whereas Observables model event sequences across time."
    ))

    # Q10: Reactive Interop: toSignal() and toObservable()
    qs.append(format_q(
        10,
        "How do toSignal and toObservable work and what are their context restrictions?",
        ["Infosys", "Deloitte", "Capgemini", "TCS"],
        "toSignal and toObservable bridge reactive models, requiring an active injection context for automatic lifecycle management.",
        "Angular provides interop utilities in `@angular/core/rxjs-interop`. The `toSignal()` function subscribes to an observable and stores emissions in a signal. It must run inside an injection context to clean up the subscription when the host destroys. Conversely, `toObservable()` monitors a signal and emits changes into an observable stream via internal effects. Calling them outside constructors requires passing an `Injector` explicitly. In one of my projects, toSignal simplified consuming real-time notification streams.",
        [
            ("toSignal()", "converts observable stream into reactive signal", True),
            ("toObservable()", "converts signal state changes into observable", True),
            ("Injection context", "execution frame resolving dependencies and cleanup", True),
            ("initialValue", "configures fallback value before first emission", False),
            ("DestroyRef", "cleans underlying subscriptions on teardown", False)
        ],
        "toSignal is a digital picture frame displaying the latest broadcast photo; toObservable is a camera filming the frame changes.",
        """// ❌ Bad: calling toSignal outside injection context
setTimeout(() => {
  this.user = toSignal(this.user$); // NG0203 error!
});

// ✅ Good: declare toSignal in class field initializer
readonly user = toSignal(this.userService.user$);""",
        "What happens if an observable converted by toSignal() emits an error?",
        "By default, toSignal rethrows errors into the reactive graph, crashing subsequent reads unless configured with `rejectErrors: true`.",
        """| Utility | Source Type | Output Type | Default Teardown |
| :--- | :--- | :--- | :--- |
| `toSignal()` | Observable | Read-only Signal | Host component destruction |
| `toObservable()` | Signal | Observable stream | Unsubscribe or takeUntil |""",
        "toSignal subscribes immediately using an internal effect consumer, updating an internal writable signal and unsubscribing via DestroyRef."
    ))

    # Q11: Combining Observables: forkJoin vs combineLatest vs withLatestFrom
    qs.append(format_q(
        11,
        "How do forkJoin, combineLatest, and withLatestFrom differ in production use?",
        ["Cognizant", "Accenture", "TCS", "Persistent"],
        "forkJoin waits for all to complete; combineLatest emits on any source change; withLatestFrom samples on primary triggers.",
        "These combination operators handle multiple streams under different trigger policies. `forkJoin` waits for all source observables to complete and emits their final values in parallel. `combineLatest` emits whenever any source emits, provided every source has emitted at least once. `withLatestFrom` emits only when its master source emits, sampling current values from secondary observables. Selecting the wrong operator causes stale data or hung streams. In one of my projects, forkJoin parallelized multiple dashboard configuration requests.",
        [
            ("forkJoin", "waits for all source streams to complete", True),
            ("combineLatest", "emits latest values whenever any source updates", True),
            ("withLatestFrom", "samples secondary streams on master trigger emission", True),
            ("Completion requirement", "stream must complete before emitting in forkJoin", False),
            ("Cold observable", "stream producing values upon subscription", False)
        ],
        "forkJoin waits for everyone to finish exams; combineLatest updates scores on any goal; withLatestFrom takes a photo when the shutter clicks.",
        """// ❌ Bad: combineLatest when completion is required
combineLatest([httpA$, httpB$]).subscribe(res => {
  this.handleData(res);
});

// ✅ Good: forkJoin waits for completion
forkJoin({
  users: this.getUsers(),
  roles: this.getRoles()
}).subscribe();""",
        "What happens if one stream inside forkJoin throws an HTTP error?",
        "The entire forkJoin operation terminates immediately, discarding successful responses from all other sibling streams.",
        """| Operator | Trigger Rule | Requires Completion |
| :--- | :--- | :--- |
| `forkJoin` | All streams complete | Yes |
| `combineLatest` | Any stream emits | No |
| `withLatestFrom` | Master stream emits | No |""",
        "forkJoin maintains an internal buffer tracking the latest item of each stream, emitting the combined dictionary upon the final completion."
    ))

    # Q12: Component Communication: Decorators vs Modern Primitives
    qs.append(format_q(
        12,
        "How do modern component communication primitives compare to legacy decorators?",
        ["TCS", "Capgemini", "Infosys", "Wipro"],
        "Modern primitives replace decorators with type-safe signals, eliminating boilerplate and manual lifecycle synchronization.",
        "Legacy Angular used `@Input()` and `@Output()` decorators, requiring manual `ngOnChanges` checks to track incoming mutations. Modern Angular uses functional primitives: `input()`, `output()`, and `model()`. Signal inputs provide read-only reactive values that integrate directly into computed graphs. Event outputs use lightweight native dispatchers without EventEmitter class overhead. Two-way model signals eliminate separate property and event pairs. In one of my projects, converting to signal primitives reduced component code size by twenty percent.",
        [
            ("input()", "read-only signal input property", True),
            ("output()", "lightweight native event dispatcher", True),
            ("model()", "bidirectional synchronized writable signal", True),
            ("@Input() decorator", "legacy property binding decorator", False),
            ("EventEmitter", "legacy event dispatching utility class", False)
        ],
        "Legacy decorators were paper forms passed through committees; modern primitives are direct telephone lines between desks.",
        """// ❌ Bad: legacy decorator requiring ngOnChanges
@Input() filter = '';
ngOnChanges(c: SimpleChanges) { this.applyFilter(); }

// ✅ Good: modern signal input with computed derivation
readonly filter = input('');
readonly results = computed(() => this.filterData(this.filter()));""",
        "Can legacy decorators and modern signal primitives coexist in the same application?",
        "Yes. Angular supports incremental migration; components using signal inputs can interact seamlessly with components using legacy decorators.",
        """| Feature | Legacy Decorator | Modern Primitive |
| :--- | :--- | :--- |
| **Input Property** | `@Input()` | `input()` |
| **Output Event** | `@Output() = new EventEmitter()` | `output()` |
| **Two-Way Binding** | `@Input` + `@Output Change` | `model()` |
| **Type Safety** | Loose getter/setter | Strict Signal typing |""",
        "The compiler transforms input() declarations into ViewEngine instructions that link parent binding values directly to child reactive nodes."
    ))

    # Q13: ViewChild vs ContentChild & Static vs Dynamic Resolution
    qs.append(format_q(
        13,
        "What is the difference between ViewChild and ContentChild and how does static resolution work?",
        ["Cognizant", "Deloitte", "Persistent", "Accenture"],
        "ViewChild queries internal template elements, ContentChild queries projected markup, and static true resolves before change detection.",
        "DOM query mechanisms target different template locations. `ViewChild` inspects elements inside the component's own template, resolving in `ngAfterViewInit`. `ContentChild` inspects external elements projected via `<ng-content>`, resolving earlier in `ngAfterContentInit`. Setting `{ static: true }` resolves the query before change detection in `ngOnInit`, but fails if elements are gated by conditional blocks like `@if`. Modern `viewChild()` signals eliminate static flag confusion. In one of my projects, viewChild signals simplified accessing canvas elements.",
        [
            ("ViewChild", "queries internal template DOM nodes", True),
            ("ContentChild", "queries external projected content nodes", True),
            ("static: true", "resolves query before change detection in ngOnInit", True),
            ("viewChild()", "modern signal-based DOM query primitive", False),
            ("Content projection", "renders projected external markup slots", False)
        ],
        "ViewChild is checking the TV in your living room; ContentChild is inspecting luggage brought by a guest.",
        """// ❌ Bad: static true on conditional element
@ViewChild('modal', { static: true })
modal!: ElementRef; // fails if inside @if!

// ✅ Good: modern viewChild signal handles conditionals
readonly modal = viewChild<ElementRef>('modal');""",
        "What does a viewChild() signal return when an element is removed by an @if block?",
        "The viewChild signal reactively emits undefined when the DOM element unmounts, and emits the element reference when it re-renders.",
        """| Query Target | Resolution Hook | Works Inside @if |
| :--- | :--- | :--- |
| `ViewChild { static: true }` | `ngOnInit` | No |
| `ViewChild { static: false }` | `ngAfterViewInit` | Yes |
| `viewChild()` signal | Reactive on render | Yes |""",
        "Static queries resolve during component view creation, whereas dynamic queries re-run during embedded view container updates."
    ))

    # Q14: Cross-Component Communication: Signals State Service vs BehaviorSubject
    qs.append(format_q(
        14,
        "How do you architect cross-component communication using a Signals service versus BehaviorSubject?",
        ["TCS", "Infosys", "Capgemini", "Accenture"],
        "Use a singleton service with private writable signals, exposing read-only signals to prevent uncontrolled external mutations.",
        "Sharing state across unrelated components uses an injectable singleton service provided in root. In modern Angular, the service manages private writable signals internally. Public consumers access read-only signals via `.asReadonly()` to enforce unidirectional updates. This avoids BehaviorSubject boilerplate, subscription leaks, and extra pipe transformations. Components read signals directly in templates, triggering fine-grained updates. In one of my projects, a signal cart service eliminated thirty subscription handlers across checkout views.",
        [
            ("Singleton service", "centralized state container provided in root", True),
            ("asReadonly()", "exposes read-only signal view to consumers", True),
            ("Encapsulation", "restricting state mutations to service methods", True),
            ("BehaviorSubject", "legacy state container requiring manual unsubscribe", False),
            ("Fine-grained reactivity", "re-renders only dependent template bindings", False)
        ],
        "A bank vault where customers can view their balance through glass, but only teller methods can deposit funds.",
        """// ❌ Bad: exposing writable BehaviorSubject directly
public user$ = new BehaviorSubject<User | null>(null);

// ✅ Good: private writable signal with public read-only view
private readonly _user = signal<User | null>(null);
readonly user = this._user.asReadonly();""",
        "Why is exposing writable signals directly from a shared service considered an anti-pattern?",
        "Exposing writable signals allows arbitrary components to call `.set()`, bypassing validation logic and breaking predictable unidirectional state flow.",
        """| Criterion | Signal Service | BehaviorSubject Service |
| :--- | :--- | :--- |
| **Boilerplate** | Minimal | High |
| **Teardown** | Automatic | Requires unsubscription |
| **Derivations** | `computed()` | `pipe(map())` |
| **Template Reading** | Direct call `user()` | Requires `AsyncPipe` |""",
        "When an injected signal updates, Angular marks only the components whose templates read that signal dirty, avoiding broad tree checks."
    ))

    # Q15: RxJS Flattening Operators Mastery
    qs.append(format_q(
        15,
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
        """// ❌ Bad: mergeMap causes out-of-order responses
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

    # Q16: Real-World Typeahead Live Search
    qs.append(format_q(
        16,
        "How do you implement typeahead live search preventing race conditions and stream death?",
        ["Infosys", "Capgemini", "Accenture", "TCS"],
        "Use switchMap with debounceTime, distinctUntilChanged, and an inner catchError operator to keep the outer stream alive.",
        "A production typeahead search must handle rapid keystrokes, out-of-order responses, and API failures. We apply `debounceTime(300)` to wait for user typing to pause, and `distinctUntilChanged()` to skip duplicate terms. We use `switchMap` to cancel pending in-flight HTTP requests when new terms arrive. Critically, we place `catchError` inside the inner switchMap observable. Catching errors internally returns a fallback array, keeping the outer listener alive. In one of my projects, this architecture prevented search box lockups.",
        [
            ("switchMap", "cancels stale in-flight requests on new input", True),
            ("debounceTime", "delays emission until typing pauses for duration", True),
            ("Inner catchError", "recovers from network failures without stream termination", True),
            ("distinctUntilChanged", "ignores consecutive identical search terms", False),
            ("takeUntilDestroyed", "cleans subscription on component destruction", False)
        ],
        "A fast-food cashier taking only the newest order while dropping cancelled requests, without shutting down the counter on errors.",
        """// ❌ Bad: outer catchError permanently breaks input listener
search$.pipe(
  switchMap(q => this.http.get(`/items?q=${q}`)),
  catchError(() => of([])) // outer stream dies!
).subscribe();

// ✅ Good: inner catchError keeps outer stream alive
search$.pipe(
  switchMap(q => this.http.get(`/items?q=${q}`).pipe(catchError(() => of([]))))
).subscribe();""",
        "Why does placing catchError on the outer stream break subsequent search typing?",
        "When an observable stream errors, RxJS contracts mandate immediate termination; catching errors on the outer stream unsubscribes the input listener permanently.",
        """| Pipeline Step | Operator | Primary Responsibility |
| :--- | :--- | :--- |
| **1. Throttle typing** | `debounceTime(300)` | Prevents request storms |
| **2. Deduplicate** | `distinctUntilChanged()` | Skips identical queries |
| **3. Cancel stale** | `switchMap()` | Aborts in-flight calls |
| **4. Error boundary** | Inner `catchError()` | Keeps listener alive |""",
        "switchMap maintains an active subscription reference. On new emissions, it calls unsubscribe() on the active inner subscriber before subscribing to the new observable."
    ))

    # Q17: Preventing Double-Click Submissions: exhaustMap vs concatMap
    qs.append(format_q(
        17,
        "How do you prevent duplicate form submissions using exhaustMap versus sequential queueing with concatMap?",
        ["TCS", "Cognizant", "Deloitte", "Persistent"],
        "exhaustMap ignores clicks while an active request runs; concatMap queues clicks sequentially for ordered processing.",
        "Preventing duplicate submissions requires matching operator semantics to business requirements. `exhaustMap` ignores all subsequent button clicks while an existing request is pending. It drops accidental double-clicks automatically until the backend responds. Conversely, `concatMap` queues every submission in strict order. Use concatMap when every click represents a distinct operation that must be saved sequentially. In one of my projects, exhaustMap eliminated duplicate checkout orders during peak sale traffic.",
        [
            ("exhaustMap", "ignores incoming clicks while request is active", True),
            ("concatMap", "buffers and executes requests in strict sequence", True),
            ("Double-click prevention", "blocks duplicate requests from rapid user clicks", True),
            ("Idempotency", "ensuring duplicate requests do not alter system state", False),
            ("Inner completion", "signal releasing exhaustMap to accept new emissions", False)
        ],
        "exhaustMap is a locked voting booth while someone votes; concatMap is a post office queue where everyone waits their turn.",
        """// ❌ Bad: mergeMap sends duplicate concurrent orders
click$.pipe(
  mergeMap(() => this.orderService.submitOrder())
).subscribe();

// ✅ Good: exhaustMap ignores clicks until order finishes
click$.pipe(
  exhaustMap(() => this.orderService.submitOrder())
).subscribe();""",
        "What happens if an exhaustMap inner observable never completes?",
        "If the inner observable never completes, exhaustMap remains blocked forever, ignoring all future incoming click events permanently.",
        """| Operator | Incoming Event Behavior | Best Use Case |
| :--- | :--- | :--- |
| `exhaustMap` | Discards while busy | Login and payment buttons |
| `concatMap` | Queues in memory | Sequential logging or sync |
| `switchMap` | Aborts active request | Search and tab switching |""",
        "exhaustMap tracks an internal `hasSubscription` boolean. While true, incoming values are discarded without invocation of the project function."
    ))

    return qs
