# Selnecker Paedagogia Christiana 1577 — Pars I Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds the shareable-named PDF (and DOCX) for Paedagogia Pars I (Decalogue).
# When Pars II is ready, copy this file to `build-shareable-pars-ii.ps1` and
# adjust the mdFile / shareableStem.
#
# Dependencies:
#   - Pandoc          : $env:LOCALAPPDATA\Pandoc\pandoc.exe (or on PATH)
#   - LibreOffice     : "C:\Program Files\LibreOffice\program\soffice.exe"
#   - Reference DOCX  : shared/reference-custom.docx (shared across volumes)

$ErrorActionPreference = 'Stop'

# --- Locate repo root ---------------------------------------------------------
$repoRoot = & git rev-parse --show-toplevel 2>$null
if (-not $repoRoot) {
    $repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
}
$repoRoot = $repoRoot.Trim() -replace '/', '\'

# --- Tool locations -----------------------------------------------------------
$pandoc = if (Get-Command pandoc -ErrorAction SilentlyContinue) {
    (Get-Command pandoc).Source
} else {
    "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
}
$lo = 'C:\Program Files\LibreOffice\program\soffice.exe'

if (-not (Test-Path $pandoc)) {
    Write-Error "Pandoc not found at $pandoc"; exit 1
}
if (-not (Test-Path $lo)) {
    Write-Error "LibreOffice not found at $lo"; exit 1
}

# --- Volume paths -------------------------------------------------------------
$volumeDir  = Join-Path $repoRoot 'dogmatics\selnecker-paedagogia-christiana-1565'
$reviewDir  = Join-Path $volumeDir 'review'
$mdFile     = 'paedagogia-pars-i-1577.md'
$refDoc     = Join-Path $repoRoot 'shared\reference-custom.docx'

if (-not (Test-Path $refDoc)) {
    Write-Error "Reference doc not found: $refDoc"; exit 1
}

$shareableStem = 'Nikolaus-Selnecker-Christian-Paedagogy-Pars-I-Exposition-of-the-Decalogue-1577-English-Scholastic-Lutherans'

Set-Location $reviewDir

# --- Clean prior artefacts ----------------------------------------------------
Remove-Item "$shareableStem.docx", "$shareableStem.pdf",
            'paedagogia-pars-i-1577.docx', 'paedagogia-pars-i-1577.pdf' `
            -ErrorAction SilentlyContinue

# --- Step 1: pandoc -> DOCX ----------------------------------------------------
Write-Host 'Building shareable Selnecker Paedagogia Pars I 1577...' -ForegroundColor Cyan
Write-Host "  pandoc: $mdFile -> $shareableStem.docx"

& $pandoc $mdFile -o "$shareableStem.docx" `
    --standalone `
    --from='markdown+smart+raw_tex+fenced_divs+raw_attribute' `
    --reference-doc=$refDoc 2>&1 | Out-Null

if (-not (Test-Path "$shareableStem.docx")) {
    Write-Error 'DOCX build failed'; exit 1
}

# --- Step 2: convert DOCX to PDF ----------------------------------------------
Write-Host "  LibreOffice: $shareableStem.docx -> $shareableStem.pdf"
$profileDir = Join-Path $env:TEMP "lo-profile-$(Get-Random)"
$profileUrl = 'file:///' + ($profileDir -replace '\\', '/')
Start-Process -FilePath $lo -ArgumentList @(
    '--headless', '--norestore',
    "-env:UserInstallation=$profileUrl",
    '--convert-to', 'pdf', '--outdir', '.',
    "$shareableStem.docx"
) -Wait -NoNewWindow | Out-Null

if (Test-Path $profileDir) {
    Remove-Item $profileDir -Recurse -Force -ErrorAction SilentlyContinue
}

Get-ChildItem "$shareableStem.*" | Select-Object Name, Length | Format-Table -AutoSize
