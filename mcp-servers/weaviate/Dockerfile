# MCP Weaviate server for Project Chimera (used by docker-compose)
FROM python:3.11-slim

WORKDIR /app

# Install from project root context (docker-compose builds from repo root)
# This Dockerfile is built with context mcp-servers/weaviate
COPY pyproject.toml ./
COPY server.py ./

RUN pip install --no-cache-dir weaviate-client>=4.0.0 mcp>=1.0.0

EXPOSE 3000

# Default: stdio (override in compose if using HTTP transport)
CMD ["python", "server.py"]
