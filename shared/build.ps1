# Scholastic Lutherans — Universal build script
# ═══════════════════════════════════════════════════════════════════════════
# Builds one work's DOCX and PDF from its master Markdown.
#
# Usage:
#   .\shared\build.ps1 -Category catechetical -Work chytraeus-catechismus-1594
#
# Produces:
#   <category>/<work>/review/<work>.docx
#   <category>/<work>/review/<work>.pdf
#
# Assumes: Pandoc installed at $env:LOCALAPPDATA\Pandoc\pandoc.exe
#          LibreOffice installed at C:\Program Files\LibreOffice\program\soffice.exe
#          Master file at <category>/<work>/review/<work>.md
#          Reference DOCX at shared/reference-custom.docx
#
# Build cadence discipline: MAX 2 builds per volume (mid-checkpoint + final).
# Between builds, commit the Markdown edits normally.

param(
    [Parameter(Mandatory=$true)][string]$Category,
    [Parameter(Mandatory=$true)][string]$Work
)

$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
$lo = "C:\Program Files\LibreOffice\program\soffice.exe"
$repoRoot = "$HOME\Documents\Github\scholastic-lutherans"
$reviewDir = Join-Path $repoRoot "$Category\$Work\review"
$mdFile = "$Work.md"
$docxFile = "$Work.docx"
$pdfFile = "$Work.pdf"
$refDoc = Join-Path $repoRoot "shared\reference-custom.docx"

if (-not (Test-Path (Join-Path $reviewDir $mdFile))) {
    Write-Error "Master file not found: $(Join-Path $reviewDir $mdFile)"
    exit 1
}

Set-Location $reviewDir
Remove-Item $docxFile, $pdfFile -ErrorAction SilentlyContinue

Write-Host "Building $Category/$Work ..." -ForegroundColor Cyan
Write-Host "  pandoc: $mdFile -> $docxFile"

& $pandoc $mdFile -o $docxFile --standalone `
    --from="markdown+smart+raw_tex+fenced_divs+raw_attribute" `
    --reference-doc=$refDoc 2>&1 | Out-Null

if (-not (Test-Path $docxFile)) {
    Write-Error "DOCX build failed"
    exit 1
}

Write-Host "  LibreOffice: $docxFile -> $pdfFile"
$profileDir = "$env:TEMP\lo-profile-$(Get-Random)"
$profileUrl = "file:///" + ($profileDir -replace '\\','/')
Start-Process -FilePath $lo -ArgumentList @(
    "--headless", "-env:UserInstallation=$profileUrl",
    "--convert-to", "pdf", "--outdir", ".",
    $docxFile
) -Wait -NoNewWindow | Out-Null

Get-ChildItem "$Work.*" | Select-Object Name, Length | Format-Table -AutoSize
