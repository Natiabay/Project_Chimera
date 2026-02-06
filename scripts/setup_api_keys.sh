#!/bin/bash

# Project Chimera: Quick API Keys Setup
echo "🚀 Setting up Project Chimera API Keys for 3-Day Challenge"

# Create .env from example if not exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✅ Created .env file"
else
    echo "⚠️  .env file already exists"
fi

echo ""
echo "📋 REQUIRED SETUP (10 minutes):"
echo ""
echo "1. WEAVIATE (Vector Database):"
echo "   - Go to: https://console.weaviate.cloud/"
echo "   - Click 'Create Sandbox' (FREE for 14 days)"
echo "   - Copy 'Cluster URL' and 'API Key' to .env"
echo ""
echo "2. GEMINI API (AI Model):"
echo "   - Go to: https://aistudio.google.com/app/apikey"
echo "   - Click 'Create API Key' (FREE: 60 req/min)"
echo "   - Copy key to GEMINI_API_KEY in .env"
echo ""
echo "3. LOCAL DATABASES:"
echo "   Run these commands:"
echo "   brew install postgresql redis  # or apt-get install"
echo "   brew services start postgresql"
echo "   brew services start redis"
echo "   createdb chimera"
echo ""
echo "4. COINBASE AGENTKIT (TESTNET):"
echo "   - Go to: https://portal.cdp.coinbase.com/"
echo "   - Sign up for Developer Preview"
echo "   - Use Base Sepolia testnet for development"
echo ""
echo "🎯 For the challenge, you can use TEST values in .env"
echo "   The system will work with mock data for demonstration."
echo ""
echo "✅ Setup complete! Edit .env with your actual keys."
