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
A monolith runs all domain features in a single process, whereas microservices split capabilities into autonomous services with private databases communicating over network protocols.

**🗣️ Spoken answer (30–45 seconds)**
A monolith bundles every feature into one deployable unit and shared database. Microservices split the application into autonomous services organized around business domains. Each service strictly owns its private database and communicates over APIs or messaging. In production, teams can deploy catalog updates independently without risking payment flows. If one service fails, the remaining system remains available and healthy. However, you trade single-server simplicity for distributed network latency and tracing overhead.

**🎯 Terms the interviewer listens for**
- ⭐ **Monolithic Architecture**: Single process containing all application business capabilities.
- ⭐ **Microservices Architecture**: Autonomous, independently deployable services organized around domains.
- ⭐ **Bounded Context**: Explicit boundary defining domain model ownership.
- **Database-per-Service**: Persistence encapsulation preventing direct cross-service table access.
- **Loose Coupling**: Services interact strictly through published contracts without dependencies.
- **High Cohesion**: Related business logic changes together within same service.

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
Each microservice must own its private database to ensure loose coupling, independent schema migrations, and prevent cross-team locking bottlenecks in production.

**🗣️ Spoken answer (30–45 seconds)**
In microservices, each service must exclusively encapsulate its own database. Direct cross-database queries or shared tables create hidden coupling across domain teams. When one team alters a column, dependent services break without warning. Sharing tables also creates database lock contention across independent services. Encapsulating persistence ensures services can evolve their schemas and scale independently. Teams also gain the freedom to select specialized storage engines like relational or document stores.

**🎯 Terms the interviewer listens for**
- ⭐ **Database-per-Service**: Architectural pattern where each service owns its persistence exclusively.
- ⭐ **Polyglot Persistence**: Selecting different storage technologies tailored for specific domain requirements.
- ⭐ **Encapsulation**: Hiding internal data structures behind strictly defined API boundaries.
- **Schema Evolution**: Modifying database columns without impacting external calling services.
- **Shared Database**: Tightly coupled pattern sharing tables across multiple service boundaries.
- **API Composition**: Assembling responses in memory across multiple independent service calls.

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
Two-Phase Commit is usually avoided in distributed systems because it holds database locks across the network, amplifying latency and risking coordinator failure.

**🗣️ Spoken answer (30–45 seconds)**
Two-Phase Commit is usually avoided in distributed systems because it holds locks across the network. The coordinator asks all nodes to prepare, holding row locks until all participants vote. If a network delay occurs or a node stalls, locks remain open indefinitely. This exhausts database connection pools and blocks incoming user traffic. In distributed systems, network partitions make synchronous locking impractical. Modern systems prefer eventual consistency using compensating transactions rather than distributed locking.

**🎯 Terms the interviewer listens for**
- ⭐ **Two-Phase Commit**: Distributed consensus protocol executing prepare and commit phases synchronously.
- ⭐ **Network Latency Amplification**: Compounding round-trip delays across multiple remote service coordinators.
- ⭐ **Single Point of Failure**: System vulnerability where coordinator outage freezes all participant resources.
- **Distributed Lock**: Exclusive resource lock held across distinct physical network machines.
- **Connection Starvation**: Depletion of database connection pool threads waiting on locks.
- **Eventual Consistency**: State convergence across distributed services over time without locks.

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
The Saga pattern coordinates distributed transactions as a series of local database transactions, using compensating transactions on failure and idempotent retries for forward progress.

**🗣️ Spoken answer (30–45 seconds)**
The Saga pattern manages long-running distributed workflows using discrete local transactions. In choreography, services react autonomously to published domain events without a central coordinator. In orchestration, a dedicated state machine explicitly commands each participant service. If any step fails, the Saga runs compensating transactions to semantically undo completed steps. Forward progress relies on idempotent retries to handle transient network hiccups. Orchestration is preferred for complex enterprise workflows because it provides centralized state visibility.

