#!/usr/bin/env python3
"""
Generator for 03_Angular_Signals_Deep_Dive.md adhering strictly to SSE-1.
Contains all 51 questions (Q1 to Q43 + Q44 to Q51 converted from Case Studies)
plus clean architecture references.
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

def build_deep_dive():
    header = """# 03. Modern Angular (v16–v18+) & Signals Experienced Developer (5–10+ YOE) Interview Master Guide — India Context

> **Target Audience:** Experienced Full-Stack & Frontend Developers (5–10+ Years of Experience) preparing for Senior Developer, Tech Lead, Module Lead, and Frontend Architect rounds in India.  
> **Applicable Companies:**  
> - **Top IT Services & Global Consultancies:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, HCL, LTIMindtree, Tech Mahindra, Hexaware, Persistent Systems, Nagarro, EPAM Systems, Coforge, Virtusa, Deloitte, EY, PwC, KPMG.  
> - **Tier-1 Global Capability Centers (GCCs) & Tech Hubs:** Wells Fargo, Morgan Stanley, JPMorgan Chase, Barclays, Walmart Global Tech India, Lowe's India, Target India, Optum, Fidelity Investments, Standard Chartered, HSBC Technology India.  
> - **Top Indian Product Firms & High-Growth Tech:** Swiggy, Zomato, Flipkart, MakeMyTrip, PhonePe, Paytm, Jio, Tata Neu, Zepto.  
>
> **Philosophy:** Senior-level systems thinking, deep framework internals, and real-world project experience. Every question strictly follows the Speakable Senior English v1 (SSE-1) standard.

---

# TABLE OF CONTENTS

