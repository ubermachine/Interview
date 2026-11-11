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
The automatic memory manager [Garbage Collector] groups objects into generations zero, one, two, and the large object heap based on expected lifetime.

**🗣️ Spoken answer (30–45 seconds)**
The automatic memory manager [Garbage Collector] organizes the heap into generations zero, one, and two, plus the large object heap. Most temporary objects die in generation zero shortly after allocation. Surviving objects advance to generation one, and long-lived singletons move to generation two. Objects eighty-five thousand bytes or larger land on the large object heap directly. In one of my projects, avoiding large buffer allocations prevented expensive pause times [Stop-The-World GC] and memory fragmentation.

**🎯 Terms the interviewer listens for**
- ⭐ **Generational hypothesis**: Most objects die very shortly after allocation.
- ⭐ **Ephemeral generations**: Generations zero and one collected during short pauses.
- ⭐ **Large Object Heap [LOH]**: Separate heap for objects eighty-five thousand bytes or larger.
- **Stop-the-world pause**: Freezing application threads while collecting memory.
- **Mark-sweep-compact**: Algorithm identifying live objects and defragmenting heap space.
- **Finalization queue**: Internal list tracking objects awaiting finalizer execution.

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
Workstation GC optimizes for UI responsiveness on a single thread, whereas Server GC optimizes for throughput using dedicated threads per CPU core.

**🗣️ Spoken answer (30–45 seconds)**
Workstation mode minimizes UI latency, while server mode maximizes throughput across multiple cores. Workstation GC runs on one background thread sharing CPU with application logic. Server GC creates a dedicated managed heap and thread per logical processor. ASP.NET Core enables server mode by default to scale with high concurrent traffic. In one of my projects, tuning server GC prevented request queuing during traffic spikes.

**🎯 Terms the interviewer listens for**
- ⭐ **Server GC**: One managed heap and thread per CPU core.
- ⭐ **Workstation GC**: Single heap optimizing for responsive client desktop apps.
- ⭐ **Concurrent GC**: Collecting memory concurrently without stopping all worker threads.
- **Throughput**: Total requests processed over a sustained time window.
- **Thread affinity**: Binding worker threads to dedicated processor cores.
- **Background GC**: Collecting ephemeral generations while user threads continue running.

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
Dispose provides immediate deterministic cleanup invoked by application code, while Finalize is an unpredictable fallback run by the runtime finalizer thread.

**🗣️ Spoken answer (30–45 seconds)**
Dispose provides immediate deterministic cleanup, while Finalize is an emergency runtime fallback. Calling `Dispose` releases unmanaged operating system resources like file handles immediately. Finalizers run unpredictably on a single background thread when garbage collection sweeps. Relying on finalizers delays memory reclamation and promotes objects into generation two. In one of my projects, calling `GC.SuppressFinalize` inside `Dispose` prevented unnecessary GC promotion.

**🎯 Terms the interviewer listens for**
- ⭐ **Deterministic cleanup**: Freeing resources immediately at a known program location.
- ⭐ **Finalizer [~ClassName]**: Runtime fallback method called before memory collection.
- ⭐ **GC.SuppressFinalize**: Instructs the runtime to skip finalization queue execution.
- **Unmanaged resources**: Operating system handles, sockets, and native memory.
- **using statement**: Language shortcut translating to a try-finally disposal block.
- **Finalization queue**: Internal list tracking objects with pending finalizer execution.

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
The compiler transforms asynchronous methods into a state machine struct, releasing the current thread to the thread pool while awaiting I/O completion.

**🗣️ Spoken answer (30–45 seconds)**
Asynchronous methods do not create new threads for network or file I/O. The compiler rewrites the method into a state machine [IAsyncStateMachine]. When hitting an `await`, the current thread returns to the thread pool. Operating system completion ports [IOCP] notify the runtime when data arrives. In one of my projects, async code allowed twenty web threads to serve ten thousand concurrent users.

**🎯 Terms the interviewer listens for**
- ⭐ **IAsyncStateMachine**: Compiler-generated struct tracking execution progress across suspension points.
- ⭐ **I/O Completion Ports [IOCP]**: Operating system notification mechanism for non-blocking I/O.
- ⭐ **Thread yielding**: Returning worker threads to the pool during pause.
- **Continuation callback**: Delegate invoked when an awaited asynchronous operation finishes.
- **TaskCompletionSource**: Mechanism to create tasks completing on external events.
- **Synchronization context**: Legacy component absent in ASP.NET Core web runtimes.

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
ValueTask is a value type struct that avoids allocating a Task when the result is already available, such as on a cache hit.

