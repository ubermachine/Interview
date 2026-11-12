# 00. Terminology Master Key — say the right term, every time

> **Why this file exists:** You understand the plain explanation but can't recall the
> exact term under pressure. This key glues each TERM to its MEANING and to a sentence
> you can say. Drill it daily (§4). Every other module now puts the term FIRST.

## How to read an entry
**TERM** = the word to say · *meaning* = what it is in plain words · *say it* = a natural
interview sentence using the term. Say the term OUT LOUD inside the sentence.

---

## 1. .NET / C#
| TERM | Meaning | Say it |
|---|---|---|
| **Transient** | new instance every request | "Validators are Transient—stateless and cheap." |
| **Scoped** | one instance per HTTP request | "DbContext is Scoped, one per request." |
| **Singleton** | one instance for the whole app | "The cache is a Singleton, shared everywhere." |
| **Captive dependency** | long-lived service traps a short-lived one | "A Singleton holding a Scoped DbContext is a captive dependency." |
| **IoC container** | creates & injects dependencies | "The IoC container resolves constructor dependencies." |
| **Expression tree** | query stored as data, turned into SQL | "IQueryable keeps the query as an expression tree." |
| **Deferred execution** | runs only when enumerated | "Deferred execution means five Wheres still make one query." |
| **Materialize** | run & load the rows | "I materialize with ToListAsync at the end." |
| **Server-side evaluation** | filtering in the database | "IQueryable gives server-side evaluation." |
| **Immutability** | can't change after creation | "String immutability means every edit allocates a new object." |
| **GC pressure / Gen 0** | short-lived garbage piling up | "String += in a loop creates Gen 0 GC pressure." |
| **Boxing** | value type wrapped in a heap object | "Generics avoid boxing in hot loops." |
| **Value / reference type** | copied value vs shared reference | "A struct is a value type; a class is a reference type." |
| **Value equality** | equal when contents match | "Records give value equality for free." |
| **Dynamic dispatch / vtable** | CLR picks the override at runtime | "Overriding uses vtable dispatch at runtime." |
| **Compile-time constant / IL inlining** | value baked into callers | "const is inlined into callers' IL—changes need a rebuild." |
| **Delegate** | type-safe function pointer | "A delegate lets me pass behavior as a value." |
| **Closure** | lambda capturing an outer variable | "A closure allocates a hidden class for the captured variable." |
| **Deterministic cleanup** | you control when resources release | "IDisposable gives deterministic cleanup." |
| **Unmanaged resources** | OS handles the GC can't free | "Sockets and file handles are unmanaged resources." |
| **State machine** | compiler's pause/resume code for async | "await compiles into a state machine." |
| **Non-blocking I/O** | no thread waits on the network | "await uses non-blocking I/O." |
| **Sync-over-async** | blocking with .Result / .Wait() | "Sync-over-async causes thread starvation." |
| **Thread starvation** | all pool threads blocked | "Blocking calls starve the thread pool." |
| **Middleware / request pipeline** | component in the request chain | "Logging middleware runs for every request." |
| **Short-circuit** | return early, skip the rest | "Auth middleware short-circuits with 401." |
| **ModelState** | MVC's validation results | "The filter checks ModelState.IsValid." |
| **Claims** | key-value facts about the user | "The JWT carries role and tenant claims." |
| **ClockSkew** | token-expiry grace period | "I set ClockSkew to zero for exact expiry." |
| **CORS / preflight** | browser's cross-origin check | "The browser sends a preflight OPTIONS first." |
| **Eager loading / N+1** | fetch up front vs one query per child | "Include avoids the N+1 problem." |
| **Change tracking** | EF watching entities for edits | "AsNoTracking disables change tracking for reads." |
| **Optimistic concurrency** | detect conflict via a version column | "I use optimistic concurrency with a rowversion." |
| **Generational hypothesis** | most objects die young | "The GC is built on the generational hypothesis." |
| **IAsyncStateMachine** | compiler-generated async state tracker | "The compiler turns async into an IAsyncStateMachine." |
| **IOCP (I/O Completion Ports)** | OS notification for finished I/O | "IOCP notifies the runtime when data arrives." |
| **ValueTask** | struct avoiding Task allocation on cache hit | "ValueTask avoids heap allocation on synchronous completion." |
| **ThreadPool starvation** | all workers blocked, requests queue | "Sync-over-async causes ThreadPool starvation under load." |
| **RequestDelegate** | Func<HttpContext, Task> in the pipeline | "Each middleware is a RequestDelegate." |
| **IHttpClientFactory** | pooled handlers avoiding socket exhaustion | "IHttpClientFactory pools HttpMessageHandlers." |
| **Socket exhaustion** | ports stuck in TIME_WAIT | "Creating HttpClient per request causes socket exhaustion." |
| **ProblemDetails (RFC 7807)** | standard error response format | "ProblemDetails gives clients a machine-readable error." |
| **Lazy<T>** | thread-safe deferred initialization | "Lazy<T> initializes the singleton on first access." |
| **IDisposable / using** | deterministic resource release pattern | "The using statement guarantees Dispose is called." |
| **CancellationToken** | cooperative cancellation signal | "I propagate CancellationToken to every async layer." |

## 2. SQL Server
| TERM | Meaning | Say it |
|---|---|---|
| **Clustered index** | the table's physical row order | "The clustered index is the table itself, sorted." |
| **Non-clustered index** | separate structure pointing to rows | "It's like the index at the back of a book." |
| **Covering index** | index holds every column needed | "A covering index removes the key lookup." |
| **Key lookup** | extra hop from index back to table | "The key lookup was the bottleneck." |
| **Index seek / scan** | jump to the row vs read everything | "We want a seek, not a scan." |
| **B-tree** | the balanced tree indexes use | "Indexes are B-trees." |
| **Execution plan** | the optimizer's chosen steps | "I read the execution plan for the costly operator." |
| **Parameter sniffing** | plan cached for first parameter values | "Parameter sniffing gave a bad plan for other values." |
| **SARGable** | a predicate the index can seek on | "A function on the column makes it non-SARGable." |
| **CTE** | named temporary result (WITH) | "I wrap DENSE_RANK in a CTE." |
| **Window function** | computes across related rows (OVER) | "DENSE_RANK is a window function." |
| **DENSE_RANK** | rank with no gaps on ties | "DENSE_RANK handles ties without skipping ranks." |
| **PARTITION BY** | restart ranking per group | "PARTITION BY department ranks within each." |
| **Deadlock** | two transactions each waiting on the other | "SQL Server detects it and kills one." |
| **Isolation level** | how much transactions see of each other | "Read Committed is the default isolation level." |
| **ACID** | atomicity, consistency, isolation, durability | "ACID makes the transfer safe." |
| **Write-ahead log** | changes logged before commit | "Durability comes from the write-ahead log." |
| **Lock escalation** | many row locks become a table lock | "Big deletes trigger lock escalation." |
| **RBAR** | row by agonizing row | "Scalar UDFs run RBAR—slow." |
| **TempDB spill** | sort overflow to disk | "The sort spilled to TempDB." |
| **Page extent deallocation** | TRUNCATE's fast bulk removal | "TRUNCATE deallocates pages, not rows." |
| **Minimal logging** | only page pointers logged, not row data | "TRUNCATE uses minimal logging." |
| **Identity seed reset** | TRUNCATE resets the counter | "TRUNCATE resets the identity seed." |
| **Set operator** | UNION / INTERSECT / EXCEPT | "UNION ALL is the fastest set operator." |
| **Inline Table-Valued Function (iTVF)** | set-based UDF the optimizer inlines | "An iTVF is inlined into the outer query." |

## 3. Angular
| TERM | Meaning | Say it |
|---|---|---|
| **Signal** | reactive value that notifies readers | "I hold state in a signal." |
| **Computed** | derived signal that caches its result | "Total is a computed signal." |
| **OnPush** | check only when inputs change | "OnPush skips unnecessary change detection." |
| **Change detection** | Angular checking what to re-render | "Zone.js triggers change detection." |
| **runOutsideAngular** | run without triggering checks | "I run mousemove outside Angular for 60fps." |
| **switchMap** | cancel old, keep latest | "switchMap cancels stale searches." |
| **mergeMap** | run all in parallel | "mergeMap fires them concurrently." |
| **concatMap** | queue in order | "concatMap keeps writes ordered." |
| **exhaustMap** | ignore new while one runs | "exhaustMap blocks double-click submits." |
| **Observable / subscription** | stream of values / listening to it | "An unclosed subscription leaks memory." |
| **takeUntilDestroyed** | auto-unsubscribe on destroy | "takeUntilDestroyed prevents the leak." |
| **Debounce** | wait for a pause before firing | "debounceTime waits for typing to stop." |
| **Interceptor** | middleware for HTTP calls | "The interceptor attaches the token." |
| **Route guard / UrlTree** | allows a route / redirect object | "The guard returns a UrlTree to redirect." |
| **Standalone component** | component without an NgModule | "Standalone removes the module boilerplate." |
| **NgZone** | Angular's execution context for change detection | "NgZone wraps async events for change detection." |
| **DestroyRef** | lifecycle hook for cleanup | "I inject DestroyRef for manual cleanup." |
| **Content projection (ng-content)** | slot for parent-provided markup | "ng-content is Angular's slot mechanism." |
| **ViewChild / ContentChild** | query a child element or component | "ViewChild grabs the reference after render." |

