#!/bin/bash
# Activate virtual environment if exists
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

# Export PYTHONPATH to include project root
export PYTHONPATH=$(pwd)

# Run pytest with all tests
pytest --maxfail=1 --disable-warnings -q