- [MODULE 1: COMPONENT LIFECYCLE HOOKS & EXECUTION ORDER](#module-1-component-lifecycle-hooks--execution-order)
  - [Q1: Component Lifecycle Sequence & Exact Execution Order](#q1-component-lifecycle-sequence--exact-execution-order)
  - [Q2: Parent-Child Lifecycle Hook Execution Order](#q2-parent-child-lifecycle-hook-execution-order)
  - [Q3: ngOnChanges vs ngOnInit vs ngDoCheck](#q3-ngonchanges-vs-ngoninit-vs-ngdocheck)
  - [Q4: ngAfterViewInit vs ngAfterContentInit & ExpressionChangedAfterItHasBeenCheckedError](#q4-ngafterviewinit-vs-ngaftercontentinit--expressionchangedafterithasbeencheckederror)
- [MODULE 2: ANGULAR SIGNALS (v16–v18+) REACTIVE PRIMITIVES](#module-2-angular-signals-v16v18-reactive-primitives)
  - [Q5: The Modern Signals Trio: signal(), computed(), and effect() Under the Hood](#q5-the-modern-signals-trio-signal-computed-and-effect-under-the-hood)
  - [Q6: Array & Object State Mutations: Direct .push() Anti-Pattern vs .set() and .update()](#q6-array--object-state-mutations-direct-push-anti-pattern-vs-set-and-update)
  - [Q7: untracked() Signal Reads & Breaking Circular Dependency Cascades](#q7-untracked-signal-reads--breaking-circular-dependency-cascades)
  - [Q8: Modern Signal Inputs & Two-Way Binding: input(), input.required(), and model()](#q8-modern-signal-inputs--two-way-binding-input-inputrequired-and-model)
- [MODULE 3: SIGNALS VS RXJS OBSERVABLES & REACTIVE INTEROP](#module-3-signals-vs-rxjs-observables--reactive-interop)
  - [Q9: Angular Signals vs RxJS Observables: When to Use Which (State vs Events)](#q9-angular-signals-vs-rxjs-observables-when-to-use-which-state-vs-events)
  - [Q10: Reactive Interop: toSignal() and toObservable() Execution Contexts & Pitfalls](#q10-reactive-interop-tosignal-and-toobservable-execution-contexts--pitfalls)
  - [Q11: Combining Observables: forkJoin vs combineLatest vs withLatestFrom](#q11-combining-observables-forkjoin-vs-combinelatest-vs-withlatestfrom)
- [MODULE 4: COMPONENT COMMUNICATION ARCHITECTURES](#module-4-component-communication-architectures)
  - [Q12: Component Communication: Decorators (@Input/@Output) vs Modern Primitives (input/output/model)](#q12-component-communication-decorators-inputoutput-vs-modern-primitives-inputoutputmodel)
  - [Q13: ViewChild vs ContentChild & Static vs Dynamic Resolution ({ static: true | false })](#q13-viewchild-vs-contentchild--static-vs-dynamic-resolution--static-true--false-)
  - [Q14: Cross-Component Communication via Shared Service: Signals State Service vs BehaviorSubject](#q14-cross-component-communication-via-shared-service-signals-state-service-vs-behaviorsubject)
- [MODULE 5: RXJS FLATTENING OPERATORS MASTERY](#module-5-rxjs-flattening-operators-mastery)
  - [Q15: RxJS Flattening Operators: switchMap vs mergeMap vs concatMap vs exhaustMap](#q15-rxjs-flattening-operators-switchmap-vs-mergemap-vs-concatmap-vs-exhaustmap)
  - [Q16: Real-World Typeahead Live Search: Race-Condition Prevention with switchMap](#q16-real-world-typeahead-live-search-race-condition-prevention-with-switchmap)
  - [Q17: Preventing Double-Click Submissions with exhaustMap vs Sequential Queueing with concatMap](#q17-preventing-double-click-submissions-with-exhaustmap-vs-sequential-queueing-with-concatmap)
- [MODULE 6: CHANGE DETECTION STRATEGIES & ZONELESS ARCHITECTURE](#module-6-change-detection-strategies--zoneless-architecture)
  - [Q18: Default vs ChangeDetectionStrategy.OnPush & Why Immutability is Mandatory](#q18-default-vs-changedetectionstrategyonpush--why-immutability-is-mandatory)
  - [Q19: ChangeDetectorRef Mechanics: markForCheck() vs detectChanges() vs detach() / reattach()](#q19-changedetectorref-mechanics-markforcheck-vs-detectchanges-vs-detach--reattach)
  - [Q20: Modern Zoneless Angular: provideExperimentalZonelessChangeDetection() vs NgZone.runOutsideAngular()](#q20-modern-zoneless-angular-provideexperimentalzonelesschangedetection-vs-ngzonerunoutsideangular)
- [MODULE 7: DIRECTIVES: BUILT-IN CONTROL FLOW & CUSTOM ATTRIBUTES](#module-7-directives-built-in-control-flow--custom-attributes)
  - [Q21: Structural Directives (*ngIf, *ngFor) vs Modern Built-in Control Flow (@if, @for with track, @switch)](#q21-structural-directives-ngif-ngfor-vs-modern-built-in-control-flow-if-for-with-track-switch)
  - [Q22: Custom Attribute Directives using ElementRef, Renderer2, and Modern host Property Bindings](#q22-custom-attribute-directives-using-elementref-renderer2-and-modern-host-property-bindings)
- [MODULE 8: PIPES: PURE VS IMPURE ARCHITECTURE](#module-8-pipes-pure-vs-impure-architecture)
  - [Q23: Pure vs Impure Pipes: Change Detection Cycles, In-Memory Caching & Performance Risks](#q23-pure-vs-impure-pipes-change-detection-cycles-in-memory-caching--performance-risks)
- [MODULE 9: HIERARCHICAL DEPENDENCY INJECTION & PROVIDERS](#module-9-hierarchical-dependency-injection--providers)
  - [Q24: Hierarchical DI: Root Injector vs Environment Injector vs Element Injector](#q24-hierarchical-di-root-injector-vs-environment-injector-vs-element-injector)
  - [Q25: Provider Configuration: useClass vs useExisting vs useFactory vs useValue & Multi-Providers](#q25-provider-configuration-useclass-vs-useexisting-vs-usefactory-vs-usevalue--multi-providers)
  - [Q26: Modern Functional DI: inject() vs Constructor Injection & Injection Context Rules](#q26-modern-functional-di-inject-vs-constructor-injection--injection-context-rules)
- [MODULE 10: REACTIVE FORMS VS TEMPLATE-DRIVEN FORMS](#module-10-reactive-forms-vs-template-driven-forms)
  - [Q27: Reactive Forms vs Template-Driven Forms: Architecture, Scalability & Dynamic Validation](#q27-reactive-forms-vs-template-driven-forms-architecture-scalability--dynamic-validation)
  - [Q28: FormGroup, FormControl, and FormArray: Dynamic Fields & Custom Async Validators](#q28-formgroup-formcontrol-and-formarray-dynamic-fields--custom-async-validators)
- [MODULE 11: MODERN ROUTING, NAVIGATION & LAZY LOADING](#module-11-modern-routing-navigation--lazy-loading)
  - [Q29: Lazy Loading Standalone Components (loadComponent) vs Route Modules (loadChildren)](#q29-lazy-loading-standalone-components-loadcomponent-vs-route-modules-loadchildren)
  - [Q30: Functional Route Guards: CanActivateFn, CanDeactivateFn, and Atomic UrlTree Redirects](#q30-functional-route-guards-canactivatefn-candeactivatefn-and-atomic-urltree-redirects)
  - [Q31: Modern Route Resolvers: ResolveFn vs Direct Signal Service Ingestion](#q31-modern-route-resolvers-resolvefn-vs-direct-signal-service-ingestion)
- [MODULE 12: HTTP CLIENT & FUNCTIONAL INTERCEPTORS](#module-12-http-client--functional-interceptors)
  - [Q32: Functional HTTP Interceptors (HttpInterceptorFn): Bearer Token Injection & Request Cloning](#q32-functional-http-interceptors-httpinterceptorfn-bearer-token-injection--request-cloning)
  - [Q33: Silent JWT Token Refresh & 401 Unauthorized Retry Queueing](#q33-silent-jwt-token-refresh--401-unauthorized-retry-queueing)
- [MODULE 13: MEMORY LEAK PREVENTION & TEARDOWN MECHANICS](#module-13-memory-leak-prevention--teardown-mechanics)
  - [Q34: Root Causes of Angular Memory Leaks: Uncancelled Subscriptions & Detached DOM Trees](#q34-root-causes-of-angular-memory-leaks-uncancelled-subscriptions--detached-dom-trees)
  - [Q35: Modern Teardown Patterns: takeUntilDestroyed(), DestroyRef.onDestroy(), and AsyncPipe](#q35-modern-teardown-patterns-takeuntildestroyed-destroyrefondestroy-and-asyncpipe)
- [MODULE 14: STATE MANAGEMENT: LOCAL VS NGRX SIGNALSTORE](#module-14-state-management-local-vs-ngrx-signalstore)
  - [Q36: State Management Decision Matrix: Local Signals vs Service Signals vs NgRx SignalStore](#q36-state-management-decision-matrix-local-signals-vs-service-signals-vs-ngrx-signalstore)
  - [Q37: Modern NgRx SignalStore Architecture: signalStore(), withState(), withComputed(), and withMethods()](#q37-modern-ngrx-signalstore-architecture-signalstore-withstate-withcomputed-and-withmethods)
- [MODULE 15: PERFORMANCE TUNING & ENTERPRISE OPTIMIZATIONS](#module-15-performance-tuning--enterprise-optimizations)
  - [Q38: Deferrable Views (@defer, @placeholder, @loading, @error) and Trigger Conditions](#q38-deferrable-views-defer-placeholder-loading-error-and-trigger-conditions)
  - [Q39: Enterprise Angular Performance Optimization Checklist: track in @for, NgOptimizedImage, and Bundle Splitting](#q39-enterprise-angular-performance-optimization-checklist-track-in-for-ngoptimizedimage-and-bundle-splitting)
- [MODULE 16: BONUS SENIOR INTERVIEW ROUND QUESTIONS](#module-16-bonus-senior-interview-round-questions)
  - [Q40: Global Error Handling in Angular: Writing a Custom ErrorHandler for Centralized Logging](#q40-global-error-handling-in-angular-writing-a-custom-errorhandler-for-centralized-logging)
  - [Q41: Angular Security & XSS Protection: Built-in Sanitization, DomSanitizer, and CSP](#q41-angular-security--xss-protection-built-in-sanitization-domsanitizer-and-csp)
  - [Q42: Angular Server-Side Rendering (SSR) & Non-Destructive Hydration Internals](#q42-angular-server-side-rendering-ssr--non-destructive-hydration-internals)
  - [Q43: RxJS Operator Nuances: take(1) vs first() vs single() & shareReplay(1) Memory Leaks](#q43-rxjs-operator-nuances-take1-vs-first-vs-single--sharereplay1-memory-leaks)
- [MODULE 17: PRODUCTION ARCHITECTURE & SYSTEM DESIGN CASE STUDIES](#module-17-production-architecture--system-design-case-studies)
  - [Q44: Migrating Enterprise Angular Applications to Standalone Architecture & Control Flow](#q44-migrating-enterprise-angular-applications-to-standalone-architecture--control-flow)
  - [Q45: High-Throughput E-Commerce Cart & Live Pricing using Push-Pull Signal Graph](#q45-high-throughput-e-commerce-cart--live-pricing-using-push-pull-signal-graph)
  - [Q46: High-Scale Typeahead Catalog Search with Race-Condition Prevention](#q46-high-scale-typeahead-catalog-search-with-race-condition-prevention)
  - [Q47: High-Frequency Modal Dialogs: Preventing Detached DOM Memory Leaks](#q47-high-frequency-modal-dialogs-preventing-detached-dom-memory-leaks)
  - [Q48: High-Frequency 60 FPS Real-Time Canvas Rendering with NgZone Escaping](#q48-high-frequency-60-fps-real-time-canvas-rendering-with-ngzone-escaping)
  - [Q49: Silent JWT Token Refresh and Atomic Route Guiding in Modern Angular](#q49-silent-jwt-token-refresh-and-atomic-route-guiding-in-modern-angular)
  - [Q50: Enterprise State Management Architecture with NgRx SignalStore](#q50-enterprise-state-management-architecture-with-ngrx-signalstore)
  - [Q51: Real-Time Polling Dashboard Widget with Resilient Cleanup Architecture](#q51-real-time-polling-dashboard-widget-with-resilient-cleanup-architecture)
- [ADVANCED ENTERPRISE REFERENCE & PRODUCTION ARCHITECTURE](#advanced-enterprise-reference--production-architecture)
"""
    return header

print("Writing generator script...")
