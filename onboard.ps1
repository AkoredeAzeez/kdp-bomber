# Genie onboarding - one-click setup. Run once per machine to auto-install everything Genie needs.
#   Right-click Onboard_Genie.cmd -> Run,  OR  in PowerShell:  .\onboard.ps1
# Works from either layout: installed to ~/Genie (per-customer install) or the portable package.
$ErrorActionPreference = 'Continue'
function Line($m,$c='Cyan'){ Write-Host $m -ForegroundColor $c }
function RefreshPath { $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User") }

Line "==================================================================" 'Cyan'
Line " GENIE ONBOARDING - installing every dependency automatically" 'Cyan'
Line "==================================================================" 'Cyan'

# Locate the installed Genie project (the folder that holds .agents\skills\...).
$rel = ".agents\skills\uapf-codex-failover\genie_failover.py"
$proj = $null
foreach ($c in @(
        $PSScriptRoot,
        (Join-Path $PSScriptRoot '..'),
        (Join-Path $PSScriptRoot '..\1_claude-code-project'),
        (Join-Path $env:USERPROFILE 'Genie'))) {
    if ($c -and (Test-Path (Join-Path $c $rel))) { $proj = (Resolve-Path $c).Path; break }
}
if ($proj) { Line "Genie project: $proj" 'Green' } else { Line "Genie project folder not auto-found (health check will be skipped)." 'DarkYellow' }

# 0) Python (install if missing)
$py = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $py) {
    Line "[0/5] Python not found - installing Python 3.12 ..." 'Yellow'
    winget install --id Python.Python.3.12 --silent --accept-source-agreements --accept-package-agreements
    RefreshPath
} else { Line "[0/5] Python found: $($py.Source)" 'Green' }

# 1) Python packages (DOCX build, image fallback, render-QA gate)
Line "[1/5] Installing Python packages ..." 'Cyan'
python -m pip install --upgrade pip 2>&1 | Out-Null
python -m pip install python-docx docxcompose gradio_client pymupdf numpy comtypes pillow requests
Line "      python-docx, docxcompose, gradio_client, pymupdf, numpy, comtypes, pillow, requests" 'Green'

# 2) Codex CLI (failover agent) + Claude Code CLI (primary)
Line "[2/5] Installing Codex CLI and Claude Code CLI (winget) ..." 'Cyan'
winget install --id OpenAI.Codex --silent --accept-source-agreements --accept-package-agreements
winget install --id Anthropic.ClaudeCode --silent --accept-source-agreements --accept-package-agreements
RefreshPath

# 3) Flow image pipeline -> %LOCALAPPDATA%\FlowPipeline
Line "[3/5] Flow image pipeline ..." 'Cyan'
$fp  = Join-Path $PSScriptRoot "FlowPipeline"
$dst = Join-Path $env:LOCALAPPDATA "FlowPipeline"
if (Test-Path $fp) {
    New-Item -ItemType Directory -Force -Path $dst | Out-Null
    Copy-Item "$fp\*" $dst -Recurse -Force
    Line "      FlowPipeline -> $dst" 'Green'
} elseif (Test-Path $dst) {
    Line "      FlowPipeline already installed at $dst" 'Green'
} else {
    Line "      (FlowPipeline not bundled here - the installer places it at $dst)" 'DarkYellow'
}

# 4) Best-effort health check of the failover controller
Line "[4/5] Verifying the failover controller ..." 'Cyan'
if ($proj) {
    $gf = Join-Path $proj $rel
    try { python "$gf" health --project "$proj" } catch { Line "      (health check skipped)" 'DarkYellow' }
}

# 5) Interactive sign-ins (cannot be automated - the user must do these once)
Line "[5/5] Two one-time sign-ins remain (interactive):" 'Yellow'
Line "      1) codex login --device-auth      (sign in with your ChatGPT account)" 'Yellow'
Line "      2) claude                          (run once in your Genie project folder;" 'Yellow'
Line "                                          approve the 'codex' MCP server, then /exit)" 'Yellow'
Line "      Also sign into Google Flow (labs.google) and KDP in your browser." 'Yellow'
Line "      Details: Codex_Failover_Setup.md (in your Genie folder)." 'Yellow'
Line ""
Line "Onboarding install steps complete. Do the two sign-ins above and you're ready." 'Green'
