# Architecture Strategy — Project Chimera

## High-Level Architecture

```mermaid
flowchart TB
    subgraph External
        MCP[MCP Servers]
        News[News API]
        Weaviate[Weaviate]
        Coinbase[Coinbase AgentKit]
    end
    subgraph Chimera API
        FastAPI[FastAPI]
        Planner[Planner Service]
        Worker[Worker Service]
        Judge[Judge Service]
        CFO[CFO Service]
    end
    subgraph Data
        PG[(PostgreSQL)]
        Redis[(Redis)]
    end
    FastAPI --> Planner
    FastAPI --> Worker
    FastAPI --> Judge
    FastAPI --> CFO
    Planner --> Worker
    Worker --> Judge
    Worker --> MCP
    Worker --> News
    Worker --> Weaviate
    CFO --> Coinbase
    FastAPI --> PG
    FastAPI --> Redis
```

## Planner–Worker–Judge (FastRender Swarm)

```mermaid
sequenceDiagram
    participant User
    participant Planner
    participant Worker
    participant Judge
    participant CFO
    User->>Planner: Goal
    Planner->>Planner: Decompose into tasks
    Planner->>Worker: Task list
    loop For each task
        Worker->>Worker: Execute (skills + MCP)
        Worker->>Judge: Output
        Judge->>Judge: Validate (confidence)
        alt Financial task
            Worker->>CFO: check_budget
            CFO->>Worker: approved/rejected
        end
    end
    Worker->>User: Results
```

## Data Flow

| Layer        | Responsibility                          |
|-------------|------------------------------------------|
| **API**     | FastAPI routers, health, metrics         |
| **Services**| Planner, Worker, Judge, CFO (business logic) |
| **Skills**  | fetch_trends, generate_content, execute_transaction |
| **MCP**     | All external calls (no direct APIs)      |
| **Data**    | PostgreSQL (ops), Weaviate (memory), Redis (cache) |

## Decisions

- **MCP-only external calls**: Ensures platform-agnostic publishing and testability.
- **CFO Judge**: All financial flows pass budget and anomaly checks before execution.
- **Skills vs MCP**: Skills are Python modules; MCP exposes tools/resources. Skills use MCP.
