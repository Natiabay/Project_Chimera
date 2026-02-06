# Technical Schemas (From SRS)

**Executable specs (linked):**
- **API:** [openapi.json](openapi.json) — generated from FastAPI; run `uv run python scripts/generate_openapi.py`
- **Database ERD:** [database_erd.md](database_erd.md) — PostgreSQL entity-relationship diagram (Mermaid)
- **MCP interface contract:** [mcp_interface_schema.json](mcp_interface_schema.json) — Runtime MCP tools/resources contract

---

## AgentTaskSchema
Payload between Planner and Worker (FR 6.0).

```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://twitter/mentions/123", "mcp://memory/recent"]
  },
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}
```

## MCPToolSchema
Standard MCP tool definition (SRS Section 6.2).

```json
{
  "name": "post_content",
  "description": "Publishes text and media to a connected social platform",
  "inputSchema": {
    "type": "object",
    "properties": {
      "platform": {
        "type": "string",
        "enum": ["twitter", "instagram", "threads"]
      },
      "text_content": {
        "type": "string",
        "description": "The body of the post/tweet"
      },
      "media_urls": {
        "type": "array",
        "items": { "type": "string" }
      },
      "disclosure_level": {
        "type": "string",
        "enum": ["automated", "assisted", "none"]
      }
    },
    "required": ["platform", "text_content"]
  }
}
```

## DatabaseSchemas
See **[database_erd.md](database_erd.md)** for the full PostgreSQL ERD (Mermaid). Summary:

| Store | Purpose |
|-------|---------|
| Weaviate | Agent memories, persona definitions, world knowledge |
| PostgreSQL | User data, campaign configs, operational logs (see ERD) |
| Redis | Episodic cache, task queues (Celery/BullMQ) |
| OnChain | Immutable financial transaction ledger |
