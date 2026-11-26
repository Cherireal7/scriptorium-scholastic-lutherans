# Musculus · Precationes ex veteribus orthodoxis doctoribus · Working Notes

Two English volumes, built from the same working files:

| Volume | Latin edition | Scan | PDF pages |
|---|---|---|---|
| Strict 1561 edition | Frankfurt on the Oder, 1561 (VD16 ZV 26230), [5] + 139 leaves | BSB Munich, Asc. 5561 x, `bsb10173614` (= Google Books `lHw7AAAAcAAJ`, the link the requester sent) | 197 |
| Enlarged 1573 edition | Leipzig, Andreas Schneider, typis Voegelianis, 1573 (VD16 M 7192), 262 pp. | BSB Munich, Asc. 5554 s, `bsb00019110` (public domain mark) | 267 |

Status (2026-11-26): both translated, audited and built.

## What is here

```
musculus-precationes/
├── notes.md                    this file
├── CONVENTIONS.md              translation rules used for both volumes
├── build.py                    python3 build.py 1561 | 1573  →  review/<shareable name>.pdf
├── review/
│   ├── translation-1573/       Markdown parts 01–10 (title, calendar, preface, sections I–XVIII, index, two appendices)
│   ├── translation-1561/       Markdown parts 01–10 (title, dedication, sections I–XVIII, appendix)
│   ├── front-<edition>.html    half-title, title page, copyright page
│   └── translators-note-<edition>.md
├── audit-1573/                 second-reader logs, one per part, and the collation of the two editions
├── audit-1561/                 logs of the 1561 pass, one per part
└── sources-original/           (git-ignored) fetch scripts; scans live in ~/Documents/Scholastic-Lutherans/sources/musculus-precationes/
```

## How it was made

1. **Source.** BSB open IIIF API: manifest, page images and the library's hOCR per page (see `sources-original/fetch-page*.sh`). Halle, DDB, PRDL, the MDZ website and Google Books block scripted access.
2. **Translation (1573).** Eight parallel translators, each on a fixed image range, reading the page images with the OCR as an aid. Format rules in `CONVENTIONS.md`.
3. **Audit (1573).** Eight second readers who had not translated the text compared every page with the image; 23 corrections, logged in `audit-1573/`. A page-by-page count of English against Latin showed nothing skipped.
4. **Collation.** `audit-1573/collation-1561-1573.md`: 1573 contains every prayer of 1561 in the same order and adds 94 pieces at the ends of ten sections, a calendar, a new preface and an index.
5. **1561 volume.** Each section re-read against the 1561 images: 1573-only pieces removed, leaf markers put in, 43 wording variants followed with footnotes. Single pass (no second reader on the 1561 changes).
6. **Build.** Markdown → HTML → Chrome headless PDF, two passes for the contents page numbers. 6.14 × 9.21 in, Palatino, red headings, small-caps running heads.

## Differences from the other volumes of the programme

- Prayer register: *thou / thee*, to sit beside the KJV psalms.
- Notes stand at the end of each section, not in one apparatus at the end of the volume.
- Original page (1573) or leaf (1561) numbers are shown in the text in small red brackets.
- The build is HTML/Chrome on macOS, not pandoc → DOCX → LibreOffice.

## Open points

- 1573 volume: six `[?]` readings (five in the calendar, one dedicatee's surname, "Jokisl", probably Jokisch); KJV "LORD" in the Psalms is not uniform; "Oratio" is "Collect" in some sections and "Prayer" in others.
- 1561 volume: a few of the 43 variants may be slips of the 1561 press that 1573 corrected; the footnotes give both readings and `audit-1561/*-log.md` lists each under "Doubtful".
- Other printings (1559, 1562, 1571, 1580) not compared; sources of single prayers not traced (several unattributed pieces are probably Erasmus, *Precationes aliquot novae*; the fifteen "O Jesu" prayers are those ascribed to St Bridget).
