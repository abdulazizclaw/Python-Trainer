@echo off
REM Python Trainer - Installation Script for Windows

echo ========================================
echo Python Trainer - Installation
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed.
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo + %PYTHON_VERSION% found

echo.
echo Cloning Python Trainer repository...
if not exist "Python-Trainer" (
    git clone https://github.com/abdulazizclaw/Python-Trainer.git
)
cd Python-Trainer

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo + Installation complete!
echo ========================================
echo.
echo To start the tutorial, run:
echo   python run_tutorial.py
echo.
pause
