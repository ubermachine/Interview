MODULE_15 = '''---

# MODULE 15: PERFORMANCE TUNING & ENTERPRISE OPTIMIZATIONS

## Q38: Deferrable Views (@defer, @placeholder, @loading, @error) and Trigger Conditions
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Walmart (Cutting-edge Angular 17-18 performance round).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Deferrable Views (**`@defer`**) revolutionize Angular bundle splitting by enabling declarative, template-level lazy-loading. Any standalone components, directives, pipes, and associated CSS used inside an `@defer` block are automatically extracted into separate JavaScript chunks by the compiler. These chunks are only fetched from the server when specific trigger conditions are met (e.g. `on viewport`, `on idle`, `on interaction`, `on timer`, or custom `when condition`). It includes coordinated blocks for `@placeholder`, `@loading` (with minimum display timers to prevent visual flicker), and `@error`."
* **🧠 Intuitive Real-World Analogy:**  
  * **Traditional Eager Template (Loading All 500 Pages of an Encyclopedia):** When you open a webpage, the browser downloads the heavy analytics chart, the PDF export generator, and the comments widget—even though they sit at the very bottom of the page 3,000 pixels below the screen fold.
  * **`@defer (on viewport)` (Lazy Smart Delivery):** The browser loads only the visible top article. A lightweight placeholder is drawn for the bottom chart. As the user scrolls down and the placeholder approaches the viewport, the browser quietly streams the chart JavaScript bundle and renders it seamlessly.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component } from '@angular/core';
import { HeavyStockChartComponent } from './heavy-stock-chart.component';

@Component({
  selector: 'app-perf-dashboard',
  standalone: true,
  imports: [HeavyStockChartComponent],
  template: `
    <!-- ✅ Lazily downloads HeavyStockChart chunk only when scrolled into view! -->
    @defer (on viewport; prefetch on idle) {
      <app-heavy-stock-chart />
    } @placeholder (minimum 500ms) {
      <div class="skeleton-chart">Scroll to view chart...</div>
    } @loading (after 100ms; minimum 300ms) {
      <div class="spinner">Downloading chart engine...</div>
    } @error {
      <p class="error">Failed to load chart module.</p>
    }
  `
})
export class PerfDashboardComponent {}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What prevents a component inside an `@defer` block from being code-split into a lazy chunk?"  
  * *Senior Answer:* "If the deferred component is **statically referenced anywhere outside the `@defer` block** in the same component's template or in any other eagerly-loaded component in that compilation unit, the compiler cannot code-split it! Because an eager code path exists, Webpack/esbuild must bundle the component directly into the main chunk, completely defeating `@defer`. Furthermore, components deferred inside `@defer` must be **standalone**; `NgModule`-declared components cannot be individually code-split by `@defer`."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Trigger Condition | When Chunk is Downloaded | Best Enterprise Use Case | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`on viewport`** | When placeholder enters user screen | Below-the-fold heavy charts, footer widgets, comments. | Always provide `@placeholder` with height so viewport trigger can detect it. |
| **`on idle`** | When browser requestIdleCallback fires | Non-urgent secondary widgets, help modals. | Default trigger; loads when main thread is idle. |
| **`on interaction(btn)`** | When user clicks or focuses trigger element | Heavy modal dialogs, export dialogs, complex filters. | Declare `#btn` on trigger; use `@defer (on interaction(btn))`. |
| **`prefetch on idle`** | Prefetches JS chunk in background early | Reduces perceived rendering lag when trigger fires. | Pair triggers: `@defer (on viewport; prefetch on idle)`. |

---

## Q39: Enterprise Angular Performance Optimization Checklist: track in @for, NgOptimizedImage, and Bundle Splitting
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Walmart (The Lead Architect Performance Auditing question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Senior Angular performance optimization targets three critical browser rendering metrics: **Core Web Vitals (LCP, INP, CLS)**, **Memory GC Footprint**, and **Initial JavaScript Payload Size**. A production-ready performance checklist mandates: 1) `ChangeDetectionStrategy.OnPush` across 100% of components, 2) mandatory unique identity expressions in `@for (item of items; track item.id)`, 3) using **`NgOptimizedImage` (`ngSrc`)** with `priority` flags for hero images to eliminate Largest Contentful Paint delays, 4) route and `@defer` chunk splitting, and 5) migrating to Zoneless microtask scheduling to eliminate `zone.js` runtime overhead."
* **🧠 Intuitive Real-World Analogy:**  
  * Optimizing an enterprise Angular frontend is like tuning a Formula 1 race car:
    * **`OnPush` & Signals:** Removing 200 kg of unnecessary iron chassis (eliminating whole-tree dirty checking).
    * **`NgOptimizedImage`:** Aerodynamic low-drag tires ensuring maximum immediate acceleration off the start line (sub-second LCP).
    * **`track item.id`:** Precision pit-stop crew that only changes the single flat tire rather than dismantling the entire car engine at every pit stop.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, ChangeDetectionStrategy } from '@angular/core';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-hero-banner',
  standalone: true,
  imports: [NgOptimizedImage],
  changeDetection: ChangeDetectionStrategy.OnPush, // 1. Subtree Pruning
  template: `
    <!-- 2. NgOptimizedImage: Automatic srcset, lazy loading, LCP priority, CLS prevention -->
    <img 
      [ngSrc]="heroImage" 
      width="1200" 
      height="600" 
      priority 
      alt="Exclusive Diwali Shopping Offers" />
  `
})
export class HeroBannerComponent {
  heroImage = '/assets/images/diwali-banner.webp';
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why does `NgOptimizedImage` mandate explicit `width` and `height` attributes (or `fill`), and what happens if you forget them?"  
  * *Senior Answer:* "`NgOptimizedImage` enforces explicit `width` and `height` attributes (or the `fill` directive with aspect ratio) specifically to eliminate **Cumulative Layout Shift (CLS)**. When dimensions are omitted, the browser cannot reserve physical screen space before image bytes arrive over the network, causing content below the image to jerk downward when rendering finishes. If dimensions are omitted, the Angular compiler throws a build/runtime error warning you that Core Web Vitals will be penalized."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Performance Metric | Primary Root Cause | Senior Production Fix | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **High LCP (Slow Hero Images)** | Unoptimized image sizes, late network fetch | `NgOptimizedImage` with `priority` | Use `ngSrc="..."`, provide explicit `width`/`height`, add `priority` for above-the-fold hero images. |
| **UI Stutter on List Updates** | Re-creating all DOM nodes on array update | `@for (item of list; track item.id)` | Never use `track $index` on mutating lists; always track unique database ID. |
| **High Initial Bundle Size (>2MB)** | Eagerly loading non-landing features | `loadComponent` and `@defer` | Split routes with `loadComponent`; defer below-fold charts with `@defer (on viewport)`. |
| **High INP (Interaction to Next Paint)** | Heavy Zone.js whole-tree CD checking | `OnPush` + Zoneless Signals | Migrate components to `OnPush`; enable `provideExperimentalZonelessChangeDetection()`. |
'''
