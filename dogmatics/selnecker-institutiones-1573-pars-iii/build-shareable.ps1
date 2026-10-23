# Selnecker Institutio Pars III 1579 — Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds the shareable-named PDF (and DOCX) for Pars III (catechetical).
#
# Dependencies:
#   - Pandoc          : $env:LOCALAPPDATA\Pandoc\pandoc.exe (or on PATH)
#   - LibreOffice     : "C:\Program Files\LibreOffice\program\soffice.exe"
#   - Reference DOCX  : shared/reference-custom.docx (shared across volumes)
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
$volumeDir  = Join-Path $repoRoot 'dogmatics\selnecker-institutiones-1573-pars-iii'
$reviewDir  = Join-Path $volumeDir 'review'
$mdFile     = 'selnecker-institutio-pars-iii-1579.md'
$refDoc     = Join-Path $repoRoot 'shared\reference-custom.docx'

if (-not (Test-Path $refDoc)) {
    Write-Error "Reference doc not found: $refDoc"
    exit 1
}

$shareableStem = 'Nikolaus-Selnecker-The-Institution-of-the-Christian-Religion-Pars-III-1579-English-Scholastic-Lutherans'

Set-Location $reviewDir

# --- Clean prior artefacts ----------------------------------------------------
Remove-Item "$shareableStem.docx", "$shareableStem.pdf",
            'selnecker-institutio-pars-iii-1579.docx', 'selnecker-institutio-pars-iii-1579.pdf' `
            -ErrorAction SilentlyContinue

# --- Step 1: pandoc -> DOCX ----------------------------------------------------
Write-Host 'Building shareable Selnecker Institutio Pars III 1579...' -ForegroundColor Cyan
Write-Host "  pandoc: $mdFile -> $shareableStem.docx"

& $pandoc $mdFile -o "$shareableStem.docx" `
    --standalone `
    --from='markdown+smart+raw_tex+fenced_divs+raw_attribute' `
    --reference-doc=$refDoc 2>&1 | Out-Null

if (-not (Test-Path "$shareableStem.docx")) {
    Write-Error 'DOCX build failed'
    exit 1
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

# --- Cleanup ------------------------------------------------------------------
if (Test-Path $profileDir) {
    Remove-Item $profileDir -Recurse -Force -ErrorAction SilentlyContinue
}

Get-ChildItem "$shareableStem.*" | Select-Object Name, Length | Format-Table -AutoSize
