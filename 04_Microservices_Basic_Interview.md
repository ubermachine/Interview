# 04. Microservices Architecture & Distributed System Design — Basic Interview & Everyday Concepts

> **Target Audience:** Engineers preparing for technical screening rounds, preliminary system design evaluations, and architectural discussions at top product firms and Global Capability Centers (GCCs).  
> **Standard:** Speakable Senior English v1 (SSE-1) Standard Format. Crisp spoken answers (30–45 seconds), clear memory analogies, clean 5–15 line code snippets, and quick visual comparison tables.

---

# Table of Contents
- [Q1: What is a microservices architecture, and how does it differ from a monolith?](#q1-what-is-a-microservices-architecture-and-how-does-it-differ-from-a-monolith)
- [Q2: Why must each microservice have its own private database?](#q2-why-must-each-microservice-have-its-own-private-database)
- [Q3: Why is Two-Phase Commit (2PC) usually avoided in distributed systems?](#q3-why-is-two-phase-commit-2pc-usually-avoided-in-distributed-systems)
- [Q4: What is the Saga pattern, and what is the difference between choreography and orchestration?](#q4-what-is-the-saga-pattern-and-what-is-the-difference-between-choreography-and-orchestration)
- [Q5: What is a compensating transaction, and how does it differ from a database rollback?](#q5-what-is-a-compensating-transaction-and-how-does-it-differ-from-a-database-rollback)
- [Q6: What is the dual-write problem, and why does it risk data inconsistency?](#q6-what-is-the-dual-write-problem-and-why-does-it-risk-data-inconsistency)
- [Q7: What is the Transactional Outbox pattern, and how does it prevent lost messages?](#q7-what-is-the-transactional-outbox-pattern-and-how-does-it-prevent-lost-messages)
- [Q8: What is an idempotent consumer, and why is message deduplication required?](#q8-what-is-an-idempotent-consumer-and-why-is-message-deduplication-required)
- [Q9: What is CQRS (Command Query Responsibility Segregation)?](#q9-what-is-cqrs-command-query-responsibility-segregation)
- [Q10: What is an API Gateway, and why do microservices place one at the network edge?](#q10-what-is-an-api-gateway-and-why-do-microservices-place-one-at-the-network-edge)
- [Q11: Why do internal microservices use gRPC instead of REST?](#q11-why-do-internal-microservices-use-grpc-instead-of-rest)
- [Q12: What is the Circuit Breaker pattern, and what are its three operational states?](#q12-what-is-the-circuit-breaker-pattern-and-what-are-its-three-operational-states)
- [Q13: What is distributed tracing, and how does OpenTelemetry trace requests across services?](#q13-what-is-distributed-tracing-and-how-does-opentelemetry-trace-requests-across-services)
- [Q14: How does an end-to-end checkout flow handle inventory, payment, and failure?](#q14-how-does-an-end-to-end-checkout-flow-handle-inventory-payment-and-failure)

---

## Q1: What is a microservices architecture, and how does it differ from a monolith?
*Commonly asked at: TCS, Infosys, Cognizant, Wipro*

**⚡ One-line answer**
**Microservices** means autonomous services organized around business domains with private databases, whereas a monolith runs in one single process.

**🗣️ Spoken answer (30–45 seconds)**
A **monolith** is a single process running all application features on a shared database. In contrast, **microservices** are autonomous, independently deployable services organized around business domains. Each microservice encapsulates a **bounded context**, which is an autonomous domain boundary isolating models and logic. We enforce **database-per-service**, meaning private data persistence owned exclusively by one service. This guarantees **loose coupling**, where services interact solely through published network contracts, giving teams true deployment autonomy without cross-service schema lock-in.

**🎯 Terms the interviewer listens for**
- ⭐ **Monolith** — single deployable process running all application features
- ⭐ **Microservices** — autonomous, independently deployable services organized around domains
- ⭐ **Bounded context** — autonomous domain boundary isolating models and data
- **Database-per-service** — private data store owned exclusively by one service
- **Loose coupling** — services interacting strictly through published network contracts
- **Independent deployability** — releasing one service without redeploying dependent services

**🧠 Memory hook**
A monolith is a department store with one shared register; microservices are independent shopping mall stores, each managing its own checkout desk.

**💻 Code**
```csharp
// ❌ Shared process and monolithic database context
public class MonolithOrderService {
    public void Checkout(Order o) { /* Saves to shared DB */ }
}

// ✅ Autonomous microservice calling independent payment boundary
public class MicroserviceOrderService {
    public async Task CheckoutAsync(Order o, HttpClient client) {
        await client.PostAsJsonAsync("https://payment-svc/charges", o);
    }
}
```

**⚠️ Likely follow-up**
*Q: When should a team avoid decomposing into microservices?*
A: Keep a single deployable application [modular monolith] when domain boundaries are uncertain or teams are under fifteen engineers. Splitting too early introduces network serialization costs, distributed failures, and deployment complexity before the organization needs independent scaling.

**📊 Quick comparison**
| Dimension | Monolith | Microservices |
| :--- | :--- | :--- |
| Deployment | Single deployable unit | Independent service deployments |
| Database | Single shared database | Database per service |
| Blast Radius | Process crash impacts all | Failure isolated to service |
| Scaling | Scale entire application | Scale hot services only |
| Complexity | Low initial operational overhead | High operational network overhead |

**🔬 Under the hood (optional)**
Independent microservices communicate across network sockets via TCP or HTTP/2 rather than memory pointers. This replaces local function call overhead with network serialization, TCP handshakes, kernel socket buffers, and latency hops.

---

## Q2: Why must each microservice have its own private database?
*Commonly asked at: Wells Fargo, Barclays, Infosys, Capgemini*

**⚡ One-line answer**
**Database-per-service** means each microservice exclusively owns its private database to prevent coupling and ensure independent schema migrations.

**🗣️ Spoken answer (30–45 seconds)**
The **database-per-service** pattern means a private persistence store owned exclusively by one microservice without external access. Sharing tables causes tight coupling and lock contention. Enforcing private persistence enables **schema evolution**, which is altering database structures without breaking external calling services. It also unlocks **polyglot persistence**, the practice of selecting specialized storage engines tailored for specific domain requirements like relational or document stores. To assemble cross-service views, we use **API composition**, assembling client responses in memory across multiple service endpoints without direct database joins.

**🎯 Terms the interviewer listens for**
- ⭐ **Database-per-service** — private persistence store owned exclusively by one microservice
- ⭐ **Schema evolution** — altering database structures without breaking external calling services
- ⭐ **Polyglot persistence** — selecting specialized storage engines tailored for specific domain requirements
- **API composition** — assembling client responses in memory across multiple service endpoints
- **Data encapsulation** — hiding internal tables behind explicit public API contracts
- **Shared database** — anti-pattern sharing tables directly across multiple service boundaries

**🧠 Memory hook**
HDFC Bank cannot run SQL queries directly on ICICI Bank tables; both banks exchange standardized messages while keeping ledgers private.

**💻 Code**
```csharp
// ❌ Cross-database query breaks boundary encapsulation
var items = await dbContext.InventoryItems
    .FromSqlRaw("SELECT * FROM InventoryDb.dbo.Items").ToListAsync();

// ✅ Communication across independent boundary using client contract
var items = await inventoryClient.GetFromJsonAsync<List<ItemDto>>("/items");
```

**⚠️ Likely follow-up**
*Q: How do you show an order with customer details without SQL joins?*
A: Join data in memory using parallel API calls [API composition] or stream changes into a denormalized read view [CQRS materialized projection]. In-memory composition works well for light traffic, while materialized views serve high-scale queries in single-digit milliseconds.

**📊 Quick comparison**
| Dimension | Database-per-Service | Shared Database |
| :--- | :--- | :--- |
| Coupling | Loose service decoupling | Tight schema lock-in |
| Migrations | Fully independent deployments | Risky coordinated table migrations |
| Scalability | Independent database horizontal scaling | Monolithic database connection bottleneck |
| Technology | Polyglot database selection | Single database vendor constraint |
| Consistency | Eventual consistency required | Immediate relational ACID guarantees |

**🔬 Under the hood (optional)**
Enforcing a database boundary eliminates cross-database transactions. Queries cannot hold shared lock latches across tables owned by different teams. This removes connection pool contention on the database engine and isolates memory buffer cache allocation to one bounded context.

---

## Q3: Why is Two-Phase Commit (2PC) usually avoided in distributed systems?
*Commonly asked at: Morgan Stanley, Amazon, Swiggy, Wells Fargo*

**⚡ One-line answer**
**Two-Phase Commit** is a distributed consensus protocol holding database locks across network boundaries, causing latency amplification and coordinator bottlenecks.

**🗣️ Spoken answer (30–45 seconds)**
**Two-Phase Commit** is a distributed consensus protocol executing prepare and commit phases synchronously across nodes. It is avoided because it holds distributed locks across the network during both phases. This causes **latency amplification**, which is compounding round-trip network delays across multiple remote participants. A slow participant or **coordinator failure**, a crash freezing participant locks indefinitely, leads to **connection starvation**, depleting database connection pools. Modern distributed architectures avoid cross-network locking entirely, choosing **eventual consistency**, where data replicas converge over time through asynchronous messaging.

**🎯 Terms the interviewer listens for**
- ⭐ **Two-Phase Commit** — distributed consensus protocol executing prepare and commit phases synchronously
- ⭐ **Latency amplification** — compounding round-trip network delays across multiple remote participants
- ⭐ **Eventual consistency** — data replicas converging to a consistent state over time
- **Coordinator failure** — crash of central coordinator freezing participant locks indefinitely
- **Connection starvation** — exhausting database connection pool threads waiting on locks
- **Distributed lock** — exclusive resource lock held across distinct physical network machines

**🧠 Memory hook**
A dinner group where nobody can leave until every single person completes a mobile payment simultaneously; one dead battery traps everyone.

**💻 Code**
```csharp
// ❌ Holding distributed row locks across network boundaries
using var scope = new TransactionScope(TransactionScopeAsyncFlowOption.Enabled);
await customerDb.DeductBalanceAsync(userId, amount); // Holds lock
await orderDb.CreateOrderAsync(order); // Holds second lock
scope.Complete(); // Network blip freezes connection pools!

// ✅ Discrete local transaction with asynchronous message dispatch
await orderDb.CreateOrderAsync(order);
await messagePublisher.PublishAsync(new OrderPlacedEvent(order.Id));
```

**⚠️ Likely follow-up**
*Q: What replaces Two-Phase Commit when coordinating distributed business transactions?*
A: Distributed architectures use ordered local transactions [Saga pattern]. Each service commits locally in its own database and triggers the next step through events or a workflow orchestrator. If a step fails, backward recovery actions [compensating transactions] undo prior business changes.

**📊 Quick comparison**
| Attribute | Two-Phase Commit (2PC) | Saga Pattern |
| :--- | :--- | :--- |
| Locking | Distributed network row locks | Local database transactions only |
| Consistency | Immediate ACID consistency | Eventual BASE consistency |
| Availability | Low during network partitions | High system availability |
| Throughput | Severely limited by latency | High parallel message throughput |
| Failure Handling | Synchronous coordinator rollback | Asynchronous compensating transactions |

**🔬 Under the hood (optional)**
Under 2PC, each participant writes a commit record to its write-ahead log during the prepare phase. The database retains in-doubt exclusive locks on affected rows until the coordinator sends the final commit message, blocking concurrent transactions on those storage pages.

---

## Q4: What is the Saga pattern, and what is the difference between choreography and orchestration?
*Commonly asked at: Swiggy, Flipkart, Walmart, JPMorgan*

**⚡ One-line answer**
**Saga** means a cross-service transaction coordinated as local steps with compensating rollbacks on failure.

**🗣️ Spoken answer (30–45 seconds)**
A **Saga** means a cross-service transaction coordinated as local steps with compensating rollbacks. In **choreography**, which is decentralized coordination where services autonomously publish and listen to events, there is no single controller. In **orchestration**, a central coordinator using a dedicated workflow state machine commands participants directly. If a step fails, the saga executes a **compensating transaction**, an explicit semantic undo operation reversing a previously committed local step. Orchestration is preferred for complex enterprise workflows because it provides centralized status visibility and avoids circular event loops.

**🎯 Terms the interviewer listens for**
- ⭐ **Saga** — cross-service transaction coordinated as local steps with compensating rollbacks
- ⭐ **Orchestration** — centralized coordination using a dedicated workflow state machine
- ⭐ **Choreography** — decentralized coordination where services autonomously publish and listen to events
- **Compensating transaction** — semantic undo operation reversing a previously committed local step
- **State machine** — centralized component tracking execution status and compensation steps
- **Idempotent retry** — repeating operations safely without duplicate business side effects

**🧠 Memory hook**
Choreography is a chaotic WhatsApp trip group where everyone texts updates; orchestration is a professional tour manager directing every booking step.

**💻 Code**
```csharp
// ❌ Choreography spaghetti: services listen to cascading event chains
public void Handle(PaymentApproved e) => _bus.Publish(new ShipOrder(e.Id));

// ✅ Orchestrated state machine executing steps with compensating actions
public async Task ExecuteSagaAsync(OrderState state, CancellationToken ct) {
    if (!await _paymentClient.ChargeAsync(state.OrderId, ct)) {
        await _inventoryClient.ReleaseReservationAsync(state.OrderId, ct);
    }
}
```

**⚠️ Likely follow-up**
*Q: When should a team choose choreography over orchestration?*
A: Choose decentralized event flows [choreography] for simple two-step workflows like sending welcome emails after user registration. For multi-step workflows like checkout or loan approval, central coordination [orchestration] prevents circular event loops and makes debugging step failures straightforward.

**📊 Quick comparison**
| Feature | Choreography | Orchestration |
| :--- | :--- | :--- |
| Coordination | Decentralized event pub-sub | Centralized workflow state machine |
| Coupling | Loose publisher-subscriber coupling | Orchestrator knows participant contracts |
| Visibility | Difficult to trace end-to-end | Single location inspects state |
| Complexity | High cognitive load at scale | Low cognitive workflow tracking |
| Best For | Simple 2 to 3 step flows | Complex multi-step business transactions |

**🔬 Under the hood (optional)**
Sagas do not provide ACID isolation. Concurrent transactions can read intermediate uncommitted business state. Systems mitigate this using semantic locking flags, such as marking an order status as PendingPayment, preventing other workflows from altering the entity until completion.

---

## Q5: What is a compensating transaction, and how does it differ from a database rollback?
*Commonly asked at: Barclays, TCS, Cognizant, Nagarro*

**⚡ One-line answer**
**Compensating transaction** means an application-level forward action that semantically reverses a previously committed local transaction.

**🗣️ Spoken answer (30–45 seconds)**
A **database rollback** is a storage engine abort discarding uncommitted write-ahead log operations before a transaction finishes. Once committed, data is permanent. A **compensating transaction** means a forward application action that semantically reverses a committed transaction. Instead of deleting rows, it applies a **semantic undo**, which is a business-level reversal creating compensating records like issuing a customer refund. This approach preserves an immutable **audit trail**, a chronological ledger recording both original charges and reversals, ensuring full financial traceability across microservice boundaries.

**🎯 Terms the interviewer listens for**
- ⭐ **Compensating transaction** — forward application action that semantically reverses a committed transaction
- ⭐ **Database rollback** — storage engine abort discarding uncommitted write-ahead log operations
- ⭐ **Semantic undo** — business-level reversal creating compensating records rather than deleting rows
- **Audit trail** — immutable chronological ledger preserving both original operations and refunds
- **Forward recovery** — driving a distributed saga forward through idempotent retries
- **Local transaction** — atomic ACID operation executed strictly inside one database boundary

**🧠 Memory hook**
A database rollback is hitting Backspace before printing; a compensating transaction is printing a credit note after the invoice was already issued.

**💻 Code**
```csharp
// ❌ Impossible: Attempting to rollback an already committed transaction
await paymentDb.RollbackCommittedPaymentAsync(chargeId); // Not supported!

// ✅ Compensating transaction: issue an explicit business refund
public async Task CompensateOrderAsync(Guid orderId, CancellationToken ct) {
    await _paymentClient.RefundChargeAsync(new RefundRequest(orderId), ct);
    await _orderRepo.UpdateStatusAsync(orderId, OrderStatus.Cancelled, ct);
}
```

**⚠️ Likely follow-up**
*Q: What happens if a compensating transaction fails halfway through?*
A: Sagas must never drop a failed compensating action. The coordinator uses automatic retries [idempotent retries] with exponential backoff until it succeeds. If repeated attempts fail due to external system outages, the failure is routed to a human operator queue [dead letter queue] for administrative review.

**📊 Quick comparison**
| Dimension | Database Rollback | Compensating Transaction |
| :--- | :--- | :--- |
| Execution Level | Storage engine transaction log | Application business service logic |
| Timing | Before transaction commits | After previous transaction committed |
| Mechanism | Erases dirty memory buffers | Inserts new compensating record |
| Audit History | Leaves no database record | Preserves complete financial audit |
| Scope | Single physical database | Multiple distributed microservice boundaries |

**🔬 Under the hood (optional)**
Database engines execute rollbacks by walking undo logs backwards to restore previous page images before releasing locks. Compensating transactions execute standard insert and update SQL statements, acquiring fresh row locks and generating new transaction log sequence numbers.

---

## Q6: What is the dual-write problem, and why does it risk data inconsistency?
*Commonly asked at: PhonePe, Zepto, Goldman Sachs, EPAM*

**⚡ One-line answer**
**Dual-write problem** means modifying a database and publishing to a message broker without atomicity, risking permanent data inconsistency.

**🗣️ Spoken answer (30–45 seconds)**
The **dual-write problem** means updating a database and publishing an event without distributed atomicity across systems. Because databases and brokers use separate connections, a **partial failure**, where one write succeeds while the other fails, corrupts state. If you commit the database first and crash, messages are lost forever. If you publish first and the database rolls back, you emit a **phantom event**, a message published for an operation that failed locally. This causes **data inconsistency**, a state divergence between database records and published events.

**🎯 Terms the interviewer listens for**
- ⭐ **Dual-write problem** — writing to database and message broker without distributed atomic guarantees
- ⭐ **Partial failure** — scenario where one system write succeeds while another fails
- ⭐ **Phantom event** — notification published for an operation that failed locally
- **Data inconsistency** — state divergence between primary database records and message brokers
- **Transactional outbox** — saving domain data and events within one database transaction
- **Atomic transaction** — all-or-nothing guarantee provided strictly within one storage engine

**🧠 Memory hook**
A restaurant waiter who takes your cash but forgets to hand the kitchen your food ticket before taking his lunch break; orders vanish.

**💻 Code**
```csharp
// ❌ Dual-write trap: Crash between lines causes permanent inconsistency
await _orderDbContext.Orders.AddAsync(order, ct);
await _orderDbContext.SaveChangesAsync(ct); // Database committed
// Crash here loses event forever!
await _messageBus.PublishAsync(new OrderCreatedEvent(order.Id), ct);

// ✅ Atomically persist entity and outbox record
await _orderDbContext.OutboxMessages.AddAsync(new OutboxMessage(order), ct);
await _orderDbContext.SaveChangesAsync(ct);
```

**⚠️ Likely follow-up**
*Q: Can distributed two-phase commit solve the dual-write issue reliably?*
A: While distributed transactions [XA / 2PC] theoretically bridge databases and brokers, most modern message systems like Apache Kafka and AWS SQS do not support 2PC coordinators. Even where supported, network latency and lock holding make it impractical for high-throughput production systems.

**📊 Quick comparison**
| Scenario | Outcome if API Crashes | Business Consequence |
| :--- | :--- | :--- |
| DB First, Bus Second | DB saved, message lost | Downstream services never fulfill order |
| Bus First, DB Second | Message sent, DB failed | Consumers process non-existent phantom orders |
| Dual-Write with 2PC | Holds distributed locks | Connection pool exhaustion under latency |
| Transactional Outbox | Atomic local ACID write | Guaranteed at-least-once message delivery |

**🔬 Under the hood (optional)**
TCP sockets to relational databases and Kafka brokers operate on separate OS file descriptors and wire protocols. Without a distributed coordinator protocol holding locks across both connections, neither system knows if the other connection successfully flushed packets to non-volatile disk storage.

---

## Q7: What is the Transactional Outbox pattern, and how does it prevent lost messages?
*Commonly asked at: Wells Fargo, Walmart, Swiggy, Accenture*

**⚡ One-line answer**
**Transactional outbox** means saving outgoing events into an outbox table in the same local transaction as business entities.

**🗣️ Spoken answer (30–45 seconds)**
The **transactional outbox** pattern means saving domain entities and outbound events in one local transaction to guarantee atomicity. Instead of publishing directly to Kafka, the application writes both records within a single database commit. Next, **Change Data Capture**, a mechanism streaming database log changes directly into message brokers automatically, tails the transaction log to publish messages without polling overhead. Alternatively, a background worker polls and relays messages. This guarantees **at-least-once delivery**, ensuring every published record arrives at least once, completely eliminating lost messages during crashes.

**🎯 Terms the interviewer listens for**
- ⭐ **Transactional outbox** — saving domain entities and outbound events in one local transaction
- ⭐ **Change Data Capture** — streaming database log changes directly into message brokers automatically
- ⭐ **At-least-once delivery** — messaging guarantee ensuring every published record arrives at least once
- **Polling publisher** — background worker querying unprocessed outbox records using skip-locked semantics
- **Outbox table** — dedicated relational table storing serialized event payloads before dispatch
- **Write-ahead log** — database storage journal recording sequential page mutations before disk writes

**🧠 Memory hook**
A chequebook with counterfoils; you write the check and record the stub in the same book before tearing out the payment.

**💻 Code**
```csharp
// ❌ Publishing directly to broker outside database transaction
await _db.SaveChangesAsync(ct);
await _kafka.ProduceAsync("orders", new Message { Value = orderJson }, ct);

// ✅ Save entity and outbox message atomically
using var tx = await _db.Database.BeginTransactionAsync(ct);
_db.Orders.Add(order);
_db.OutboxMessages.Add(new OutboxMessage("OrderCreated", orderJson));
await _db.SaveChangesAsync(ct);
await tx.CommitAsync(ct);
```

**⚠️ Likely follow-up**
*Q: How do you prevent multiple outbox publisher pods from processing the same row?*
A: Prevent multi-pod contention using read-past row locks [UPDLOCK, READPAST in SQL Server, or FOR UPDATE SKIP LOCKED in PostgreSQL]. Each worker pod locks and processes fifty rows while other pods skip directly to the next unlocked batch, preventing duplicate publishing and lock contention.

**📊 Quick comparison**
| Relay Mechanism | Latency | Database Query Overhead | Complexity |
| :--- | :--- | :--- | :--- |
| Periodic Polling | 1 to 5 seconds | Low to medium index queries | Very simple to implement |
| Polling with SKIP LOCKED | Sub-second polling | Light lock-free indexed queries | Moderate multi-pod safety |
| Change Data Capture (CDC) | Sub-100 milliseconds | Zero query load on database | Requires Debezium or Kafka Connect |

**🔬 Under the hood (optional)**
Change Data Capture tools like Debezium connect as replication clients to the database engine. In PostgreSQL, it reads the Write-Ahead Log (WAL); in SQL Server, it reads the active transaction log. It extracts outbox table row inserts without executing SQL SELECT queries against production tables.

---

## Q8: What is an idempotent consumer, and why is message deduplication required?
*Commonly asked at: Swiggy, Paytm, Zepto, Infosys*

**⚡ One-line answer**
**Idempotent consumer** means a message receiver that produces identical system state regardless of repeated duplicate deliveries.

**🗣️ Spoken answer (30–45 seconds)**
An **idempotent consumer** means a message receiver producing identical system state despite repeated duplicate deliveries. Message brokers like Kafka guarantee **at-least-once delivery**, a messaging guarantee ensuring messages arrive but allowing potential duplicates from network retries or consumer rebalances. Without idempotency, duplicate events cause double-charging or phantom orders. To prevent this, consumers implement a **deduplication inbox**, which is a database table tracking processed message identifiers to prevent duplicate execution. When an incoming message ID already exists, the consumer acknowledges it and skips business logic immediately.

**🎯 Terms the interviewer listens for**
- ⭐ **Idempotent consumer** — message receiver producing identical system state despite repeated duplicate deliveries
- ⭐ **At-least-once delivery** — messaging guarantee ensuring messages arrive, allowing potential duplicate deliveries
- ⭐ **Deduplication inbox** — database table tracking processed message identifiers to prevent duplicate execution
- **Idempotency key** — unique identifier used to detect and reject duplicate incoming requests
- **Natural key** — unique business attribute preventing duplicate entries via database constraints
- **Distributed cache** — high-speed key-value store performing atomic message existence checks

**🧠 Memory hook**
An elevator call button; pressing the button ten times illuminates the light once and brings the elevator to your floor only once.

**💻 Code**
```csharp
// ❌ Naive consumer charges repeatedly on duplicates
public async Task HandleAsync(OrderPlaced msg) => await _billing.ChargeAsync(msg);

// ✅ Check inbox table before applying side effects
public async Task HandleAsync(OrderPlaced msg, AppDbContext db, CancellationToken ct) {
    var exists = await db.Inbox.AnyAsync(x => x.MessageId == msg.Id, ct);
    if (exists) return; // Skip already processed duplicate
    await _billing.ChargeAsync(msg);
    db.Inbox.Add(new InboxRecord(msg.Id));
    await db.SaveChangesAsync(ct);
}
```

**⚠️ Likely follow-up**
*Q: How do you handle high-throughput idempotency when database writes are too slow?*
A: Use a fast in-memory store [Redis SET with NX and expiry]. Check and insert the message identifier atomically before processing. If Redis returns false, the message is currently in flight or completed. For final persistence consistency, back it with a database unique index.

**📊 Quick comparison**
| Deduplication Strategy | Performance | Durability | Best Use Case |
| :--- | :--- | :--- | :--- |
| Relational Inbox Table | 5 to 15 ms | High relational ACID guarantee | Financial ledgers, order billing |
| Redis Atomic SET NX | Sub-millisecond | Moderate in-memory cache | High-throughput webhooks, telemetry |
| Natural Domain Constraint | Zero overhead | Built into business tables | Unique email registration, payments |

**🔬 Under the hood (optional)**
In PostgreSQL or SQL Server, declaring `MessageId` as a unique clustered or B-Tree primary key causes duplicate inserts to throw unique key violation error 2627 or 23505. The consumer catches this specific database constraint error, rolls back the local transaction, and immediately acknowledges the broker message.

---

## Q9: What is CQRS (Command Query Responsibility Segregation)?
*Commonly asked at: Wells Fargo, EPAM, LTIMindtree, Nagarro*

**⚡ One-line answer**
**CQRS** means separating command write models from query read models to optimize and scale them independently.

**🗣️ Spoken answer (30–45 seconds)**
**CQRS** means separating command write operations from query read operations across distinct paths. The write side processes a **command**, an intent to mutate system state containing business payload and validation rules. The read side executes a **Query**, which is a read-only request retrieving data without modifying any underlying state. This pattern avoids complex relational joins by maintaining a **materialized view**, a pre-computed denormalized read model stored for sub-millisecond retrieval. Although it introduces eventual consistency, CQRS allows read and write models to scale horizontally and independently.

**🎯 Terms the interviewer listens for**
- ⭐ **CQRS** — architectural pattern separating command write operations from query read operations
- ⭐ **Command** — intent to mutate system state containing business payload and validation
- ⭐ **Query** — read-only request retrieving data without modifying any underlying state
- **Materialized view** — pre-computed denormalized read model stored for sub-millisecond retrieval
- **Eventual consistency** — asynchronous synchronization delay between write mutations and read projections
- **Asymmetric scaling** — scaling read replicas and write nodes independently according to traffic

**🧠 Memory hook**
A newspaper publisher; reporters write and edit articles in the editorial office, while millions of readers read the printed, formatted paper.

**💻 Code**
```csharp
// ❌ Mixing dashboard queries with transactional models
var report = await _orderDbContext.Orders.Include(o => o.Items).ToListAsync();

// ✅ Command mutates domain, Query reads projection
public record CreateOrderCommand(Guid Id, decimal Amount) : IRequest<bool>;
public record GetOrderSummaryQuery(Guid Id) : IRequest<OrderSummaryDto>;

// Fast Dapper query bypasses change tracking
public async Task<OrderSummaryDto> Handle(GetOrderSummaryQuery q, IDbConnection db) =>
    await db.QuerySingleAsync<OrderSummaryDto>("SELECT * FROM OrderSummaries WHERE Id=@Id", q);
```

**⚠️ Likely follow-up**
*Q: Does CQRS require using two separate physical databases?*
A: No, CQRS is a pattern, not a two-database mandate. You can implement CQRS within a single relational database by using normalized tables for commands and SQL views or separate reporting tables for queries. Separate datastores like Elasticsearch are added only when read traffic demands independent scaling.

**📊 Quick comparison**
| Aspect | Command Side (Write) | Query Side (Read) |
| :--- | :--- | :--- |
| Responsibility | State mutations, business invariants | Read-only data presentation |
| Optimization | Write latency, transaction integrity | Query speed, denormalized projections |
| Data Model | Normalized relational schema | Flattened JSON or key-value |
| Consistency | Strict immediate ACID consistency | Eventual consistency via events |
| Tools | Rich domain entities, EF Core | Fast micro-ORMs like Dapper |

**🔬 Under the hood (optional)**
Bypassing ORM change trackers on the query side eliminates snapshot allocation in memory. Using lightweight mapping queries directly streams row buffers from the TDS network stream into DTO memory structs, reducing Gen 0 allocations by up to 80% on high-traffic endpoints.

---

## Q10: What is an API Gateway, and why do microservices place one at the network edge?
*Commonly asked at: Cognizant, Wipro, TCS, Capgemini*

**⚡ One-line answer**
**API gateway** is a reverse proxy at the network edge providing routing, security, and protocol aggregation for clients.

**🗣️ Spoken answer (30–45 seconds)**
An **API gateway** is a single edge entry point reverse-proxying client traffic to backend microservices. Placing a **reverse proxy**, an intermediate edge server forwarding incoming client requests to backends, shields internal network topologies from public exposure. The gateway centralizes **cross-cutting concerns**, which are shared infrastructure features like authentication, TLS termination, and rate limiting. This offloads repetitive token validation and security policies from backend service teams. It can also aggregate multiple downstream responses into one payload, reducing mobile network round-trips and optimizing client bandwidth.

**🎯 Terms the interviewer listens for**
- ⭐ **API gateway** — single edge entry point reverse-proxying client traffic to backend microservices
- ⭐ **Reverse proxy** — intermediate edge server forwarding incoming client requests to backends
- ⭐ **Cross-cutting concerns** — shared infrastructure features like authentication, rate limiting, and telemetry
- **TLS termination** — decrypting encrypted HTTPS traffic at gateway edge before routing
- **BFF pattern** — backend-for-frontend gateways tailored specifically for individual client platform needs
- **YARP** — Microsoft high-performance .NET reverse proxy library for routing traffic

**🧠 Memory hook**
An airport main reception desk; travelers check in and clear security once before proceeding to individual flight gates.

**💻 Code**
```csharp
// ❌ Clients call internal microservices directly with exposed ports
// Browser calls: https://api.internal:5001/orders and https://api.internal:5002/users

// ✅ Gateway routes clients using Microsoft YARP
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));
var app = builder.Build();
app.MapReverseProxy();
```

**⚠️ Likely follow-up**
*Q: What is the risk of putting too much business logic inside an API Gateway?*
A: Overloading gateways with business rules creates a centralized deployment bottleneck [smart proxy anti-pattern]. Gateways should remain lightweight reverse proxies handling routing and security. Business domain validation belongs inside individual microservices, not inside gateway routing layers.

**📊 Quick comparison**
| Responsibility | Handled by API Gateway | Handled by Microservice |
| :--- | :--- | :--- |
| Authentication | Validates JWT signature at edge | Authorizes domain policy permissions |
| Routing | Reverse proxy path matching | Executes business domain workflow |
| Rate Limiting | IP and client request throttling | Resource-specific domain constraints |
| Data Persistence | Stateless, zero database access | Owns private relational/NoSQL DB |
| Protocol | Exposes public REST/JSON endpoints | Communicates internally via gRPC |

**🔬 Under the hood (optional)**
Microsoft YARP uses ASP.NET Core `System.IO.Pipelines` to stream HTTP bytes directly from client sockets to backend sockets without intermediate byte array allocations. This eliminates Large Object Heap pressure and minimizes Gen 0 garbage collection pauses under high concurrency.

---

## Q11: Why do internal microservices use gRPC instead of REST?
*Commonly asked at: Swiggy, Morgan Stanley, Barclays, Walmart*

**⚡ One-line answer**
**gRPC** is a high-performance remote procedure call framework using Protocol Buffers and HTTP/2 for low-latency service communication.

**🗣️ Spoken answer (30–45 seconds)**
Internal microservices choose **gRPC**, a high-performance remote procedure call framework using Protocol Buffers and HTTP/2, over REST for internal communication. REST relies on text-based JSON over HTTP/1.1, requiring heavy CPU parsing and multiple TCP connections. In contrast, gRPC uses **Protocol Buffers**, a compact binary serialization format packing strongly typed structured data efficiently. Furthermore, gRPC leverages **HTTP/2 multiplexing**, which is sending multiple concurrent requests bidirectionally over a single persistent TCP connection. This eliminates head-of-line blocking, slashes CPU serialization costs, and minimizes inter-service network latency under heavy loads.

**🎯 Terms the interviewer listens for**
- ⭐ **gRPC** — high-performance remote procedure call framework using Protocol Buffers and HTTP/2
- ⭐ **Protocol Buffers** — compact binary serialization format packing strongly typed structured data efficiently
- ⭐ **HTTP/2 multiplexing** — sending multiple concurrent requests bidirectionally over a single TCP connection
- **Contract-first design** — defining service schemas in proto files before generating client code
- **Head-of-line blocking** — network transmission bottleneck where slow requests block subsequent packet streams
- **HPACK compression** — header compression algorithm reducing repetitive HTTP header network overhead

**🧠 Memory hook**
REST is sending handwritten letters through postal mail; gRPC is two pilots talking in compressed military radio code over an open channel.

**💻 Code**
```csharp
// ❌ REST JSON text serialization over HTTP/1.1
var response = await httpClient.GetAsync($"https://orders/api/{id}");
var order = await response.Content.ReadFromJsonAsync<OrderDto>();

// ✅ gRPC binary serialization over multiplexed HTTP/2
var reply = await grpcClient.GetOrderAsync(new OrderRequest { Id = id });
```

**⚠️ Likely follow-up**
*Q: Why not use gRPC for public web browsers instead of REST?*
A: Web browsers lack low-level control over HTTP/2 framing, requiring translation proxies [gRPC-Web]. Additionally, public web clients require human-readable payloads, simple caching headers, and firewall compatibility, making standard REST over JSON the practical choice for public ingress APIs.

**📊 Quick comparison**
| Metric | REST over JSON | gRPC over Protobuf |
| :--- | :--- | :--- |
| Serialization | Text-based JSON parsing | Compact binary serialization |
| Protocol | HTTP/1.1 or HTTP/2 | Strictly HTTP/2 transport |
| Multiplexing | Limited connection reuse | True bidirectional stream multiplexing |
| Schema | Optional Swagger OpenAPI | Mandatory strict Proto IDL |
| Best For | Public external mobile/web clients | Internal high-throughput service mesh |

**🔬 Under the hood (optional)**
Protocol Buffers use varint encoding and tag-length-value binary formatting. Integers are compressed into variable byte sequences rather than ASCII characters. HTTP/2 frames binary payloads into discrete frames with HPACK header compression, avoiding TCP slow-start and reducing packet counts.

---

## Q12: What is the Circuit Breaker pattern, and what are its three operational states?
*Commonly asked at: Wells Fargo, Infosys, Capgemini, Accenture*

**⚡ One-line answer**
**Circuit breaker** means a stability pattern that fails fast during downstream outages to prevent cascading system failures.

**🗣️ Spoken answer (30–45 seconds)**
A **circuit breaker** means a resilience pattern failing fast during dependency outages to prevent cascading failure. In the **closed state**, the normal operating condition routing requests while tracking error rates, traffic flows unimpeded. When failures exceed a threshold, the breaker trips to the **open state**, which is a tripped condition failing calls immediately without sending downstream network traffic. This shields thread pools from timeout exhaustion. After a cooldown period, it enters **half-open state**, a trial condition allowing limited canary calls to test dependency recovery before resuming normal operations.

**🎯 Terms the interviewer listens for**
- ⭐ **Circuit breaker** — resilience pattern failing fast to prevent cascading system collapse
- ⭐ **Closed state** — normal operating condition routing requests while tracking error rates
- ⭐ **Open state** — tripped condition failing calls immediately without sending downstream network traffic
- **Half-open state** — trial condition allowing limited canary calls to test dependency recovery
- **Cascading failure** — chain reaction where one slow service exhausts caller thread pools
- **Fail-fast** — rejecting calls instantaneously to prevent blocking thread pools on timeouts

**🧠 Memory hook**
A household electrical breaker; it trips to cut electricity during a short circuit, preventing the entire house wiring from catching fire.

**💻 Code**
```csharp
// ❌ Hanging threads: every call waits 30s during outage
var res = await httpClient.GetAsync("https://slow-service/api");

// ✅ Polly v8 circuit breaker failing fast during outages
var pipeline = new ResiliencePipelineBuilder()
    .AddCircuitBreaker(new HttpCircuitBreakerStrategyOptions {
        FailureRatio = 0.5,
        SamplingDuration = TimeSpan.FromSeconds(10),
        BreakDuration = TimeSpan.FromSeconds(30)
    }).Build();
await pipeline.ExecuteAsync(async token => await httpClient.GetAsync(url, token));
```

**⚠️ Likely follow-up**
*Q: What is the difference between a Circuit Breaker and a Retry policy?*
A: A retry policy repeats requests hoping transient glitches clear. If a downstream service is down, immediate retries overwhelm the failing dependency [retry storm]. A circuit breaker detects sustained failure, stops all retries immediately, and lets the downstream service recover without load.

**📊 Quick comparison**
| Breaker State | Network Calls Allowed? | Behavior on Execution | Transition Trigger |
| :--- | :--- | :--- | :--- |
| Closed | Yes, all calls allowed | Executes call, counts failures | Error rate exceeds threshold |
| Open | No, all calls blocked | Throws BrokenCircuitException immediately | Break duration cooldown expires |
| Half-Open | Yes, limited trial calls | Tests downstream service health | Trials succeed → Closed |

**🔬 Under the hood (optional)**
Polly tracks failure ratios within a rolling sampling window using lock-free atomic counters. When the breaker trips to Open, it sets a timestamp marker. Subsequent threads check this timestamp in user-mode memory without performing I/O, throwing exceptions in nanoseconds to conserve CPU and thread pools.

---

## Q13: What is distributed tracing, and how does OpenTelemetry trace requests across services?
*Commonly asked at: Swiggy, JPMorgan, Nagarro, EPAM*

**⚡ One-line answer**
**Distributed tracing** means tracking request execution across multiple microservices by propagating a unique correlation trace identifier.

**🗣️ Spoken answer (30–45 seconds)**
**Distributed tracing** means a diagnostic observability method monitoring request lifecycles across distributed service boundaries. At the edge gateway, the system generates a **Trace ID**, a globally unique identifier correlating all operations across an end-to-end distributed transaction. Across services, each operation receives a **Span ID**, which is a unique identifier representing a single contiguous unit of execution. Using **context propagation**, injecting and extracting trace headers across network hops, **OpenTelemetry** exports linked spans to backends like Jaeger to pinpoint latency bottlenecks.

**🎯 Terms the interviewer listens for**
- ⭐ **Distributed tracing** — diagnostic observability method monitoring request lifecycles across service boundaries
- ⭐ **Trace ID** — globally unique identifier correlating operations across an end-to-end transaction
- ⭐ **Span ID** — unique identifier representing a single contiguous unit of service execution
- **Context propagation** — injecting and extracting trace metadata across network protocol boundaries
- **OpenTelemetry** — vendor-neutral observability framework standardizing traces, metrics, and logs
- **W3C Trace Context** — standard specification defining HTTP headers for distributed trace propagation

**🧠 Memory hook**
A courier tracking barcode; the package retains one tracking number, while each warehouse scans a checkpoint stamp as it moves across cities.

**💻 Code**
```csharp
// ❌ Missing correlation: downstream logs are disconnected and orphaned
_logger.LogInformation("Processing payment for order {OrderId}", orderId);

// ✅ OpenTelemetry automatic W3C traceparent propagation in .NET
builder.Services.AddOpenTelemetry()
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddOtlpExporter());
```

**⚠️ Likely follow-up**
*Q: What is the difference between a Trace ID and a Span ID?*
A: A Trace ID is the single global identifier for the entire end-to-end request journey across all microservices. A Span ID represents a single discrete leg of that journey inside one service, such as an SQL query or HTTP call, containing its own start and end timestamps.

**📊 Quick comparison**
| Concept | Scope | Generated At | Purpose |
| :--- | :--- | :--- | :--- |
| Trace ID | Global across entire journey | API Gateway entry point | Links all logs and spans |
| Span ID | Local to one operation | Start of individual step | Measures latency of step |
| traceparent | W3C HTTP header format | Outgoing client request | Propagates IDs across network |
| Baggy / Baggage | Key-value pairs across hops | Originating service | Shares contextual tenant metadata |

**🔬 Under the hood (optional)**
The W3C `traceparent` header uses a four-field format: `00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`. This represents version, 16-byte Trace ID, 8-byte parent Span ID, and 1-byte trace flags indicating whether sampling was enabled for the request.

---

## Q14: How does an end-to-end checkout flow handle inventory, payment, and failure?
*Commonly asked at: Flipkart, Swiggy, Wells Fargo, Walmart*

**⚡ One-line answer**
**Saga orchestrator** means a centralized coordinator managing multi-service workflows and executing compensating actions upon intermediate failures.

**🗣️ Spoken answer (30–45 seconds)**
The checkout flow relies on a **Saga orchestrator**, a centralized coordinator managing multi-service workflows and executing compensating actions. The order service sets a **semantic state**, which is a business status flag like Pending or Cancelled managing intermediate progress. The orchestrator first calls inventory to reserve stock, then invokes payment. If the payment gateway fails, the orchestrator triggers a **compensating transaction**, an explicit semantic undo action reversing previously committed state by releasing reserved inventory. Finally, the order updates to Cancelled, ensuring data consistency across distributed boundaries without distributed locks.

**🎯 Terms the interviewer listens for**
- ⭐ **Saga orchestrator** — centralized coordinator managing multi-service workflows and executing compensating actions
- ⭐ **Compensating transaction** — semantic undo action reversing previously committed state after failures
- ⭐ **Semantic state** — business status flags like Pending or Cancelled managing intermediate progress
- **Idempotent consumer** — message handler producing identical state despite duplicate deliveries
- **Transactional outbox** — atomically persisting domain entities and outbound events within local transactions
- **Dead-letter queue** — secondary queue isolating persistently failing messages for manual engineering investigation

**🧠 Memory hook**
A wedding planner booking the church, banquet hall, and caterer; if the caterer cancels, the planner automatically refunds the hall and church bookings.

**💻 Code**
```csharp
// ❌ Fire-and-forget without compensation leaves reserved stock orphaned
await _inventory.ReserveAsync(orderId);
await _payment.ChargeAsync(orderId); // Fails, stock stays locked forever!

// ✅ Orchestrated workflow executing compensating action on payment failure
if (!await _payment.ChargeAsync(orderId, ct)) {
    await _inventory.ReleaseStockAsync(orderId, ct);
    await _orderRepo.MarkCancelledAsync(orderId, ct);
}
```

**⚠️ Likely follow-up**
*Q: How do you prevent overselling during flash sale traffic spikes?*
A: Buffer incoming checkout requests through an in-memory atomic cache [Redis DECR]. Decrement stock atomically before creating database orders. If Redis drops below zero, reject the request immediately at the ingress tier without touching backend databases or initiating payment calls.

**📊 Quick comparison**
| Checkout Step | Primary Action | Compensating Action |
| :--- | :--- | :--- |
| 1. Order Service | Create order with Pending status | Mark order status as Cancelled |
| 2. Inventory Service | Reserve item stock quantities | Release reserved item stock |
| 3. Payment Service | Charge customer card or UPI | Issue customer payment refund |
| 4. Shipping Service | Create dispatch delivery label | Cancel courier pickup manifest |

**🔬 Under the hood (optional)**
High-throughput checkout engines decouple the public API from relational databases. Gateway requests write to Kafka partitioned by Customer ID. Dedicated consumer pods process orders in strict sequential order per customer, eliminating concurrency race conditions on account balances and inventory lines.
