# Kirchner Methodica 1595 — VOLUME COMPLETE

**Task:** *Timotheus Kirchner, Methodica Explicatio* (Jena: Beyer, 1595) — English rendering.

## Status as of 2026-09-09

**COMPLETE.** No further tranches. Do not open a fresh chat to continue this volume.

- **Last commit at completion:** T107 (Fladyng's *Vita Kirchneri* + Aquila's Epitaphium).
- **MD file:** `review/kirchner-methodica-1595.md` — ~14.2k lines, closing marker at end of file.
- **Tranches:** 107 committed (T1–T107).
- **Main body:** 46 Loci, 929 top-level Questions, 442 formal Objections.
- **Appendix:** Fladyng's biography of Kirchner (T107).
- **PDF/DOCX build:** `pwsh -f build-shareable.ps1` from the volume root.

## What was deliberately omitted

The printed 1595 volume ends with two Latin apparatus sections that were **not** translated:

1. **Index Locorum huius Libelli** (OCR 48719 – ~51500): a table of contents mapping locus/chapter headings to page-numbers in the Beyer 1595 print. Its entries look like "Locus I. De Sacra Scriptura ... p.1.2" — those page-numbers refer to the *Latin* print, not to our English MD file, so translating them would produce dead references.

2. **Index Scripturae in hoc Methodico Libello Explicatorum** (OCR ~51500 – 51938): a Scripture-passage index likewise keyed to Latin page-numbers.

3. **Printer's colophon** (OCR 51934–51945): *"Soli Domino, Deo veritatis, sit gloria, Amen. LIPSIAE. Ex officina Typographica."*

An earlier draft of this handoff had speculated that a "short-form second catechetical cycle" of Loci I–XXIV followed the main body. **That was a misreading of the Index Locorum.** No such second cycle exists in the volume.

## What is next for the wider programme

Kirchner Methodica 1595 is now closed. Update the parent programme memory / progress board to move to the next volume in queue. Historical checkpoint memory `reference-methodica-1595-handoff-2026-09-08` can be retired or marked as *volume closed 2026-09-09* on your next memory-maintenance pass.

## If future revision is needed

- All 46 Loci are inside one MD file. Search by `## Locus N.` for locus-level anchors, or `## Question N.` inside each locus.
- The end-of-tranche end-markers (in italic `*[...]*` blocks) were removed and replaced as each tranche was appended. Only the final volume-complete marker remains — the intermediate ones are recoverable from git history if a per-tranche breakdown is ever needed.
- Style rules used consistently across T1–T107 are documented in the older versions of this handoff and in memory `reference-scholastic-lutherans-workflow`.
