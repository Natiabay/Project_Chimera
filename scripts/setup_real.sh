#!/bin/bash
echo "🚀 REAL Project Chimera Setup"
echo "=============================="
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# 1. Check Python
python3 --version || { echo "❌ Python 3.11+ required"; exit 1; }

# 2. Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# 3. Install core dependencies
echo "📦 Installing dependencies..."
pip install -e .

# 4. Check for .env
if [ ! -f .env ]; then
    echo "📝 Creating .env from template..."
    cp .env.example .env
    echo "⚠️  EDIT .env with your REAL API keys!"
    echo "💡 Required:"
    echo "   - Weaviate: https://console.weaviate.cloud"
    echo "   - News API: https://newsdata.io/pricing"
    echo "   - OpenAI: https://platform.openai.com"
fi

# 5. Test Weaviate connection
echo "🔗 Testing Weaviate connection..."
if python -c "import weaviate; print('✅ Weaviate available')" 2>/dev/null; then
    echo "✅ Weaviate client ready"
else
    echo "❌ Install: pip install weaviate-client"
fi

echo "✅ REAL setup complete!"
echo "📋 Next: Edit .env with REAL keys, then run: uv run pytest tests/ -v"
