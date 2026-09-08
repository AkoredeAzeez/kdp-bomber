Set-Location $PSScriptRoot
Clear-Host
Write-Host ""
Write-Host "  =============================================="
Write-Host "   GENIE  --  AI Book Production Studio"
Write-Host "  =============================================="
Write-Host ""
Write-Host "  Getting your book dashboard ready..."
Write-Host ""
python genie_progress.py --brief 2>$null
Write-Host ""
Write-Host "  ----------------------------------------------"
Write-Host "  Ready! Here is what you can say to Genie:"
Write-Host ""
Write-Host "    'Write a book about [your topic]'   -- start a new book"
Write-Host "    'Genie, standup'                    -- full status update"
Write-Host "    'Resume [book title]'               -- continue a book"
Write-Host "    'Genie, help'                       -- see everything Genie can do"
Write-Host "  ----------------------------------------------"
Write-Host ""
claude
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "  Could not start Genie automatically."
    Write-Host "  Please open Claude Code and navigate to this folder:"
    Write-Host "  $PSScriptRoot"
    Write-Host ""
    Read-Host "  Press Enter to close"
}
