# 01. .NET Core & C# Web API: Basic Interview & Screening Guide (India Context)

> **Target Audience:** Screening rounds, technical phone screens, Technical Round 1 (0–6+ YOE), and rapid revision.  
> **Focus:** 100% focused on real-world Indian technical screening rounds (TCS, Infosys, Cognizant, Wipro, Accenture, Capgemini, HCL, LTIMindtree, Nagarro, EPAM, GCCs). Crisp direct answers, exact formal CS keywords that score marks on the interviewer's evaluation sheet, intuitive Indian everyday analogies, and simple 5–15 line copy-pasteable code snippets.

---

# TABLE OF CONTENTS

- [Part 1: Core .NET Runtime & Web Architecture Rapid Revision](#part-1-core-net-runtime--web-architecture-rapid-revision)
  - [1.1 How .NET Garbage Collection Works (Generations 0, 1, 2 & LOH)](#11-how-net-garbage-collection-works-generations-0-1-2--loh)
  - [1.2 Workstation GC vs Server GC](#12-workstation-gc-vs-server-gc)
  - [1.3 The Disposable Pattern & Finalizer (Dispose vs Finalize)](#13-the-disposable-pattern--finalizer-dispose-vs-finalize)
  - [1.4 Async/Await Under The Hood (State Machine & Non-Blocking I/O)](#14-asyncawait-under-the-hood-state-machine--non-blocking-io)
  - [1.5 Task vs ValueTask](#15-task-vs-valuetask)
  - [1.6 ThreadPool Starvation & Sync-Over-Async Trap](#16-threadpool-starvation--sync-over-async-trap)
  - [1.7 ASP.NET Core Request Pipeline & Middleware Execution](#17-aspnet-core-request-pipeline--middleware-execution)
  - [1.8 Dependency Injection Lifetimes & Captive Dependency](#18-dependency-injection-lifetimes--captive-dependency)
  - [1.9 IHttpClientFactory & Socket Exhaustion vs DNS Bug](#19-ihttpclientfactory--socket-exhaustion-vs-dns-bug)

- [Part 2: Top 26 Most-Asked Indian Screening & Technical Round 1 Hitlist](#part-2-top-26-most-asked-indian-screening--technical-round-1-hitlist)
  - [Q1: SOLID Principles with Real-Time Project Examples](#q1-solid-principles-with-real-time-project-examples)
  - [Q2: IEnumerable vs IQueryable vs IList vs ICollection](#q2-ienumerable-vs-iqueryable-vs-ilist-vs-icollection)
  - [Q3: String vs StringBuilder & String Immutability](#q3-string-vs-stringbuilder--string-immutability)
  - [Q4: ref vs out vs in vs params](#q4-ref-vs-out-vs-in-vs-params)
  - [Q5: throw vs throw ex vs throw new CustomException](#q5-throw-vs-throw-ex-vs-throw-new-customexception)
  - [Q6: Abstract Class vs Interface (with C# 8+ Default Methods)](#q6-abstract-class-vs-interface-with-c-8-default-methods)
  - [Q7: Boxing and Unboxing Mechanics & Performance](#q7-boxing-and-unboxing-mechanics--performance)
  - [Q8: Method Overloading vs Method Overriding vs Method Shadowing (new)](#q8-method-overloading-vs-method-overriding-vs-method-shadowing-new)
  - [Q9: const vs readonly vs static readonly](#q9-const-vs-readonly-vs-static-readonly)
  - [Q10: Dependency Injection Lifetimes (Transient, Scoped, Singleton) & Captive Dependency](#q10-dependency-injection-lifetimes-transient-scoped-singleton--captive-dependency)
  - [Q11: Middleware vs Action Filters in ASP.NET Core](#q11-middleware-vs-action-filters-in-aspnet-core)
  - [Q12: Writing Custom Middleware for Global Exception Handling (ProblemDetails RFC 7807)](#q12-writing-custom-middleware-for-global-exception-handling-problemdetails-rfc-7807)
  - [Q13: JWT Authentication & Authorization in Web API](#q13-jwt-authentication--authorization-in-web-api)
  - [Q14: CORS (Cross-Origin Resource Sharing) Configuration](#q14-cors-cross-origin-resource-sharing-configuration)
  - [Q15: Eager Loading (.Include) vs Lazy Loading vs Explicit Loading](#q15-eager-loading-include-vs-lazy-loading-vs-explicit-loading)
  - [Q16: First vs FirstOrDefault vs Single vs SingleOrDefault vs Find](#q16-first-vs-firstordefault-vs-single-vs-singleordefault-vs-find)
  - [Q17: AsNoTracking() vs Tracked Queries](#q17-asnotracking-vs-tracked-queries)
  - [Q18: async and await Internals: Does it Create a New Thread?](#q18-async-and-await-internals-does-it-create-a-new-thread)
  - [Q19: lock vs SemaphoreSlim in Asynchronous Code](#q19-lock-vs-semaphoreslim-in-asynchronous-code)
  - [Q20: Clustered vs Non-Clustered Index in SQL Server](#q20-clustered-vs-non-clustered-index-in-sql-server)
  - [Q21: Finding the 2nd Highest / Nth Highest Salary](#q21-finding-the-2nd-highest--nth-highest-salary)
  - [Q22: DELETE vs TRUNCATE vs DROP](#q22-delete-vs-truncate-vs-drop)
  - [Q23: UNION vs UNION ALL](#q23-union-vs-union-all)
  - [Q24: Primary Key vs Unique Key](#q24-primary-key-vs-unique-key)
  - [Q25: Stored Procedure vs User-Defined Function (UDF)](#q25-stored-procedure-vs-user-defined-function-udf)
  - [Q26: ACID Properties Explained with a Banking Scenario](#q26-acid-properties-explained-with-a-banking-scenario)

---

# Part 1: Core .NET Runtime & Web Architecture Rapid Revision

## 1.1 How .NET Garbage Collection Works (Generations 0, 1, 2 & LOH)
* **⚡ Direct Screening Answer:**  
  ".NET Garbage Collection is an automatic memory manager based on the Generational Hypothesis: newly allocated objects die quickly, while older objects survive longer. The managed heap is split into Generation 0 (short-lived ephemeral allocations), Generation 1 (buffer between short and long), Generation 2 (long-lived objects, singletons), and the Large Object Heap (LOH) for objects $\ge$ 85,000 bytes."
* **🎯 Formal Rubric Keywords:** **Generational Hypothesis**, **Mark-Sweep-Compact**, **Generation 0/1/2**, **Large Object Heap ($\ge 85,000$ bytes)**, **Stop-The-World (STW) Pause**, **Ephemeral Segment**.
* **🧠 Everyday Analogy:**  
  * **Gen 0:** Sticky notes on your desk during a phone call; thrown into the dustbin immediately.
  * **Gen 1:** Documents inside your desk drawer for the current week's sprint.
  * **Gen 2:** Permanent steel safe file archives; cleaning requires halting office operations.
  * **LOH:** Heavy industrial machines ($> 85$ kg); swept in place without moving to prevent back injuries (memory copying).
* **💻 Simple Code Example:**
```csharp
// Gen 0 Allocation: Short-lived string or DTO
for (int i = 0; i < 1000; i++)
{
    var dto = new OrderDto(i, "Pending"); // Allocated in Gen 0, collected rapidly
}

// LOH Allocation: Arrays >= 85,000 bytes go straight to Large Object Heap!
byte[] largeBuffer = new byte[90000]; // 90 KB -> Bypasses Gen 0/1/2, allocated directly in LOH!
```

---

## 1.2 Workstation GC vs Server GC
* **⚡ Direct Screening Answer:**  
  "Workstation GC is designed for client/desktop applications; it uses a single GC thread on a single heap to preserve UI responsiveness. Server GC is designed for high-throughput backend APIs; it creates **one dedicated managed heap and one dedicated GC thread per logical CPU core**, collecting heaps concurrently at full CPU utilization."
* **🎯 Formal Rubric Keywords:** **Workstation GC (Single-threaded UI responsiveness)**, **Server GC (Dedicated heap & thread per CPU core)**, **Concurrent Mark & Sweep**, **Throughput vs Latency Optimization**, **Background GC (`gcServer = true`)**.
* **🧠 Everyday Analogy:**  
  * **Workstation GC:** A single quiet railway ticket clerk handling passengers one by one calmly without making noise.
  * **Server GC:** A 16-counter mega reservation counter at New Delhi railway station with 16 clerks working at maximum speed simultaneously.
* **💻 Simple Configuration Example:**
```xml
<!-- In YourProject.csproj or runtimeconfig.json -->
<PropertyGroup>
  <!-- Server GC enabled by default in ASP.NET Core -->
  <ServerGarbageCollection>true</ServerGarbageCollection>
  <ConcurrentGarbageCollection>true</ConcurrentGarbageCollection>
</PropertyGroup>
```

---

## 1.3 The Disposable Pattern & Finalizer (Dispose vs Finalize)
* **⚡ Direct Screening Answer:**  
  "`Dispose()` provides **deterministic, immediate cleanup** of unmanaged resources (database connections, open file handles, sockets) called explicitly by developers via `using`. The **Finalizer (`~ClassName()`)** is a non-deterministic fallback invoked by the GC finalizer thread only if the developer forgot to call `Dispose()`. Calling `GC.SuppressFinalize(this)` inside `Dispose()` removes the object from the finalization queue."
* **🎯 Formal Rubric Keywords:** **Deterministic Cleanup vs Non-Deterministic Finalization**, **Unmanaged Resources (OS Handles, Native Memory)**, **`GC.SuppressFinalize(this)`**, **Finalizer Thread Queue**, **`try-finally` Expansion**.
* **🧠 Everyday Analogy:**  
  * **`Dispose()`:** You return your borrowed office laptop to IT on your last working day; cleared immediately.
  * **Finalizer:** You walk away with the laptop; 3 months later, an audit recovery team hunts down the laptop from your home.
* **💻 Simple Code Example:**
```csharp
public class FileManager : IDisposable
{
    private FileStream? _fileStream = new FileStream("data.bin", FileMode.Open);

    public void Dispose()
    {
        _fileStream?.Dispose();
        _fileStream = null;
        GC.SuppressFinalize(this); // Skips expensive Finalizer queue!
    }

    ~FileManager() // Emergency finalizer fallback
    {
        _fileStream?.Dispose();
    }
}
```

---

## 1.4 Async/Await Under The Hood (State Machine & Non-Blocking I/O)
* **⚡ Direct Screening Answer:**  
  "`async` and `await` do **NOT** spawn background threads for I/O operations. The Roslyn compiler rewrites your async method into an internal state machine struct (`IAsyncStateMachine`). When execution hits `await`, the current thread is immediately released back to the ThreadPool. The OS kernel monitors the network socket via I/O Completion Ports (IOCP), and upon packet receipt, a ThreadPool worker thread resumes execution."
* **🎯 Formal Rubric Keywords:** **`IAsyncStateMachine` Struct**, **ThreadPool Thread Yielding**, **I/O Completion Ports (IOCP)**, **Non-Blocking Execution**, **`SynchronizationContext` (None in ASP.NET Core)**.
* **🧠 Everyday Analogy:**  
  * **Dominos Token Buzzer:** You order pizza; cashier gives you an electronic buzzer and you sit down (thread released!). When pizza bakes, buzzer vibrates and any free employee hands you the box.
* **💻 Simple Code Example:**
```csharp
[HttpGet("data")]
public async Task<IActionResult> GetDataAsync()
{
    // Await releases Kestrel worker thread to serve other users! Zero threads blocked!
    string response = await _httpClient.GetStringAsync("https://api.external.com/rates");
    return Ok(response);
}
```

---

## 1.5 Task vs ValueTask
* **⚡ Direct Screening Answer:**  
  "`Task` is a Reference Type allocated on the Managed Heap on every method call. `ValueTask` is a Value Type struct stored on the execution stack. In high-frequency, hot-path methods where the result is often available synchronously (e.g. in-memory cache hits), `ValueTask` avoids heap allocation entirely, saving significant GC Gen 0 pressure."
* **🎯 Formal Rubric Keywords:** **Reference Type Heap Allocation vs Value Type Stack Allocation**, **Synchronous Completion Hot-Path**, **GC Gen 0 Pressure Reduction**, **Cannot Await Multiple Times (`ValueTask` restriction)**.
* **🧠 Everyday Analogy:**  
  * **Task:** Taking an official stamped paper invoice out of an office filing cabinet every time someone asks for the date.
  * **ValueTask:** Looking at your wristwatch; zero paper allocated.
* **💻 Simple Code Example:**
```csharp
// ValueTask avoids heap allocation if item is already in local memory!
public ValueTask<string> GetTokenAsync(string key)
{
    if (_cache.TryGetValue(key, out var cachedToken))
    {
        return new ValueTask<string>(cachedToken); // Synchronous: ZERO heap allocation!
    }

    return new ValueTask<string>(FetchFromNetworkAsync(key)); // Asynchronous fallback
}
```

---

## 1.6 ThreadPool Starvation & Sync-Over-Async Trap
* **⚡ Direct Screening Answer:**  
  "Calling `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()` on an asynchronous task is the **Sync-Over-Async anti-pattern**. It blocks the executing ThreadPool worker thread. Under flash traffic, all worker threads become blocked waiting for async completions, causing **ThreadPool Starvation**, queuing incoming HTTP requests, and driving API latency to complete timeout failure."
* **🎯 Formal Rubric Keywords:** **Sync-Over-Async Anti-Pattern**, **ThreadPool Starvation**, **`.Result` / `.Wait()` Blocking**, **Thread Pool Worker Queue Exhaustion**, **Async All The Way Down**.
* **🧠 Everyday Analogy:**  
  * Bank teller freezing at the cash counter for 15 minutes waiting for a delivery van, refusing to serve the 200 customers waiting in line.
* **💻 Simple Code Example:**
```csharp
// ❌ WRONG: Blocks thread, triggers starvation under load!
var data = _myService.FetchDataAsync().Result;

// ✅ CORRECT: Asynchronous all the way down
var data = await _myService.FetchDataAsync();
```

---

## 1.7 ASP.NET Core Request Pipeline & Middleware Execution
* **⚡ Direct Screening Answer:**  
  "ASP.NET Core processes HTTP requests using a chained pipeline of Middleware components invoked sequentially via a `RequestDelegate` (`Func<HttpContext, Task>`). Each middleware can inspect or mutate the request, invoke the `next()` middleware, and process the outgoing response on its way back up the pipeline."
* **🎯 Formal Rubric Keywords:** **`RequestDelegate`**, **Middleware Chaining**, **Bidirectional Pipeline Execution**, **Terminal Middleware (`app.Run`)**, **Branching Pipeline (`app.Map`)**.
* **🧠 Everyday Analogy:**  
  * An assembly conveyor belt: Raw product enters, Inspector 1 verifies badge (Auth), Inspector 2 checks package size (CORS), Inspector 3 packages goods (Routing/Endpoint), and on the way out, Inspector 1 stamps the final shipping label.
* **💻 Simple Code Example:**
```csharp
app.Use(async (context, next) =>
{
    // 1. Logic before next middleware
    Console.WriteLine($"Incoming: {context.Request.Path}");

    await next(); // 2. Call next middleware in chain

    // 3. Logic after downstream middleware finishes
    Console.WriteLine($"Outgoing: {context.Response.StatusCode}");
});
```

---

## 1.8 Dependency Injection Lifetimes & Captive Dependency
* **⚡ Direct Screening Answer:**  
  "ASP.NET Core has 3 lifetimes: **Transient** (new instance per injection), **Scoped** (single instance per HTTP request lifecycle), and **Singleton** (single instance for entire application lifetime). A **Captive Dependency** occurs when a longer-lived service (Singleton) injects a shorter-lived service (Scoped `DbContext`), trapping the scoped instance and causing concurrency crashes."
* **🎯 Formal Rubric Keywords:** **Inversion of Control (IoC)**, **Transient / Scoped / Singleton**, **`IServiceScope`**, **Captive Dependency Anti-Pattern**, **`IServiceScopeFactory` Resolution**.
* **🧠 Everyday Analogy:**  
  * Transient = Paper tea cup (fresh every time).  
  * Scoped = Lunch plate in cafeteria (yours for the 30-min lunch).  
  * Singleton = Office water cooler machine (1 for the entire building).
* **💻 Simple Code Example:**
```csharp
// Program.cs
builder.Services.AddTransient<IEmailService, EmailService>();
builder.Services.AddScoped<IOrderRepository, OrderRepository>(); // Scoped to HTTP Request
builder.Services.AddSingleton<ICacheManager, MemoryCacheManager>(); // App-wide single instance

// Resolving Scoped inside Singleton safely:
public class BackgroundWorker
{
    private readonly IServiceScopeFactory _scopeFactory;
    public BackgroundWorker(IServiceScopeFactory scopeFactory) => _scopeFactory = scopeFactory;

    public void DoWork()
    {
        using var scope = _scopeFactory.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
    }
}
```

---

## 1.9 IHttpClientFactory & Socket Exhaustion vs DNS Bug
* **⚡ Direct Screening Answer:**  
  "Creating `new HttpClient()` per request leaves sockets lingering in `TIME_WAIT` state, leading to **Socket Exhaustion**. Conversely, making `HttpClient` a static singleton caches DNS lookups indefinitely, missing IP address changes (**DNS Stale Cache Bug**). `IHttpClientFactory` solves both by pooling and rotating underlying `HttpMessageHandler` instances every 2 minutes while keeping `HttpClient` facades short-lived."
* **🎯 Formal Rubric Keywords:** **Socket Exhaustion (`TIME_WAIT` State)**, **DNS Stale Cache Bug**, **`HttpMessageHandler` Pooling (2-minute rotation)**, **Typed Clients (`AddHttpClient<T>`)**.
* **🧠 Everyday Analogy:**  
  * Hotel rental car fleet: You don't buy a new car for every trip (Socket Exhaustion) or keep a 1990 car forever (DNS bug); the hotel fleet manager pools, services, and rotates engines every 2 hours.
* **💻 Simple Code Example:**
```csharp
// Program.cs: Register Typed Client with pooled handler & DNS rotation!
builder.Services.AddHttpClient<PaymentClient>(client =>
{
    client.BaseAddress = new Uri("https://api.payments.com");
    client.Timeout = TimeSpan.FromSeconds(5);
});
```

---

# Part 2: Top 26 Most-Asked Indian Screening & Technical Round 1 Hitlist

## Q1: SOLID Principles with Real-Time Project Examples
* **⚡ Direct Screening Answer:**  
  "SOLID represents 5 core object-oriented principles: **Single Responsibility** (a class should have only one reason to change), **Open/Closed** (open for extension, closed for modification), **Liskov Substitution** (subtypes must be substitutable for base types without breaking contracts), **Interface Segregation** (fine-grained client-specific interfaces rather than fat general-purpose ones), and **Dependency Inversion** (high-level modules depend on abstractions, not concrete details)."
* **🎯 Formal Rubric Keywords:** **High Cohesion**, **Low Coupling**, **Strategy Pattern**, **Behavioral Subtyping**, **Role-Based Interfaces**, **Inversion of Control (IoC)**.
* **🧠 Everyday Indian Analogy:**  
  * **S:** Swiss Army Knife anti-pattern; give each tool one job.  
  * **O:** Smartphone OS: install apps from App Store without cracking open the motherboard.  
  * **L:** Electric auto-rickshaw vs Petrol auto-rickshaw: both follow driver steering and brake pedals identically.  
  * **I:** Vegetarian restaurant menu: don't force a vegetarian to review a seafood contract.  
  * **D:** Wall electrical power socket: your laptop charger plugs into the standard wall socket interface, not soldered into house wires.
* **💻 Simple Code Example:**
```csharp
// S & D: Service depends on interface abstraction; handles 1 responsibility
public interface IPaymentGateway { Task PayAsync(decimal amount); }

public class UpiPayment : IPaymentGateway
{
    public Task PayAsync(decimal amount) => Task.CompletedTask;
}

public class CheckoutService
{
    private readonly IPaymentGateway _gateway;
    public CheckoutService(IPaymentGateway gateway) => _gateway = gateway; // Dependency Inversion!

    public async Task Process(decimal amount) => await _gateway.PayAsync(amount);
}
```

---

## Q2: IEnumerable vs IQueryable vs IList vs ICollection
* **⚡ Direct Screening Answer:**  
  "`IEnumerable` is for in-memory collections and evaluates filtering on the client side (in C# RAM), whereas `IQueryable` represents an expression tree that translates LINQ queries to native SQL for execution directly on the database server. `ICollection` adds mutation methods (`Add`, `Remove`, `Count`), and `IList` adds index-based access (`list[0]`)."
* **🎯 Formal Rubric Keywords:** **Expression Tree (`System.Linq.Expressions`)**, **`IQueryProvider`**, **Client-Side vs Server-Side Evaluation**, **Deferred Execution**, **Forward-Only Cursor (`IEnumerator`)**.
* **🧠 Everyday Indian Analogy:**  
  * **`IEnumerable`:** Swiggy delivery person brings the entire restaurant kitchen, pots, and chef to your living room table so you can pick 1 biryani (massive network waste).  
  * **`IQueryable`:** You order 1 biryani from the waiter; the kitchen cooks it and delivers only 1 plate to your table.
* **💻 Simple Code Example:**
```csharp
// ❌ IEnumerable: Downloads all 500,000 orders into RAM, then filters!
IEnumerable<Order> orders = dbContext.Orders;
var active = orders.Where(o => o.Status == "Active").ToList();

// ✅ IQueryable: Generates SELECT * FROM Orders WHERE Status = 'Active'; on SQL Server!
IQueryable<Order> query = dbContext.Orders;
var activeFast = query.Where(o => o.Status == "Active").ToList();
```

---

## Q3: String vs StringBuilder & String Immutability
* **⚡ Direct Screening Answer:**  
  "`string` is immutable—once allocated on the managed heap, its contents cannot be modified. Every concatenation (`str += "text"`) allocates a brand-new string on the heap, creating high GC Gen 0 pressure. `StringBuilder` is mutable; it maintains an internal chunked character buffer that expands in place without allocating new heap objects on every append."
* **🎯 Formal Rubric Keywords:** **Immutability**, **Managed Heap Allocation**, **GC Gen 0 Allocation Pressure**, **Internal Buffer Geometric Growth**, **`string.Concat` Optimization**.
* **🧠 Everyday Indian Analogy:**  
  * **String:** Printed PVC Aadhaar Card (cannot scratch to edit; must print and pay for a new card).  
  * **StringBuilder:** Classroom whiteboard (write, erase, and append on the same board).
* **💻 Simple Code Example:**
```csharp
// ❌ Inefficient: Allocates 1,000 strings on heap!
string text = "";
for (int i = 0; i < 1000; i++) text += i;

// ✅ Senior: Single pre-allocated mutable buffer
var sb = new StringBuilder(5000);
for (int i = 0; i < 1000; i++) sb.Append(i);
string result = sb.ToString();
```

---

## Q4: ref vs out vs in vs params
* **⚡ Direct Screening Answer:**  
  "`ref` passes a parameter by reference and requires the caller to initialize it before passing; `out` passes by reference and requires the called method to assign a value before returning; `in` passes by reference read-only for zero-copy performance; and `params` allows passing a comma-separated variable number of arguments as an array."
* **🎯 Formal Rubric Keywords:** **Pass-by-Reference vs Pass-by-Value**, **Managed Pointer (`T&`)**, **Definite Assignment Rule**, **Zero-Copy Struct Optimization**, **Array Packing Overhead**.
* **🧠 Everyday Indian Analogy:**  
  * `ref`: Google Doc with edit access (both read and edit).  
  * `out`: Blank exam answer sheet (must write before leaving).  
  * `in`: Laminated office security ID (read fast, cannot tamper).  
  * `params`: Swiggy cart (bundle 1, 5, or 10 items freely into 1 delivery bag).
* **💻 Simple Code Example:**
```csharp
void Update(ref int val) => val += 10;
bool TryGet(out int result) { result = 42; return true; } // Mandatory assign!
decimal Tax(in decimal amount) => amount * 0.18m; // Readonly reference!
int Sum(params int[] nums) => nums.Sum(); // Variable arguments!
```

---

## Q5: throw vs throw ex vs throw new CustomException
* **⚡ Direct Screening Answer:**  
  "`throw;` re-throws the current exception while strictly preserving the entire original call stack trace and line numbers. `throw ex;` destroys the stack trace, resetting the origin to the current catch block and hiding where the bug actually happened in production. Wrapping with `throw new CustomException("...", ex);` retains business context while keeping the root cause in `InnerException`."
* **🎯 Formal Rubric Keywords:** **Stack Unwinding**, **Call Stack Trace Preservation**, **`throw;` vs `throw ex;`**, **InnerException Chaining**, **Loss of Root-Cause Line Number**.
* **🧠 Everyday Indian Analogy:**  
  * `throw;`: Honest courier: shows parcel was damaged at Chennai Depot Bay 4.  
  * `throw ex;`: Fraud courier: rips off the tracking label and claims it was damaged at Bangalore Hub today.
* **💻 Simple Code Example:**
```csharp
try
{
    _paymentClient.Process(); // Exception on line 52 inside PaymentClient
}
catch (SocketException ex)
{
    // ❌ FATAL BUG: Overwrites stack trace! Line 52 lost forever!
    // throw ex;

    // ✅ SENIOR PATTERN: Preserves original line 52
    throw; 
}
```

---

## Q6: Abstract Class vs Interface (with C# 8+ Default Methods)
* **⚡ Direct Screening Answer:**  
  "An **Interface** defines a contract ('what' an object can do) and supports multiple inheritance; since C# 8, interfaces can contain default implementations, but **cannot have instance fields or state**. An **Abstract Class** defines identity ('is-a' hierarchy) and can hold instance state, fields, constructors, and access modifiers (`protected`), but C# only permits single class inheritance."
* **🎯 Formal Rubric Keywords:** **Contract vs Identity Hierarchy**, **Multiple Interface Inheritance vs Single Class Inheritance**, **Lack of Instance State in Interfaces**, **Virtual Method Table (vtable)**, **Default Interface Methods (DIM)**.
* **🧠 Everyday Indian Analogy:**  
  * Interface = Driving License: You can hold 3 licenses (Car, Bike, Heavy Vehicle). Specifies what you can drive, holds no physical blood or bones.  
  * Abstract Class = Biological DNA (Mammal): You have lungs, blood, and heart (instance state). You can only have 1 biological parent species.
* **💻 Simple Code Example:**
```csharp
public interface INotification
{
    Task SendAsync(string msg);
    Task SendUrgentAsync(string msg) => SendAsync($"[URGENT]: {msg}"); // Default Method!
}

public abstract class BaseService
{
    protected readonly ILogger _logger; // Holds state & fields!
    protected BaseService(ILogger logger) => _logger = logger;
    public abstract Task ExecuteAsync();
}
```

---

## Q7: Boxing and Unboxing Mechanics & Performance
* **⚡ Direct Screening Answer:**  
  "**Boxing** is the implicit conversion of a Value Type (stored on the Stack, e.g. `int`, `struct`) into a Reference Type or Interface (allocated on the Managed Heap). **Unboxing** is the explicit conversion of that heap object back to a stack value. Boxing degrades performance because it allocates a 16-byte object header on the heap, triggering frequent GC Gen 0 collections."
* **🎯 Formal Rubric Keywords:** **Value Type vs Reference Type**, **Stack Allocation vs Managed Heap Allocation**, **16-byte Object Header (MethodTable + SyncBlockIndex)**, **GC Gen 0 Allocation Pressure**, **Generics Prevention**.
* **🧠 Everyday Indian Analogy:**  
  * Boxing = Packing a loose apple into a cardboard Amazon delivery box with shipping labels and barcode stickers, and storing it in a warehouse.  
  * Unboxing = Opening the box, checking the label, and taking the apple back onto your desk.
* **💻 Simple Code Example:**
```csharp
int x = 42;
object boxed = x;        // 📦 Boxing: Allocates 24 bytes on managed heap!
int unboxed = (int)boxed; // 📤 Unboxing: Explicit cast back to stack

// Generics eliminate boxing completely:
List<int> numbers = new(); // Zero boxing!
numbers.Add(42);
```

---

## Q8: Method Overloading vs Method Overriding vs Method Shadowing (new)
* **⚡ Direct Screening Answer:**  
  "**Overloading** is compile-time polymorphism where methods share the same name with different parameter signatures. **Overriding** is runtime polymorphism where a subclass provides an alternate implementation of a `virtual` base method using `override` (resolved dynamically via vtable). **Method Shadowing (`new`)** hides the base method without polymorphism; if called via a base class reference, the base method runs."
* **🎯 Formal Rubric Keywords:** **Compile-Time vs Runtime Polymorphism**, **Early Binding vs Late Binding**, **Virtual Method Table (vtable)**, **Method Hiding (`new` keyword)**, **Dynamic Dispatch**.
* **🧠 Everyday Indian Analogy:**  
  * Overloading = Multi-pin wall charger (different pins, same wall plug).  
  * Overriding = Upgraded smartphone OS ringtone (plays the new tune automatically).  
  * Shadowing = Disguise mask over face (if someone calls your official name on the ID card, the base person answers).
* **💻 Simple Code Example:**
```csharp
public class Base { public virtual void Run() => Console.WriteLine("Base"); }
public class Child : Base { public override void Run() => Console.WriteLine("Child"); }
public class Shadow : Base { public new void Run() => Console.WriteLine("Shadow"); }

Base b1 = new Child();
b1.Run(); // "Child" (Runtime vtable dispatch!)

Base b2 = new Shadow();
b2.Run(); // "Base" (Compile-time reference type wins! Shadow method hidden!)
```

---

## Q9: const vs readonly vs static readonly
* **⚡ Direct Screening Answer:**  
  "`const` is a compile-time constant evaluated during compilation and hardcoded directly into the calling assembly's IL; it cannot be modified once compiled. `readonly` is an instance constant assigned at declaration or inside the constructor. `static readonly` is initialized once per application lifecycle during static constructor execution."
* **🎯 Formal Rubric Keywords:** **Compile-Time vs Runtime Constant**, **IL Literal Inlining**, **Cross-Assembly Versioning Trap**, **Static Constructor Initializer (`.cctor`)**.
* **🧠 Everyday Indian Analogy:**  
  * `const`: Permanent birthmark (inked into your DNA).  
  * `readonly`: Passport number (assigned when you are born/registered).  
  * `static readonly`: Office Wi-Fi password (loaded dynamically on router startup; identical for all employees).
* **💻 Simple Code Example:**
```csharp
public class Config
{
    public const string Version = "1.0"; // Inlined in IL at compile time!
    public readonly DateTime CreatedAt;   // Set in constructor!
    public static readonly string DbConn; // Set once in static constructor!

    public Config() => CreatedAt = DateTime.UtcNow;
    static Config() => DbConn = Environment.GetEnvironmentVariable("CONN") ?? "";
}
```

---

## Q10: Dependency Injection Lifetimes (Transient, Scoped, Singleton) & Captive Dependency
* **⚡ Direct Screening Answer:**  
  "**Transient** creates a new instance every time it is injected. **Scoped** creates one instance per HTTP request and shares it across all components during that request. **Singleton** creates one instance for the entire application life. A **Captive Dependency** occurs when a Singleton injects a Scoped service (`DbContext`), trapping it in memory and causing thread-safety crashes."
* **🎯 Formal Rubric Keywords:** **Inversion of Control (IoC)**, **`AddTransient` / `AddScoped` / `AddSingleton`**, **Per-Request Scope (`IServiceScope`)**, **Captive Dependency Anti-Pattern**, **`IServiceScopeFactory`**.
* **🧠 Everyday Indian Analogy:**  
  * Transient = Paper tea cup (throw away after each sip).  
  * Scoped = Lunch thali plate (yours for the 30-min lunch).  
  * Singleton = Office water cooler machine (1 machine shared by everyone).
* **💻 Simple Code Example:**
```csharp
builder.Services.AddTransient<IValidator, OrderValidator>();
builder.Services.AddScoped<IOrderRepo, OrderRepo>();     // Scoped per HTTP request
builder.Services.AddSingleton<ICache, MemoryCache>();   // App-wide singleton

// Fixing Captive Dependency in a Singleton:
public class QueueWorker
{
    private readonly IServiceScopeFactory _factory;
    public QueueWorker(IServiceScopeFactory factory) => _factory = factory;

    public void Process()
    {
        using var scope = _factory.CreateScope();
        var repo = scope.ServiceProvider.GetRequiredService<IOrderRepo>();
    }
}
```

---

## Q11: Middleware vs Action Filters in ASP.NET Core
* **⚡ Direct Screening Answer:**  
  "**Middleware** sits in the outer HTTP pipeline (`RequestDelegate`) and runs before routing; it has no knowledge of MVC controllers, model state, or action arguments. **Action Filters** sit inside the MVC pipeline after endpoint routing has matched, providing access to `ActionArguments`, model validation state, and controller metadata."
* **🎯 Formal Rubric Keywords:** **HTTP Pipeline (`RequestDelegate`) vs MVC Filter Pipeline**, **`HttpContext` Level vs Action Level**, **Endpoint Routing Pre/Post Boundary**, **`ActionArguments` & `ModelState` Access**.
* **🧠 Everyday Indian Analogy:**  
  * Middleware = Security guard at company gate (checks ID badge; doesn't care what project you code).  
  * Action Filter = Project Manager at your desk (inspects your daily code task report).
* **💻 Simple Code Example:**
```csharp
// Middleware: Runs on raw HttpContext for all requests
app.Use(async (context, next) =>
{
    Console.WriteLine($"Path: {context.Request.Path}");
    await next();
});

// Action Filter: Runs inside MVC with access to ActionArguments
public class ValidationFilter : IActionFilter
{
    public void OnActionExecuting(ActionExecutingContext ctx)
    {
        if (!ctx.ModelState.IsValid) ctx.Result = new BadRequestObjectResult(ctx.ModelState);
    }
    public void OnActionExecuted(ActionExecutedContext ctx) { }
}
```

---

## Q12: Writing Custom Middleware for Global Exception Handling (ProblemDetails RFC 7807)
* **⚡ Direct Screening Answer:**  
  "A Global Exception Handling Middleware intercepts unhandled exceptions across the entire downstream pipeline, logs the error with a unique `TraceIdentifier`, and returns a standardized RFC 7807 `ProblemDetails` JSON response with appropriate HTTP status codes, preventing sensitive database or CLR stack traces from leaking to clients."
* **🎯 Formal Rubric Keywords:** **Global Exception Handling Middleware**, **RFC 7807 `ProblemDetails`**, **`TraceIdentifier` / Correlation ID**, **Security Sanitization (CWE-209)**, **`Response.HasStarted` Check**.
* **🧠 Everyday Indian Analogy:**  
  * Airport Lost & Found desk: Instead of passenger panicking on the runway, they receive an official incident tracking receipt with a reference ID.
* **💻 Simple Code Example:**
```csharp
public class ExceptionMiddleware
{
    private readonly RequestDelegate _next;
    public ExceptionMiddleware(RequestDelegate next) => _next = next;

    public async Task InvokeAsync(HttpContext context)
    {
        try { await _next(context); }
        catch (Exception ex)
        {
            context.Response.ContentType = "application/problem+json";
            context.Response.StatusCode = (int)HttpStatusCode.InternalServerError;
            var problem = new ProblemDetails
            {
                Status = 500,
                Title = "An error occurred.",
                Detail = ex.Message,
                Instance = context.Request.Path
            };
            await context.Response.WriteAsJsonAsync(problem);
        }
    }
}
```

---

## Q13: JWT Authentication & Authorization in Web API
* **⚡ Direct Screening Answer:**  
  "JWT (RFC 7519) is a stateless, cryptographically signed token containing Header, Payload (Claims), and Signature separated by dots. In ASP.NET Core, `AddAuthentication().AddJwtBearer()` validates the cryptographic signature, checks issuer, audience, and expiration, and hydrates `HttpContext.User` with a `ClaimsPrincipal` for role and policy authorization."
* **🎯 Formal Rubric Keywords:** **RFC 7519 Specification**, **Header.Payload.Signature**, **`SymmetricSecurityKey` / `AsymmetricSecurityKey`**, **`TokenValidationParameters`**, **`ClockSkew = TimeSpan.Zero`**, **Claims-Based Authorization**.
* **🧠 Everyday Indian Analogy:**  
  * Airport Boarding Pass: Contains passenger name, seat 12B, flight AI-202 (Claims). Signed with airport digital barcode seal. Anyone can read your name, but cannot tamper with seat 12B without invalidating the signature.
* **💻 Simple Code Example:**
```csharp
// Program.cs Configuration
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = "https://myapi.com",
            ValidateAudience = true,
            ValidAudience = "https://myapi.com",
            ValidateLifetime = true,
            ClockSkew = TimeSpan.Zero, // Eliminate 5-min grace drift!
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(builder.Configuration["JwtKey"]!))
        };
    });
```

---

## Q14: CORS (Cross-Origin Resource Sharing) Configuration
* **⚡ Direct Screening Answer:**  
  "CORS is a browser security mechanism that prevents frontend web apps on one origin (`https://client.com`) from making AJAX requests to a backend API on another origin (`https://api.com`). The browser sends a preflight `OPTIONS` request. In ASP.NET Core, we configure CORS via `AddCors()` and attach `app.UseCors()` strictly between `UseRouting()` and `UseAuthentication()`."
* **🎯 Formal Rubric Keywords:** **Same-Origin Policy (SOP)**, **Preflight `OPTIONS` Request**, **`Access-Control-Allow-Origin`**, **Middleware Placement Ordering**, **`AllowCredentials` Wildcard Security Prohibition**.
* **🧠 Everyday Indian Analogy:**  
  * International visa border check: The browser is the immigration officer asking the destination country: "Do you accept visitors from domain X with method POST?".
* **💻 Simple Code Example:**
```csharp
builder.Services.AddCors(opt =>
{
    opt.AddPolicy("AllowUI", p => p.WithOrigins("https://myangularapp.com")
                                   .AllowAnyMethod()
                                   .AllowAnyHeader()
                                   .AllowCredentials());
});

app.UseRouting();
app.UseCors("AllowUI"); // ⚠️ Order: Must be between UseRouting and UseAuthorization!
app.UseAuthentication();
app.UseAuthorization();
```

---

## Q15: Eager Loading (.Include) vs Lazy Loading vs Explicit Loading
* **⚡ Direct Screening Answer:**  
  "**Eager Loading** queries related data upfront using `.Include()` via a SQL `LEFT JOIN`. **Lazy Loading** defers child queries until navigation properties are accessed in C# code, triggering the disastrous **N+1 Query Problem** (1 query for parents + N queries for children). **Explicit Loading** manually queries related child data on demand using `Entry(parent).Collection().Load()`."
* **🎯 Formal Rubric Keywords:** **Eager Loading (`.Include()`, `.ThenInclude()`)**, **Lazy Loading (`virtual` proxies)**, **N+1 Query Problem**, **Explicit Loading (`Entry().Load()`)**, **`.AsSplitQuery()` Optimization**.
* **🧠 Everyday Indian Analogy:**  
  * Eager Loading = Full lunch thali: Waiter brings rice, roti, dal, and sweet in 1 single plate.  
  * Lazy Loading = Waiter brings rice, then walks back to kitchen for roti, then walks back for dal (100 trips for 100 items).  
  * Explicit Loading = Eating rice, and only asking for sweet if you are still hungry.
* **💻 Simple Code Example:**
```csharp
// ❌ Lazy Loading N+1: 1 query for customers + 1,000 queries for orders!
var customers = db.Customers.ToList();
foreach(var c in customers) Console.WriteLine(c.Orders.Count); // Hidden SQL queries!

// ✅ Eager Loading: Exactly 1 optimized SQL query!
var fastCustomers = await db.Customers
    .Include(c => c.Orders)
    .AsNoTracking()
    .ToListAsync();
```

---

## Q16: First vs FirstOrDefault vs Single vs SingleOrDefault vs Find
* **⚡ Direct Screening Answer:**  
  "`First()` returns the first matching element or throws if empty. `FirstOrDefault()` returns null/default instead of throwing. `Single()` and `SingleOrDefault()` verify uniqueness and throw if **more than 1** element matches (generates `SELECT TOP(2)`). `Find()` searches by primary key and checks the `DbContext` local memory cache first before querying SQL."
* **🎯 Formal Rubric Keywords:** **`SELECT TOP(1)` vs `SELECT TOP(2)`**, **Uniqueness Enforcement vs Performance**, **`InvalidOperationException` on Multiple Matches**, **`DbSet.Find()` First-Level Cache Lookup**.
* **🧠 Everyday Indian Analogy:**  
  * `First`: Grab the first taxi in line. If empty queue, get angry (Exception).  
  * `FirstOrDefault`: Grab first taxi in line. If empty, walk calmly (Null).  
  * `SingleOrDefault`: Checking for your passport. If you find 2 passports with your name, raise emergency alarm (Data corruption!).  
  * `Find`: Checking your pocket first for your house keys before checking the locker.
* **💻 Simple Code Example:**
```csharp
var u1 = await db.Users.FirstOrDefaultAsync(u => u.Email == email); // SELECT TOP(1)
var u2 = await db.Users.SingleOrDefaultAsync(u => u.Email == email); // SELECT TOP(2) - Throws if duplicate!
var u3 = await db.Users.FindAsync(userId); // Checks DbContext RAM first; 0 SQL if already tracked!
```

---

## Q17: AsNoTracking() vs Tracked Queries
* **⚡ Direct Screening Answer:**  
  "By default, EF Core tracks all entities in its internal `ChangeTracker`, creating an in-memory snapshot clone of every property to detect future updates during `SaveChanges()`. For read-only GET endpoints, calling `.AsNoTracking()` bypasses snapshot creation, reducing memory allocation by 50% and executing queries 30–40% faster."
* **🎯 Formal Rubric Keywords:** **EF Core `ChangeTracker`**, **In-Memory Property Snapshot Cloning**, **Read-Only Query Optimization**, **Identity Resolution**, **Memory Allocation Reduction**.
* **🧠 Everyday Indian Analogy:**  
  * Tracked Query = Full hotel check-in: passport scanned, luggage logged, room key issued, tracked in guest register.  
  * `AsNoTracking` = Visitor sitting in hotel lobby for 5 minutes having tea; zero registration paperwork.
* **💻 Simple Code Example:**
```csharp
[HttpGet("products")]
public async Task<IActionResult> GetProducts()
{
    // Senior Best Practice for all GET APIs: Zero snapshot memory overhead!
    var products = await _context.Products
        .AsNoTracking()
        .Where(p => p.IsActive)
        .ToListAsync();

    return Ok(products);
}
```

---

## Q18: async and await Internals: Does it Create a New Thread?
* **⚡ Direct Screening Answer:**  
  "No, `async` and `await` do **NOT** create a new thread for I/O operations. Instead, `await` yields the current worker thread back to the ThreadPool. The OS device driver handles the I/O asynchronously via hardware I/O Completion Ports (IOCP). When data arrives, the OS alerts the runtime, and any available ThreadPool worker thread resumes execution."
* **🎯 Formal Rubric Keywords:** **Thread Yielding vs Thread Creation**, **`IAsyncStateMachine`**, **I/O Completion Ports (IOCP)**, **Non-Blocking OS Interrupt**, **ThreadPool Scalability**.
* **🧠 Everyday Indian Analogy:**  
  * Bank customer service token system: You take a token and sit down. The counter serves the next 30 customers. When your token number is called, any available clerk assists you.
* **💻 Simple Code Example:**
```csharp
// Thread #4 enters
var data = await _httpClient.GetStringAsync("https://api.com"); 
// While waiting on network, Thread #4 is FREE to serve other incoming requests!
// Thread #7 (or any free thread) resumes here when network data returns!
```

---

## Q19: lock vs SemaphoreSlim in Asynchronous Code
* **⚡ Direct Screening Answer:**  
  "The C# `lock` keyword compiles to `Monitor.Enter/Exit`, which requires thread affinity (the exact same OS thread must acquire and release it). Because async methods can resume on a different ThreadPool worker thread after `await`, using `lock` inside async code is a **compile-time error (CS1996)**. To synchronize async code, we use **`SemaphoreSlim.WaitAsync()`**."
* **🎯 Formal Rubric Keywords:** **Thread Affinity of `lock` (`Monitor.Enter/Exit`)**, **Compiler Error CS1996**, **`SemaphoreSlim.WaitAsync()`**, **Non-Blocking Asynchronous Synchronization**, **`try-finally` Release Pattern**.
* **🧠 Everyday Indian Analogy:**  
  * `lock`: A door lock that requires the exact same person's thumbprint to lock and unlock. If another worker takes over the shift, the door jams forever.  
  * `SemaphoreSlim`: A single brass token key. Any authorized shift worker can hold the token, do work, and hand the token back.
* **💻 Simple Code Example:**
```csharp
private readonly SemaphoreSlim _semaphore = new SemaphoreSlim(1, 1);

public async Task<string> GetDataAsync()
{
    await _semaphore.WaitAsync(); // Non-blocking async lock!
    try
    {
        return await FetchDataInternalAsync();
    }
    finally
    {
        _semaphore.Release(); // Always release in finally!
    }
}
```

---

## Q20: Clustered vs Non-Clustered Index in SQL Server
* **⚡ Direct Screening Answer:**  
  "A **Clustered Index** defines the physical storage order of rows in a table; its leaf nodes *are* the actual data pages (strictly 1 Clustered Index per table, created by Primary Key). A **Non-Clustered Index** is a separate B-Tree structure whose leaf nodes contain key values and a row locator pointing back to the clustered key (up to 999 per table). We use `INCLUDE` to create Covering Indexes and eliminate Key Lookups."
* **🎯 Formal Rubric Keywords:** **B-Tree Structure**, **Physical Storage Order**, **Leaf Nodes = Data Pages (Clustered)**, **Row Locator / Clustered Key Pointer (Non-Clustered)**, **Covering Index (`INCLUDE` clause)**, **Key Lookup / Bookmark Lookup**.
* **🧠 Everyday Indian Analogy:**  
  * Clustered Index = English Dictionary (the words are physically arranged alphabetically; the content *is* the index).  
  * Non-Clustered Index = Textbook Index at the back (lists keywords with page numbers pointing you back into chapters).
* **💻 Simple T-SQL Example:**
```sql
-- Clustered Index: Physical order
CREATE TABLE Orders ( OrderId INT PRIMARY KEY, CustomerId INT, Status VARCHAR(20) );

-- Non-Clustered Covering Index: Eliminates Key Lookups!
CREATE NONCLUSTERED INDEX NIX_Orders_CustomerId_Status 
ON Orders(CustomerId, Status) 
INCLUDE (OrderId);
```

---

## Q21: Finding the 2nd Highest / Nth Highest Salary
* **⚡ Direct Screening Answer:**  
  "We use **`DENSE_RANK()`** inside a Common Table Expression (CTE) ordered by Salary descending. `DENSE_RANK()` is preferred over `RANK()` because `DENSE_RANK()` does not skip rank numbers when duplicate salaries exist (e.g. if two employees tie for 1st rank, `DENSE_RANK()` labels the next salary as 2, whereas `RANK()` skips to 3)."
* **🎯 Formal Rubric Keywords:** **Common Table Expression (CTE)**, **Ranking Window Function (`DENSE_RANK()`)**, **Ties Handling**, **`RANK()` (Skips) vs `DENSE_RANK()` (Consecutive)**, **`OFFSET ... FETCH` Alternative**.
* **🧠 Everyday Indian Analogy:**  
  * Olympic Medal Ties: Two athletes win Gold (Rank 1). `DENSE_RANK` awards Silver (Rank 2) to the next athlete. `RANK` skips Silver and gives them Bronze (Rank 3).
* **💻 Simple T-SQL Example:**
```sql
-- Gold Standard Solution (Works for any Nth Highest with ties):
WITH SalaryRankCTE AS
(
    SELECT EmployeeId, Name, Salary,
           DENSE_RANK() OVER (ORDER BY Salary DESC) AS RankNum
    FROM Employees
)
SELECT EmployeeId, Name, Salary
FROM SalaryRankCTE
WHERE RankNum = 2; -- Change to N for Nth highest!
```

---

## Q22: DELETE vs TRUNCATE vs DROP
* **⚡ Direct Screening Answer:**  
  "`DELETE` is a DML command that deletes rows one-by-one, allows a `WHERE` clause, logs every deleted row in the transaction log (`LDF`), and fires triggers. `TRUNCATE` is a DDL command that deallocates entire data pages at once; it is faster, uses minimal logging, cannot have a `WHERE` clause, resets identity seed to 1, and can be rolled back inside a transaction. `DROP` removes the entire table schema and data permanently."
* **🎯 Formal Rubric Keywords:** **DML vs DDL**, **Row-by-Row Logging vs Page Extent Deallocation**, **Identity Seed Reset**, **`AFTER DELETE` Trigger Execution**, **Rollback Capability in Both (`BEGIN TRAN; TRUNCATE; ROLLBACK;`)**.
* **🧠 Everyday Indian Analogy:**  
  * DELETE = Pencil eraser: Erases words line by line.  
  * TRUNCATE = Unclipping all written pages from a ring binder; the empty binder is clean and ready for page 1.  
  * DROP = Throwing the binder and desk out the window.
* **💻 Simple T-SQL Example:**
```sql
DELETE FROM Orders WHERE Status = 'Cancelled'; -- Row-by-row, triggers run
TRUNCATE TABLE StagingOrders;                  -- Fast page deallocation, resets identity

-- TRUNCATE CAN BE ROLLED BACK (Contrary to myth!):
BEGIN TRANSACTION;
TRUNCATE TABLE TempOrders;
ROLLBACK TRANSACTION; -- Data fully restored!
```

---

## Q23: UNION vs UNION ALL
* **⚡ Direct Screening Answer:**  
  "`UNION` combines result sets of two queries and **eliminates duplicate rows** by running an expensive Distinct Sort in TempDB. `UNION ALL` simply concatenates both result sets together without checking for duplicates. In production, senior developers always default to **`UNION ALL`** unless deduplication is explicitly required, because `UNION ALL` avoids high-CPU sorting overhead."
* **🎯 Formal Rubric Keywords:** **Set Operator**, **Duplicate Elimination Overhead**, **TempDB Distinct Sort Operator**, **Concatenation Throughput**, **Execution Plan Cost**.
* **🧠 Everyday Indian Analogy:**  
  * `UNION`: Reading two guest lists, comparing every single name, crossing off duplicates with a red pen, and writing a new sheet.  
  * `UNION ALL`: Stapling the two guest lists together with a paper clip in 1 second.
* **💻 Simple T-SQL Example:**
```sql
-- ❌ UNION: Expensive Distinct Sort in TempDB!
SELECT CustomerId, City FROM RetailCustomers
UNION
SELECT CustomerId, City FROM CorporateCustomers;

-- ✅ UNION ALL: Direct fast concatenation with zero sorting!
SELECT CustomerId, City FROM RetailCustomers
UNION ALL
SELECT CustomerId, City FROM CorporateCustomers;
```

---

## Q24: Primary Key vs Unique Key
* **⚡ Direct Screening Answer:**  
  "A **Primary Key** uniquely identifies each row in a table, does **not allow NULL** values, and creates a Clustered Index by default (strictly 1 Primary Key per table). A **Unique Key** constraint also enforces uniqueness, creates a Non-Clustered Index by default, and allows **exactly one NULL value** in SQL Server (you can have multiple Unique Keys per table)."
* **🎯 Formal Rubric Keywords:** **Entity Integrity Constraint**, **Nullability (PK Disallows NULLs, Unique allows 1 NULL in SQL Server)**, **Clustered Index vs Non-Clustered Index Default**, **Cardinality (1 PK vs Multiple Unique Constraints)**.
* **🧠 Everyday Indian Analogy:**  
  * Primary Key = Aadhaar Number: Mandatory for every citizen; strictly unique; cannot be null.  
  * Unique Key = Passport / PAN Number: Unique if present, but some citizens may not have one yet (allows NULL).
* **💻 Simple T-SQL Example:**
```sql
CREATE TABLE Users (
    UserId INT IDENTITY(1,1) PRIMARY KEY, -- Primary Key: No NULLs, Clustered Index
    Email VARCHAR(255) NOT NULL UNIQUE,   -- Unique Key 1: Unique, Non-Clustered
    PanCard VARCHAR(10) NULL UNIQUE       -- Unique Key 2: Unique, allows 1 NULL!
);
```

---

## Q25: Stored Procedure vs User-Defined Function (UDF)
* **⚡ Direct Screening Answer:**  
  "A **Stored Procedure** can execute DML operations (`INSERT`, `UPDATE`, `DELETE`), manage transactions (`BEGIN TRAN`, `COMMIT`), return multiple result sets, and use output parameters, but cannot be invoked directly inside a `SELECT` statement. A **Function (UDF)** cannot perform DML, cannot manage transactions, must return a value or table, and can be used directly inside `SELECT`, `WHERE`, and `JOIN` clauses."
* **🎯 Formal Rubric Keywords:** **Procedural vs Deterministic Expression**, **DML Operations Allowed in SPs / Disallowed in UDFs**, **Transaction Management (`BEGIN TRAN`)**, **Query Embeddability (`SELECT dbo.fn_Tax()`)**, **Execution Plan Caching**.
* **🧠 Everyday Indian Analogy:**  
  * Stored Procedure = Factory assembly robot: Takes raw materials, paints cars, updates inventory, and manages the line.  
  * Function = Pocket calculator: Computes $\sqrt{x}$ and gives you the answer; cannot paint cars or modify factory inventory.
* **💻 Simple T-SQL Example:**
```sql
-- Stored Procedure: Can perform DML and manage transactions
CREATE PROCEDURE sp_TransferFunds @From INT, @To INT, @Amt DECIMAL(18,2)
AS
BEGIN
    BEGIN TRANSACTION;
    UPDATE Accounts SET Balance = Balance - @Amt WHERE Id = @From;
    UPDATE Accounts SET Balance = Balance + @Amt WHERE Id = @To;
    COMMIT TRANSACTION;
END;

-- Function: Cannot perform DML, used directly inside SELECT
CREATE FUNCTION fn_AnnualTax (@Salary DECIMAL(18,2)) RETURNS DECIMAL(18,2)
AS BEGIN RETURN (@Salary * 12) * 0.15; END;

-- Usage in SELECT:
SELECT Name, Salary, dbo.fn_AnnualTax(Salary) AS Tax FROM Employees;
```

---

## Q26: ACID Properties Explained with a Banking Scenario
* **⚡ Direct Screening Answer:**  
  "ACID guarantees database transaction reliability: **Atomicity** ('All or Nothing'—if money is debited from Account A but crediting Account B fails, the debit rolls back), **Consistency** (data satisfies all schema rules, constraints, and balance invariants before and after), **Isolation** (concurrent transactions cannot view each other's uncommitted modifications), and **Durability** (once committed, changes survive server crashes or power failures via the Write-Ahead Transaction Log)."
* **🎯 Formal Rubric Keywords:** **ACID Guarantees**, **Atomicity (All-or-Nothing / Rollback)**, **Consistency (Constraints & Foreign Keys)**, **Isolation (Isolation Levels: Read Committed, Snapshot)**, **Durability (Write-Ahead Logging / WAL / `LDF`)**.
* **🧠 Everyday Indian Analogy:**  
  * **ATM Withdrawal Scenario (₹5,000):**  
    * **A:** Either ₹5,000 cash comes out and account is debited ₹5,000, OR cash jams and your account is refunded ₹5,000 immediately. Never half-done.  
    * **C:** Your balance cannot drop below zero if no overdraft facility exists.  
    * **I:** While the ATM is debiting your money, your mobile app checking balance at that exact millisecond does not see an uncommitted ghost balance.  
    * **D:** Once the cash and receipt are in your hands, a power cut at the bank does not erase the transaction.
* **💻 Simple T-SQL Example:**
```sql
BEGIN TRANSACTION;
BEGIN TRY
    -- 1. Debit Account A
    UPDATE Accounts SET Balance = Balance - 5000 WHERE AccountId = 101 AND Balance >= 5000;
    
    -- 2. Credit Account B
    UPDATE Accounts SET Balance = Balance + 5000 WHERE AccountId = 202;

    COMMIT TRANSACTION; -- Atomicity & Durability guaranteed!
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION; -- Undoes all changes on failure!
    THROW;
END CATCH;
```

---
