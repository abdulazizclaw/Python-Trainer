# Quick Start Guide

## For macOS/Linux

```bash
# Clone the repository
git clone https://github.com/abdulazizclaw/Python-Trainer.git
cd Python-Trainer

# Run the install script
bash INSTALL.sh

# Or manually:
pip3 install -r requirements.txt
python3 run_tutorial.py
```

## For Windows

```bash
# Clone the repository
git clone https://github.com/abdulazizclaw/Python-Trainer.git
cd Python-Trainer

# Run the install script
INSTALL.bat

# Or manually:
pip install -r requirements.txt
python run_tutorial.py
```

## Key Points

**Use `python3` and `pip3` on macOS/Linux** (not `python` or `pip`)

**Use `python` and `pip` on Windows**

## Troubleshooting

### Command not found: python3
- macOS: Install Python 3 from https://www.python.org/
- Linux: `sudo apt-get install python3 python3-pip`

### Permission denied on INSTALL.sh
```bash
chmod +x INSTALL.sh
bash INSTALL.sh
```

### pip: command not found
Use `pip3` on macOS/Linux instead of `pip`

## Start Learning

Once installed, run:
```bash
python3 run_tutorial.py  # macOS/Linux
python run_tutorial.py   # Windows
```

Then choose `1` to start Module 1: Fundamentals
