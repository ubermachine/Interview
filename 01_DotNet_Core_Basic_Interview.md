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
  "The .NET Garbage Collector is an automatic memory manager built on the Generational Hypothesis: most objects die young. The managed heap is split into three generational segments plus the LOH: **Gen 0** handles short-lived allocations like strings and DTOs; **Gen 1** acts as an ephemeral buffer; **Gen 2** holds long-lived objects like singletons and static caches; and the **Large Object Heap (LOH)** handles objects $\ge$ 85,000 bytes. The GC uses a Mark-Sweep-Compact algorithm, keeping Gen 0 collections lightning-fast while minimizing expensive Gen 2 Stop-the-World pauses."
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
  "The core difference is throughput versus UI responsiveness. **Workstation GC** is optimized for client apps—it runs on a single thread with a single managed heap to prevent UI freezing. **Server GC** is the default in ASP.NET Core for high-throughput APIs: it creates **one dedicated managed heap and one dedicated GC worker thread per logical CPU core**, collecting memory concurrently across all cores to maximize throughput under heavy load."
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
  "`Dispose()` provides **deterministic, immediate cleanup** of unmanaged resources like database connections, open files, and sockets, called directly via `using`. The **Finalizer (`~ClassName()`)** is an emergency fallback invoked by the GC finalizer thread only if a developer forgot to call `Dispose()`. In our classes, we always call `GC.SuppressFinalize(this)` inside `Dispose()` to remove the object from the finalization queue and avoid expensive promotions to Gen 1 and 2."
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
  "`async` and `await` do **NOT** spawn background threads for I/O operations. The Roslyn compiler rewrites your method into a state machine struct (`IAsyncStateMachine`). When execution hits `await`, the current thread is immediately returned to the ThreadPool to handle other HTTP requests. The OS kernel handles the network call using I/O Completion Ports (IOCP), and once data arrives, a ThreadPool worker thread picks up execution right where it left off."
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
  "`Task` is a Reference Type allocated on the Managed Heap on every method call. `ValueTask` is a Value Type struct stored on the execution stack. In high-frequency hot paths where an operation frequently completes synchronously—like a cache hit—`ValueTask` returns the result with **zero heap allocations**, saving massive GC Gen 0 pressure. If it must do real I/O, it wraps a normal `Task` as a fallback."
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
  "Calling `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()` on an asynchronous task is the **Sync-Over-Async anti-pattern**. It holds the current ThreadPool worker thread hostage while waiting for an asynchronous callback. Under high traffic, all ThreadPool threads become blocked simultaneously—causing **ThreadPool Starvation**, queuing incoming HTTP requests, and causing API latency to spike until the service crashes."
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
  "ASP.NET Core processes requests through a chained pipeline of Middleware components invoked sequentially via a `RequestDelegate` (`Func<HttpContext, Task>`). Each middleware can inspect or mutate the request on the way in, invoke `await next()` to pass control downstream, and then inspect or modify the response on its way back up the pipeline."
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
  "ASP.NET Core offers 3 lifetimes: **Transient** (new instance every time it is injected), **Scoped** (one instance shared across a single HTTP request), and **Singleton** (one single instance for the entire application life). A **Captive Dependency** occurs when a longer-lived service—like a Singleton—injects a shorter-lived service—like a Scoped `DbContext`—holding it captive in memory forever and causing concurrency crashes."
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
  "Creating `new HttpClient()` manually per request leaves underlying TCP sockets lingering in `TIME_WAIT` state, leading to **Socket Exhaustion**. Conversely, keeping a static singleton `HttpClient` caches DNS records forever, missing DNS and IP address changes. `IHttpClientFactory` solves both: it pools and rotates the underlying `HttpMessageHandler` sockets every two minutes while keeping `HttpClient` instances lightweight and short-lived."
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
  "SOLID represents five core architectural guardrails: **Single Responsibility** (a class should have only one reason to change, like separating order processing from PDF generation), **Open/Closed** (open for extension, closed for modification via strategy interfaces like `IPaymentGateway`), **Liskov Substitution** (subtypes must honor base contracts without throwing `NotImplementedException`), **Interface Segregation** (fine-grained role interfaces instead of fat monolithic ones), and **Dependency Inversion** (high-level services depend on abstractions, injected via ASP.NET Core DI)."
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
  "The real difference is where query filtering happens. `IQueryable` translates LINQ expression trees into native SQL executed directly on the database server. `IEnumerable` pulls all raw records across the network into application RAM and filters them in C#. Once data is loaded in memory, `ICollection` provides counts and mutations (`Add`/`Remove`), while `IList` provides direct index-based access (`list[0]`)."
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
  "`string` is an immutable reference type on the managed heap. Every concatenation (`+=`) allocates a brand-new string on the heap and discards the old one, causing severe GC Gen 0 pressure in loops. `StringBuilder` is mutable; it maintains an internal chunked character buffer that expands in place, eliminating temporary heap allocations during repetitive string building."
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
  "`ref` passes an argument by reference for read-write access and requires caller initialization; `out` passes by reference for write-only access and legally forces the callee to assign a value before exiting; `in` passes by reference read-only for zero-copy struct performance; and `params` bundles a variable number of comma-separated arguments into an array."
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
  "`throw;` re-throws the current exception while strictly preserving the entire original call stack trace and line numbers. `throw ex;` destroys the stack trace, resetting the origin to the current catch block and hiding where the bug actually happened in production. Wrapping with `throw new CustomException("...", ex);` maintains architectural layering while preserving the diagnostic root cause in `InnerException`."
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
  "The core difference comes down to **identity versus capability**. An **Interface** defines a capability ('what' a class can do) with multiple inheritance—ideal for dependency injection and mocking—but it **cannot hold instance fields or state**. An **Abstract Class** defines shared identity ('what' a class is) and can maintain internal state, fields, constructors, and access modifiers (`protected`), but C# restricts you to single class inheritance. Even with C# 8 default methods, interfaces still cannot hold instance state."
