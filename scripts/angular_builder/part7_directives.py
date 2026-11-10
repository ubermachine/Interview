MODULE_7 = '''---

# MODULE 7: DIRECTIVES: BUILT-IN CONTROL FLOW & CUSTOM ATTRIBUTES

## Q21: Structural Directives (*ngIf, *ngFor) vs Modern Built-in Control Flow (@if, @for with track, @switch)
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 99% of modern Angular interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular 17 introduced built-in control flow syntax (`@if`, `@for`, `@switch`) directly into the compiler, completely replacing legacy microsyntax structural directives (`*ngIf`, `*ngFor`, `*ngSwitch`). Built-in control flow provides up to **90% faster template compilation**, eliminates the need to import `CommonModule`, provides strict TypeScript type narrowing across `@else` branches, natively supports `@empty` blocks, and makes the `track` expression mandatory in `@for`, permanently eliminating the infamous unoptimized list re-rendering bugs caused by forgetting `trackBy`."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `*ngIf` & `*ngFor` (Using Third-Party Intermediary Agents):** In older Angular, Angular had to wrap elements in invisible `<ng-template>` elements and instantiate a full Directive class (`NgForOf`) with multiple runtime dependency injections just to render a loop!
  * **Built-in Control Flow (Native CPU Instruction Set):** Modern control flow compiles directly into native JavaScript `if/else` and `for` loops inside the template's generated type-check and render functions—zero directive overhead, zero indirection.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, signal } from '@angular/core';

interface Product { id: string; name: string; inStock: boolean; }

@Component({
  selector: 'app-catalog',
  standalone: true,
  template: `
    @if (isLoading()) {
      <p>Loading catalog...</p>
    } @else if (products().length > 0) {
      <ul>
        @for (item of products(); track item.id; let idx = $index, count = $count) {
          <li>#{{ idx + 1 }}/{{ count }}: {{ item.name }}</li>
        } @empty {
          <li>No products available in this category.</li>
        }
      </ul>
    }
  `
})
export class CatalogComponent {
  isLoading = signal(false);
  products = signal<Product[]>([ { id: 'P-1', name: 'MacBook Pro', inStock: true } ]);
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why is `track` mandatory in `@for`, and why is using `track $index` dangerous when rendering dynamic lists with user inputs or animations?"  
  * *Senior Answer:* "The `track` expression is mandatory because Angular uses it to uniquely identify DOM nodes across array mutations. If you use `track $index`, Angular associates the DOM node with the array position rather than the data entity. If you delete Item #1, Item #2 shifts to index 0; Angular will **reuse the first DOM element for the second item**, causing unchecked form inputs, focus states, CSS animations, and child component states to stay attached to the wrong item! You must always track a stable, unique business key (`track item.id`). Only use `track $index` for strictly static, immutable, read-only lists."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Syntax / Feature | Legacy Structural Directive | Modern Control Flow (v17+) | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Conditional display** | `*ngIf="condition; else alt"` | `@if (condition) { } @else { }` | Use `@if`; supports multi-branch `@else if` and type narrowing without `ng-template`. |
| **List rendering** | `*ngFor="let item of list; trackBy: fn"` | `@for (item of list; track item.id)` | Use `@for`; always track unique identifier (`item.id`). |
| **Empty list fallback** | Requires separate `*ngIf="list.length === 0"` | `@empty { <p>No items</p> }` | Append `@empty` block directly inside `@for`. |
| **Multi-condition switch** | `[ngSwitch]` + `*ngSwitchCase` | `@switch (val) { @case (x) { } }` | Replace heavy switch directives with native `@switch`. |

---

## Q22: Custom Attribute Directives using ElementRef, Renderer2, and Modern host Property Bindings
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Persistent, EPAM (Custom directives and DOM security).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Attribute directives modify the behavior, appearance, or accessibility of existing DOM elements. Direct DOM manipulation using `ElementRef.nativeElement` is a severe security vulnerability (XSS) and breaks Server-Side Rendering (SSR) because the DOM API does not exist in Node.js. Senior engineers use **`Renderer2`** for safe, platform-agnostic DOM transformations. Furthermore, modern Angular deprecates `@HostBinding()` and `@HostListener()` in favor of the **`host` property** inside the `@Directive` decorator metadata, creating cleaner, faster, and statically analyzable host bindings."
* **🧠 Intuitive Real-World Analogy:**  
  * **Direct `ElementRef.nativeElement` (Surgical Blade without Gloves):** You directly touch and modify the physical organs of the patient. If you operate in a different environment (Node.js SSR / Web Worker), the patient dies because there is no physical body to touch!
  * **`Renderer2` (Robotic Surgical Arms):** You issue abstract commands: "Apply red color to surface". The robotic adapter knows how to translate this safely whether operating in a real browser hospital, a cloud server test chamber, or a mobile webview.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Directive, ElementRef, Renderer2, inject, input } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true,
  host: {
    // ✅ Modern Host Bindings (Replaces @HostListener and @HostBinding)
    '(mouseenter)': 'onMouseEnter()',
    '(mouseleave)': 'onMouseLeave()',
    '[style.cursor]': '"pointer"'
  }
})
export class HighlightDirective {
  private el = inject(ElementRef);
  private renderer = inject(Renderer2);
  highlightColor = input('yellow', { alias: 'appHighlight' });

  onMouseEnter() { this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.highlightColor()); }
  onMouseLeave() { this.renderer.removeStyle(this.el.nativeElement, 'backgroundColor'); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why did Angular introduce the `host` property in `@Directive` / `@Component` and recommend against `@HostBinding` and `@HostListener`?"  
  * *Senior Answer:* "`@HostBinding` and `@HostListener` are decorator-based annotations that scatter host binding declarations throughout the TypeScript class body. This causes runtime reflection overhead, makes it difficult for developers and compilers to see all host interactions in one glance, and causes inheritance conflicts when extending classes. The `host: { ... }` object in decorator metadata centralizes all DOM events, classes, attributes, and styles into a single declarative object that the compiler optimizes into direct template instructions with zero runtime decorator overhead."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| DOM Requirement | What to Use | SSR Safe? | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Safe style/class manipulation** | `Renderer2.setStyle()` / `addClass()` | **YES** | Inject `Renderer2`; use `setStyle`/`removeStyle` instead of `nativeElement.style`. |
| **Binding host events (click, hover)** | `host: { '(click)': 'onClick()' }` | **YES** | Declare inside directive metadata `host` object. Avoid `@HostListener`. |
| **Binding host classes / attributes** | `host: { '[class.active]': 'isActive()' }` | **YES** | Bind directly to properties or signals inside metadata `host` object. |
| **Direct native DOM access (measuring canvas)** | `ElementRef.nativeElement` | **NO** (Browser only) | Guard with `if (isPlatformBrowser(platformId))` before accessing `nativeElement`. |
'''
