#!/bin/bash

# Project Chimera: AI Agent Onboarding Script
# This script sets up the environment for an AI agent to start contributing.

echo "🚀 Onboarding AI Agent to Project Chimera"

# Step 1: Clone the repository (if not already)
if [ ! -d "PROJECT_CHIMERA" ]; then
    echo "Please clone the repository first: git clone <your-repo-url>"
    exit 1
else
    cd PROJECT_CHIMERA
    git pull origin main
fi

# Step 2: Set up environment
echo "Setting up Python environment..."
make setup

# Step 3: Run tests to see what's failing
echo "Running tests to identify gaps..."
make test

# Step 4: Run spec-check to understand requirements
make spec-check

# Step 5: Display available skills
echo "Available skills to implement:"
ls skills/

echo ""
echo "📋 Onboarding complete!"
echo "The AI agent can now start working on failing tests."
echo "Refer to:"
echo "1. specs/ - for requirements"
echo "2. tests/ - for what needs to be built"
echo "3. .cursor/rules - for coding standards"