* **🎯 Formal Rubric Keywords:** **Capability vs Identity Hierarchy**, **Multiple Interface Implementation vs Single Class Inheritance**, **Lack of Instance State / Fields in Interfaces**, **Virtual Method Table (vtable)**, **Default Interface Methods (DIM)**.
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
  "**Boxing** is the implicit conversion of a Value Type from the stack into a Reference Type or Interface on the managed heap, wrapping it in a 16-byte object header. **Unboxing** is the explicit cast extracting the value back to the stack. Boxing causes severe performance degradation in hot paths because allocating temporary heap objects triggers continuous GC Gen 0 collections. We prevent it by using Generics (`List<T>`)."
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
  "**Overloading** is compile-time polymorphism where methods share the same name with different parameter signatures. **Overriding** is true runtime polymorphism where a subclass provides an alternate implementation of a `virtual` base method using `override` (resolved dynamically via vtable). **Method Shadowing (`new`)** hides the base method without polymorphism; if called via a base class reference, the base method runs."
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
  "`const` is a compile-time constant evaluated during compilation and hardcoded directly into the calling assembly's IL; changing it requires recompiling all consumer DLLs. `readonly` is an instance constant assigned at declaration or inside the constructor. `static readonly` is a runtime type-level constant initialized once per application lifecycle when the static constructor executes."
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
  "The real architectural line in the sand is **scope and awareness**. **Middleware** sits in the outer HTTP pipeline (`RequestDelegate`) and runs before routing; it handles raw `HttpContext` for every incoming request—like authentication, CORS, and logging—but has zero awareness of MVC controllers, actions, or model state. **Action Filters** execute deep inside the MVC pipeline after endpoint routing selects a matching action; they have direct access to `ActionArguments`, model validation state, and controller metadata. I reach for Middleware when I need global HTTP plumbing, and Action Filters when I need controller-specific business inspection or model auditing."
* **🎯 Formal Rubric Keywords:** **HTTP Pipeline (`RequestDelegate`) vs MVC Filter Pipeline**, **`HttpContext` Level vs Action Level**, **Endpoint Routing Pre/Post Boundary**, **`ActionArguments` & `ModelState` Access**.
* **🧠 Everyday Indian Analogy:**  
  * **Middleware:** Security guard at the tech park main entrance gate. He checks your entry badge; he doesn't know what department you belong to or what project file you're coding.  
  * **Action Filter:** The Project Lead sitting right at your desk. She inspects your exact sprint task report and validates your inputs before you start coding.
