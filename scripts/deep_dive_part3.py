#!/usr/bin/env python3
"""
Deep Dive Part 3: Modules 11 to 16 (Q29 to Q43)
"""
from generate_deep_dive import format_q

def get_part3_questions():
    qs = []

    # Q29: Lazy Loading Standalone vs Route Modules
    qs.append(format_q(
        29,
        "How do you implement lazy loading for standalone components versus route modules?",
        ["TCS", "Infosys", "Cognizant", "Capgemini"],
        "Modern Angular uses loadComponent to lazy load standalone components directly, eliminating NgModule routing boilerplate.",
        "Modern Angular routes lazy load standalone components using `loadComponent` paired with ES dynamic imports. This removes the need for separate feature modules and routing module declarations. Modern bundlers analyze these dynamic imports to generate isolated, granular JavaScript chunks for each route. When a user navigates to the route, Angular fetches the specific component chunk on demand. In one of my projects, converting to loadComponent reduced the initial application bundle size by thirty-five percent.",
        [
            ("loadComponent", "lazy loads standalone component chunks dynamically", True),
            ("Dynamic import()", "ES module syntax triggering bundler code-splitting", True),
            ("loadChildren", "lazy loads child route configuration arrays", True),
            ("Code splitting", "bundler splits route chunks for lazy loading", False),
            ("Tree-shaking", "dead-code elimination stripping unused module exports", False)
        ],
        "Ordering room service dish by dish as you get hungry, rather than preparing an entire five-course buffet in advance.",
        """// ❌ Bad: legacy module lazy loading with boilerplate
{
  path: 'admin',
  loadChildren: () => import('./admin.module').then(m => m.AdminModule)
}

// ✅ Good: modern standalone component lazy loading
{
  path: 'admin',
  loadComponent: () => import('./admin.component').then(m => m.AdminComponent)
}""",
        "Can you still lazy load a collection of child routes together in modern Angular?",
        "Yes. Use `loadChildren: () => import('./admin.routes').then(m => m.ADMIN_ROUTES)` to load a standalone route configuration array.",
        """| Routing Property | Target Entity | Chunk Granularity |
| :--- | :--- | :--- |
| `loadComponent` | Single Standalone Component | Granular component chunk |
| `loadChildren` | Route array or NgModule | Feature-wide chunk |""",
        "When a route activates, the Router resolves the dynamic import promise, injects route providers, and creates the component in an EnvironmentInjector."
    ))

    # Q30: Functional Route Guards & Atomic UrlTree
    qs.append(format_q(
        30,
        "How do modern functional route guards work and why should they return a UrlTree?",
        ["Accenture", "Cognizant", "Persistent", "Deloitte"],
        "Functional guards protect routes using lightweight functions, and returning a UrlTree executes an atomic redirect without race conditions.",
        "Angular replaces class-based guards with functional guards like `CanActivateFn` and `CanDeactivateFn`. Functional guards inject services using `inject()`, eliminating class ceremony. When redirecting unauthorized users, guards should return a `UrlTree` created via `Router.createUrlTree()` rather than returning false and calling `router.navigate()`. Returning a UrlTree executes an atomic navigation redirect, preventing competing router lifecycles and preserving clean browser history. In one of my projects, UrlTree guards stopped redirect flickering.",
        [
            ("CanActivateFn", "functional route guard verifying access permissions", True),
            ("UrlTree", "atomic router representation for navigation targets", True),
            ("CanDeactivateFn", "functional guard preventing unsaved form departures", True),
            ("Atomic redirect", "single-phase redirect avoiding concurrent navigations", False),
            ("inject()", "resolves authentication tokens in functional guards", False)
        ],
        "A airport boarding pass scanner: returning true opens the gate; returning a UrlTree directs you directly to the baggage counter.",
        """// ❌ Bad: returning false with separate navigation call
if (!auth.isLoggedIn()) { router.navigate(['/login']); return false; }

// ✅ Good: return atomic UrlTree redirect directly
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  return auth.isLoggedIn() ? true : inject(Router).createUrlTree(['/login']);
};""",
        "What happens if multiple guards run on a route and one returns a UrlTree?",
        "Navigation to the original target cancels immediately, and the router transitions to the returned UrlTree, prioritizing security overrides.",
        """| Guard Style | Implementation | Boilerplate |
| :--- | :--- | :--- |
| **Class-based** | Implements `CanActivate` interface | High class ceremony |
| **Functional** | Composable `CanActivateFn` function | Minimal function |""",
        "The router evaluates guards concurrently. If any guard emits a UrlTree, router traversal halts, discarding remaining guards and redirecting."
    ))

    # Q31: Modern Route Resolvers: ResolveFn vs Direct Signal Ingestion
    qs.append(format_q(
        31,
        "When should you use a ResolveFn versus ingesting state directly via Signal services?",
        ["Infosys", "Capgemini", "TCS", "Wipro"],
        "Use ResolveFn when rendering requires pre-fetched data; use Signal services when components render skeletons while streaming data.",
        "Route resolvers pre-fetch data before route transitions complete, using functional `ResolveFn`. Resolvers prevent blank screens by delaying navigation until data arrives. However, slow network calls delay route transitions noticeably, hurting perceived performance. In modern reactive architecture, we navigate immediately, render skeleton screens, and fetch data via Signal services reactively. In one of my projects, switching from resolvers to signal services made page transitions feel instant.",
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

    # Q32: Functional HTTP Interceptors: Bearer Token Injection & Request Cloning
    qs.append(format_q(
        32,
        "How do functional HTTP interceptors work and why is request cloning required?",
        ["TCS", "Cognizant", "Deloitte", "Accenture"],
        "Functional interceptors clone immutable requests to attach authentication headers and process responses globally.",
        "Modern Angular uses functional HTTP interceptors [HttpInterceptorFn] configured via `provideHttpClient(withInterceptors([...]))`. Because HttpRequest objects are immutable, interceptors cannot modify headers in place. Instead, they call `req.clone({ setHeaders: { Authorization: token } })`. The modified request passes down the pipeline by calling `next(clonedReq)`. Interceptors also handle responses and global errors using standard RxJS operators. In one of my projects, a functional interceptor injected JWT tokens across all outgoing API calls.",
        [
            ("HttpInterceptorFn", "functional middleware intercepting HTTP traffic", True),
            ("Request cloning", "mutating headers via immutable request clone", True),
            ("Authorization header", "bearer token attached to authenticated requests", True),
            ("withInterceptors", "registers functional interceptors in application config", False),
            ("HttpHandlerFn", "passes modified requests down the handler pipeline", False)
        ],
        "A customs officer inspecting outgoing luggage: they cannot alter your bag directly, but they can place verified tags on a clone.",
        """// ❌ Bad: attempting to modify request headers in place
req.headers.set('Authorization', token); // headers are immutable!

// ✅ Good: clone request to attach authentication headers
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).getToken();
  return next(token ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } }) : req);
};""",
        "Why are HttpRequest instances designed to be immutable in Angular?",
        "Immutability allows safe request retries and prevents race conditions when multiple interceptors inspect or re-dispatch the same request.",
        """| Style | Registration Syntax | Boilerplate |
| :--- | :--- | :--- |
| **Class-based** | `HTTP_INTERCEPTORS` multi-token | High class ceremony |
| **Functional** | `withInterceptors([fn])` | Composable function |""",
        "Functional interceptors chain as an onion-style pipeline. The final handler invokes the platform XMLHttpRequest or Fetch backend."
    ))

    # Q33: Silent JWT Token Refresh & 401 Unauthorized Retry Queueing
    qs.append(format_q(
        33,
        "How do you implement silent JWT refresh and request queueing for 401 errors?",
        ["Capgemini", "Infosys", "Persistent", "TCS"],
        "Catch 401 errors in an interceptor, execute a single refresh token request, and queue concurrent requests until it completes.",
        "When an access token expires, the backend returns a 401 Unauthorized response. The interceptor intercepts this error, sets a concurrency lock, and triggers the refresh endpoint. Subsequent failing requests wait in a queue using a `BehaviorSubject`. Once refreshed, the new token emits, unlocking queued requests to retry with updated headers. If refresh fails, the user is logged out immediately. In one of my projects, this queueing prevented multi-tab logout cascades.",
        [
            ("Silent refresh", "renewing expired access tokens without user interruption", True),
            ("401 Unauthorized", "HTTP error code indicating expired access credentials", True),
            ("Concurrency lock", "flag preventing duplicate concurrent refresh requests", True),
            ("Token rotation", "issuing new access and refresh tokens upon renewal", False),
            ("Retry queue", "buffering requests until token refresh completes", False)
        ],
        "A hotel keycard expiring while friends order drinks: one person visits reception for a fresh card while others wait at the table.",
        """// ❌ Bad: triggering multiple concurrent refresh API calls
catchError(err => auth.refreshToken()); // multi-request storms!

// ✅ Good: concurrency lock with BehaviorSubject queue
if (!isRefreshing) {
  isRefreshing = true;
  return auth.refreshToken().pipe(
    switchMap(token => { isRefreshing = false; return next(clone(req, token)); })
  );
}""",
        "What happens if the silent token refresh API call itself returns a 401 error?",
        "The refresh lock clears, all active user session tokens are wiped, and the user is redirected to the login page immediately.",
        """| Step | Action Taken | State Variable |
| :--- | :--- | :--- |
| **1. First 401** | Triggers refresh call | `isRefreshing = true` |
| **2. Concurrent 401** | Queues in BehaviorSubject | Waits for new token |
| **3. Refresh Success** | Emits token to queue | `isRefreshing = false` |
| **4. Refresh Failure** | Logs out user | Session destroyed |""",
        "Waiting requests subscribe to a BehaviorSubject with filter(token => token !== null) and take(1), resuming execution when the new token emits."
    ))

    # Q34: Angular Memory Leaks: Uncancelled Subscriptions & Detached DOM
    qs.append(format_q(
        34,
        "What are the root causes of memory leaks in Angular and how do you profile them?",
        ["TCS", "Accenture", "Cognizant", "Deloitte"],
        "Memory leaks stem from unclosed subscriptions retaining component closures; profile them using Chrome DevTools heap snapshots.",
        "Memory leaks happen when destroyed components cannot be garbage collected. Long-lived subscriptions capturing component references are the primary cause. Uncleared timers, window event listeners, and detached DOM trees also retain memory. To diagnose leaks, take Chrome DevTools heap snapshots before and after view navigation. Comparing snapshots reveals retained objects holding active memory closures. In one of my projects, heap snapshots revealed retained modal DOM trees caused by uncleared intervals.",
        [
            ("Memory leak", "failure to release unused memory allocations", True),
            ("Detached DOM tree", "DOM nodes removed from document but retained in memory", True),
            ("Heap snapshot", "diagnostic snapshot of memory objects in DevTools", True),
            ("Closure retention", "callbacks preventing garbage collection of this references", False),
            ("Garbage collection", "browser memory reclamation for unreachable objects", False)
        ],
        "Leaving rented equipment checked out under your name after moving out of town, continuing to accrue daily rental charges.",
        """// ❌ Bad: singleton stream retains destroyed component closure
ngOnInit(): void {
  this.bus.events$.subscribe(ev => this.handleEvent(ev));
}

// ✅ Good: tie subscription lifecycle to component context
private readonly sub = toSignal(this.bus.events$);""",
        "Why do detached DOM trees consume disproportionately large amounts of memory?",
        "Retaining a single detached DOM element in a closure retains all of its child elements, attributes, and attached event listener scopes.",
        """| Leak Source | Retention Mechanism | Detection Method |
| :--- | :--- | :--- |
| **Unclosed Subscription** | Closure retains `this` pointer | Retained Component instance |
| **Uncleared Timer** | Event loop retains callback | Persistent CPU usage |
| **Detached DOM Tree** | JavaScript holds element pointer | Detached DOM in Heap |""",
        "In the V8 engine, an object is eligible for garbage collection only when no active root reference path exists in the memory graph."
    ))

    # Q35: Modern Teardown: takeUntilDestroyed vs DestroyRef vs AsyncPipe
    qs.append(format_q(
        35,
        "How do modern teardown patterns like takeUntilDestroyed compare to AsyncPipe?",
        ["Infosys", "Capgemini", "Wipro", "TCS"],
        "takeUntilDestroyed cleans subscriptions in TypeScript; AsyncPipe cleans subscriptions in templates automatically upon view destruction.",
        "Modern Angular provides several declarative teardown strategies. The `AsyncPipe` manages subscriptions directly within templates, subscribing on view creation and unsubscribing when the element unmounts. In TypeScript logic, `takeUntilDestroyed()` automatically disposes subscriptions when the host component destroys. It relies on the current `DestroyRef` within an active injection context. Alternatively, `DestroyRef.onDestroy()` registers custom cleanup callbacks. In one of my projects, takeUntilDestroyed eliminated all manual ngOnDestroy boilerplate.",
        [
            ("takeUntilDestroyed()", "unsubscribes automatically when component destroys", True),
            ("DestroyRef", "functional teardown hook replacing ngOnDestroy", True),
            ("AsyncPipe", "template pipe handling subscribe and unsubscribe", True),
            ("Injection context", "execution scope providing access to DestroyRef", False),
            ("ngOnDestroy", "legacy lifecycle hook for teardown logic", False)
        ],
        "AsyncPipe is a library book returned automatically when due; takeUntilDestroyed is an automatic service cancellation when moving.",
        """// ❌ Bad: manual Subject for unsubscription boilerplate
private destroy$ = new Subject<void>();
ngOnDestroy() { this.destroy$.next(); }

// ✅ Good: modern takeUntilDestroyed tied to injection context
this.data$.pipe(takeUntilDestroyed()).subscribe();""",
        "Can you call takeUntilDestroyed() inside ngOnInit instead of the constructor?",
        "Yes, but you must pass an injected `DestroyRef` explicitly: `takeUntilDestroyed(this.destroyRef)` since ngOnInit is outside injection context.",
        """| Teardown Pattern | Execution Context | Boilerplate Level |
| :--- | :--- | :--- |
| `AsyncPipe` | HTML Template | Zero TypeScript code |
| `takeUntilDestroyed()` | Constructor or field | Single operator call |
| `DestroyRef.onDestroy()` | Functional teardown | Composable callback |
| Legacy `ngOnDestroy` | Class lifecycle hook | High manual ceremony |""",
        "takeUntilDestroyed resolves DestroyRef, registering an onDestroy callback that emits and completes an internal Subject."
    ))

    # Q36: State Management Decision Matrix: Signals vs SignalStore vs Redux
    qs.append(format_q(
        36,
        "How do you decide between Local Signals, Service Signals, NgRx SignalStore, and Classic Redux?",
        ["TCS", "Accenture", "Cognizant", "Persistent"],
        "Use local signals for component state, service signals for simple sharing, and NgRx SignalStore for enterprise modular state.",
        "State management architecture should match problem complexity. Use local component signals for simple presentation state like modal toggles and forms. Use an injectable service with signals for shared state across a few related components. For enterprise applications with complex caching, pagination, and optimistic updates, choose `@ngrx/signals` [SignalStore]. SignalStore provides structured state, computed values, and rxMethod side effects with zero Redux ceremony. In one of my projects, migrating from Redux to SignalStore reduced boilerplate by sixty percent.",
        [
            ("Local Signals", "component-scoped reactive state container", True),
            ("Shared Signal Service", "injectable service holding shared signals", True),
            ("NgRx SignalStore", "composable, lightweight enterprise state container", True),
            ("Classic Redux Store", "action, reducer, and effect based architecture", False),
            ("Tree-shaking", "bundler strips unreferenced state slices", False)
        ],
        "Local signal is a personal notepad; signal service is a shared office whiteboard; SignalStore is a structured filing cabinet.",
        """// ❌ Bad: classic Redux ceremony with actions and reducers
export const loadItems = createAction('[Cart] Load');
export const cartReducer = createReducer(...);

// ✅ Good: modern lightweight NgRx SignalStore
export const CartStore = signalStore(
  withState({ items: [] })
);""",
        "Why is NgRx SignalStore preferred over classic NgRx Global Store for new applications?",
        "SignalStore eliminates actions, reducers, and string action types, providing fine-grained reactivity, native signal integration, and modular composability.",
        """| Dimension | Local Signals | Signal Service | NgRx SignalStore | Classic Redux |
| :--- | :--- | :--- | :--- | :--- |
| **Scope** | Component | Feature | Composable | Global App |
| **Boilerplate** | None | Low | Low | Very High |
| **Side Effects** | None | Manual | `rxMethod` | `@Effect()` |
| **Reactivity** | Signals | Signals | Signals | Observables |""",
        "SignalStore uses functional composition functions [withState, withComputed, withMethods] to build a typed state container."
    ))

    # Q37: Modern NgRx SignalStore Architecture
    qs.append(format_q(
        37,
        "Explain the anatomy and features of modern NgRx SignalStore.",
        ["Capgemini", "Infosys", "Deloitte", "TCS"],
        "NgRx SignalStore defines state using withState, memoized derivations using withComputed, and methods using withMethods.",
        "NgRx SignalStore is a composable state management solution. It configures state slices using `withState(initialState)`. Each state slice is a signal; `computed` caches its result until an input changes. Derived memoized calculations are added using `withComputed()`. Methods and side effects are defined using `withMethods()`, updating state via `patchState()` and `rxMethod`. In one of my projects, SignalStore provided clean caching for our user management portal.",
        [
            ("signalStore()", "factory function creating a composable store", True),
            ("withState()", "defines reactive state slices as signals", True),
            ("withComputed()", "adds memoized computed signals to the store", True),
            ("withMethods()", "defines state mutation and async methods", False),
            ("patchState()", "atomic state update utility function", False)
        ],
        "SignalStore is a modular kitchen: countertops store items, appliances compute recipes, and cooks execute prep methods.",
        """// ❌ Bad: mutating store state properties directly
store.items = [...newItems]; // direct mutation illegal!

// ✅ Good: atomic state update with patchState
updateCart(item: CartItem): void {
  patchState(store, state => ({ items: [...state.items, item] }));
}""",
        "Can a SignalStore be provided at the component level for automatic teardown?",
        "Yes. Provide the SignalStore in the component's `providers: [CartStore]` array; it will instantiate with the component and destroy automatically.",
        """| Feature | Primary Function | Returned Property |
| :--- | :--- | :--- |
| `withState` | Declares reactive state | Read-only Signals |
| `withComputed` | Derives memoized state | Computed Signals |
| `withMethods` | State update & side effects | Store methods |
| `withHooks` | Lifecycle initialization | onInit, onDestroy |""",
        "SignalStore builds an object whose properties map directly to signals; patchState evaluates state updaters and sets signals cleanly."
    ))

    # Q38: Deferrable Views (@defer) & Trigger Conditions
    qs.append(format_q(
        38,
        "How do Deferrable Views work under the hood and what are their trigger conditions?",
        ["TCS", "Cognizant", "Persistent", "Accenture"],
        "Deferrable views lazy load template chunks on triggers like viewport, interaction, hover, timer, or browser idle time.",
        "Deferrable views provide compiler-level declarative lazy loading for template segments. When the compiler detects `@defer`, it isolates inner components into separate JavaScript chunks. At runtime, Angular downloads chunks based on triggers like `on viewport`, `on interaction`, `on hover`, and `on idle`. Companion blocks include `@placeholder`, `@loading`, and `@error`. In one of my projects, deferring below-the-fold charts reduced initial JavaScript load by forty percent.",
        [
            ("@defer", "template block for lazy loading markup chunks", True),
            ("on viewport", "loads chunk when placeholder enters viewport", True),
            ("on idle", "loads chunk during browser idle time", True),
            ("@placeholder", "markup displayed before deferred load begins", False),
            ("@loading", "markup shown while the chunk is actively downloading", False)
        ],
        "Deferrable views are like ordering courses at a dinner table: the main course arrives only after appetizers finish.",
        """// ❌ Bad: bundling heavy chart into initial page chunk
<app-heavy-chart [data]="metrics" />

// ✅ Good: defer chunk loading until scrolled into view
@defer (on viewport) {
  <app-heavy-chart [data]="metrics" />
}
@placeholder {
  <div class="h-40">Loading chart...</div>
}""",
        "Why must on viewport triggers be paired with a @placeholder block?",
        "IntersectionObserver requires a rendered DOM element in the document tree to track viewport entry; without a placeholder, observation fails.",
        """| Trigger | Activation Condition | Recommended Use Case |
| :--- | :--- | :--- |
| `on viewport` | Placeholder enters viewport | Below-the-fold content |
| `on interaction` | Click or keydown on element | Modals, expandable menus |
| `on hover` | Cursor hovers over target | Tooltips, preview cards |
| `on idle` | Main thread becomes idle | Analytics, background widgets |""",
        "The Angular compiler extracts @defer contents into a dynamic import() chunk, wiring browser observers to trigger chunk download."
    ))

    # Q39: Enterprise Angular Performance Optimization Checklist
    qs.append(format_q(
        39,
        "What are the top performance optimization techniques for enterprise Angular applications?",
        ["Deloitte", "Infosys", "Capgemini", "TCS"],
        "Optimize enterprise applications using OnPush change detection, mandatory track keys, deferrable views, NgOptimizedImage, and route splitting.",
        "Enterprise frontend optimization requires a multi-layered architectural approach. At runtime, enforce `ChangeDetectionStrategy.OnPush` and modern Signals to prune unnecessary component dirty checking passes. In templates, always specify unique keys in `@for (...; track item.id)` to avoid DOM recreation. Use `@defer` for below-the-fold components to reduce initial bundle parse times. For assets, adopt `NgOptimizedImage` for automated lazy loading and responsive sizing. In one of my projects, this checklist improved our Lighthouse score from 58 to 94.",
        [
            ("OnPush change detection", "prunes clean subtrees during change passes", True),
            ("track expression", "preserves DOM nodes during list diffing", True),
            ("NgOptimizedImage", "directive optimizing image loading and sizing", True),
            ("@defer views", "declarative template code-splitting primitive", False),
            ("Zoneless mode", "removes Zone.js change detection overhead", False)
        ],
        "Tuning a race car: lighten the chassis, install responsive fuel injectors, and streamline tires for maximum speed.",
        """// ❌ Bad: unoptimized list and plain img tag
<img src="large-hero.jpg">
<div *ngFor="let item of items">{{ item.name }}</div>

// ✅ Good: NgOptimizedImage with keyed control loop
<img ngSrc="hero.jpg" width="800" height="400" priority>
@for (item of items(); track item.id) { <div>{{ item.name }}</div> }""",
        "What critical optimizations does NgOptimizedImage provide over raw <img> tags?",
        "It enforces aspect ratio dimensions, automatically generates srcset attributes, enables lazy loading, and warns against layout shifts.",
        """| Area | Optimization Technique | Performance Benefit |
| :--- | :--- | :--- |
| **Change Detection** | `OnPush` + Signals | Eliminates full-tree checks |
| **Bundle Size** | `@defer` + `loadComponent` | Shrinks initial JS bundle |
| **List Rendering** | `@for (...; track id)` | Prevents DOM recycling lag |
| **Images** | `NgOptimizedImage` | Lowers LCP, eliminates CLS |""",
        "esbuild builds an exact dependency graph. Standalone components enable aggressive dead-code elimination, stripping unreferenced code."
    ))

    # Q40: Global Error Handling: Custom ErrorHandler
    qs.append(format_q(
        40,
        "How do you implement centralized global error handling and telemetry in Angular?",
        ["TCS", "Accenture", "Cognizant", "Wipro"],
        "Implement a custom ErrorHandler class and provide it in application configuration to intercept uncaught exceptions globally.",
        "Angular catches all unhandled runtime errors through its built-in `ErrorHandler` class. By default, it prints error stack traces to the browser console. For enterprise applications, create a class implementing `ErrorHandler` and override `handleError(error: unknown)`. Inside, extract the error message, stack trace, and user context, forwarding telemetry to monitoring backends like Sentry. Register it in `app.config.ts` using `{ provide: ErrorHandler, useClass: GlobalErrorHandler }`. In one of my projects, this centralized error logging reduced defect resolution times.",
        [
            ("ErrorHandler", "centralized class catching unhandled errors", True),
            ("handleError()", "method executed when an unhandled exception occurs", True),
            ("Telemetry logging", "forwarding client diagnostics to monitoring services", True),
            ("Zone.js error trap", "catches asynchronous errors in microtasks", False),
            ("provideErrorHandler", "configures application error handling token", False)
        ],
        "A central emergency command center that receives alarms from every sensor in a skyscraper.",
        """// ❌ Bad: local try-catch blocks that swallow errors silently
try { init(); } catch (e) { /* ignored! */ }

// ✅ Good: centralized global error handler service
@Injectable()
export class GlobalErrorHandler implements ErrorHandler {
  handleError(error: unknown): void {
    inject(TelemetryService).logException(error);
  }
}""",
        "Why should you avoid injecting HTTP services directly into an ErrorHandler constructor?",
        "ErrorHandler is instantiated before standard networking dependencies; constructor injection can trigger circular dependency crashes during application bootstrap.",
        """| Error Mechanism | Scope | Primary Purpose |
| :--- | :--- | :--- |
| `ErrorHandler` | Whole application | Uncaught crash telemetry |
| `HttpInterceptor` | Network layer | 4xx/5xx network retries |
| `catchError()` | Specific RxJS stream | Local fallback values |""",
        "Zone.js catches unhandled promise rejections and asynchronous callbacks, routing them through ApplicationRef into the ErrorHandler."
    ))

    # Q41: Angular Security & XSS Protection: Built-in Sanitization, DomSanitizer, CSP
    qs.append(format_q(
        41,
        "How does Angular protect against Cross-Site Scripting (XSS) and when should you use DomSanitizer?",
        ["Capgemini", "Infosys", "Deloitte", "TCS"],
        "Angular sanitizes untrusted bindings automatically; use DomSanitizer only to explicitly trust verified external content.",
        "Angular treats all untrusted values as dangerous by default. During binding compilation, Angular evaluates values against security contexts, stripping executable scripts, javascript: pseudo-protocols, and malicious attributes. If you must render trusted HTML strings or dynamic iframe URLs, use `DomSanitizer`. Methods like `bypassSecurityTrustHtml` instruct Angular to bypass sanitization. You should use it only after thoroughly validating input sources. In one of my projects, sanitizing third-party SVG icons prevented potential script injections.",
        [
            ("DomSanitizer", "service for bypassing Angular security sanitization", True),
            ("Security context", "categorizes bindings like HTML, style, URL", True),
            ("XSS protection", "stripping executable malicious scripts from markup", True),
            ("Content Security Policy", "HTTP header restricting browser resource origins", False),
            ("bypassSecurityTrustHtml", "marks HTML string as safe for rendering", False)
        ],
        "Airport baggage security: all luggage is scanned by default, and only diplomatic pouches receive explicit security exemptions.",
        """// ❌ Bad: rendering raw HTML directly risks injection
<div [innerHTML]="untrustedContent"></div>

// ✅ Good: sanitize through DomSanitizer after verification
readonly safeHtml = computed(() => {
  return this.sanitizer.bypassSecurityTrustHtml(this.content());
});""",
        "What happens if an attacker injects a <script> tag into an interpolated {{ value }} binding?",
        "Angular treats interpolation strictly as plain text, escaping HTML characters so the browser never executes the script.",
        """| Binding Type | Default Security | Sanitizer Required |
| :--- | :--- | :--- |
| `{{ value }}` | Encoded as plain text | Never |
| `[innerHTML]` | Sanitized by context | Only for custom trusted markup |
| `[src]` | URL sanitized | Only for trusted dynamic URLs |""",
        "Angular's compiler maps bindings to contexts (HTML, STYLE, SCRIPT, URL, RESOURCE_URL), applying regular expression cleaners per context."
    ))

    # Q42: Angular Server-Side Rendering & Non-Destructive Hydration
    qs.append(format_q(
        42,
        "How does Non-Destructive Hydration work in modern Angular Server-Side Rendering?",
        ["TCS", "Cognizant", "Persistent", "Accenture"],
        "Non-destructive hydration reuses server-rendered DOM nodes, attaching client event listeners without destroying existing markup.",
        "In legacy Angular SSR, client bootstrap destroyed server-rendered HTML and re-rendered the entire component tree. This caused visible screen flickering and lost form input states. Modern Angular uses non-destructive hydration enabled via `provideClientHydration()`. The server generates DOM nodes with hydration annotation attributes. On the client, Angular traverses existing nodes, matching components to elements and attaching event listeners without recreating DOM nodes. In one of my projects, hydration reduced Largest Contentful Paint by forty percent.",
        [
            ("provideClientHydration()", "enables non-destructive hydration in bootstrap", True),
            ("DOM recycling", "attaches events to existing nodes without recreation", True),
            ("Flickering reduction", "prevents visible page flashes during page load", True),
            ("Largest Contentful Paint", "Core Web Vital metric measuring visual load speed", False),
            ("Hydration mismatch", "error when client DOM diverges from server HTML", False)
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
        "What causes hydration mismatch warnings in the developer console?",
        "Mismatches occur when client markup diverges from server HTML, commonly caused by reading browser globals like `window` or `localStorage` during render.",
        """| SSR Mode | DOM Destruction | Visual Flash | Performance |
| :--- | :--- | :--- | :--- |
| **Legacy SSR** | Complete wipe and redraw | High flicker | Poor LCP |
| **Non-Destructive** | Reuses server DOM nodes | Zero flicker | Optimal LCP |""",
        "The server annotates DOM nodes with hydration IDs. On the client, Angular reconciles template instructions against these IDs."
    ))

    # Q43: RxJS Operator Nuances: take(1) vs first() vs single() & shareReplay
    qs.append(format_q(
        43,
        "How do take(1), first(), and single() differ, and why is shareReplay(1) dangerous without refCount?",
        ["Infosys", "Deloitte", "Wipro", "TCS"],
        "take(1) completes on the first emission; first() errors if empty; shareReplay without refCount retains source connections forever.",
        "These three completion operators differ in error handling: `take(1)` emits the first item and completes, or completes cleanly if empty. `first()` emits the first matching item, but throws an `EmptyError` if the stream completes empty. `single()` asserts that exactly one item emits, erroring on empty or multiple emissions. Furthermore, `shareReplay(1)` without `refCount: true` keeps underlying subscriptions open indefinitely. In one of my projects, adding refCount fixed memory growth in our navigation service.",
        [
            ("take(1)", "emits first value and completes without empty error", True),
            ("first()", "emits first value but throws EmptyError if empty", True),
            ("single()", "errors if emission count is not exactly one", True),
            ("refCount: true", "unsubscribes from source when subscriber count hits zero", False),
            ("shareReplay(1)", "multicasts and caches latest emissions for late subscribers", False)
        ],
        "take(1) catches the first bus; first() demands a bus exists; shareReplay without refCount leaves the tap running after everyone leaves.",
        """// ❌ Bad: shareReplay without refCount leaks source connection
readonly config$ = this.http.get('/config').pipe(shareReplay(1));

// ✅ Good: refCount ensures source unsubscription on zero consumers
readonly config$ = this.http.get('/config').pipe(
  shareReplay({ bufferSize: 1, refCount: true })
);""",
        "What happens when all subscribers unsubscribe from a shareReplay stream with refCount true?",
        "The internal subscriber reference counter reaches zero, unsubscribing from the source stream and disposing cached buffer allocations cleanly.",
        """| Operator | Zero Items Emitted | Multiple Items Emitted |
| :--- | :--- | :--- |
| `take(1)` | Completes cleanly | Emits first & completes |
| `first()` | Throws `EmptyError` | Emits first & completes |
| `single()` | Throws `EmptyError` | Throws error |""",
        "When refCount is true, an internal subscriber reference counter tracks active observers, triggering source disposal when the count reaches zero."
    ))

    return qs
