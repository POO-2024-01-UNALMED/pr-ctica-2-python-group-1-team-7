@echo off
cd /d "%~dp0"

pip install Pillow

python src//uiMain//main.py

pause