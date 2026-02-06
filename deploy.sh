#!/bin/bash
echo "🚀 REAL Project Chimera Deployment"
echo "==================================="

# 1. Check Docker and Docker Compose
docker --version || { echo "❌ Docker required"; exit 1; }
docker-compose --version || { echo "❌ Docker Compose required"; exit 1; }

# 2. Load environment
if [ ! -f .env.production ]; then
    echo "❌ Create .env.production first"
    echo "💡 Copy .env.example to .env.production and fill REAL values"
    exit 1
fi

# 3. Start services
echo "🔄 Starting services..."
docker-compose --env-file .env.production up -d

# 4. Wait for services
echo "⏳ Waiting for services to be ready..."
sleep 10

# 5. Check health
echo "🏥 Checking service health..."
docker-compose ps

# 6. Show endpoints
echo ""
echo "✅ Deployment complete!"
echo ""
echo "🌐 Endpoints:"
echo "   - Weaviate: http://localhost:8080"
echo "   - PostgreSQL: localhost:5432"
echo "   - Redis: localhost:6379"
echo "   - MCP Weaviate: http://localhost:3001"
echo "   - Chimera API: http://localhost:8000"
echo "   - Grafana: http://localhost:3000 (admin/admin)"
echo ""
echo "📋 To view logs: docker-compose logs -f"
echo "🛑 To stop: docker-compose down"