**🎯 Terms the interviewer listens for**
- ⭐ **Saga Pattern**: Sequence of local transactions updating services and publishing events.
- ⭐ **Saga Orchestration**: Central coordinator commanding participant services through explicit message requests.
- ⭐ **Saga Choreography**: Decentralized pub-sub flow where services react independently to events.
- **Compensating Transaction**: Semantic undo operation reversing a previously committed local transaction.
- **Idempotent Retries**: Repeating operations safely without duplicating business side effects.
- **State Machine**: Explicit tracker maintaining current step, status, and rollback state.

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
A compensating transaction is an application-level forward action that semantically reverses a committed local transaction, unlike a database rollback which undoes uncommitted writes.

**🗣️ Spoken answer (30–45 seconds)**
A database rollback undoes uncommitted writes in memory or transaction logs before a commit completes. Once a microservice commits data to its database, that transaction is permanent. A compensating transaction is a new business action that semantically reverses the previous action. For example, if a payment succeeds but inventory fails, the payment service issues a refund transaction. It does not delete the original charge row from the database. Instead, it creates an explicit refund record, preserving an accurate audit ledger.

**🎯 Terms the interviewer listens for**
- ⭐ **Compensating Transaction**: Explicit semantic undo operation executed after a transaction commits.
- ⭐ **Database Rollback**: Storage engine abort discarding uncommitted write-ahead log operations.
- ⭐ **Audit Trail**: Immutable historical ledger recording both operations and refunds.
- **Forward Recovery**: Driving a failing distributed workflow forward toward consistent resolution.
- **Semantic Undo**: Business-level reversal such as refunding a charged credit card.
- **Local Transaction**: Atomic ACID unit executed strictly inside one database boundary.

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
The dual-write problem occurs when updating a database and publishing a message to a broker without atomicity, risking permanent data inconsistency on partial failure.

**🗣️ Spoken answer (30–45 seconds)**
The dual-write problem happens when a service must modify a database and notify an external message broker. Because the database and message broker are separate distributed systems, they cannot share a local transaction. If you commit to the database first, a crash before messaging loses the event. Downstream microservices never learn about the update. If you publish to the broker first, a database error produces phantom events for operations that never existed. In production, this breaks order fulfillment and creates irreconcilable ledger mismatches.

**🎯 Terms the interviewer listens for**
- ⭐ **Dual-Write Problem**: Writing to two distinct distributed storage systems without atomic guarantees.
- ⭐ **Partial Failure**: Distributed scenario where one system succeeds while another fails.
- ⭐ **Data Inconsistency**: State mismatch between primary database tables and event brokers.
- **Phantom Event**: Notification published for a business transaction that failed locally.
- **Lost Notification**: Committed business data that was never broadcast to consumers.
- **Atomic Transaction**: All-or-nothing guarantee provided strictly within one storage engine.

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
The Transactional Outbox pattern saves outgoing messages into an outbox table in the same local transaction as business data, relaying them reliably to the broker.

**🗣️ Spoken answer (30–45 seconds)**
The Transactional Outbox pattern guarantees reliable messaging without distributed two-phase commit. Instead of publishing to Kafka directly, the service writes the domain entity and an outbox message into the same database transaction. This guarantees atomic persistence using local database ACID properties. An asynchronous publisher worker then reads unpublished outbox rows and relays them to the message broker. Change Data Capture can also tail the database transaction log directly. This eliminates lost notifications and ensures at-least-once delivery to downstream consumers.

**🎯 Terms the interviewer listens for**
- ⭐ **Transactional Outbox Pattern**: Saving domain data and outbound events in one local transaction.
- ⭐ **Change Data Capture**: Streaming database log changes directly into message brokers automatically.
- ⭐ **At-Least-Once Delivery**: Messaging guarantee ensuring every published record arrives at least once.
- **Local Transaction**: Atomic database commit ensuring all internal writes succeed together.
- **Polling Publisher**: Background worker querying unprocessed outbox records using skip-locked semantics.
- **Write-Ahead Log**: Database storage journal recording sequential page mutations before disk writes.

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
An idempotent consumer produces identical business state regardless of whether a message is processed once or multiple times, preventing duplicate operations like double charging.

**🗣️ Spoken answer (30–45 seconds)**
Message brokers like Kafka and RabbitMQ guarantee at-least-once delivery, not exactly-once delivery. Network retries, consumer restarts, and rebalancing frequently deliver duplicate messages to consumers. Downstream microservices must be idempotent so reprocessing produces the exact same state without duplicate side effects. Consumers implement deduplication using unique database constraints or fast distributed cache keys. When an incoming message ID already exists in the processed inbox table, the consumer acknowledges and skips execution. This safeguards systems against double debits and duplicate orders.

