MODULE_9 = '''---

# MODULE 9: HIERARCHICAL DEPENDENCY INJECTION & PROVIDERS

## Q24: Hierarchical DI: Root Injector vs Environment/Module Injector vs Element/Component Injector
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo (Asked in 98% of architectural rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular's Dependency Injection system is hierarchical and tree-structured, consisting of two main injector hierarchies: the **Environment Hierarchy** (starting at `NullInjector` -> `PlatformInjector` -> `RootInjector` (`providedIn: 'root'`) -> Route/Environment Injectors) and the **Element Hierarchy** (created for each DOM component or directive via `providers: [...]` or `viewProviders: [...]`). When a component requests a dependency, Angular resolves it locally at the Element Injector; if not found, it bubbles up through parent Element Injectors to the Environment/Root Injector before failing at `NullInjector`."
* **🧠 Intuitive Real-World Analogy:**  
  * **Root Injector (`providedIn: 'root'` - The Central City Water Supply):** One shared main pipeline for the entire city. Every house in the city drinks from this single shared reservoir.
  * **Element / Component Injector (`providers: [CartService]` - A Private Rooftop Water Tank):** A specific apartment building installs its own private rooftop water tank. The residents of that building drink exclusively from their private tank. When the building is demolished, the private tank is destroyed with it.
  * **`NullInjector`:** The boundary of the known universe. If water isn't found anywhere in the state, it throws a drought alert (`NullInjectorError: No provider for X!`).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, Injectable } from '@angular/core';

// 1. Root Injector: Application-wide singleton
@Injectable({ providedIn: 'root' })
export class GlobalAuthService { user = 'Admin'; }

// 2. Component/Element Injector: Isolated instance per component lifecycle
@Injectable()
export class WizardStateService { currentStep = 1; }

@Component({
  selector: 'app-checkout-wizard',
  standalone: true,
  providers: [WizardStateService], // ✅ New instance scoped strictly to this wizard tree!
  template: `<p>Step: {{ wizard.currentStep }}</p>`
})
export class CheckoutWizardComponent {
  constructor(public wizard: WizardStateService, public auth: GlobalAuthService) {}
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "If Service A is provided in `providedIn: 'root'`, and Component B also declares `providers: [Service A]`, which instance does Component B and its child components receive?"  
  * *Senior Answer:* "Component B and all of its nested children will receive a **brand-new, localized instance** created by Component B's Element Injector, shadowing the root singleton! Any state mutations Component B performs on Service A will only affect its local instance; the rest of the application will continue interacting with the untouched root singleton instance. When Component B is destroyed, its local Service A instance is destroyed and garbage-collected."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Injector Scope | Configuration Syntax | Instance Lifetime | Best Enterprise Use Case |
| :--- | :--- | :--- | :--- |
| **Root Singleton** | `@Injectable({ providedIn: 'root' })` | App lifetime (1 instance) | Auth services, API clients, global caches, notification brokers. |
| **Route-Scoped / Environment** | `providers: [...]` in Route definition | Active route lifetime | Feature stores, route resolvers, module-specific configurations. |
| **Component-Scoped / Element** | `@Component({ providers: [Service] })` | Component DOM lifetime | Isolated multi-step wizard state, modal dialog controllers, tabs. |
| **View-Scoped** | `@Component({ viewProviders: [S] })` | Scoped only to template view | Prevents projected content (`<ng-content>`) from injecting the service. |

---

## Q25: Provider Configuration: useClass vs useExisting vs useFactory vs useValue & Multi-Providers
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Persistent, Nagarro, EPAM (Asked in 95% of senior interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular DI providers map an `InjectionToken` to an implementation using four core recipes: **`useClass`** instantiates a new instance of an alternative class (ideal for mocking services in unit tests); **`useExisting`** aliases an existing provider token to another token without creating a duplicate instance; **`useValue`** injects a static configuration object, primitive, or constant; and **`useFactory`** invokes a dynamic factory function with resolved DI dependencies. Setting **`multi: true`** allows multiple providers to register under a single token, producing an array of implementations (such as `HTTP_INTERCEPTORS` or `APP_INITIALIZER`)."
* **🧠 Intuitive Real-World Analogy:**  
  * **`useClass`:** You order a Toyota taxi, and the dispatcher sends a brand-new electric BYD car instead.
  * **`useExisting`:** Calling someone by their nickname: "Babu" and "Dr. Amit Roy" are the exact same human being living in that house.
  * **`useValue`:** Pasting a sticky note with your Wi-Fi password on the refrigerator.
  * **`useFactory`:** Ordering a custom birthday cake: the baker reads the dietary allergies, bakes the cake dynamically, and delivers the finished cake.
  * **`multi: true` (Multi-Plug Surge Protector):** One wall power strip into which you plug a laptop charger, phone charger, and monitor simultaneously.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { InjectionToken, inject } from '@angular/core';

export const API_URL = new InjectionToken<string>('API_URL');
export const LOGGER_TOKEN = new InjectionToken<any>('LOGGER_TOKEN');

export const appProviders = [
  // 1. useValue: Static config injection
  { provide: API_URL, useValue: 'https://api.enterprise.com/v1' },
  // 2. useClass: Swapping implementation (e.g. MockAuthService during testing)
  { provide: AuthService, useClass: environment.production ? AuthService : MockAuthService },
  // 3. useExisting: Alias without new instance
  { provide: ModernLogger, useExisting: LegacyLogger },
  // 4. useFactory: Dynamic generation with dependencies
  { provide: ConfigService, useFactory: () => inject(HttpClient).get('/config.json') },
  // 5. multi: true: Accumulating multiple items in an array
  { provide: LOGGER_TOKEN, useValue: new ConsoleLogger(), multi: true },
  { provide: LOGGER_TOKEN, useValue: new CloudLogger(), multi: true }
];
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What is the critical difference between `useClass` and `useExisting`? What happens if you use `useClass` to alias an existing singleton?"  
  * *Senior Answer:* "The critical difference is **instance creation**: `useClass` creates a **brand-new instance** of the specified class. If you write `{ provide: TokenB, useClass: ServiceA }`, Angular instantiates a second, completely separate instance of `ServiceA`. Any state mutations made via `TokenB` will not reflect in `ServiceA`! If you want both tokens to reference the exact same singleton instance in memory, you must use `useExisting`: `{ provide: TokenB, useExisting: ServiceA }`."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Provider Recipe | Creates New Instance? | Best Production Use Case | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`useValue`** | No (Injects constant) | App configuration objects, API base URLs, feature flags. | `{ provide: CONFIG_TOKEN, useValue: APP_CONFIG }` |
| **`useClass`** | **YES** (Always instantiates) | Mocking dependencies in tests; platform-specific service swaps. | `{ provide: PaymentService, useClass: MockPaymentService }` |
| **`useExisting`** | **NO** (Points to existing) | Narrowing API interfaces; aliasing old token to new service. | `{ provide: ReadOnlyStore, useExisting: FullStoreService }` |
| **`useFactory`** | Yes (Via function return) | Complex dynamic initialization; conditional service wiring. | `{ provide: Theme, useFactory: (d: Device) => d.isDark ? ... }` |
| **`multi: true`** | Appends to Token Array | Plugin architectures, interceptors, initializers (`APP_INITIALIZER`). | Add `multi: true` to all provider objects for that token. |

---

## Q26: Modern Functional DI: inject() vs Constructor Injection & Injection Context Rules
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Deloitte, EY, Morgan Stanley, Wells Fargo (Modern Angular 14-18+ architecture question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "The `inject()` function enables functional dependency injection without the boilerplate of verbose constructor parameters and `super()` plumbing in class hierarchies. More importantly, it unlocks **composable functional utilities** (like reusable functional route guards, interceptors, and custom reactive helpers). However, `inject()` can **only be invoked within an active Injection Context**—such as during class property initialization, constructor execution, or inside `runInInjectionContext()`. Calling it inside asynchronous callbacks or lifecycle hooks throws runtime error `NG0203`."
* **🧠 Intuitive Real-World Analogy:**  
  * **Constructor Injection (The Traditional Form):** You apply for an Aadhaar card. The form has 10 mandatory blank boxes printed on page 1. Every time you create an instance, you must fill out every box in the exact order. If you inherit from a base class, you must duplicate all 10 fields and pass them down with `super()`.
  * **`inject()` Function (The Smart Card Reader):** You tap your card on the reader anywhere on your desk during check-in, and your credentials are retrieved instantly on demand.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, inject, DestroyRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

// Reusable Composable Functional Utility:
export function injectRouteParam(paramName: string) {
  const route = inject(ActivatedRoute); // ✅ Valid because invoked during construction!
  return route.snapshot.paramMap.get(paramName);
}

@Component({ selector: 'app-product-detail', standalone: true, template: `...` })
export class ProductDetailComponent {
  private http = inject(HttpClient);           // ✅ Clean property injection
  productId = injectRouteParam('id');           // ✅ Custom composable utility
  destroyRef = inject(DestroyRef);

  handleAsyncAction() {
    // ❌ WRONG: Calling inject(HttpClient) here throws NG0203!
    // ✅ Must use this.http stored from the constructor injection context
    this.http.get(`/api/products/${this.productId}`).subscribe();
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What is `runInInjectionContext` and when is it required?"  
  * *Senior Answer:* "`runInInjectionContext(injector, fn)` allows you to programmatically create an injection context at arbitrary points in time outside class instantiation. For example, if an asynchronous callback, WebSocket listener, or third-party library event arrives and you need to execute code that invokes `inject()` (or creates an `effect()` or `toSignal()`), calling it normally throws `NG0203`. By injecting an `EnvironmentInjector` beforehand and wrapping the execution in `runInInjectionContext(this.injector, () => { ... })`, Angular restores the active injection scope."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Injection Style | Where It Can Run | Key Benefits | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`inject(Token)`** | Property initializers, constructors, factory functions | Clean composable functions; no `super()` chaining needed. | `private http = inject(HttpClient);` at field declaration level. |
| **Constructor DI** | `constructor(private http: HttpClient)` | Legacy standard; familiar across OOP frameworks. | Maintained for legacy codebases; migrate new features to `inject()`. |
| **Async / Callback Injection** | Inside `runInInjectionContext(injector, fn)` | Enables functional DI in deferred or asynchronous events. | Inject `EnvironmentInjector` in constructor; pass to `runInInjectionContext`. |
| **`NG0203` Error Prevention** | Class initialization time | Prevents runtime injection failures. | Never call `inject()` inside lifecycle hooks (`ngOnInit`) or event handlers. |
'''