* **💻 Simple Code Example:**
```csharp
// 1. Middleware: Runs on raw HttpContext across the entire application
app.Use(async (context, next) =>
{
    Console.WriteLine($"Incoming Path: {context.Request.Path}");
    await next(); // Pass down the pipeline
});

// 2. Action Filter: Runs inside MVC with full access to ActionArguments & ModelState
public class ValidationFilter : IActionFilter
{
    public void OnActionExecuting(ActionExecutingContext ctx)
    {
        if (!ctx.ModelState.IsValid)
            ctx.Result = new BadRequestObjectResult(ctx.ModelState);
    }
    public void OnActionExecuted(ActionExecutedContext ctx) { }
}
```

---

## Q12: Writing Custom Middleware for Global Exception Handling (ProblemDetails RFC 7807)
* **⚡ Direct Screening Answer:**  
  "In a production API, you never let unhandled exceptions crash silently or leak raw database stack traces to the public. A **Global Exception Middleware** wraps the entire downstream pipeline in a centralized `try-catch`. When an unhandled domain error bubbles up, it intercepts the exception, logs it with a unique `context.TraceIdentifier` for telemetry, maps the exception type to the proper semantic status code—like 404 for `KeyNotFoundException` or 400 for `ValidationException`—and writes an RFC 7807 compliant `ProblemDetails` JSON response. That gives API consumers a standardized, machine-readable error payload without exposing sensitive internal CLR or SQL metadata."
* **🎯 Formal Rubric Keywords:** **Global Exception Handling Middleware**, **RFC 7807 `ProblemDetails` Standard**, **`TraceIdentifier` / Correlation ID**, **Information Disclosure Prevention (CWE-209)**, **`Response.HasStarted` Guard**.
* **🧠 Everyday Indian Analogy:**  
  * **Airport Lost & Found Desk:** Instead of a distressed passenger panicking on the airplane runway, they are directed to an official desk that issues a standardized incident claim receipt (`ProblemDetails`) stamped with a tracking reference number (`TraceIdentifier`).
* **💻 Simple Code Example:**
```csharp
public class ExceptionHandlingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<ExceptionHandlingMiddleware> _logger;

    public ExceptionHandlingMiddleware(RequestDelegate next, ILogger<ExceptionHandlingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try { await _next(context); }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Unhandled fault on {TraceId}", context.TraceIdentifier);
            if (context.Response.HasStarted) throw; // Cannot alter committed response stream!

            context.Response.ContentType = "application/problem+json";
            context.Response.StatusCode = ex switch
            {
                KeyNotFoundException => (int)HttpStatusCode.NotFound,
                ArgumentException => (int)HttpStatusCode.BadRequest,
                _ => (int)HttpStatusCode.InternalServerError
            };

            var problem = new ProblemDetails
            {
                Status = context.Response.StatusCode,
                Title = "An error occurred while processing your request.",
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
  "A JWT (RFC 7519) is a stateless, cryptographically signed token split into three dot-separated Base64Url segments: **Header, Payload, and Signature**. In ASP.NET Core, `AddAuthentication().AddJwtBearer()` validates the cryptographic signature with our secret key, checks issuer, audience, and expiry, and unpacks the claims into `HttpContext.User` as a `ClaimsPrincipal`. The senior catch I always mention: ASP.NET Core defaults to a 5-minute clock drift allowance, so you must explicitly set `ClockSkew = TimeSpan.Zero` in `TokenValidationParameters`—otherwise expired tokens remain valid for an extra 300 seconds."
* **🎯 Formal Rubric Keywords:** **RFC 7519 Specification**, **Header.Payload.Signature Anatomy**, **`SymmetricSecurityKey` / `AsymmetricSecurityKey`**, **`TokenValidationParameters`**, **`ClockSkew = TimeSpan.Zero`**, **Claims-Based Authorization (`ClaimsPrincipal`)**.
* **🧠 Everyday Indian Analogy:**  
  * **Airport Boarding Pass:** Lists your Name, Flight 6E-204, Seat 14A (Claims/Payload). It is stamped with the airline's official digital hologram barcode (Cryptographic Signature). Any passenger can read the text, but nobody can alter the seat number without invalidating the seal.
* **💻 Simple Code Example:**
```csharp
// Program.cs Configuration
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = "https://api.mycorp.com",
            ValidateAudience = true,
            ValidAudience = "https://api.mycorp.com",
            ValidateLifetime = true,
            ClockSkew = TimeSpan.Zero, // Senior guard: Eliminates 5-min grace drift!
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(builder.Configuration["Jwt:SigningKey"]!))
        };
    });

