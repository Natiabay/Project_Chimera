# Changelog

All notable changes to Project Chimera are documented here.

## [1.0.0] — 2025-02-06

### Added

- **App structure**: Reorganized `app/` with `models/` (Agent, Campaign, Task, Content, Transaction, ai_models, agent_persona), `services/` (Planner, Worker, Judge, CFO), `utils/` (logging, security, validation).
- **Skills**: `skill_fetch_trends`, `skill_generate_content`, `skill_execute_transaction` with `requirements.txt` where needed.
- **Tests**: Structured into `tests/unit/`, `tests/integration/`, `tests/e2e/` with test_models, test_api_integration, test_agent_workflow.
- **Research**: `architecture_strategy.md`, `market_analysis.md`, `tooling_strategy.md`.
- **Monitoring**: `alerts.yaml`, `grafana/chimera-dashboard.json`.
- **Kubernetes**: `service.yaml`, `ingress.yaml`, `hpa.yaml`, `secrets.yaml`; deployment split from Service/HPA.
- **CI/CD**: `tests.yml`, `deploy.yml` workflows.
- **Root files**: `.gitignore`, `docker-compose.prod.yml`, `.env.production.example`, `README.md`, `CHANGELOG.md`, `LICENSE`.
- **Scripts**: `setup.sh`, `setup_real.sh`, `run.bat`, `run.ps1` in `scripts/`.
- **Database**: `database/init.sql` (moved from root); docker-compose updated.

### Changed

- Imports updated to `app.models`, `app.models.ai_models`, `app.models.agent_persona`.
- `app/db_models.py` and `app/ai_models.py` kept as deprecated re-exports for compatibility.

### Fixed

- Pytest collects tests from `tests/unit`, `tests/integration`, `tests/e2e`.

---

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
