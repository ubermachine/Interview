MODULE_10 = '''---

# MODULE 10: REACTIVE FORMS VS TEMPLATE-DRIVEN FORMS

## Q27: Reactive Forms vs Template-Driven Forms: Architecture, Scalability & Dynamic Validation
* **Asked At:** TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, Deloitte, EY, Persistent, Nagarro, EPAM (Asked in 99% of enterprise Angular interviews).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "The choice between Reactive Forms and Template-Driven Forms is an architectural decision regarding where form logic and state live: **Reactive Forms** build an explicit, programmatic, synchronous model tree (`FormGroup`, `FormControl`) in TypeScript, providing direct immutability, full unit testability without DOM rendering, and immediate synchronous validation. **Template-Driven Forms** (`[(ngModel)]`) delegate form state and validation implicitly to directives in the HTML template, making state asynchronous, difficult to unit test, and poorly suited for dynamic runtime fields. For enterprise applications (banking, insurance, e-commerce), Reactive Forms are the non-negotiable standard."
* **🧠 Intuitive Real-World Analogy:**  
  * **Reactive Forms (The Legal Court Document):** Written and signed in the lawyer's office (TypeScript class) with strict clauses and notary stamps. You can inspect, audit, and validate every clause without stepping outside into the street (DOM).
  * **Template-Driven Forms (The Sticky Notes on the Refrigerator Door):** You scribble notes on sticky pads stuck to the fridge door (HTML template). If the fridge is removed (DOM unmounted), your entire data model vanishes!
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, inject } from '@angular/core';
import { FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-kyc-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="kycForm" (ngSubmit)="submit()">
      <input formControlName="panNumber" placeholder="ABCDE1234F" />
      @if (kycForm.controls.panNumber.invalid && kycForm.controls.panNumber.touched) {
        <span>Invalid PAN Format</span>
      }
    </form>
  `
})
export class KycFormComponent {
  private fb = inject(FormBuilder);
  kycForm = this.fb.group({
    panNumber: ['', [Validators.required, Validators.pattern(/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/)]]
  });
  submit() { if (this.kycForm.valid) console.log(this.kycForm.getRawValue()); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "What is the difference between `form.value` and `form.getRawValue()` in Reactive Forms?"  
  * *Senior Answer:* "`form.value` only returns values for controls that are **enabled**; it completely omits any controls that have been disabled via `control.disable()`. If you send `this.form.value` in a POST payload to a backend API, disabled fields (like a disabled `userId`, `accountNumber`, or read-only `taxRate`) will be completely missing from the JSON payload. `form.getRawValue()` extracts values from **all controls regardless of disabled status**, guaranteeing complete payload serialization."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Form Architecture | State Location | Scalability & Testing | Best Enterprise Scenario |
| :--- | :--- | :--- | :--- |
| **Reactive Forms** (`ReactiveFormsModule`) | TypeScript Class (Synchronous tree) | ⚡ **Highly Scalable & Unit-Testable** without DOM. | Complex enterprise forms, multi-step banking KYC, dynamic arrays. |
| **Template-Driven Forms** (`FormsModule`) | HTML Template (Asynchronous `ngModel`) | ⚠️ **Limited Scalability**; testing requires DOM fixtures. | Simple static forms (single newsletter signup, simple search box). |
| **Serialization Safety** | `form.getRawValue()` | Captures disabled field values | Always use `this.form.getRawValue()` when submitting to backend APIs. |

---

## Q28: FormGroup, FormControl, and FormArray: Dynamic Fields & Custom Async Validators
* **Asked At:** Wells Fargo, Morgan Stanley, Walmart Global Tech, Cognizant, Infosys, Capgemini, EPAM (Complex dynamic forms round).
* **⚡ 30-Second Senior Opening Pitch:**  
  > "`FormArray` manages an ordered, dynamically resizable collection of `FormControl`, `FormGroup`, or nested `FormArray` instances, ideal for dynamic line items such as multi-nominee insurance forms or invoice line items. Custom synchronous validators implement the `ValidatorFn` signature (`(control) => ValidationErrors | null`). Custom **asynchronous validators** implement `AsyncValidatorFn`, returning an `Observable<ValidationErrors | null>`. In enterprise applications, asynchronous validators (like checking Aadhaar or email uniqueness against an API) must be debounced and piped with `distinctUntilChanged` and `switchMap` to avoid hammering backend databases."
* **🧠 Intuitive Real-World Analogy:**  
  * **`FormControl`:** A single blank field on a passport form: "First Name".
  * **`FormGroup`:** A designated section: "Permanent Address" containing Street, City, and PIN Code.
  * **`FormArray` (The 'Add Another Family Member' Button):** A button that dynamically staples another blank family member registration card onto your application packet. You can add 10 members or delete 3 dynamically.
* **💻 Simple, Clean, Runnable Code Snippet (5–15 lines):**
```typescript
import { Component, inject } from '@angular/core';
import { FormBuilder, FormArray, Validators, ReactiveFormsModule, AbstractControl, AsyncValidatorFn } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { timer, of } from 'rxjs';
import { switchMap, map, catchError } from 'rxjs/operators';

// Custom Async Validator: Checks username availability with debounce
export function uniqueUsernameValidator(http: HttpClient): AsyncValidatorFn {
  return (control: AbstractControl) => {
    if (!control.value) return of(null);
    return timer(400).pipe( // 400ms debounce
      switchMap(() => http.get<{ exists: boolean }>(`/api/users/check?u=${control.value}`)),
      map(res => res.exists ? { usernameTaken: true } : null),
      catchError(() => of(null))
    );
  };
}

@Component({
  selector: 'app-dynamic-nominees',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <button (click)="addNominee()">+ Add Nominee</button>
    @for (ctrl of nominees.controls; track $index) {
      <div [formGroup]="$any(ctrl)"><input formControlName="name" /></div>
    }
  `
})
export class DynamicNomineesComponent {
  private fb = inject(FormBuilder);
  form = this.fb.group({ nominees: this.fb.array([]) });
  get nominees() { return this.form.get('nominees') as FormArray; }
  addNominee() { this.nominees.push(this.fb.group({ name: ['', Validators.required] })); }
}
```
* **⚠️ Senior Trap & Cross-Question:**  
  * *Trap Question:* "Why do asynchronous validators fire on every keystroke by default, and how does this affect form status?"  
  * *Senior Answer:* "By default, form validation triggers on `change` (every keystroke). Asynchronous validators set the control status to `PENDING` while the network promise/observable is in-flight, which disables submission buttons and causes UI flickering. Furthermore, without a timer/debounce, 10 keystrokes send 10 parallel HTTP requests. The senior fix is twofold: 1) add a `timer(300)` debounce inside the async validator pipeline, and 2) configure `{ updateOn: 'blur' }` on the `FormControl` options so validation only executes when the user unfocuses the input."
* **📊 "When to Use What & What Must Be Done" Quick Decision Guide:**
| Dynamic Form Task | What to Use | Best Practice | What Must Be Done |
| :--- | :--- | :--- | :--- |
| **Variable line items (Invoices, Nominees)** | `FormArray` | Push/remove `FormGroup` items dynamically | `this.nominees.push(this.fb.group({...}))` and `this.nominees.removeAt(index)`. |
| **Custom Synchronous Validation** | `ValidatorFn` | Return `{ errorKey: true }` or `null` | Example: `(ctrl) => ctrl.value > 100 ? null : { minAge: true }`. |
| **Server-side validation (Email uniqueness)** | `AsyncValidatorFn` | Return `Observable<ValidationErrors \| null>` | Always debounce with `timer(300)` and swallow network errors with `catchError(() => of(null))`. |
| **Preventing keystroke validation spam** | `updateOn: 'blur'` | Delays validation until input loses focus | `new FormControl('', { validators: [...], updateOn: 'blur' })`. |
'''
