MODULE_11 = '''---

# MODULE 11: MODERN ROUTING, NAVIGATION & LAZY LOADING

## Q29: Lazy Loading Standalone Components (loadComponent) vs Route Modules (loadChildren)
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 99% of modern architecture rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Modern Angular replaces the boilerplate of lazy-loaded feature modules (`loadChildren: () => import('./m').then(m => m.FeatureModule)`) with direct standalone component lazy-loading via **`loadComponent`**. This allows Webpack and Vite/esbuild to create fine-grained, self-contained JavaScript chunks. For nested sub-routes, modern Angular uses **`loadChildren: () => import('./routes').then(m => m.ROUTES)`** to lazily load route configuration arrays directly without `NgModule` wrappers, slashing initial bundle sizes and maximizing code splitting efficiency."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `NgModule` Lazy Loading (Shipping a Giant Wooden Freight Container):** You order a book from Amazon. The shipping company delivers an entire shipping container to your driveway containing the book, a table, a chair, and a wardrobe all locked inside.
  * **Modern `loadComponent` (Instant Digital Courier):** You tap "Read", and only the specific chapter PDF you requested is streamed directly to your tablet.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Routes } from '@angular/router';

export const APP_ROUTES: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  // 1. loadComponent: Lazily loads single standalone component chunk
  {
    path: 'dashboard',
    loadComponent: () => import('./features/dashboard/dashboard.component').then(m => m.DashboardComponent)
  },
  // 2. loadChildren: Lazily loads an array of child standalone routes (Zero NgModule!)
  {
    path: 'orders',
    loadChildren: () => import('./features/orders/order.routes').then(m => m.ORDER_ROUTES)
  }
];
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What happens if a developer imports a lazy-loaded standalone component in the `imports: [...]` array of the root component while also defining it in `loadComponent`?"  
  * *Senior Answer:* "This is a classic bundle bloat bug! If you statically import the component (`import { DashboardComponent } from '...'`) and include it in the root component's `imports` array, the compiler includes `DashboardComponent` in the **initial main JavaScript bundle**. Even though your route declares `loadComponent`, the lazy-loading benefit is completely defeated because the code was already downloaded eagerly during initial application bootstrap. Route standalone components must **never be statically imported by eager components**."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Route Target | Modern Syntax | Bundle Consequence | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Single Standalone Page** | `loadComponent: () => import(...).then(m => m.Comp)` | Emits isolated chunk (e.g. `dashboard.js`) | Ensure component is declared with `standalone: true`. |
| **Feature with multiple sub-routes** | `loadChildren: () => import(...).then(m => m.ROUTES)` | Lazily loads child route array chunk | Export `const ROUTES: Routes = [...]` in feature file. |
| **Initial landing / 404 page** | Eager `component: HomeComponent` | Bundled directly into `main.js` | Use strictly for the primary landing view to prevent navigation delay. |

---

## Q30: Functional Route Guards: CanActivateFn, CanDeactivateFn, and Atomic UrlTree Redirects
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Wells Fargo, Morgan Stanley, Walmart (Security & Navigation round).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular 15+ deprecated class-based guards (`implements CanActivate`) in favor of functional guards (**`CanActivateFn`**, **`CanDeactivateFn`**). Functional guards are composable functions that resolve dependencies via `inject()`. When authentication fails, a senior guard should **never call `this.router.navigate(['/login'])` imperatively and return `false`**; instead, it must return an **atomic `UrlTree`** using `router.parseUrl('/login')`. Returning a `UrlTree` cancels the current navigation and starts the new navigation atomically in a single pass, preventing race conditions and browser history corruption."
* **🧠 Intuitive Real-World Analogy:**  
  * **Imperative `router.navigate()` (The Confused Traffic Cop):** A traffic cop stops your car at a toll booth, shouts "Stop! You cannot enter!" (returns false), and then frantically runs across 3 lanes of traffic to manually steer your steering wheel toward an exit ramp. Other cars behind you crash into each other!
  * **Atomic `UrlTree` (The Automated Switch Track):** The electronic railroad switch smoothly shifts the track underneath the train directly toward the detour station in one fluid mechanical movement.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { inject } from '@angular/core';
import { CanActivateFn, Router, UrlTree } from '@angular/router';
import { AuthService } from './auth.service';

// 1. Functional CanActivate Guard returning atomic UrlTree:
export const authGuard: CanActivateFn = (route, state): boolean | UrlTree => {
  const auth = inject(AuthService);
  const router = inject(Router);

  // ✅ Returning UrlTree redirects atomically without race conditions!
  return auth.isLoggedIn() ? true : router.parseUrl(`/login?returnUrl=${encodeURIComponent(state.url)}`);
};

// 2. Functional CanDeactivate Guard: Unsaved changes check
export interface CanComponentDeactivate { hasUnsavedChanges: () => boolean; }
export const unsavedChangesGuard = (comp: CanComponentDeactivate) => {
  return comp.hasUnsavedChanges() ? confirm('You have unsaved changes. Leave page?') : true;
};
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why does returning `router.navigate(['/login'])` followed by `return false` cause subtle bugs in high-traffic or slow network environments?"  
  * *Senior Answer:* "`router.navigate()` launches a brand-new, secondary asynchronous navigation while the original primary navigation is still in the middle of resolving its guard chain. This causes Angular to fire conflicting `NavigationCancel` and `NavigationStart` events, pollutes browser history with aborted entries, and can lead to subtle race conditions where guards for the aborted route continue running in the background. Returning a `UrlTree` informs the router's internal navigation state machine to seamlessly redirect within the *same* navigation transition."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Guard Requirement | Guard Type | Return Signature | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Authentication check** | `CanActivateFn` | `boolean \| UrlTree \| Observable<boolean \| UrlTree>` | Return `router.parseUrl('/login')` on failure. |
| **Role-based permissions (Admin)** | `CanMatchFn` | `boolean \| UrlTree` | Skips matching route entirely; falls through to alternative routes. |
| **Preventing dirty form abandonment** | `CanDeactivateFn<T>` | `boolean \| Promise<boolean>` | Inspect component interface: `comp.isDirty()`. |
| **Combining multiple guards** | Function composition | Pipeline execution | Chain functions: `canActivate: [authGuard, roleGuard]`. |

---

## Q31: Modern Route Resolvers: ResolveFn vs Direct Signal Service Ingestion
* **Asked At:** Cognizant, Infosys, Capgemini, Persistent, Nagarro, EPAM (Modern UX and routing patterns).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "A Route Resolver (**`ResolveFn`**) pre-fetches essential data before a route is activated, guaranteeing the destination component only renders when data is fully available. In modern Angular with standalone routing, resolver data can be bound directly to component inputs using **`withComponentInputBinding()`**. However, if a resolver API takes 5 seconds, the UI stays completely frozen on the previous screen without user feedback. Therefore, modern senior architecture often replaces resolvers with **immediate navigation + skeleton loaders powered by Signal services**, or reserves resolvers strictly for critical, fast metadata."
* **🧠 Intuitive Real-World Analogy:**  
  * **Route Resolver (The Old-School Hotel):** You arrive at the reception desk. The receptionist refuses to let you into your hotel room until room service has laid out the hot dinner on your dining table. You stand waiting in the lobby for 45 minutes feeling trapped.
  * **Signal Skeleton Loader (Modern Five-Star Service):** The receptionist hands you your key immediately. You enter your air-conditioned room, sit on the couch (skeleton screen), and room service delivers your dinner 3 minutes later while you relax.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { inject } from '@angular/core';
import { ResolveFn, ActivatedRouteSnapshot } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { provideRouter, withComponentInputBinding } from '@angular/router';

// 1. Functional Resolver
export const productResolver: ResolveFn<any> = (route: ActivatedRouteSnapshot) => {
  return inject(HttpClient).get(`/api/products/${route.paramMap.get('id')}`);
};

// 2. app.config.ts: Automatically binds resolved data to component inputs!
export const appRoutingConfig = provideRouter(
  [{ path: 'product/:id', resolve: { product: productResolver }, loadComponent: () => import('./detail.component') }],
  withComponentInputBinding() // ✅ Resolved 'product' binds directly to input()!
);
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "How does `withComponentInputBinding()` change how components consume route parameters, query parameters, and resolver data?"  
  * *Senior Answer:* "By adding `withComponentInputBinding()` to `provideRouter()`, Angular automatically binds route path parameters (e.g. `:id`), query parameters (e.g. `?tab=details`), and resolved data keys (e.g. `resolve: { product }`) directly to matching component inputs! The component no longer needs to inject `ActivatedRoute` or subscribe to `paramMap` observables. You simply declare `id = input.required<string>()` and `product = input<Product>()`, and Angular populates them reactively."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Architecture Choice | When to Use | Trade-offs | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Functional `ResolveFn`** | Critical SEO metadata, small fast configuration payloads | Blocks page transition until HTTP call completes | Return `http.get()`; enable `withComponentInputBinding()`. |
| **Signal Service + Skeleton UI** | Heavy dashboards, medium/slow APIs, e-commerce | Page renders instantly; smooth perceived performance | Navigate immediately; set `isLoading = signal(true)`; fetch in service. |
| **Parameter Ingestion** | `withComponentInputBinding()` | Eliminates `ActivatedRoute.params.subscribe()` boilerplate | Add to `provideRouter()`; declare `id = input<string>()`. |
'''