app.UseAuthentication();
app.UseAuthorization();
```

---

## Q14: CORS (Cross-Origin Resource Sharing) Configuration
* **⚡ Direct Screening Answer:**  
  "CORS is a **browser-enforced security boundary**, not a backend firewall. When a client-side frontend at `https://frontend.com` makes an AJAX or Fetch call to a backend at `https://api.com`, the browser issues a preflight `OPTIONS` request asking if the API allows that origin, HTTP method, and custom header. In ASP.NET Core, we register named policies via `AddCors()` and attach `app.UseCors()` in the pipeline. Two non-negotiable senior rules: first, `app.UseCors()` must be placed strictly between `app.UseRouting()` and `app.UseAuthentication()`. Second, the CORS spec strictly forbids combining `.AllowAnyOrigin()` with `.AllowCredentials()`—if you send cookies or tokens, you must specify exact origins."
* **🎯 Formal Rubric Keywords:** **Same-Origin Policy (SOP)**, **Preflight `OPTIONS` Handshake**, **`Access-Control-Allow-Origin`**, **Middleware Ordering (`UseRouting -> UseCors -> UseAuthentication`)**, **`AllowCredentials` Wildcard Prohibition**.
* **🧠 Everyday Indian Analogy:**  
  * **International Embassy Visa Check:** The web browser is the border officer. Before allowing your React app to visit a foreign server, it asks the server: 'Do you permit visitors from domain X with method PUT?'. If the server doesn't respond with an official visa stamp (`Access-Control-Allow-Origin`), the browser refuses to hand over the response.
* **💻 Simple Code Example:**
```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowClientApp", policy =>
    {
        policy.WithOrigins("https://portal.mycorp.com")
              .AllowAnyMethod()
              .AllowAnyHeader()
              .AllowCredentials(); // Safe: Explicit origin permits credentials!
    });
});

var app = builder.Build();

app.UseRouting();

// ⚠️ SENIOR ORDER: Must sit between UseRouting and UseAuthentication!
app.UseCors("AllowClientApp");

app.UseAuthentication();
app.UseAuthorization();
```

---

## Q15: Eager Loading (.Include) vs Lazy Loading vs Explicit Loading
* **⚡ Direct Screening Answer:**  
  "The fundamental divide comes down to **when SQL queries fire and how many round-trips hit your database engine**. **Eager Loading** queries parent and child tables upfront in a single round-trip using `.Include()` via a SQL `LEFT JOIN`. **Lazy Loading** defers fetching until navigation properties are accessed in memory, which inevitably causes the catastrophic **N+1 query storm** inside loops (1 query for parents, plus 1,000 separate queries for each child). **Explicit Loading** manually queries navigation properties on demand using `Entry(parent).Collection().Load()`. In high-throughput production APIs, I almost exclusively use Eager Loading combined with `.AsNoTracking()` or project directly into DTOs."
* **🎯 Formal Rubric Keywords:** **Eager Loading (`.Include()`, `.ThenInclude()`)**, **Lazy Loading (`virtual` Proxies / IL Weaving)**, **N+1 Query Explosion**, **Explicit Loading (`Entry().Load()`)**, **`.AsSplitQuery()` Cartographic Optimization**.
* **🧠 Everyday Indian Analogy:**  
  * **Eager Loading (Full South Indian Thali):** The waiter serves rice, sambar, rasam, and dessert all at once on a single brass plate (1 trip).  
  * **Lazy Loading (Forgetful Waiter):** The waiter brings rice. You ask for dal, he walks to the kitchen. You ask for curd, he walks to the kitchen again. 100 customers = 300 exhausting kitchen trips.  
  * **Explicit Loading (A La Carte Order):** You eat your main course first, and only call the waiter to bring dessert if you decide you have room for it.
