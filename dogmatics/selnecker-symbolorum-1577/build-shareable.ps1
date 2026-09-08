# Selnecker Symbolorum 1577 — Shareable Build
# ═══════════════════════════════════════════════════════════════════════════
# Builds ONLY the shareable-named PDF (and DOCX).
# Does not produce the working-name build artifact.

$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
$lo = "C:\Program Files\LibreOffice\program\soffice.exe"
$repoRoot = "$HOME\Documents\Github\scholastic-lutherans"
$reviewDir = Join-Path $repoRoot "dogmatics\selnecker-symbolorum-1577\review"
$mdFile = "selnecker-symbolorum-1577.md"
$refDoc = Join-Path $repoRoot "shared\reference-custom.docx"

$shareableStem = "Nikolaus-Selnecker-Exposition-of-the-Apostles-Nicene-and-Athanasian-Creeds-1577-English-Scholastic-Lutherans"

Set-Location $reviewDir

# Remove any prior artifacts
Remove-Item "$shareableStem.docx", "$shareableStem.pdf", "selnecker-symbolorum-1577.docx", "selnecker-symbolorum-1577.pdf" -ErrorAction SilentlyContinue

Write-Host "Building shareable Selnecker Symbolorum 1577..." -ForegroundColor Cyan
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
