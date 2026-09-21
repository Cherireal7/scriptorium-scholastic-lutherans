# Bundled fonts

Files needed by build scripts that reference typographic-display faces on
the title/cover pages of finished volumes.

## IM Fell English

Kirchner Methodica 1595, Balduin Casibus Conscientiae 1628, and other
Wittenberg-orthodoxy volumes reference **IM Fell English** on title-page
runs. It is a public-domain revival by Igino Marini of 17th-century punches
cut by John Fell (Bishop of Oxford) — a genuinely period-appropriate face
for the 1580–1690 texts.

Files here:

- `IMFeENrm28P.ttf` — Regular (roman)
- `IMFeENit28P.ttf` — Italic
- `OFL.txt` — SIL Open Font License 1.1 (redistribution allowed with license)

Source: <https://github.com/google/fonts/tree/main/ofl/imfellenglish>
Family page: <https://fonts.google.com/specimen/IM+Fell+English>

## Installing on a build machine

Windows (per-user, no admin needed):

```powershell
$src  = 'C:\Users\hp\documents\github\scholastic-lutherans\shared\fonts'
$dest = "$env:LOCALAPPDATA\Microsoft\Windows\Fonts"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Get-ChildItem "$src\*.ttf" | ForEach-Object {
    $target = Join-Path $dest $_.Name
    Copy-Item $_.FullName $target -Force
    Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts' `
        -Name 'IM Fell English (TrueType)' -Value $target
}
```

On the current machine this has already been done (2026-09-21). Restart
Word / LibreOffice to pick the font up.

Linux/macOS: copy the `.ttf` files to `~/.fonts/` (Linux) or
`~/Library/Fonts/` (macOS), then `fc-cache -fv` if on Linux.

## Fallback if not installed

The DOCX title pages reference the face by name only. If the face is not
installed, Word/LibreOffice silently substitute the default serif. The
volume still builds cleanly — just with a slightly less period-appropriate
title-page look.
