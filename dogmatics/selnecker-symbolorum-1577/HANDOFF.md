# Handoff — Selnecker Vol III (Symbolorum Exegesis 1577)

**Read this first.** This document is a self-contained brief for whoever picks up the translation of Selnecker's third volume in a fresh chat. Everything you need to start T1 is here or in the file paths named here — no prior-chat context required.

## What this project is

You are translating **Nikolaus Selnecker · *Symbolorum Apostolici, Niceni, et Athanasiani Exegesis*** (Leipzig, Rhamba, 1577) from Latin into modern English, for publication as the third volume in the Scholastic-Lutherans Selnecker programme.

Volumes I and II (*Institutionis Christianae Religionis* Pars I & Pars II) are already complete and published as shareable PDFs in this repo. This volume is the natural continuation of that dogmatic arc: it takes up the mature Lutheran Christology (Communicatio Idiomatum, Majesty of the Son of Man, ubiquity, Real Presence) that Pars II only touched on, and it reprints Selnecker's own 1560 Heidelberg disputation on the Lord's Supper as an appendix.

**Important:** There is no *Institutio Pars III*. The *Institutio* is a two-part work. The 1577 *Symbolorum exegesis* is the standalone volume that fills the "volume III" slot in Selnecker's dogmatic-catechetical output. Do not go looking for a Pars III — you will not find one.

## Where everything lives

Working directory: `dogmatics/selnecker-symbolorum-1577/`

```
selnecker-symbolorum-1577/
├── HANDOFF.md                                       # this file
├── notes.md                                         # source bibliography + full structural map + tranche plan
├── build-shareable.ps1                              # PowerShell build (pandoc → DOCX → LibreOffice → PDF)
├── sources-original/
│   ├── selnecker-symbolorum-1577.pdf                # 41.3 MB · 399 PDF-pages · 368 print pages · BSB copy
│   ├── extract.py                                   # pdfplumber extraction script
│   └── symbolorum-full.txt                          # 13,340-line OCR of the whole book
├── latex/                                           # (empty; reserved for LaTeX-format outputs if wanted)
└── review/                                          # (empty; you will create selnecker-symbolorum-1577.md here)
```

**Model volumes to consult** whenever a convention question arises:

- Pars I: `dogmatics/selnecker-institutiones-1573/review/selnecker-institutiones-1573.md`
- Pars II (most recent, most refined): `dogmatics/selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md`
- Pars I notes: `dogmatics/selnecker-institutiones-1573/notes.md`
- Pars II notes (full T1–T10 tranche history): `dogmatics/selnecker-institutiones-1573-pars-ii/notes.md`

## Start-of-work checklist

