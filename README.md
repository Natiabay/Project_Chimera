# Project Chimera

Autonomous Influencer Network — FastRender Swarm (Planner–Worker–Judge), MCP-only external calls, and Coinbase AgentKit for agentic commerce.

## Features

- **MCP-first**: All external APIs (social, news, memory, wallet) via Model Context Protocol.
- **Planner–Worker–Judge**: Decompose goals → execute tasks → validate outputs.
- **CFO Judge**: Budget governance and transaction approval (FR 5.2).
- **Skills**: `skill_fetch_trends`, `skill_generate_content`, `skill_execute_transaction`.

## Quick Start

```bash
# Clone and setup
git clone <repo>
cd Project_Chimera
cp .env.example .env   # Add your API keys
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API: http://localhost:8000  
- Docs: http://localhost:8000/docs  
- Health: http://localhost:8000/health  

## Structure

- `app/` — FastAPI app, `models/`, `services/`, `routers/`, `utils/`
- `skills/` — Agent skills (trends, content, transaction)
- `mcp-servers/` — MCP servers (e.g. Weaviate)
- `specs/` — SRS, technical and functional specs
- `tests/` — `unit/`, `integration/`, `e2e/`
- `k8s/` — Kubernetes manifests
- `monitoring/` — Prometheus alerts, Grafana dashboard

## Tests

```bash
uv run pytest tests/ -v
uv run pytest tests/unit/ -v
uv run pytest tests/integration/ -v
```

## Deployment

- **Docker**: `docker build -t project-chimera .`
- **Compose (prod)**: `docker-compose -f docker-compose.prod.yml up -d`
- **Kubernetes**: `kubectl apply -k k8s/`

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) and [specs/](specs/) for details.

## License

MIT — see [LICENSE](LICENSE).
