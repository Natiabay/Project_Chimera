# Project Chimera — File & Structure Summary

This document summarizes the repo layout and how the News API is integrated so you can understand the project at a glance.

---

## 1. High-level architecture (diagram)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           PROJECT CHIMERA                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│   ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────────────┐  │
│   │   .cursor/  │     │   app/       │     │   skills/                        │  │
│   │   MCP &     │     │   FastAPI    │────▶│   skill_fetch_trends  ◀── .env   │  │
│   │   rules     │     │   health     │     │   (uses NEWSDATA_API_KEY)        │  │
│   └─────────────┘     └──────┬───────┘     │   skill_generate_content         │  │
│                              │             │   skill_execute_transaction      │  │
│                              │             └─────────────────────────────────┘  │
│                              │                           │                       │
│                              ▼                           ▼                       │
│   ┌─────────────┐     ┌──────────────┐     ┌─────────────────────────────────┐  │
│   │  specs/     │     │ docker-      │     │   mcp-servers/weaviate/           │  │
│   │  SRS, FR    │     │ compose.yml  │────▶│   Weaviate MCP server             │  │
│   └─────────────┘     │ (weaviate,   │     └─────────────────────────────────┘  │
│                      │  postgres,   │                                            │
│                      │  redis,      │     ┌─────────────────────────────────┐  │
│                      │  chimera-api,│     │   models/agent_persona.py        │  │
│                      │  grafana)    │     │   tests/                         │  │
│                      └──────────────┘     └─────────────────────────────────┘  │
│                                                                                   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Directory tree and purpose

| Path | Purpose |
|------|--------|
| **`.cursor/`** | Cursor IDE config: `mcp.json` (MCP servers), `rules/` (project_chimera.mdc, mcp_triggers.mdc). |
| **`.env`** | **Local env (gitignored).** Contains real keys, including **NEWSDATA_API_KEY** for the News API. |
| **`.env.example`** | Template for env vars (no real keys). Documents `NEWSDATA_API_KEY` placeholder. |
| **`app/`** | FastAPI app: `main.py`, `config.py`, `database.py`, `health.py`. **`app/models/`** (Agent, Campaign, Task, Content, Transaction, ai_models, agent_persona). **`app/services/`** (Planner, Worker, Judge, CFO). **`app/utils/`** (logging, security, validation). **`app/routers/`** (trends, agents, content, commerce). |
| **`skills/`** | Agent skills: **`skill_fetch_trends`** (uses NewsData.io via `NEWSDATA_API_KEY`), `skill_generate_content`, `skill_execute_transaction` — each with `requirements.txt` where needed. |
| **`mcp-servers/weaviate/`** | Weaviate MCP server (Dockerfile, server.py, pyproject.toml). |
| **`models/`** | Top-level domain models (e.g. `agent_persona.py`); primary models live in **`app/models/`**. |
| **`specs/`** | Specs: `_meta.md`, `functional.md`, `technical.md`, `openclaw_integration.md`. |
| **`tests/`** | **`tests/unit/`**, **`tests/integration/`**, **`tests/e2e/`** (test_models, test_api_integration, test_agent_workflow, etc.). |
| **`research/`** | `tooling_strategy.md`, `architecture_strategy.md`, `market_analysis.md`. |
| **`scripts/`** | `setup.sh`, `setup_real.sh`, `run.bat`, `run.ps1`, `setup_api_keys.sh`, `onboard_ai_agent.sh`. |
| **`database/`** | `init.sql` (Postgres init; referenced by docker-compose). |
| **`monitoring/`** | `dashboard.py`, `alerts.yaml`, `grafana/chimera-dashboard.json`. |
| **`k8s/`** | `deployment.yaml`, `service.yaml`, `ingress.yaml`, `hpa.yaml`, `secrets.yaml`. |
| **`docker-compose.yml`** | Runs Weaviate, Postgres, Redis, MCP Weaviate, chimera-api (passes `NEWSDATA_API_KEY`), Grafana. |
| **`docker-compose.prod.yml`** | Production compose (see `.env.production.example`). |
| **`deploy.sh`** | Deployment script. |
| **`pyproject.toml` / `uv.lock`** | Python project and lockfile. |
| **`.gitignore`**, **`README.md`**, **`CHANGELOG.md`**, **`LICENSE`** | Root project files. |

---

## 3. News API integration (where it’s used)

- **Config:** Set your News API key in **`.env`** (gitignored) as `NEWSDATA_API_KEY=pub_YOUR_KEY`. Never commit real keys. Get a key at https://newsdata.io/
- **Code:** **`skills/skill_fetch_trends/__init__.py`** reads `NEWSDATA_API_KEY` (or `NEWS_API_KEY`) from the environment and calls NewsData.io for trend fetching.
- **Docker:** **`docker-compose.yml`** passes `NEWSDATA_API_KEY` into the `chimera-api` service so the same key works in containers.
- **Template:** **`.env.example`** has a placeholder only; copy to `.env` and add your key locally.

---

## 4. Quick reference — important files

| File | Role |
|------|------|
| `app/main.py` | FastAPI entrypoint; lifespan, routers, health. |
| `app/health.py` | Defines `/health`, `/health/liveness`, `/health/readiness`. |
| `app/models/` | SQLAlchemy models (Agent, Campaign, Task, Content, Transaction) and `ai_models`, `agent_persona`. |
| `app/services/` | PlannerService, WorkerService, JudgeService, CFOService (Planner–Worker–Judge). |
| `skills/skill_fetch_trends/__init__.py` | Fetches trends using NewsData.io; uses `NEWSDATA_API_KEY`. |
| `.env` | Your local env with real API keys (including News). |
| `docker-compose.yml` | Full stack: DBs, MCP Weaviate, chimera-api (with News key), Grafana. |
| `specs/_meta.md` | Vision, constraints, success metrics, OpenClaw phases. |

---

You can use this diagram and table to navigate the repo and see how the News API key flows from `.env` → skills and Docker.
