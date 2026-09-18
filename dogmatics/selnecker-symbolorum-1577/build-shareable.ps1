# Selnecker Symbolorum 1577 — Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds ONLY the shareable-named PDF (and DOCX).
# Uses a Symbolorum-specific reference DOCX that has running headers (chapter
# name at top of each page via STYLEREF field) and centered page-numbers in
# the footer. Runs a LibreOffice Basic macro to refresh the Table of Contents
# and cross-reference fields before the final PDF export.
#
# Dependencies:
#   - Pandoc          : $env:LOCALAPPDATA\Pandoc\pandoc.exe (or on PATH)
#   - LibreOffice     : "C:\Program Files\LibreOffice\program\soffice.exe"
#   - Reference DOCX  : reference-selnecker-symbolorum.docx (this volume)
#
# Repo root is auto-detected via `git rev-parse` so this script is portable.

$ErrorActionPreference = 'Stop'

# --- Locate repo root without hard-coded paths --------------------------------
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
    Write-Error "Pandoc not found at $pandoc. Install from https://pandoc.org/installing.html"
    exit 1
}
if (-not (Test-Path $lo)) {
    Write-Error "LibreOffice not found at $lo. Install from https://www.libreoffice.org/"
    exit 1
}

# --- Volume paths -------------------------------------------------------------
$volumeDir  = Join-Path $repoRoot 'dogmatics\selnecker-symbolorum-1577'
$reviewDir  = Join-Path $volumeDir 'review'
$mdFile     = 'selnecker-symbolorum-1577.md'
$refDoc     = Join-Path $volumeDir 'reference-selnecker-symbolorum.docx'

if (-not (Test-Path $refDoc)) {
    Write-Error "Reference doc not found: $refDoc"
    exit 1
}

$shareableStem = 'Nikolaus-Selnecker-Exposition-of-the-Apostles-Nicene-and-Athanasian-Creeds-1577-English-Scholastic-Lutherans'

Set-Location $reviewDir

# --- Clean prior artefacts ----------------------------------------------------
Remove-Item "$shareableStem.docx", "$shareableStem.pdf",
            'selnecker-symbolorum-1577.docx', 'selnecker-symbolorum-1577.pdf' `
            -ErrorAction SilentlyContinue

# --- Step 1: pandoc -> DOCX ----------------------------------------------------
Write-Host 'Building shareable Selnecker Symbolorum 1577...' -ForegroundColor Cyan
Write-Host "  pandoc: $mdFile -> $shareableStem.docx"

& $pandoc $mdFile -o "$shareableStem.docx" `
    --standalone `
    --from='markdown+smart+raw_tex+fenced_divs+raw_attribute' `
    --reference-doc=$refDoc 2>&1 | Out-Null

if (-not (Test-Path "$shareableStem.docx")) {
    Write-Error 'DOCX build failed'
    exit 1
}

# --- Step 2: update TOC + STYLEREF + PAGE fields via LibreOffice's Python-UNO
Write-Host '  LibreOffice UNO: refreshing TOC and cross-reference fields'
$profileDir = Join-Path $env:TEMP "lo-profile-$(Get-Random)"
$loPython   = 'C:\Program Files\LibreOffice\program\python.exe'
$updateScript = Join-Path $volumeDir 'update-fields.py'
$absDocx    = (Resolve-Path "$shareableStem.docx").Path

if ((Test-Path $loPython) -and (Test-Path $updateScript)) {
    & $loPython $updateScript $absDocx $profileDir 2>&1 | ForEach-Object { Write-Host "    $_" }
} else {
    Write-Host '    (skipped: LibreOffice Python or update-fields.py not found)' -ForegroundColor Yellow
}

# --- Step 3: convert the updated DOCX to PDF ----------------------------------
Write-Host "  LibreOffice: $shareableStem.docx -> $shareableStem.pdf"
$profileUrl = 'file:///' + ($profileDir -replace '\\', '/')
Start-Process -FilePath $lo -ArgumentList @(
    '--headless', '--norestore',
    "-env:UserInstallation=$profileUrl",
    '--convert-to', 'pdf', '--outdir', '.',
    "$shareableStem.docx"
) -Wait -NoNewWindow | Out-Null

# --- Cleanup ------------------------------------------------------------------
if (Test-Path $profileDir) {
    Remove-Item $profileDir -Recurse -Force -ErrorAction SilentlyContinue
}

Get-ChildItem "$shareableStem.*" | Select-Object Name, Length | Format-Table -AutoSize
