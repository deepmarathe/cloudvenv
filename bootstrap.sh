#!/bin/bash

echo "🚀 Bootstrapping CloudVenv..."

# Install gdown if not present
pip install --quiet gdown

# Download the prebuilt virtual environment from Google Drive
gdown https://drive.google.com/uc?id=1yzvH01OiODoGzswDydwZ8UxlfbaQtIF0

# Download the latest CLI tool from your GitHub repo
curl -sLO https://raw.githubusercontent.com/deepmarathe/cloudvenv/main/cloudvenv_cli.py

# Create the directory if not exists and extract
mkdir -p ~/.cloudvenv/top-packages-env
tar -xzf top-packages-env.tar.gz -C ~/.cloudvenv/

# Run the CLI installer for consistency (optional)
python3 cloudvenv_cli.py install top-packages-env

# Clean up
rm cloudvenv_cli.py top-packages-env.tar.gz

echo "✅ Done! Now run:"
echo "   source ~/.cloudvenv/top-packages-env/bin/activate"
