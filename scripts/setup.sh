#!/bin/bash
set -euo pipefail
echo "Setting up Disaster Recovery Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
