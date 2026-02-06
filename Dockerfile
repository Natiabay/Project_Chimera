# Multi-stage Docker build for production
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc g++ libpq-dev curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv

COPY . .

RUN uv venv /app/venv && . /app/venv/bin/activate && uv pip install --system --no-cache-dir -e . || pip install --no-cache-dir -e .

# Stage 2: Runtime
FROM python:3.11-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y curl postgresql-client redis-tools && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/venv /app/venv
COPY . .

ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONPATH="/app:$PYTHONPATH"
ENV PYTHONUNBUFFERED=1

RUN useradd -m -u 1000 chimera && chown -R chimera:chimera /app
USER chimera

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
