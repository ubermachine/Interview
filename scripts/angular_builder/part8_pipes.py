MODULE_8 = '''---

# MODULE 8: PIPES: PURE VS IMPURE ARCHITECTURE

## Q23: Pure vs Impure Pipes: Change Detection Cycles, In-Memory Caching & Performance Risks
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 95% of performance & core rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Pipes transform template data declaratively. The fundamental architectural difference lies in their execution trigger: **Pure pipes (`pure: true`, the default)** execute ONLY when their input value changes by primitive value or object reference identity (`!==`). Angular caches (memoizes) the return value across change detection cycles. Conversely, **Impure pipes (`pure: false`)** execute on **every single change detection cycle**—every keystroke, mouse movement, timer, and resolved Promise. Implementing heavy array filtering or complex calculations inside an impure pipe is a catastrophic performance anti-pattern that can trigger thousands of evaluations per second."
* **🧠 Intuitive Real-World Analogy:**  
  * **Pure Pipe (The Fast Toll Booth FastTag Scanner):** A car drives past the toll barrier. The scanner reads the car's license plate. If the same car hasn't moved, the toll gate stays open without rescanning. It only rescans when a *different* car arrives.
  * **Impure Pipe (The Over-Zealous Ticket Inspector):** An inspector who stands inside the train car and demands to re-check and punch your ticket every 3 seconds for the entire 4-hour journey!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Pipe, PipeTransform } from '@angular/core';

// 1. PURE PIPE (Default): Memoized, only re-evaluates when input changes by identity
@Pipe({ name: 'inrCurrency', standalone: true, pure: true })
export class InrCurrencyPipe implements PipeTransform {
  transform(value: number, showSymbol = true): string {
    return (showSymbol ? '₹' : '') + value.toLocaleString('en-IN', { maximumFractionDigits: 2 });
  }
}

// ⚠️ IMPURE PIPE CODE SMELL: Re-evaluates on EVERY single change detection tick!
@Pipe({ name: 'badFilter', standalone: true, pure: false })
export class BadFilterPipe implements PipeTransform {
  transform(items: any[], term: string): any[] {
    console.warn('⚠️ FIRES HUNDREDS OF TIMES A SECOND!');
    return items?.filter(i => i.name.toLowerCase().includes(term.toLowerCase())) || [];
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why doesn't Angular include a built-in `FilterPipe` or `OrderByPipe` like AngularJS 1.x did? How should a senior engineer implement list filtering in modern Angular?"  
  * *Senior Answer:* "The Angular core team intentionally removed `FilterPipe` and `OrderByPipe` because an array filter pipe must be declared `pure: false` to detect when someone pushes or removes an item from an array without changing the array reference. An impure filter pipe iterates and clones the entire array on **every single tick of the change detection loop**, causing massive GC pressure and UI frame drops. In modern Angular, list filtering must be performed **inside the component class using a `computed()` signal** or in an RxJS pipeline (`combineLatest`), executing the filter strictly when the search query or items array actually changes."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Pipe Strategy | When It Executes | Performance Rating | Best Use Case / Action |
| :--- | :--- | :--- | :--- |
| **Pure Pipe (`pure: true`)** | When input primitive or reference changes (`!==`) | ⚡ **Ultra Fast (O(1) Cache Hit)** | Currency formatting, date formatting, uppercase transforms, unit conversions. |
| **Impure Pipe (`pure: false`)** | On **EVERY** change detection cycle | ⚠️ **Extremely Dangerous if abused** | Only for reactive pipes holding internal subscriptions (e.g. Angular's built-in `AsyncPipe`). |
| **Array Filtering / Sorting** | Derived state in component | ⚡ **Optimal O(K)** | **Never use an impure pipe!** Use `filteredItems = computed(() => this.items().filter(...));`. |
'''