**🗣️ Spoken answer (30–45 seconds)**
ValueTask is a struct that avoids allocating a Task when the result is already available. Task is a reference type that always allocates an object on the managed heap. When operations frequently complete synchronously, ValueTask eliminates garbage collection allocation pressure. If the operation must perform real asynchronous I/O, it wraps a normal Task fallback. In one of my projects, returning ValueTask in a memory cache dropped Gen 0 collections significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **ValueTask<T>**: Stack-allocated struct avoiding reference heap allocations for completions.
- ⭐ **Synchronous completion**: Returning a cached or precomputed result without suspension.
- ⭐ **GC Gen 0 pressure**: Overhead caused by rapidly allocating short-lived heap objects.
- **Heap allocation**: Reserving dynamic memory managed by garbage collection.
- **IValueTaskSource**: Advanced interface allowing reusable custom ValueTask backings.
- **Single-await constraint**: Rule prohibiting awaiting a ValueTask instance multiple times.

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
Sync-over-async blocks thread pool threads waiting on asynchronous tasks, starving incoming requests because the thread pool injects new worker threads slowly.

**🗣️ Spoken answer (30–45 seconds)**
Sync-over-async occurs when synchronous code calls `.Result` or `.Wait()` on asynchronous methods. This holds the current thread pool worker hostage while waiting for a completion callback. Under high load, all threads become blocked and new incoming HTTP requests queue up. The .NET thread pool injects new threads slowly at roughly one thread every five hundred milliseconds. In one of my projects, removing `.GetAwaiter().GetResult()` dropped p99 API latency instantly.

**🎯 Terms the interviewer listens for**
- ⭐ **Sync-over-async**: Anti-pattern of blocking synchronously on asynchronous operations.
- ⭐ **ThreadPool starvation**: Depletion of worker threads causing queued pending work items.
- ⭐ **Thread injection rate**: Throttled pace at which runtime spawns new worker threads.
- **Hill-climbing algorithm**: Heuristic engine dynamically sizing the thread pool.
- **Work-stealing queue**: Thread-local queues allowing idle threads to take pending tasks.
- **Deadlock risk**: Cyclic waiting condition when continuation requires the blocked thread.

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
The pipeline executes a chain of RequestDelegate components sequentially, letting each component process the request on entry and response on return.

**🗣️ Spoken answer (30–45 seconds)**
The pipeline executes a chain of RequestDelegate delegates wrapped around HttpContext. `RequestDelegate` is defined as `Func<HttpContext, Task>`. Each middleware runs outside MVC and can process requests before calling `await next()`. Registered before `UseRouting` it cannot see the endpoint; after it, it can. It never sees action arguments or ModelState, which belong strictly to MVC filters. In one of my projects, placing authentication middleware after routing enabled endpoint-aware authorization checks.

**🎯 Terms the interviewer listens for**
- ⭐ **RequestDelegate**: Delegate matching Func<HttpContext, Task> processing web requests.
- ⭐ **Bidirectional pipeline**: Processing request on incoming journey and response on outgoing.
- ⭐ **Endpoint routing boundary**: Separation between raw HTTP middleware and endpoint metadata.
- **app.Use**: Chaining middleware component with downstream next delegate invocation.
- **app.Run**: Terminal middleware terminating pipeline execution without calling next.
- **app.Map**: Branching pipeline execution based on request URL path matching.

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
ASP.NET Core provides transient, scoped, and singleton lifetimes, while captive dependencies occur when a longer-lived service traps a shorter-lived dependency.

**🗣️ Spoken answer (30–45 seconds)**
ASP.NET Core dependency injection manages transient, scoped, and singleton service lifetimes. Transient provides new instances every time, while scoped creates one instance per HTTP request. Singleton maintains a single instance across the entire application lifetime. A captive dependency happens when a singleton service injects a scoped service directly. In one of my projects, resolving scoped dependencies via `IServiceScopeFactory` prevented DbContext concurrency crashes.

**🎯 Terms the interviewer listens for**
- ⭐ **Captive dependency**: Bug where longer-lived service holds shorter-lived service in memory.
- ⭐ **IServiceScopeFactory**: Factory interface used to create manual child request scopes.
- ⭐ **Scoped lifetime**: Single instance shared across a single logical HTTP request.
- **Transient lifetime**: New service instance allocated on every injection request.
- **Singleton lifetime**: Single instance created once and shared application-wide.
- **ValidateScopes**: DI container configuration setting catching captive dependencies at startup.

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
IHttpClientFactory pools underlying message handlers to prevent socket exhaustion while rotating them every two minutes to respect DNS updates.

**🗣️ Spoken answer (30–45 seconds)**
Creating new HttpClient instances manually causes TCP socket exhaustion in TIME_WAIT state. Conversely, keeping a static HttpClient instance ignores domain name [DNS] changes indefinitely. `IHttpClientFactory` solves both problems by pooling underlying socket handlers [HttpMessageHandler]. It rotates handlers every two minutes by default, refreshing DNS without dropping active connections. In one of my projects, typed clients eliminated outgoing connection errors during cloud migrations.

**🎯 Terms the interviewer listens for**
- ⭐ **IHttpClientFactory**: Factory managing lifecycle and pooling of underlying HTTP handlers.
- ⭐ **Socket exhaustion**: Depletion of available TCP client ports trapped in TIME_WAIT.
- ⭐ **DNS rotation**: Periodic handler expiration honoring updated IP address records.
- **HttpMessageHandler**: Low-level runtime component managing raw HTTP socket connections.
- **Typed client**: Strongly-typed service class injecting an configured HttpClient instance.
- **Two-minute lifetime**: Default rotation period for pooled HTTP handler connections.

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
SOLID represents five object-oriented design principles that isolate changes, reduce code coupling, and ensure software maintainability across evolving enterprise applications.

