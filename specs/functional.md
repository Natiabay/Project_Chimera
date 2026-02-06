# Functional Requirements (From SRS)

## Cognitive Core (FR 1.0-1.2)
- FR 1.0: Persona via SOUL.md file (YAML frontmatter + markdown)
- FR 1.1: Hierarchical memory (Redis + Weaviate)
- FR 1.2: Dynamic persona evolution via Judge

## Perception System (FR 2.0-2.2)
- FR 2.0: Active MCP Resource monitoring (twitter://, news://)
- FR 2.1: Semantic filtering with 0.75 threshold
- FR 2.2: Trend detection via background Worker

## Creative Engine (FR 3.0-3.2)
- FR 3.0: Multimodal generation via MCP Tools
- FR 3.1: Character consistency lock (LoRA/style ID)
- FR 3.2: Hybrid video rendering (Tier 1: Static+Motion, Tier 2: Full)

## Action System (FR 4.0-4.1)
- FR 4.0: Platform-agnostic publishing via MCP Tools
- FR 4.1: Bi-directional interaction loop (Ingest→Plan→Generate→Act→Verify)

## Agentic Commerce (FR 5.0-5.2)
- FR 5.0: Non-custodial wallet management (Coinbase AgentKit)
- FR 5.1: Autonomous on-chain transactions (native_transfer, deploy_token)
- FR 5.2: Budget governance via CFO Judge sub-agent

## Orchestration (FR 6.0-6.1)
- FR 6.0: Planner-Worker-Judge services
- FR 6.1: Optimistic Concurrency Control (OCC)
