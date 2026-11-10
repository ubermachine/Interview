MODULE_13 = '''---

# MODULE 13: MEMORY LEAK PREVENTION & TEARDOWN MECHANICS

## Q34: Root Causes of Angular Memory Leaks: Uncancelled Subscriptions & Detached DOM Trees
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Walmart (Asked in 99% of senior technical audits).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular memory leaks predominantly occur when a short-lived component subscribes to a **long-lived Observable** (such as a root singleton service, `Router.events`, or `fromEvent(window)`) without unsubscribing when the component is destroyed. The long-lived Observable maintains a closure reference to the subscriber callback, which in turn retains a reference to the component instance (`this`). Because the component instance still references its template DOM elements, the JavaScript V8 Garbage Collector cannot sweep the component, creating a **Detached DOM Tree memory leak** that steadily increases browser RAM until the tab crashes."
* **🧠 Intuitive Real-World Analogy:**  
  * **The Uncancelled Gym Membership:** You move from Bengaluru to Delhi. However, your bank account in Bengaluru is set to auto-debit your gym membership every month. Even though you don't live in Bengaluru anymore, the gym still keeps your file open in their active filing cabinet, and your bank keeps paying them money forever until you explicitly walk in and submit a cancellation notice!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, OnInit, OnDestroy, inject } from '@angular/core';
import { GlobalChatService } from './global-chat.service';
import { Subscription } from 'rxjs';

@Component({ selector: 'app-leak-demo', standalone: true, template: `...` })
export class LeakDemoComponent implements OnInit, OnDestroy {
  private chat = inject(GlobalChatService); // Singleton service (lives forever)
  private sub?: Subscription;

  ngOnInit() {
    // ❌ DANGEROUS: If sub is not unsubscribed, component & DOM stay leaked in RAM forever!
    this.sub = this.chat.messages$.subscribe(msg => {
      console.log('Received message in modal', msg);
    });
  }
  ngOnDestroy() {
    // ✅ SENIOR TEARDOWN: Sever the closure link so GC can free memory!
    this.sub?.unsubscribe();
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Do Angular `HttpClient` calls (e.g. `this.http.get('/api/data').subscribe()`) cause memory leaks if you don't unsubscribe?"  
  * *Senior Answer:* "No, `HttpClient` Observables do **not** cause permanent memory leaks because Angular's `HttpClient` automatically calls `observer.complete()` immediately after emitting the single HTTP response. Upon completion, RxJS internally tears down its observer list and releases closure references, allowing the Garbage Collector to free the component. **However**, failing to unsubscribe from in-flight HTTP requests can still cause unwanted side effects if the response arrives *after* the component has unmounted (e.g. attempting to update destroyed UI state), which is why cancelling in-flight requests with `takeUntilDestroyed()` is still best practice."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Observable Source | Auto-Completes? | Memory Leak Risk? | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`HttpClient` (`http.get`, `post`)** | **YES** (Emits 1 value and completes) | **LOW** (Temporary pending leak only) | Unsubscribe with `takeUntilDestroyed()` to abort useless pending requests on navigation. |
| **Singleton Services (`BehaviorSubject`, events)** | **NO** (Lives for entire app lifetime) | 🚨 **EXTREME (Permanent Detached DOM Leak)** | **MANDATORY TEARDOWN:** Use `takeUntilDestroyed()` or `AsyncPipe`. |
| **Global Window / DOM Events (`fromEvent(window)`)** | **NO** (Lives until window closes) | 🚨 **EXTREME** | Must unsubscribe or use `DestroyRef.onDestroy()`. |
| **ActivatedRoute (`route.params`, `queryParams`)** | **YES** (Scoped to component route) | **NONE** (Angular tears down route scope) | Safe without manual unsubscribe, but good practice to keep consistent. |

---

## Q35: Modern Teardown Patterns: takeUntilDestroyed(), DestroyRef.onDestroy(), and AsyncPipe
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Persistent, Nagarro, EPAM (Asked in 99% of modern Angular code reviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Modern Angular completely eliminates the legacy boilerplate of declaring a `private destroy$ = new Subject<void>()`, emitting `next()` in `ngOnDestroy`, and chaining `takeUntil(this.destroy$)`. We now use **`takeUntilDestroyed()`** from `@angular/core/rxjs-interop`. When called within an active injection context (constructor or field initializers), it automatically discovers the component's **`DestroyRef`** and cancels the subscription upon DOM unmount. For non-RxJS teardown (such as `clearInterval`, WebSockets, or third-party JS charts), we register cleanup callbacks directly via **`DestroyRef.onDestroy(() => ...)`**."
* **🧠 Intuitive Real-World Analogy:**  
  * **Legacy `Subject + takeUntil` (Manual Signature Stamp):** Every time you check into an office, you have to stamp a physical paper badge, and remember to stamp it again when leaving, or the security gates lock you in.
  * **Modern `takeUntilDestroyed()` (RFID Badge with Auto-Deactivation):** Your badge automatically deactivates the millisecond your badge turns past the exit turnstile. Zero manual signatures, zero human error.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, inject, DestroyRef } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { interval } from 'rxjs';
import { StockTickerService } from './stock-ticker.service';

@Component({ selector: 'app-modern-teardown', standalone: true, template: `...` })
export class ModernTeardownComponent {
  private ticker = inject(StockTickerService);
  private destroyRef = inject(DestroyRef);

  constructor() {
    // 1. Modern RxJS Teardown: Automatically unhooks when component destroyed!
    this.ticker.prices$.pipe(takeUntilDestroyed()).subscribe(price => console.log(price));

    // 2. Modern Non-RxJS Cleanup (intervals, DOM listeners, third-party libraries):
    const timerId = setInterval(() => console.log('Heartbeat ping'), 5000);
    this.destroyRef.onDestroy(() => clearInterval(timerId)); // ✅ Clean teardown!
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What runtime error occurs if you call `takeUntilDestroyed()` inside `ngOnInit()`, and how do you resolve it?"  
  * *Senior Answer:* "Calling `takeUntilDestroyed()` inside `ngOnInit()` throws runtime error **`NG0203: takeUntilDestroyed can only be used within an injection context`**. Because `ngOnInit` executes after class construction has finished, the injection context is no longer active. To resolve this outside the constructor, you must inject `DestroyRef` in your constructor/field initializer (`private destroyRef = inject(DestroyRef)`) and pass it explicitly into the operator: `takeUntilDestroyed(this.destroyRef)`."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Teardown Mechanism | Context Requirement | Best Use Case | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`takeUntilDestroyed()`** | Inside Constructor / Field init | RxJS stream subscription teardown | Pipe directly: `stream$.pipe(takeUntilDestroyed()).subscribe(...)`. |
| **`takeUntilDestroyed(destroyRef)`** | Outside Constructor (e.g. `ngOnInit` or methods) | Late-bound RxJS stream subscriptions | Pass explicit ref: `pipe(takeUntilDestroyed(this.destroyRef))`. |
| **`DestroyRef.onDestroy(() => ...)`** | Injectable anywhere | Non-RxJS resources (`setInterval`, Canvas, Chart.js) | Register cleanup function: `this.destroyRef.onDestroy(() => chart.destroy())`. |
| **`AsyncPipe` (`\| async`)** | In HTML Template | Declarative Observable template rendering | Angular handles subscription and unsubscription automatically. |
| **`toSignal(obs$)`** | Inside Injection Context | Declarative conversion of stream to Signal | Angular automatically unsubscribes when component scope is destroyed. |
'''
