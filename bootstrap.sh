#!/bin/bash

echo "🚀 Bootstrapping CloudVenv..."

curl -sLO https://raw.githubusercontent.com/<your-username>/cloudvenv/main/cloudvenv_cli.py
python3 cloudvenv_cli.py install top-packages-env
rm cloudvenv_cli.py
echo "✅ Done! Now run:"
echo "   source ~/.cloudvenv/top-packages-env/bin/activate"