1. `Read` this file and `notes.md` in full.
2. `Read` the first ~800 lines of the Pars II working MD (`dogmatics/selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md`) to internalise the front-matter conventions (YAML header, `{=openxml}` half-title / title / colophon blocks, Translator's Note, Biographical Sketch, Table of Contents).
3. `Read` the last ~200 lines of the same Pars II MD to see how the endnote apparatus is presented.
4. Skim the OCR (`sources-original/symbolorum-full.txt`) at the tranche boundaries in the structural-map table (in `notes.md`) to confirm what you're about to translate.
5. Create `review/selnecker-symbolorum-1577.md` and begin **T1** (front matter — see below).

## Tranche plan

Full detail is in `notes.md` under **Suggested tranche plan (Vol III — proposed)**. In brief:

| T | Content | Approx OCR lines |
|---|---|---|
| **T0** | Source + OCR + structural survey (done — this handoff) | — |
| **T1** | Translator's Note + Biographical Sketch + Title-page + Dedication (April 1575) + The Three Creeds printed together | ~1500 |
| **T2** | *Enarratio Symboli* general prolegomena (creeds, synods, divisions) | 1477–2376 |
| **T3a-c** | Article I *Credo in Deum Patrem* — three parts | 2377–6498 |
| **T4a-c** | Article II *Credo in Iesum Christum* — three parts | 6499–10579 |
| **T5** | Doctrina de Communicatione Idiomatum (Chalcedon-Greek intense) | 10580–11000 |
| **T6** | Ascension article + An Christus sit omnipræsens | 11001–11578 |
| **T7** | De Sessione ad dexteram + De Adoratione + De Iudicio | 11579–12623 |
| **T8** | Article III opener (Spiritus + Ecclesia + Epiphanius Greek) | 12624–12754 |
| **T9** | **Heidelberg Disputation 1560** — historically significant | 12755–13229 |
| **T10** | De Iuda accipiente patristic catena + Colophon + endnote apparatus + constructed TOC | 13230–13337 |
| **Audit + Build** | Parallel-agent audit + PDF build | — |

Adjust as you go — the Pars II tranche plan mutated significantly in flight; the plan is a starting frame, not a contract.

## Non-negotiable conventions

These are carried over from Pars I & II and are load-bearing. Do not silently drop them.

1. **Bible-citation policy.** Every scripture quotation in the body is *your own* English rendering of Selnecker's *own* Latin citation. **Do not quote NKJV, NIV, ESV, KJV, or any other modern English Bible version anywhere in the volume** — not even as a footnote proof-text. This sidesteps the NKJV 500-verse licence limit and the NIV citation restrictions entirely. Preserve Selnecker's own numbering (which follows the Vulgate on some Psalms); flag any divergence from Hebrew/English numbering inline the first time it occurs in a section.

2. **Latin-original block preservation.** Verse-fragments, poetic distichs, Chalcedon-formula Greek, and any Greek code-switching passage are quoted in the Latin/Greek original *first*, followed immediately by an English rendering in the next paragraph or on the next line. This is especially critical in T5 (Communicatio Idiomatum) and T8 (Epiphanius Greek Creed-fragment) — the volume's argument sometimes turns on the exact Greek term.

3. **Greek passage cross-check against JPG facsimile.** The OCR has sporadic Greek-character corruption where the Antiqua Greek types were confused with Latin. Every substantive Greek passage in the translation must be cross-checked against the actual page image before shipping. Use `pdfplumber` or a PDF-viewer to render the specific PDF-page for the Greek passage; do not trust the OCR-extracted Greek without verification.

4. **Endnote apparatus at volume end, cross-referenced.** Numbered endnotes ¹ ² ³ … using superscript Unicode digits. Collect them in a single apparatus at the very end of the volume, immediately before back-matter (this volume has no printed back-matter, so endnotes are the final section). Cross-references between endnotes use `[[note-N]]` syntax that Pandoc will preserve. See Pars II endnote apparatus for the exact form.

5. **Reader-facing Translator's Note = no internals.** The Translator's Note that ships to readers must not mention local file paths (`sources-original/`, `shared/`, `terms.yaml`), tranche-plan language ("T1", "T3b", etc.), memory-link `[[...]]` syntax, or any internal build detail. It should read as though written for a book buyer. The Pars II Translator's Note (post-completion rewrite in commit `faa50ef`) is the model — copy its structure.

6. **Structural section-header convention.** In the working MD, use:
   - `#` — volume title
   - `##` — Translator's Note / Biographical Sketch / Table of Contents / major creed articles (Prolegomena, Article I, Article II, Article III, Heidelberg Disputation, De Iuda, Endnotes)
   - `###` — sub-articles within a creed (e.g. *De Communicatione Idiomatum*, *De Ascensione*, *An Christus sit omnipræsens*)
   - `####` — scholia / questions / catena subdivisions

7. **Endnote debt discipline.** If you use an endnote-superscript in the body during a tranche, you must add the corresponding endnote entry in the same commit. Do not defer. Pars II had to run a T-audit-1 backfill because 53 endnote entries had been superscripted without corresponding entries — that's a preventable failure mode.

8. **Commit as you finish each tranche.** Do not batch multiple tranches into one commit. The Pars II git log is the model — each `T{N}{letter}` gets its own commit with a message that itemises the sections completed and the endnote-range added. This is important for both incremental review and rollback safety.

## Build pipeline

`build-shareable.ps1` is pre-populated with the correct paths and the shareable-name stem:

    Nikolaus-Selnecker-Exposition-of-the-Apostles-Nicene-and-Athanasian-Creeds-1577-English-Scholastic-Lutherans

Run from PowerShell:

    powershell -File "C:\Users\hp\documents\github\scholastic-lutherans\dogmatics\selnecker-symbolorum-1577\build-shareable.ps1"

Produces `Nikolaus-Selnecker-…-Scholastic-Lutherans.docx` and `.pdf` in `review/`. It uses:
- Pandoc at `$env:LOCALAPPDATA\Pandoc\pandoc.exe`
- LibreOffice at `C:\Program Files\LibreOffice\program\soffice.exe`
- Reference DOCX at `shared/reference-custom.docx` (shared across all volumes in the repo)

## Bibliographic details for the front matter

Use these verbatim in the title-page and colophon blocks:

- **Title (as printed):** *Symbolorvm Apostolici, Niceni, et Athanasiani Exegesis, fideliter repetens doctrinam perpetuam Ecclesiæ Dei de præcipuis Capitibus & Articulis Christianæ Fidei, inprimis de Diuinitate æterna Filij Dei, de Vnione hypostatica duarum naturarum in Christo, de Maiestate Filij hominis, de Communicatione idiomatum: de Cœna Domini &c. Contra recentes horum temporum blasphemias.*
- **Author (as printed):** *Nicolao Selneccero D. Electorali Professore in Academia Lipsica.*
- **Motto (title-page, Augustine epist. 7):** *Nimis peruersè seipsum amat, qui & alios errare vult, ut error ipsius lateat.*
- **Imprint:** *Lipsiæ, Iohannes Rhamba excudebat. M.D.LXXVII.* (Leipzig, Johann Rhamba, 1577)
- **VD16 identifier:** unverified in the sourcing session — check VD16 directly if you want to cite it (candidate: VD16 S 5568 or thereabouts; Pars II is S 5566).
- **Physical description of the scan:** 368 printed pages, octavo, BSB Munich shelfmark stamp `00021305` on every folio verso. Google-Books ID `hyfSeau9q60C`. Downloaded 2026-09-08.
- **1575 first-edition reference (for the Translator's Note):** the 1577 imprint is the enlarged reissue of the 1575 first edition (Google-Books `QyE8AAAAcAAJ`, also BSB Munich). The Dedicatory Epistle carries the original April-1575 date; Selnecker did not re-date it for the reissue.
- **Dedicatee:** Johann Günther, Count of Schwarzburg — of the four Imperial Counts, Count of Schwarzburg-Arnstadt-Sondershausen-Leutenberg. A Lutheran count of one of Selnecker's supportive territorial families.

## Suggested T1 opening (front matter to draft)

Follow Pars II's opening structure exactly, but re-write every prose paragraph fresh for this volume. The half-title / title-page / colophon `{=openxml}` blocks can be adapted almost verbatim (change the section titles, the imprint line to *Leipzig · Johann Rhamba · 1577*, and the italic side-note *[Vol III of the Selnecker programme]* — do not say "Pars III" or "Part Three of Three" since the *Institutio* itself is a two-part work).

The Translator's Note for this volume differs from Pars II's in one important respect: **Pars II's note is a post-completion note for a completed volume**. Yours is being written at the start of Vol III of an ongoing three-volume programme, so it should:
- Situate this volume as the natural continuation of the *Institutio* (not as a "Pars III"),
- Explain the Heidelberg-Disputation-1560 appendix's historical significance (Selnecker at Heidelberg pre-Kryptocalvinist turn),
- Reiterate the Bible-citation and Latin-original-preservation policies (verbatim from Pars II — those paragraphs are not volume-specific),
- Note that the 1577 imprint is the enlarged reissue of 1575 and carries the original 1575 dedication,
- Note the absence of printed back-matter apparatus in this edition (no Elenchus, no Patrum Sententiae index, no subject index) — flag whether the English edition will construct one from scratch or ship without.

## When you are done

Run the parallel-agent audit at the end (Pars II T-audit-1 methodology): spawn 3–4 `Explore` subagents in parallel to audit different portions of the OCR against the English translation for missing biblical citations, missing Father-quotations, missing thesis-numbers, missing Antithesis-catalogue items. Pars II ran 4 agents and each returned "no substantive gaps" — that is the bar.

Then commit the final `Nikolaus-Selnecker-…-Scholastic-Lutherans.pdf` alongside the working MD and push to `origin/master`. The user has been running with a solo-master workflow; no PR gate.

## Git / repo etiquette carried from Pars II

- Commit messages use the format `Selnecker Symbolorum T{N}{letter}: <what-was-done> (OCR ln <start>-<end>, ~<lines>) — <one-line-narrative>` — see the Pars II git log for the pattern.
- Do not push directly to shared remotes without the user's OK. Solo workflow so far, but confirm.
- Never `git add -A` — always add specific files by name to avoid committing scratch files.

Good luck. Everything is in place — the PDF is downloaded, the OCR is extracted, the structural map is written, the build script is ready. All that remains is the translation itself.
