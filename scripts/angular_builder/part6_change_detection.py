MODULE_6 = '''---

# MODULE 6: CHANGE DETECTION STRATEGIES & ZONELESS ARCHITECTURE

## Q18: Default vs ChangeDetectionStrategy.OnPush & Why Immutability is Mandatory
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Morgan Stanley, Wells Fargo, Walmart (Asked in 99% of senior performance rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Under default change detection, Angular traverses the entire component tree from root to leaf on every single asynchronous event patched by `zone.js` (every click, timer, HTTP response). `ChangeDetectionStrategy.OnPush` optimizes this by pruning entire component subtrees from dirty checking. An `OnPush` component will **only** be re-checked if: 1) an `@Input()` reference changes by identity (`!==`), 2) a DOM event originates from that component or its children, 3) an `AsyncPipe` or Angular Signal emits, or 4) `ChangeDetectorRef.markForCheck()` is called manually. Because inputs are checked by reference identity, **immutability is mandatory**."
* **🧠 Intuitive Real-World Analogy:**  
  * **Default Change Detection (The Colony Watchman Knocking on Every Door):** Whenever the postman brings a letter to the front gate, the security guard walks through all 200 villas in the gated society, knocking on every single bedroom door asking "Is this letter for you?" even if the letter is clearly addressed to Villa #5!
  * **OnPush Strategy (The Smart Society Intercom):** The security guard sits at the gate. If a package arrives, he rings only the specific intercom of Villa #5. The other 199 villas remain completely undisturbed.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, ChangeDetectionStrategy, input } from '@angular/core';

export interface UserProfile { id: string; name: string; balance: number; }

@Component({
  selector: 'app-user-badge',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush, // ✅ OnPush Pruning Enabled
  template: `<div><h3>{{ user().name }}</h3><p>Balance: ₹{{ user().balance }}</p></div>`
})
export class UserBadgeComponent {
  user = input.required<UserProfile>(); // Checked by referential identity (Object.is)
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "If you push an item into an array with `this.items.push(newItem)` in a parent component, and pass `items` into an `OnPush` child component, why does the child component NOT update?"  
  * *Senior Answer:* "`OnPush` relies on JavaScript referential identity (`Object.is` / `===`). When you call `items.push()`, you mutate the existing array in-place; its memory address on the V8 heap remains identical. During change detection, Angular compares `prevInput === currInput` (which returns `true`), assumes nothing changed, and completely skips checking the child component! To make `OnPush` detect the update, you must produce a **brand-new array reference**: `this.items = [...this.items, newItem]`, or use an Angular Signal (`items.update(l => [...l, newItem])`)."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Change Detection Mode | Dirty Checking Scope | Performance Impact | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Default (`CheckAlways`)** | Entire application tree from root to leaf | O(N) where N = total DOM bindings in app; causes micro-stutters. | Avoid for production enterprise apps; migrate to OnPush. |
| **`OnPush`** | Only pruned subtree when input reference changes or event fires | O(log N) or localized O(1); eliminates redundant checks. | Configure `changeDetection: ChangeDetectionStrategy.OnPush` on ALL components. Enforce immutable state updates. |
| **Signal-driven Zoneless** | Fine-grained reactive nodes directly notify the scheduler | Bypasses `zone.js` completely; maximum performance. | Enable `provideExperimentalZonelessChangeDetection()` in `app.config.ts`. |

---

## Q19: ChangeDetectorRef Mechanics: markForCheck() vs detectChanges() vs detach() / reattach()
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Capgemini, Persistent, Nagarro, EPAM (Change detection mechanics deep dive).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`ChangeDetectorRef` controls the change detection engine at the component view level: **`markForCheck()`** does not run change detection immediately; instead, it walks up the component tree marking all ancestor components as dirty so they will be inspected during the *next scheduled change detection cycle*. **`detectChanges()`** executes change detection *immediately and synchronously* on the component and its children, regardless of whether dirty flags were set. **`detach()`** unlinks the component's change detector from the change detection tree entirely, which is used alongside `reattach()` to freeze high-frequency DOM repaints."
* **🧠 Intuitive Real-World Analogy:**  
  * **`markForCheck()` (Raising a Hand in a Classroom):** You raise your hand to ask a question. The teacher doesn't stop speaking mid-sentence; she will call on you when the next Q&A round starts.
  * **`detectChanges()` (Ringing the Fire Alarm Bell):** You press the alarm button, forcing the entire classroom to immediately halt what they are doing and inspect the room right now.
  * **`detach()` / `reattach()` (Taking a Laptop Offline):** You turn off Wi-Fi on your laptop while typing a fast document so incoming email notifications don't interrupt your typing, then reconnect Wi-Fi (`reattach`) when you are finished.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, ChangeDetectorRef, inject, OnInit } from '@angular/core';

@Component({ selector: 'app-cdr-demo', standalone: true, template: `...` })
export class CdrDemoComponent implements OnInit {
  private cdr = inject(ChangeDetectorRef);
  livePrice = 0;

  ngOnInit() {
    // 1. External non-Angular event / WebSocket callback:
    externalWebSocket.onmessage = (event) => {
      this.livePrice = event.data.price;
      // ✅ Tells Angular: Check this OnPush view in the next tick
      this.cdr.markForCheck();
    };
  }

  forceImmediateRender() {
    // ⚠️ Synchronous immediate check of this component + children
    this.cdr.detectChanges();
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why is calling `detectChanges()` inside `ngAfterViewInit` dangerous, and what error can it trigger if not careful?"  
  * *Senior Answer:* "Calling `detectChanges()` synchronously forces an out-of-band change detection cycle. If you mutate a bound property in `ngAfterViewInit` and call `this.cdr.detectChanges()`, you force a full child re-render immediately. While it can suppress `ExpressionChangedAfterItHasBeenCheckedError`, doing so repeatedly degrades rendering throughput and can mask underlying architectural flaws in data flow. Furthermore, if a child component in that subtree mutates parent state during that immediate check, it can cause cyclical rendering crashes."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Method | Execution Timing | Subtree Affected | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **`markForCheck()`** | Asynchronous (Next CD cycle) | Ancestors up to Root | Call when updating `OnPush` component state from external subscriptions or callbacks outside Angular. |
| **`detectChanges()`** | Synchronous (Immediate) | Current component & children | Use sparingly when an immediate DOM measurement or synchronous repaint is strictly required. |
| **`detach()`** | Immediate unlinking | Current component & children | Detach high-frequency updating widgets (e.g. 60 FPS live stock charts) from regular change detection passes. |
| **`reattach()`** | Re-links into CD tree | Current component & children | Re-link the detached component when the user switches tabs back or updates pause. |

---

## Q20: Modern Zoneless Angular: provideExperimentalZonelessChangeDetection() vs NgZone.runOutsideAngular()
* **Asked At:** Wells Fargo, Morgan Stanley, Walmart Global Tech, Swiggy, Persistent, EPAM (The premier Angular 18 architectural round).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "For years, Angular relied on `zone.js` to monkey-patch all browser asynchronous APIs (`setTimeout`, `Promise`, `addEventListener`, `fetch`) to trigger application-wide change detection ticks. This added 100 KB to bundles, complicated debugging with giant async stack traces, and caused performance issues on high-frequency events. In modern Angular 18, we can completely eliminate `zone.js` using `provideExperimentalZonelessChangeDetection()`. In Zoneless mode, change detection is driven cleanly by Signal notifications and microtask scheduling. In hybrid or Zone-based apps, we use `NgZone.runOutsideAngular()` to escape the change detection zone for 60 FPS animations, WebSockets, or canvas rendering."
* **🧠 Intuitive Real-World Analogy:**  
  * **`zone.js` (The Micro-Managing Boss):** A boss who stands over your shoulder all day. Every time you sip coffee, open a browser tab, or type a letter, the boss calls an all-hands department meeting asking *"Did anything change?"*
  * **Zoneless Signals (The Slack Notification System):** You work in peace. Whenever an actual update is ready, a targeted Slack ping notifies only the specific project team to refresh their view.
  * **`NgZone.runOutsideAngular()` (Entering a Soundproof Booth):** Stepping into a soundproof cabin so your rapid typing doesn't trigger the boss's microphone.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { ApplicationConfig, provideExperimentalZonelessChangeDetection } from '@angular/core';
import { Component, NgZone, ElementRef, inject, OnInit } from '@angular/core';

// 1. app.config.ts: Completely eliminates zone.js from polyfills!
export const appConfig: ApplicationConfig = {
  providers: [provideExperimentalZonelessChangeDetection()]
};

// 2. High-Frequency 60 FPS Escaping:
@Component({ selector: 'app-canvas', standalone: true, template: `<canvas #box></canvas>` })
export class CanvasComponent implements OnInit {
  private zone = inject(NgZone);
  private el = inject(ElementRef);

  ngOnInit() {
    // ✅ Escaping Zone prevents change detection on every mouse move!
    this.zone.runOutsideAngular(() => {
      this.el.nativeElement.addEventListener('mousemove', (e: MouseEvent) => {
        // High-frequency 60 FPS direct canvas drawing without triggering Angular CD
      });
    });
  }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "In a Zoneless Angular application, what happens if you mutate a standard non-signal class property (`this.name = 'Rahul'`) from a `setTimeout` without calling `markForCheck()`?"  
  * *Senior Answer:* "The UI template will **never update!** In a Zoneless application, there is no `zone.js` monkey-patching `setTimeout` to trigger change detection. Angular only knows to update the DOM when a reactive primitive (an Angular Signal) emits, an `AsyncPipe` receives a new value, or `ChangeDetectorRef.markForCheck()` is called manually. In Zoneless Angular, all state bound to templates must be encapsulated in **Angular Signals** (`name = signal('Rahul')`)."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Architecture / Scenario | What to Use | Pros & Cons | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **New Angular 18 Enterprise Projects** | `provideExperimentalZonelessChangeDetection()` | Removes 100 KB `zone.js`; instant startup; zero stack-trace pollution. | Add to `appConfig.providers`; remove `zone.js` from `angular.json` polyfills. |
| **High-Frequency Mouse / Scroll / Canvas events** | `NgZone.runOutsideAngular(() => ...)` | Runs callbacks without waking Angular change detection. | Bind event listener inside `runOutsideAngular`; re-enter zone via `run()` only if UI must update. |
| **WebSocket live financial price ticks (Zone-based)** | `NgZone.runOutsideAngular()` + Signals | Prevents 100 CD cycles per second across the whole DOM tree. | Buffer ticks outside Zone; update a `signal()` which schedules a single coalesced render tick. |
'''
