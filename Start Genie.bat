@echo off
title Genie - AI Book Production Studio
cd /d "%~dp0"
cls
echo.
echo  ==============================================
echo   GENIE  --  AI Book Production Studio
echo  ==============================================
echo.
echo  Getting your book dashboard ready...
echo.
python genie_progress.py --brief 2>nul
echo.
echo  ----------------------------------------------
echo  Ready! Here is what you can say to Genie:
echo.
echo    "Write a book about [your topic]"   -- start a new book
echo    "Genie, standup"                    -- full status update
echo    "Resume [book title]"               -- continue a book
echo    "Genie, help"                       -- see everything Genie can do
echo  ----------------------------------------------
echo.
claude
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  Could not start Genie automatically.
    echo  Please open Claude Code and navigate to this folder:
    echo  %CD%
    echo.
    pause
)
