# Handoff — Selnecker Institutio Pars III (Jena 1579, VD16 S 5567, catechetical)

**Read this first.** This is a self-contained brief for whoever picks up the translation of Selnecker's Institutio Pars III in a fresh chat. Everything you need to start T1 is here or in the file paths named below — no prior-chat context required.

## What this project is

You are translating **Nikolaus Selnecker · *Institutionis Christianae Religionis Pars Tertia, Continens Doctrinam Catecheticam*** (Jena, Jakob Tröster, 1579) from Latin and Greek into modern English, for publication as the completion of the three-part Jena 1579 Institutio in the Scholastic-Lutherans Selnecker programme.

Pars I and Pars II are already complete and published as shareable PDFs in this repo. Pars III is the **catechetical capstone**: Luther's Small Catechism printed Græcè & Latinè in parallel + a Decalogi Explicatio + Quaestiones Catecheticae ad usum Scholarum (schoolroom Q&A). It is a bilingual Latin schoolbook, not a Loci-style dogmatic.

**Why Pars III matters:** our earlier memory recorded (erroneously) that "the Institutio is a two-part work." That is wrong — the canonical Jena 1579 Tröster set is three parts (VD16 S 5565 + S 5566 + **S 5567** = this volume). The 2026-10-23 bibliographic sweep corrected that. Translating Pars III completes the canonical set.

## Where everything lives

Working directory: `dogmatics/selnecker-institutiones-1573-pars-iii/`

```
selnecker-institutiones-1573-pars-iii/
├── HANDOFF.md                              # this file
├── notes.md                                # source + structural map + tranche plan
├── build-shareable.ps1                     # Pandoc → DOCX → LibreOffice → PDF
├── sources-original/
│   ├── selnecker-institutio-pars-iii-1579.pdf   # 178 MB · 346 pages · BSB IIIF assembly
│   ├── download-and-assemble.py            # the IIIF downloader (don't re-run unless replacing source)
│   ├── extract.py                          # pdfplumber scaffold (NB: current PDF has no text layer)
│   └── jpg/p00001.jpg … p00346.jpg         # raw IIIF images — feed to Claude vision per-page
├── latex/                                  # (empty; reserved)
└── review/                                 # (empty; you will create selnecker-institutio-pars-iii-1579.md here)
```

**Model volumes to consult** whenever a convention question arises:
- Pars I MD: `dogmatics/selnecker-institutiones-1573/review/selnecker-institutiones-1573.md`
- Pars II MD (most refined): `dogmatics/selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md`
- Symbolorum 1577 MD (bilingual Greek precedent): `dogmatics/selnecker-symbolorum-1577/review/selnecker-symbolorum-1577.md`
- Pars I notes.md, Pars II notes.md, Symbolorum notes.md

## Start-of-work checklist