* **💻 Simple Code Example:**
```csharp
// ❌ Lazy Loading N+1 Trap: 1 query for customers + 500 queries for orders in loop!
var customers = await _context.Customers.ToListAsync();
foreach (var c in customers) Console.WriteLine(c.Orders.Count); 

// ✅ Eager Loading: Exactly 1 optimized SQL query fetching everything needed!
var safeCustomers = await _context.Customers
    .Include(c => c.Orders)
    .AsNoTracking()
    .ToListAsync();

// ⚡ Explicit Loading: Manually load children on demand when a condition is met
if (customer.RequiresAudit)
{
    await _context.Entry(customer).Collection(c => c.Orders).LoadAsync();
}
```

---

## Q16: First vs FirstOrDefault vs Single vs SingleOrDefault vs Find
* **⚡ Direct Screening Answer:**  
  "The difference comes down to **intent, performance, and uniqueness verification**. `First()` returns the first matching record or throws an exception if empty; `FirstOrDefault()` returns null/default instead of throwing. `Single()` and `SingleOrDefault()` are uniqueness verifiers—they instruct EF Core to generate `SELECT TOP 2` under the hood and will throw an `InvalidOperationException` if more than one match exists. `Find()` is fundamentally different: it searches strictly by Primary Key and checks EF Core's local `DbContext` memory cache first. If the entity is already tracked in RAM, it returns it instantly with zero SQL round-trips."
* **🎯 Formal Rubric Keywords:** **`SELECT TOP(1)` vs `SELECT TOP(2)` Generation**, **Data Integrity & Uniqueness Enforcement**, **`InvalidOperationException` on Cardinality Violation**, **`DbSet.Find()` First-Level Cache Lookup**.
* **🧠 Everyday Indian Analogy:**  
  * **`First`:** Taking the first auto-rickshaw standing in line. If the stand is empty, you get furious (Exception).  
  * **`FirstOrDefault`:** Checking the auto stand. If empty, you walk away calmly (Null).  
  * **`SingleOrDefault`:** Looking up an Aadhaar Card number. If the system finds 2 people with the exact same Aadhaar, it triggers a fraud alert (Duplicate Exception).  
  * **`Find`:** Checking your own pocket first for your car keys before driving all the way home to search the drawer.
* **💻 Simple Code Example:**
```csharp
// 1. FirstOrDefault: Generates SELECT TOP(1) - Fast lookup, ignores duplicates
var user = await _context.Users.FirstOrDefaultAsync(u => u.Email == email);

// 2. SingleOrDefault: Generates SELECT TOP(2) - Throws if duplicate exists!
var uniqueUser = await _context.Users.SingleOrDefaultAsync(u => u.Email == email);

// 3. FindAsync: Checks DbContext local cache first; generates 0 SQL if already loaded!
var cachedUser = await _context.Users.FindAsync(userId);
```

---

## Q17: AsNoTracking() vs Tracked Queries
* **⚡ Direct Screening Answer:**  
  "By default, EF Core tracks every entity loaded into memory inside its `ChangeTracker`. It clones an in-memory snapshot of every single property so that when you call `SaveChangesAsync()`, it can run snapshot diffing to generate `UPDATE` statements. For read-only GET endpoints, that snapshot cloning is pure wasted CPU and memory overhead. Calling `.AsNoTracking()` tells EF Core to instantiate the C# objects and immediately detach them. In our production APIs, applying `.AsNoTracking()` to all GET queries cut heap memory allocations by 50% and yielded 30 to 40% faster query execution."
