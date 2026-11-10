MODULE_12 = '''---

# MODULE 12: HTTP CLIENT & FUNCTIONAL INTERCEPTORS

## Q32: Functional HTTP Interceptors (HttpInterceptorFn): JWT Bearer Token Injection & Request Cloning
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 100% of Angular enterprise rounds).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "Angular 15+ introduced functional interceptors (**`HttpInterceptorFn`**), configured via `provideHttpClient(withInterceptors([authInterceptor]))`, replacing verbose class-based interceptors and the `HTTP_INTERCEPTORS` multi-provider token. Because `HttpRequest` objects are strictly **immutable** to guarantee safe concurrent pipeline transformations, an interceptor cannot modify headers directly. Instead, you must use **`req.clone({ setHeaders: { ... } })`** to generate a new cloned request before forwarding it to `next(clonedReq)`."
* **🧠 Intuitive Real-World Analogy:**  
  * **Immutable Request Cloning (The Notarized Government Document):** When you submit your degree certificate to a visa consulate, the officer doesn't write on your original certificate with a permanent marker. They make a Xerox photocopy (`req.clone()`), stamp the official visa approval seal on the copy (`setHeaders`), and place the stamped copy in the dispatch tray (`next()`).
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthService } from './auth.service';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(AuthService);
  const token = authService.getToken();

  // ⚠️ HttpRequest is immutable: Must produce a clone!
  if (token && !req.url.includes('/api/auth/login')) {
    const clonedReq = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` }
    });
    return next(clonedReq);
  }
  return next(req);
};
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What is the difference between `setHeaders` and `headers: req.headers.set()` inside `req.clone()`?"  
  * *Senior Answer:* "`setHeaders` is a clean, declarative configuration object that merges new headers with existing ones, overwriting matching keys while preserving all other existing headers. Conversely, manually passing `headers: req.headers.set('Authorization', '...')` requires mutating the `HttpHeaders` instance first, which is verbose and prone to accidentally clobbering other custom headers if someone passes an unmerged new `HttpHeaders` map. `setHeaders` is the standardized, production-safe approach."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Interceptor Task | Modern Approach | Configuration Location | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **JWT Bearer Token Injection** | `HttpInterceptorFn` | `provideHttpClient(withInterceptors([authInterceptor]))` | Check token existence; clone with `setHeaders: { Authorization }`. |
| **Correlation ID / Tracing** | `req.clone({ setHeaders: { 'X-Correlation-ID': uuid() } })` | Global interceptor | Attach unique UUID to every outgoing request for distributed telemetry. |
| **Legacy Class Interceptor Migration** | Replace `HTTP_INTERCEPTORS` token with functional | In `app.config.ts` | Convert `intercept(req, next)` into pure `(req, next) => ...`. |
| **Conditional Bypass** | Inspect `req.url` or `HttpContextToken` | Per-request metadata | Check `if (req.context.get(BYPASS_AUTH)) return next(req);`. |

---

## Q33: Silent JWT Token Refresh & 401 Unauthorized Retry Queueing
* **Asked At:** Wells Fargo, Morgan Stanley, JPMorgan Chase, Walmart Global Tech, Barclays, Swiggy (Mandatory senior banking security question).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "When an access token expires in an enterprise application, backend APIs return `401 Unauthorized`. A production-grade HTTP interceptor must silently catch the 401, pause outgoing concurrent requests, trigger a single refresh token HTTP call, update the JWT credentials, and **retry all queued failed requests with the new token** without logging out the user. If multiple parallel API calls fail with 401 simultaneously, we use a **mutex lock (`isRefreshing` flag) and a `BehaviorSubject`** or RxJS stream to queue pending requests so only one refresh API call is dispatched."
* **🧠 Intuitive Real-World Analogy:**  
  * **The Highway FastTag Recharging Gate:** Five cars arrive at the toll barrier at the exact same second, but the FastTag RFID tag is low on balance (401 Unauthorized). The toll operator raises the barrier stop-arm (mutex lock). Car 1's driver completes a fast UPI recharge (refresh token). Once recharged, the operator lifts the gate and allows all 5 cars to pass smoothly through the gate without anyone having to turn their car around and drive back home!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { HttpInterceptorFn, HttpErrorResponse } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthService } from './auth.service';
import { catchError, switchMap, filter, take, throwError, BehaviorSubject } from 'rxjs';

let isRefreshing = false;
const refreshTokenSubject = new BehaviorSubject<string | null>(null);

export const jwtRefreshInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401 && !req.url.includes('/auth/refresh')) {
        if (!isRefreshing) {
          isRefreshing = true;
          refreshTokenSubject.next(null);
          return auth.refreshToken().pipe(
            switchMap(res => {
              isRefreshing = false;
              refreshTokenSubject.next(res.accessToken);
              return next(req.clone({ setHeaders: { Authorization: `Bearer ${res.accessToken}` } }));
            }),
            catchError(err => { isRefreshing = false; auth.logout(); return throwError(() => err); })
          );
        } else {
          // Queue parallel requests until refresh completes!
          return refreshTokenSubject.pipe(
            filter(token => token !== null),
            take(1),
            switchMap(token => next(req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })))
          );
        }
      }
      return throwError(() => error);
    })
  );
};
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What happens if the Refresh Token itself has expired or is revoked by the server?"  
  * *Senior Answer:* "If the refresh token itself is expired or invalidated (which also returns 401 or 403 on the `/auth/refresh` endpoint), the retry loop must immediately break! Notice the check `!req.url.includes('/auth/refresh')`. If the refresh endpoint fails, the interceptor catches it in the inner `catchError`, resets `isRefreshing = false`, forcefully purges all stored credentials, triggers `auth.logout()`, and redirects the user to the login screen with a session-expired toast alert to prevent an infinite recursive refresh loop."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Error Scenario | Strategy | Handling Mechanics | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **First 401 Access Token Expired** | Initiate silent refresh | Set `isRefreshing = true`; call `/auth/refresh` | Clone failed request with new token and retry. |
| **Concurrent 401s during refresh** | Queue via `BehaviorSubject` | Filter non-null tokens; take(1) | `refreshTokenSubject.pipe(filter(t => !!t), take(1), switchMap(...))`. |
| **Refresh Token also Expired (401/403)** | Force logout & redirect | Reset mutex lock; clear storage | Call `auth.logout()`; navigate to `/login?reason=session_expired`. |
| **Non-401 Errors (400, 404, 500)** | Pass-through to application | Do not trigger auth logic | Propagate directly via `throwError(() => error)`. |
'''
