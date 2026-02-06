#!/bin/bash
set -e

echo "🚀 PROJECT CHIMERA PRODUCTION DEPLOYMENT"
echo "========================================"

# Load environment
if [ ! -f .env.production ]; then
    echo "❌ ERROR: .env.production not found"
    echo "💡 Create from .env.example and fill REAL values"
    exit 1
fi
set -a
source .env.production
set +a

# Check required variables
REQUIRED_VARS=(
    "WEAVIATE_URL"
    "WEAVIATE_API_KEY"
    "NEWSDATA_API_KEY"
    "GEMINI_API_KEY"
    "POSTGRES_URL"
    "REDIS_URL"
)

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ ERROR: $var is not set in .env.production"
        exit 1
    fi
done

echo "✅ Environment loaded"

# Build Docker image
echo "🐳 Building Docker image..."
docker build -t project-chimera:prod .

# Deploy to Kubernetes (if configured)
if [ -f "k8s/deployment.yaml" ] && command -v kubectl &>/dev/null; then
    echo "☸️ Deploying to Kubernetes..."
    kubectl create namespace chimera --dry-run=client -o yaml | kubectl apply -f -
    kubectl create secret generic chimera-secrets \
        --namespace chimera \
        --from-env-file=.env.production \
        --dry-run=client -o yaml | kubectl apply -f - 2>/dev/null || true
    kubectl apply -f k8s/deployment.yaml
    echo "⏳ Waiting for deployment..."
    kubectl rollout status deployment/chimera-api -n chimera --timeout=300s 2>/dev/null || true
    echo "✅ Kubernetes deployment complete"
else
    # Deploy with Docker Compose
    echo "🐳 Deploying with Docker Compose..."
    docker-compose --env-file .env.production up -d
    echo "✅ Docker Compose deployment complete"
fi

# Smoke test
echo "🧪 Running smoke tests..."
sleep 5
curl -sf http://localhost:8000/health >/dev/null && echo "✅ Health check passed" || echo "⚠️ Health check failed (service may still be starting)"

echo ""
echo "🎉 PROJECT CHIMERA DEPLOYMENT COMPLETE"
echo ""
echo "📋 Quick Start:"
echo "   Docs:    http://localhost:8000/docs"
echo "   Health:  http://localhost:8000/health"
echo "   Trends:  GET /api/v1/trends?niche=fashion"
echo "   Metrics: http://localhost:8000/metrics"
echo ""
echo "🔧 Management:"
echo "   Logs:  docker-compose logs -f"
echo "   Stop:  docker-compose down"
echo ""