* **🎯 Formal Rubric Keywords:** **EF Core `ChangeTracker`**, **In-Memory Property Snapshot Cloning**, **Snapshot Diffing Algorithm**, **Read-Only Query Optimization**, **Allocation Reduction & GC Pressure Relief**.
* **🧠 Everyday Indian Analogy:**  
  * **Tracked Query (5-Star Hotel Check-In):** Your passport is photocopied, bags cataloged, credit card authorized, and front desk tracks your every movement until checkout.  
  * **`AsNoTracking` (Lobby Cafe Customer):** You step in, buy a cup of coffee, sit for 10 minutes, and leave. Zero registration forms, zero administrative baggage.
* **💻 Simple Code Example:**
```csharp
[HttpGet("catalog")]
public async Task<IActionResult> GetProductCatalog()
{
    // Production Senior Standard: Zero tracking snapshots in RAM!
    var products = await _context.Products
        .AsNoTracking()
        .Where(p => p.IsActive)
        .OrderBy(p => p.Name)
        .ToListAsync();

    return Ok(products);
}
```

---

## Q18: async and await Internals: Does it Create a New Thread?
* **⚡ Direct Screening Answer:**  
  "No, `async` and `await` do **NOT** spawn a new background thread for I/O operations. When you hit an `await` on an asynchronous I/O operation—like a database query or an HTTP call—the compiler-generated `IAsyncStateMachine` hooks up a continuation callback and **yields the current worker thread immediately back to the ThreadPool** so it can process other incoming requests. The actual waiting happens at the hardware and kernel level via I/O Completion Ports (IOCP). When the network packet or disk read finishes, an OS hardware interrupt signals the CLR, and any free ThreadPool worker resumes the method right where it paused. It is purely about thread utilization and server throughput, not thread creation."
* **🎯 Formal Rubric Keywords:** **Thread Yielding vs Thread Creation**, **`IAsyncStateMachine` Struct State Machine**, **I/O Completion Ports (IOCP)**, **Non-Blocking OS Interrupts**, **ThreadPool Scalability & Throughput**.
* **🧠 Everyday Indian Analogy:**  
  * **Bank Token System:** You walk up to the teller, submit your passbook for printing, receive token #45, and take a seat. The teller doesn't stand frozen staring at the printer; they immediately serve the next 15 customers in line. When your passbook is printed, any free teller announces token #45 and hands you your book.
* **💻 Simple Code Example:**
```csharp
// ThreadPool Worker Thread #5 enters here:
public async Task<string> FetchExternalOrderAsync(string orderId)
{
    // Thread #5 is RELEASED immediately back to ThreadPool to handle new incoming HTTP requests!
    // Zero CPU threads are blocked waiting on the wire!
    var json = await _httpClient.GetStringAsync($"https://orders.internal/api/{orderId}");

    // Network hardware alerts IOCP -> ThreadPool Worker Thread #12 (or any free thread) resumes:
    return json.Trim();
}
```

---

## Q19: lock vs SemaphoreSlim in Asynchronous Code
* **⚡ Direct Screening Answer:**  
  "The C# `lock` keyword compiles down to `Monitor.Enter` and `Monitor.Exit`, which strictly enforce **thread affinity**—the exact same OS thread that acquires the lock must be the one that releases it. But in async code, an execution can pause at an `await` on Thread A and resume on Thread B, causing `lock` to fail compile-time with error CS1996. To synchronize asynchronous workflows across thread transitions, we use **`SemaphoreSlim.WaitAsync()`**. It allows non-blocking asynchronous waiting without tying up an OS thread, and can be safely released from whichever thread resumes execution inside a `finally` block."
* **🎯 Formal Rubric Keywords:** **Thread Affinity of `lock` (`Monitor.Enter/Exit`)**, **Compiler Error CS1996**, **`SemaphoreSlim.WaitAsync()`**, **Non-Blocking Asynchronous Synchronization**, **`try-finally` Release Guarantee**.
* **🧠 Everyday Indian Analogy:**  
  * **`lock`:** A biometric fingerprint lock on a security door that requires the exact same guard to lock and unlock it. If the guard's shift ends mid-operation, nobody else can open the door.  
  * **`SemaphoreSlim`:** A physical brass key token hanging on the wall. Guard A takes the key to enter. When Guard B finishes the work, Guard B safely hangs the key back on the wall.
