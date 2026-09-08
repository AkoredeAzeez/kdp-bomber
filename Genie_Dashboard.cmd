@echo off
REM Refresh and open the Genie book-production dashboard.
cd /d "%~dp0"
python genie_dashboard.py
start "" "%~dp0Genie_Dashboard.html"
