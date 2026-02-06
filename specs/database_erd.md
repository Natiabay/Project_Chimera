# Database ERD — Project Chimera

Executable specification: Entity-Relationship view of PostgreSQL and linked stores.  
**Referred from:** [technical.md](technical.md#databaseschemas)

## PostgreSQL (Operational Data)

```mermaid
erDiagram
    agents ||--o{ campaigns : "has"
    agents ||--o{ content : "creates"
    agents ||--o{ transactions : "executes"
    campaigns ||--o{ tasks : "contains"
    campaigns ||--o{ content : "produces"

    agents {
        string id PK
        string name
        string persona_id
        string wallet_address
        string soul_md_path
        json voice_traits
        json directives
        boolean is_active
        float daily_budget
        float spent_today
        int total_posts
        int total_engagement
        float total_revenue
        datetime created_at
        datetime updated_at
    }

    campaigns {
        string id PK
        string agent_id FK
        string name
        string description
        string goal
        string niche
        float total_budget
        float spent_budget
        string status
        float confidence_threshold
        datetime start_date
        datetime end_date
        datetime created_at
    }

    tasks {
        string id PK
        string campaign_id FK
        string task_type
        string priority
        string status
        json input_data
        json output_data
        string assigned_worker
        float confidence_score
        string judge_decision
        datetime started_at
        datetime completed_at
        datetime created_at
    }

    content {
        string id PK
        string agent_id FK
        string campaign_id FK
        string content_type
        string platform
        string text_content
        json media_urls
        float generation_cost
        datetime published_at
        boolean disclosure_flag
        int impressions
        int likes
        datetime created_at
    }

    transactions {
        string id PK
        string agent_id FK
        string transaction_type
        string network
        string token_symbol
        float amount
        string transaction_hash
        string status
        boolean cfo_approved
        boolean budget_check_passed
        datetime created_at
    }
```

## Store Purposes (Reference)

| Store      | Purpose |
|-----------|---------|
| PostgreSQL | Agents, campaigns, tasks, content, transactions (above ERD) |
| Weaviate  | Agent memories, persona definitions, world knowledge |
| Redis     | Episodic cache, task queues |
| OnChain   | Immutable financial transaction ledger |
