# 01. .NET Core & C# Web API: Basic Interview & Screening Guide (India Context)

> **Target Audience:** Screening rounds, technical phone screens, Technical Round 1 (0–6+ YOE), and rapid revision.  
> **Standard:** Speakable Senior English v1 (SSE-1) — concise, spoken-first, rubric-aligned interview answers.

---

# TABLE OF CONTENTS

- [Part 1: Core .NET Runtime & Web Architecture Rapid Revision](#part-1-core-net-runtime-web-architecture-rapid-revision)
  - [1.1: How does .NET Garbage Collection manage memory across generations?](#11-how-does-net-garbage-collection-manage-memory-across-generations)
  - [1.2: What is the difference between Workstation GC and Server GC?](#12-what-is-the-difference-between-workstation-gc-and-server-gc)
  - [1.3: How does the IDisposable pattern differ from Finalize?](#13-how-does-the-idisposable-pattern-differ-from-finalize)
  - [1.4: How do async and await work under the hood without blocking threads?](#14-how-do-async-and-await-work-under-the-hood-without-blocking-threads)
  - [1.5: When should you use ValueTask instead of Task?](#15-when-should-you-use-valuetask-instead-of-task)
  - [1.6: What causes ThreadPool starvation and how does sync-over-async trigger it?](#16-what-causes-threadpool-starvation-and-how-does-sync-over-async-trigger-it)
  - [1.7: How does the ASP.NET Core middleware request pipeline execute?](#17-how-does-the-aspnet-core-middleware-request-pipeline-execute)
  - [1.8: What are Dependency Injection lifetimes and how do you avoid captive dependencies?](#18-what-are-dependency-injection-lifetimes-and-how-do-you-avoid-captive-dependencies)
  - [1.9: Why should you use IHttpClientFactory instead of instantiating HttpClient directly?](#19-why-should-you-use-ihttpclientfactory-instead-of-instantiating-httpclient-directly)

- [Part 2: Top 26 Most-Asked Indian Screening & Technical Round 1 Hitlist](#part-2-top-26-most-asked-indian-screening-technical-round-1-hitlist)
  - [Q1: How do you explain and apply SOLID principles in a real-world Web API?](#q1-how-do-you-explain-and-apply-solid-principles-in-a-real-world-web-api)
  - [Q2: What is the difference between IEnumerable, IQueryable, ICollection, and IList?](#q2-what-is-the-difference-between-ienumerable-iqueryable-icollection-and-ilist)
  - [Q3: What is string immutability and when should you use StringBuilder?](#q3-what-is-string-immutability-and-when-should-you-use-stringbuilder)
  - [Q4: What is the difference between ref, out, in, and params in C#?](#q4-what-is-the-difference-between-ref-out-in-and-params-in-c)
  - [Q5: What is the difference between throw, throw ex, and throw new CustomException?](#q5-what-is-the-difference-between-throw-throw-ex-and-throw-new-customexception)
  - [Q6: When should you use an abstract class versus an interface with C# 8+ default methods?](#q6-when-should-you-use-an-abstract-class-versus-an-interface-with-c-8-default-methods)
  - [Q7: How do boxing and unboxing work and what is their performance cost?](#q7-how-do-boxing-and-unboxing-work-and-what-is-their-performance-cost)
  - [Q8: What is the difference between method overloading, overriding, and method shadowing?](#q8-what-is-the-difference-between-method-overloading-overriding-and-method-shadowing)
  - [Q9: What is the difference between const, readonly, and static readonly?](#q9-what-is-the-difference-between-const-readonly-and-static-readonly)
  - [Q10: How do Dependency Injection lifetimes work and what is a captive dependency?](#q10-how-do-dependency-injection-lifetimes-work-and-what-is-a-captive-dependency)
  - [Q11: What is the architectural difference between Middleware and Action Filters in ASP.NET Core?](#q11-what-is-the-architectural-difference-between-middleware-and-action-filters-in-aspnet-core)
  - [Q12: How do you write custom middleware for global exception handling using ProblemDetails?](#q12-how-do-you-write-custom-middleware-for-global-exception-handling-using-problemdetails)
  - [Q13: How do JWT authentication and authorization work in ASP.NET Core Web API?](#q13-how-do-jwt-authentication-and-authorization-work-in-aspnet-core-web-api)
  - [Q14: How does CORS work in ASP.NET Core and how do you configure it safely?](#q14-how-does-cors-work-in-aspnet-core-and-how-do-you-configure-it-safely)
  - [Q15: What is the difference between Eager Loading, Lazy Loading, and Explicit Loading in EF Core?](#q15-what-is-the-difference-between-eager-loading-lazy-loading-and-explicit-loading-in-ef-core)
  - [Q16: What is the difference between First, FirstOrDefault, Single, SingleOrDefault, and Find in EF Core?](#q16-what-is-the-difference-between-first-firstordefault-single-singleordefault-and-find-in-ef-core)
  - [Q17: What does AsNoTracking do in EF Core and when should you use it?](#q17-what-does-asnotracking-do-in-ef-core-and-when-should-you-use-it)
  - [Q18: Does async and await create a new background thread for I/O operations?](#q18-does-async-and-await-create-a-new-background-thread-for-io-operations)
  - [Q19: Why should you use SemaphoreSlim instead of lock in asynchronous C# code?](#q19-why-should-you-use-semaphoreslim-instead-of-lock-in-asynchronous-c-code)
  - [Q20: What is the difference between a Clustered Index and a Non-Clustered Index in SQL Server?](#q20-what-is-the-difference-between-a-clustered-index-and-a-non-clustered-index-in-sql-server)
  - [Q21: How do you find the 2nd highest or Nth highest salary in SQL Server?](#q21-how-do-you-find-the-2nd-highest-or-nth-highest-salary-in-sql-server)
  - [Q22: What is the difference between DELETE, TRUNCATE, and DROP in SQL Server?](#q22-what-is-the-difference-between-delete-truncate-and-drop-in-sql-server)
  - [Q23: What is the difference between UNION and UNION ALL in SQL Server?](#q23-what-is-the-difference-between-union-and-union-all-in-sql-server)
  - [Q24: What is the difference between a Primary Key and a Unique Key constraint?](#q24-what-is-the-difference-between-a-primary-key-and-a-unique-key-constraint)
  - [Q25: What is the difference between a Stored Procedure and a User-Defined Function (UDF)?](#q25-what-is-the-difference-between-a-stored-procedure-and-a-user-defined-function-udf)
  - [Q26: How do you explain ACID properties with a real-world banking scenario?](#q26-how-do-you-explain-acid-properties-with-a-real-world-banking-scenario)

---

# Part 1: Core .NET Runtime & Web Architecture Rapid Revision

## 1.1: How does .NET Garbage Collection manage memory across generations?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Generational GC** means the runtime groups objects by expected lifetime into Gen 0, Gen 1, Gen 2, and the LOH.

**🗣️ Spoken answer (30–45 seconds)**
Under the **generational hypothesis**, most objects die shortly after allocation. The **.NET Generational GC** organizes memory into **ephemeral generations**—**Gen 0** for short-lived temporaries and **Gen 1** for buffers—while long-lived objects advance to **Gen 2**. Objects ≥85 KB land directly on the **Large Object Heap (LOH)**, which is swept in place to avoid expensive compaction. In my project, using **MemoryPool** to reuse large buffers eliminated **GC pressure** from repeated LOH allocations.

**🎯 Terms the interviewer listens for**
- ⭐ **Generational hypothesis** — most objects die very shortly after allocation
- ⭐ **Ephemeral generations** — Gen 0 and Gen 1 collected during short pauses
- ⭐ **Large Object Heap (LOH)** — separate heap for objects ≥85 KB
- **Stop-the-world pause** — freezing app threads while collecting memory
- **Mark-sweep-compact** — algorithm identifying live objects and defragmenting
- **Finalization queue** — internal list tracking objects awaiting finalizer

**🧠 Memory hook**
Generation zero is a desk wastebasket emptied every hour; generation two is a warehouse requiring a full shutdown to clean.

**💻 Code**
```csharp
// ❌ Bad: repeated large buffer allocations
byte[] temp = new byte[90000];
ProcessData(temp);

// ✅ Good: reuse shared memory pool
using var owner = MemoryPool<byte>.Shared.Rent(90000);
ProcessData(owner.Memory.Span);
```

**⚠️ Likely follow-up**
**Question:** Why does allocating eighty-five thousand bytes skip generation zero?
**Answer:** Compacting huge memory chunks is too expensive. The runtime sweeps large objects in place to avoid heavy CPU memory-copying overhead.

**📊 Quick comparison**
| Generation | Target Lifetime | Compaction |
| :--- | :--- | :--- |
| Gen 0 | Short-lived temporaries | Frequent and fast |
| Gen 1 | Ephemeral buffer | Fast transition |
| Gen 2 | Long-lived singletons | Full sweep pause |
| LOH | Eighty-five kilobytes plus | Swept in place |

**🔬 Under the hood**
Generation zero allocations happen on thread-local allocation contexts [TLAC]. This lets threads allocate without global heap locks, yielding extreme allocation speed until a generation budget triggers collection.

---

## 1.2: What is the difference between Workstation GC and Server GC?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Server GC** means one managed heap and dedicated GC thread per CPU core, maximizing throughput for web workloads.

**🗣️ Spoken answer (30–45 seconds)**
**Server GC** creates a dedicated managed heap and collection thread per logical processor, maximizing throughput under high concurrent traffic. **Workstation GC** uses a single heap optimized for UI responsiveness on desktop applications. ASP.NET Core enables **Concurrent GC** by default, collecting in the background without stopping all worker threads. In my project, tuning **Server GC** prevented request queuing during traffic spikes by parallelizing collection across cores.

**🎯 Terms the interviewer listens for**
- ⭐ **Server GC** — one managed heap and thread per CPU core
- ⭐ **Workstation GC** — single heap optimized for responsive desktop apps
- ⭐ **Concurrent GC** — collecting without stopping all worker threads
- **Throughput** — total requests processed over a sustained window
- **Thread affinity** — binding worker threads to dedicated processor cores
- **Background GC** — collecting ephemeral generations while user threads run

**🧠 Memory hook**
Workstation GC is one clerk serving a single line; Server GC is sixteen clerks running sixteen airport security lanes in parallel.

**💻 Code**
```xml
<!-- ❌ Bad: workstation GC in high-load API -->
<ServerGarbageCollection>false</ServerGarbageCollection>

<!-- ✅ Good: enable server GC for throughput -->
<ServerGarbageCollection>true</ServerGarbageCollection>
<ConcurrentGarbageCollection>true</ConcurrentGarbageCollection>
```

**⚠️ Likely follow-up**
**Question:** When would you use Workstation GC inside an ASP.NET Core container?
**Answer:** In microservices running in single-core containers with strictly constrained memory budgets, Workstation GC reduces baseline memory footprint.

**📊 Quick comparison**
| Mode | Heap Count | GC Threads | Best Target |
| :--- | :--- | :--- | :--- |
| Workstation | Single heap | Single thread | Desktop applications |
| Server | One per core | One per core | High-load web APIs |

**🔬 Under the hood**
Server GC assigns each core an independent allocation segment. When any segment exhausts its budget, a coordinated rendezvous signal pauses all mutator threads to conduct collection.

---

## 1.3: How does the IDisposable pattern differ from Finalize?
*Commonly asked at: TCS, Infosys, Wipro, Capgemini*

**⚡ One-line answer**
**Deterministic cleanup** means Dispose releases resources immediately, while Finalize is an unpredictable runtime fallback.

**🗣️ Spoken answer (30–45 seconds)**
**Deterministic cleanup** via Dispose releases **unmanaged resources** like file handles and sockets immediately at a known program location. The **Finalizer (~ClassName)** is a runtime fallback that runs unpredictably on a single background thread during garbage collection. Relying on finalizers delays memory reclamation and promotes objects into Gen 2. Calling **GC.SuppressFinalize** inside Dispose prevents unnecessary GC promotion. In my project, the **using statement** guaranteed Dispose was always called, even on exceptions.

**🎯 Terms the interviewer listens for**
- ⭐ **Deterministic cleanup** — freeing resources immediately at a known location
- ⭐ **Finalizer (~ClassName)** — runtime fallback called before memory collection
- ⭐ **GC.SuppressFinalize** — instructs runtime to skip finalization queue
- **Unmanaged resources** — OS handles, sockets, and native memory
- **using statement** — language shortcut translating to try-finally Dispose
- **Finalization queue** — internal list tracking pending finalizer execution

**🧠 Memory hook**
Dispose is returning your rental car keys immediately; Finalize is the company hunting down the abandoned car weeks later.

**💻 Code**
```csharp
// ❌ Bad: leaks handle if exception occurs
var stream = new FileStream("data.bin", FileMode.Open);
Process(stream);

// ✅ Good: deterministic cleanup via using declaration
using var safeStream = new FileStream("data.bin", FileMode.Open);
Process(safeStream);
```

**⚠️ Likely follow-up**
**Question:** Why should you always call GC.SuppressFinalize(this) inside Dispose()?
**Answer:** It removes the object from the finalization queue, avoiding an extra collection cycle and premature promotion into generation two.

**📊 Quick comparison**
| Aspect | Dispose | Finalize |
| :--- | :--- | :--- |
| Invocation | Deterministic via code | Non-deterministic via GC |
| Execution thread | Calling worker thread | Dedicated finalizer thread |
| Performance | Negligible overhead | Promotes object generation |

**🔬 Under the hood**
Objects with finalizers survive generation zero collections because they require queue registration. The finalizer thread processes them asynchronously before their memory can be reclaimed in a subsequent cycle.

---

## 1.4: How do async and await work under the hood without blocking threads?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**IAsyncStateMachine** is a compiler-generated struct that pauses and resumes async methods, releasing the thread during I/O.

**🗣️ Spoken answer (30–45 seconds)**
The compiler rewrites each async method into an **IAsyncStateMachine** struct that tracks execution across suspension points. On hitting an await, the current thread yields back to the pool via **thread yielding**. The OS delivers completion signals through **I/O Completion Ports (IOCP)**, a kernel notification mechanism for non-blocking I/O. No new threads are created for network or file operations. In my project, async code allowed twenty web threads to serve ten thousand concurrent users without blocking.

**🎯 Terms the interviewer listens for**
- ⭐ **IAsyncStateMachine** — compiler-generated struct tracking execution across suspensions
- ⭐ **I/O Completion Ports (IOCP)** — OS notification mechanism for non-blocking I/O
- ⭐ **Thread yielding** — returning worker threads to the pool during I/O
- **Continuation callback** — delegate invoked when an awaited operation finishes
- **TaskCompletionSource** — creates tasks that complete on external events
- **Synchronization context** — legacy component absent in ASP.NET Core

**🧠 Memory hook**
A restaurant waiter takes your order to the kitchen and serves other diners; he does not stand staring at the oven.

**💻 Code**
```csharp
// ❌ Bad: blocks threadpool thread while waiting
var task = client.GetStringAsync(url);
var result = task.Result;

// ✅ Good: yields thread during network I/O
var safeResult = await client.GetStringAsync(url);
return safeResult;
```

**⚠️ Likely follow-up**
**Question:** Why does ASP.NET Core omit a SynchronizationContext?
**Answer:** Removing SynchronizationContext eliminates lock contention and thread affinity overhead, allowing continuations to resume on any free thread pool thread.

**📊 Quick comparison**
| Mechanism | Thread Usage | CPU Blocking | Scalability |
| :--- | :--- | :--- | :--- |
| Synchronous | Keeps thread busy | Blocks thread completely | Low under concurrency |
| Asynchronous | Yields thread immediately | Zero blocking overhead | High server throughput |

**🔬 Under the hood**
When an awaited task is not completed, AwaitUnsafeOnCompleted registers the continuation. The state machine captures local variables as fields on the struct, boxing to the heap only when necessary.

---

## 1.5: When should you use ValueTask instead of Task?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**ValueTask<T>** is a stack-allocated struct that avoids Task heap allocation when the result is already available synchronously.

**🗣️ Spoken answer (30–45 seconds)**
**ValueTask<T>** is a struct that avoids allocating a heap object when the result is already available, such as on a cache hit via **synchronous completion**. Task is a reference type that always allocates on the managed heap, generating **GC Gen 0 pressure** from short-lived objects. If the operation must perform real asynchronous I/O, ValueTask wraps a normal Task fallback internally. In my project, returning **ValueTask** from a memory cache dropped Gen 0 collections significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **ValueTask<T>** — stack-allocated struct avoiding heap allocation on sync completion
- ⭐ **Synchronous completion** — returning cached result without suspension
- ⭐ **GC Gen 0 pressure** — overhead from rapidly allocating short-lived heap objects
- **Heap allocation** — reserving dynamic memory managed by garbage collection
- **IValueTaskSource** — advanced interface allowing reusable custom backings
- **Single-await constraint** — rule prohibiting awaiting ValueTask multiple times

**🧠 Memory hook**
Task is an official paper receipt printed from a machine; ValueTask is checking your wristwatch with zero paper waste.

**💻 Code**
```csharp
// ❌ Bad: allocates Task object on cache hit
public Task<string> GetData(string k) => Task.FromResult(_cache[k]);

// ✅ Good: zero heap allocation on cache hit
public ValueTask<string> GetData(string k) => 
    _cache.TryGetValue(k, out var v) ? new(v) : new(FetchAsync(k));
```

**⚠️ Likely follow-up**
**Question:** Why cannot you await a ValueTask multiple times?
**Answer:** ValueTask may wrap a pooled IValueTaskSource that gets recycled immediately after the first await, causing corruption on subsequent awaits.

**📊 Quick comparison**
| Type | Memory Location | Synchronous Allocation | Multiple Awaits |
| :--- | :--- | :--- | :--- |
| Task<T> | Managed heap | Allocates object | Allowed safely |
| ValueTask<T> | Stack struct | Zero heap allocation | Strictly prohibited |

**🔬 Under the hood**
ValueTask<T> is a discriminated union containing either a TResult, a Task<TResult>, or an IValueTaskSource<TResult>. If the result is ready, no object is instantiated.

---

## 1.6: What causes ThreadPool starvation and how does sync-over-async trigger it?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Sync-over-async** means blocking on .Result/.Wait(), starving the thread pool because new threads inject slowly.

**🗣️ Spoken answer (30–45 seconds)**
**Sync-over-async** occurs when synchronous code calls `.Result` or `.Wait()` on async methods, holding worker threads hostage. Under high load this causes **ThreadPool starvation**, where all pool threads are blocked and incoming requests queue. The .NET **thread injection rate** adds new threads slowly—roughly one every 500 ms—so recovery is sluggish. In my project, removing `.GetAwaiter().GetResult()` from a hot path dropped p99 API latency instantly.

**🎯 Terms the interviewer listens for**
- ⭐ **Sync-over-async** — anti-pattern of blocking synchronously on async operations
- ⭐ **ThreadPool starvation** — depletion of worker threads causing queued requests
- ⭐ **Thread injection rate** — throttled pace the runtime spawns new workers
- **Hill-climbing algorithm** — heuristic dynamically sizing the thread pool
- **Work-stealing queue** — thread-local queues letting idle threads take tasks
- **Deadlock risk** — cyclic waiting when continuation needs the blocked thread

**🧠 Memory hook**
A bank teller freezing at the counter waiting for mail delivery, refusing to serve hundreds of customers waiting outside.

**💻 Code**
```csharp
// ❌ Bad: sync-over-async triggers threadpool starvation
var task = _orderService.GetOrdersAsync();
var data = task.Result;

// ✅ Good: async all the way down
var safeData = await _orderService.GetOrdersAsync();
return safeData;
```

**⚠️ Likely follow-up**
**Question:** What tool do you use to diagnose ThreadPool starvation in production?
**Answer:** Use dotnet-counters monitoring ThreadPool.ThreadCount and ThreadPool.QueueLength, or capture a memory dump with dotnet-dump inspecting active stacks.

**📊 Quick comparison**
| Pattern | Thread Behavior | Starvation Risk | Throughput |
| :--- | :--- | :--- | :--- |
| await task | Releases thread to pool | Zero starvation | Maximum scalability |
| .Result / .Wait() | Freezes worker thread | Extreme under load | Latency spikes |

**🔬 Under the hood**
The CLR thread pool uses a hill-climbing algorithm to regulate concurrency. When threads block on kernel events, throughput drops, but the runtime only creates new threads slowly to prevent thrashing.

---

## 1.7: How does the ASP.NET Core middleware request pipeline execute?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**RequestDelegate** is the Func<HttpContext, Task> that chains middleware into a bidirectional request-response pipeline.

**🗣️ Spoken answer (30–45 seconds)**
Each middleware is a **RequestDelegate** (a `Func<HttpContext, Task>`) that forms a **bidirectional pipeline**, processing the request on entry and the response on return. Registered before UseRouting, middleware cannot see endpoint metadata; after UseRouting, it crosses the **endpoint routing boundary** and can inspect route data. Middleware never sees action arguments or ModelState, which belong to MVC filters. In my project, placing authentication middleware after routing enabled endpoint-aware authorization checks.

**🎯 Terms the interviewer listens for**
- ⭐ **RequestDelegate** — Func<HttpContext, Task> processing web requests
- ⭐ **Bidirectional pipeline** — processing request inbound and response outbound
- ⭐ **Endpoint routing boundary** — separation between raw HTTP and endpoint metadata
- **app.Use** — chains middleware with downstream next delegate
- **app.Run** — terminal middleware terminating pipeline execution
- **app.Map** — branches pipeline based on URL path matching

**🧠 Memory hook**
An airport security line where each guard inspects your ticket sequentially, passing you forward until the return exit stamp.

**💻 Code**
```csharp
// ❌ Bad: terminal middleware stops all downstream components
app.Run(async ctx => await ctx.Response.WriteAsync("Done"));

// ✅ Good: chains execution and measures downstream duration
app.Use(async (ctx, next) => {
    var sw = Stopwatch.StartNew();
    await next();
    ctx.Response.Headers["X-Elapsed"] = sw.ElapsedMilliseconds.ToString();
});
```

**⚠️ Likely follow-up**
**Question:** What is the difference between app.Use and app.Map?
**Answer:** app.Use chains a middleware into the main linear pipeline, whereas app.Map branches the pipeline based on matched URL path prefixes.

**📊 Quick comparison**
| Method | Pipeline Action | Forwards to Next? | Use Case |
| :--- | :--- | :--- | :--- |
| app.Use | Chains middleware | Yes via await next() | Cross-cutting logic |
| app.Run | Terminates pipeline | No | Terminal endpoints |
| app.Map | Branches pipeline | Conditionally | Health check routes |

**🔬 Under the hood**
Application builder chains Use calls in reverse order using delegate closures. The resulting compiled delegate pipeline is a single composite RequestDelegate executed with zero allocation per request.

---

## 1.8: What are Dependency Injection lifetimes and how do you avoid captive dependencies?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Captive dependency** means a long-lived service traps a shorter-lived one, causing leaks or concurrency bugs.

**🗣️ Spoken answer (30–45 seconds)**
ASP.NET Core provides three DI lifetimes: **Transient** creates a new instance every injection, **Scoped** creates one per HTTP request, and **Singleton** lives for the entire app. A **captive dependency** occurs when a Singleton injects a Scoped service directly, trapping it forever. Resolving scoped services safely inside singletons requires **IServiceScopeFactory** to create manual child scopes. In my project, this pattern prevented DbContext concurrency crashes in background workers.

**🎯 Terms the interviewer listens for**
- ⭐ **Captive dependency** — long-lived service trapping a shorter-lived one
- ⭐ **IServiceScopeFactory** — factory to create manual child request scopes
- ⭐ **Scoped lifetime** — single instance shared per HTTP request boundary
- **Transient lifetime** — new instance on every injection request
- **Singleton lifetime** — one instance shared application-wide
- **ValidateScopes** — DI setting catching captive dependencies at startup

**🧠 Memory hook**
Transient is a paper cup; scoped is a restaurant plate during dinner; singleton is the office water cooler.

**💻 Code**
```csharp
// ❌ Bad: singleton captures scoped DbContext directly
public class Worker(AppDbContext db) { }

// ✅ Good: creates safe scope inside singleton service
public class Worker(IServiceScopeFactory factory) {
    public void Run() {
        using var scope = factory.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    }
}
```

**⚠️ Likely follow-up**
**Question:** How does the runtime help you detect captive dependencies in development?
**Answer:** ASP.NET Core enables ValidateScopes and ValidateOnBuild by default in development mode, throwing an InvalidOperationException on startup if detected.

**📊 Quick comparison**
| Lifetime | Creation Frequency | Disposal Timing | Thread Safety |
| :--- | :--- | :--- | :--- |
| Transient | Every injection | End of scope | Thread safe |
| Scoped | Once per request | Request completion | Single thread only |
| Singleton | Once per app | App shutdown | Must be thread-safe |

**🔬 Under the hood**
Each created scope maintains a Disposables list. When the scope terminates, it iterates through this list in reverse order, calling Dispose on every resolved IDisposable instance.

---

## 1.9: Why should you use IHttpClientFactory instead of instantiating HttpClient directly?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**IHttpClientFactory** is a factory that pools HTTP handlers, preventing socket exhaustion and rotating DNS every two minutes.

**🗣️ Spoken answer (30–45 seconds)**
Creating HttpClient manually causes **socket exhaustion** where TCP ports get stuck in TIME_WAIT state. A static HttpClient ignores **DNS rotation**, pointing at stale IPs indefinitely. **IHttpClientFactory** solves both by pooling **HttpMessageHandler** instances and rotating them every two minutes, refreshing DNS without dropping active connections. In my project, registering typed clients via the factory eliminated outgoing connection errors during cloud deployment migrations.

**🎯 Terms the interviewer listens for**
- ⭐ **IHttpClientFactory** — factory managing lifecycle and pooling of HTTP handlers
- ⭐ **Socket exhaustion** — TCP port depletion trapped in TIME_WAIT state
- ⭐ **DNS rotation** — periodic handler expiration honoring updated IP records
- **HttpMessageHandler** — low-level component managing raw HTTP connections
- **Typed client** — strongly-typed service injecting a configured HttpClient
- **Two-minute lifetime** — default rotation period for pooled handlers

**🧠 Memory hook**
A car rental fleet where cars are returned, cleaned, and swapped every two minutes so engines stay modern.

**💻 Code**
```csharp
// ❌ Bad: instantiating HttpClient causes socket exhaustion
using var client = new HttpClient();
var data = await client.GetStringAsync(url);

// ✅ Good: register typed client in Program.cs
builder.Services.AddHttpClient<PaymentService>(c => {
    c.BaseAddress = new Uri("https://api.payments.com");
});
```

**⚠️ Likely follow-up**
**Question:** What is the default handler lifetime in IHttpClientFactory?
**Answer:** The default handler lifetime is two minutes, balancing active socket reuse against DNS record changes.

**📊 Quick comparison**
| Approach | Socket Reuse | DNS Awareness | Lifecycle Safety |
| :--- | :--- | :--- | :--- |
| new HttpClient() | No (Socket leak) | Yes | Danger in loops |
| Static HttpClient | Yes | No (Stale IP) | Risk on DNS shift |
| IHttpClientFactory | Yes (Pooled) | Yes (Two minutes) | Recommended standard |

**🔬 Under the hood**
IHttpClientFactory creates an ActiveHandlerTrackingEntry. After two minutes, the entry moves to an expired cleanup queue where it is disposed only after all ongoing HTTP requests complete.

---

# Part 2: Top 26 Most-Asked Indian Screening & Technical Round 1 Hitlist

## Q1: How do you explain and apply SOLID principles in a real-world Web API?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**SOLID** is five OOP design principles that isolate changes, reduce coupling, and ensure maintainability.

**🗣️ Spoken answer (30–45 seconds)**
**SOLID** provides five architectural guardrails preventing code rot. **Single Responsibility** keeps each class focused on one business task. **Open/Closed** lets you extend behavior through abstractions without modifying existing code. Liskov Substitution ensures derived types honor base contracts. Interface Segregation splits fat contracts into role-based interfaces. **Dependency Inversion** decouples high-level services from concrete implementations via abstractions. In my project, abstracting payment gateways allowed adding providers without altering checkout logic.

**🎯 Terms the interviewer listens for**
- ⭐ **Single Responsibility** — class should have only one reason to change
- ⭐ **Open/Closed Principle** — open for extension, closed for modification
- ⭐ **Dependency Inversion** — high-level modules depend on abstractions, not concretes
- **Liskov Substitution** — derived types must substitute base types safely
- **Interface Segregation** — clients should not implement unused methods
- **High cohesion** — keeping related logic grouped tightly inside one class

**🧠 Memory hook**
A smartphone where you plug in headphones and install apps without opening the motherboard or rewriting the operating system.

**💻 Code**
```csharp
// ❌ Bad: tightly coupled to concrete class
public class OrderService {
    private readonly SqlRepo _repo = new();
}

// ✅ Good: depends on abstraction via DI
public class OrderService(IOrderRepo repo) {
    private readonly IOrderRepo _repo = repo;
}
```

**⚠️ Likely follow-up**
**Question:** How does Interface Segregation differ from Single Responsibility?
**Answer:** Single responsibility governs class implementation duties, whereas interface segregation governs client-facing contract granularity so clients only implement methods they use.

**📊 Quick comparison**
| Principle | Core Focus | Primary Benefit |
| :--- | :--- | :--- |
| S | One class responsibility | High cohesion |
| O | Extension via abstractions | Zero regression risk |
| L | Contract substitutability | Predictable polymorphism |
| I | Focused role interfaces | Minimal boilerplate |
| D | Abstraction inversion | Decoupled dependencies |

**🔬 Under the hood**
In ASP.NET Core, Dependency Inversion is implemented via the built-in IServiceProvider container, which maps service interfaces to concrete type descriptors stored in a thread-safe registry.

---

## Q2: What is the difference between IEnumerable, IQueryable, ICollection, and IList?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**IQueryable** is a provider-based interface that compiles expression trees into SQL for server-side evaluation.

**🗣️ Spoken answer (30–45 seconds)**
**IQueryable<T>** translates **expression trees** (code represented as data nodes) into native SQL for **server-side evaluation** on the database. **IEnumerable<T>** streams records forward-only in memory using deferred execution. ICollection adds mutation methods like Add and Remove, while IList extends collection with zero-based index access. In my project, returning IQueryable instead of IEnumerable stopped loading thousands of rows into server RAM unnecessarily.

**🎯 Terms the interviewer listens for**
- ⭐ **IQueryable<T>** — provider-based query compiling expression trees into SQL
- ⭐ **IEnumerable<T>** — forward-only in-memory sequence with deferred iteration
- ⭐ **Expression tree** — data structure representing code logic as syntax nodes
- **ICollection<T>** — collection adding element count and mutation methods
- **IList<T>** — indexable collection providing random-position access
- **Deferred execution** — delaying query evaluation until enumerated

**🧠 Memory hook**
IEnumerable is buying the whole buffet to eat one dish; IQueryable is ordering only that single dish from the kitchen menu.

**💻 Code**
```csharp
// ❌ Bad: loads all rows into RAM
IEnumerable<Order> list = db.Orders;
var shipped = list.Where(o => o.Shipped).ToList();

// ✅ Good: executes WHERE on SQL Server
IQueryable<Order> query = db.Orders;
var shippedFast = query.Where(o => o.Shipped).ToList();
```

**⚠️ Likely follow-up**
**Question:** Why does calling .ToList() change query execution behavior?
**Answer:** .ToList() triggers immediate execution, materializing SQL query results from the database into in-memory managed objects on the heap.

**📊 Quick comparison**
| Interface | Filtering Location | Direct Indexing | Mutation Support |
| :--- | :--- | :--- | :--- |
| IEnumerable | In memory | No | Read only |
| IQueryable | Database server | No | Read only |
| ICollection | In memory | No | Add and Remove |
| IList | In memory | Yes (list[0]) | Full indexing |

**🔬 Under the hood**
IQueryable wraps an IQueryProvider. When LINQ operators append to the expression tree, the provider parses the tree visitor into dialect-specific SQL, executing remotely on GetEnumerator().

---

## Q3: What is string immutability and when should you use StringBuilder?
*Commonly asked at: TCS, Infosys, Wipro, Capgemini*

**⚡ One-line answer**
**String immutability** means every modification allocates a new object; **StringBuilder** mutates an internal buffer in place.

**🗣️ Spoken answer (30–45 seconds)**
**String immutability** means C# strings cannot be changed after creation—every concatenation allocates a brand-new heap object. **StringBuilder** maintains a growable internal buffer that mutates in place, avoiding intermediate allocations. In loops, repeated string += creates heavy **GC pressure** from short-lived Gen 0 objects. The CLR also uses **string interning** to share a single heap instance for identical literals. In my project, replacing concatenation in a CSV loop with StringBuilder cut Gen 0 pauses significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **String immutability** — inability to modify text after object creation
- ⭐ **StringBuilder** — mutable character buffer resizing without intermediate allocations
- ⭐ **String interning** — CLR pool sharing single heap instances for identical literals
- **GC pressure** — overhead caused by rapid short-lived allocations
- **Buffer doubling** — capacity growth algorithm resizing when filled
- **Heap allocation** — memory assigned to reference type instances

**🧠 Memory hook**
String is a printed permanent passport requiring a new booklet for any change; StringBuilder is a reusable dry-erase whiteboard.

**💻 Code**
```csharp
// ❌ Bad: creates 1000 temporary strings
string s = "";
for (int i = 0; i < 1000; i++) s += i;

// ✅ Good: mutates preallocated internal buffer
var sb = new StringBuilder(4000);
for (int i = 0; i < 1000; i++) sb.Append(i);
```

**⚠️ Likely follow-up**
**Question:** When is string concatenation faster than using StringBuilder?
**Answer:** For three or four static strings, the Roslyn compiler optimizes concatenation into a single string.Concat call, outperforming StringBuilder initialization.

**📊 Quick comparison**
| Feature | string | StringBuilder |
| :--- | :--- | :--- |
| Mutability | Immutable | Mutable buffer |
| Thread Safety | Inherently thread-safe | Not thread-safe |
| Memory Impact | Allocates on edit | Reuses memory buffer |
| Best For | Few static strings | Loops and dynamic text |

**🔬 Under the hood**
StringBuilder manages memory as linked chunks of character arrays (m_ChunkChars). When capacity is exceeded, it links a new block or expands geometrically, eliminating contiguous array reallocations.

---

## Q4: What is the difference between ref, out, in, and params in C#?
*Commonly asked at: Accenture, Capgemini, Infosys, Cognizant*

**⚡ One-line answer**
**Pass-by-reference** means ref, out, and in all pass managed pointers, differing in assignment and mutability rules.

**🗣️ Spoken answer (30–45 seconds)**
**Pass-by-reference** lets ref, out, and in transmit a managed pointer instead of copying a value. **ref** requires caller initialization and allows two-way read/write. **out** enforces **definite assignment**, requiring the callee to assign before returning. **in** passes a readonly reference, achieving **zero-copy for large structs** without allowing mutation. params accepts a variable argument list packed into an array. In my project, using in for coordinate structs improved mathematical calculation performance.

**🎯 Terms the interviewer listens for**
- ⭐ **Pass-by-reference** — transmitting a managed pointer instead of copying
- ⭐ **Definite assignment** — compiler guarantee variables are assigned before reading
- ⭐ **Zero-copy for large structs** — in keyword avoids expensive struct copies
- **ref keyword** — two-way read/write parameter by reference
- **out parameter** — enforces mandatory callee assignment before return
- **params keyword** — accepts variable-count arguments as an array

**🧠 Memory hook**
ref is a shared shared doc; out is an empty exam sheet you must fill; in is a laminated photo ID.

**💻 Code**
```csharp
// ❌ Bad: copies large struct on every call
public decimal Calc(MatrixLarge data) => data.M11 * 2;

// ✅ Good: passes readonly reference without copy
public decimal Calc(in MatrixLarge data) => data.M11 * 2;

// ✅ Good: out guarantees mandatory initialization
public bool TryParse(string s, out int val) => int.TryParse(s, out val);
```

**⚠️ Likely follow-up**
**Question:** Can you overload a method differing only by ref and out?
**Answer:** No, the compiler treats ref and out identically in IL metadata signatures, causing a compilation error if only their modifier differs.

**📊 Quick comparison**
| Keyword | Caller Initialization | Callee Must Assign | Mutability |
| :--- | :--- | :--- | :--- |
| ref | Required | Optional | Read and Write |
| out | Not required | Mandatory | Write before exit |
| in | Required | Prohibited | Read-only access |
| params | Optional array | Optional | Standard array |

**🔬 Under the hood**
Under the hood, ref, out, and in compile to identical CLR managed pointers (T&). The differences exist purely as Roslyn compiler safety rules enforcing definite assignment and immutability invariants.

---

## Q5: What is the difference between throw, throw ex, and throw new CustomException?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Stack trace preservation** means bare `throw;` keeps the original call history, while `throw ex` resets it.

**🗣️ Spoken answer (30–45 seconds)**
**Stack trace preservation** is critical for debugging production issues. Bare **throw;** rethrows the current exception preserving the entire original call stack and line numbers. **throw ex** is an anti-pattern that resets the stack trace to the catch block, destroying origin information. Wrapping with a custom exception preserves root causes via **InnerException** chaining. In my project, eliminating throw ex reduced production incident investigation time significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **Stack trace preservation** — retaining original call history and line numbers
- ⭐ **throw;** — rethrows current exception preserving complete diagnostic trace
- ⭐ **InnerException chaining** — linking previous failure causes inside wrapped exceptions
- **throw ex bug** — anti-pattern resetting stack origin to catch block
- **Stack unwinding** — freeing call frames during exception bubbling
- **Exception shielding** — preventing internal leaks to external API clients

**🧠 Memory hook**
Bare throw is an honest courier reporting the exact warehouse crash; throw ex tears off the tracking label and blames the local driver.

**💻 Code**
```csharp
try {
    ExecutePayment();
} catch (DbException ex) {
    // ❌ Bad: destroys line numbers of origin
    // throw ex;

    // ✅ Good: preserves complete call stack trace
    throw;
}
```

**⚠️ Likely follow-up**
**Question:** When should you create a custom exception in modern .NET?
**Answer:** Create custom exceptions for domain-specific business rules requiring distinct HTTP status code mapping, such as PaymentDeclinedException returning status 422.

**📊 Quick comparison**
| Statement | Preserves Stack? | Modifies Exception | Best Practice |
| :--- | :--- | :--- | :--- |
| throw; | Yes, full trace | No | Standard rethrow |
| throw ex; | No, resets origin | No | Dangerous anti-pattern |
| throw new(..., ex) | Preserves in Inner | Wraps into custom | Domain exception |

**🔬 Under the hood**
The CLR writes stack frames into an internal field on Exception. Calling throw ex overwrites this field with the current instruction pointer, erasing previous frames from memory.

---

## Q6: When should you use an abstract class versus an interface with C# 8+ default methods?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Interface contract** is a pure behavioral specification without state; an abstract class shares identity, fields, and constructors.

**🗣️ Spoken answer (30–45 seconds)**
An **interface contract** defines what a class can do—pure behavioral specification supporting multiple implementation and ideal for DI and mocking. An **abstract class** defines what a class is, allowing **single inheritance** with shared instance state, fields, and constructors. Even with C# 8 **default interface methods** added for backward compatibility, interfaces still cannot declare instance fields. In my project, abstract base repositories shared audit fields while interfaces exposed public contracts for injection.

**🎯 Terms the interviewer listens for**
- ⭐ **Interface contract** — pure behavioral specification without instance state
- ⭐ **Single inheritance** — language rule restricting classes to one base class
- ⭐ **Default interface methods** — interface implementations for backward compatibility
- **Multiple implementation** — implementing several interfaces in one class
- **Abstract class** — base class sharing code and state via inheritance
- **Virtual method table (vtable)** — memory table for dynamic dispatch

**🧠 Memory hook**
An interface is a driving license specifying skills; an abstract class is biological mammal DNA providing lungs and heart state.

**💻 Code**
```csharp
// ❌ Bad: interface cannot hold instance state
public interface IBadRepo {
    // protected string _conn; // Compile error!
}

// ✅ Good: abstract class holds shared fields
public abstract class BaseRepo(string conn) {
    protected readonly string _conn = conn;
}
```

**⚠️ Likely follow-up**
**Question:** Why cannot a class access a default interface method directly through its instance?
**Answer:** Default interface methods require explicit interface casting because they do not become part of the class public surface area.

**📊 Quick comparison**
| Feature | Interface | Abstract Class |
| :--- | :--- | :--- |
| Inheritance | Multiple allowed | Single class only |
| Instance Fields | Strictly prohibited | Allowed with state |
| Constructors | None | Supported |
| Access Modifiers | Public default | Public, protected, internal |

**🔬 Under the hood**
Interface dispatch uses interface method tables [IMT] resolved via dynamic stubs. Abstract class overrides resolve via direct slot offsets in the class virtual method table [vtable], providing slightly faster dispatch.

---

## Q7: How do boxing and unboxing work and what is their performance cost?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Boxing** means wrapping a stack value type into a heap object with a 16-byte header; unboxing extracts it back.

**🗣️ Spoken answer (30–45 seconds)**
**Boxing** converts a value type on the stack into a reference object on the managed heap, adding a 16-byte **object header** containing the method table pointer and sync block index. **Unboxing** verifies the type and copies the bits back onto the stack. Continuous boxing in hot loops creates short-lived allocations that trigger frequent GC pauses. **Generics** like `List<T>` eliminate boxing entirely at compile time. In my project, replacing ArrayList with generic List<int> eliminated millions of heap allocations.

**🎯 Terms the interviewer listens for**
- ⭐ **Boxing** — converting stack value type into heap-allocated reference object
- ⭐ **Object header** — 16-byte overhead with method table and sync block index
- ⭐ **Generics eliminate boxing** — parameterized types avoid boxing at compile time
- **Unboxing** — casting boxed object back into stack value type
- **Type safety check** — runtime verification that boxed type matches cast
- **GC Gen 0 churn** — excessive short-lived allocations triggering collection

**🧠 Memory hook**
Boxing is packing an apple into a bubble-wrapped cardboard parcel to store; unboxing is opening the box to retrieve it.

**💻 Code**
```csharp
// ❌ Bad: boxes int on every add
var list = new System.Collections.ArrayList();
list.Add(42);

// ✅ Good: generics avoid boxing completely
var safeList = new List<int>();
safeList.Add(42);
```

**⚠️ Likely follow-up**
**Question:** What exception is thrown if you unbox to the wrong value type?
**Answer:** The runtime throws an InvalidCastException because unboxing requires an exact type match before any numeric conversion can occur.

**📊 Quick comparison**
| Operation | Source Memory | Target Memory | Overhead |
| :--- | :--- | :--- | :--- |
| Boxing | Execution stack | Managed heap | Allocates sixteen bytes |
| Unboxing | Managed heap | Execution stack | Type verification check |
| Generics | Execution stack | Execution stack | Zero allocation overhead |

**🔬 Under the hood**
In Intermediate Language, boxing generates the box instruction. The runtime reserves an object header with MethodTable pointer and SyncBlockIndex, copying value bits into the object payload.

---

## Q8: What is the difference between method overloading, overriding, and method shadowing?
*Commonly asked at: TCS, Infosys, Capgemini, Accenture*

**⚡ One-line answer**
**Dynamic dispatch** means overriding resolves via the vtable at runtime, unlike compile-time overloading or shadowing.

**🗣️ Spoken answer (30–45 seconds)**
Method overloading defines multiple methods with identical names but distinct parameter signatures, resolved at **compile-time**. Method overriding provides runtime polymorphism through **dynamic dispatch**, where the CLR resolves calls via the **vtable** (virtual method table) to the concrete override. Method shadowing uses the `new` keyword to hide base members without participating in vtable dispatch—called through a base reference, the base method runs. In my project, accidental shadowing caused subtle accounting bugs that override would have prevented.

**🎯 Terms the interviewer listens for**
- ⭐ **Compile-time vs runtime polymorphism** — overloading at compile, overriding at runtime
- ⭐ **vtable** — internal lookup table resolving dynamic method addresses at runtime
- ⭐ **Dynamic dispatch** — runtime resolution selecting implementation by object type
- **Method overloading** — same name with distinct parameter signatures
- **Method shadowing (new)** — hiding base method without virtual dispatch
- **Early binding** — resolving method targets during compilation

**🧠 Memory hook**
Overloading is a multi-socket power adapter; overriding is a new smartphone ringtone; shadowing is wearing a disguise mask over your face.

**💻 Code**
```csharp
public class Base { public virtual string Name() => "Base"; }
public class Bad : Base { public new string Name() => "New"; }
public class Good : Base { public override string Name() => "Over"; }

// ❌ Shadowing hides polymorphism: prints "Base"
Base b1 = new Bad();
Console.WriteLine(b1.Name());

// ✅ Overriding honors dynamic type: prints "Over"
Base b2 = new Good();
Console.WriteLine(b2.Name());
```

**⚠️ Likely follow-up**
**Question:** Can you override a method that is not marked virtual or abstract?
**Answer:** No, C# requires methods to be explicitly declared virtual, abstract, or override in base classes to enable dynamic override dispatch.

**📊 Quick comparison**
| Concept | Binding Time | Keyword Used | Base Invocation Via Reference |
| :--- | :--- | :--- | :--- |
| Overloading | Compile time | None | Signature based |
| Overriding | Runtime | override | Derived method runs |
| Shadowing | Compile time | new | Base method runs |

**🔬 Under the hood**
The compiler emits callvirt for virtual methods. At runtime, the CLR dereferences the object MethodTable, looks up the vtable slot index, and jumps to the concrete override implementation.

---

## Q9: What is the difference between const, readonly, and static readonly?
*Commonly asked at: Capgemini, Accenture, Cognizant, Infosys*

**⚡ One-line answer**
**Compile-time constant** means a value baked into callers' IL; readonly and static readonly evaluate at runtime.

**🗣️ Spoken answer (30–45 seconds)**
A **compile-time constant** (const) is baked directly into callers via **IL inlining**—embedding literal values in bytecode—meaning changes require rebuilding all callers. A **readonly** field is an instance variable assignable only at declaration or inside constructors. A **static readonly** field is a runtime value initialized once per process in the **static constructor (.cctor)** when the type first loads. In my project, switching from const to static readonly eliminated multi-library deployment versioning mismatches.

**🎯 Terms the interviewer listens for**
- ⭐ **Compile-time constant** — value baked into callers' IL requiring rebuild on change
- ⭐ **IL inlining** — embedding literal values directly into referencing calling assemblies
- ⭐ **Static constructor (.cctor)** — special class constructor running once when type first loads
- **readonly field** — instance variable assignable only at declaration or in constructors
- **static readonly** — runtime value initialized once per process on type initialization
- **Assembly versioning trap** — bug when updated constants are not recompiled in consumers

**🧠 Memory hook**
const is a permanent birthmark in DNA; readonly is a passport number given at birth; static readonly is office Wi-Fi set on startup.

**💻 Code**
```csharp
// ❌ Bad: inlines across DLL boundaries
public const string ApiUrl = "https://v1.api.com";

// ✅ Good: evaluated safely at runtime
public static readonly string SafeUrl = 
    Environment.GetEnvironmentVariable("API_URL") ?? "https://api.com";
```

**⚠️ Likely follow-up**
**Question:** Why is public const considered dangerous in shared NuGet packages?
**Answer:** Because referencing assemblies inline the constant value during compilation, running with obsolete values until every consumer assembly is recompiled.

**📊 Quick comparison**
| Modifier | Evaluation Time | Assigned In | Lifetime Scope |
| :--- | :--- | :--- | :--- |
| const | Compile time | Declaration only | Inlined in IL |
| readonly | Runtime | Constructor | Per instance |
| static readonly | Runtime | Static constructor | Once per process |

**🔬 Under the hood**
The compiler replaces const with ldc.i4 or ldstr instructions in calling code. In contrast, static readonly accesses emit ldsfld, reading memory initialized during the type initializer [.cctor].

---

## Q10: How do Dependency Injection lifetimes work and what is a captive dependency?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Captive dependency** means a Singleton traps a Scoped service, causing memory leaks and thread-safety crashes.

**🗣️ Spoken answer (30–45 seconds)**
ASP.NET Core supports three DI lifetimes: **Transient** creates fresh instances every injection, **Scoped** creates one per HTTP request, and **Singleton** lives application-wide. A **captive dependency** occurs when a Singleton injects a Scoped service like DbContext, trapping it forever and causing memory leaks and multithreaded crashes. Using **IServiceScopeFactory** to create manual child scopes resolves this safely. In my project, the **root container** was leaking Scoped services until we added ValidateScopes in development mode.

**🎯 Terms the interviewer listens for**
- ⭐ **Transient lifetime** — new service instance on every injection call
- ⭐ **Scoped lifetime** — single instance per incoming HTTP request boundary
- ⭐ **Captive dependency** — long-lived service trapping shorter-lived one in memory
- **Singleton lifetime** — one instance created once, shared application-wide
- **IServiceScopeFactory** — factory to spawn manual child scopes safely
- **Root container** — top-level DI container holding singletons and registrations

**🧠 Memory hook**
Transient is a paper cup; scoped is your lunch plate during a meal; singleton is the shared office water cooler.

**💻 Code**
```csharp
// ❌ Bad: singleton captures scoped DbContext
public class QueueService(AppDbContext db) { }

// ✅ Good: creates scope manually inside singleton
public class QueueService(IServiceScopeFactory factory) {
    public async Task Process() {
        using var scope = factory.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
        await db.SaveChangesAsync();
    }
}
```

**⚠️ Likely follow-up**
**Question:** Why is DbContext configured as scoped by default?
**Answer:** Because DbContext is not thread-safe and tracks entity states; scoping isolates changes per HTTP request without cross-request state pollution.

**📊 Quick comparison**
| Lifetime | Created Per | Disposed At | Thread Safety |
| :--- | :--- | :--- | :--- |
| Transient | Each resolution | Scope end | Thread safe |
| Scoped | HTTP request | Request end | Single request only |
| Singleton | Application startup | App shutdown | Must handle concurrency |

**🔬 Under the hood**
The container maintains dictionary tables of service descriptors. Resolving a scoped service from the root container causes a memory leak, as the root retains disposal references until the application shuts down.

---

## Q11: What is the architectural difference between Middleware and Action Filters in ASP.NET Core?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**RequestDelegate** is the raw HTTP pipeline delegate; Action Filters run inside MVC with access to ActionExecutingContext.

**🗣️ Spoken answer (30–45 seconds)**
**RequestDelegate** (a `Func<HttpContext, Task>`) runs in the outer HTTP pipeline, processing raw requests without MVC awareness. After UseRouting, middleware crosses the **endpoint routing boundary** and can see route metadata. **Action filters** run inside MVC, receiving an **ActionExecutingContext** that exposes action arguments, ModelState, and controller metadata. Middleware never sees action parameters or ModelState. In my project, moving authorization from filters into middleware protected static files and API endpoints uniformly.

**🎯 Terms the interviewer listens for**
- ⭐ **RequestDelegate** — Func<HttpContext, Task> processing web requests
- ⭐ **Endpoint routing boundary** — separation between raw HTTP and endpoint metadata
- ⭐ **ActionExecutingContext** — filter context granting access to parameters and metadata
- **HttpContext** — raw HTTP request and response encapsulation
- **Action filter** — MVC pipeline component inspecting action arguments
- **Short-circuiting** — terminating request early without calling downstream

**🧠 Memory hook**
Middleware is the tech park gate security checking badges; an action filter is your team lead inspecting the exact sprint task at your desk.

**💻 Code**
```csharp
// ❌ Bad: cannot access action arguments in middleware
app.Use(async (ctx, next) => {
    // ctx.ActionArguments; // Does not exist!
    await next();
});

// ✅ Good: filter accesses action parameters cleanly
public class ValidateFilter : IActionFilter {
    public void OnActionExecuting(ActionExecutingContext ctx) {
        if (!ctx.ModelState.IsValid) ctx.Result = new BadRequestResult();
    }
    public void OnActionExecuted(ActionExecutedContext ctx) { }
}
```

**⚠️ Likely follow-up**
**Question:** Can middleware modify the response status code after calling next()?
**Answer:** Only if HttpResponse.HasStarted is false; once response headers flush to the network stream, attempting to modify status codes throws an InvalidOperationException.

**📊 Quick comparison**
| Feature | Middleware | Action Filter |
| :--- | :--- | :--- |
| Pipeline Layer | Outer HTTP pipeline | Inner MVC pipeline |
| Target Delegate | Func<HttpContext, Task> | Action method invocation |
| Sees Action Args | Never | Yes (ActionArguments) |
| Sees ModelState | Never | Yes (ModelState) |

**🔬 Under the hood**
UseRouting matches incoming URLs to endpoints, populating Endpoint metadata on HttpContext. Middleware registered after UseRouting reads this metadata via GetEndpoint(), while filters execute via ControllerActionInvoker.

---

## Q12: How do you write custom middleware for global exception handling using ProblemDetails?
*Commonly asked at: TCS, Infosys, Cognizant, Capgemini*

**⚡ One-line answer**
**ProblemDetails (RFC 7807)** is a standard error response format; global middleware maps unhandled exceptions into it.

**🗣️ Spoken answer (30–45 seconds)**
Global exception middleware wraps the pipeline in try-catch, mapping unhandled errors into **ProblemDetails (RFC 7807)**, a standardized machine-readable error format. It logs diagnostics using the **TraceIdentifier**, a unique correlation ID per request. Before writing the response, it checks Response.HasStarted to avoid **information disclosure** of raw stack traces to public callers. In my project, mapping domain exceptions to HTTP status codes via ProblemDetails gave clients consistent error payloads.

**🎯 Terms the interviewer listens for**
- ⭐ **ProblemDetails (RFC 7807)** — standard machine-readable HTTP error response
- ⭐ **TraceIdentifier** — unique correlation ID tracking requests across logs
- ⭐ **Information disclosure** — security vulnerability leaking stack traces
- **Global exception middleware** — outer pipeline catching all unhandled errors
- **Response.HasStarted** — guard checking if response headers were sent
- **Status code mapping** — translating exception types into HTTP codes

**🧠 Memory hook**
An airport lost-and-found desk giving you a standardized incident report receipt instead of having you panic on the airport runway.

**💻 Code**
```csharp
// ❌ Bad: unhandled error leaks stack trace
// app.Use(async (ctx, next) => { await next(); });

// ✅ Good: centralized exception handling with ProblemDetails
public class ErrorMiddleware(RequestDelegate next, ILogger<ErrorMiddleware> logger) {
    public async Task InvokeAsync(HttpContext ctx) {
        try { await next(ctx); }
        catch (Exception ex) {
            logger.LogError(ex, "Trace: {Id}", ctx.TraceIdentifier);
            if (ctx.Response.HasStarted) throw;
            ctx.Response.StatusCode = 500;
            await ctx.Response.WriteAsJsonAsync(new ProblemDetails { Status = 500, Title = "Server Error" });
        }
    }
}
```

**⚠️ Likely follow-up**
**Question:** What built-in alternative exists in ASP.NET Core 8 for exception handling?
**Answer:** ASP.NET Core 8 provides IExceptionHandler and AddProblemDetails(), allowing modular exception handling without writing custom middleware manually.

**📊 Quick comparison**
| Approach | Catches Middleware Errors | Standard Payload | Setup Complexity |
| :--- | :--- | :--- | :--- |
| Try-Catch Controller | No | Inconsistent | High repetitive code |
| Exception Filter | No (MVC only) | Custom | Moderate |
| Global Middleware | Yes (Entire pipeline) | RFC 7807 | Centralized single point |

**🔬 Under the hood**
If an exception occurs after HttpResponse.HasStarted flips to true, the response stream cannot be reset. The middleware must rethrow, causing the server to abort the underlying TCP connection cleanly.

---

## Q13: How do JWT authentication and authorization work in ASP.NET Core Web API?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**ClaimsPrincipal** is the identity object populated from a validated JWT bearer token on HttpContext.User.

**🗣️ Spoken answer (30–45 seconds)**
JWT authentication validates a **Bearer token** (a signed header.payload.signature) and populates a **ClaimsPrincipal** on HttpContext.User containing the user's claims and roles. Middleware verifies signature, issuer, audience, and expiration. By default, token validation permits five minutes of **ClockSkew** tolerance for clock drift. Setting ClockSkew to zero prevents expired token acceptance. In my project, enforcing zero ClockSkew with symmetric key validation tightened our API security posture.

**🎯 Terms the interviewer listens for**
- ⭐ **ClaimsPrincipal** — identity object on HttpContext containing user claims
- ⭐ **ClockSkew** — time drift tolerance defaulting to five minutes
- ⭐ **Bearer token** — signed token proving identity via authorization header
- **Symmetric security key** — shared secret for HMAC signature verification
- **Token validation parameters** — settings for signature, audience, and lifetime
- **Stateless authentication** — verifying requests without server-side sessions

**🧠 Memory hook**
A tamper-proof airline boarding pass showing your name and seat, signed with a digital hologram barcode verified by security guards.

**💻 Code**
```csharp
// ❌ Bad: default clock skew allows expired tokens
// options.TokenValidationParameters = new();

// ✅ Good: eliminates grace drift on token expiry
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o => o.TokenValidationParameters = new() {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ClockSkew = TimeSpan.Zero,
        IssuerSigningKey = new SymmetricSecurityKey(key)
    });
```

**⚠️ Likely follow-up**
**Question:** How do you revoke a stateless JWT before its natural expiration?
**Answer:** Store revoked token identifiers [JTI] in a fast distributed cache like Redis, checking the blacklist during token validation.

**📊 Quick comparison**
| Aspect | Session Cookie | JWT Bearer |
| :--- | :--- | :--- |
| Server State | Stored in memory | Completely stateless |
| Scalability | Requires sticky sessions | Scales horizontally |
| Mobile Support | Awkward cookie handling | Standard HTTP header |
| Revocation | Instant on server | Requires blacklist cache |

**🔬 Under the hood**
JwtSecurityTokenHandler decodes Base64Url segments, verifies the signature against the raw bytes using cryptographic algorithms, and constructs Claim objects assigned to ClaimsIdentity on the executing context.

---

## Q14: How does CORS work in ASP.NET Core and how do you configure it safely?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Same-Origin Policy** is the browser rule CORS relaxes via preflight OPTIONS handshakes and access-control headers.

**🗣️ Spoken answer (30–45 seconds)**
Browsers enforce the **Same-Origin Policy (SOP)**, blocking scripts from accessing resources on different domains. CORS relaxes this via a **Preflight OPTIONS** handshake where the browser asks the server which origins, methods, and headers are allowed. The server responds with the **Access-Control-Allow-Origin** header listing permitted domains. In ASP.NET Core, UseCors must sit between UseRouting and UseAuthentication. In my project, specifying explicit client domains prevented cross-origin exposure while supporting credentials.

**🎯 Terms the interviewer listens for**
- ⭐ **Same-Origin Policy (SOP)** — browser rule restricting cross-domain resource access
- ⭐ **Preflight OPTIONS** — preliminary handshake checking permitted methods and headers
- ⭐ **Access-Control-Allow-Origin** — response header indicating allowed client origins
- **AllowCredentials** — policy permitting cookies and auth headers in requests
- **Middleware ordering** — positioning UseCors between UseRouting and UseAuth
- **Wildcard prohibition** — spec rule blocking AllowAnyOrigin with credentials

**🧠 Memory hook**
An embassy visa officer: before letting a foreign visitor through, the browser checks if the destination server officially stamped permission for that origin.

**💻 Code**
```csharp
// ❌ Bad: wildcard origin with credentials throws exception
// policy.AllowAnyOrigin().AllowCredentials();

// ✅ Good: specify explicit trusted origins safely
builder.Services.AddCors(opts => opts.AddPolicy("Portal", p => {
    p.WithOrigins("https://portal.mycorp.com")
     .AllowAnyMethod()
     .AllowAnyHeader()
     .AllowCredentials();
}));
```

**⚠️ Likely follow-up**
**Question:** Does CORS protect backend APIs from malicious curl or Postman requests?
**Answer:** No, CORS is enforced strictly by web browsers; non-browser tools like curl or Postman bypass CORS headers completely.

**📊 Quick comparison**
| Policy Setting | Origins Allowed | Credentials Allowed | Security Profile |
| :--- | :--- | :--- | :--- |
| AllowAnyOrigin | Any website (*) | No (Forbidden) | Public read-only APIs |
| Explicit Origins | Listed domains | Yes | Secure enterprise standard |

**🔬 Under the hood**
If the incoming request contains an Origin header, CorsMiddleware matches it against the configured policy. For preflight OPTIONS requests, it writes access headers and returns HTTP 204 No Content immediately.

---

## Q15: What is the difference between Eager Loading, Lazy Loading, and Explicit Loading in EF Core?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Eager loading (.Include)** means fetching related entities upfront in one query, avoiding the N+1 problem.

**🗣️ Spoken answer (30–45 seconds)**
**Eager loading** via `.Include` fetches parent and child records together in one SQL round-trip. **Lazy loading proxies** (Castle DynamicProxy wrappers) intercept navigation property reads and fire separate queries on access, risking the **N+1 problem**—one parent query followed by N child queries. When multiple collection includes cause row duplication, **.AsSplitQuery()** prevents **cartesian explosion** by splitting into separate coordinated SQL queries. In my project, eager loading with projection eliminated thousands of duplicate database queries.

**🎯 Terms the interviewer listens for**
- ⭐ **Eager loading (.Include)** — fetching related data upfront in one query
- ⭐ **N+1 problem** — one parent query followed by N child queries
- ⭐ **Cartesian explosion** — excessive row duplication from joining multiple collections
- **Lazy loading proxies** — runtime wrappers intercepting navigation reads
- **Explicit loading** — fetching related data manually via Entry().Load()
- **.AsSplitQuery()** — splitting multi-include into separate SQL queries

**🧠 Memory hook**
Eager loading is a full lunch platter served at once; lazy loading is a forgetful waiter making separate trips for every side dish.

**💻 Code**
```csharp
// ❌ Bad: lazy loading triggers N+1 queries
var users = await db.Users.ToListAsync();
foreach (var u in users) Console.WriteLine(u.Orders.Count);

// ✅ Good: eager loading in single SQL query
var safeUsers = await db.Users
    .Include(u => u.Orders)
    .AsNoTracking()
    .ToListAsync();
```

**⚠️ Likely follow-up**
**Question:** When should you use .AsSplitQuery() with eager loading?
**Answer:** Use .AsSplitQuery() when including multiple sibling collection navigations to avoid cartesian explosion and duplicate row transmission across the network.

**📊 Quick comparison**
| Strategy | Query Count | Memory Impact | Risk Factor |
| :--- | :--- | :--- | :--- |
| Eager Loading | One query (or split) | Low to moderate | Cartesian duplication |
| Lazy Loading | N+1 queries | Low initial, high later | Severe database load |
| Explicit Loading | On demand manual | Fully controlled | Manual code overhead |

**🔬 Under the hood**
Lazy loading replaces entity classes with dynamic runtime subclasses using Castle DynamicProxy. Overridden virtual navigation property getters invoke an injected ILazyLoader delegate, issuing a synchronous query if not already loaded.

---

## Q16: What is the difference between First, FirstOrDefault, Single, SingleOrDefault, and Find in EF Core?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Cardinality verification** means Single generates SELECT TOP 2 to enforce uniqueness, unlike First's TOP 1.

**🗣️ Spoken answer (30–45 seconds)**
First and FirstOrDefault generate SELECT TOP 1, returning the first match. Single and SingleOrDefault perform **cardinality verification** by generating **SELECT TOP(1) vs TOP(2)**, throwing if multiple matches exist. **First-level cache (Find)** is unique because it checks the local DbContext ChangeTracker by primary key before hitting the database. If the entity is already tracked, Find returns it with zero database round-trips. In my project, Find avoided redundant queries on frequently accessed lookup records.

**🎯 Terms the interviewer listens for**
- ⭐ **SELECT TOP(1) vs TOP(2)** — SQL limit for single fetch vs uniqueness check
- ⭐ **Cardinality verification** — enforcing that predicates match exactly one row
- ⭐ **First-level cache (Find)** — looking up entities in local DbContext memory
- **FirstOrDefault** — returns match or null without throwing
- **SingleOrDefault** — throws if more than one match exists
- **Primary key lookup** — fast index search by table primary key

**🧠 Memory hook**
First takes the first cab in line; Single checks if two cabs have identical license plates; Find checks your own pocket first.

**💻 Code**
```csharp
// ❌ Bad: SingleOrDefault throws if duplicates exist
var user = await db.Users.SingleOrDefaultAsync(u => u.City == "Delhi");

// ✅ Good: FirstOrDefault when only first record needed
var topUser = await db.Users.FirstOrDefaultAsync(u => u.City == "Delhi");

// ✅ Good: Find checks local memory cache first
var cached = await db.Users.FindAsync(userId);
```

**⚠️ Likely follow-up**
**Question:** Why does SingleOrDefault generate SELECT TOP 2 in SQL?
**Answer:** It requests two rows so that if a second row exists, EF Core detects the cardinality violation and throws an InvalidOperationException.

**📊 Quick comparison**
| Method | SQL Limit | Throws on Multiple? | Checks Local Cache? |
| :--- | :--- | :--- | :--- |
| First | TOP 1 | No | No |
| FirstOrDefault | TOP 1 | No | No |
| Single | TOP 2 | Yes | No |
| SingleOrDefault | TOP 2 | Yes | No |
| Find | TOP 1 (by PK) | No | Yes (Checks RAM first) |

**🔬 Under the hood**
DbSet.Find examines the ChangeTracker state manager entries for matching entity type and primary key values. If found, it returns the tracked instance immediately without establishing a database connection.

---

## Q17: What does AsNoTracking do in EF Core and when should you use it?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**ChangeTracker** is EF Core's engine monitoring entity modifications; AsNoTracking disables it for read-only query speed.

**🗣️ Spoken answer (30–45 seconds)**
By default, EF Core's **ChangeTracker** monitors every queried entity by performing **snapshot cloning**—copying property values into memory to detect future modifications. Calling **AsNoTracking** provides a major **read-only optimization**, disabling snapshot tracking and reducing heap allocations and GC pressure. Untracked entities cannot be persisted via SaveChangesAsync. In my project, applying AsNoTracking to read-only reporting endpoints reduced query latency and memory consumption by more than forty percent.

**🎯 Terms the interviewer listens for**
- ⭐ **ChangeTracker** — EF Core engine monitoring entity modifications and relationships
- ⭐ **Snapshot cloning** — in-memory copying of property values used for diffing
- ⭐ **Read-only optimization** — skipping tracking overhead for read-only query workloads
- **AsNoTracking** — query modifier disabling entity tracking
- **AsNoTrackingWithIdentityResolution** — avoids duplicate instances while omitting snapshot tracking overhead
- **Memory allocation reduction** — decreasing heap usage by eliminating tracking graph nodes

**🧠 Memory hook**
Tracked query is a hotel guest registering passport and card; AsNoTracking is buying a quick takeaway coffee with zero paperwork.

**💻 Code**
```csharp
// ❌ Bad: tracks 5,000 entities unnecessarily in RAM
var list = await db.Products.ToListAsync();

// ✅ Good: read-only query with zero tracking snapshots
var fastList = await db.Products
    .AsNoTracking()
    .ToListAsync();
```

**⚠️ Likely follow-up**
**Question:** What is the difference between AsNoTracking and AsNoTrackingWithIdentityResolution?
**Answer:** AsNoTrackingWithIdentityResolution ensures multiple occurrences of the same row share one object instance in memory without maintaining full change-tracking snapshots.

**📊 Quick comparison**
| Feature | Tracked Query | AsNoTracking |
| :--- | :--- | :--- |
| Snapshot Cloning | Yes (All properties) | No |
| Updates via SaveChanges | Supported automatically | Not tracked |
| Heap Memory Usage | High | Minimal |
| Best For | Edit, Delete, Update | GET endpoints and reports |

**🔬 Under the hood**
Tracked entities create an InternalEntityEntry binding to the StateManager. This entry holds original value buffers and relationship graph pointers. AsNoTracking bypasses entry creation, directly materializing the POCO object.

---

## Q18: Does async and await create a new background thread for I/O operations?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Non-blocking I/O** means async/await yields the thread instead of spawning a new one; IOCP delivers completion.

**🗣️ Spoken answer (30–45 seconds)**
Async and await do not spawn new threads for I/O. When an await hits pending I/O, the **IAsyncStateMachine** registers a continuation and executes **thread yielding**, returning the active thread to the pool. The operating system kernel handles the network transfer via **I/O Completion Ports (IOCP)**. When data arrives from the network, a **hardware interrupt** signals the kernel to post a work item, resuming on a free thread. In my project, async calls allowed our service to handle high concurrency without thread starvation.

**🎯 Terms the interviewer listens for**
- ⭐ **Thread yielding** — returning worker threads to the pool during I/O
- ⭐ **I/O Completion Ports (IOCP)** — OS notification mechanism for non-blocking I/O
- ⭐ **Hardware interrupt** — low-level signal notifying CPU that device data arrived
- **IAsyncStateMachine** — compiler struct managing states across suspensions
- **Non-blocking execution** — running without holding CPU threads idle
- **Throughput scalability** — processing concurrent requests with minimal threads

**🧠 Memory hook**
Ordering food at a counter: you take a token and sit down while the chef cooks; nobody stands frozen blocking the queue.

**💻 Code**
```csharp
// ❌ Bad: holds worker thread idle during I/O
var task = client.GetStringAsync(url);
var result = task.Result;

// ✅ Good: releases worker thread back to pool
var safeResult = await client.GetStringAsync(url);
return safeResult;
```

**⚠️ Likely follow-up**
**Question:** Does Task.Run also avoid creating threads?
**Answer:** No, Task.Run queues CPU-bound work onto a thread pool worker thread; it is meant for compute tasks, not I/O operations.

**📊 Quick comparison**
| Mechanism | Thread Count During I/O | CPU Core Usage | Best Target |
| :--- | :--- | :--- | :--- |
| Synchronous I/O | One blocked thread | Wasted waiting | Legacy console apps |
| Asynchronous I/O | Zero threads blocked | Zero CPU during wait | High-load Web APIs |
| Task.Run | One thread pool thread | Consumes CPU cycles | Heavy computation |

**🔬 Under the hood**
The device driver initiates direct memory access [DMA]. When the network card finishes receiving packets, it raises an interrupt service routine [ISR], prompting the Windows kernel to post an entry to the ThreadPool completion port.

---

## Q19: Why should you use SemaphoreSlim instead of lock in asynchronous C# code?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**SemaphoreSlim.WaitAsync** is an async-safe synchronization primitive, unlike lock which requires thread affinity (CS1996).

**🗣️ Spoken answer (30–45 seconds)**
The C# lock statement enforces **thread affinity** using Monitor.Enter—the same thread must enter and exit. Because await can resume on a different pool thread, using await inside lock triggers **compiler error CS1996**. **SemaphoreSlim.WaitAsync** acquires a synchronization slot asynchronously without blocking threads and can be released from any resuming thread in a finally block. In my project, SemaphoreSlim safely serialized token refresh calls across concurrent async requests.

**🎯 Terms the interviewer listens for**
- ⭐ **SemaphoreSlim.WaitAsync** — async-safe synchronization without blocking threads
- ⭐ **Thread affinity** — requirement that acquiring and releasing thread match
- ⭐ **Compiler error CS1996** — error when using await inside a lock block
- **Monitor.Enter / Exit** — CLR primitives underlying C# lock statements
- **Async-safe mutex** — single-slot semaphore with count one
- **try-finally release** — pattern guaranteeing semaphore release on faults

**🧠 Memory hook**
lock is a fingerprint lock requiring the same person to enter and leave; SemaphoreSlim is a shared key token hanging on the wall.

**💻 Code**
```csharp
// ❌ Bad: lock cannot contain await (CS1996)
// lock (_gate) { await FetchAsync(); }

// ✅ Good: async-safe synchronization via SemaphoreSlim
private readonly SemaphoreSlim _gate = new(1, 1);
public async Task SafeRun() {
    await _gate.WaitAsync();
    try { await FetchAsync(); }
    finally { _gate.Release(); }
}
```

**⚠️ Likely follow-up**
**Question:** What happens if you forget the finally block with SemaphoreSlim.Release()?
**Answer:** If an exception occurs, the semaphore is never released, causing all subsequent calls to wait indefinitely, resulting in a permanent application deadlock.

**📊 Quick comparison**
| Primitive | Async Await Safe | Thread Affinity | Blocking Behavior |
| :--- | :--- | :--- | :--- |
| lock(obj) | No (CS1996) | Enforced | Synchronous thread freeze |
| SemaphoreSlim | Yes (WaitAsync) | None | Asynchronous yielding |
| ReaderWriterLock | No | Enforced | Synchronous thread freeze |

**🔬 Under the hood**
SemaphoreSlim.WaitAsync returns a completed task if the count is above zero. If zero, it allocates a node in an internal queue and returns a Task, which completes when another thread calls Release().

---

## Q20: What is the difference between a Clustered Index and a Non-Clustered Index in SQL Server?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Clustered index** is a B-tree whose leaf nodes are the actual data pages, defining the table's physical row order.

**🗣️ Spoken answer (30–45 seconds)**
A **clustered index** is a B-tree whose leaf level contains the actual data pages, defining the table's physical row order—each table can have only one. A **non-clustered index** is a separate B-tree storing keys plus row locator pointers. When queries need unindexed columns, SQL Server performs expensive **key lookups** back to the base pages. Adding columns via INCLUDE creates a **covering index** that eliminates these lookups. In my project, covering indexes reduced query execution from seconds to milliseconds.

**🎯 Terms the interviewer listens for**
- ⭐ **Clustered index** — B-tree whose leaf level is the actual data pages
- ⭐ **Non-clustered index** — auxiliary B-tree storing keys plus row pointers
- ⭐ **Key lookup** — secondary lookup fetching unindexed columns from base pages
- **Covering index** — index containing all query columns via INCLUDE
- **B-tree leaf nodes** — bottom level storing data or pointers
- **Row locator** — pointer referencing data row via clustered key or RID

**🧠 Memory hook**
A clustered index is a phone directory sorted alphabetically; a non-clustered index is the back-of-book index pointing you to page numbers.

**💻 Code**
```sql
-- ❌ Bad: triggers expensive key lookups
CREATE NONCLUSTERED INDEX IX_Cust ON Orders(CustomerId);

-- ✅ Good: covering index eliminates key lookups
CREATE NONCLUSTERED INDEX IX_Cust_Cover ON Orders(CustomerId)
INCLUDE (OrderDate, TotalAmount);
```

**⚠️ Likely follow-up**
**Question:** Can a table have a Clustered Index without a Primary Key?
**Answer:** Yes, you can create a clustered index on any suitable column without defining a primary key, although primary keys default to clustered.

**📊 Quick comparison**
| Feature | Clustered Index | Non-Clustered Index |
| :--- | :--- | :--- |
| Count Per Table | Strictly one | Up to 999 |
| Leaf Level | Actual data pages | Pointers to rows |
| Physical Order | Dictates storage order | Independent of data |
| Default On | Primary Key | Unique constraint |

**🔬 Under the hood**
Clustered index leaf nodes are actual eight-kilobyte data pages linked in a doubly-linked list. Non-clustered leaf nodes store clustering key values for clustered tables, or eight-byte Row Identifiers [RID] for heap tables.

---

## Q21: How do you find the 2nd highest or Nth highest salary in SQL Server?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**DENSE_RANK()** is a window function assigning contiguous ranks without gaps, ideal for Nth-highest queries inside a CTE.

**🗣️ Spoken answer (30–45 seconds)**
**DENSE_RANK()** is a **window function** computing across related rows that assigns contiguous ranks without gaps on ties, unlike RANK(). Wrapping it inside a **Common Table Expression (CTE)**—a temporary named result set—allows filtering WHERE Rnk = N cleanly for any Nth highest salary. Subqueries handle second-highest but fail to generalize to arbitrary ranks. In my project, using DENSE_RANK inside a CTE solved compensation band reporting without missing tied salaries.

**🎯 Terms the interviewer listens for**
- ⭐ **DENSE_RANK()** — window function assigning contiguous ranks without skipping on ties
- ⭐ **Common Table Expression (CTE)** — temporary named result set within an executing query
- ⭐ **Window function** — computes across related rows using an OVER() clause
- **RANK()** — window function that skips ranks on ties
- **OFFSET-FETCH** — ANSI SQL pagination syntax for skipping rows
- **PARTITION BY** — restart ranking per group subset

**🧠 Memory hook**
Olympic medals: two runners tie for gold; DENSE_RANK awards silver next, whereas RANK skips silver and hands bronze.

**💻 Code**
```sql
-- ❌ Bad: RANK skips numbers on ties
-- SELECT Salary, RANK() OVER (ORDER BY Salary DESC)

-- ✅ Good: handles ties cleanly for Nth highest
WITH RankedSalaries AS (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rnk
    FROM Employees
)
SELECT DISTINCT Salary FROM RankedSalaries WHERE Rnk = 2;
```

**⚠️ Likely follow-up**
**Question:** Why is MAX subquery less desirable than DENSE_RANK for the 5th highest salary?
**Answer:** Finding the 5th highest salary with subqueries requires multiple deeply nested queries, whereas DENSE_RANK() simply filters by Rnk = 5 cleanly.

**📊 Quick comparison**
| Ranking Function | Behavior on Ties (100, 100, 90) | Generates Gaps | Generalizes to Nth |
| :--- | :--- | :--- | :--- |
| ROW_NUMBER() | 1, 2, 3 | Arbitrary assignment | No (Splits ties) |
| RANK() | 1, 1, 3 | Yes (Skips 2) | Unreliable on ties |
| DENSE_RANK() | 1, 1, 2 | No (Continuous) | Yes (Recommended) |

**🔬 Under the hood**
SQL Server evaluates window ranking functions during the SELECT logical query phase. The engine sorts rows via an in-memory segment operator, comparing adjacent values to increment the dense rank counter without disk spills.

---

## Q22: What is the difference between DELETE, TRUNCATE, and DROP in SQL Server?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Page extent deallocation** means TRUNCATE releases whole data pages with minimal logging, unlike row-by-row DELETE.

**🗣️ Spoken answer (30–45 seconds)**
DELETE is a DML command removing individual rows with full logging and trigger execution. TRUNCATE is a DDL command that performs **page extent deallocation**, releasing whole 8 KB data pages instead of logging each row, using **minimal logging** for speed. It also triggers an **identity seed reset** back to the initial value. Contrary to myth, TRUNCATE can be rolled back inside an active transaction. In my project, TRUNCATE emptied staging tables in milliseconds without log bloat.

**🎯 Terms the interviewer listens for**
- ⭐ **Page extent deallocation** — releasing whole data pages, not individual rows
- ⭐ **Minimal logging** — logging page allocation changes, not row data
- ⭐ **Identity seed reset** — resetting auto-increment counter to initial value
- **DML vs DDL** — data manipulation vs data definition language
- **Trigger execution** — automated procedure fired on row deletion
- **Active transaction rollback** — TRUNCATE can be rolled back in a transaction

**🧠 Memory hook**
DELETE is using a pencil eraser word by word; TRUNCATE unclips all pages from the binder; DROP throws the entire binder away.

**💻 Code**
```sql
-- ❌ Slow: logs every row deletion individually
DELETE FROM StagingData;

-- ✅ Fast: page deallocation with rollback support
BEGIN TRANSACTION;
TRUNCATE TABLE StagingData;
-- If needed, can safely roll back:
ROLLBACK TRANSACTION;
```

**⚠️ Likely follow-up**
**Question:** Why does TRUNCATE fail if another table has a Foreign Key pointing to it?
**Answer:** SQL Server blocks TRUNCATE on referenced tables even if the referencing table is empty, because page deallocation bypasses row-level foreign key validation checks.

**📊 Quick comparison**
| Property | DELETE | TRUNCATE | DROP |
| :--- | :--- | :--- | :--- |
| Command Type | DML | DDL | DDL |
| WHERE Clause | Supported | Not supported | Not supported |
| Logging Level | Full row-by-row | Minimal page logging | Minimal catalog |
| Identity Seed | Preserved | Reset to seed | Table removed |
| Fires Triggers | Yes | No | No |

**🔬 Under the hood**
TRUNCATE modifies page allocation maps [IAM and PFS pages] directly. It marks allocation extents as free in the system catalog, generating minimal log records compared to DELETE, which records every row before image.

---

## Q23: What is the difference between UNION and UNION ALL in SQL Server?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**UNION ALL** means concatenating result sets directly without the distinct-sort overhead that UNION adds.

**🗣️ Spoken answer (30–45 seconds)**
**UNION ALL** combines result sets directly without inspecting rows for duplicates, avoiding sorting overhead. In contrast, **UNION** introduces a **Distinct Sort** operator requiring an in-memory grant to eliminate duplicate rows. If memory is insufficient, the sort triggers a **TempDB spill**, writing intermediate runs to disk and multiplying latency. Default to UNION ALL unless deduplication is required. In my project, switching to UNION ALL on reporting views removed heavy query memory grants.

**🎯 Terms the interviewer listens for**
- ⭐ **UNION ALL** — concatenates multiple query result sets without removing duplicates
- ⭐ **Distinct Sort** — execution plan operator sorting rows to eliminate duplicates
- ⭐ **TempDB spill** — writing sort data to disk when memory grant exhausts
- **Memory grant** — memory allocated for sort and hash operations
- **Hash Aggregate** — alternative operator hashing rows to deduplicate
- **Set operator** — SQL operator combining rows from multiple queries

**🧠 Memory hook**
UNION ALL is stapling two papers together; UNION is checking every single line item with a marker to cross out duplicates.

**💻 Code**
```sql
-- ❌ Bad: distinct sort consumes unnecessary memory
SELECT City FROM RetailCustomers
UNION
SELECT City FROM CorporateCustomers;

-- ✅ Good: fast concatenation without sort overhead
SELECT City FROM RetailCustomers
UNION ALL
SELECT City FROM CorporateCustomers;
```

**⚠️ Likely follow-up**
**Question:** When is using UNION strictly necessary over UNION ALL?
**Answer:** Use UNION only when queries produce overlapping duplicate rows and the consumer or report explicitly requires distinct records.

**📊 Quick comparison**
| Operator | Duplicate Handling | Sort Overhead | Memory Grant |
| :--- | :--- | :--- | :--- |
| UNION | Removes duplicates | Distinct Sort or Hash | Required |
| UNION ALL | Preserves duplicates | Zero sorting overhead | None |

**🔬 Under the hood**
The query optimizer estimates distinct row cardinality. If the requested memory grant is insufficient for the Distinct Sort operation, the query spills intermediate sort runs to TempDB worktables, multiplying execution time.

---

## Q24: What is the difference between a Primary Key and a Unique Key constraint?
*Commonly asked at: TCS, Infosys, Cognizant, Accenture*

**⚡ One-line answer**
**Primary key constraint** is a non-nullable unique identifier defaulting to clustered; a Unique Key allows one NULL.

**🗣️ Spoken answer (30–45 seconds)**
A **primary key constraint** uniquely identifies each row, strictly rejects NULL values, and defaults to a clustered index—one per table. A **unique key constraint** also enforces uniqueness but follows the **single null rule** in SQL Server, permitting exactly one NULL value, and defaults to a non-clustered index. Tables can have multiple unique keys. In my project, unique keys enforced unique email addresses on optional user profiles while the primary key identified rows.

**🎯 Terms the interviewer listens for**
- ⭐ **Primary key constraint** — entity identifier disallowing nulls, defaults clustered
- ⭐ **Unique key constraint** — alternate key enforcing uniqueness, permits one null
- ⭐ **Single null rule** — SQL Server allows exactly one null in unique indexes
- **Clustered index default** — auto-created on primary key definition
- **Non-clustered index default** — auto-created on unique constraints
- **Entity integrity** — every table record must be identifiable

**🧠 Memory hook**
Primary key is an Aadhaar or Social Security number that everyone must have; Unique key is a passport number that remains optional.

**💻 Code**
```sql
-- ✅ Good: PK non-null, Unique allows null
CREATE TABLE Users (
    UserId INT IDENTITY(1,1) PRIMARY KEY,
    Email VARCHAR(150) NOT NULL UNIQUE,
    PassportNumber VARCHAR(20) NULL UNIQUE
);
-- ❌ Bad: second null in PassportNumber fails
-- INSERT INTO Users VALUES ('a@b.com', NULL);
-- INSERT INTO Users VALUES ('c@d.com', NULL);
```

**⚠️ Likely follow-up**
**Question:** How can you allow multiple NULL values in a unique column in SQL Server?
**Answer:** Create a Unique Filtered Index using WHERE ColumnName IS NOT NULL, allowing multiple null records while enforcing uniqueness on populated values.

**📊 Quick comparison**
| Characteristic | Primary Key | Unique Key |
| :--- | :--- | :--- |
| NULL Values | Strictly zero allowed | Exactly one allowed |
| Count Per Table | Maximum one | Multiple allowed |
| Default Index | Clustered index | Non-clustered index |
| Foreign Key Target | Standard target | Supported as target |

**🔬 Under the hood**
Under the hood, SQL Server enforces both constraints via unique indexes. A Primary Key sets the NOT NULL constraint in system metadata, whereas a Unique constraint creates an index with the UNIQUE flag enabled.

---

## Q25: What is the difference between a Stored Procedure and a User-Defined Function (UDF)?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Stored procedure** is a precompiled routine executing DML and transactions; a UDF is side-effect-free and composable in queries.

**🗣️ Spoken answer (30–45 seconds)**
**Stored procedures** execute procedural logic, perform DML modifications, and manage database transactions, but cannot be embedded inside SELECT or WHERE clauses. A **User-Defined Function (UDF)** computes calculations without side-effects and embeds directly into queries. Scalar UDFs often trigger **RBAR** (row-by-agonizing-row) execution penalties. An **Inline Table-Valued Function (iTVF)** is a parameterized view that the optimizer expands directly into the calling query plan, avoiding RBAR. In my project, replacing scalar UDFs with iTVFs improved report speed dramatically.

**🎯 Terms the interviewer listens for**
- ⭐ **Stored procedure** — precompiled routine executing DML and transactions
- ⭐ **Inline Table-Valued Function (iTVF)** — parameterized view inlined into query plans
- ⭐ **RBAR** — row-by-agonizing-row execution penalty in scalar functions
- **User-Defined Function (UDF)** — side-effect-free routine returning values
- **Side-effect prohibition** — rule preventing functions from modifying data
- **Transaction management** — controlling BEGIN, COMMIT, ROLLBACK boundaries

**🧠 Memory hook**
A stored procedure is a factory assembly robot modifying parts; a function is a desk calculator giving an answer without touching inventory.

**💻 Code**
```sql
-- ❌ Bad: scalar UDF causes RBAR execution
-- SELECT Id, dbo.fn_CalcTax(Salary) FROM Employees;

-- ✅ Good: inline TVF expands into query plan
CREATE FUNCTION dbo.fn_GetDeptEmps(@DeptId INT)
RETURNS TABLE AS RETURN (
    SELECT Id, Name, Salary FROM Employees WHERE DeptId = @DeptId
);
```

**⚠️ Likely follow-up**
**Question:** Why are Inline Table-Valued Functions faster than Multi-Statement Table-Valued Functions?
**Answer:** Inline TVFs treat the query as a macro, folding it into the outer query plan, whereas multi-statement TVFs populate physical TempDB table variables.

**📊 Quick comparison**
| Capability | Stored Procedure | User-Defined Function |
| :--- | :--- | :--- |
| Can Modify Data (DML) | Yes | Strictly prohibited |
| Usable Inside SELECT | No | Yes |
| Transaction Control | Yes (BEGIN TRAN) | No |
| Return Types | Zero, scalar, or sets | Scalar or table |

**🔬 Under the hood**
Scalar UDFs invoke the expression evaluator once per processed row, switching contexts between the relational engine and the T-SQL interpreter. SQL Server 2019 introduced Scalar UDF Inlining to mitigate this penalty automatically.

---

## Q26: How do you explain ACID properties with a real-world banking scenario?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Atomicity** means all operations succeed or all roll back; ACID also guarantees consistency, isolation, and durability.

**🗣️ Spoken answer (30–45 seconds)**
**Atomicity** ensures that debiting Account A and crediting Account B succeed together or roll back completely—no partial state. **Consistency** enforces schema rules like non-negative balance constraints. **Isolation** prevents concurrent users from seeing intermediate balances during execution. Durability flushes committed changes via the **write-ahead log** (WAL) to disk before data pages update. In my project, explicit transaction scopes guaranteed zero discrepancies during payment gateway callbacks.

**🎯 Terms the interviewer listens for**
- ⭐ **Atomicity** — all operations succeed or all roll back completely
- ⭐ **Isolation** — concurrency barrier hiding uncommitted transaction state
- ⭐ **Write-ahead log (WAL)** — logging to disk before data page updates
- **Consistency** — invariant enforcement adhering to schema rules
- **Durability** — committed data survives power failures and crashes
- **Transaction rollback** — reversing uncommitted operations to consistent state

**🧠 Memory hook**
ATM withdrawal: cash dispensed and account debited together; if cash jams, your balance is fully restored with zero phantom deductions.

**💻 Code**
```sql
-- ❌ Bad: no transaction rollback on failure
UPDATE Accounts SET Balance = Balance - 500 WHERE Id = 101;
UPDATE Accounts SET Balance = Balance + 500 WHERE Id = 202;

-- ✅ Good: atomic transaction with rollback
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE Accounts SET Balance = Balance - 500 WHERE Id = 101 AND Balance >= 500;
    UPDATE Accounts SET Balance = Balance + 500 WHERE Id = 202;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    THROW;
END CATCH;
```

**⚠️ Likely follow-up**
**Question:** How does Write-Ahead Logging guarantee durability during an abrupt power failure?
**Answer:** SQL Server flushes transaction log records to disk before modifying data pages in memory, allowing recovery processes to replay committed transactions upon restart.

**📊 Quick comparison**
| Property | Core Guarantee | Failure Consequence | Mechanism Used |
| :--- | :--- | :--- | :--- |
| Atomicity | All or nothing | Full rollback | Transaction log undo |
| Consistency | Valid schema rules | Aborts transaction | Constraints and keys |
| Isolation | Hidden in-flight state | Concurrency locks | Locks or snapshot |
| Durability | Committed data persists | Survives crashes | Write-ahead logging |

**🔬 Under the hood**
SQL Server enforces durability via the Write-Ahead Logging [WAL] protocol. During COMMIT, the log manager writes log records synchronously to disk (LDF), while dirty data pages in the buffer pool are flushed asynchronously later by the checkpoint process.

---
