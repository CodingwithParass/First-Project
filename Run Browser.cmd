@echo off
title Code with Paras Browser Launcher
color 0A

echo ===================================================
echo       Starting Code with Paras Browser
echo       Channel: @CodewithParas
echo ===================================================
echo.

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
color 0C
echo [ERROR] Python is not installed or not added to PATH!
echo Please install Python from https://www.python.org/
echo Make sure to check the box: "Add Python to PATH"
echo.
pause
exit /b
)

:: 2. Check and install pywebview if missing
echo [] Checking required libraries...
python -c "import webview" >nul 2>&1
if %errorlevel% neq 0 (
echo [] pywebview not found. Installing now...
pip install pywebview
if %errorlevel% neq 0 (
color 0C
echo [ERROR] Failed to install pywebview. Check your internet connection.
pause
exit /b
)
)

:: 3. Launch the Python browser script
echo.
echo [*] Launching Code with Paras Browser...
echo.
python main.py

:: 4. Exit gracefully after closing the browser
if %errorlevel% neq 0 (
color 0C
echo.
echo [!] Browser closed with an issue.
pause
)
exit