**🎯 Terms the interviewer listens for**
- ⭐ **Idempotent Consumer**: Message receiver producing identical system state despite repeated duplicate deliveries.
- ⭐ **At-Least-Once Delivery**: Broker guarantee ensuring messages arrive, allowing potential duplicate deliveries.
- ⭐ **Deduplication Inbox**: Database table tracking processed message identifiers to prevent duplicate execution.
- **Idempotency Key**: Unique client-supplied identifier used to detect duplicate incoming requests.
- **Consumer Rebalance**: Kafka partition reassignment causing re-delivery of uncommitted batch messages.
- **Natural Key**: Domain identifier used for unique database constraint enforcement.

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
CQRS separates read and write models into distinct data paths, allowing independent optimization, scaling, and schema modeling for updates versus queries.

**🗣️ Spoken answer (30–45 seconds)**
CQRS separates write operations from read queries. The write side processes commands, validates rich business rules, and saves normalized data into a transactional store. The read side serves queries from denormalized views optimized for presentation screens. This eliminates complex relational joins on operational databases. In high-scale systems, writes emit domain events to synchronize read replicas asynchronously. While CQRS introduces eventual consistency between models, it allows write and read tiers to scale horizontally and independently.

**🎯 Terms the interviewer listens for**
- ⭐ **CQRS**: Architectural pattern separating command write operations from query read operations.
- ⭐ **Command**: Intention to mutate system state containing business payload and validation.
- ⭐ **Query**: Read-only request retrieving data without modifying any underlying state.
- **Materialized View**: Pre-computed denormalized read model stored for sub-millisecond retrieval.
- **Eventual Consistency**: Asynchronous delay before write mutations appear on read projections.
- **MediatR Pipeline**: In-process messaging mediator decoupling command and query dispatching logic.

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
An API Gateway is a reverse proxy at the network edge providing unified routing, authentication offloading, rate limiting, and response aggregation for client applications.

**🗣️ Spoken answer (30–45 seconds)**
An API Gateway sits between external clients and backend microservices as a reverse proxy. It provides a single public domain endpoint, shielding internal network topologies. The gateway offloads cross-cutting concerns like TLS termination, JWT token validation, rate limiting, and CORS handling. This prevents every downstream service team from reinventing authentication logic. It also supports API composition, aggregating multiple microservice calls into one response for mobile clients. In modern .NET architectures, Microsoft YARP provides high-throughput reverse proxy routing.

**🎯 Terms the interviewer listens for**
- ⭐ **API Gateway**: Edge reverse proxy routing external requests to internal microservices.
- ⭐ **Cross-Cutting Concerns**: Shared infrastructure capabilities like authentication, logging, and rate limiting.
- ⭐ **Reverse Proxy**: Server forwarding client network requests to backend destination servers.
- **TLS Termination**: Decrypting HTTPS traffic at gateway edge before internal routing.
- **BFF Pattern**: Backend-for-Frontend gateways tailored specifically for mobile or web clients.
- **YARP**: Yet Another Reverse Proxy, Microsoft high-performance .NET reverse proxy.

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
Internal microservices use gRPC over HTTP/2 with Protocol Buffers because binary serialization delivers higher throughput, lower latency, and strict type safety over REST.

**🗣️ Spoken answer (30–45 seconds)**
Internal microservices prefer gRPC over REST for high-throughput service communication. REST uses human-readable JSON over HTTP/1.1, requiring heavy string parsing and opening new TCP connections per request. In contrast, gRPC uses binary Protocol Buffers over HTTP/2. This shrinks payload sizes significantly and enables multiplexing thousands of concurrent calls over a single TCP connection. Contracts are strictly enforced using Proto files, providing automatic cross-language client generation. In production, this cuts inter-service network latency and reduces server CPU serialization overhead.

