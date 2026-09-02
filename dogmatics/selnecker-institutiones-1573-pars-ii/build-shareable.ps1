# Selnecker Pars II — Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds ONLY the shareable-named PDF (and DOCX).
# Does not produce the working-name build artifact.

$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
$lo = "C:\Program Files\LibreOffice\program\soffice.exe"
$repoRoot = "$HOME\Documents\Github\scholastic-lutherans"
$reviewDir = Join-Path $repoRoot "dogmatics\selnecker-institutiones-1573-pars-ii\review"
$mdFile = "selnecker-institutiones-1573-pars-ii.md"
$refDoc = Join-Path $repoRoot "shared\reference-custom.docx"

$shareableStem = "Nikolaus-Selnecker-The-Institution-of-the-Christian-Religion-Pars-II-1579-English-Scholastic-Lutherans"

Set-Location $reviewDir

# Remove any prior artifacts
Remove-Item "$shareableStem.docx", "$shareableStem.pdf", "selnecker-institutiones-1573-pars-ii.docx", "selnecker-institutiones-1573-pars-ii.pdf" -ErrorAction SilentlyContinue

Write-Host "Building shareable Selnecker Pars II..." -ForegroundColor Cyan
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