## 4. Microservices
| TERM | Meaning | Say it |
|---|---|---|
| **Saga** | cross-service transaction as local steps + undo | "I coordinate the order with a saga." |
| **Compensating transaction** | action that undoes a committed step | "Refund compensates the charge." |
| **Orchestration / choreography** | central coordinator vs event-reacting services | "Orchestration uses a state machine." |
| **Eventual consistency** | consistent once the saga finishes | "The system reaches eventual consistency." |
| **Transactional outbox** | save event in the same DB commit | "The outbox stops us losing events." |
| **Idempotent** | safe to process twice | "Consumers must be idempotent for retries." |
| **Circuit breaker** | stop calling a failing service | "The breaker trips after repeated failures." |
| **CQRS** | separate read and write models | "CQRS splits commands from queries." |
| **Event sourcing** | store state as a sequence of events | "Event sourcing rebuilds state from events." |
| **API gateway** | single entry point for clients | "The gateway routes to services." |
| **Correlation ID** | ID tying logs across services | "I propagate a correlation ID for tracing." |
| **Temporal coupling** | caller needs callee up right now | "Sync calls create temporal coupling." |
| **Backpressure** | slow the producer when consumer lags | "A bounded channel gives backpressure." |
| **Bounded context** | autonomous domain boundary for a service | "Each microservice owns a bounded context." |
| **Service mesh** | infrastructure layer for service-to-service comms | "The service mesh handles mTLS and retries." |
| **Strangler fig** | incremental migration pattern | "We migrate with the strangler fig pattern." |

## 5. Concurrency
| TERM | Meaning | Say it |
|---|---|---|
| **Race condition** | outcome depends on thread timing | "Two threads incrementing cause a race condition." |
| **Deadlock** | threads each waiting on the other's lock | "Lock ordering prevents deadlock." |
| **Lock / Monitor** | only one thread in a section | "lock uses Monitor under the hood." |
| **SemaphoreSlim** | a lock that works with async | "I use SemaphoreSlim for async locking." |
| **Interlocked** | atomic CPU-level operation | "Interlocked.Increment is atomic." |
| **Thread-safe** | safe from many threads | "Immutable objects are thread-safe." |
| **Optimistic concurrency** | check a version at write time | "rowversion enables optimistic concurrency." |
| **Pessimistic locking** | lock the row up front | "UPDLOCK takes a pessimistic lock." |
| **Fencing token** | number that rejects stale lock holders | "A fencing token stops a paused node writing." |
| **ConcurrentDictionary** | thread-safe dictionary using fine-grained locks | "ConcurrentDictionary uses striped locks." |
| **Volatile** | prevents CPU/compiler reordering | "volatile ensures read/write visibility." |
| **SpinLock** | busy-wait lock for ultra-short critical sections | "SpinLock avoids context-switch overhead." |

## 6. Security
| TERM | Meaning | Say it |
|---|---|---|
| **Authentication / authorization** | who you are / what you may do | "AuthN validates the JWT; AuthZ checks the policy." |
| **BOLA / IDOR** | accessing someone else's record by ID | "BOLA is the top API vulnerability." |
| **Mass assignment** | client binding to sensitive fields | "DTOs prevent mass assignment." |
| **SQL injection / parameterized query** | input run as SQL / input sent as a value | "Parameterized queries stop SQL injection." |
| **XSS / CSRF** | injected script / forged browser request | "Encoding stops XSS; SameSite mitigates CSRF." |
| **DTO** | shaped input/output object | "I bind to a DTO, not the entity." |
| **Tenant isolation** | each customer sees only their data | "Global query filters enforce tenant isolation." |
| **Non-repudiation** | sender can't deny signing (RS256 only) | "RS256 provides non-repudiation." |
| **PKCE** | proof key that stops code interception | "SPAs use PKCE to protect the auth code." |
| **OWASP Top 10** | industry-standard vulnerability list | "I design against the OWASP Top 10." |
| **Rate limiting** | throttling requests per client | "Rate limiting prevents abuse and DoS." |
| **HTTPS / TLS** | encrypted transport | "TLS encrypts data in transit." |

---

## 7. Question → Terms to say (the recall bridge)

> **How to use:** Cover the right column. Read the question. Say the terms from memory.
> Anything you miss goes on tomorrow's repeat list.

