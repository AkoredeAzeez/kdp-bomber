@echo off
REM One-click Genie onboarding. Double-click this file, or run from a terminal.
REM It auto-installs Python packages, the Codex CLI, the Claude Code CLI, and the Flow image pipeline.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0onboard.ps1"
echo.
pause