**🗣️ Spoken answer (30–45 seconds)**
SOLID provides five architectural guardrails preventing code rot in evolving enterprise applications. Single responsibility keeps classes focused on one distinct business task alone. Open-closed and Liskov substitution rely on polymorphic interfaces to extend features safely without breaking caller expectations. Interface segregation splits fat contracts into role-based interfaces. Dependency inversion decouples high-level business services from concrete data access implementations. In one of my projects, abstracting payment gateways allowed adding providers without altering checkout code.

**🎯 Terms the interviewer listens for**
- ⭐ **Single Responsibility**: Class should have only one reason to change.
- ⭐ **Open/Closed Principle**: Open for extension but closed for modification.
- ⭐ **Dependency Inversion**: High-level modules depend on abstractions, not concrete classes.
- **Liskov Substitution**: Derived types must substitute base types without breaking code.
- **Interface Segregation**: Clients should not implement methods they do not need.
- **High cohesion**: Keeping related business logic grouped tightly inside one class.

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
IQueryable executes expression trees remotely on the database, IEnumerable filters in memory, ICollection adds mutation, and IList provides indexed positional access.

**🗣️ Spoken answer (30–45 seconds)**
The key distinction is execution boundary and collection capability. `IQueryable` translates expression trees into database queries [SQL] for server-side evaluation. `IEnumerable` streams records in memory; you can enumerate it many times, but each pass is forward-only, no indexing. `ICollection` adds element count and mutation methods like add and remove. `IList` extends collection with zero-based index access. In one of my projects, returning `IQueryable` instead of `IEnumerable` stopped loading thousands of rows into server RAM.

**🎯 Terms the interviewer listens for**
- ⭐ **IQueryable<T>**: Provider-based query compiling expression trees into native SQL.
- ⭐ **IEnumerable<T>**: Forward-only in-memory sequence supporting multiple deferred iterations.
- ⭐ **Expression tree**: Data structure representing code logic as syntax nodes.
- **ICollection<T>**: Collection contract adding element count and mutation methods.
- **IList<T>**: Indexable collection providing random position access and removal.
- **Deferred execution**: Delaying query evaluation until enumerated via foreach or ToList.

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
String is an immutable reference type where every modification allocates new memory, whereas StringBuilder modifies an internal buffer in place.

**🗣️ Spoken answer (30–45 seconds)**
Strings in C# cannot be modified after instantiation [String Immutability]. Every concatenation allocates a brand-new string object on the managed heap. `StringBuilder` maintains a growable internal buffer of characters instead. It mutates memory in place, doubling buffer capacity only when filled. You should use `StringBuilder` inside loops or when concatenating text dynamically. In one of my projects, replacing string concatenation in a CSV loop reduced Gen 0 pauses significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **String immutability**: Inability to modify text characters after object creation.
- ⭐ **StringBuilder**: Mutable character buffer dynamically resizing without intermediate allocations.
- ⭐ **String interning**: CLR pool sharing single heap instances for identical literals.
- **Gen 0 pressure**: Garbage collection overhead caused by rapid short-lived allocations.
- **Buffer doubling**: Capacity growth algorithm resizing array when capacity fills up.
- **Heap allocation**: Memory assigned dynamically to reference type instances.

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
Ref enables two-way parameter passing, out enforces caller output assignment, in passes readonly references, and params accepts variable argument counts.

**🗣️ Spoken answer (30–45 seconds)**
These keywords modify how arguments pass into C# methods. `ref` passes a variable by reference and requires caller initialization beforehand. `out` passes by reference and requires the called method to assign a value before returning. `in` passes value types by readonly reference, avoiding expensive memory copies of large structs. `params` allows callers to pass a variable list of arguments packed into an array. In one of my projects, using `in` for coordinate structs increased mathematical calculation performance.

**🎯 Terms the interviewer listens for**
- ⭐ **ref keyword**: Passes argument by reference for two-way reading and writing.
- ⭐ **out parameter**: Enforces mandatory callee assignment before method completion.
- ⭐ **in parameter**: Passes reference as readonly to eliminate struct copying overhead.
- **params keyword**: Accepts variable number of comma-separated arguments as array.
- **Definite assignment**: Compiler guarantee that variables contain values before reading.
- **Managed pointer**: Pointer to managed memory verified by runtime type safety.

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
Throw preserves the original stack trace, throw ex wipes previous stack frames, and wrapping with custom exceptions preserves root causes in InnerException.

**🗣️ Spoken answer (30–45 seconds)**
How you rethrow exceptions determines whether production bugs can be debugged. Using bare `throw` preserves the entire original call stack and line numbers. Using `throw ex` resets the stack trace to the catch block, destroying origin information. Wrapping with custom exceptions encapsulates errors while preserving original diagnostics in `InnerException`. In one of my projects, eliminating `throw ex` reduced production incident investigation time significantly.

