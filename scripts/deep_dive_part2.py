#!/usr/bin/env python3
"""
Deep Dive Part 2: Modules 6 to 10 (Q18 to Q28)
"""
from generate_deep_dive import format_q

def get_part2_questions():
    qs = []

    # Q18: Default vs OnPush & Immutability
    qs.append(format_q(
        18,
        "Why is immutability mandatory when using ChangeDetectionStrategy.OnPush in Angular?",
        ["TCS", "Accenture", "Cognizant", "Infosys"],
        "OnPush checks input references using Object.is; in-place mutations keep the same reference, so Angular skips re-rendering.",
        "Change detection verifies whether component bindings require DOM updates. The Default strategy checks every single component whenever any asynchronous event occurs. `ChangeDetectionStrategy.OnPush` prunes clean component subtrees from change detection sweeps. It checks an OnPush component only when input references change, signals update, or local event listeners fire. Because OnPush uses reference equality [Object.is], in-place object mutations are ignored. In one of my projects, adopting OnPush reduced change detection cycles by seventy percent.",
        [
            ("OnPush strategy", "prunes component subtrees from change detection passes", True),
            ("Reference equality", "evaluates memory address identity of objects", True),
            ("Immutability", "producing new references without in-place mutation", True),
            ("markForCheck()", "flags component and ancestors for change verification", False),
            ("Subtree pruning", "skipping unchanged branches during change detection", False)
        ],
        "Default is checking every room in a hotel; OnPush is checking only rooms that hung a cleaning sign outside.",
        """// ❌ Bad: mutating object skips OnPush check
this.user.name = 'Vikram';
// UI fails to update!

// ✅ Good: produce new reference using spread operator
this.user = { ...this.user, name: 'Vikram' };""",
        "What triggers change detection in an OnPush component besides new input references?",
        "Local template DOM events, emitted signals read in the template, and manual calls to `markForCheck()` or `detectChanges()`.",
        """| Strategy | Checking Frequency | Dependency On Immutability |
| :--- | :--- | :--- |
| **Default** | Every asynchronous macro/microtask | Low (dirty checks properties) |
| **OnPush** | Inputs change, signals update, events | Mandatory (checks references) |""",
        "The runtime checks the component ViewFlags. If OnPush is set and no dirty flag is present, the entire component view traversal is skipped."
    ))

    # Q19: ChangeDetectorRef Mechanics
    qs.append(format_q(
        19,
        "How do markForCheck, detectChanges, detach, and reattach differ in ChangeDetectorRef?",
        ["Infosys", "Capgemini", "Deloitte", "Persistent"],
        "markForCheck schedules ancestor verification; detectChanges runs immediate local detection; detach disconnects views from the change detection tree.",
        "ChangeDetectorRef controls change detection execution programmatically. `markForCheck()` flags the component and all its ancestors dirty for the upcoming change detection sweep. `detectChanges()` runs immediate change detection synchronously on the component and its children. `detach()` disconnects a component view from change detection passes, useful for high-frequency data streams. `reattach()` restores the view to the tree when updates complete. In one of my projects, detaching canvas views during animations prevented browser thread lag.",
        [
            ("markForCheck()", "flags ancestor path dirty for upcoming check", True),
            ("detectChanges()", "runs synchronous immediate change detection locally", True),
            ("detach()", "disconnects view from change detection passes", True),
            ("reattach()", "re-links detached view back into detection tree", False),
            ("ViewRef", "internal representation of component view node", False)
        ],
        "markForCheck raises a flag for the postal worker; detectChanges delivers the letter immediately; detach unplugs the mailbox.",
        """// ❌ Bad: detectChanges inside loops causes UI lag
items.forEach(() => {
  this.cdr.detectChanges();
});

// ✅ Good: markForCheck schedules single coordinated sweep
this.cdr.markForCheck();""",
        "Can detectChanges() trigger ExpressionChangedAfterItHasBeenCheckedError in development mode?",
        "Yes. Calling detectChanges() synchronously inside lifecycle hooks like ngAfterViewInit can trigger this error if properties mutate afterwards.",
        """| Method | Execution Timing | Tree Scope |
| :--- | :--- | :--- |
| `markForCheck()` | Next tick cycle | Ancestors to current |
| `detectChanges()` | Immediate synchronous | Current view and children |
| `detach()` | Permanent until reattach | Current view and children |
| `reattach()` | Restores view | Current view and children |""",
        "markForCheck iterates up the parent view hierarchy setting `ViewFlags.Dirty`. ApplicationRef.tick() traverses down, checking marked branches."
    ))

    # Q20: Modern Zoneless Angular vs NgZone
    qs.append(format_q(
        20,
        "How does modern Zoneless Angular compare to NgZone.runOutsideAngular?",
        ["Accenture", "TCS", "Cognizant", "Wipro"],
        "Zoneless uses signals to schedule microtask sweeps without Zone.js monkey-patching; runOutsideAngular bypasses Zone.js selectively.",
        "Zone.js monkey-patches browser asynchronous APIs to trigger full-tree change detection whenever promises, timers, or events fire. This introduces bundle overhead and broad re-checking passes. Historically, developers used `NgZone.runOutsideAngular()` to escape Zone.js for high-frequency events. Modern Angular introduces experimental zoneless mode via `provideExperimentalZonelessChangeDetection()`. In zoneless mode, Signal notifications schedule microtask updates directly without Zone.js. In one of my projects, enabling zoneless eliminated Zone.js overhead from fifty dashboard charts.",
        [
            ("Zoneless Angular", "change detection without Zone.js monkey-patching", True),
            ("NgZone.runOutsideAngular()", "runs code without triggering change detection", True),
            ("Microtask scheduler", "batches signal notifications into single browser frames", True),
            ("Monkey-patching", "runtime modification of native browser APIs", False),
            ("provideExperimentalZonelessChangeDetection()", "enables zoneless change detection in bootstrap", False)
        ],
        "Zone.js is a colony siren sounding on every car arrival; Zoneless is private text alerts sent only to the receiving house.",
        """// ❌ Bad: high-frequency canvas updates inside Angular zone
window.addEventListener('mousemove', () => this.draw());

// ✅ Good: run outside zone to avoid detection
this.ngZone.runOutsideAngular(() => {
  window.addEventListener('mousemove', () => this.draw());
});""",
        "What happens if you mutate a plain class property in a zoneless Angular application?",
        "In zoneless mode, plain property mutations do not trigger change detection; you must use signals or call markForCheck explicitly.",
        """| Feature | Zone.js Architecture | Modern Zoneless Architecture |
| :--- | :--- | :--- |
| **API Patching** | Monkey-patches window APIs | Pure native browser APIs |
| **Trigger Mechanism** | Any macro/microtask completion | Signals and explicit events |
| **Bundle Impact** | Adds ~35 KB (Zone.js payload) | Zero Zone.js bundle overhead |
| **Debugging** | Deep patched stack traces | Clean native stack traces |""",
        "In zoneless mode, signal notifications push dirty states to an internal scheduler that coalesces updates into `queueMicrotask()`."
    ))

    # Q21: Structural Directives vs Modern Control Flow
    qs.append(format_q(
        21,
        "How does modern built-in control flow outperform legacy structural directives?",
        ["TCS", "Infosys", "Capgemini", "Deloitte"],
        "Built-in control flow compiles directly into native runtime instructions, eliminating directive wrappers and enabling compile-time type narrowing.",
        "Legacy Angular used structural directives like `*ngIf`, `*ngFor`, and `*ngSwitch`. They required instantiating dynamic directive classes, creating ViewContainerRef containers, and allocating embedded views. Modern Angular replaces them with compiler-native control flow: `@if`, `@for`, and `@switch`. Built-in control flow lowers directly into instructions like `ɵɵconditional` and `ɵɵrepeater`. It enforces mandatory tracking keys and enables TypeScript type narrowing in template branches. In one of my projects, modern control flow cut list rendering times by half.",
        [
            ("Built-in control flow", "compiler-native template branching and looping syntax", True),
            ("track expression", "mandates unique identity key for list diffing", True),
            ("Type narrowing", "TypeScript narrows union types within @if branches", True),
            ("ɵɵrepeater", "compiler instruction executing optimized list diffing", False),
            ("ViewContainerRef", "legacy container dynamically inserting embedded views", False)
        ],
        "Legacy directives were outside contractors hired to build partitions; modern control flow is sliding partition doors built into walls.",
        """// ❌ Bad: legacy loop without trackBy destroys DOM nodes
<div *ngFor="let item of items">{{ item.name }}</div>

// ✅ Good: modern @for with mandatory compile-time track
@for (item of items(); track item.id) {
  <div>{{ item.name }}</div>
} @empty {
  <p>No items found.</p>
}""",
        "Why does modern @for provide an @empty block?",
        "The `@empty` block renders fallback markup automatically when an iterable collection has zero items, eliminating separate `@if` checks.",
        """| Feature | Legacy Structural Directives | Modern Built-in Control Flow |
| :--- | :--- | :--- |
| **Syntax** | `*ngIf`, `*ngFor`, `*ngSwitch` | `@if`, `@for`, `@switch` |
| **Module Import** | Requires `CommonModule` | Zero imports required |
| **Tracking Key** | Optional `trackBy` function | Mandatory `track` expression |
| **Empty Fallback** | Manual separate `*ngIf` | Integrated `@empty` block |""",
        "The compiler transforms @if into ɵɵconditional branch jumps, and @for into ɵɵrepeater which executes an in-place list diffing algorithm."
    ))

    # Q22: Custom Attribute Directives & Modern host Bindings
    qs.append(format_q(
        22,
        "How do you build custom attribute directives using modern host property bindings?",
        ["Cognizant", "Persistent", "Accenture", "TCS"],
        "Build custom directives with ElementRef and Renderer2, declaring host element bindings cleanly inside the decorator host property.",
        "Custom attribute directives alter element appearance or behavior without modifying template DOM structure. Historically, directives used `@HostBinding` and `@HostListener` decorators on class properties. Modern Angular declares host attributes and listeners inside the directive `host` property. For DOM styling, directives inject `ElementRef` and `Renderer2` to maintain platform abstraction. Modern directives can also be composed using Host Directives. In one of my projects, host directives attached focus traps to dialog components cleanly.",
        [
            ("host property", "metadata object configuring host element bindings", True),
            ("Renderer2", "platform-independent DOM manipulation abstraction layer", True),
            ("Host Directives", "composing directive behaviors directly into components", True),
            ("ElementRef", "wrapper around native DOM element reference", False),
            ("Directive composition", "attaching reusable directive logic without inheritance", False)
        ],
        "An attribute directive is a smartphone protective case: it adds shock resistance without altering internal phone electronics.",
        """// ❌ Bad: scattered legacy decorators on class methods
@HostBinding('class.hovered') isHovered = false;
@HostListener('mouseenter') onEnter() { this.isHovered = true; }

// ✅ Good: centralized modern host property binding
@Directive({
  selector: '[appHighlight]',
  standalone: true,
  host: {
    '[class.hovered]': 'isHovered()',
    '(mouseenter)': 'isHovered.set(true)',
    '(mouseleave)': 'isHovered.set(false)'
  }
})
export class HighlightDirective { readonly isHovered = signal(false); }""",
        "What are Host Directives and when should you use them?",
        "Host Directives allow components to declare other directives in their `hostDirectives` array, composing behaviors without class inheritance.",
        """| Pattern | Syntax Location | Code Clutter |
| :--- | :--- | :--- |
| **host metadata** | Inside `@Directive({ host: ... })` | Minimal |
| **@HostBinding** | Decorator on class properties | High class boilerplate |
| **@HostListener** | Decorator on class methods | Method wrapper bloat |""",
        "The Angular compiler lowers host property entries directly into component view creation and update instructions during compilation."
    ))

    # Q23: Pure vs Impure Pipes: In-Memory Caching & Performance Risks
    qs.append(format_q(
        23,
        "What are the performance risks of impure pipes and how does pure pipe caching work?",
        ["Infosys", "Deloitte", "Wipro", "TCS"],
        "Pure pipes evaluate only on input reference changes; impure pipes run on every change cycle, risking severe UI frame drops.",
        "Angular pipes transform values inside template expressions. A pure pipe evaluates only when its input arguments change by reference [Object.is]. Angular caches the transformation result, reusing it across change detection passes without re-executing. An impure pipe runs on every single change detection cycle regardless of changes. Placing heavy algorithms or array filtering inside impure pipes causes UI sluggishness. In one of my projects, replacing an impure search filter with a computed signal restored 60 FPS scrolling.",
        [
            ("Pure pipe", "evaluates only on primitive or reference changes", True),
            ("Impure pipe", "executes during every change detection cycle", True),
            ("Memoization", "caches output value for identical input references", True),
            ("Frame drops", "UI lag caused by long-running template expressions", False),
            ("Object.is equality", "algorithm verifying input reference changes", False)
        ],
        "A pure pipe is an airport flight display updated only on schedule changes; an impure pipe is a clock ticking continuously.",
        """// ❌ Bad: impure pipe filters array on every tick
@Pipe({ name: 'filterList', pure: false })
export class BadFilterPipe implements PipeTransform {}

// ✅ Good: pure pipe evaluates only on reference change
@Pipe({ name: 'formatCurrency', pure: true })
export class GoodFormatPipe implements PipeTransform {
  transform(v: number): string { return `$${v.toFixed(2)}`; }
}""",
        "Why is an array filter pipe considered an anti-pattern in Angular?",
        "Mutating arrays via push keeps the same reference so pure pipes miss it, while impure pipes run on every keystroke, degrading performance.",
        """| Pipe Type | Evaluation Frequency | In-Memory Cache |
| :--- | :--- | :--- |
| **Pure** | On input reference mutation | Yes (caches last output) |
| **Impure** | Every change detection cycle | No (recomputes always) |""",
        "Angular assigns a transform cache slot to pure pipes. If input arguments match the cached pointers, the cached value is returned."
    ))

    # Q24: Hierarchical DI: Root Injector vs Environment vs Element Injector
    qs.append(format_q(
        24,
        "How does Angular's hierarchical dependency injection resolve services across injectors?",
        ["Accenture", "TCS", "Cognizant", "Capgemini"],
        "Angular resolves tokens by traversing the ElementInjector tree upward, then falling back to the EnvironmentInjector hierarchy.",
        "Angular features a two-tiered hierarchical dependency injection architecture. When a component requests a dependency, Angular first searches the `ElementInjector` tree starting from the host component element upward through parent templates. If the token is not found, resolution falls back to the `EnvironmentInjector` hierarchy. This traverses from route-scoped injectors up to the `RootInjector` and `PlatformInjector`. Understanding this resolution order prevents captive dependencies. In one of my projects, providing state at route level isolated multi-tab editor state.",
        [
            ("ElementInjector", "injector tree associated with template DOM elements", True),
            ("EnvironmentInjector", "injector hierarchy for routes and application scope", True),
            ("RootInjector", "top-level application injector for singletons", True),
            ("Hierarchical resolution", "upward traversal from element to root container", False),
            ("PlatformInjector", "system-level injector configured above application", False)
        ],
        "Searching for a book: check your personal desk first, then your department bookshelf, and finally the central university library.",
        """// ❌ Bad: providing state service in multiple components
@Component({ providers: [CartService] })
// Creates separate cart instances per component!

// ✅ Good: provide service at route or root level
@Injectable({ providedIn: 'root' })
export class CartService {}""",
        "What happens if a token cannot be found anywhere in the injector hierarchy?",
        "Angular throws an `NG0201: NullInjectorError` unless the dependency is marked with `@Optional()` or injected with `{ optional: true }`.",
        """| Injector Layer | Lifetime Scope | Configured Via |
| :--- | :--- | :--- |
| **ElementInjector** | Component DOM lifetime | `providers: [...]` in `@Component` |
| **EnvironmentInjector** | Route / Feature lifetime | `providers: [...]` in Routes |
| **RootInjector** | Application lifetime | `providedIn: 'root'` |""",
        "Angular traverses node injectors via parent pointers. If null is reached, it delegates to the EnvironmentInjector until NullInjector is hit."
    ))

    # Q25: Provider Configuration: useClass vs useExisting vs useFactory vs useValue
    qs.append(format_q(
        25,
        "How do useClass, useExisting, useFactory, and useValue differ in Angular DI?",
        ["TCS", "Infosys", "Deloitte", "Wipro"],
        "useClass instantiates a class; useExisting aliases a token; useFactory creates instances via function; useValue supplies static constants.",
        "Angular provider objects configure how the dependency injection container resolves tokens. `useClass` creates a new instance of a specified class when the token is requested. `useExisting` aliases an existing token to another token, sharing a single singleton instance. `useFactory` invokes a factory function with injected dependencies to construct dynamic instances. `useValue` supplies static configuration objects or constant values directly. In one of my projects, useExisting aliased mock services during automated testing without rewriting components.",
        [
            ("useClass", "instantiates new class instance for provider token", True),
            ("useExisting", "creates an alias pointing to an existing token", True),
            ("useFactory", "executes factory function to resolve dependency", True),
            ("useValue", "binds static object or primitive constant directly", False),
            ("multi: true", "aggregates multiple providers under a single token", False)
        ],
        "useClass is hiring an employee; useExisting is assigning an alias; useFactory is ordering custom catering; useValue is handing out gift cards.",
        """// ❌ Bad: useClass on two tokens creates duplicate singletons
{ provide: LoggerService, useClass: CustomLogger }
{ provide: ApiLogger, useClass: CustomLogger } // 2 instances!

// ✅ Good: useExisting aliases token to share single instance
{ provide: ApiLogger, useExisting: LoggerService }""",
        "What is the purpose of the multi: true provider configuration option?",
        "Setting `multi: true` tells Angular to collect multiple provider values into an array, commonly used for HTTP interceptors and app initializers.",
        """| Provider Option | Resolution Mechanism | Best Use Case |
| :--- | :--- | :--- |
| `useClass` | Instantiates class via `new` | Swapping service implementations |
| `useExisting` | References existing token | Token aliasing & mocking |
| `useFactory` | Runs function with arguments | Dynamic runtime configuration |
| `useValue` | Returns static value | Config constants & tokens |""",
        "The DI registry maps tokens to ProviderRecords. When requested, it evaluates the record type, calling factory or constructor instructions."
    ))

    # Q26: Modern Functional DI: inject() vs Constructor Injection
    qs.append(format_q(
        26,
        "What are the advantages of modern inject() and what rules govern the Injection Context?",
        ["Capgemini", "Cognizant", "Persistent", "Accenture"],
        "inject() resolves tokens in field initializers and guards, eliminating constructor boilerplate and super() parameter forwarding.",
        "The `inject()` function provides functional dependency injection in modern Angular. It resolves tokens during class field declaration, constructor execution, or inside functional route guards. It eliminates constructor parameter bloat and avoids passing dependencies down inheritance hierarchies using `super()`. Calling `inject()` outside an active injection context throws runtime error `NG0203`. To use inject inside asynchronous callbacks, wrap execution in `runInInjectionContext`. In one of my projects, inject() simplified reusable composable state functions.",
        [
            ("inject()", "functional API resolving tokens from active injector", True),
            ("Injection context", "time window when dependency resolution is legal", True),
            ("runInInjectionContext()", "manually restores injection frame for callbacks", True),
            ("NG0203 error", "thrown when inject() is called outside context", False),
            ("Constructor injection", "legacy parameter-based dependency resolution", False)
        ],
        "Constructor injection is declaring all luggage at customs; inject() is pulling tools from a workstation dispenser as you need them.",
        """// ❌ Bad: verbose constructor forwarding to base class
constructor(http: HttpClient, router: Router) { super(http, router); }

// ✅ Good: functional field injection with zero constructor ceremony
private readonly http = inject(HttpClient);
private readonly router = inject(Router);""",
        "How do you resolve a dependency using inject() inside an asynchronous setTimeout callback?",
        "Capture an `EnvironmentInjector` during initialization, then invoke `runInInjectionContext(injector, () => inject(ServiceName))`.",
        """| Feature | Constructor Injection | Functional inject() |
| :--- | :--- | :--- |
| **Declaration** | Constructor parameters | Class field initializers |
| **Inheritance** | Requires `super()` forwarding | Zero `super()` parameters |
| **Functional Guards** | Not supported | Fully supported |
| **Timing Rule** | Instantiation phase | Injection context only |""",
        "Angular manages an internal injector stack. When a component instantiates, its injector pushes to the top; inject() queries the top injector."
    ))

    # Q27: Reactive Forms vs Template-Driven Forms Architecture
    qs.append(format_q(
        27,
        "How do Reactive Forms and Template-Driven Forms compare in architecture and testability?",
        ["TCS", "Infosys", "Deloitte", "Wipro"],
        "Reactive Forms build explicit programmatic form trees in TypeScript, while Template-Driven Forms rely on template directives.",
        "Angular provides two form paradigms. Reactive Forms build an explicit object graph in TypeScript using FormControl, FormGroup, and FormArray. They offer synchronous data access, strict compile-time typing, and unit testability without DOM rendering. Template-Driven Forms rely on template directives like `ngModel`, with asynchronous data binding that depends on DOM change cycles. Reactive Forms are preferred for complex, dynamic enterprise applications. In one of my projects, migrating to typed Reactive Forms prevented payload schema mismatches.",
        [
            ("Reactive Forms", "programmatic synchronous form control model", True),
            ("Template-Driven Forms", "declarative template-based asynchronous form model", True),
            ("Typed forms", "compile-time type safety for form control values", True),
            ("FormControl", "atomic entity tracking field value and validity", False),
            ("FormGroup", "aggregates child form controls into single entity", False)
        ],
        "Reactive forms are an architectural schematic drawn on paper; template forms are adjusting tent poles directly on the campsite.",
        """// ❌ Bad: untyped loose form control declaration
const search = new FormControl('');

// ✅ Good: typed non-nullable form control with validator
const search = new FormControl('', {
  nonNullable: true,
  validators: [Validators.required]
});""",
        "How do you make an entire FormGroup strictly typed in modern Angular?",
        "Define an interface matching form fields, then instantiate `FormGroup<MyFormInterface>` to get compile-time checking on `.value`.",
        """| Dimension | Reactive Forms | Template-Driven Forms |
| :--- | :--- | :--- |
| **Model Creation** | Programmatic in TypeScript | Implicit via directives |
| **Data Flow** | Synchronous | Asynchronous |
| **Validation** | Pure TypeScript functions | Directives in template |
| **Unit Testing** | Testable without DOM | Requires DOM harness |""",
        "Reactive forms extend AbstractControl, maintaining internal value and status observables that update synchronously without DOM interaction."
    ))

    # Q28: FormGroup, FormControl, and FormArray: Dynamic Fields & Async Validators
    qs.append(format_q(
        28,
        "How do you implement dynamic field arrays and custom async validators in Reactive Forms?",
        ["Accenture", "Cognizant", "Capgemini", "TCS"],
        "Use FormArray to add or remove controls dynamically, and apply async validators returning observables of validation errors.",
        "Complex enterprise forms require dynamic fields and asynchronous validation. `FormArray` manages an indexed list of AbstractControl instances, allowing controls to be added or removed dynamically at runtime. Custom asynchronous validators verify values against backend APIs, returning an Observable of `ValidationErrors` or null. Async validators run only after synchronous validation passes, preventing unnecessary network traffic. In one of my projects, FormArray managed dynamic invoice item lines with real-time tax calculation.",
        [
            ("FormArray", "manages dynamically sized list of form controls", True),
            ("AsyncValidatorFn", "asynchronous validator returning observable error object", True),
            ("ValidationErrors", "dictionary describing validation failure reasons", True),
            ("statusChanges", "observable stream emitting VALID, INVALID, or PENDING", False),
            ("Pending state", "form status while async validators are in flight", False)
        ],
        "FormArray is an expandable accordion folder where you can insert or remove document sheets on demand.",
        """// ❌ Bad: synchronous validator doing network requests
(control) => { this.http.get('/check'); return null; }

// ✅ Good: async validator returning observable error object
const uniqueEmail: AsyncValidatorFn = (control) => {
  return inject(UserService).checkEmail(control.value).pipe(
    map(exists => exists ? { emailTaken: true } : null)
  );
};""",
        "Why do async validators run only after all synchronous validators pass?",
        "Running sync validators first filters out basic invalid inputs like required or minLength, preventing wasteful backend API requests.",
        """| Control Entity | Structure | Primary Use Case |
| :--- | :--- | :--- |
| `FormControl` | Single scalar value | Input, checkbox, select |
| `FormGroup` | Key-value dictionary | User profile, address object |
| `FormArray` | Numeric-indexed array | Line items, phone numbers |""",
        "When an async validator triggers, the control enters the PENDING status. On emission, it switches to VALID or INVALID, notifying parents."
    ))

    return qs
