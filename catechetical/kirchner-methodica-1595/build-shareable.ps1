# Kirchner Methodica 1595 — Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds ONLY the shareable-named PDF (and DOCX).
# Does not produce the working-name build artifact.

$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
$lo = "C:\Program Files\LibreOffice\program\soffice.exe"
$repoRoot = "$HOME\Documents\Github\scholastic-lutherans"
$reviewDir = Join-Path $repoRoot "catechetical\kirchner-methodica-1595\review"
$mdFile = "kirchner-methodica-1595.md"
$refDoc = Join-Path $repoRoot "shared\reference-custom.docx"

$shareableStem = "Timotheus-Kirchner-Methodica-Explicatio-1595-English-Scholastic-Lutherans"

Set-Location $reviewDir

# Remove any prior artifacts
Remove-Item "$shareableStem.docx", "$shareableStem.pdf", "kirchner-methodica-1595.docx", "kirchner-methodica-1595.pdf" -ErrorAction SilentlyContinue

Write-Host "Building shareable Kirchner Methodica 1595..." -ForegroundColor Cyan
Write-Host "  pandoc: $mdFile -> $shareableStem.docx"

& $pandoc $mdFile -o "$shareableStem.docx" --standalone `
    --from="markdown+smart+raw_tex+fenced_divs+raw_attribute" `
    --reference-doc=$refDoc 2>&1 | Out-Null

if (-not (Test-Path "$shareableStem.docx")) {
    Write-Error "DOCX build failed"
    exit 1
}

Write-Host "  LibreOffice: $shareableStem.docx -> $shareableStem.pdf"
$profileDir = "$env:TEMP\lo-profile-$(Get-Random)"
$profileUrl = "file:///" + ($profileDir -replace '\\','/')
Start-Process -FilePath $lo -ArgumentList @(
    "--headless", "-env:UserInstallation=$profileUrl",
    "--convert-to", "pdf", "--outdir", ".",
    "$shareableStem.docx"
) -Wait -NoNewWindow | Out-Null

Get-ChildItem "$shareableStem.*" | Select-Object Name, Length | Format-Table -AutoSize
