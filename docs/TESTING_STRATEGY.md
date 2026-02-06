# Testing Strategy — Project Chimera

## TDD (Test-Driven Development)

We follow **True TDD**: failing tests exist **before** implementation and define the agent’s goal posts.

- **Unit tests** (`tests/unit/`): Model contracts, skill interfaces, utilities. Each test is tied to an SRS **Functional Requirement (FR)** where applicable.
- **Integration tests** (`tests/integration/`): API endpoints, MCP tool contracts. Tests may intentionally fail until the implementation meets the spec.
- **E2E tests** (`tests/e2e/`): Full Planner → Worker → Judge workflow.

## FR Traceability

Tests reference the SRS explicitly, e.g.:

- `FR 1.0`: Persona / AgentPersona
- `FR 2.0, 2.1`: Trend fetching, semantic filtering
- `FR 3.0, 3.1`: Content generation contract
- `FR 4.0`: MCP tool standardization (post_content schema)
- `FR 5.2`: CFO Judge budget enforcement
- `FR 6.0`: Planner–Worker–Judge task schema

## Intentional Failures

Some tests use `assert True == False` or expect exceptions until the feature is implemented. This is by design: the test defines the contract; implementation is done to make the test pass.

## Running Tests

```bash
uv run pytest tests/ -v
uv run pytest tests/unit/ -v
uv run pytest tests/integration/ -v
uv run pytest tests/e2e/ -v
```

CI runs all tests (including inside Docker) and lint/security checks.