* **💻 Simple Code Example:**
```csharp
public class SafeAsyncCache
{
    // InitialCount: 1, MaxCount: 1 behaves as an async-safe mutex!
    private readonly SemaphoreSlim _semaphore = new SemaphoreSlim(1, 1);
    private readonly Dictionary<string, string> _cache = new();

    public async Task<string> GetOrAddAsync(string key, Func<Task<string>> valueFactory)
    {
        // ❌ lock(_lock) { await valueFactory(); } -> Compile Error CS1996!

        // ✅ Non-blocking async lock acquisition:
        await _semaphore.WaitAsync();
        try
        {
            if (_cache.TryGetValue(key, out var cached)) return cached;
            var fresh = await valueFactory();
            _cache[key] = fresh;
            return fresh;
        }
        finally
        {
            _semaphore.Release(); // Guarantee release even if valueFactory throws!
        }
    }
}
```

---

## Q20: Clustered vs Non-Clustered Index in SQL Server
* **⚡ Direct Screening Answer:**  
  "In SQL Server, a **Clustered Index *is* the table**—its leaf nodes are the physical data pages, meaning a table can have strictly **one** Clustered Index (created by default on the Primary Key). A **Non-Clustered Index is a separate B-Tree cheat sheet** whose leaf nodes store index keys and row pointers back to the clustered key (up to 999 per table). In production, whenever I see an expensive Key Lookup in the execution plan, I add the missing columns to the **`INCLUDE`** clause to create a Covering Index and satisfy the query entirely from leaf pages."
* **🎯 Formal Rubric Keywords:** **B-Tree Structure**, **Physical Storage Order**, **Leaf Nodes = Data Pages (Clustered)**, **Row Locator / Clustered Key Pointer (Non-Clustered)**, **Covering Index (`INCLUDE` clause)**, **Key Lookup / Bookmark Lookup**.
* **🧠 Everyday Indian Analogy:**  
  * Clustered Index = English Dictionary (the words are physically arranged alphabetically; the content *is* the index).  
  * Non-Clustered Index = Textbook Index at the back (lists keywords with page numbers pointing you back into chapters).
* **💻 Simple T-SQL Example:**
```sql
-- Clustered Index: Dictates physical storage order
CREATE TABLE Orders ( OrderId INT PRIMARY KEY, CustomerId INT, Status VARCHAR(20) );

-- Non-Clustered Covering Index: Eliminates Key Lookups!
CREATE NONCLUSTERED INDEX NIX_Orders_CustomerId_Status 
ON Orders(CustomerId, Status) 
INCLUDE (OrderId);
```

---

## Q21: Finding the 2nd Highest / Nth Highest Salary
* **⚡ Direct Screening Answer:**  
  "I always solve this using **`DENSE_RANK()` inside a Common Table Expression (CTE)**. Candidates often reach for `RANK()`, but if two employees tie for the #1 salary, `RANK()` assigns both Rank 1 and skips Rank 2, so querying for Rank 2 returns zero rows! `DENSE_RANK()` guarantees consecutive ranking without gaps. For pagination in SQL Server 2012+, we can also use `OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY`, but `DENSE_RANK()` remains the universal senior production standard."
* **🎯 Formal Rubric Keywords:** **Common Table Expression (CTE)**, **Ranking Window Function (`DENSE_RANK()`)**, **Ties Handling**, **`RANK()` (Skips) vs `DENSE_RANK()` (Consecutive)**, **`OFFSET ... FETCH` Alternative**.
* **🧠 Everyday Indian Analogy:**  
  * Olympic Medal Ties: Two athletes tie for Gold (Rank 1). `DENSE_RANK` awards Silver (Rank 2) to the next athlete. `RANK` skips Silver completely and gives them Bronze (Rank 3).
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
  "`DELETE` is a row-by-row DML command: it supports a `WHERE` clause, writes every deleted row into the transaction log (`LDF`), and fires `AFTER DELETE` triggers. `TRUNCATE` is a DDL command: it deallocates entire 8KB data page extents at once with minimal logging, resets the identity seed to 1, and runs in milliseconds, but is blocked if foreign keys reference the table. `DROP` destroys the entire table schema and data permanently. And contrary to the popular interview myth: **`TRUNCATE` CAN be rolled back** inside an active transaction."
