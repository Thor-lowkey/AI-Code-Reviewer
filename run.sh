#!/bin/bash

# Navigate to the script's root directory location
cd "$(dirname "$0")"

# Get the absolute path of the root directory
PROJECT_ROOT=$(pwd)

# Explicit path to the venv Python interpreter
VENV_PYTHON="$PROJECT_ROOT/venv/bin/python"

# Verify the virtual environment python interpreter exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ Error: Virtual environment python execution layer not found."
    exit 1
fi

echo "⚡ Executing architecture suite using native venv Python context..."

# 1. Start the FastAPI backend using 'python -m uvicorn'
echo "🚀 Launching FastAPI Backend Server..."
cd "$PROJECT_ROOT/backend"
"$VENV_PYTHON" -m uvicorn main:app --reload --port 8000 &
BACKEND_PID=$!

# 2. Give the backend a brief moment to initialize and bind ports
sleep 2

# 3. Start the Streamlit Frontend using 'python -m streamlit'
echo "🖥️ Launching Streamlit Frontend Architecture..."
cd "$PROJECT_ROOT/frontend"
"$VENV_PYTHON" -m streamlit run app.py

# 4. Cleanup process: Gracefully terminate background systems on exit (Ctrl+C)
echo "🧹 Shutting down background architecture systems..."
kill $BACKEND_PID 2>/dev/null