**🎯 Terms the interviewer listens for**
- ⭐ **Stack trace preservation**: Retaining original method call history and line numbers.
- ⭐ **throw statement**: Rethrows current active exception preserving complete diagnostic trace.
- ⭐ **throw ex bug**: Anti-pattern resetting stack origin to current catch block.
- **InnerException**: Property linking previous failure causes inside wrapped custom exceptions.
- **Stack unwinding**: Process of freeing call frames during exception bubbling.
- **Exception shielding**: Preventing internal implementation leaks to external API clients.

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
Interfaces define behavioral contracts with multiple implementation support, while abstract classes provide shared identity, internal state, and protected member access.

**🗣️ Spoken answer (30–45 seconds)**
Interfaces define what a class can do, while abstract classes define what a class is. Interfaces support multiple implementation and are ideal for dependency injection and mocking. Abstract classes allow single inheritance but can hold instance state, fields, and constructors. Even with C# 8 default methods, interfaces cannot declare instance fields or state. In one of my projects, abstract base repositories shared audit fields, while interfaces exposed public contracts.

**🎯 Terms the interviewer listens for**
- ⭐ **Interface contract**: Pure behavioral specification without instance fields or state.
- ⭐ **Abstract class**: Base class sharing code and instance state via inheritance.
- ⭐ **Default interface methods**: Interface method implementations added for backward library compatibility.
- **Multiple implementation**: Implementing several interface contracts within one class.
- **Single inheritance**: Language rule restricting classes to exactly one base class.
- **Virtual method table [vtable]**: Memory table used by runtime for dynamic dispatch.

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
Boxing wraps a value type into a heap object header, while unboxing extracts the raw value back to the stack.

**🗣️ Spoken answer (30–45 seconds)**
Boxing converts a value type on the stack into an object on the managed heap. The runtime allocates memory and copies the raw bits into a new object container. Unboxing verifies the type pointer and copies the bits back onto the stack. Continuous boxing in high-traffic loops creates short-lived heap allocations, triggering frequent garbage collection pauses. In one of my projects, replacing `ArrayList` with generic `List<int>` eliminated millions of allocations.

**🎯 Terms the interviewer listens for**
- ⭐ **Boxing**: Converting stack value type into heap-allocated reference object.
- ⭐ **Unboxing**: Explicitly casting boxed object back into stack value type.
- ⭐ **Object header**: Sixteen-byte overhead containing method table and synchronization block index.
- **Generics [List<T>]**: Parameterized collections eliminating boxing conversions at compile time.
- **Type safety check**: Runtime verification ensuring boxed type matches unboxing cast.
- **GC Gen 0 churn**: Excessive allocation of short-lived objects triggering garbage collection.

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
Overloading resolves multiple signatures at compile time, overriding resolves virtual methods dynamically at runtime, and shadowing hides base methods without polymorphism.

**🗣️ Spoken answer (30–45 seconds)**
These three mechanisms represent different polymorphism approaches in C#. Overloading defines multiple methods with identical names but distinct parameter signatures at compile time. Overriding provides runtime polymorphism, dispatching calls dynamically through the virtual method table [vtable]. Shadowing uses the `new` keyword to hide base members without virtual dispatch. When called through a base reference, a shadowed method executes base logic instead. In one of my projects, accidental shadowing caused subtle accounting calculation bugs.

**🎯 Terms the interviewer listens for**
- ⭐ **Method overloading**: Same method name with distinct parameter signatures at compile-time.
- ⭐ **Method overriding**: Runtime polymorphism substituting virtual base methods via vtable dispatch.
- ⭐ **Method shadowing [new]**: Hiding base class methods without participating in virtual dispatch.
- **Virtual Method Table [vtable]**: Internal lookup table resolving dynamic method addresses at runtime.
- **Early binding**: Resolving method invocation targets during compilation phase.
- **Dynamic dispatch**: Runtime resolution selecting implementation based on concrete object type.

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
Const is inlined at compile time, readonly is set per instance at runtime, and static readonly is initialized once per process when first used.

**🗣️ Spoken answer (30–45 seconds)**
The key distinction is when values evaluate and how long they persist. `const` values are inlined directly into calling Intermediate Language at compile time. Instance `readonly` fields are set during declaration or inside constructor execution. `static readonly` fields are initialized once per process, when the type is first used. Updating a `const` in a shared library requires recompiling all consumer libraries. In one of my projects, switching from `const` to `static readonly` eliminated multi-library deployment mismatches.

**🎯 Terms the interviewer listens for**
- ⭐ **const literal**: Compile-time constant inlined directly into calling assembly bytecode.
- ⭐ **readonly field**: Instance variable assignable only at declaration or in constructors.
- ⭐ **static readonly**: Runtime value initialized once per process on type initialization.
- **Compile-time inlining**: Embedding literal values directly into referencing calling assemblies.
- **Static constructor [.cctor]**: Special class constructor running once when type first loads.
- **Assembly versioning trap**: Bug when updated constants are not recompiled in consumers.

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
Lifetimes dictate instance persistence, while captive dependencies happen when a long-lived service holds a shorter-lived service, causing memory leaks and thread crashes.

