# Project Chimera: Automation Makefile
.PHONY: setup test docker-test docker-build docker-run spec-check clean help

# Configuration
VENV_PATH := .venv
PYTHON := python
UV := uv
DOCKER_IMAGE := project-chimera
DOCKER_TAG := latest

# Colors for output
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m # No Color

# --- Development Commands ---
setup:
	@echo "$(GREEN)Setting up Project Chimera environment...$(NC)"
	@$(UV) --python 3.11 venv $(VENV_PATH)
	@. $(VENV_PATH)/bin/activate && $(UV) pip install -e .
	@echo "$(GREEN)✅ Environment setup complete$(NC)"

test:
	@echo "$(GREEN)Running Project Chimera tests...$(NC)"
	@. $(VENV_PATH)/bin/activate && $(PYTHON) -m pytest tests/ -v
	@echo "$(GREEN)✅ Tests completed$(NC)"

# --- Docker Commands ---
docker-build:
	@echo "$(GREEN)Building Docker image: $(DOCKER_IMAGE):$(DOCKER_TAG)$(NC)"
	@docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .
	@echo "$(GREEN)✅ Docker image built$(NC)"

docker-test: docker-build
	@echo "$(GREEN)Running tests in Docker container...$(NC)"
	@docker run --rm $(DOCKER_IMAGE):$(DOCKER_TAG)
	@echo "$(GREEN)✅ Docker tests completed$(NC)"

docker-run:
	@echo "$(GREEN)Running Project Chimera in Docker...$(NC)"
	@docker run -d \
		-p 3000:3000 \
		--name chimera \
		--env-file .env \
		$(DOCKER_IMAGE):$(DOCKER_TAG)
	@echo "$(GREEN)✅ Container running on http://localhost:3000$(NC)"

# --- Specification Validation ---
spec-check:
	@echo "$(GREEN)Checking specification alignment...$(NC)"
	@echo "1. Checking for SRS Functional Requirement references..."
	@grep -r "FR [0-9]\+\.[0-9]\+" specs/ tests/ skills/ || true
	@echo "\n2. Checking for required directories..."
	@[ -d "specs" ] && echo "✅ specs/ directory exists" || echo "❌ Missing specs/"
	@[ -d "tests" ] && echo "✅ tests/ directory exists" || echo "❌ Missing tests/"
	@[ -d "skills" ] && echo "✅ skills/ directory exists" || echo "❌ Missing skills/"
	@[ -d "models" ] && echo "✅ models/ directory exists" || echo "❌ Missing models/"
	@echo "\n3. Checking for critical files..."
	@[ -f "specs/_meta.md" ] && echo "✅ specs/_meta.md exists" || echo "❌ Missing specs/_meta.md"
	@[ -f "specs/functional.md" ] && echo "✅ specs/functional.md exists" || echo "❌ Missing specs/functional.md"
	@[ -f "specs/technical.md" ] && echo "✅ specs/technical.md exists" || echo "❌ Missing specs/technical.md"
	@[ -f "Dockerfile" ] && echo "✅ Dockerfile exists" || echo "❌ Missing Dockerfile"
	@[ -f "Makefile" ] && echo "✅ Makefile exists" || echo "❌ Missing Makefile"
	@echo "\n$(GREEN)✅ Specification check completed$(NC)"

# --- Utility Commands ---
clean:
	@echo "$(GREEN)Cleaning up...$(NC)"
	@docker system prune -f || true
	@rm -rf __pycache__ .pytest_cache .coverage htmlcov dist build || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN)✅ Cleanup completed$(NC)"

help:
	@echo "$(GREEN)Project Chimera Automation Commands:$(NC)"
	@echo "  make setup         - Setup virtual environment and install dependencies"
	@echo "  make test          - Run tests locally"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-test   - Build and run tests in Docker"
	@echo "  make docker-run    - Run application in Docker container"
	@echo "  make spec-check    - Validate specification alignment"
	@echo "  make clean         - Clean temporary files and Docker artifacts"
	@echo "  make help          - Show this help message"