* **🎯 Formal Rubric Keywords:** **DML vs DDL**, **Row-by-Row Logging vs Page Extent Deallocation**, **Identity Seed Reset**, **`AFTER DELETE` Trigger Execution**, **Rollback Capability in Both (`BEGIN TRAN; TRUNCATE; ROLLBACK;`)**.
* **🧠 Everyday Indian Analogy:**  
  * DELETE = Pencil eraser: Erases words line by line. Leaves eraser dust in the log.  
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
  "In production code reviews, I **always default to `UNION ALL`**. Both operators combine result sets from multiple queries, but `UNION` performs an expensive Distinct Sort operator in TempDB to eliminate duplicate rows, which wastes CPU and memory grants. `UNION ALL` simply concatenates both streams directly with zero sorting overhead. I only allow `UNION` if there is an explicit business requirement to deduplicate overlapping records."
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
  "A **Primary Key** defines the core identity of a table: it strictly rejects `NULL` values, defaults to creating a Clustered Index, and a table can have strictly **one** Primary Key. A **Unique Key** constraint enforces uniqueness on alternate business attributes (like Email or PAN Card): it defaults to a Non-Clustered Index, you can have multiple per table, and in SQL Server, it permits **strictly one NULL value**."
* **🎯 Formal Rubric Keywords:** **Entity Integrity Constraint**, **Nullability (PK Disallows NULLs, Unique allows 1 NULL in SQL Server)**, **Clustered Index vs Non-Clustered Index Default**, **Cardinality (1 PK vs Multiple Unique Constraints)**.
* **🧠 Everyday Indian Analogy:**  
  * Primary Key = Aadhaar Number: Mandatory for every citizen; strictly unique; cannot be null.  
  * Unique Key = Passport / PAN Number: Unique if present, but some citizens may not have one yet (allows NULL).
* **💻 Simple T-SQL Example:**
```sql
CREATE TABLE Users (
    UserId INT IDENTITY(1,1) PRIMARY KEY, -- Primary Key: No NULLs, Clustered Index
    Email VARCHAR(255) NOT NULL UNIQUE,   -- Unique Key 1: Unique, Non-Clustered
    PanCard VARCHAR(10) NULL UNIQUE       -- Unique Key 2: Unique, allows 1 NULL in SQL Server!
);
```

---

## Q25: Stored Procedure vs User-Defined Function (UDF)
* **⚡ Direct Screening Answer:**  
  "The architectural split is about **side-effects and query composability**. A **Stored Procedure** is procedural: it can execute DML (`INSERT/UPDATE`), manage transactions (`BEGIN TRAN`, `COMMIT`), and return multiple result sets, but cannot be embedded inside a `SELECT` statement. A **Function** must be deterministic and side-effect free: it cannot perform DML or manage transactions, but can be used directly inside `SELECT`, `WHERE`, and `JOIN` clauses. In production, I avoid Scalar UDFs due to row-by-row (RBAR) performance penalties and use **Inline Table-Valued Functions (iTVF)** instead."
* **🎯 Formal Rubric Keywords:** **Procedural vs Deterministic Expression**, **DML Operations Allowed in SPs / Disallowed in UDFs**, **Transaction Management (`BEGIN TRAN`)**, **Query Embeddability (`SELECT dbo.fn_Tax()`)**, **Execution Plan Caching**, **Scalar UDF RBAR Performance Trap vs Inline TVF**.
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
  "ACID guarantees database transaction reliability during financial operations: **Atomicity** means 'all or nothing'—if money is debited from Account A but crediting Account B fails, the debit rolls back completely. **Consistency** guarantees that account balances satisfy all constraints and invariants before and after the transaction. **Isolation** ensures that concurrent transactions or mobile app balance queries cannot view uncommitted, interim changes. **Durability** guarantees that once committed, data is flushed to the Write-Ahead Transaction Log (`LDF`) on disk, surviving power outages or server crashes."
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