**🗣️ Spoken answer (30–45 seconds)**
ASP.NET Core supports transient, scoped, and singleton service lifetimes. Transient creates fresh instances on every injection, while scoped creates one instance per HTTP request. Singleton maintains one instance across the entire application lifecycle. A captive dependency occurs when a singleton service injects a scoped dependency like a database context. This traps the scoped dependency forever, causing memory leaks and multithreaded database crashes. In one of my projects, using `IServiceScopeFactory` resolved scoped services inside background singletons safely.

**🎯 Terms the interviewer listens for**
- ⭐ **Transient lifetime**: New service instance allocated on every injection call.
- ⭐ **Scoped lifetime**: Single instance created per incoming HTTP request boundary.
- ⭐ **Captive dependency**: Long-lived service trapping shorter-lived dependency in memory.
- **Singleton lifetime**: Single instance created once and shared application wide.
- **IServiceScopeFactory**: Factory interface used to spawn manual child scopes safely.
- **Root container**: Top-level DI container holding application singletons and registrations.

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
Middleware operates globally on raw HttpContext in the outer pipeline, while Action Filters execute inside MVC with access to action arguments and ModelState.

**🗣️ Spoken answer (30–45 seconds)**
The architectural boundary between them is pipeline scope and MVC awareness. Middleware represents a `RequestDelegate` [`Func<HttpContext, Task>`] running outside MVC. Registered before `UseRouting` it cannot see the endpoint; after it, it can. It never sees action arguments or ModelState. Action filters run inside MVC after routing, accessing controller metadata, parameters, and results. In one of my projects, moving authorization from filters into middleware protected static files and endpoints uniformly.

**🎯 Terms the interviewer listens for**
- ⭐ **RequestDelegate**: Delegate matching Func<HttpContext, Task> processing web requests.
- ⭐ **Action filter**: MVC pipeline component inspecting action arguments and model state.
- ⭐ **Endpoint routing boundary**: Pipeline transition separating raw HTTP from endpoint selection.
- **HttpContext**: Raw HTTP request and response encapsulation object.
- **ActionExecutingContext**: Filter context granting access to parameters and controller metadata.
- **Short-circuiting**: Terminating request processing early without calling downstream delegates.

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
Global exception middleware wraps downstream execution in try-catch, mapping unhandled errors into standardized RFC 7807 ProblemDetails JSON responses without leaking stack traces.

**🗣️ Spoken answer (30–45 seconds)**
Global exception handling middleware wraps the entire request pipeline in centralized error handling. When downstream components throw unhandled exceptions, the middleware intercepts them cleanly. It logs diagnostic details using the request correlation identifier [`TraceIdentifier`]. It maps exception types to appropriate HTTP status codes, such as NotFound for missing keys. Then it serializes an RFC 7807 ProblemDetails JSON payload back to the client. In one of my projects, this prevented exposing internal SQL stack traces to public callers.

**🎯 Terms the interviewer listens for**
- ⭐ **ProblemDetails [RFC 7807]**: Standardized machine-readable specification for HTTP error responses.
- ⭐ **TraceIdentifier**: Unique correlation identifier tracking requests across log messages.
- ⭐ **Information disclosure**: Security vulnerability leaking raw stack traces to callers.
- **Global exception middleware**: Outer pipeline component catching all downstream unhandled errors.
- **Response.HasStarted**: Boolean guard checking if response headers were already sent.
- **Status code mapping**: Translating domain exception types into standard HTTP codes.

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
JWT is a stateless signed token consisting of header, payload, and signature, validated by middleware to populate HttpContext.User with claims.

**🗣️ Spoken answer (30–45 seconds)**
JSON Web Tokens provide stateless authentication split into header, payload, and signature. The client sends the bearer token in the HTTP Authorization request header. Authentication middleware validates the signature, issuer, audience, and expiration date using secret keys. Once validated, the runtime unpacks claims into a ClaimsPrincipal on `HttpContext.User`. By default, token validation permits five minutes of clock skew tolerance. In one of my projects, setting clock skew to zero prevented expired token acceptance.

**🎯 Terms the interviewer listens for**
- ⭐ **ClaimsPrincipal**: Identity object on HttpContext containing user claims and roles.
- ⭐ **ClockSkew**: Time drift tolerance defaulting to five minutes in ASP.NET Core.
- ⭐ **Bearer token**: Cryptographic token proving identity via possession in authorization header.
- **Symmetric security key**: Shared secret key used to sign and verify HMAC signatures.
- **Token validation parameters**: Configuration settings specifying signature, audience, and lifetime rules.
- **Stateless authentication**: Verifying requests without storing session records in server memory.

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
CORS is a browser security mechanism enforcing cross-origin access rules via preflight OPTIONS requests, configured using named policies in ASP.NET Core.

**🗣️ Spoken answer (30–45 seconds)**
CORS is a browser-enforced security check, not a server firewall. Browsers send an HTTP OPTIONS preflight request before making cross-domain AJAX calls. The server responds with allowed origins, headers, and HTTP methods. In ASP.NET Core, `app.UseCors` must sit between `UseRouting` and `UseAuthentication`. The CORS specification strictly forbids combining wildcard origins with credential sharing. In one of my projects, specifying explicit client domains prevented cross-site scripting exposure.

