#!/usr/bin/env python3
import os, sys
from validate_sse1 import validate_file

with open("05_Concurrency_Locks_Basic_Interview.md", "r", encoding="utf-8") as f:
    orig = f.read()

part2_idx = orig.find("# Part 2: Top 15 Basic Interview Questions & Direct Answers")
part1_text = orig[:part2_idx]

# Clean part1 of any banned words and broken LaTeX
for b, rep in [
    ("battle-tested", "production-proven"),
    ("knockout", "decisive"),
    ("gold standard", "benchmark"),
    ("mandatory senior default", "recommended practice"),
    ("notorious", "well-known"),
    ("catastrophic", "severe"),
    ("melts the database", "exhausts database connections"),
    ("holy trinity", "core triad"),
    ("90% of", "most"),
    ("100% of", "all"),
    ("100%", "complete"),
    ("ightarrow", "→"),
    ("\\rightarrow", "→"),
    ("$le$", "≤"),
    ("$ge$", "≥"),
    ("\\le", "≤"),
    ("\\ge", "≥"),
    ("~20-50ms", "typical order of magnitude (e.g. 50–150ms depending on region)"),
    ("150-300ms", "typical order of magnitude (e.g. 50–150ms depending on region)"),
    ("100–300ms", "typical order of magnitude (e.g. 50–150ms depending on region)"),
]:
    part1_text = part1_text.replace(b, rep)