| If they ask… | Say these terms |
|---|---|
| .NET Garbage Collection manage memory across generations | Generational hypothesis, Ephemeral generations, Large Object Heap (LOH) |
| Workstation GC and Server GC | Server GC, Workstation GC, Concurrent GC |
| The IDisposable pattern differ from Finalize | Deterministic cleanup, Finalizer (~ClassName), GC.SuppressFinalize |
| How do async and await work under the hood without blocking th... | IAsyncStateMachine, I/O Completion Ports (IOCP), Thread yielding |
| Use ValueTask instead of Task | ValueTask<T>, Synchronous completion, GC Gen 0 pressure |
| What causes ThreadPool starvation and how does sync-over-async... | Sync-over-async, ThreadPool starvation, Thread injection rate |
| The ASP.NET Core middleware request pipeline execute | RequestDelegate, Bidirectional pipeline, Endpoint routing boundary |
| Dependency Injection lifetimes and how do you avoid captive de... | Captive dependency, IServiceScopeFactory, Scoped lifetime |
| Why should you use IHttpClientFactory instead of instantiating... | IHttpClientFactory, Socket exhaustion, DNS rotation |
| Explain and apply SOLID principles in a real-world Web API | Single Responsibility, Open/Closed Principle, Dependency Inversion |
| IEnumerable, IQueryable, ICollection, and IList | IQueryable<T>, IEnumerable<T>, Expression tree |
| String immutability and when should you use StringBuilder | String immutability, StringBuilder, String interning |
| Ref, out, in, and params in C# | Pass-by-reference, Definite assignment, Zero-copy for large structs |
| Throw, throw ex, and throw new CustomException | Stack trace preservation, throw;, InnerException chaining |
| Use an abstract class versus an interface with C# 8+ default m... | Interface contract, Single inheritance, Default interface methods |
| How do boxing and unboxing work and what is their performance ... | Boxing, Object header, Generics eliminate boxing |
| Method overloading, overriding, and method shadowing | Compile-time vs runtime polymorphism, vtable, Dynamic dispatch |
| Const, readonly, and static readonly | Compile-time constant, IL inlining, Static constructor (.cctor) |
| How do Dependency Injection lifetimes work and what is a capti... | Transient lifetime, Scoped lifetime, Captive dependency |
| The architectural difference between Middleware and Action Fil... | RequestDelegate, Endpoint routing boundary, ActionExecutingContext |
| Write custom middleware for global exception handling using Pr... | ProblemDetails (RFC 7807), TraceIdentifier, Information disclosure |
| How do JWT authentication and authorization work in ASP.NET Co... | ClaimsPrincipal, ClockSkew, Bearer token |
| CORS work in ASP.NET Core and how do you configure it safely | Same-Origin Policy (SOP), Preflight OPTIONS, Access-Control-Allow-Origin |
| Eager Loading, Lazy Loading, and Explicit Loading in EF Core | Eager loading (.Include), N+1 problem, Cartesian explosion |
| First, FirstOrDefault, Single, SingleOrDefault, and Find in EF... | SELECT TOP(1) vs TOP(2), Cardinality verification, First-level cache (Find) |
| AsNoTracking do in EF Core and when should you use it | ChangeTracker, Snapshot cloning, Read-only optimization |
| Does async and await create a new background thread for I/O op... | Thread yielding, I/O Completion Ports (IOCP), Hardware interrupt |
| Why should you use SemaphoreSlim instead of lock in asynchrono... | SemaphoreSlim.WaitAsync, Thread affinity, Compiler error CS1996 |
| A Clustered Index and a Non-Clustered Index in SQL Server | Clustered index, Non-clustered index, Key lookup |
| Find the 2nd highest or Nth highest salary in SQL Server | DENSE_RANK(), Common Table Expression (CTE), Window function |
| DELETE, TRUNCATE, and DROP in SQL Server | Page extent deallocation, Minimal logging, Identity seed reset |
| UNION and UNION ALL in SQL Server | UNION ALL, Distinct Sort, TempDB spill |
| A Primary Key and a Unique Key constraint | Primary key constraint, Unique key constraint, Single null rule |
| A Stored Procedure and a User-Defined Function (UDF) | Stored procedure, Inline Table-Valued Function (iTVF), RBAR |
| Explain ACID properties with a real-world banking scenario | Atomicity, Isolation, Write-ahead log (WAL) |
| SOLID Principles with Real-Time Project Examples | Single Responsibility, Open/Closed, Dependency Inversion |
| IEnumerable vs IQueryable vs IList vs ICollection | Expression tree, Server-side evaluation, Deferred execution |
| String vs StringBuilder & String Immutability | Immutability, StringBuilder, GC pressure |
| Ref vs out vs in vs params | Pass-by-reference, Definite assignment, Zero-copy |
| Throw vs throw ex vs throw new CustomException | Stack trace preservation, throw;, InnerException chaining |
| Abstract Class vs Interface (with C# 8+ Default Methods) | Interface contract, Single inheritance, Default interface methods |
| Boxing and Unboxing Mechanics & Performance | Boxing, Object header, Generics |
| Method Overloading vs Method Overriding vs Method Shadowing (new) | Compile-time polymorphism, vtable, Dynamic dispatch |
| Const vs readonly vs static readonly | Compile-time constant, IL inlining, Static constructor |
| Delegates, Func, Action, Predicate & Lambda Expressions | Delegate, Closure, Func |
| Extension Methods in C# | Extension method, this modifier, Instance precedence |
| Nullable Types, Null-Forgiving (!) & Null-Coalescing (??, ??=) | Nullable value type, Nullable reference types, Null-coalescing |
| Class vs struct vs record (Record Class vs Record Struct) | Record, Value equality, Non-destructive mutation |
| IDisposable Pattern & the using Statement | Deterministic cleanup, Unmanaged resources, GC.SuppressFinalize |
| Dependency Injection Lifetimes (Transient vs Scoped vs Singlet... | Transient, Scoped, Captive dependency |
| Middleware vs Action Filters (app.Use vs app.Run vs app.Map) | RequestDelegate, Endpoint routing boundary, Action filter |
| Writing Custom Middleware for Global Exception Handling | Global exception middleware, TraceIdentifier, ProblemDetails |
| ASP.NET Core Filter Pipeline Order of Execution | Authorization filter, Resource filter, Action filter |
| JWT Authentication & Authorization in Web API | Bearer token, ClaimsPrincipal, ClockSkew |
| CORS (Cross-Origin Resource Sharing) Configuration | Same-Origin Policy, Preflight OPTIONS, Access-Control-Allow-Origin |
| Configuration & Options Pattern (IOptions vs IOptionsSnapshot ... | Options pattern, IOptionsSnapshot, IOptionsMonitor |
| HTTP Status Codes & RESTful API Best Practices | REST, Idempotency, ProblemDetails |
| IHttpClientFactory: Typed Client vs Socket Exhaustion vs DNS Bug | Socket exhaustion, DNS stale cache bug, IHttpClientFactory |
| Eager Loading (.Include) vs Lazy Loading vs Explicit Loading | Eager loading, N+1 problem, Cartesian explosion |
| First vs FirstOrDefault vs Single vs SingleOrDefault vs Find | FirstOrDefault, SingleOrDefault, Find |
| AsNoTracking() vs Tracked Queries | ChangeTracker, Snapshot cloning, AsNoTracking |
| Code-First Migrations & Production CI/CD Scripts | Code-first migrations, __EFMigrationsHistory, Idempotent script |
| EF Core vs Dapper: When to Use Which | Full ORM, Micro-ORM, CQRS |
| Select() vs SelectMany() in LINQ | Select, SelectMany, CROSS APPLY |
| Handling Concurrency in EF Core with RowVersion | Optimistic concurrency, Rowversion, DbUpdateConcurrencyException |
| Async and await Internals: Does it Create a New Thread | Non-blocking I/O, State machine, IOCP |
| The Sync-over-Async Trap (.Result & .Wait Deadlocks) | Sync-over-async, SynchronizationContext, ThreadPool starvation |
| Task.WhenAll vs Task.WaitAll vs Task.WhenAny | Task.WhenAll, Task.WaitAll, Task.WhenAny |
| CancellationToken Propagation in Web APIs | CancellationToken, Cooperative cancellation, RequestAborted |
| Lock vs SemaphoreSlim in Asynchronous Code | Thread affinity, CS1996, SemaphoreSlim |
| Repository Pattern & Unit of Work in EF Core Projects | Data access abstraction, Repository pattern, Unit of work |
| Thread-Safe Singleton Pattern (Double-Check vs Lazy<T>) | Lazy<T>, Double-checked locking, volatile |
| Factory Pattern vs Abstract Factory Pattern | Factory Method, Abstract Factory, Keyed services |
| CQRS & MediatR Pattern in Web APIs | CQRS, Mediator pattern, Pipeline behavior |
| Caching Strategies: IMemoryCache vs IDistributedCache (Redis) | IMemoryCache, IDistributedCache, Cache stampede |
| Microservices Communication: Synchronous vs Asynchronous | Temporal coupling, Asynchronous messaging, Transactional outbox |
| Clustered vs Non-Clustered Index | Clustered index, Non-clustered index, Covering index |
| Finding the 2nd Highest / Nth Highest Salary | CTE, DENSE_RANK, Window function |
| DELETE vs TRUNCATE vs DROP | Page extent deallocation, Minimal logging, Identity seed reset |
| UNION vs UNION ALL | Distinct sort, TempDB spill, UNION ALL |
| Primary Key vs Unique Key | Primary key, Clustered index, Unique key |
| Stored Procedure vs User-Defined Function (UDF) | Stored procedure, RBAR, Inline TVF |
| ACID Properties Explained with a Banking Scenario | Atomicity, Isolation, Write-ahead log |
| A clustered and a non-clustered index | Clustered index, Non-clustered index, Covering index |
| Find the second highest or Nth highest salary in SQL | DENSE_RANK, CTE, Window function |
| DELETE, TRUNCATE, and DROP | TRUNCATE, Page extent deallocation, Minimal logging |
| UNION and UNION ALL | UNION ALL, Distinct sort, TempDB spill |
| A Primary Key and a Unique Key constraint | Primary Key, Entity integrity, Clustered index |
| A Stored Procedure and a User-Defined Function | Stored procedure, Side-effect-free, Inline Table-Valued Function (iTVF) |
| How do SQL Server joins work and how do they handle NULL values | Three-valued logic, Relational equality predicate, Outer join |
| Find and delete duplicate records in a table | ROW_NUMBER, PARTITION BY, Window function |
| ACID properties and how do they ensure transactional integrity | ACID, Atomicity, Write-ahead logging |
| Database normalization normal forms from 1NF through BCNF | Normalization, 1NF, 2NF |
| Index Seek, Index Scan, Table Scan, and Key Lookup | Index seek, Index scan, Key lookup |
| What makes a query SARGable and why do functions on indexed co... | SARGable, Non-SARGable predicate, Index scan |
| AFTER and INSTEAD OF triggers | AFTER trigger, INSTEAD OF trigger, Inserted and deleted tables |
| The WHERE clause and the HAVING clause | WHERE clause, HAVING clause, Logical query processing |
| Choose between a CTE, Temp Table, and Table Variable | Temporary table, Table variable, CTE |
| A page split and how does it impact SQL Server performance | Page split, Internal fragmentation, Index fill factor |
| PAGELATCH_* and PAGEIOLATCH_* wait types | PAGELATCH, PAGEIOLATCH, Buffer pool cache |
| A random GUID dangerous as a clustered index key | Random GUID, Mid-page split, Internal fragmentation |
| A memory grant and what causes TempDB spills | Memory grant, Cardinality estimation, TempDB spill |
| The CXPACKET wait type signify and how is it tuned | CXPACKET, Cost Threshold for Parallelism, MAXDOP |
| OPTIMIZE FOR UNKNOWN and OPTION (RECOMPILE) | OPTION (RECOMPILE), OPTIMIZE FOR UNKNOWN, Plan cache |
| SQL Server maintain statistics and when do they become stale | Statistics, Histogram, Cardinality estimation |
| A Filtered Index and an Indexed View | Filtered index, Indexed view, SCHEMABINDING |
| The dangers of using NOLOCK or READ UNCOMMITTED in production | NOLOCK, Dirty read, Read Committed Snapshot Isolation (RCSI) |
| SET NOCOUNT ON do and why should it be used | SET NOCOUNT ON, DONE_IN_PROC token, Network round-trip latency |
| DATETIME and DATETIME2 | DATETIME2, Nanosecond precision, Millisecond rounding |
| ISNULL and COALESCE | COALESCE, ISNULL, Data type precedence |
| REORGANIZE and REBUILD for index maintenance | Index rebuild, Index reorganize, Automatic statistics update |
| An Adaptive Join in modern SQL Server | Adaptive join, Intelligent Query Processing, Adaptive threshold |
| Why does OFFSET-FETCH become slow on deep pagination and how d... | Keyset paging, Linear degradation, Logarithmic search |
| Find the second highest or Nth highest salary in SQL | DENSE_RANK, CTE, Window function |
| Find and delete duplicate records in a table | ROW_NUMBER, PARTITION BY, Window function |
| How do SQL Server joins work and how do they handle NULL values | Three-valued logic, Relational equality predicate, Outer join |
| UNION and UNION ALL | UNION ALL, Distinct sort, TempDB spill |
| A Stored Procedure and a User-Defined Function | Stored procedure, Side-effect-free, Inline Table-Valued Function (iTVF) |
| Choose between a CTE, Temp Table, and Table Variable | Temporary table, Table variable, CTE |
| A Primary Key and a Unique Key constraint | Primary Key, Entity integrity, Clustered index |
| DELETE, TRUNCATE, and DROP | TRUNCATE, Page extent deallocation, Minimal logging |
| Database normalization normal forms from 1NF through BCNF | Normalization, 1NF, 2NF |
| AFTER and INSTEAD OF triggers | AFTER trigger, INSTEAD OF trigger, Inserted and deleted tables |
| A clustered and a non-clustered index | Clustered index, Non-clustered index, Covering index |
| Index Seek, Index Scan, Table Scan, and Key Lookup | Index seek, Index scan, Key lookup |
| How do covering indexes with INCLUDE columns eliminate costly ... | Covering index, INCLUDE clause, Key lookup elimination |
| What makes a query SARGable and why do functions on indexed co... | SARGable, Non-SARGable predicate, Index scan |
| Parameter sniffing and how do you diagnose and fix it in produ... | Parameter sniffing, Data distribution skew, Plan cache instability |
| The differences between Nested Loops, Hash Match, and Merge Jo... | Nested Loops, Merge join operator, Hash Match join |
| SQL Server maintain statistics and when do cardinality estimat... | Statistics, Histogram, Cardinality estimation |
| ACID properties and how do they ensure transactional integrity | ACID, Atomicity, Write-ahead logging |
| Transaction isolation levels and what concurrency anomalies do... | Isolation level, Dirty read, Non-repeatable read |
| What causes deadlocks in SQL Server and how do you diagnose an... | Deadlock, Cyclic lock dependency, Deadlock victim |
| SQL Server lock modes and what triggers lock escalation to a t... | Lock escalation, Granular lock modes, Intent locks |
| A page split and how does it impact SQL Server performance | Page split, Internal fragmentation, Index fill factor |
| PAGELATCH_* and PAGEIOLATCH_* wait types | PAGELATCH, PAGEIOLATCH, Buffer pool cache |
| A random GUID dangerous as a clustered index key | Random GUID, Mid-page split, Internal fragmentation |
| UNION and UNION ALL | UNION ALL, Distinct sort, TempDB spill |
| A memory grant and what causes TempDB spills | Memory grant, Cardinality estimation, TempDB spill |
| The CXPACKET wait type signify and how is it tuned | CXPACKET, Cost Threshold for Parallelism, MAXDOP |
| OPTIMIZE FOR UNKNOWN and OPTION (RECOMPILE) | OPTION (RECOMPILE), OPTIMIZE FOR UNKNOWN, Plan cache |
| What causes an Index Scan on an index whose leading key column... | Index scan, Non-SARGable function, Implicit datatype conversion |
| SQL Server maintain statistics and when do they become stale | Statistics, Histogram, Cardinality estimation |
| A Filtered Index and an Indexed View | Filtered index, Indexed view, SCHEMABINDING |
| The FORCESEEK table hint do and when should it be used | FORCESEEK, Error 8622, Temporary stabilization hint |
| SNAPSHOT isolation and SERIALIZABLE isolation | SNAPSHOT isolation, Optimistic row versioning, Key-range locking |
| A Cardinality Estimation (CE) feedback loop in modern SQL Server | Cardinality Estimation feedback, Intelligent Query Processing, Query Store hint persistence |
| The dangers of using NOLOCK or READ UNCOMMITTED in production | NOLOCK, Dirty read, Read Committed Snapshot Isolation (RCSI) |
| Eliminate TempDB allocation contention on GAM, SGAM, and PFS p... | Allocation map contention, Multiple TempDB data files, Uniform extent allocation |
| The differences between Nested Loops, Hash Match, and Merge Jo... | Nested Loops, Merge join operator, Hash Match join |
| SET NOCOUNT ON do and why should it be used | SET NOCOUNT ON, DONE_IN_PROC token, Network round-trip latency |
| A Plan Guide and when should it be used in production | Plan Guide, Third-party application tuning, Query Store hints |
| Sys.dm_exec_query_stats and sys.dm_exec_requests | sys.dm_exec_query_stats, sys.dm_exec_requests, Real-time wait analysis |
| REORGANIZE and REBUILD for index maintenance | Index rebuild, Index reorganize, Automatic statistics update |
| DATETIME and DATETIME2 | DATETIME2, Nanosecond precision, Millisecond rounding |
| An Adaptive Join in modern SQL Server | Adaptive join, Intelligent Query Processing, Adaptive threshold |
| Identify what is preventing transaction log (LDF) truncation | Log reuse wait, Virtual Log File (VLF), Active transaction blocker |
| Choose between a CTE, Temp Table, and Table Variable | Temporary table, Table variable, CTE |
| The Query Optimizer calculate the estimated cost of an executi... | Cost-based optimizer, Unitless cost metric, CPU versus I/O weighting |
| Standalone Components & Directives | (core terms pending) |
| Built-in Control Flow (@if, @for, @switch) | (core terms pending) |
| Deferrable Views (@defer) | (core terms pending) |
| Functional Dependency Injection via inject() | (core terms pending) |
| Angular Signals & The Reactive Trio | (core terms pending) |
| RxJS Flattening Operators | (core terms pending) |
| Memory Leak Prevention & Teardown Mechanics | (core terms pending) |
| Change Detection Optimization (OnPush) | (core terms pending) |
| Functional Interceptors & Route Guards | (core terms pending) |
| Modern State Management with SignalStore | (core terms pending) |
| Angular component lifecycle hooks and what is their execution ... | ngOnInit, ngOnChanges, ngOnDestroy |
| Angular Signals and RxJS Observables | Signal, Observable, toSignal() |
| Pass data between parent and child components using modern pri... | input(), output(), model() |
| ViewChild and ContentChild | ViewChild, ContentChild, Content projection |
| Structural directives and attribute directives | Structural directives, Attribute directives, track expression |
| Pure and impure pipes | Pure pipe, Impure pipe, Memoization |
| Dependency Injection in Angular: providedIn root vs component-... | providedIn, Component providers, Hierarchical DI |
| Change Detection in Angular? Explain Default vs OnPush. | Change detection, OnPush strategy, markForCheck() |
| RxJS flattening operators: switchMap, mergeMap, concatMap, and... | switchMap, mergeMap, concatMap |
| Implement lazy loading and functional route guards in modern A... | loadComponent, CanActivateFn, UrlTree |
| Reactive Forms vs Template-Driven Forms and custom validation. | FormControl, FormGroup, ValidatorFn |
| How do HTTP Interceptors work in modern Angular and how do you... | HttpInterceptorFn, Request cloning, JWT bearer token |
| What causes memory leaks in Angular applications and how do yo... | takeUntilDestroyed(), DestroyRef, Detached DOM tree |
| The exact difference between signal, computed, and effect | signal(), computed(), effect() |
| Mutating a Signal array directly with push an anti-pattern | Object.is, update(), Immutable update |
| What causes ExpressionChangedAfterItHasBeenCheckedError and ho... | Unidirectional data flow, Verification pass, ngAfterViewInit |
| ViewChild static true and static false | static, static, viewChild() |
| How do forkJoin, combineLatest, and withLatestFrom differ | forkJoin, combineLatest, withLatestFrom |
| Subject, BehaviorSubject, and ReplaySubject | Subject, BehaviorSubject, ReplaySubject |
| Share state between unrelated components using modern Angular | Injectable service, asReadonly(), computed() |
| The purpose of untracked inside an effect or computed signal | untracked(), Reactive context, Circular dependency |
| Deferrable Views (@defer) and their trigger conditions. | @defer, on viewport, on interaction |
| Implement global error handling in Angular | ErrorHandler, handleError(), Centralized logging |
| The difference between Renderer2 and direct ElementRef.nativeE... | Renderer2, ElementRef, Server-Side Rendering (SSR) |
| Angular protect against Cross-Site Scripting (XSS) and when sh... | DomSanitizer, Security context, XSS protection |
| Non-Destructive Hydration in modern Angular Server-Side Rendering | Non-destructive hydration, provideClientHydration(), DOM flickering |
| Take(1), first(), and single() in RxJS | take(1), first(), single() |
| Host property bindings vs @HostBinding and @HostListener. | host property, @HostBinding, @HostListener |
| Component input transforms like booleanAttribute and numberAtt... | booleanAttribute, numberAttribute, Input transform |
| ShareReplay(1) dangerous without refCount true | shareReplay(1), refCount, Subscription retention |
| The exact execution sequence of Angular component lifecycle hooks | ngOnInit, ngOnChanges, ngOnDestroy |
| The parent-child lifecycle hook execution order during creatio... | Top-down creation, Bottom-up view completion, Top-down teardown |
| NgOnChanges, ngOnInit, and ngDoCheck | ngOnInit, ngOnChanges, ngDoCheck |
| What causes ExpressionChangedAfterItHasBeenCheckedError and wh... | Unidirectional data flow, Verification sweep, ngAfterViewInit |
| How do signal, computed, and effect work under the hood in mod... | signal(), computed(), effect() |
| Mutating an array with push an anti-pattern in Angular Signals | Object.is, Immutable update, update() |
| The purpose of untracked inside an effect or computed signal | untracked(), Reactive context, Circular dependency |
| How do modern signal inputs and two-way model signals work in ... | input(), input.required(), model() |
| Use Angular Signals versus RxJS Observables | Synchronous state, Asynchronous stream, toSignal() |
| How do toSignal and toObservable work and what are their conte... | toSignal(), toObservable(), Injection context |
| How do forkJoin, combineLatest, and withLatestFrom differ in p... | forkJoin, combineLatest, withLatestFrom |
| How do modern component communication primitives compare to le... | input(), output(), model() |
| ViewChild and ContentChild and how does static resolution work | ViewChild, ContentChild, static |
| Architect cross-component communication using a Signals servic... | Singleton service, asReadonly(), Encapsulation |
| How do switchMap, mergeMap, concatMap, and exhaustMap differ i... | switchMap, mergeMap, concatMap |
| Implement typeahead live search preventing race conditions and... | switchMap, debounceTime, Inner catchError |
| Prevent duplicate form submissions using exhaustMap versus seq... | exhaustMap, concatMap, Double-click prevention |
| Immutability mandatory when using ChangeDetectionStrategy.OnPu... | OnPush strategy, Reference equality, Immutability |
| How do markForCheck, detectChanges, detach, and reattach diffe... | markForCheck(), detectChanges(), detach() |
| Modern Zoneless Angular compare to NgZone.runOutsideAngular | provideExperimentalZonelessChangeDetection(), NgZone.runOutsideAngular(), Microtask scheduler |
| Modern built-in control flow outperform legacy structural dire... | @for block, track expression, @empty block |
| Build custom attribute directives using modern host property b... | host property, Renderer2, ElementRef |
| The performance risks of impure pipes and how does pure pipe c... | Pure pipe, Impure pipe, Memoization |
| Angular's hierarchical dependency injection resolve services a... | ElementInjector, EnvironmentInjector, Hierarchical DI |
| How do useClass, useExisting, useFactory, and useValue differ ... | useClass, useFactory, useValue |
| The advantages of modern inject() and what rules govern the In... | inject(), Injection context, runInInjectionContext |
| How do Reactive Forms and Template-Driven Forms compare in arc... | FormControl, FormGroup, Typed forms |
| Implement dynamic field arrays and custom async validators in ... | FormArray, AsyncValidatorFn, Validation debouncing |
| Implement lazy loading for standalone components versus route ... | loadComponent, Code splitting, Standalone component |
| How do modern functional route guards work and why should they... | CanActivateFn, UrlTree, Atomic navigation |
| Use a ResolveFn versus ingesting state directly via Signal ser... | ResolveFn, Signal service ingestion, Perceived performance |
| How do functional HTTP interceptors work and why is request cl... | HttpInterceptorFn, Request cloning, Authorization header |
| Implement silent JWT refresh and request queueing for 401 errors | Silent refresh, 401 Unauthorized, Concurrency lock |
| The root causes of memory leaks in Angular and how do you prof... | Memory leak, Detached DOM tree, Heap snapshot |
| How do modern teardown patterns like takeUntilDestroyed compar... | takeUntilDestroyed(), DestroyRef, AsyncPipe |
| Decide between Local Signals, Service Signals, NgRx SignalStor... | Local Signals, Shared Signal Service, NgRx SignalStore |
| The anatomy and features of modern NgRx SignalStore. | signalStore(), withState(), withComputed() |
| How do Deferrable Views work under the hood and what are their... | @defer, on viewport, on idle |
| The top performance optimization techniques for enterprise Ang... | OnPush change detection, track expression, NgOptimizedImage |
| Implement centralized global error handling and telemetry in A... | ErrorHandler, handleError(), Centralized logging |
| Angular protect against Cross-Site Scripting (XSS) and when sh... | DomSanitizer, Security context, XSS protection |
| Non-Destructive Hydration work in modern Angular Server-Side R... | provideClientHydration(), Non-destructive hydration, DOM flickering |
| How do take(1), first(), and single() differ, and why is share... | take(1), first(), refCount |
| Migrate enterprise Angular applications from NgModules to Stan... | Standalone component, Built-in control flow, Automated schematic |
| Build a high-throughput e-commerce cart and live pricing engin... | Push-pull graph, Glitch-free evaluation, computed() |
| Implement a typeahead search catalog preventing race condition... | switchMap, debounceTime, Inner catchError |
| Prevent detached DOM tree memory leaks when displaying high-fr... | Detached DOM tree, takeUntilDestroyed(), DestroyRef |
| Achieve 60 FPS performance for high-frequency real-time update... | NgZone.runOutsideAngular(), 60 FPS rendering, OnPush change detection |
| Implement silent JWT token refresh and atomic route guarding i... | HttpInterceptorFn, Silent refresh, Concurrency lock |
| Design an enterprise state management architecture using NgRx ... | signalStore(), withState(), withComputed() |
| Build a real-time polling dashboard widget with clean teardown... | timer(), switchMap, takeUntilDestroyed() |
| Angular Architectural Evolution (v14 to v18+) | (core terms pending) |
| Angular Signals & Zoneless Change Detection | (core terms pending) |
| RxJS Concurrency & Flattening Strategies | (core terms pending) |
| Memory Leak Prevention & Teardown Architecture | (core terms pending) |
| Change Detection Optimization: OnPush & NgZone Escaping | (core terms pending) |
| Functional Interceptors & Modern Route Guards | (core terms pending) |
| Enterprise State Management with NgRx SignalStore | (core terms pending) |
| The exact difference between signal, computed, and effect | Signal, Computed, Effect |
| Mutating a Signal array directly with push an anti-pattern | Object.is, Immutable update, Update method |
| The purpose of untracked inside an effect or computed signal | untracked, Reactive context, Circular dependency |
| Deferrable Views (@defer) and their trigger conditions. | @defer, on viewport, on idle |
| How do forkJoin and combineLatest differ in execution and emis... | forkJoin, combineLatest, Stream completion |
| BehaviorSubject and ReplaySubject(1) | BehaviorSubject, ReplaySubject, Seed value |
| What causes ExpressionChangedAfterItHasBeenCheckedError and ho... | ExpressionChangedAfterItHasBeenCheckedError, Verification digest, Unidirectional data flow |
| ViewChild static true and static false | static, static, Conditional DOM |
| The modern @for block outperform *ngFor with trackBy | @for block, track expression, @empty block |
| Implement global error handling in Angular | ErrorHandler, handleError method, Logging service |
| The difference between Renderer2 and direct ElementRef.nativeE... | Renderer2, Server-side rendering (SSR), DOM abstraction layer |
| Tree-Shaking work for Angular Services | providedIn, Dead-code elimination, Static analysis |
| Content Projection and how does Multi-Slot Projection work | Content projection, <ng-content> tag, Multi-slot projection |
| Subject and BehaviorSubject | Subject, BehaviorSubject, Initial seed value |
| Angular protect against Cross-Site Scripting (XSS) and when sh... | DomSanitizer, XSS protection, Security context |
| Non-Destructive Hydration in modern Angular Server-Side Rendering | Non-destructive hydration, DOM recycling, Largest Contentful Paint (LCP) |
| The purpose of runInInjectionContext in modern Angular | runInInjectionContext, Injection context, EnvironmentInjector |
| Take(1) and first() in RxJS | take(1), First operator, EmptyError exception |
| Host property bindings vs @HostBinding and @HostListener. | Host property binding, @HostBinding, @HostListener |
| Component input transforms like booleanAttribute and numberAtt... | Input transforms, booleanAttribute, numberAttribute |
| Router.navigate and router.navigateByUrl | router.navigate, router.navigateByUrl, UrlTree |
| ShareReplay(1) dangerous without refCount true | shareReplay(1), refCount, Subscription retention |
| Handle Route Resolvers in modern Angular | ResolveFn, Route transition delay, Skeleton screen |
| The purpose of NgOptimizedImage (ngSrc) and what optimizations... | NgOptimizedImage, Cumulative Layout Shift (CLS), priority attribute |
| How do Angular Signals handle circular dependency loops | Circular dependency, Directed Acyclic Graph (DAG), NG0600 error |
| How do switchMap, mergeMap, concatMap, and exhaustMap differ i... | switchMap, mergeMap, concatMap |
| A microservices architecture, and how does it differ from a mo... | Monolith, Microservices, Bounded context |
| Why must each microservice have its own private database | Database-per-service, Schema evolution, Polyglot persistence |
| Two-Phase Commit (2PC) usually avoided in distributed systems | Two-Phase Commit, Latency amplification, Eventual consistency |
| The Saga pattern, and what is the difference between choreogra... | Saga, Orchestration, Choreography |
| A compensating transaction, and how does it differ from a data... | Compensating transaction, Database rollback, Semantic undo |
| The dual-write problem, and why does it risk data inconsistency | Dual-write problem, Partial failure, Phantom event |
| The Transactional Outbox pattern, and how does it prevent lost... | Transactional outbox, Change Data Capture, At-least-once delivery |
| An idempotent consumer, and why is message deduplication required | Idempotent consumer, At-least-once delivery, Deduplication inbox |
| CQRS (Command Query Responsibility Segregation) | CQRS, Command, Query |
| An API Gateway, and why do microservices place one at the netw... | API gateway, Reverse proxy, Cross-cutting concerns |
| Why do internal microservices use gRPC instead of REST | gRPC, Protocol Buffers, HTTP/2 multiplexing |
| The Circuit Breaker pattern, and what are its three operationa... | Circuit breaker, Closed state, Open state |
| Distributed tracing, and how does OpenTelemetry trace requests... | Distributed tracing, Trace ID, Span ID |
| An end-to-end checkout flow handle inventory, payment, and fai... | Saga orchestrator, Compensating transaction, Semantic state |
| When should an enterprise break a monolith into microservices,... | Modular monolith, Database-per-service, Bounded context |
| Choose between synchronous REST, gRPC, and asynchronous event-... | Protocol Buffers, HTTP/2 multiplexing, At-least-once delivery |
| Coordinate distributed transactions across microservices witho... | Saga pattern, Saga orchestration, Compensating transaction |
| The Transactional Outbox pattern, and how does Change Data Cap... | Transactional outbox, Dual-write problem, Change Data Capture |
| Guarantee distributed idempotency across multiple API instance... | Idempotency key, Inbox pattern, Atomic cache check |
| Design an API Gateway layer for routing, auth offload, and rat... | YARP, Authentication offload, Rate limiting |
| Implement resilience pipelines with Polly v8 circuit breakers ... | Polly resilience pipeline, Exponential backoff with jitter, Circuit breaker |
| Architect CQRS and MediatR pipeline behaviors in .NET to segre... | CQRS, MediatR pipeline behavior, FluentValidation |
| Implement end-to-end distributed tracing across microservices ... | OpenTelemetry, W3C Trace Context, Span |
| Complete Production Checkout Saga Orchestrator (C#) | (core terms pending) |
| Complete Polly v8 Enterprise Resilience Pipeline Builder (C#) | (core terms pending) |
| Production Redis Lua Script for Atomic Inventory Reservation | (core terms pending) |
| Design distributed data persistence and solve the database-per... | Database-per-service, Bounded context, Eventual consistency |
| Prevent data loss from the dual-write problem using the Transa... | Transactional outbox, Dual-write problem, Change Data Capture |
| Design an idempotent consumer to guarantee deduplication in ev... | Idempotent consumer, Inbox pattern, At-least-once delivery |
| Architect CQRS and MediatR pipelines in .NET for high-throughp... | CQRS, MediatR pipeline behavior, Materialized read view |
| Configure API Gateways and choose between internal gRPC and ex... | YARP, Protocol Buffers, HTTP/2 multiplexing |
| Design resilience pipelines using Polly v8 circuit breakers an... | Polly v8 Resilience Pipeline, Circuit breaker, Exponential backoff with jitter |
| Implement distributed tracing and observability using OpenTele... | Distributed tracing, W3C Trace Context, Span |
| Design an end-to-end high-scale e-commerce checkout and paymen... | High-Level Design, Atomic decrement, Saga orchestrator |
| Implement a low-level design for a checkout Saga orchestrator ... | State machine, Compensating transaction, Durable state store |
| Defend a senior distributed system design under interview cros... | Architectural trade-off, CAP theorem, Failure mode analysis |
| Pitching Concurrency in Interviews: The Problem-Solver Mindset | Financial correctness, Race condition, Idempotency |
| The Classic lock(obj) Trap in Asynchronous C# | Thread affinity, Compiler error CS1996, SemaphoreSlim.WaitAsync() |
| Keyed In-Process Async Locking (Entity-Level Synchronization) | Keyed in-process locking, Entity-level synchronization, Throughput scalability |
| Distributed Race Conditions: Why In-Process Locks Fail Across ... | Process isolation, Horizontal scaling, Distributed race condition |
| Distributed Lock 1: Azure Blob Lease | Azure Blob Lease, Lease duration, HTTP 412 Precondition Failed |
| Distributed Lock 2: Redis Redlock Algorithm | Redis Redlock, SET NX PX, Atomic Lua script |
| Distributed Lock 3: SQL Server Application Locks (sp_getapplock) | sp_getapplock, Application lock, Lock timeout |
| Message Brokers: Out-of-Order Message Processing & FIFO Sessions | Message sessions, SessionId, Strict FIFO order |
| Message Brokers: At-Least-Once Delivery & Duplicate Messages | At-least-once delivery, Idempotent consumer, Deduplication table |
| Message Brokers: The Dual-Write Problem & Transactional Outbox | Dual-write problem, Transactional Outbox pattern, Atomic database transaction |
| Message Brokers: Poison Messages, Cascading Crashes & DLQs | Poison message, Dead-Letter Queue (DLQ), MaxDeliveryCount |
| Azure Cosmos DB: HTTP 429 RequestRateTooLarge & RU Throttling | RU throttling, HTTP 429 RequestRateTooLarge, RetryAfterMs |
| Azure Cosmos DB: Optimistic Concurrency Control (OCC) with ETags | Optimistic Concurrency Control (OCC), _etag token, HTTP 412 Precondition Failed |
| Azure Blob Storage: Memory Spikes & LOH Fragmentation on Uploads | LOH fragmentation, Large Object Heap (LOH), Streaming upload |
| Azure Blob Storage: Orphaned Blobs on Failed Operations | Orphaned blob, Inconsistent state, Outbox cleanup worker |
| SQL Server: Fixing Cyclic Deadlocks with UPDLOCK, ROWLOCK | Cyclic deadlock, Deadlock victim, UPDLOCK table hint |
| SQL Server: Lock Escalation from Row Lock to Table Lock | Lock escalation, Table lock, Lock contention |
| Why would you choose SemaphoreSlim instead of lock in modern C# | SemaphoreSlim.WaitAsync(), Thread affinity, Compiler error CS1996 |
| Prevent race conditions when ten pods process the same custome... | Idempotency key, Idempotent consumer, Optimistic concurrency lock |
| The Transactional Outbox Pattern and why is it needed in event... | Transactional Outbox pattern, Atomic database transaction, Outbox relay worker |
| Make an event consumer truly idempotent | Idempotent consumer, Inbox deduplication table, Unique constraint violation |
| Troubleshoot and fix Cosmos DB 429 RequestRateTooLarge errors | HTTP 429 RequestRateTooLarge, Hot physical partition, Synthetic partition key |
| Detect and fix deadlocks in SQL Server from a microservice per... | XML deadlock graph, Deadlock victim, Resource lock ordering |
| Azure Service Bus Sessions and standard Queues | Azure Service Bus Sessions, SessionId, FIFO sequence preservation |
| Prevent a memory leak when using ConcurrentDictionary for keye... | Semaphore memory leak, Reference-counted semaphores, Conditional dictionary removal |
| When would you use an Azure Blob Lease as a distributed lock i... | Azure Blob Lease, Coarse-grained distributed locks, Redis Redlock |
| How Cosmos DB Change Feed handles consumer concurrency across ... | Change Feed Processor, Lease container, Continuation token |
| Implement distributed transactions across microservices withou... | Saga pattern, Saga orchestrator, Compensating transactions |
| Handle database connection drops or failovers during an active... | Execution strategy, EnableRetryOnFailure, ExecuteAsync delegate |
| Implement backpressure in a high-throughput event consumer | Backpressure, Bounded channel, Prefetch count |
| Pessimistic Locking and Optimistic Locking, and when do you ch... | Pessimistic locking, Optimistic Concurrency Control (OCC), rowversion |
| Debug a production distributed race condition that only appear... | Distributed race condition, OpenTelemetry distributed tracing, Extended Events deadlock graph |
| `async` / `await` Under the Hood: Does it Create a New Thread?... | Non-blocking I/O, I/O Completion Ports (IOCP), IAsyncStateMachine |
| Sync-over-Async Anti-Pattern: Why `.Result` and `.Wait()` Caus... | Sync-over-async, ThreadPool starvation, SynchronizationContext |
| In-Process Locking: `lock` (Monitor) vs. `SemaphoreSlim` (Why ... | Thread affinity, SynchronizationLockException, SemaphoreSlim |
| Task Execution Mechanics: `Task.Run` vs. `Task.Factory.StartNe... | Task.Run, Task.WhenAll, Async concurrency |
| Low-Level Thread-Safe Primitives: `Interlocked` Atomic Operati... | Interlocked, Volatile, Lock-free programming |
| Deadlock Prevention & Resolution: Resource Ordering, Lock Time... | Deadlock, Resource ordering, Lock timeout |
| High-Throughput Producer-Consumer Pipelines: Bounded `Channel<... | Channel<T>, Backpressure, Bounded capacity |
| Distributed Locking Across Horizontal Pods: Redis (`StringSetA... | Distributed lock, Redlock, Fencing token |
| The Classic `lock (obj)` Trap in Asynchronous C# | Thread affinity, SynchronizationLockException, SemaphoreSlim |
| Keyed In-Process Async Locking (Entity-Level Synchronization) | Keyed async locking, Striped locking, Reference counting |
| 🎯 Simple Use Cases & "When to Use What" Decision Guide: In-Pro... | Distributed race condition, Distributed lock, Fencing token |
| Distributed Lock Solution 1: Azure Blob Lease | Azure Blob Lease, HTTP 409 Conflict, Leader election |
| Distributed Lock Solution 2: Redis Redlock Algorithm | Redlock, Quorum, Drift time |
| SQL Server Application Locks (`sp_getapplock`) | sp_getapplock, Transaction-scoped lock, Lock owner |
| 🎯 Simple Use Cases & "When to Use What" Decision Guide: Distri... | (core terms pending) |
| Bug 1: Out-of-Order Message Processing | Message reordering, Service Bus Sessions, State machine validation |
| Bug 2: At-Least-Once Delivery & Duplicate Message Processing | At-least-once delivery, Idempotent consumer, Deduplication table |
| Bug 3: The Dual-Write Problem (DB Update vs Broker Publish) | Dual-write problem, Transactional outbox, Outbox publisher |
| Bug 4: Poison Messages & Cascading Consumer Crashes | Poison message, Dead-letter queue (DLQ), Exponential backoff |
| 🎯 Simple Use Cases & "When to Use What" Decision Guide: Messag... | (core terms pending) |
| HTTP 429: RequestRateTooLarge (RU Saturation) | Request Units (RUs), Partition key hot spotting, Retry-After header |
| Optimistic Concurrency Control (OCC) with ETags | Optimistic Concurrency Control (OCC), ETag, AccessCondition |
| Memory Spikes & LOH Fragmentation on Large Uploads | Large Object Heap (LOH), LOH fragmentation, ArrayPool<T> |
| Orphaned Blobs on Failed Operations | Orphaned blob, Staging prefix, Blob Lifecycle Management |
| Fixing Cyclic Deadlocks with `UPDLOCK, ROWLOCK` | Cyclic deadlock, UPDLOCK, ROWLOCK |
| Lock Escalation from Row Lock to Table Lock | Lock escalation, Escalation threshold, Batching updates |
| Why would you choose `SemaphoreSlim` instead of `lock` in mode... | SemaphoreSlim, Thread affinity, SynchronizationLockException |
| Prevent a distributed race condition when 10 Kubernetes pods p... | Distributed lock, Idempotency key, Fencing token |
| The Transactional Outbox Pattern and what exact problem does i... | Transactional outbox pattern, Dual-write problem, Outbox processor |
| Make an event consumer truly idempotent | Idempotent consumer, Deduplication key, Natural idempotency |
| How did you troubleshoot and resolve Cosmos DB 429 errors in p... | Request Units (RUs), Hot partition, Diagnostic logs |
| Detect and fix deadlocks in SQL Server from a microservice per... | Deadlock graph, Resource ordering, UPDLOCK |
| Azure Service Bus Sessions and standard Queues | Service Bus Sessions, Session lock, FIFO processing |
| Prevent a memory leak when using `ConcurrentDictionary<string,... | Keyed lock memory leak, Reference counting, RefCountedSemaphore |
| When would you use an Azure Blob Lease as a distributed lock i... | Azure Blob Lease, Leader election, Coarse-grained locking |
| How Cosmos DB Change Feed handles consumer concurrency. | Change Feed, Change Feed Processor (CFP), Lease container |
| Implement distributed transactions across microservices withou... | Saga pattern, Compensating transaction, Saga orchestrator |
| Handle database connection drops or failovers during an active... | Execution strategy, Transient error, Idempotent transaction |
| Implement backpressure in a high-throughput event consumer to ... | Backpressure, PrefetchCount, Bounded Channel |
| Pessimistic Locking (`UPDLOCK` / `SELECT FOR UPDATE`) and Opti... | Optimistic locking, Pessimistic locking, Rowversion |
| Debug a production distributed race condition that only reprod... | Distributed race condition, Distributed tracing, OpenTelemetry |
| The Classic `lock (obj)` Trap in Asynchronous C# | Thread affinity, SemaphoreSlim, SynchronizationLockException |
| Keyed In-Process Async Locking (Entity-Level Synchronization) | Keyed async locking, ConcurrentDictionary, Reference counting |
| Distributed Lock Solution 1: Azure Blob Lease | Azure Blob Lease, Leader election, Lease renewal heartbeat |
| Distributed Lock Solution 2: Redis Redlock Algorithm | Redis Redlock, Time-to-live (TTL), Watchdog timer |
| SQL Server Application Locks (`sp_getapplock`) | sp_getapplock, Transaction-scoped lock, Lock timeout |
| Bug 1: Out-of-Order Message Processing | Out-of-order delivery, Message sessions, Optimistic sequence versioning |
| Bug 2: At-Least-Once Delivery & Duplicate Message Processing | At-least-once delivery, Idempotent consumer, Inbox pattern |
| Bug 3: The Dual-Write Problem (DB Update vs Broker Publish) | Dual-write problem, Transactional outbox, Outbox publisher |
| Bug 4: Poison Messages & Cascading Consumer Crashes | Poison message, Dead-letter queue (DLQ), Circuit breaker |
| HTTP 429: RequestRateTooLarge (RU Saturation) | Request Units (RU/s), HTTP 429, Partition key hotspot |
| Optimistic Concurrency Control (OCC) with ETags | Optimistic Concurrency Control (OCC), ETag header, HTTP 412 Precondition Failed |
| Memory Spikes & LOH Fragmentation on Large Uploads | Large Object Heap (LOH), ArrayPool, Streaming upload |
| Orphaned Blobs on Failed Operations | Orphaned blobs, Two-phase blob commit, Blob lifecycle management |
| Fixing Cyclic Deadlocks with `UPDLOCK, ROWLOCK` | UPDLOCK, Cyclic deadlock, Lock conversion deadlock |
| Lock Escalation from Row Lock to Table Lock | Lock escalation, Batch chunking, Lock escalation threshold |
| Why would you choose `SemaphoreSlim` instead of `lock` in mode... | SemaphoreSlim, Thread affinity, SynchronizationLockException |
| Prevent a distributed race condition when 10 Kubernetes pods p... | Distributed mutual exclusion, Idempotency key, Fencing token |
| The Transactional Outbox Pattern and what exact problem does i... | Transactional outbox, Dual-write problem, Outbox publisher |
| Make an event consumer truly idempotent | Idempotent consumer, Inbox pattern, Unique constraint |
| How did you troubleshoot and resolve Cosmos DB 429 errors in p... | HTTP 429, Partition key hotspot, Request Units (RU/s) |
| Detect and fix deadlocks in SQL Server from a microservice per... | Cyclic deadlock, system_health session, UPDLOCK |
| Azure Service Bus Sessions and standard Queues | Message sessions, SessionId, Session lock |
| Prevent a memory leak when using `ConcurrentDictionary<string,... | ConcurrentDictionary, Reference counting, Gen 2 memory leak |
| When would you use an Azure Blob Lease as a distributed lock i... | Azure Blob Lease, Leader election, Coarse-grained locking |
| How Cosmos DB Change Feed handles consumer concurrency. | Lease container, Continuation token, Partition rebalancing |
| Implement distributed transactions across microservices withou... | Saga pattern, Compensating transaction, Saga orchestration |
| Handle database connection drops or failovers during an active... | Execution strategy, Transient SQL error, Idempotent transaction |
| Implement backpressure in a high-throughput event consumer to ... | Consumer backpressure, Bounded channel, Prefetch count |
| Pessimistic Locking (`UPDLOCK` / `SELECT FOR UPDATE`) and Opti... | Pessimistic locking, Optimistic Concurrency Control (OCC), rowversion |
| Debug a production distributed race condition that only reprod... | Distributed tracing, Deadlock XML graph, Load testing harness |
| Authentication and Authorization | Authentication, Authorization, HTTP 403 Forbidden |
| OAuth 2.0, OpenID Connect (OIDC), and JWT | OAuth 2.0, OpenID Connect, JSON Web Token (JWT) |
| Inside a JSON Web Token (JWT) and how does the server verify it | JSON Web Token (JWT), Payload claims, Digital signature |
| Symmetric (HS256) and Asymmetric (RS256) signing | RS256, HS256, JSON Web Key Set (JWKS) |
| Handle instant logout or token revocation with stateless JWTs | Token revocation, Refresh token, Redis blacklist |
| Cross-Origin Resource Sharing (CORS) and why do browsers block... | CORS, Same-Origin Policy, Preflight OPTIONS request |
| SQL Injection and Cross-Site Scripting (XSS), and how do you p... | Parameterized query, Cross-Site Scripting (XSS), Context-aware encoding |
| Unit Testing and Integration Testing with WebApplicationFactory | WebApplicationFactory, Testcontainers, Mocking frameworks |
| Docker and why should you use Multi-Stage Docker builds | Multi-Stage Build, Hardened runtime image, Non-root user |
| Kubernetes Liveness and Readiness Probes | Liveness Probe, Readiness Probe, Cascading reboot storm |
| Blue-Green Deployment and Canary Deployment | Blue-Green Deployment, Canary Deployment, Blast radius |
| Authentication and Authorization in ASP.NET Core Web API? Expl... | Authentication, ClaimsPrincipal, ClockSkew |
| Role-Based vs Claims-Based vs Policy-Based Authorization in .N... | Policy-based authorization, IAuthorizationRequirement, AuthorizationHandler |
| Broken Object-Level Authorization (BOLA / IDOR) and Mass Assig... | BOLA, Tenant isolation, DTO |
| Protect ASP.NET Core APIs against SQL Injection (SQLi), Cross-... | SQL injection, Parameterized query, Cross-Site Scripting (XSS) |
| CORS (Cross-Origin Resource Sharing)? Why does the browser tri... | Same-Origin Policy, Preflight OPTIONS, Access-Control-Allow-Origin |
| Manage application secrets in modern .NET? Explain User Secret... | User Secrets, Azure Key Vault, Managed Identity |
| The Testing Pyramid in .NET. When do you write Unit Tests with... | Testing Pyramid, Unit tests, WebApplicationFactory |
| The architecture of a Production Multi-Stage Dockerfile for AS... | Multi-stage build, Non-root user, Chiseled runtime |
| Walk me through an enterprise CI/CD Pipeline for .NET APIs usi... | CI/CD pipeline, SonarQube quality gate, Deployment stages |
| Core Kubernetes fundamentals for .NET developers: Pods vs Depl... | Pod, Kubernetes Deployment, Ingress controller |
| OAuth2 vs. OpenID Connect (OIDC) vs. JWT | OpenID Connect, OAuth2, JSON Web Token |
| The ASP.NET Core Authentication Pipeline Sequence | (core terms pending) |
| Symmetric (HS256) vs. Asymmetric (RS256) Signing | (core terms pending) |
| Stateless JWT Revocation (Handling Instant Logout & Banned Users) | (core terms pending) |
| Proof Key for Code Exchange (PKCE) for Single Page Application... | PKCE, Public client, Code verifier |
| Web Vulnerability Defenses: CORS, SQL Injection (SQLi) & XSS | Cross-Origin Resource Sharing, SQL injection, Cross-Site Scripting |
| Integration Testing with `WebApplicationFactory<Program>` & Te... | WebApplicationFactory, Testcontainers, Dialect fidelity |
| Eliminating Test Flakiness & Concurrency Bugs in xUnit | (core terms pending) |
| Production Multi-Stage Dockerfile for .NET Core API | Multi-stage build, Docker layer caching, Non-root execution |
| Kubernetes Health Probes: Liveness vs. Readiness | Liveness probe, Readiness probe, Cascading restart storm |
| CI/CD Deployment Strategies: Blue-Green, Canary & Feature Toggles | Blue-green deployment, Canary release, Feature flags |
| The .NET Generational Garbage Collector work | Generational hypothesis, Ephemeral generations, Large Object Heap (LOH) |
| Server GC vs. Workstation GC & Kubernetes OOMKilled | Server GC, Workstation GC, OOMKilled (Exit Code 137) |
| Memory Layout of an Object on the 64-bit CLR Heap | Object Header, MethodTable Pointer, 8-byte memory alignment |
| `ArrayPool<T>` and Why Forgetting to Return Causes Leaks | ArrayPool<T>, Power-of-two bucketing, clearArray |
| `Span<T>` and `Memory<T>`: Why is Span a `ref struct` | Span<T>, ref struct, Memory<T> |
| Why `.GetAwaiter().GetResult()` Causes Thread Pool Starvation | Sync-over-async, ThreadPool starvation, Thread injection rate |
| `IAsyncEnumerable<T>` vs. `Task<IEnumerable<T>>` | IAsyncEnumerable<T>, Asynchronous streaming, Pull-based backpressure |
| The 3 Cardinal Rules of `ValueTask<T>` | ValueTask<T>, Single-await constraint, Synchronous completion |
| Why `lock (obj)` is Illegal in Async Methods | Compiler error CS1996, Thread affinity, SemaphoreSlim.WaitAsync() |
| `System.Threading.Channels` vs. `BlockingCollection<T>` | System.Threading.Channels, Producer-consumer pattern, Bounded channel |
| Captive Dependencies in ASP.NET Core DI | Captive dependency, IServiceScopeFactory, Manual scope creation |
| Middleware vs. Action Filters vs. Resource Filters Execution O... | Middleware, Resource Filters, Action Filters |
| `IHttpClientFactory` Handler Rotation vs. Socket Exhaustion | IHttpClientFactory, Socket exhaustion, Pooled handler rotation |
| The 4 Built-In Rate Limiting Algorithms in .NET 7/8 | Rate limiting, Sliding window algorithm, Token bucket algorithm |
| `IEnumerable<T>` vs. `IQueryable<T>` in LINQ | IQueryable<T>, Expression tree, Server-side evaluation |
| Cartesian Explosion in EF Core & Split Queries | Cartesian explosion, AsSplitQuery, Eager loading (.Include) |
| `AsNoTracking()` vs. `AsNoTrackingWithIdentityResolution()` | AsNoTracking, Snapshot cloning, AsNoTrackingWithIdentityResolution |
| Global Query Filters for Soft Deletes and Multi-Tenancy | Global Query Filters, Soft delete filtering, Multi-tenant isolation |
| Result Pattern vs. Throwing Exceptions for Business Validation | Result pattern, Exception stack unwinding, Typed domain error |
| Finding the Nth Highest Salary (`DENSE_RANK` vs. `RANK`) | DENSE_RANK(), RANK(), Window ranking function |
| Deleting Duplicate Records While Keeping the Lowest ID | ROW_NUMBER(), PARTITION BY duplicate columns, CTE deletion |
| Calculating Running Total (Cumulative Balance) Partitioned by ... | SUM() OVER(), PARTITION BY customer ID, ORDER BY transaction date |
| Finding Users with 3 or More Consecutive Login Days | DATEADD grouping, Gaps and Islands problem, HAVING COUNT filter |
| Recursive CTE for Organizational Reporting Hierarchy | Recursive CTE, Anchor member, UNION ALL recursion |
| Physical 8KB Page Architecture & Random GUID Clustered Keys | 8KB data page, Page split, Index fragmentation |
| Key Lookup Elimination via Covering Indexes (`INCLUDE`) | Covering index, Key lookup, INCLUDE clause |
| `FILLFACTOR`: When to Set to 80% or 90% Instead of 100% | FILLFACTOR, FILLFACTOR 80 to 90 percent, Leaf page free space |
| Index Reorganize vs. Index Rebuild | Index reorganize, Index rebuild, Online rebuild (ONLINE = ON) |
| Non-SARGable Queries (`YEAR(CreatedDate) = 2026`) | Non-SARGable query, Index seek, SARGable range predicate |
| Parameter Sniffing Diagnosis & 4 Remedies | Parameter sniffing, OPTIMIZE FOR UNKNOWN, OPTION (RECOMPILE) |
| Diagnosing High-CPU, Missing Indexes & Blocking via DMVs | Dynamic Management Views (DMVs), total_worker_time, Head blocker session |
| Cyclic Deadlocks & `WITH (UPDLOCK, ROWLOCK)` | Cyclic read-modify-write deadlock, WITH (UPDLOCK, ROWLOCK), Update Lock (U) |
| Read Committed Snapshot Isolation (RCSI) & TempDB Overhead | Read Committed Snapshot Isolation (RCSI), TempDB version store, 14-byte row pointer |
| Lock Escalation Threshold (~5,000 Locks) & Chunking | Lock escalation, Coarse-grained table lock, Batch chunking |
| Key-Range Locking in `SERIALIZABLE` Isolation | Key-range locking, Phantom reads, SERIALIZABLE isolation |
| How the .NET Generational Garbage Collector works. What trigge... | Generational hypothesis, Ephemeral generations, Large Object Heap (LOH) |
| Server GC and Workstation GC? Why does a .NET Core API running... | Server GC, Workstation GC, OOMKilled (Exit Code 137) |
| The memory layout of an object on the 64-bit CLR managed heap.... | Object Header, MethodTable Pointer, 8-byte alignment |
| `ArrayPool<T>` and `MemoryPool<T>`. Why does forgetting to ret... | ArrayPool, Silent pool leak, Data bleed |
| `Span<T>` and `Memory<T>`? Why is `Span<T>` declared as a `ref... | Span<T>, ref struct, Memory<T> |
| What happens under the hood when a developer writes `.GetAwait... | Sync-over-async, ThreadPool starvation, Hill climbing algorithm |
| `IAsyncEnumerable<T>` vs `Task<IEnumerable<T>>`. In what real-... | IAsyncEnumerable<T>, Chunked transfer encoding, EnumeratorCancellation |
| The 3 cardinal rules of using `ValueTask<T>` instead of `Task<... | ValueTask<T>, IValueTaskSource<T>, Single-await rule |
| `lock (obj)` illegal inside an asynchronous method in C#? What... | Thread affinity, SynchronizationLockException, SemaphoreSlim |
| `System.Threading.Channels` (`Channel<T>`). Why is it vastly s... | Channel<T>, BlockingCollection<T>, Bounded channel backpressure |
| A Captive Dependency? How does it cause silent data corruption... | Captive dependency, Scoped lifetime, ValidateScopes |
| The execution order of Middleware vs Action Filters vs Resourc... | Middleware pipeline, Resource filters, Action filters |
| `IHttpClientFactory` message handler rotation. Why does `new H... | IHttpClientFactory, Socket exhaustion, DNS staleness |
| The 4 Built-In Rate Limiting Algorithms in .NET 7/8 (`System.T... | Token bucket, Sliding window, Concurrency limiter |
| `IEnumerable<T>` vs `IQueryable<T>` in LINQ. Show an exact pro... | IQueryable<T>, IEnumerable<T>, Expression tree |
| Cartesian Explosion in EF Core? How do Split Queries solve it,... | Cartesian explosion, AsSplitQuery, AsSingleQuery |
| `AsNoTracking()` and `AsNoTrackingWithIdentityResolution()` in... | AsNoTracking, AsNoTrackingWithIdentityResolution, Change tracker |
| Implement Soft Deletes and Multi-Tenancy globally in EF Core w... | Global query filters, Soft delete, IgnoreQueryFilters |
| Why does throwing exceptions for business validation severely ... | Result pattern, Stack frame unwinding, Domain validation |
| Write a query to find the Nth Highest Salary from the Employee... | DENSE_RANK, RANK, Common Table Expression (CTE) |
| Write a query to identify and delete duplicate records from a ... | ROW_NUMBER, PARTITION BY, CTE deletion |
| Calculate the Running Total (Cumulative Balance) of Account Tr... | Running total, ROWS BETWEEN frame, RANGE framing |
| Find Users who logged into the application for 3 or more conse... | Gaps and islands, Date subtraction technique, Constant island key |
| Write a Recursive Common Table Expression (CTE) to display an ... | Recursive CTE, Anchor member, Recursive member |
| The physical architecture of an 8KB data page. What happens wh... | 8KB data page, Page split, NEWSEQUENTIALID |
| A Key Lookup in an Execution Plan? How do you eliminate it wit... | Key lookup, Covering index, INCLUDE clause |
| `FILLFACTOR`? When should you set it to 80% or 90% instead of ... | FILLFACTOR, Page split, Buffer pool density |
| Index Reorganize vs Index Rebuild: When should you choose whic... | Index reorganize, Index rebuild, Logical fragmentation |
| Why `WHERE YEAR(CreatedDate) = 2026` is Non-SARGable. How does... | SARGable query, Index seek, Clustered index scan |
| Parameter Sniffing? How do you diagnose it, and what are the 4... | Parameter sniffing, OPTIMIZE FOR UNKNOWN, OPTION (RECOMPILE) |
| Identify high-CPU queries, missing indexes, and active blockin... | Dynamic Management Views (DMVs), sys.dm_exec_query_stats, sys.dm_exec_requests |
| How a Cyclic Read-Modify-Write Deadlock occurs. How does `WITH... | Deadlock, UPDLOCK hint, Deadlock victim |
| Read Committed Snapshot Isolation (RCSI). How does it eliminat... | Read Committed Snapshot Isolation (RCSI), TempDB version store, PAGELATCH_UP contention |
| Lock Escalation? At what threshold does it happen, and how do ... | Lock escalation, 5,000 lock threshold, Chunked batch deletion |
| Key-Range Locking in `SERIALIZABLE` isolation. What is the dif... | Key-range locking, Phantom read, RangeS-S lock |
| How the .NET Generational Garbage Collector works. What trigge... | Generational hypothesis, Large Object Heap, LOH fragmentation |
| Server GC and Workstation GC? Why does a .NET Core API running... | Server GC, Workstation GC, Background GC |
| The memory layout of an object on the 64-bit CLR managed heap.... | Object header, MethodTable pointer, SyncBlock |
| `ArrayPool<T>` and `MemoryPool<T>`. Why does forgetting to ret... | ArrayPool, Buffer leak, Dirty buffer |
| `Span<T>` and `Memory<T>`? Why is `Span<T>` declared as a `ref... | Span<T>, ref struct, Memory<T> |
| What happens under the hood when a developer writes `.GetAwait... | IAsyncStateMachine, Non-blocking I/O, Task.Delay |
| `IAsyncEnumerable<T>` vs `Task<IEnumerable<T>>`. In what real-... | IAsyncEnumerable, First-Byte Latency, Backpressure |
| The 3 cardinal rules of using `ValueTask<T>` instead of `Task<... | ValueTask, Task<T>, IValueTaskSource |
| `lock (obj)` illegal inside an asynchronous method in C#? What... | SemaphoreSlim, Thread affinity, CS1996 |
| `System.Threading.Channels` (`Channel<T>`). Why is it vastly s... | Channel<T>, BoundedChannel, Backpressure |
| A Captive Dependency? How does it cause silent data corruption... | Captive dependency, ValidateScopes, IServiceScopeFactory |
| The execution order of Middleware vs Action Filters vs Resourc... | RequestDelegate, Action filter, Endpoint routing boundary |
| `IHttpClientFactory` message handler rotation. Why does `new H... | IHttpClientFactory, Socket exhaustion, DNS stale cache bug |
| The 4 Built-In Rate Limiting Algorithms in .NET 7/8 (`System.T... | FixedWindow, SlidingWindow, TokenBucket |
| `IEnumerable<T>` vs `IQueryable<T>` in LINQ. Show an exact pro... | Expression tree, Server-side evaluation, Deferred execution |
| Cartesian Explosion in EF Core? How do Split Queries solve it,... | Cartesian explosion, Eager loading, AsSplitQuery |
| `AsNoTracking()` and `AsNoTrackingWithIdentityResolution()` in... | AsNoTracking, Snapshot cloning, AsNoTrackingWithIdentityResolution |
| Implement Soft Deletes and Multi-Tenancy globally in EF Core w... | Global query filter, Soft delete, IgnoreQueryFilters |
| Why does throwing exceptions for business validation severely ... | Result pattern, Stack unwinding, Two-track execution |
| Write a query to find the Nth Highest Salary from the Employee... | CTE, DENSE_RANK, Window function |
| Write a query to identify and delete duplicate records from a ... | CTE, ROW_NUMBER, PARTITION BY |
| Calculate the Running Total (Cumulative Balance) of Account Tr... | Running total, RANGE BETWEEN, ROWS BETWEEN |
| Find Users who logged into the application for 3 or more conse... | Gaps-and-Islands, DENSE_RANK, DATEADD |
| Write a Recursive Common Table Expression (CTE) to display an ... | Recursive CTE, Anchor member, Recursive member |
| The physical architecture of an 8KB data page. What happens wh... | B-tree index, Leaf page, Forwarding record |
| A Key Lookup in an Execution Plan? How do you eliminate it wit... | Key lookup, Covering index, INCLUDE clause |
| `FILLFACTOR`? When should you set it to 80% or 90% instead of ... | Page split, Index fragmentation, FILLFACTOR |
| Index Reorganize vs Index Rebuild: When should you choose whic... | Index Reorganize, Index Rebuild, Schema lock |
| Why `WHERE YEAR(CreatedDate) = 2026` is Non-SARGable. How does... | SARGable, Index seek, Index scan |
| Parameter Sniffing? How do you diagnose it, and what are the 4... | Parameter sniffing, OPTIMIZE FOR, RECOMPILE |
| Identify high-CPU queries, missing indexes, and active blockin... | Dynamic Management Views, sys.dm_exec_query_stats, sys.dm_db_missing_index_details |
| How a Cyclic Read-Modify-Write Deadlock occurs. How does `WITH... | Deadlock, Deadlock victim, Lock ordering |
| Read Committed Snapshot Isolation (RCSI). How does it eliminat... | Read Committed Snapshot Isolation, tempdb row versioning, Snapshot Isolation |
| Lock Escalation? At what threshold does it happen, and how do ... | Lock escalation, Table lock, Batch deletion |
| Key-Range Locking in `SERIALIZABLE` isolation. What is the dif... | Serializable, Phantom read, Key-range locking |

## 8. Drill method (15 min/day — active recall, not re-reading)
1. **Meaning → Term:** cover column 1, read the meaning, say the term aloud.
2. **Question → Terms:** cover the right column of §7, read the question, list terms from memory.
3. **Term → Sentence:** pick a term, say a full sentence using it (column 3 models this).
4. Anything you miss goes on tomorrow's repeat list. That's spaced repetition.