**🎯 Terms the interviewer listens for**
- ⭐ **gRPC**: High-performance remote procedure call framework using HTTP/2 and Protobuf.
- ⭐ **Protocol Buffers**: Language-neutral binary serialization format compacting structured payload data.
- ⭐ **HTTP/2 Multiplexing**: Sending concurrent requests bidirectionally over a single persistent TCP connection.
- **Contract-First Design**: Defining interface contracts using proto files before implementing services.
- **Head-of-Line Blocking**: Network delay where one slow request blocks subsequent requests.
- **HPACK Header Compression**: Compressing HTTP headers to eliminate redundant network wire overhead.

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
The Circuit Breaker pattern prevents cascading system collapse by failing fast when a downstream dependency fails, automatically recovering when the service becomes healthy.

**🗣️ Spoken answer (30–45 seconds)**
The Circuit Breaker pattern prevents cascading failures when downstream dependencies experience outages. In the Closed state, requests pass through normally while monitoring error rates. When consecutive failures exceed a configured threshold, the breaker trips to the Open state. In Open state, calls fail fast immediately without making network calls, shielding upstream thread pools from timeout exhaustion. After a cooldown duration, the breaker enters Half-Open state, allowing trial requests through. If trials succeed, it returns to Closed; if they fail, it reopens.

**🎯 Terms the interviewer listens for**
- ⭐ **Circuit Breaker Pattern**: Resilience pattern that detects failures and encapsulates failing logic.
- ⭐ **Closed State**: Normal operational state routing requests and tracking failure rates.
- ⭐ **Open State**: Tripped state failing calls immediately without reaching out downstream.
- **Half-Open State**: Trial state sending limited canary requests to test recovery.
- **Fail-Fast**: Rejecting calls instantaneously to avoid blocking threads on timeouts.
- **Cascading Failure**: Chain reaction where one slow service exhausts threads across callers.

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
Distributed tracing tracks the complete lifecycle of a request across microservices by propagating a unique Trace ID across all network hops via standard headers.

**🗣️ Spoken answer (30–45 seconds)**
In microservices, a single user request traverses multiple independent services. Finding the root cause of an error in disconnected server logs is challenging. Distributed tracing assigns every incoming request a unique Trace ID at the gateway. Services propagate this identifier across HTTP or gRPC hops using W3C Trace Context headers. Each service records its local execution duration under a child Span ID. OpenTelemetry exports these traces to backends like Jaeger, allowing engineers to visualize latency bottlenecks across systems.

**🎯 Terms the interviewer listens for**
- ⭐ **Distributed Tracing**: Diagnostic technique monitoring requests across distributed multi-service network boundaries.
- ⭐ **Trace ID**: Globally unique identifier linking all operations across an end-to-end flow.
- ⭐ **Span ID**: Unique identifier representing a single unit of contiguous service work.
- **W3C Trace Context**: Standard HTTP header format propagating traceparent and tracestate headers.
- **OpenTelemetry**: Vendor-neutral observability framework collecting metrics, logs, and distributed traces.
- **Context Propagation**: Injecting and extracting trace metadata across network protocol boundaries.

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
An end-to-end checkout flow coordinates inventory reservation, payment processing, and notification through an orchestrated Saga, triggering compensating rollbacks if any step fails.

**🗣️ Spoken answer (30–45 seconds)**
The checkout flow begins when an API Gateway receives an order request and forwards it to the Order Service. The Order Service creates an order record in Pending state and starts a Saga orchestrator. First, the orchestrator reserves stock in the Inventory Service. Next, it commands the Payment Service to charge the customer. If the payment gateway fails, the orchestrator invokes a compensating transaction on the Inventory Service to release reserved stock. Finally, it updates the order status to Cancelled and notifies the customer via messaging.

**🎯 Terms the interviewer listens for**
- ⭐ **Saga Orchestrator**: Central service coordinating discrete transactional steps across business microservices.
- ⭐ **Compensating Action**: Reversible undo operation executed when a downstream step fails.
- ⭐ **Semantic Status**: Business state indicators like Pending or Cancelled managing intermediate progress.
- **Idempotent Ingress**: Preventing duplicate order placement by checking unique client submission keys.
- **Dead-Letter Queue**: Secondary queue capturing persistently failing messages for manual engineering triage.
- **Transactional Outbox**: Storing events atomically alongside local domain mutations for guaranteed delivery.

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