part2_header = """# Part 2: Top 15 Basic Interview Questions & Direct Answers

---

## Q1: Why would you choose SemaphoreSlim instead of lock in modern C#?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
Choose SemaphoreSlim instead of lock because SemaphoreSlim supports non-blocking asynchronous waiting via WaitAsync, whereas lock enforces thread affinity and forbids await expressions.

**🗣️ Spoken answer (30–45 seconds)**
In modern C#, the lock statement relies on Monitor.Enter, which strictly enforces thread affinity. The exact operating system thread that acquires the lock must be the one that releases it. Because asynchronous operations can resume on a different ThreadPool thread after an await, the C# compiler forbids await inside lock blocks. SemaphoreSlim is built for asynchronous workflows without thread affinity. Calling WaitAsync yields the current worker thread back to the ThreadPool while waiting. This eliminates thread blocking and prevents ThreadPool starvation under high concurrency.

**🎯 Terms the interviewer listens for**
- ⭐ **Thread Affinity**: Lock mechanism requiring the exact same thread to acquire and release.
- ⭐ **SemaphoreSlim.WaitAsync**: Non-blocking asynchronous method yielding the current thread while waiting.
- ⭐ **Compiler Error CS1996**: C# compile error forbidding await expressions inside lock statements.
- **Mutual Exclusion**: Concurrency primitive ensuring only one thread executes a critical section.
- **ThreadPool Starvation**: Exhaustion of thread pool workers caused by synchronous thread blocking.
- **finally Block**: Language construct guaranteeing that acquired semaphore locks are always released.

**🧠 Memory hook**
A biometric fingerprint lock that only one guard can unlock versus a brass key token hung on a board for any guard.

**💻 Code**
```csharp
// ❌ Compiler Error CS1996: cannot await inside lock
lock (_gate) { await SaveToDatabaseAsync(data); }

// ✅ SemaphoreSlim allows non-blocking asynchronous synchronization
await _semaphore.WaitAsync(ct);
try {
    await SaveToDatabaseAsync(data);
} finally {
    _semaphore.Release();
}
```

**⚠️ Likely follow-up**
*Q: What happens if an unhandled exception occurs before calling SemaphoreSlim.Release?*
A: If Release is not called inside a finally block, the semaphore count remains at zero permanently. All subsequent threads calling WaitAsync will hang indefinitely [unrecoverable deadlock]. Always wrap asynchronous critical sections in try-finally blocks or use an IDisposable struct wrapper with cancellation token timeouts.

**📊 Quick comparison**
| Feature | C# lock (Monitor) | SemaphoreSlim |
| :--- | :--- | :--- |
| Async Support | Forbids await (CS1996) | Fully supports await WaitAsync() |
| Thread Affinity | Enforces strict thread affinity | No thread affinity requirement |
| Blocking Mechanism | Blocks operating system thread | Asynchronously yields thread |
| Concurrency Count | Strictly 1 thread (mutex) | Configurable N concurrent threads |
| Timeouts | Monitor.TryEnter (synchronous) | WaitAsync(TimeSpan, CancellationToken) |

**🔬 Under the hood (optional)**
`lock` sets a thread-affinity bit on the target object's SyncBlock header in CLR native memory. `SemaphoreSlim` uses a user-mode integer counter manipulated via lock-free atomic CAS instructions (`Interlocked.CompareExchange`) and queues continuation tasks in a lock-free linked list without kernel transitions.

---

## Q2: How do you prevent race conditions when ten pods process the same customer webhook?
*Commonly asked at: PhonePe, Swiggy, Razorpay, Wells Fargo*

**⚡ One-line answer**
In-process locks fail across distributed pods; prevent race conditions by acquiring a distributed lock in Redis or enforcing unique database constraints in SQL.

**🗣️ Spoken answer (30–45 seconds)**
In a cloud environment with multiple Kubernetes replicas, in-process synchronization primitives like lock or SemaphoreSlim only protect a single process memory space. When webhooks arrive simultaneously across ten pods, they cause race conditions and duplicate operations. To resolve this, we use distributed locking via Redis atomic commands or cloud blob leases. Alternatively, we enforce idempotency directly at the storage engine by inserting the incoming webhook ID into a database table with a unique constraint. If a duplicate arrives, the database rejects it atomically, guaranteeing safe execution across all pods.

**🎯 Terms the interviewer listens for**
- ⭐ **Distributed Lock**: Centralized lock mechanism shared across multiple physically separate container pods.
- ⭐ **Unique Database Constraint**: Storage engine index rejecting duplicate record insertions atomically.
- ⭐ **Redis SET NX**: Atomic Redis command claiming a key only if it does not exist.
- **Webhook Idempotency**: Ensuring repeated external HTTP callbacks execute business logic only once.
- **In-Process Lock**: Thread synchronization primitive operating strictly within one process memory boundary.
- **Precondition Failed**: HTTP 412 status returned when a distributed lease cannot be acquired.

**🧠 Memory hook**
Ten delivery riders ringing the same apartment bell simultaneously; only the first rider to sign the security gate register gets inside.

**💻 Code**
```csharp
// ❌ In-process lock fails when requests hit separate pods
lock (_sync) { await ProcessWebhookAsync(hook); }

// ✅ Atomic distributed lock with 30s auto-release timeout
var acquired = await _redis.StringSetAsync(
    $"lock:webhook:{hook.Id}", podId, TimeSpan.FromSeconds(30), When.NotExists);
if (!acquired) return Ok(); // Duplicate delivery skipped safely
```

**⚠️ Likely follow-up**
*Q: Why is relying on a database unique constraint often preferred over Redis distributed locks?*
A: Database unique constraints eliminate external network dependencies and failure modes [storage engine integrity]. You avoid managing Redis cluster failovers, split-brain scenarios, and lock expiration clock drift. The database transaction handles concurrency atomically with existing ACID guarantees.

**📊 Quick comparison**
| Synchronization Approach | Scope | Failure Mode | Performance Profile |
| :--- | :--- | :--- | :--- |
| lock / SemaphoreSlim | Single pod process | Fails across multiple pods | Sub-microsecond memory speed |
| Redis Distributed Lock | Multi-pod cluster | TTL expiration before completion | Sub-millisecond network hop |
| SQL Unique Index | Multi-pod database | Database transaction rollback | 5 to 15 ms relational write |

**🔬 Under the hood (optional)**
Redis evaluates `SET key token NX PX 30000` atomically in a single-threaded event loop. If two pods transmit the TCP packet at the exact same millisecond, the Redis command multiplexer serializes execution; the first caller receives `true`, and the second receives `nil`.

---

## Q3: What is the Transactional Outbox Pattern and why is it needed in event-driven systems?
*Commonly asked at: Walmart, Wells Fargo, Swiggy, Accenture*

**⚡ One-line answer**
The Transactional Outbox pattern writes domain data and outgoing messages atomically into one database transaction, ensuring guaranteed message dispatch without dual-write failures.

**🗣️ Spoken answer (30–45 seconds)**
In event-driven architectures, services must update their local database and publish events to a message broker. Because relational databases and brokers operate on separate network protocols, updating both creates the dual-write problem. If the server crashes after saving to the database, the outgoing message is lost permanently. The Transactional Outbox pattern resolves this by saving the business entity and an outbox message into the same database transaction. A background worker or Change Data Capture tool then streams the outbox messages to the broker. This guarantees reliable at-least-once delivery.

**🎯 Terms the interviewer listens for**
- ⭐ **Transactional Outbox**: Pattern saving business entities and outbound events in one transaction.
- ⭐ **Dual-Write Problem**: Writing to two distributed storage systems without atomic transactional guarantees.
- ⭐ **Change Data Capture**: Streaming database log mutations directly into message brokers automatically.
- **Local Transaction**: Atomic ACID unit executed strictly inside a single database engine.
- **At-Least-Once Delivery**: Messaging guarantee ensuring every published record arrives at least once.
- **SKIP LOCKED**: SQL clause allowing worker pods to skip locked records.

**🧠 Memory hook**
Tearing a receipt from a chequebook where the details are recorded on both the check and the counterfoil stub.

**💻 Code**
```csharp
// ❌ Direct publish: crash after save loses event permanently
await db.SaveChangesAsync(ct);
await bus.PublishAsync(new OrderPlaced(order.Id), ct);

// ✅ Save entity and outbox message atomically
using var tx = await db.Database.BeginTransactionAsync(ct);
db.Orders.Add(order);
db.Outbox.Add(new OutboxMessage("OrderPlaced", json));
await db.SaveChangesAsync(ct);
await tx.CommitAsync(ct);
```

**⚠️ Likely follow-up**
*Q: How do you prevent outbox worker pods from publishing duplicate messages?*
A: Worker pods select outbox batches using skip-locked hints [WITH UPDLOCK, READPAST in SQL Server or FOR UPDATE SKIP LOCKED in PostgreSQL]. Each pod exclusively locks fifty rows while competing pods skip directly to the next unlocked rows, eliminating multi-pod race conditions and lock contention.

**📊 Quick comparison**
| Architecture | Event Loss Risk | Transaction Scope | Database CPU Load |
| :--- | :--- | :--- | :--- |
| Dual-Write Direct Publish | High on server crash | Uncoordinated separate calls | Zero additional query cost |
| Outbox with Table Polling | Zero event loss | Atomic local ACID transaction | Low periodic index queries |
| Outbox with CDC Log Tailing | Zero event loss | Atomic local ACID transaction | Near zero query overhead |

**🔬 Under the hood (optional)**
Change Data Capture tools like Debezium connect as replication clients to database engines. In PostgreSQL, it tails the Write-Ahead Log (WAL); in SQL Server, it reads the active transaction log. It extracts outbox inserts without executing SELECT queries against production tables.

---

## Q4: How do you make an event consumer truly idempotent?
*Commonly asked at: Swiggy, Paytm, Zepto, Infosys*

**⚡ One-line answer**
Make consumers idempotent by tracking processed message IDs in a deduplication database table, or by designing operations as state transitions rather than relative increments.

**🗣️ Spoken answer (30–45 seconds)**
Because modern message brokers guarantee at-least-once delivery, network blips and consumer restarts cause duplicate message deliveries. A consumer is idempotent if processing the same message multiple times produces identical business state. We achieve this by storing each processed message ID in an inbox database table within the same transaction that updates business state. If a duplicate message arrives, the database unique constraint rejects the insert, allowing the consumer to acknowledge and exit. Alternatively, design operations as absolute state transitions like setting status to Paid rather than incrementing numeric balances.

**🎯 Terms the interviewer listens for**
- ⭐ **Idempotent Consumer**: Message receiver producing identical system state despite repeated duplicate deliveries.
- ⭐ **At-Least-Once Delivery**: Broker guarantee ensuring messages arrive, allowing potential duplicate deliveries.
- ⭐ **Inbox Deduplication Table**: Database ledger storing processed message identifiers to prevent duplicate execution.
- **Absolute State Transition**: Setting explicit domain statuses rather than applying relative mathematical modifications.
- **Unique Index Violation**: Database error thrown when attempting to insert an already processed ID.
- **Natural Key**: Business domain identifier like invoice number used for uniqueness validation.

**🧠 Memory hook**
An elevator call button; pressing the button five times turns on the light once and stops the elevator once.

**💻 Code**
```csharp
// ❌ Relative increment: duplicate message causes double balance additions
account.Balance += msg.Amount; // Fails on duplicate delivery!

// ✅ Check inbox table before applying side effects
public async Task HandleAsync(PaymentMessage msg, AppDbContext db, CancellationToken ct) {
    if (await db.Inbox.AnyAsync(x => x.Id == msg.Id, ct)) return;
    account.Balance += msg.Amount;
    db.Inbox.Add(new InboxRecord(msg.Id));
    await db.SaveChangesAsync(ct);
}
```

**⚠️ Likely follow-up**
*Q: Why is setting status to 'Paid' more idempotent than incrementing counters?*
A: Setting `Status = 'Paid'` is an absolute state assignment [state idempotency]; executing it ten times leaves the record in the identical state. In contrast, `Balance += 100` is a relative mathematical increment that compounds errors on every duplicate delivery unless wrapped in an inbox deduplication transaction.

**📊 Quick comparison**
| Deduplication Strategy | Mechanism | Storage Engine | Failure Handling |
| :--- | :--- | :--- | :--- |
| Relational Inbox Table | Unique index on MessageId | SQL Server / PostgreSQL | Transaction rollback on duplicate |
| Redis Atomic Key | SET key token NX with TTL | Redis in-memory cache | Skips execution if key exists |
| Absolute State Update | UPDATE Status = 'Paid' | Native database SQL | Repeated updates yield same state |

**🔬 Under the hood (optional)**
When a consumer attempts to insert an existing `MessageId` into a table with a unique constraint, SQL Server throws error 2627 and PostgreSQL throws error 23505. The consumer catches this specific database constraint error, rolls back the local transaction, and immediately acknowledges the message.

---

## Q5: How do you troubleshoot and fix Cosmos DB 429 RequestRateTooLarge errors?
*Commonly asked at: Microsoft, Wells Fargo, Accenture, Capgemini*

**⚡ One-line answer**
Troubleshoot Cosmos DB 429 errors by analyzing partition key skew in Azure Monitor, optimizing query RU costs, and configuring client SDK exponential retry policies.

**🗣️ Spoken answer (30–45 seconds)**
HTTP 429 indicates that incoming requests have exceeded the provisioned Request Units for a physical partition. The primary cause is partition key skew, where a single hot partition receives excessive write traffic. To troubleshoot, inspect Azure Monitor metrics to identify which partition key range is throttling. In the .NET SDK, configure CosmosClientOptions with exponential backoff and jitter for transient bursts. To fix hot partitions, redesign the partition key to distribute traffic evenly using high-cardinality keys like CustomerId. Also, optimize queries to use point reads and add index coverage to lower RU consumption.

**🎯 Terms the interviewer listens for**
- ⭐ **HTTP 429 RequestRateTooLarge**: Status code returned when request throughput exceeds provisioned Request Units.
- ⭐ **Request Units (RU)**: Normalized unit of throughput measuring compute, memory, and IOPS in Cosmos DB.
- ⭐ **Hot Partition**: Physical storage partition experiencing disproportionately high traffic due to key skew.
- **High-Cardinality Key**: Partition key containing thousands of distinct values to distribute storage evenly.
- **Point Read**: Direct key-value lookup by ID and partition key costing exactly 1 RU.
- **CosmosClientOptions**: .NET SDK configuration setting retry counts and maximum retry wait times.

**🧠 Memory hook**
A shopping mall with twenty doors, but everyone crowds through Door 1 because of a bad floor sign; spread the doors.

**💻 Code**
```csharp
// ❌ Expensive query cross-partition scan costs 50+ Request Units
var query = container.GetItemQueryIterator<Item>("SELECT * FROM c WHERE c.Type='A'");

// ✅ Point read using Id and PartitionKey costs exactly 1 RU
ItemResponse<Item> res = await container.ReadItemAsync<Item>(
    id: "item-123",
    partitionKey: new PartitionKey("tenant-456"));
```

**⚠️ Likely follow-up**
*Q: What is the difference between manual RU provisioning and Autoscale RU in Cosmos DB?*
A: Manual provisioning assigns a fixed throughput limit, charging for peak capacity continuously [static provisioning]. Autoscale dynamically scales throughput between ten percent and one hundred percent of a configured maximum based on real-time request volume, preventing 429 errors while optimizing cloud hosting costs during idle hours.

**📊 Quick comparison**
| Remediation Technique | Implementation | Impact on 429s | Cost Impact |
| :--- | :--- | :--- | :--- |
| Point Reads (Id + PK) | Replace query with ReadItemAsync | Reduces RU cost from 50 to 1 | Reduces required RU capacity |
| SDK Retry Policy | MaxRetryAttemptsOnRateLimitedRequests | Recovers from short bursts | Zero additional cloud cost |
| High-Cardinality PK | Redesign partition key strategy | Eliminates hot partition skew | Prevents wasted RU allocations |
| Autoscale Provisioning | Enable autoscale in Azure portal | Instantly scales RU on bursts | Pays only for consumed capacity |

**🔬 Under the hood (optional)**
Cosmos DB divides total container throughput equally across all physical partitions. If a container has 10,000 RUs across 10 physical partitions, each partition gets exactly 1,000 RUs. If one hot partition receives 1,500 RUs, it throttles with 429 even though 8,500 RUs sit completely idle.

---

## Q6: How do you detect and fix deadlocks in SQL Server from a microservice perspective?
*Commonly asked at: Morgan Stanley, Barclays, Infosys, Cognizant*

**⚡ One-line answer**
Detect deadlocks using Extended Events XML deadlock graphs, and prevent them by acquiring identical resource access orders and using UPDLOCK hints on read-modify workflows.

**🗣️ Spoken answer (30–45 seconds)**
A deadlock occurs when two transactions hold locks and each waits for the other to release its lock. SQL Server resolves this by terminating the transaction with lower rollback cost and returning error 1205. To detect deadlocks, configure Extended Events to capture the `xml_deadlock_report`. In microservices, the most common cause is lock-conversion deadlocks, where both sessions read a row with Shared locks and then try to update it. To fix this, use `WITH (UPDLOCK, ROWLOCK)` during the initial read. Also, ensure all application code modifies database tables in identical alphabetical order.

**🎯 Terms the interviewer listens for**
- ⭐ **Deadlock (Error 1205)**: Mutual blocking between two transactions resolved only by killing a victim.
- ⭐ **Extended Events XML Deadlock Graph**: Diagnostic trace capturing query text, resource names, and lock modes.
- ⭐ **UPDLOCK Lock Hint**: Hint acquiring Update locks on read to prevent lock-conversion deadlocks.
- **Shared (S) Lock**: Read lock compatible with other readers but incompatible with exclusive locks.
- **Exclusive (X) Lock**: Write lock prohibiting concurrent read or write access on resources.
- **Lock Ordering**: Ensuring all transactions access resources in identical sequential order everywhere.

**🧠 Memory hook**
Two cars meeting on a narrow one-lane bridge; neither driver will reverse, so the traffic officer must tow one car away.

**💻 Code**
```csharp
// ❌ S-lock conversion deadlock: both read then both update
var order = await db.Orders.FirstAsync(x => x.Id == id); // S-lock

// ✅ UPDLOCK prevents concurrent update lock conversions
var order = await db.Orders
    .FromSqlInterpolated($"SELECT * FROM Orders WITH (UPDLOCK, ROWLOCK) WHERE Id={id}")
    .FirstAsync();
```

**⚠️ Likely follow-up**
*Q: How does Read Committed Snapshot Isolation (RCSI) impact deadlocks in SQL Server?*
A: RCSI eliminates reader-writer deadlocks by using row versioning in TempDB [optimistic read versioning]. Readers never acquire Shared locks and never block writers, and writers never block readers. However, writer-writer deadlocks still occur when two concurrent transactions attempt to update the same rows.

**📊 Quick comparison**
| Deadlock Prevention Strategy | Mechanism | Trade-off | Best For |
| :--- | :--- | :--- | :--- |
| Enforced Access Ordering | Access Table A before Table B | Requires code discipline | Multi-table batch transactions |
| WITH (UPDLOCK, ROWLOCK) | Update lock on initial read | Serializes concurrent readers | Read-modify-write workflows |
| RCSI Isolation Level | Serves row versions from TempDB | Adds TempDB storage overhead | High-read reporting environments |

**🔬 Under the hood (optional)**
The SQL Server Deadlock Monitor thread wakes every 5 seconds (or every 100ms when deadlocks are detected). It searches the lock manager hash table for cycles in the wait-for graph. When a cycle is detected, it selects the transaction that generated the least transaction log bytes as the victim.

---

## Q7: What is the difference between Azure Service Bus Sessions and standard Queues?
*Commonly asked at: Wells Fargo, Capgemini, TCS, Wipro*

**⚡ One-line answer**
Service Bus Sessions guarantee strict first-in-first-out message ordering and stateful grouping per Session ID, whereas standard queues allow out-of-order parallel processing.

**🗣️ Spoken answer (30–45 seconds)**
Standard Azure Service Bus queues distribute messages across competing consumer pods for maximum parallel throughput. However, if five messages for Customer 10 arrive, different pods process them simultaneously, leading to out-of-order execution. Service Bus Sessions solve this by attaching a Session ID, such as CustomerId or OrderId. When a consumer pod locks a session, it gains exclusive ownership of all messages for that Session ID. All subsequent messages for that customer process sequentially in strict FIFO order on that pod. This ensures ledger updates and order workflows never process out of sequence.

**🎯 Terms the interviewer listens for**
- ⭐ **Azure Service Bus Sessions**: Feature guaranteeing strict FIFO ordering for messages sharing a Session ID.
- ⭐ **Competing Consumers Pattern**: Multiple worker pods reading concurrently from a queue for scale.
- ⭐ **Session Lock**: Exclusive lease granted to one consumer pod for a Session ID.
- **Out-of-Order Processing**: Defect where downstream messages execute before earlier prerequisite messages.
- **FIFO (First-In-First-Out)**: Guarantee that messages process in exact order of arrival.
- **Session State**: Ephemeral storage attached to a session used for tracking state checkpoints.

**🧠 Memory hook**
Standard queue is five supermarket checkouts where anyone enters; session is a bank passbook counter where your account is handled sequentially.

**💻 Code**
```csharp
// ❌ Standard queue: competing consumers process customer events out of order
await _sender.SendMessageAsync(new ServiceBusMessage(json));

// ✅ Sessions: enforce strict FIFO ordering per CustomerId
var message = new ServiceBusMessage(json) { SessionId = customerId };
await _sender.SendMessageAsync(message);
```

**⚠️ Likely follow-up**
*Q: What is the throughput trade-off when enabling Service Bus Sessions?*
A: Sessions serialize message processing per Session ID to preserve order [partitioned serialization]. While total throughput remains high across thousands of distinct Session IDs, individual session processing speed is bounded by a single consumer thread. If you require millions of unordered events per second, use standard queues or Kafka.

**📊 Quick comparison**
| Capability | Standard Queue | Service Bus Session |
| :--- | :--- | :--- |
| Message Ordering | Best-effort, no strict guarantee | Guaranteed strict FIFO per Session |
| Concurrency | Parallel competing consumers across pods | Single consumer per active Session |
| Grouping Key | None | Required `SessionId` property |
| State Storage | Stateless message processing | Stores ephemeral session state |
| Best For | Bulk image processing, emails | Financial ledgers, multi-step orders |

**🔬 Under the hood (optional)**
When a consumer calls `AcceptNextSessionAsync`, Service Bus acquires a distributed lock on that Session ID metadata partition in the broker. The lock prevents any other consumer instance from receiving messages tagged with that Session ID until the holding consumer explicitly closes the session or the session lock expires.

---

## Q8: How do you prevent a memory leak when using ConcurrentDictionary for keyed locking?
*Commonly asked at: Swiggy, Uber, JPMorgan, Nagarro*

**⚡ One-line answer**
Prevent memory leaks in keyed locking by wrapping SemaphoreSlim in a reference-counted container, safely removing the key from the dictionary when the counter reaches zero.

**🗣️ Spoken answer (30–45 seconds)**
Keyed locking synchronizes operations per entity ID, like CustomerId, allowing different customers to process in parallel. Junior developers often implement this by calling `ConcurrentDictionary.GetOrAdd` to create a `SemaphoreSlim`. However, keys are never removed from the dictionary. After millions of requests, millions of idle semaphores accumulate in memory, causing severe Gen 2 heap bloat. The solution is reference counting. We wrap each semaphore in an object with a reference counter. When a thread enters, it increments the count. When releasing, if the count hits zero, it removes the entry under lock, cleanly freeing memory.

**🎯 Terms the interviewer listens for**
- ⭐ **Keyed Locking**: Granular in-process synchronization restricting lock contention to specific entity IDs.
- ⭐ **Reference Counting**: Memory management technique tracking active thread references to clean up unneeded objects.
- ⭐ **Memory Leak in Managed Code**: Unintentional memory retention where unused dictionary objects remain rooted in Gen 2.
- **ConcurrentDictionary.GetOrAdd**: Thread-safe hash table method adding keys only if absent.
- **Eviction Lock**: Synchronization ensuring removal does not race with concurrent key acquisitions.
- **Deterministic Cleanup**: Explicitly releasing and disposing unmanaged or pooling resources immediately.

**🧠 Memory hook**
Borrowing a library book; the librarian records the loan count, and shelves the book away only when all borrowers have returned it.

**💻 Code**
```csharp
// ❌ Memory leak: semaphores accumulate in dictionary forever
var sem = _dict.GetOrAdd(key, _ => new SemaphoreSlim(1, 1));

// ✅ Reference counting: prune dictionary entry when count reaches 0
Interlocked.Increment(ref wrapper.RefCount);
await wrapper.Semaphore.WaitAsync(ct);
try { await ExecuteWorkAsync(); }
finally {
    if (Interlocked.Decrement(ref wrapper.RefCount) == 0)
        _dict.TryRemove(key, out _);
    wrapper.Semaphore.Release();
}
```

**⚠️ Likely follow-up**
*Q: What race condition can occur when removing a semaphore from the dictionary?*
A: Thread A decrements the count to zero and begins removal. Simultaneously, Thread B retrieves the same semaphore from the dictionary before removal completes. Thread A then removes it, leaving Thread B with an orphaned semaphore [eviction race condition]. Protect dictionary removal and creation with a synchronized lock block.

**📊 Quick comparison**
| Keyed Locking Approach | Concurrency Isolation | Memory Leak Risk | Implementation Complexity |
| :--- | :--- | :--- | :--- |
| Global lock(obj) | Zero parallelism (global bottleneck) | Zero memory leak risk | Simplest implementation |
| Naive ConcurrentDictionary | Entity-level concurrency | High Gen 2 memory retention | Low complexity |
| Reference-Counted Semaphore | Entity-level concurrency | Zero leak (pruned on 0) | Moderate synchronization complexity |

**🔬 Under the hood (optional)**
`ConcurrentDictionary` internal buckets retain table entries indefinitely until explicitly removed via `TryRemove`. Because `SemaphoreSlim` contains unmanaged wait handles and OS kernel links, retaining millions of semaphores bloats the finalization table and forces the garbage collector to perform expensive Gen 2 sweeps.

---

## Q9: When would you use an Azure Blob Lease as a distributed lock instead of Redis?
*Commonly asked at: Barclays, Wells Fargo, Microsoft, EPAM*

**⚡ One-line answer**
Use an Azure Blob Lease for coarse-grained background tasks with zero extra infrastructure, and use Redis for high-frequency low-latency API transaction locking.

**🗣️ Spoken answer (30–45 seconds)**
Choose between Azure Blob Leases and Redis based on latency needs and infrastructure overhead. Azure Blob Leases operate over HTTPS REST APIs with a typical order of magnitude of 50 to 150 milliseconds depending on region. This latency makes Blob leases unsuitable for user-facing API request paths. However, for coarse-grained background tasks like nightly reconciliation jobs or singleton pod leader election, Blob leases are ideal. They leverage existing Azure Storage accounts without the cost or maintenance of a dedicated Redis cluster. Furthermore, leases offer guaranteed auto-expiration between fifteen and sixty seconds if a pod crashes.

**🎯 Terms the interviewer listens for**
- ⭐ **Azure Blob Lease**: Distributed lock mechanism operating on Azure Blob Storage metadata over REST.
- ⭐ **Leader Election**: Selecting a single primary worker pod across replicas to run background jobs.
- ⭐ **HTTP 412 Precondition Failed**: Status code returned when attempting to acquire an already leased blob.
- **Redis Redlock**: Distributed locking algorithm providing millisecond in-memory synchronization across nodes.
- **Lease Duration**: Configurable lock hold window between 15 and 60 seconds with auto-expiration.
- **Infrastructure Overhead**: Cost and operational burden of managing and monitoring dedicated cache clusters.

**🧠 Memory hook**
A wax seal on a bank deposit box for monthly audits versus a digital turnstile token for thousands of subway commuters.

**💻 Code**
```csharp
// ❌ High-latency Blob lease in hot user checkout path
var lease = await blobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(15));

// ✅ Background singleton leader election with automatic 30s expiry
try {
    var lease = await _blobLeaseClient.AcquireAsync(TimeSpan.FromSeconds(30), cancellationToken: ct);
    await RunNightlyPayrollJobAsync(ct);
} catch (RequestFailedException ex) when (ex.Status == 412) {
    _logger.LogInformation("Another pod is currently the active leader.");
}
```

**⚠️ Likely follow-up**
*Q: What happens if a pod holding an Azure Blob Lease crashes without releasing it?*
A: The lease automatically expires in cloud storage once the configured duration elapses [auto-release expiration]. Because the holding pod is down, its background heartbeat stops renewing the lease. Once the 30-second window expires, other worker pods acquire the lease successfully, preventing permanent system deadlocks.

**📊 Quick comparison**
| Metric | Azure Blob Lease | Redis Distributed Lock |
| :--- | :--- | :--- |
| Lock Acquisition Latency | Typical order of magnitude 50–150ms | Sub-millisecond in-memory speed |
| Infrastructure Requirement | Existing Azure Storage account | Dedicated Redis cluster needed |
| Minimum Lock Duration | 15 seconds | 1 millisecond |
| Best For | Nightly cron jobs, leader election | High-throughput cart checkout locking |
| Crash Safety | Guaranteed cloud auto-expiration | TTL expiration with heartbeat renewal |

**🔬 Under the hood (optional)**
Azure Blob Leases utilize the REST API `PUT {blob}?comp=lease` with the header `x-ms-lease-action: acquire`. The Azure Storage frontend atomically validates whether an active lease ID exists on the blob metadata. Leases can be acquired for 15 to 60 seconds. Requests lacking the active lease token fail with HTTP 412.

---

## Q10: Explain how Cosmos DB Change Feed handles consumer concurrency across multiple worker instances.
*Commonly asked at: Microsoft, Walmart, Accenture, Cognizant*

**⚡ One-line answer**
Cosmos DB Change Feed distributes partitions across worker instances using lease containers, dynamically rebalancing partition ownership when worker pods scale out or crash.

**🗣️ Spoken answer (30–45 seconds)**
The Cosmos DB Change Feed acts as an event sourcing stream that outputs committed document modifications sequentially. When running multiple consumer pods, the Change Feed Processor coordinates concurrency automatically using a dedicated lease container. Each physical partition in the database is represented by a lease document. Worker pods acquire exclusive leases on subsets of partitions using optimistic concurrency ETags. If you scale from two pods to four, the processor automatically rebalances leases across all pods. If a worker pod crashes, its lease expires, and a surviving pod resumes processing from the last recorded continuation token.

**🎯 Terms the interviewer listens for**
- ⭐ **Change Feed Processor**: High-level SDK library coordinating partition distribution and checkpointing across instances.
- ⭐ **Lease Container**: Auxiliary Cosmos DB collection tracking consumer partition ownership and continuation tokens.
- ⭐ **Continuation Token**: Opaque bookmark string recording the exact stream position within a partition.
- **Dynamic Rebalancing**: Automatically redistributing partition leases when consumer instances scale or crash.
- **Optimistic Concurrency Control**: Using HTTP ETags to update lease documents without lock contention.
- **Physical Partition**: Scalable storage and compute unit into which Cosmos DB divides container data.

**🧠 Memory hook**
A factory assembly line with ten conveyor belts; workers claim specific belts and shift to unclaimed belts when a coworker takes a break.

**💻 Code**
```csharp
// ❌ Manual partition polling risks duplicate processing and missed updates
var items = await container.GetItemQueryIterator<Item>("SELECT * FROM c");

// ✅ Change Feed Processor: multi-pod coordination via lease container
var processor = sourceContainer.GetChangeFeedProcessorBuilder<Item>("WorkerGroup", HandleChangesAsync)
    .WithInstanceName(Environment.MachineName)
    .WithLeaseContainer(leaseContainer)
    .Build();
await processor.StartAsync();
```

**⚠️ Likely follow-up**
*Q: Can two separate consumer pods process the same physical partition concurrently?*
A: No, within the same consumer group, exactly one worker instance holds the lease for a given physical partition [single-consumer partition locking]. This guarantees strict in-order message processing per partition. Separate consumer applications configure unique processor names to maintain independent lease containers.

**📊 Quick comparison**
| Concurrency Dimension | Cosmos DB Change Feed | Apache Kafka Consumer Group |
| :--- | :--- | :--- |
| Partition Ownership | Coordinated via Lease Container | Coordinated via Group Coordinator broker |
| Checkpointing | Stores Continuation Token in lease | Commits partition offset to `__consumer_offsets` |
| Rebalancing | Automatic lease steal and rebalance | Consumer group rebalance protocol |
| Ordering Guarantee | Guaranteed per physical partition key | Guaranteed per topic partition |
| Scale Limit | Maximum active pods equals partition count | Maximum active pods equals partition count |

**🔬 Under the hood (optional)**
The Change Feed Processor polls partition ranges using HTTP GET with the `If-None-Match: *` and `A-IM: Incremental feed` headers. The response returns an `ETag` continuation token header. The processor commits this token to the lease document using OCC (`If-Match`), guaranteeing zero lost checkpoints across rebalances.

---

## Q11: How do you implement distributed transactions across microservices without Two-Phase Commit?
*Commonly asked at: Swiggy, Flipkart, Walmart, JPMorgan*

**⚡ One-line answer**
Implement distributed workflows without Two-Phase Commit by using the Saga pattern, executing an ordered series of local transactions with compensating actions and idempotent retries.

**🗣️ Spoken answer (30–45 seconds)**
Two-Phase Commit does not scale across microservices because holding distributed locks across networks exhausts database connection pools. Instead, we use the Saga pattern to manage distributed transactions as an ordered series of discrete local ACID transactions. In an orchestrated Saga, a centralized state machine commands participant services. Each service commits locally in its own database and replies to the orchestrator. If any step fails midway, the orchestrator triggers compensating transactions to semantically undo previously committed steps. Forward progress uses idempotent retries to handle transient network errors.

**🎯 Terms the interviewer listens for**
- ⭐ **Saga Pattern**: Sequence of local transactions updating services and publishing events.
- ⭐ **Saga Orchestrator**: Central coordinator executing workflow steps and triggering compensations.
- ⭐ **Compensating Transaction**: Semantic undo operation reversing a previously committed local transaction.
- **Idempotent Retries**: Repeating operations safely without duplicating business side effects.
- **Semantic Lock**: Application-level status flag preventing concurrent conflicting entity modifications.
- **Pivot Transaction**: Critical step after which the Saga commits to completing forward.

**🧠 Memory hook**
Booking a vacation package; if the hotel fails after flight booking, the system issues a flight refund and cancels the trip.

**💻 Code**
```csharp
// ❌ Synchronous 2PC holds row locks across network partitions
using var scope = new TransactionScope(TransactionScopeAsyncFlowOption.Enabled);

// ✅ Saga orchestrator executing forward steps with compensating actions
public async Task RunCheckoutSagaAsync(OrderState state, CancellationToken ct) {
    if (!await _paymentClient.ChargeAsync(state.Id, state.Total, ct)) {
        await _inventoryClient.ReleaseReservationAsync(state.Id, ct);
    }
}
```

**⚠️ Likely follow-up**
*Q: What is the primary difference between a compensating transaction and a database rollback?*
A: A database rollback occurs before commit by discarding in-memory transaction logs [storage engine abort]. A compensating transaction is an explicit new forward transaction executed after an earlier transaction already committed, semantically reversing business effects while preserving full audit history [semantic undo].

**📊 Quick comparison**
| Dimension | Two-Phase Commit (2PC) | Saga Pattern |
| :--- | :--- | :--- |
| Locking | Synchronous distributed row locks | Local database transactions only |
| Consistency | Immediate ACID consistency | Eventual BASE consistency |
| Availability | Low during network partitions | High availability across services |
| Failure Handling | Coordinated rollback | Business compensating actions |
| Scalability | Severe connection pool contention | Scales smoothly with message queues |

**🔬 Under the hood (optional)**
Sagas do not provide ACID isolation. Concurrent transactions can read intermediate uncommitted business state. Systems mitigate this using semantic locking flags, such as marking an order status as PendingPayment, preventing other workflows from altering the entity until completion.

---

## Q12: How do you handle database connection drops or failovers during an active transaction in EF Core?
*Commonly asked at: Barclays, Wells Fargo, Infosys, Wipro*

**⚡ One-line answer**
Handle database connection drops using EF Core execution strategies that retry transient failures, wrapping custom transactions inside ExecuteAsync delegates to prevent half-committed state.

**🗣️ Spoken answer (30–45 seconds)**
In cloud environments, database server failovers and transient network glitches frequently sever active connections. By default, an interrupted transaction throws an exception and leaves operations in an ambiguous state. In EF Core, we configure an execution strategy such as `EnableRetryOnFailure`. When writing custom multi-statement transactions, you must wrap them inside `strategy.ExecuteAsync()`. This allows the execution strategy to rebuild the database connection and cleanly replay the entire transaction from the beginning. Idempotent business keys must be used to ensure retries never execute duplicate side effects.

**🎯 Terms the interviewer listens for**
- ⭐ **Execution Strategy**: EF Core mechanism that intercepts transient database exceptions and executes retries.
- ⭐ **EnableRetryOnFailure**: SQL Server provider option configuring automatic retries for transient connection drops.
- ⭐ **ExecuteAsync Delegate**: Wrapper required when creating explicit transactions under an EF Core retry strategy.
- **Transient Fault**: Temporary network interruption or server failover that clears within milliseconds.
- **Connection Resiliency**: System ability to recover automatically from dropped database connections.
- **Idempotent Retry**: Re-executing a transactional block safely without producing duplicate rows.

**🧠 Memory hook**
A bad phone connection dropping mid-sentence; rather than guessing what was said, you call back and repeat the sentence from the start.

**💻 Code**
```csharp
// ❌ Naive transaction crashes on failover: Cannot retry user-initiated transaction
using var tx = await db.Database.BeginTransactionAsync();

// ✅ Resilient transaction replay using EF Core execution strategy
var strategy = db.Database.CreateExecutionStrategy();
await strategy.ExecuteAsync(async () => {
    using var tx = await db.Database.BeginTransactionAsync();
    db.Orders.Add(order);
    await db.SaveChangesAsync();
    await tx.CommitAsync();
});
```

**⚠️ Likely follow-up**
*Q: What happens if an explicit transaction is opened without using strategy.ExecuteAsync?*
A: EF Core throws an `InvalidOperationException` stating that user-initiated transactions cannot be automatically retried [transaction retry restriction]. The execution strategy cannot know whether earlier statements in the transaction reached the database, so it requires the entire transaction block to be enclosed in `ExecuteAsync` to allow clean replay.

**📊 Quick comparison**
| Failure Scenario | Default EF Core Behavior | With Execution Strategy |
| :--- | :--- | :--- |
| Transient Network Blip | Throws SqlException immediately | Retries automatically with jitter |
| Azure SQL Failover | Request fails with 500 | Reconnects to new primary node |
| Multi-statement Transaction | Throws InvalidOperationException | Replays entire transaction delegate |
| Non-transient Syntax Error | Throws exception immediately | Fails fast without retrying |

**🔬 Under the hood (optional)**
`SqlServerRetryingExecutionStrategy` checks specific SQL Server error codes against an internal transient error table (e.g. 10054 connection reset, 10060 connection timeout, 40613 database unavailable during failover). Non-transient errors like constraint violations (2627) bypass the retry logic and throw immediately.

---

## Q13: How do you implement backpressure in a high-throughput event consumer?
*Commonly asked at: Swiggy, Uber, JPMorgan, EPAM*

**⚡ One-line answer**
Implement backpressure using bounded channels or pull-based consumer throttling, slowing message consumption when downstream workers or databases reach maximum capacity.

**🗣️ Spoken answer (30–45 seconds)**
In high-throughput messaging architectures, consumers can be overwhelmed by sudden traffic bursts. If consumers pull messages faster than the database can process them, unhandled tasks accumulate in memory, causing Out-Of-Memory container crashes. To implement backpressure, we use pull-based consumer models rather than unbounded push feeds. In .NET, we channel messages into a bounded `Channel<T>`. When the channel buffer fills up, writing threads asynchronously wait until worker consumers drain items. Alternatively, adjust Kafka consumer max poll records or RabbitMQ prefetch counts. This ensures memory usage remains stable regardless of traffic spikes.

**🎯 Terms the interviewer listens for**
- ⭐ **Backpressure**: Flow control mechanism regulating consumer message intake based on downstream processing speed.
- ⭐ **Bounded Channel**: Thread-safe in-memory queue with a fixed maximum capacity that suspends producers.
- ⭐ **Prefetch Count**: Broker setting limiting how many unacknowledged messages a consumer can hold.
- **Out-of-Memory (OOM)**: Container crash triggered when unconstrained queuing exhausts physical RAM.
- **Pull-Based Consumer**: Architecture where workers actively request batches rather than receiving push floods.
- **Full Mode**: Bounded channel policy determining behavior (Wait, DropNewest, DropOldest) on saturation.

**🧠 Memory hook**
A funnel on a bottle; pouring water too fast overflows the kitchen counter unless you pour at the funnel's drain rate.

**💻 Code**
```csharp
// ❌ Unbounded queue: 100,000 messages accumulate in RAM, triggering OOM
var queue = new ConcurrentQueue<Message>(); // No memory limit!

// ✅ Bounded Channel: suspends message reading when buffer reaches 1,000
var channel = Channel.CreateBounded<Message>(new BoundedChannelOptions(1000) {
    FullMode = BoundedChannelFullMode.Wait
});
await channel.Writer.WriteAsync(msg); // Asynchronously yields thread if full!
```

**⚠️ Likely follow-up**
*Q: How does RabbitMQ BasicQos prefetch count establish backpressure?*
A: `BasicQos(prefetchCount: 50)` instructs RabbitMQ to send at most fifty messages to a consumer worker until earlier messages are acknowledged [broker-level backpressure]. If processing slows down, unacknowledged messages hit fifty, and RabbitMQ pauses delivery, buffering messages safely on disk rather than overflowing consumer RAM.

**📊 Quick comparison**
| Backpressure Strategy | Enforcement Point | Behavior Under Overload | Memory Safety Profile |
| :--- | :--- | :--- | :--- |
| Unbounded Queue | Application memory | Consumes unbounded RAM | High OOM container crash risk |
| Bounded Channel<T> | In-process buffer | Writer awaits space asynchronously | Guaranteed bounded memory footprint |
| RabbitMQ Prefetch | Message Broker (TCP) | Broker pauses packet delivery | Backpressure pushed to queue storage |
| Kafka Poll Batch Size | Consumer SDK Loop | Polls next batch only after commit | Natural consumer-paced throttling |

**🔬 Under the hood (optional)**
`Channel.CreateBounded<T>` implements `BoundedChannelFullMode.Wait` using a lock-free ring buffer and asynchronous reader/writer queues. When the capacity limit is reached, `Writer.WriteAsync` returns an incomplete `ValueTask` backed by a waiter node, suspending the producer without blocking any OS thread.

---

## Q14: What is the difference between Pessimistic Locking and Optimistic Locking, and when do you choose which?
*Commonly asked at: Barclays, Morgan Stanley, Infosys, Capgemini*

**⚡ One-line answer**
Pessimistic locking acquires exclusive database locks on read to block concurrent modifications, whereas optimistic locking checks version tokens on write to detect conflicts.

**🗣️ Spoken answer (30–45 seconds)**
The choice between pessimistic and optimistic locking depends on conflict frequency. Pessimistic locking places physical database locks during reads, forcing other concurrent transactions to wait until the lock holder commits. In SQL Server, this is achieved using `WITH (UPDLOCK, ROWLOCK)`. Optimistic locking places zero database read locks; instead, rows maintain a version token, like a SQL Server `rowversion` or Cosmos DB ETag. During updates, the engine verifies the version token has not changed. If another transaction modified the row, the update affects zero rows and throws a concurrency exception.

**🎯 Terms the interviewer listens for**
- ⭐ **Pessimistic Locking**: Concurrency strategy acquiring physical database locks on read to prevent conflicts.
- ⭐ **Optimistic Concurrency Control**: Concurrency strategy verifying version tokens on update without holding read locks.
- ⭐ **rowversion**: SQL Server auto-incrementing binary token mapped by EF Core for concurrency checks.
- **DbUpdateConcurrencyException**: Exception thrown when an optimistic update affects zero database rows.
- **Lock Contention**: Performance penalty where transactions wait in queues for lock holders to finish.
- **ETag**: HTTP entity tag used by Cosmos DB to implement optimistic concurrency over REST.

**🧠 Memory hook**
Pessimistic is taking the physical office key with you; optimistic is writing your name on a whiteboard and checking if anyone erased it.

**💻 Code**
```csharp
// ❌ No concurrency control: last write silently overwrites prior changes
db.Orders.Update(order); await db.SaveChangesAsync();

// ✅ Optimistic locking using EF Core rowversion property
public class Order {
    public Guid Id { get; set; }
    [Timestamp] public byte[] RowVersion { get; set; } = default!;
}
// Throws DbUpdateConcurrencyException if another transaction updated first!
```

**⚠️ Likely follow-up**
*Q: When should you choose pessimistic locking over optimistic locking?*
A: Choose pessimistic locking when conflict contention is exceptionally high, such as reserving the final concert tickets during a flash sale [high contention workflows]. In high-contention scenarios, optimistic locking causes widespread retries and wasted CPU, whereas pessimistic locks cleanly serialize transactions at the database engine.

**📊 Quick comparison**
| Metric | Pessimistic Locking | Optimistic Locking |
| :--- | :--- | :--- |
| Lock Mechanism | Physical database row locks | Version tokens (`rowversion`, ETag) |
| Read Concurrency | Readers or writers block | Non-blocking concurrent reads |
| Collision Behavior | Queues transactions behind lock | Throws concurrency exception on conflict |
| Ideal Contention | High contention (ticket checkout) | Low to moderate contention (CMS, profiles) |
| Resource Overhead | Consumes lock manager memory | Zero lock manager memory overhead |

**🔬 Under the hood (optional)**
When EF Core saves an entity configured with `[Timestamp]`, it compiles: `UPDATE Orders SET Status = @p0 WHERE Id = @p1 AND RowVersion = @p2`. If the row was modified, `@p2` fails to match, affected row count is 0, and EF Core translates this into a `DbUpdateConcurrencyException`.

---

## Q15: How do you debug a production distributed race condition that only appears under heavy load?
*Commonly asked at: Amazon, Microsoft, Swiggy, Uber*

**⚡ One-line answer**
Debug load-only race conditions by correlating distributed traces via OpenTelemetry, inspecting concurrency metrics in Grafana, and writing automated multi-threaded stress tests using Testcontainers.

**🗣️ Spoken answer (30–45 seconds)**
Distributed race conditions rarely reproduce in local developer environments because they require concurrent multi-pod timing collisions. To debug these in production, we first inspect distributed traces using OpenTelemetry and W3C trace IDs. By correlating logs across pods for the same Customer ID, we identify overlapping database transactions. Next, inspect database Extended Events for deadlock graphs and lock escalation events. Once the sequence is understood, write a high-concurrency automated test using xUnit and Testcontainers. Launching one hundred parallel tasks against a containerized database reliably reproduces the race condition, allowing verification of the fix.

**🎯 Terms the interviewer listens for**
- ⭐ **Distributed Race Condition**: Concurrency defect where distributed system correctness depends on multi-pod execution timing.
- ⭐ **Extended Events Deadlock Graph**: Diagnostic trace capturing query text, resource locks, and deadlock victims.
- ⭐ **Testcontainers**: Automated testing library spinning up real containerized databases for stress testing.
- **W3C Trace ID**: Globally unique identifier linking logs and spans across distributed microservice hops.
- **Thread-Timing Collision**: Microsecond window where concurrent threads interleave operations on shared state.
- **High-Concurrency Harness**: Multi-threaded test runner executing parallel tasks to simulate flash load.

**🧠 Memory hook**
Two people using the same bank ATM card at separate machines in different cities at the exact same millisecond.

**💻 Code**
```csharp
// ❌ Cannot reproduce locally with single-threaded unit tests
[Fact] public async Task SingleThreadTest() => await _svc.DebitAsync(id, 100);

// ✅ High-concurrency stress harness launching 100 parallel requests
[Fact] public async Task ConcurrencyStressTest() {
    var tasks = Enumerable.Range(0, 100)
        .Select(_ => _svc.DebitAsync(id, 10, CancellationToken.None));
    await Task.WhenAll(tasks); // Flushes out timing collisions reliably!
}
```

**⚠️ Likely follow-up**
*Q: What log signal in production most reliably points to a race condition?*
A: The most common signal is duplicate database unique constraint violations (e.g. SQL Server error 2627 or Postgres 23505) logged simultaneously by different pod hostnames for the exact same entity identifier within single-digit milliseconds [concurrent insertion collision].

**📊 Quick comparison**
| Diagnostic Approach | Environment | Effectiveness | Primary Insight Gained |
| :--- | :--- | :--- | :--- |
| Local Single-Thread Unit Test | Local Dev | Zero for race conditions | Tests functional logic only |
| OpenTelemetry Distributed Traces | Production | High across microservices | Identifies overlapping pod executions |
| Extended Events XML Graph | SQL Server | High for locking bugs | Pinpoints conflicting SQL queries |
| Parallel Testcontainers Harness | CI/CD | High for automated repro | Validates fix under heavy concurrency |

**🔬 Under the hood (optional)**
In modern Linux Kubernetes pods, runtime thread stacks can be dumped during a live hang using `dotnet-dump collect -p <pid>`. Inside the SOS analysis shell, running `clrstack -all` and `syncblk` reveals managed threads blocked on Monitor SyncBlocks, uncompleted Task wait handles, or ThreadPool worker starvation.
"""

full_content = part1_text + part2_header

with open("05_Concurrency_Locks_Basic_Interview.md", "w", encoding="utf-8") as f:
    f.write(full_content)

print("Wrote 05_Concurrency_Locks_Basic_Interview.md")
b_errs, q_errs = validate_file("05_Concurrency_Locks_Basic_Interview.md")
print(f"Validation result: {b_errs} banned errors, {q_errs} question errors")
