#!/usr/bin/env python3
"""
Generator for 03_Angular_Signals_Basic_Interview.md adhering strictly to SSE-1.
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

def build_basic():
    header = """# 03. Modern Angular (v16–v18+), Signals & RxJS: Basic & Screening Interview Guide

> **Target Audience:** Frontend Developers and Full-Stack Engineers preparing for Technical Screening Rounds, Standard Frontend Interviews, and Fast Topic Revision.  
> **Philosophy:** Direct answers, intuitive real-life mental models, clear plain English explanations, zero cognitive overload, and practical production tips.

---

## Table of Contents
- [Part 1: Core Modern Angular & Signals Rapid Revision](#part-1-core-modern-angular--signals-rapid-revision)
  - [1.1 Standalone Components & Directives](#11-standalone-components--directives)
  - [1.2 Built-in Control Flow (@if, @for, @switch)](#12-built-in-control-flow-if-for-switch)
  - [1.3 Deferrable Views (@defer)](#13-deferrable-views-defer)
  - [1.4 Functional Dependency Injection via inject()](#14-functional-dependency-injection-via-inject)
  - [1.5 Angular Signals & The Reactive Trio](#15-angular-signals--the-reactive-trio)
  - [1.6 RxJS Flattening Operators](#16-rxjs-flattening-operators)
  - [1.7 Memory Leak Prevention & Teardown Mechanics](#17-memory-leak-prevention--teardown-mechanics)
  - [1.8 Change Detection Optimization (OnPush)](#18-change-detection-optimization-onpush)
  - [1.9 Functional Interceptors & Route Guards](#19-functional-interceptors--route-guards)
  - [1.10 Modern State Management with SignalStore](#110-modern-state-management-with-signalstore)
- [Part 2: Top 30 High-Frequency Angular Screening Questions & Answers](#part-2-top-30-high-frequency-angular-screening-questions--answers)
"""

    part1 = """
---

# Part 1: Core Modern Angular & Signals Rapid Revision

### 1.1 Standalone Components & Directives
Standalone components eliminate NgModule containers. Every component declares its own dependencies directly inside its `imports` array. This makes components self-contained, simpler to test, and enables dead-code elimination [tree-shaking] in modern bundlers.

### 1.2 Built-in Control Flow (@if, @for, @switch)
Modern Angular replaces structural directives (`*ngIf`, `*ngFor`) with compiler-level control blocks. The `@if` block handles branches natively, while `@for` mandates a tracking key [track] and offers an `@empty` block, eliminating wrapper allocations.

### 1.3 Deferrable Views (@defer)
Deferrable views split heavy component templates into separate JavaScript chunks. Angular loads these chunks lazily based on declarative browser triggers, including viewport visibility [viewport], user interaction [interaction], or browser idle time [idle].

### 1.4 Functional Dependency Injection via inject()
The `inject()` function resolves dependencies during class property initialization and functional route guards. It eliminates boilerplate constructors and resolves tokens within the active injection frame [injection context].

### 1.5 Angular Signals & The Reactive Trio
Signals provide fine-grained, synchronous reactivity. A `signal()` holds mutable state, `computed()` derives cached values lazily, and `effect()` schedules side effects on microtasks when dependencies change.

### 1.6 RxJS Flattening Operators
Higher-order observables require flattening strategies:
- `switchMap`: cancels stale in-flight requests, ideal for typeahead search.
- `mergeMap`: runs child streams concurrently in parallel, ideal for independent reads.
- `concatMap`: queues child streams in strict order, ideal for sequential writes.
- `exhaustMap`: ignores new emissions while active, ideal for login and submit buttons.

### 1.7 Memory Leak Prevention & Teardown Mechanics
Unclosed asynchronous subscriptions retain component references in memory. Modern Angular cleans them up automatically using `takeUntilDestroyed()`, `DestroyRef`, or declarative `toSignal()` bridges.

### 1.8 Change Detection Optimization (OnPush)
Default change detection checks the entire component tree on any asynchronous event. `ChangeDetectionStrategy.OnPush` prunes subtrees, re-checking only when input references change, signals update, or events fire inside the component.

### 1.9 Functional Interceptors & Route Guards
Angular replaces class-based middleware with lightweight functions (`HttpInterceptorFn`, `CanActivateFn`). They compose cleanly with `provideHttpClient(withInterceptors([...]))` and `provideRouter()`.

### 1.10 Modern State Management with SignalStore
NgRx SignalStore provides lightweight, modular state management. Each state slice is a signal; `computed` caches its result until an input changes. It eliminates actions and reducers while remaining fully tree-shakeable.

---

# Part 2: Top 30 High-Frequency Angular Screening Questions & Answers

"""

    questions = []

    # Q1
    q1 = format_q(
        1,
        "What are Angular component lifecycle hooks and what is their execution order?",
        ["TCS", "Infosys", "Cognizant", "Wipro"],
        "Angular lifecycle hooks run in a deterministic order from class creation to DOM teardown.",
        "Angular manages components through eight sequential lifecycle stages. The class constructor runs first for dependency injection. Next, input change detection [ngOnChanges] checks property bindings, followed by ngOnInit for initial data loading. Content projection and view rendering hooks execute next in order. Finally, teardown [ngOnDestroy] frees resources before DOM removal. In one of my projects, moving API calls to ngOnInit prevented blank screen initialization failures.",
        [
            ("ngOnInit", "runs once after input validation", True),
            ("ngOnChanges", "fires when input references mutate", True),
            ("ngOnDestroy", "cleans resources before DOM teardown", True),
            ("ngAfterViewInit", "fires when template views render", False),
            ("Unidirectional data flow", "prevents updates during render cycles", False)
        ],
        "Think of hotel guest check-in: register at desk, enter room, unpack luggage, inspect view, check out.",
        """// ❌ Bad: heavy call inside constructor
constructor(private http: HttpClient) {
  this.http.get('/users').subscribe();
}

// ✅ Good: dispatch initial calls in ngOnInit
ngOnInit(): void {
  this.userService.loadUsers();
}""",
        "Why avoid HTTP requests in the constructor?",
        "Inputs are undefined in the constructor, and it tightly couples class creation with networking, breaking isolated unit tests.",
        """| Hook | Timing | Purpose |
| :--- | :--- | :--- |
| `ngOnChanges` | Input reference changes | Validates bound data |
| `ngOnInit` | After first changes | Dispatches HTTP requests |
| `ngAfterViewInit` | Template view rendered | Initializes DOM widgets |
| `ngOnDestroy` | Before DOM removal | Cleans active subscriptions |""",
        "Angular compiles component templates into view definition nodes. The runtime traverses this tree top-down, invoking hooks at defined instruction boundaries."
    )
    questions.append(q1)

    # Q2
    q2 = format_q(
        2,
        "What is the difference between Angular Signals and RxJS Observables?",
        ["Accenture", "Capgemini", "Infosys", "Deloitte"],
        "Signals hold synchronous state with fine-grained tracking, while Observables stream asynchronous events over time.",
        "Signals represent synchronous values that always hold current state. They notify dependent consumers through a reactive dependency graph. RxJS Observables handle asynchronous event streams over time. Observables excel at cancellation, debounce timing, and WebSocket feeds. Signals do not replace RxJS; they work together. In one of my projects, converting view models to signals eliminated zone checking overhead across fifty dashboard widgets.",
        [
            ("Synchronous value", "always holds an active state", True),
            ("Event streams", "asynchronous data emissions over time", True),
            ("Push-pull graph", "efficient dependency notification and calculation", True),
            ("toSignal()", "bridges observable streams to signals", False),
            ("Fine-grained reactivity", "updates only affected DOM nodes", False)
        ],
        "A signal is a whiteboard showing today's temperature; an observable is a live radio broadcast of weather updates.",
        """// ❌ Bad: manual subscription to manage value
user$.subscribe(u => {
  this.user = u;
});

// ✅ Good: declarative signal conversion without boilerplate
readonly user = toSignal(this.userService.user$);""",
        "When should you still use RxJS instead of Signals?",
        "Use RxJS for event orchestration requiring time operators like debounce, switchMap cancellation, or multi-cast WebSocket streams.",
        """| Feature | Signals | RxJS Observables |
| :--- | :--- | :--- |
| **Data model** | Current synchronous value | Asynchronous stream over time |
| **Initial value** | Always present synchronously | May emit lazily later |
| **Operators** | computed, effect | debounce, switchMap, retry |
| **Teardown** | Automatic graph cleanup | Unsubscribe or takeUntilDestroyed |""",
        "Signals use a push-pull reactive graph. When a signal updates, dirty flags push forward, and consumers pull fresh values only on read."
    )
    questions.append(q2)

    # Q3
    q3 = format_q(
        3,
        "How do you pass data between parent and child components using modern primitives?",
        ["TCS", "Cognizant", "HCL", "Accenture"],
        "Modern Angular uses signal inputs [input()], event outputs [output()], and two-way models [model()].",
        "Modern Angular replaces traditional decorators with functional signal primitives. The `input()` function creates a read-only signal property. For mandatory attributes, `input.required()` guarantees values at compile time. Events dispatch through lightweight `output()` emitters without EventEmitter overhead. For two-way data binding, `model()` provides a writable signal synchronized with the parent. In one of my projects, migrating to signal inputs eliminated thirty manual ngOnChanges checks.",
        [
            ("input()", "read-only signal input property", True),
            ("output()", "lightweight native event emitter", True),
            ("model()", "two-way synchronized writable signal", True),
            ("input.required()", "mandates property at compile time", False),
            ("Two-way binding", "synchronizes state across boundaries", False)
        ],
        "input() is a read-only glass display; output() is a service bell; model() is a walkie-talkie between parent and child.",
        """// ❌ Bad: legacy decorator with ngOnChanges
@Input() count = 0;
@Output() countChange = new EventEmitter<number>();

// ✅ Good: modern two-way model signal
readonly count = model(0);""",
        "Can a child component write directly to an input() signal?",
        "No. An InputSignal is strictly read-only; attempting to set it triggers a compile error. Use model() for writable bindings.",
        """| Primitive | Direction | Mutability |
| :--- | :--- | :--- |
| `input()` | Parent to child | Read-only signal |
| `output()` | Child to parent | Event dispatcher |
| `model()` | Two-way sync | Writable signal |""",
        "The compiler transforms input() calls into SignalInput nodes, wiring parent bindings directly into the child component's reactive graph."
    )
    questions.append(q3)

    # Q4
    q4 = format_q(
        4,
        "What is the difference between ViewChild and ContentChild?",
        ["Wipro", "Infosys", "Tech Mahindra", "Capgemini"],
        "ViewChild queries internal template elements, while ContentChild queries external projected elements from ng-content.",
        "ViewChild queries elements located inside a component's own template. It resolves when template views render [ngAfterViewInit]. ContentChild queries elements projected from the parent through transclusion slots [ng-content]. It resolves earlier during content initialization [ngAfterContentInit]. Modern Angular provides signal-based queries via `viewChild()` and `contentChild()`. In one of my projects, querying modal footers via ContentChild enabled flexible customizable button actions.",
        [
            ("ViewChild", "queries internal template DOM nodes", True),
            ("ContentChild", "queries projected external transclusion nodes", True),
            ("Resolution timing", "content resolves before view renders", True),
            ("viewChild()", "signal-based modern view query", False),
            ("Content projection", "renders projected external markup slots", False)
        ],
        "ViewChild is inspecting the TV you bought inside your apartment; ContentChild is inspecting luggage brought by your guest.",
        """// ❌ Bad: accessing view elements before initialization
ngOnInit(): void {
  this.chart?.draw(); // undefined!
}

// ✅ Good: access after view materializes
ngAfterViewInit(): void {
  this.chart?.draw();
}""",
        "What happens if an element queried by ViewChild is hidden inside an @if block?",
        "If the condition is false, ViewChild returns undefined. Signal-based viewChild() automatically emits the element whenever it renders.",
        """| Query | Target | Hook Resolution |
| :--- | :--- | :--- |
| `ViewChild` | Internal template element | `ngAfterViewInit` |
| `ContentChild` | Projected `<ng-content>` element | `ngAfterContentInit` |
| `viewChild()` | Signal reactive element | Reactive signal value |""",
        "View queries traverse the component view hierarchy, while content queries traverse the light DOM nodes before projection into slots."
    )
    questions.append(q4)

    # Q5
    q5 = format_q(
        5,
        "What is the difference between structural directives and attribute directives?",
        ["Cognizant", "Accenture", "TCS", "Persistent"],
        "Structural directives add or destroy DOM layouts, while attribute directives alter appearance or behavior of existing elements.",
        "Structural directives modify layout by adding, removing, or replacing DOM elements. Historically they used the asterisk prefix like `*ngIf`. Modern Angular uses compiler-native control flow blocks instead. Attribute directives change element appearance or behavior without altering DOM structure. Examples include `ngClass`, `ngStyle`, or custom click listeners. In one of my projects, replacing `*ngFor` with `@for` and mandatory tracking keys eliminated repeated row recreations.",
        [
            ("Structural directive", "adds or removes DOM elements", True),
            ("Attribute directive", "modifies appearance of existing elements", True),
            ("track expression", "preserves identity during list diffing", True),
            ("ɵɵrepeater", "compiler instruction for modern loops", False),
            ("Control flow", "native blocks replacing directive overhead", False)
        ],
        "A structural directive adds or knocks down a wall; an attribute directive paints that wall blue.",
        """// ❌ Bad: unkeyed loop recreates entire DOM on changes
<div *ngFor="let item of items">
  {{ item.name }}
</div>

// ✅ Good: mandatory track expression preserves DOM nodes
@for (item of items(); track item.id) {
  <div>{{ item.name }}</div>
}""",
        "Why does modern @for mandate a track expression?",
        "Tracking keys allow Angular's list diffing algorithm to match array items with DOM nodes, preventing expensive element destructions on reorders.",
        """| Type | DOM Impact | Modern Syntax |
| :--- | :--- | :--- |
| **Structural** | Adds/removes elements | `@if`, `@for`, `@switch` |
| **Attribute** | Alters styling/behavior | `[class]`, custom directives |""",
        "Modern control flow lowers into native instructions like ɵɵconditional and ɵɵrepeater, bypassing directive class allocations completely."
    )
    questions.append(q5)

    # Q6
    q6 = format_q(
        6,
        "What is the difference between pure and impure pipes?",
        ["Infosys", "Deloitte", "LTIMindtree", "Wipro"],
        "Pure pipes execute only when input references change, while impure pipes execute on every change detection cycle.",
        "Angular pipes transform data within template expressions. A pure pipe executes only when its input argument changes by reference identity. Angular caches the pipe result to avoid repeated computations. An impure pipe runs during every change detection pass regardless of changes. Placing heavy calculations inside impure pipes causes frame drops and UI sluggishness. In one of my projects, replacing an impure search filter with a computed signal boosted scrolling to 60 FPS.",
        [
            ("Pure pipe", "executes only on primitive or reference changes", True),
            ("Impure pipe", "executes on every change detection cycle", True),
            ("Memoization", "caches output for identical input values", True),
            ("Change detection pass", "dirty check across the component tree", False),
            ("Reference equality", "checks identity using Object.is comparison", False)
        ],
        "A pure pipe is an exam results board updated only on new scores; an impure pipe is a clock ticking continuously.",
        """// ❌ Bad: impure pipe runs on every change cycle
@Pipe({ name: 'filter', pure: false })
export class BadFilterPipe implements PipeTransform {
  transform(items: Item[]): Item[] { return items; }
}

// ✅ Good: pure pipe evaluates only on reference change
@Pipe({ name: 'format', pure: true })
export class GoodFormatPipe implements PipeTransform {
  transform(val: string): string { return val.trim(); }
}""",
        "Why is an array filter pipe considered an anti-pattern?",
        "Pushing items to arrays does not change reference identity so pure pipes miss it, while impure pipes run on every keystroke, degrading performance.",
        """| Pipe Type | Execution Frequency | Default Setting |
| :--- | :--- | :--- |
| **Pure** | Only on input reference changes | `pure: true` (default) |
| **Impure** | Every change detection cycle | `pure: false` |""",
        "The compiler assigns a transform cache slot to pure pipes, evaluating them only when the input argument pointer diverges from the cached pointer."
    )
    questions.append(q6)

    # Q7
    q7 = format_q(
        7,
        "Explain Dependency Injection in Angular: providedIn root vs component-level providers.",
        ["TCS", "Accenture", "Capgemini", "Infosys"],
        "Root providers create application-wide tree-shakeable singletons, while component providers create instances scoped to that component's lifecycle.",
        "Angular features a hierarchical dependency injection system. Registering a service with `providedIn: 'root'` creates an application-wide singleton. It is fully tree-shakeable if unused in the bundle. Providing a service inside a component creates an isolated instance. That instance is shared with child components and destroyed when the parent unmounts. In one of my projects, providing editor state at the modal level guaranteed complete memory cleanup upon modal closure.",
        [
            ("providedIn: 'root'", "application-wide tree-shakeable singleton provider", True),
            ("Component providers", "scoped instance tied to component lifecycle", True),
            ("Hierarchical DI", "searches injectors from element upward to root", True),
            ("ElementInjector", "injector node assigned to a DOM element", False),
            ("Tree-shaking", "bundler eliminates unreferenced registered services", False)
        ],
        "Root provider is the building water tank shared by all; component provider is a personal water bottle in your desk drawer.",
        """// ❌ Bad: non-tree-shakeable module provider list
@NgModule({
  providers: [UserService]
})
export class AppModule {}

// ✅ Good: tree-shakeable root singleton declaration
@Injectable({ providedIn: 'root' })
export class UserService {}""",
        "What happens if both root and component declare the same service provider?",
        "The component and its children resolve the component-level instance, shadowing the root singleton for that template branch.",
        """| Provider Scope | Lifetime | Tree-Shakeable |
| :--- | :--- | :--- |
| `providedIn: 'root'` | Application lifecycle | Yes |
| `Component providers` | Component DOM lifetime | No |""",
        "Angular resolves dependencies by traversing the ElementInjector tree upward. If not found, it traverses the EnvironmentInjector hierarchy."
    )
    questions.append(q7)

    # Q8
    q8 = format_q(
        8,
        "What is Change Detection in Angular? Explain Default vs OnPush.",
        ["Cognizant", "Deloitte", "Persistent", "Capgemini"],
        "Default checks the entire component tree on any event; OnPush checks only when inputs mutate, signals update, or events fire.",
        "Change detection synchronizes component property states with the DOM view. Default strategy checks every single component whenever an asynchronous event occurs. This includes timers, clicks, and HTTP responses. The `OnPush` strategy skips unchanged component subtrees during change detection. It checks views only when input references change, signals update, or local event handlers fire. In one of my projects, enabling OnPush reduced rendering cycles by seventy percent.",
        [
            ("Default strategy", "checks all components on every asynchronous event", True),
            ("OnPush strategy", "skips clean subtrees to boost performance", True),
            ("markForCheck()", "flags ancestor path for change verification", True),
            ("Immutability", "creating new object references on update", False),
            ("Zone.js", "monkey-patches browser APIs to trigger detection", False)
        ],
        "Default is the colony watchman knocking on every single door; OnPush is the watchman checking only houses with delivery flags up.",
        """// ❌ Bad: default strategy runs on every unrelated event
@Component({
  template: `{{ calculateTotal() }}`
})
export class BadOrderComp {}

// ✅ Good: OnPush prunes checking unless input references change
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class GoodOrderComp {}""",
        "How do you manually notify Angular to check an OnPush component?",
        "Call `ChangeDetectorRef.markForCheck()` to mark the component and its ancestors dirty for the upcoming change detection pass.",
        """| Strategy | Trigger Conditions | Performance |
| :--- | :--- | :--- |
| **Default** | Any asynchronous macro/microtask | High overhead |
| **OnPush** | New input, signal, or event | Optimized |""",
        "OnPush components have their ViewFlags checked. If no dirty bit is set, the runtime skips traversing that component and all its children."
    )
    questions.append(q8)

    # Q9
    q9 = format_q(
        9,
        "Explain RxJS flattening operators: switchMap, mergeMap, concatMap, and exhaustMap.",
        ["TCS", "Infosys", "Accenture", "Wipro"],
        "Flattening operators transform higher-order streams: switchMap cancels, mergeMap parallels, concatMap queues, and exhaustMap ignores.",
        "Flattening operators subscribe to inner observables and merge results back. We select them based on exact business concurrency needs: `switchMap` cancels stale inner requests, making it ideal for typeahead search. `mergeMap` runs inner streams concurrently in parallel, ideal for independent reads. `concatMap` queues inner streams in strict order, ideal for sequential writes. `exhaustMap` ignores new triggers while an inner stream is active, ideal for login buttons. In one of my projects, exhaustMap stopped duplicate order submissions.",
        [
            ("switchMap", "cancels stale in-flight streams for search", True),
            ("mergeMap", "runs parallel independent child requests concurrently", True),
            ("concatMap", "queues streams in sequential FIFO order", True),
            ("exhaustMap", "ignores new inputs until current completes", False),
            ("Higher-order observable", "an observable that emits inner observables", False)
        ],
        "switchMap is changing TV channels; mergeMap is cooking multi-burner dishes; concatMap is supermarket billing; exhaustMap is an occupied restroom.",
        """// ❌ Bad: mergeMap causes out-of-order search responses
query$.pipe(
  mergeMap(q => this.http.get(`/search?q=${q}`))
);

// ✅ Good: switchMap cancels stale pending search requests
query$.pipe(
  switchMap(q => this.http.get(`/search?q=${q}`))
);""",
        "Which operator would you choose for file uploads and why?",
        "Use concatMap if uploads must finish in strict sequence, or mergeMap with a concurrency limit for parallel throughput.",
        """| Operator | Concurrency Rule | Primary Use Case |
| :--- | :--- | :--- |
| `switchMap` | Cancels active inner stream | Typeahead search |
| `mergeMap` | Runs parallel concurrently | Independent reads |
| `concatMap` | Queues in sequential order | Financial transactions |
| `exhaustMap` | Ignores incoming while busy | Submit & login buttons |""",
        "Higher-order operators manage inner subscription references, handling inner completion signals and outer unsubscriptions according to operator policy."
    )
    questions.append(q9)

    # Q10
    q10 = format_q(
        10,
        "How do you implement lazy loading and functional route guards in modern Angular?",
        ["Capgemini", "Cognizant", "Deloitte", "TCS"],
        "Modern Angular lazy loads components using loadComponent and protects routes using functional CanActivateFn guards.",
        "Modern routing removes module files in favor of standalone routes. We lazy load components using `loadComponent` with dynamic import statements. This splits routes into isolated JavaScript bundles downloaded on demand. Route protection uses functional guards [CanActivateFn] with `inject()`. Guards return booleans or atomic UrlTree redirects directly. In one of my projects, converting module routing to standalone lazy routes reduced initial bundle size by forty percent.",
        [
            ("loadComponent", "lazy loads standalone component JavaScript chunks", True),
            ("CanActivateFn", "functional route guard checking route access", True),
            ("UrlTree", "atomic router redirect target representation", True),
            ("Code splitting", "bundler splits route chunks for lazy loading", False),
            ("inject()", "resolves authentication services within guard context", False)
        ],
        "Lazy loading is ordering food courses sequentially; a functional guard is a restaurant host checking reservations before seating.",
        """// ❌ Bad: legacy class-based guard with CanActivate
@Injectable()
export class AuthGuard implements CanActivate {}

// ✅ Good: functional guard returning an atomic UrlTree
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  return auth.isLoggedIn() ? true : inject(Router).createUrlTree(['/login']);
};""",
        "Why is returning a UrlTree preferred over calling router.navigate() inside a guard?",
        "Returning a UrlTree executes an atomic redirect that avoids competing navigation lifecycles, preserving clean browser navigation history.",
        """| Modern Routing Feature | Replaced Legacy Feature | Advantage |
| :--- | :--- | :--- |
| `loadComponent` | `loadChildren` with NgModule | Granular chunking |
| `CanActivateFn` | `CanActivate` class interface | Zero class boilerplate |
| `UrlTree` return | `router.navigate()` in guard | Atomic redirect |""",
        "When the router navigates, it executes guards inside the route EnvironmentInjector before resolving the lazy-loaded chunk promise."
    )
    questions.append(q10)

    # Q11
    q11 = format_q(
        11,
        "Explain Reactive Forms vs Template-Driven Forms and custom validation.",
        ["Infosys", "Wipro", "TCS", "Accenture"],
        "Reactive Forms offer synchronous, programmatic form control models, while Template-Driven Forms rely on template directives.",
        "Reactive Forms build an explicit, programmatic form tree in TypeScript using FormControl, FormGroup, and FormArray. They offer synchronous access to values, typed controls, and unit testability. Template-driven forms rely on template directives like `ngModel` and asynchronous binding. Custom validators are pure functions returning validation error objects or null. Async validators return observable validation objects. In one of my projects, typed Reactive Forms caught invalid payload shapes during compilation.",
        [
            ("FormControl", "tracks individual form field value and status", True),
            ("FormGroup", "aggregates collection of child form controls", True),
            ("ValidatorFn", "pure function checking synchronous field validity", True),
            ("AsyncValidatorFn", "asynchronous validator returning an observable", False),
            ("Typed forms", "provides compile-time type safety for controls", False)
        ],
        "Reactive forms are an architect's blueprint drawn on paper; template forms are assembling a tent directly on site.",
        """// ❌ Bad: untyped loose form control declaration
const name = new FormControl('');

// ✅ Good: typed non-nullable form control with validator
const name = new FormControl('', {
  nonNullable: true,
  validators: [Validators.required]
});""",
        "What is the difference between setValue() and patchValue()?",
        "setValue() enforces strict object structure and throws an error if any field is missing; patchValue() updates partial properties safely.",
        """| Feature | Reactive Forms | Template-Driven Forms |
| :--- | :--- | :--- |
| **Model setup** | Programmatic in TypeScript | Declarative in template |
| **Data flow** | Synchronous | Asynchronous |
| **Type safety** | Strict compile-time typing | Loose template typing |
| **Testability** | Unit testable without DOM | Requires DOM rendering |""",
        "Form controls extend AbstractControl, maintaining status flags like VALID, INVALID, DIRTY, and TOUCHED, emitting changes on valueChanges observables."
    )
    questions.append(q11)

    # Q12
    q12 = format_q(
        12,
        "How do HTTP Interceptors work in modern Angular and how do you inject JWT tokens?",
        ["Cognizant", "Capgemini", "Accenture", "Persistent"],
        "Functional HTTP interceptors clone outgoing requests to attach headers and catch error responses globally.",
        "Modern Angular uses functional interceptors [HttpInterceptorFn] registered through `provideHttpClient(withInterceptors([...]))`. Because HTTP requests are immutable objects, interceptors clone the request and attach Authorization bearer headers. They invoke `next(clonedReq)` to proceed through the handler pipeline. Response errors like 401 Unauthorized are intercepted using the RxJS `catchError` operator. In one of my projects, a functional interceptor attached tokens and redirected unauthenticated users seamlessly.",
        [
            ("HttpInterceptorFn", "functional middleware intercepting HTTP traffic", True),
            ("Request cloning", "mutating headers via immutable request clone", True),
            ("JWT bearer token", "authentication token header for API security", True),
            ("withInterceptors", "registers functional interceptors in client provider", False),
            ("HttpHandlerFn", "passes modified requests down the pipeline", False)
        ],
        "An HTTP interceptor is a postal clerk stamping a security seal onto every outgoing envelope before shipping.",
        """// ❌ Bad: legacy class-based HttpInterceptor with NgModule
@Injectable()
export class AuthInterceptor implements HttpInterceptor {}

// ✅ Good: modern functional interceptor cloning bearer token
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).getToken();
  return next(token ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } }) : req);
};""",
        "Why must you clone an HttpRequest instead of modifying headers directly?",
        "HttpRequest objects are immutable to allow safe retries and avoid race conditions when multiple interceptors inspect the same request.",
        """| Interceptor Style | Registration | Boilerplate |
| :--- | :--- | :--- |
| **Class-based** | `HTTP_INTERCEPTORS` multi-token | High class ceremony |
| **Functional** | `withInterceptors([fn])` | Minimal composable function |""",
        "Functional interceptors chain as an onion-style pipeline. The final handler invokes the platform XMLHttpRequest or Fetch backend."
    )
    questions.append(q12)

    # Q13
    q13 = format_q(
        13,
        "What causes memory leaks in Angular applications and how do you prevent them?",
        ["TCS", "Infosys", "Deloitte", "Wipro"],
        "Memory leaks stem from unclosed subscriptions and uncleared intervals; fix them using takeUntilDestroyed or signals.",
        "Memory leaks occur when long-lived services or event streams retain references to destroyed component instances. Unclosed RxJS subscriptions, uncancelled setInterval timers, and global window listeners prevent garbage collection. Modern Angular prevents leaks using `takeUntilDestroyed()`, which ties subscription lifecycles to component destruction. Alternatively, converting streams to signals with `toSignal()` automatically handles teardown. In one of my projects, adding takeUntilDestroyed eliminated retained DOM leaks on modal closures.",
        [
            ("takeUntilDestroyed()", "unsubscribes automatically when component destroys", True),
            ("DestroyRef", "functional teardown hook replacing ngOnDestroy", True),
            ("Detached DOM tree", "DOM nodes retained in memory by closures", True),
            ("toSignal()", "bridges observables to signals with cleanup", False),
            ("Garbage collection", "browser memory reclamation for unreachable objects", False)
        ],
        "An unclosed subscription is an ongoing magazine subscription delivering to an empty house after you move away.",
        """// ❌ Bad: unmanaged subscription leaks component reference
ngOnInit(): void {
  this.userService.data$.subscribe();
}

// ✅ Good: automatic teardown tied to injection context
private readonly data = toSignal(this.userService.data$);""",
        "Do HTTP requests from HttpClient cause memory leaks if left unsubscribed?",
        "HttpClient observables emit once and complete automatically, releasing references; however, uncompleted responses can still execute on unmounted components.",
        """| Teardown Approach | Lifecycle Anchor | Boilerplate |
| :--- | :--- | :--- |
| `takeUntilDestroyed()` | Current `DestroyRef` | Zero manual hooks |
| `toSignal()` | Injection context | Built-in teardown |
| `AsyncPipe` | Template DOM lifetime | Automatic |
| `ngOnDestroy` manual | Component teardown | High manual risk |""",
        "When an outer observable retains an inner subscriber callback referencing `this`, the V8 engine marks the entire component closure reachable."
    )
    questions.append(q13)

    # Q14
    q14 = format_q(
        14,
        "What is the exact difference between signal, computed, and effect?",
        ["Accenture", "Cognizant", "Capgemini", "Infosys"],
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
    )
    questions.append(q14)

    # Q15
    q15 = format_q(
        15,
        "Why is mutating a Signal array directly with push an anti-pattern?",
        ["TCS", "Wipro", "Tech Mahindra", "Capgemini"],
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
    )
    questions.append(q15)

    # Q16
    q16 = format_q(
        16,
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
    )
    questions.append(q16)

    # Q17
    q17 = format_q(
        17,
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
    )
    questions.append(q17)

    # Q18
    q18 = format_q(
        18,
        "How do forkJoin, combineLatest, and withLatestFrom differ?",
        ["Cognizant", "Infosys", "Deloitte", "Capgemini"],
        "forkJoin waits for all streams to complete; combineLatest emits on any update; withLatestFrom samples secondary streams on primary emission.",
        "These combination operators handle multiple streams with different emission rules. `forkJoin` waits for all input observables to complete and emits their last values, acting like `Promise.all`. `combineLatest` emits whenever any source emits, provided every source has emitted at least once. `withLatestFrom` emits only when the master source emits, sampling current values from secondary streams. In one of my projects, forkJoin parallelized three independent configuration API calls on startup.",
        [
            ("forkJoin", "waits for all source streams to complete", True),
            ("combineLatest", "emits latest values whenever any source updates", True),
            ("withLatestFrom", "samples secondary streams on master trigger emission", True),
            ("Promise.all", "JavaScript promise combination equivalent to forkJoin", False),
            ("Cold observable", "stream that begins producing data upon subscription", False)
        ],
        "forkJoin is waiting for all team members to arrive before leaving; combineLatest is updating a score display whenever anyone scores.",
        """// ❌ Bad: sequential subscriptions delay startup
this.getA().subscribe(() => {
  this.getB().subscribe();
});

// ✅ Good: parallel execution with forkJoin
forkJoin({ a: this.getA(), b: this.getB() }).subscribe();""",
        "What happens if one source stream inside forkJoin throws an error?",
        "The entire forkJoin operation aborts immediately and errors out, dropping values from any other completed sibling streams.",
        """| Operator | Trigger Condition | Requires Completion |
| :--- | :--- | :--- |
| `forkJoin` | All sources complete | Yes |
| `combineLatest` | Any source emits new value | No |
| `withLatestFrom` | Master stream emits | No |""",
        "forkJoin buffers the latest emission of each stream. When its completion countdown hits zero, it emits the aggregated array and completes."
    )
    questions.append(q18)

    # Q19
    q19 = format_q(
        19,
        "What is the difference between Subject, BehaviorSubject, and ReplaySubject?",
        ["TCS", "Accenture", "LTIMindtree", "Persistent"],
        "Subject has no initial value; BehaviorSubject requires an initial value and retains one; ReplaySubject replays n past values.",
        "RxJS subjects act as both observable event emitters and observer consumers. A plain `Subject` emits only future events to subscribers; late subscribers receive nothing. A `BehaviorSubject` requires an initial seed value, holds its current value, and immediately replays it to new subscribers. A `ReplaySubject` buffers a specified number of historical emissions, replaying them to new subscribers regardless of timing. In one of my projects, BehaviorSubject shared authenticated user states across routes.",
        [
            ("Subject", "multicast observable without historical value storage", True),
            ("BehaviorSubject", "stores current value and requires an initial seed", True),
            ("ReplaySubject(n)", "buffers and replays specified past emissions", True),
            ("getValue()", "synchronously reads current value of BehaviorSubject", False),
            ("Multicasting", "distributes single emission to multiple subscriber observers", False)
        ],
        "Subject is live radio; BehaviorSubject is a digital clock showing current time; ReplaySubject is DVR recording past shows.",
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
| `BehaviorSubject` | Yes | Most recent value |
| `ReplaySubject(n)` | No | Past `n` emitted values |""",
        "BehaviorSubject overrides `_subscribe` to call `next()` immediately with its internal `_value` buffer before registering the observer."
    )
    questions.append(q19)

    # Q20
    q20 = format_q(
        20,
        "How do you share state between unrelated components using modern Angular?",
        ["Infosys", "Cognizant", "Capgemini", "Deloitte"],
        "Share state using a singleton injectable service containing signals, exposing read-only signals for consumption.",
        "Sharing state across unrelated components in modern Angular uses an injectable service provided in root. Inside the service, private writable signals hold mutable state. Public properties expose read-only signals using `.asReadonly()` to prevent external mutations. Components inject the service using `inject()` and read signals directly in templates. This approach eliminates BehaviorSubject boilerplate and manual unsubscriptions. In one of my projects, a signal cart service synchronized navigation badge counts seamlessly.",
        [
            ("Singleton service", "centralized state container provided in root", True),
            ("asReadonly()", "exposes read-only signal view to consumers", True),
            ("inject()", "functional resolution of state services", True),
            ("Encapsulation", "restricting state mutations to service methods", False),
            ("Fine-grained reactivity", "re-renders only dependent template bindings", False)
        ],
        "A shared state service is a central bank vault; components can check their balance anytime, but only teller methods can update funds.",
        """// ❌ Bad: exposing writable BehaviorSubject publicly
public count$ = new BehaviorSubject(0);

// ✅ Good: private writable signal with public read-only view
private readonly _cart = signal<CartItem[]>([]);
readonly cart = this._cart.asReadonly();""",
        "What is the risk of exposing a writable signal directly from a shared service?",
        "Any consuming component could mutate state arbitrarily using `.set()`, bypassing business validation and breaking predictable state management.",
        """| Pattern | Boilerplate | Auto-Teardown |
| :--- | :--- | :--- |
| **Signal Service** | Minimal | Automatic |
| **BehaviorSubject Service** | Moderate | Requires unsubscribe |
| **Classic NgRx Store** | High | Automatic via selectors |""",
        "When an injected signal updates, Angular marks only the components whose templates read that signal dirty, avoiding broad tree checks."
    )
    questions.append(q20)

    # Q21
    q21 = format_q(
        21,
        "What is the purpose of untracked inside an effect or computed signal?",
        ["TCS", "Accenture", "Cognizant", "Wipro"],
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
    )
    questions.append(q21)

    # Q22
    q22 = format_q(
        22,
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
    )
    questions.append(q22)

    # Q23
    q23 = format_q(
        23,
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
    )
    questions.append(q23)

    # Q24
    q24 = format_q(
        24,
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
    )
    questions.append(q24)

    # Q25
    q25 = format_q(
        25,
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
    )
    questions.append(q25)

    # Q26
    q26 = format_q(
        26,
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
    )
    questions.append(q26)

    # Q27
    q27 = format_q(
        27,
        "What is the difference between take(1), first(), and single() in RxJS?",
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
| `first()` | Throws `EmptyError` | Emits & completes | Emits first & completes |
| `single()` | Throws `EmptyError` | Emits & completes | Throws error |""",
        "take(1) decrements an internal counter and unsubscribes from the source observable synchronously upon receiving its first item."
    )
    questions.append(q27)

    # Q28
    q28 = format_q(
        28,
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
    )
    questions.append(q28)

    # Q29
    q29 = format_q(
        29,
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
    )
    questions.append(q29)

    # Q30
    q30 = format_q(
        30,
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
    )
    questions.append(q30)

    footer = """## Summary Cheatsheet: Modern Angular Anti-Pattern vs Clean Pattern

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
    with open('/home/ubermensch/Desktop/interview/03_Angular_Signals_Basic_Interview.md', 'w', encoding='utf-8') as f:
        f.write(full_text)
    print("03_Angular_Signals_Basic_Interview.md successfully generated!")

if __name__ == '__main__':
    build_basic()