**🎯 Terms the interviewer listens for**
- ⭐ **Same-Origin Policy [SOP]**: Browser rule restricting scripts from accessing distinct domain resources.
- ⭐ **Preflight OPTIONS**: Preliminary handshake checking permitted HTTP methods and request headers.
- ⭐ **Access-Control-Allow-Origin**: Response header indicating which client origins may read data.
- **AllowCredentials**: Policy setting permitting cookies and authorization headers in requests.
- **Middleware ordering**: Positioning UseCors between UseRouting and UseAuthentication correctly.
- **Wildcard prohibition**: Specification rule blocking AllowAnyOrigin combined with credential flags.

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
Eager loading fetches related entities upfront via joins, lazy loading loads navigation properties on first access, and explicit loading fetches them manually on demand.

**🗣️ Spoken answer (30–45 seconds)**
These loading strategies control when and how Entity Framework fetches related child entities. Eager loading uses `.Include` to query parent and child records together in one round-trip. Lazy loading uses runtime-generated proxies [`Castle DynamicProxy`], instead of bytecode modification, fetching on property access. However, looping over lazy properties causes the N+1 query problem. `.AsSplitQuery()` avoids cartesian explosion across multiple collection includes. In one of my projects, eager loading with projection eliminated thousands of duplicate database queries.

**🎯 Terms the interviewer listens for**
- ⭐ **Eager loading [.Include]**: Fetching related data upfront within the primary database query.
- ⭐ **Lazy loading proxies**: Runtime Castle DynamicProxy wrappers intercepting navigation property reads.
- ⭐ **Cartesian explosion**: Excessive row duplication caused by joining multiple child collections.
- **N+1 query problem**: Firing one parent query followed by N child queries.
- **Explicit loading**: Fetching related data manually via Entry().Collection().Load().
- **.AsSplitQuery()**: Splitting multi-include queries into separate coordinated SQL queries.

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
First returns the first match, Single validates uniqueness by querying TOP 2, and Find checks local DbContext cache before querying by primary key.

**🗣️ Spoken answer (30–45 seconds)**
These methods differ in query generation, cardinality verification, and cache behavior. `First` and `FirstOrDefault` generate a `SELECT TOP 1` query, returning null or throwing if empty. `Single` and `SingleOrDefault` generate `SELECT TOP 2`, throwing an exception if multiple matches exist. `Find` is unique because it searches by primary key, checking local memory before querying SQL. If the entity is already tracked, `Find` returns it with zero database round-trips. In one of my projects, `Find` avoided redundant queries on frequently accessed records.

**🎯 Terms the interviewer listens for**
- ⭐ **SELECT TOP(1) vs TOP(2)**: SQL limit generated to fetch single record or verify uniqueness.
- ⭐ **Cardinality verification**: Enforcing that query predicates match exactly one database row.
- ⭐ **First-level cache [Find]**: Looking up entities tracked in local DbContext memory first.
- **FirstOrDefault**: Returns matching entity or default null value without throwing.
- **SingleOrDefault**: Throws InvalidOperationException if more than one match exists.
- **Primary key lookup**: Fast index search based strictly on table primary key.

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
AsNoTracking disables ChangeTracker snapshot cloning, speeding up read-only queries and reducing memory consumption by avoiding entity tracking in DbContext.

**🗣️ Spoken answer (30–45 seconds)**
By default, Entity Framework tracks every queried entity inside its ChangeTracker. It clones property snapshots in memory to detect changes when saving. Calling `.AsNoTracking()` disables this snapshot cloning for read-only queries. This reduces memory allocations and eases garbage collection pressure significantly. Entities returned without tracking cannot be modified simply by calling `SaveChangesAsync`. In one of my projects, applying `.AsNoTracking()` to GET endpoints cut response latency in half.

**🎯 Terms the interviewer listens for**
- ⭐ **ChangeTracker**: EF Core engine monitoring entity modifications and relationships.
- ⭐ **Snapshot cloning**: In-memory copying of property values used for diffing.
- ⭐ **AsNoTracking**: Query modifier disabling entity tracking for read-only workloads.
- **AsNoTrackingWithIdentityResolution**: Avoids duplicate entity instances while omitting snapshot tracking overhead.
- **Read-only query**: Database query returning data without intent to modify.
- **Memory allocation reduction**: Decreasing heap usage by eliminating tracking graph nodes.

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
No, async and await do not spawn new threads for I/O; they yield the executing thread back to the pool until hardware completes.

**🗣️ Spoken answer (30–45 seconds)**
Asynchronous I/O operations do not create or block any operating system threads. When an `await` executes on pending I/O, the state machine registers a callback. The current thread yields immediately to the thread pool to handle other requests. The operating system kernel handles the network transfer using I/O Completion Ports [IOCP]. When data arrives, hardware interrupts signal a free thread to resume the method. In one of my projects, async calls allowed our service to handle high concurrency without thread starvation.

