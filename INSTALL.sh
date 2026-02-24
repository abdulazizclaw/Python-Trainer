#!/bin/bash
# Python Trainer - Installation Script
# For macOS and Linux

echo "========================================"
echo "Python Trainer - Installation"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "Please install Python 3 from https://www.python.org/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Clone the repository if not already in it
if [ ! -f "README.md" ] || [ ! -f "run_tutorial.py" ]; then
    echo "Cloning Python Trainer repository..."
    git clone https://github.com/abdulazizclaw/Python-Trainer.git
    cd Python-Trainer
fi

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "✅ Installation complete!"
echo "========================================"
echo ""
echo "To start the tutorial, run:"
echo "  python3 run_tutorial.py"
echo ""