1. `Read` this file and `notes.md` in full.
2. `Read` the first ~800 lines of the Pars II MD to internalise the YAML front matter, `{=openxml}` half-title/title/colophon blocks, Translator's Note, Biographical Sketch, Table of Contents.
3. `Read` the Symbolorum MD section on parallel Greek passages (search for `τηρήσας` or `Chalcedon`) to see how Greek+Latin+English parallel presentation is done.
4. Inspect `sources-original/jpg/p00001.jpg` through `p00012.jpg` to find the title page + any dedication + preface. (The front-matter boilerplate pages are usually in the first dozen.)
5. Begin **T1** (Translator's Note + Biographical Sketch + Title page + Dedication + first Luther-SC bilingual section).

## OCR strategy — different from Pars I and II

**Pars III has no Google-Books text-layer OCR available.** The assembled PDF is image-only. **Use Claude vision page-by-page** — this is the project's documented best practice anyway (cleaner than Tesseract for 16th-c. Antiqua Latin + essential for the Antiqua Greek interleaving).

Workflow for each tranche:
1. Pick the JPG range for the tranche (e.g. T2 = JPGs p00013–p00060 for Luther SC bilingual).
2. For each page, open the JPG via the `Read` tool (as an image).
3. Transcribe the Latin + Greek verbatim into a scratch buffer.
4. Translate paragraph-by-paragraph into the body MD, preserving Greek + Latin originals *before* the English rendering.

If a page is damaged, blurry, or ambiguous, flag it inline (`[OCR unclear p027: ...]`) rather than guessing.

## Tranche plan (preliminary — detail in `notes.md`)

| T | Content | Approx JPG range (verify after survey) |
|---|---|---|
| **T0** | Source + staging (done — this handoff) | — |
| **T1** | Translator's Note + Biographical Sketch + Title page + Dedication + opening Luther-SC bilingual | 1–20 |
| **T2–T3** | Luther Small Catechism Græcè & Latinè, full (Decalogue + Creed + Pater Noster + Baptism + Confession + Supper) | ~20–100 |
| **T4–T6** | Decalogi Explicatio (I–III / IV–VI / VII–X) | ~100–240 |
| **T7–T8** | Quaestiones Catecheticae ad usum Scholarum (block-by-block) | ~240–330 |
| **T9** | Colophon + endnote apparatus + constructed TOC + volume PDF build | ~330–346 |
| **Audit + Build** | Parallel-agent audit + build-shareable.ps1 | — |

Adjust in flight — these ranges are provisional until you have scanned the facsimile.

## Non-negotiable conventions

Carried over from Pars I, Pars II, and Symbolorum. Do not silently drop.

1. **Bible-citation policy.** Every scripture quotation in the body is *your own* English rendering of Selnecker's *own* Latin / Greek citation. **Do not quote NKJV, NIV, ESV, KJV, or any other modern English Bible version anywhere in the volume** — not even as a footnote. Preserve Selnecker's own numbering (which follows the Vulgate on some Psalms); flag any divergence from Hebrew/English numbering inline the first time it occurs in a section.

2. **Bilingual Greek + Latin preservation (volume-specific).** This Pars is unique: Luther's SC prints in parallel Greek and Latin columns. The English edition must preserve **both originals** — Greek first (verbatim with accents + breathings), then Latin, then English rendering below. The parallel-column format is the whole pedagogical point. Do not elide the Greek.

3. **Antiqua-Greek verification against JPG.** The IIIF images have Antiqua-Greek passages that any mechanical OCR would corrupt. For every Greek word in the translation, cross-check against the specific JPG page before committing. If a Greek word is ambiguous, flag it inline rather than silently normalise.

4. **Endnote apparatus at volume end, cross-referenced.** Numbered endnotes ¹ ² ³ … using superscript Unicode digits. Collect in a single apparatus at the very end of the volume. Cross-references between endnotes use `[[note-N]]` syntax. See Pars II for the exact form.

5. **Reader-facing Translator's Note = no internals.** No file paths (`sources-original/`, `jpg/`, `shared/`), no tranche-plan language ("T1", "T3b", etc.), no memory-link `[[...]]` syntax, no build detail. The Pars II Translator's Note is the model.

6. **Structural section-header convention.** In the working MD, use:
   - `#` — volume title
   - `##` — Translator's Note / Biographical Sketch / Table of Contents / major sections (Luther Catechism · Decalogue Exposition · Catechetical Questions · Endnotes)
   - `###` — sub-sections (e.g. the five chief parts of the Small Catechism; each commandment of the Decalogue)
   - `####` — individual questions / scholia

7. **Endnote debt discipline.** Add the endnote entry in the *same commit* as the superscript in the body. Do not defer.

8. **Commit as you finish each tranche.** Do not batch. Each `T{N}{letter}` gets its own commit. Format:
   `Selnecker Institutio Pars III T{N}{letter}: <sections> (JPGs pNNNN-pNNNN) — <one-line>`

## Build pipeline

`build-shareable.ps1` is pre-populated with the correct paths and the shareable-name stem:

    Nikolaus-Selnecker-The-Institution-of-the-Christian-Religion-Pars-III-1579-English-Scholastic-Lutherans

Run from PowerShell:

    powershell -File "C:\Users\hp\documents\github\scholastic-lutherans\dogmatics\selnecker-institutiones-1573-pars-iii\build-shareable.ps1"

Produces `.docx` and `.pdf` in `review/`. Uses:
- Pandoc at `$env:LOCALAPPDATA\Pandoc\pandoc.exe`
- LibreOffice at `C:\Program Files\LibreOffice\program\soffice.exe`
- Reference DOCX at `shared/reference-custom.docx` (shared across all volumes in the repo)

## Bibliographic details for the front matter

Use these verbatim in the title page and colophon blocks:

- **Title (as printed):** *Institvtionis Christianae Religionis Pars … 3, Continens Doctrinam Catecheticam: Catechismum D. D. Lutheri Græcè & Latinè: Decalogi Explicationem: & Quaestiones Catecheticas, accomodatas ad vsum Scholarum.*
- **Author (as printed):** *Nicolao Selneccero D. Electorali Professore in Academia Lipsica.* (verify against title-page facsimile — may read "D. Nicolaus Selnecker" or "D. Nicolao Selneccero D. Theologo"; match the facsimile exactly.)
- **Imprint:** *Jenæ, Iakob Tröster, Anno M.D.LXXIX.* (Jena, Jakob Tröster, 1579) — verify against title-page facsimile.
- **VD16 identifier:** S 5567
- **Physical description of the scan:** 346 BSB IIIF canvases, octavo, BSB Munich shelfmark Dogm. 924-3 (parent of the three-part Dogm. 924-1/2/3 set — verify against the shelfmark stamp on the frontispiece). BSB MDZ ID `bsb10175492`. Downloaded 2026-10-23.
- **Dedicatee:** verify against the facsimile (not yet surveyed).

## Suggested T1 opening

Follow Pars II's opening structure exactly, re-writing every prose paragraph fresh for this volume. The half-title / title-page / colophon `{=openxml}` blocks can be adapted almost verbatim (change the section titles, the imprint line to *Jena · Jakob Tröster · 1579*, and the sub-caption *[Pars Tertia of Three]* — the three-part structure is now bibliographically confirmed so you can say "Part Three" without hedging).

The Translator's Note for this volume should:
- Situate this as the completion of the Jena 1579 three-part set, pairing with Pars I 1579 + Pars II 1579;
- Explain the Luther-SC-in-Greek pedagogical move (Melanchthon's Lutheran-humanist programme; the Latin-school curriculum; parallel the Augustana Græca);
- Reiterate the Bible-citation and Latin/Greek-original-preservation policies (verbatim from Pars II — those paragraphs are not volume-specific);
- Note that Pars III has no Google-Books text-layer OCR, so this translation is based on direct per-page vision reading of the BSB IIIF JPGs (good — more faithful to the facsimile than relying on OCR); mention this transparently once in the Note.

## When you are done

Run the parallel-agent audit at the end (Pars II T-audit-1 methodology): spawn 3–4 `Explore` subagents in parallel to audit different portions of the facsimile (JPG ranges) against the English translation. Each agent reads a block of JPGs and the corresponding MD section and reports any paragraph-level or Scripture-reference drop. Pars II and Symbolorum each cleared the "no substantive gaps" bar with four agents; aim for the same.

Then commit the final `.pdf` alongside the working MD and push to `origin/master`. The user has been running with a solo-master workflow; no PR gate.

## Git / repo etiquette carried from Pars II

- Commit messages format: `Selnecker Institutio Pars III T{N}{letter}: <what-was-done> (JPGs pNNNN-pNNNN, ~<lines>) — <one-line-narrative>` — see Pars II git log for the pattern.
- Do not push directly to shared remotes without the user's OK. Solo workflow so far, but confirm.
- Never `git add -A` — always add specific files by name.

Good luck. Everything is in place — the PDF is assembled, the 346 JPGs are staged for vision OCR, the build script is ready. All that remains is the translation itself.