**🎯 Terms the interviewer listens for**
- ⭐ **Thread yielding**: Returning active worker thread to pool during I/O waiting.
- ⭐ **I/O Completion Ports [IOCP]**: Kernel mechanism delivering asynchronous hardware completion signals.
- ⭐ **Hardware interrupt**: Low-level signal notifying CPU that device data transfer completed.
- **IAsyncStateMachine**: Compiler struct managing execution states across suspension points.
- **Non-blocking execution**: Running without holding CPU threads idle during external operations.
- **Throughput scalability**: Ability to process concurrent requests with minimal OS threads.

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
C# lock requires thread affinity and causes compiler error CS1996 with await, whereas SemaphoreSlim supports non-blocking asynchronous waiting across threads.

**🗣️ Spoken answer (30–45 seconds)**
The standard C# `lock` statement enforces strict thread affinity using `Monitor.Enter`. The exact thread that enters a lock must be the one that releases it. Because `await` can resume on a different thread pool thread, using `await` inside `lock` fails compilation with error CS1996. `SemaphoreSlim.WaitAsync` provides an asynchronous lock that does not block underlying threads. It can be released from any resuming thread inside a finally block. In one of my projects, `SemaphoreSlim` safely serialized token refresh calls across concurrent requests.

**🎯 Terms the interviewer listens for**
- ⭐ **SemaphoreSlim.WaitAsync**: Asynchronously acquires a synchronization slot without blocking threads.
- ⭐ **Thread affinity**: Requirement that acquiring and releasing thread must match identically.
- ⭐ **Compiler error CS1996**: Error triggered when using await inside a lock block.
- **Monitor.Enter / Exit**: Low-level CLR synchronization primitives underlying C# lock statements.
- **Async-safe mutex**: Single-slot semaphore configured with initial and maximum count one.
- **try-finally release**: Mandatory pattern guaranteeing semaphore release upon unexpected faults.

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
A clustered index defines the physical order of table data pages, while a non-clustered index is an auxiliary B-tree storing pointers to rows.

**🗣️ Spoken answer (30–45 seconds)**
In SQL Server, a clustered index determines the physical data order on disk. Because rows can only be sorted in one order, each table can have only one clustered index. A non-clustered index is an auxiliary structure containing indexed keys and row pointers. When queries need unindexed columns, SQL Server performs expensive key lookups to base pages. Adding columns to the `INCLUDE` clause creates a covering index, eliminating lookups. In one of my projects, covering indexes reduced query execution time from seconds to milliseconds.

**🎯 Terms the interviewer listens for**
- ⭐ **Clustered index**: B-tree whose leaf level contains the actual table data pages.
- ⭐ **Non-clustered index**: Auxiliary B-tree storing index keys plus row locator pointers.
- ⭐ **Key lookup**: Secondary lookup fetching unindexed columns from clustered leaf pages.
- **Covering index**: Index containing all query columns using the INCLUDE clause.
- **B-tree leaf nodes**: Bottom level of index structure storing data or pointers.
- **Row locator**: Pointer referencing base data row via clustered key or RID.

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
A subquery handles ties fine for 2nd-highest, but DENSE_RANK() inside a Common Table Expression generalizes cleanly to any Nth highest salary.

**🗣️ Spoken answer (30–45 seconds)**
Finding the second highest salary requires handling duplicate salary values correctly. A subquery like `WHERE Salary < (SELECT MAX(Salary))` handles ties fine for second-highest. However, `DENSE_RANK()` inside a Common Table Expression generalizes cleanly to any Nth highest salary. Unlike `RANK()`, which skips rank numbers on ties, `DENSE_RANK()` assigns consecutive rank numbers without gaps. In SQL Server 2012 and later, `OFFSET-FETCH` on distinct salaries is also valid. In one of my projects, `DENSE_RANK()` solved compensation band reporting without missing tied salaries.

**🎯 Terms the interviewer listens for**
- ⭐ **DENSE_RANK()**: Window function assigning contiguous ranks without skipping numbers on ties.
- ⭐ **RANK()**: Window function skipping subsequent ranks when tied values occur.
- ⭐ **Common Table Expression [CTE]**: Temporary named result set referenced within an executing query.
- **Ties handling**: Correctly accounting for multiple records sharing identical salary amounts.
- **OFFSET-FETCH clause**: ANSI SQL pagination syntax skipping rows and fetching next slice.
- **Window partition**: Subset of rows processed by window functions via OVER() clause.

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
Delete removes filtered rows with logging, truncate deallocates pages and resets identities with minimal logging, and drop deletes the entire table schema.

**🗣️ Spoken answer (30–45 seconds)**
The key distinction is command classification, logging volume, and rollback behavior. `DELETE` is a DML command that removes individual rows and fires triggers. `TRUNCATE` is a DDL command deallocating entire eight-kilobyte data pages and resetting identity counters. Contrary to popular myth, `TRUNCATE` can be rolled back inside an active transaction. `DROP` removes both table data and the table schema from the database catalog. In one of my projects, `TRUNCATE` emptied staging tables in milliseconds without log bloat.

**🎯 Terms the interviewer listens for**
- ⭐ **Page extent deallocation**: Releasing whole data pages rather than logging row deletions.
- ⭐ **Minimal logging**: Logging page allocation changes instead of individual row data.
- ⭐ **Identity seed reset**: Resetting auto-increment column value back to initial definition.
- **DML vs DDL**: Data manipulation language versus data definition language statements.
- **Trigger execution**: Automated procedure fired on row deletion events.
- **Active transaction rollback**: Reversing operations using ROLLBACK TRANSACTION within active transactions.

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
UNION ALL concatenates result sets directly, while UNION adds dedup using a memory grant and spills to TempDB only if memory runs short.

**🗣️ Spoken answer (30–45 seconds)**
Both set operators combine output rows from multiple queries with matching columns. `UNION ALL` concatenates datasets directly without inspecting rows for duplicate values. `UNION` adds dedup — usually a Distinct Sort or Hash Aggregate. It uses a memory grant and spills to TempDB only if memory runs short. You should default to `UNION ALL` unless business requirements demand deduplication. In one of my projects, switching to `UNION ALL` eliminated heavy query memory grants.

**🎯 Terms the interviewer listens for**
- ⭐ **UNION ALL**: Concatenates multiple query result sets without removing duplicate rows.
- ⭐ **Distinct Sort**: Execution plan operator sorting rows to eliminate duplicate tuples.
- ⭐ **Memory grant**: Memory allocated to query for sort and hash operations.
- **Hash Aggregate**: Alternative execution plan operator hashing rows to deduplicate data.
- **TempDB spill**: Writing sort data to disk when memory grant exhausts.
- **Set operator**: SQL operator combining rows from multiple projection queries.

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
A Primary Key enforces identity, disallows nulls, and defaults to clustered, while a Unique Key allows one null and defaults to non-clustered.

**🗣️ Spoken answer (30–45 seconds)**
Primary Key and Unique Key constraints both enforce uniqueness across table columns. A Primary Key uniquely identifies each row and strictly rejects NULL values. A table can have only one Primary Key, defaulting to a clustered index. In SQL Server, a Unique Key permits exactly one NULL value. Tables can have multiple Unique Key constraints, defaulting to non-clustered indexes. In one of my projects, unique keys enforced unique email addresses on optional user profiles.

**🎯 Terms the interviewer listens for**
- ⭐ **Primary key constraint**: Entity identifier enforcing uniqueness while strictly disallowing null values.
- ⭐ **Unique key constraint**: Alternate key constraint enforcing uniqueness while permitting one null.
- ⭐ **Single null rule**: SQL Server implementation permitting exactly one null in unique indexes.
- **Clustered index default**: Default index structure created automatically on primary key definition.
- **Non-clustered index default**: Default index structure created automatically on unique constraints.
- **Entity integrity**: Database integrity rule ensuring every table record is identifiable.

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
Stored procedures execute procedural code and DML modifying data, while functions must be deterministic, return values, and can be embedded in SELECT queries.

**🗣️ Spoken answer (30–45 seconds)**
The architectural boundary between them is side-effects and query composability. Stored procedures execute procedural logic, perform DML modifications, and manage database transactions. However, procedures cannot be called inside `SELECT` or `WHERE` clauses. User-defined functions compute calculations without side-effects and embed directly into queries. Scalar functions often trigger row-by-row [RBAR] execution penalties across large tables. In one of my projects, replacing scalar functions with inline table-valued functions improved report speed.

**🎯 Terms the interviewer listens for**
- ⭐ **Stored procedure**: Precompiled procedural database routine capable of executing DML and transactions.
- ⭐ **User-defined function [UDF]**: Side-effect free routine returning scalar values or table expressions.
- ⭐ **Inline Table-Valued Function**: Parameterized view expanding directly into calling query execution plans.
- **Side-effect prohibition**: Database rule preventing functions from modifying tables or schema.
- **Transaction management**: Controlling transaction boundaries via BEGIN, COMMIT, and ROLLBACK.
- **RBAR execution**: Row-by-agonizing-row processing penalty occurring in scalar function loops.

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
ACID guarantees transaction reliability: atomicity provides all-or-nothing completion, consistency preserves rules, isolation conceals interim states, and durability ensures committed data survives crashes.

**🗣️ Spoken answer (30–45 seconds)**
ACID properties guarantee data reliability during financial transactions like fund transfers. Atomicity ensures debiting Account A and crediting Account B succeed together or roll back completely. Consistency ensures balances comply with non-negative constraints and validation invariants before and after. Isolation prevents concurrent users from viewing intermediate balances during execution. Durability flushes committed changes to the write-ahead log [`LDF`] on disk. In one of my projects, explicit transaction scopes guaranteed zero discrepancies during payment gateway callbacks.

**🎯 Terms the interviewer listens for**
- ⭐ **Atomicity**: Guarantee that all operations succeed or all roll back completely.
- ⭐ **Consistency**: Invariant enforcement ensuring database state adheres to schema rules.
- ⭐ **Isolation**: Concurrency barrier preventing uncommitted transactions from affecting other queries.
- **Durability**: Guarantee that committed data survives power failures and system crashes.
- **Write-ahead logging [WAL]**: Writing transaction log records to disk before data page updates.
- **Transaction rollback**: Reversing uncommitted operations back to initial consistent state.

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
