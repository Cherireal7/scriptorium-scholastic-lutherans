# Handoff — Selnecker Paedagogia Christiana (Frankfurt 1577, VD16 S 5626)

**Read this first.** This is a self-contained brief for whoever picks up the translation of Selnecker's *Paedagogia Christiana* in a fresh chat. Everything you need to start T1 is here or in the file paths named below — no prior-chat context required.

## What this project is

You are translating **Nikolaus Selnecker · *Pædagogiæ Christianae, denuo et ultimo auctae, Pars Prima + Pars Secunda*** (Frankfurt am Main, Nicolaus Bassaeus, 1577) from Latin into modern English, for publication as a two-volume paedagogical-catechetical set in the Scholastic-Lutherans Selnecker programme.

**The author's own self-designation of this edition is load-bearing.** The 1577 title explicitly reads *DENVO ET VLTIMO AVCTAE, ita vt eius recognitione deinceps non opus sit amplius* — "newly and finally expanded, such that no further revision will henceforth be needed." Selnecker is telling the reader that this is his definitive word on the Paedagogia. That's why the 1577 Bassaeus is the right text-base, not the 1565 Brubach editio prima nor the 1568 Rebart intermediate reissue.

## The two-part structure (not three)

**The Latin Paedagogia Christiana is a TWO-part work.** No Latin Pars III exists. VD16 S 5626 is a single number covering both volumes:

- **Pars Prima** — *Explicatio Decalogi* (Exposition of the Ten Commandments). 396 pp.
- **Pars Secunda** — *Explicatio Trium Symbolorum* (Exposition of the Three Creeds). 587 pp.

The "three-part" Paedagogia (with Prayer + Sacraments as Pars III) exists **only in the German translation by Lucas Maius** (Bärwald Leipzig 1569 / Feyerabend Frankfurt 1570 — VD16 S 5629). The prayer/sacraments material in Selnecker's Latin corpus is instead distributed across:
- *Institutio Pars II* — *De Oratione* appendix + *De Sacramentis* / *De Baptismo* / *De Coena Domini* loci
- *Institutio Pars III* — catechetical schoolbook with Luther's Small Catechism

**Do not seek a Latin Pars III.** It was never printed.

## Overlap with already-shipped volumes — translate anyway

Per user direction: "I kinda think we should translate the whole Paedagogy, even if it's overlapping — sometimes it's useful to see development in thought."

1. **Paedagogia Pars I (Decalogue)** overlaps with:
   - Already-shipped *Institutio Pars I* Locus 7 (*De lege*) — Loci-style theological treatment.
   - Being-staged *Institutio Pars III* Decalogi Explicatio — schoolroom catechesis.
   - This volume: paedagogical scaffolding for teachers + learners.

2. **Paedagogia Pars II (Three Creeds)** overlaps with:
   - Already-shipped *Symbolorum Apostolici, Niceni, et Athanasiani Exegesis* (Leipzig 1577) — mature polemical creed-exposition with Communicatio Idiomatum + Heidelberg 1560 Disputation appendix.
   - This volume: catechetical creed-exposition for school use.

In each case the overlap is *generic*: same author, same decade, same doctrinal substance, different pedagogical register. The whole point of translating both is to let the English reader see Selnecker's thinking move between registers — Loci-style for seminary, polemical-exegetical for synod, catechetical for the schoolroom.

## Where everything lives

Working directory: `dogmatics/selnecker-paedagogia-christiana-1565/`

(Folder is named after the editio-prima year 1565 by convention — see sibling `selnecker-institutiones-1573`. The text-base is actually the 1577 reissue; the folder-name convention is purely bibliographic honor-the-editio-prima.)

```
selnecker-paedagogia-christiana-1565/
├── HANDOFF.md                                 # this file
├── notes.md                                   # source + structural map + tranche plan
├── build-shareable.ps1                        # Pandoc → DOCX → LibreOffice → PDF (Pars I)
├── sources-original/
│   ├── paedagogia-pars-i-1577.pdf             # 206 MB · 432 pages · BSB IIIF assembly (bsb10175496)
│   ├── paedagogia-pars-ii-1577.pdf            # ~250 MB · ~630 pages · BSB IIIF assembly (bsb10175497)
│   ├── download-and-assemble.py               # the IIIF downloader (don't re-run unless replacing source)
│   ├── jpg-bsb10175496/p00001.jpg … p00432.jpg # raw IIIF Pars I images — Claude vision OCR per-page
│   └── jpg-bsb10175497/p00001.jpg … p00NNN.jpg # raw IIIF Pars II images
├── latex/                                     # (empty; reserved)
└── review/                                    # (empty; you will create per-pars MDs here)
```

**Model volumes to consult** whenever a convention question arises:
- *Institutio* Pars I MD: `dogmatics/selnecker-institutiones-1573/review/selnecker-institutiones-1573.md`
- *Institutio* Pars II MD (most refined): `dogmatics/selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md`
- *Symbolorum 1577* MD (the companion creed-exposition to Paedagogia Pars II): `dogmatics/selnecker-symbolorum-1577/review/selnecker-symbolorum-1577.md`

## Start-of-work checklist

1. `Read` this file and `notes.md` in full.
2. `Read` the first ~800 lines of the Institutio Pars II MD to internalise the YAML front matter, `{=openxml}` blocks, Translator's Note, Biographical Sketch, Table of Contents.
3. **Optional comparison read**: skim the first ~300 lines of the Symbolorum 1577 MD to see how Selnecker handles creed-exposition at the polemical register (useful for Pars II because of the overlap).
4. Inspect `sources-original/jpg-bsb10175496/p00001.jpg` through `p00020.jpg` to find Pars I title page + dedication + preface.
5. Decide whether to start with Pars I (Decalogue) or Pars II (Creeds). **Default: Pars I first** — it is shorter (396 pp. vs 587 pp.), overlaps less with already-shipped material (vs. Pars II's heavy Symbolorum 1577 overlap), and establishes the volume conventions.
6. Create `review/paedagogia-pars-i-1577.md` and begin **Pars I T1**.

## OCR strategy — same as Institutio Pars III

**No Google-Books text-layer OCR available.** The assembled PDFs are image-only. **Use Claude vision page-by-page** — this is the project's documented best practice anyway for 16th-c. Antiqua Latin.

Workflow for each tranche:
1. Pick the JPG range for the tranche (e.g. Pars I T2 = JPGs p00060–p00100 for Commandments I–II).
2. For each page, open the JPG via the `Read` tool (as an image).
3. Transcribe the Latin verbatim into a scratch buffer.
4. Translate paragraph-by-paragraph into the body MD.

If a page is damaged, blurry, or ambiguous, flag it inline (`[OCR unclear p027: ...]`) rather than guessing.

## Tranche plan (preliminary — detail in `notes.md`)

### Pars I (Decalogue, 432 JPGs)

| T | Content | Approx JPG range (verify after survey) |
|---|---|---|
| **T0** | Source + staging (done — this handoff) | — |
| **T1** | Translator's Note + Biographical Sketch + Title + Dedication + Preface + Prolegomena | 1–60 |
| **T2** | Commandments I–II (first table opener) | ~60–140 |
| **T3** | Commandment III (Sabbath — substantial anti-Sabbatarian + pastoral) | ~140–200 |
| **T4** | Commandment IV (Haustafel material + magistracy) | ~200–270 |
| **T5** | Commandments V–VI | ~270–330 |
| **T6** | Commandments VII–VIII | ~330–370 |
| **T7** | Commandments IX–X + Index rerum + colophon + Pars I PDF build | ~370–432 |

### Pars II (Three Creeds, ~630 JPGs)

| T | Content | Approx JPG range (verify after survey) |
|---|---|---|
| **T1** | Translator's Note (brief, cross-ref Pars I) + Title + Preface + Prolegomena | 1–50 |
| **T2** | Apostolicum — Articles I–IV (Father, Son's generation, Spirit opener) | ~50–200 |
| **T3** | Apostolicum — Articles V–VIII (Suffered, Died, Rose, Ascended) | ~200–330 |
| **T4** | Apostolicum — Articles IX–XII (Judge, Spirit, Church, Last things) | ~330–430 |
| **T5** | Nicaeno-Constantinopolitanum in full | ~430–510 |
| **T6** | Athanasianum (Quicumque) in full | ~510–580 |
| **T7** | Index + colophon + Pars II PDF build | ~580–630 |

Adjust in flight — these ranges are provisional until you have scanned the facsimile.

## Non-negotiable conventions

Carried over from Pars I, Pars II, Symbolorum, Institutio Pars III. Do not silently drop.

1. **Bible-citation policy.** Every scripture quotation in the body is *your own* English rendering of Selnecker's *own* Latin citation. **Do not quote NKJV, NIV, ESV, KJV, or any other modern English Bible version anywhere in the volume** — not even as a footnote. Preserve Selnecker's own numbering.

2. **Catechetical register.** Target reader is a Latin-school student or a teacher. Translate for *accessible plainness* rather than for Loci-style technicality. The *Paedagogia* English should be a step more plain-spoken than the *Institutio* or *Symbolorum* English.

3. **Scripture catena preservation.** The Paedagogia is dense with short-quotation catenae clustered under exegetical points. Preserve the catena structure. Each citation is Selnecker's own Latin; translate verbatim.

4. **Index rerum preservation.** Each Pars ends with *Cum Indice rerum & verborum locupletissimo*. Translate it. Follow the Institutio Pars II index precedent for structure.

5. **Endnote apparatus at volume end, cross-referenced.** Numbered endnotes ¹ ² ³ … using superscript Unicode digits. Collect in a single apparatus at the very end of each volume. Cross-references between endnotes use `[[note-N]]` syntax.

6. **Reader-facing Translator's Note = no internals.** No file paths, no tranche-plan language, no memory-link `[[...]]` syntax, no build detail. The Institutio Pars II Translator's Note is the model.

7. **Structural section-header convention.** In the working MD, use:
   - `#` — volume title
   - `##` — Translator's Note / Biographical Sketch / Table of Contents / major sections (Prolegomena · each Commandment · each Creed · Index · Endnotes)
   - `###` — sub-sections (first table / second table; each Article of the Apostles' Creed)
   - `####` — scholia / questions / catena subdivisions

8. **Endnote debt discipline.** Add the endnote entry in the same commit as the superscript. Do not defer.

9. **Commit as you finish each tranche.** Each `Paedagogia {Pars} T{N}{letter}` gets its own commit. Format:
   `Selnecker Paedagogia {I|II} T{N}{letter}: <sections> (JPGs pNNNN-pNNNN) — <one-line>`

## Build pipeline

`build-shareable.ps1` is pre-populated for Pars I with the shareable-name stem:

    Nikolaus-Selnecker-Christian-Paedagogy-Pars-I-Exposition-of-the-Decalogue-1577-English-Scholastic-Lutherans

Create a parallel `build-shareable-pars-ii.ps1` when Pars II is ready to build — use stem:

    Nikolaus-Selnecker-Christian-Paedagogy-Pars-II-Exposition-of-the-Three-Creeds-1577-English-Scholastic-Lutherans

Run from PowerShell:

    powershell -File "C:\Users\hp\documents\github\scholastic-lutherans\dogmatics\selnecker-paedagogia-christiana-1565\build-shareable.ps1"

Produces `.docx` and `.pdf` in `review/`. Uses:
- Pandoc at `$env:LOCALAPPDATA\Pandoc\pandoc.exe`
- LibreOffice at `C:\Program Files\LibreOffice\program\soffice.exe`
- Reference DOCX at `shared/reference-custom.docx` (shared across all volumes in the repo)

## Bibliographic details for the front matter

Use these verbatim in the title page and colophon blocks:

**Pars I:**
- **Title (as printed):** *D. Nicolai Selnecceri PÆDAGOGIÆ CHRISTIANAE, DENVO ET VLTIMO AVCTAE, ita, vt eius recognitione deinceps non opus sit amplius, profuturæ tàm docentibus, quàm discentibus veritatem doctrinæ cœlestis. PARS PRIMA. Cum Indice rerum & verborum locupletissimo.*
- **Motto (title-page, John 18:23):** *Si malè locutus sum, testificare de malo: sin verò bene, cur me verberas?* (= "If I have spoken evil, bear witness of the evil; but if well, why strike you me?")
- **Printer's device:** Dove with Hebrew Tetragrammaton (יהוה) above.
- **Imprint:** *Cum gratia & priuilegio ad decennium. FRANCOFVRTI AD MOENVM. M.D.LXXVII.* (Frankfurt am Main [Nicolaus Bassaeus], 1577)
- **VD16 identifier:** S 5626
- **Physical description:** 396 printed pages (432 BSB IIIF canvases), octavo, BSB Munich shelfmark Dogm. 926-1. BSB MDZ ID `bsb10175496`. Downloaded 2026-10-23.

**Pars II:**
- **Title (as printed, from p00001.jpg):** *D. Nicolai Selnecceri PÆDAGOGIAE CHRISTIANAE, CONTINENTIS CAPITA ET LOCOS doctrinae Euangelicae, forma & serie catechetica, ad vsum docentium & discentium doctrinam Filij Dei scriptae, & multis in locis auctae. PARS SECVNDA. Cum Indice rerum & verborum locupletissimo.*
- **Printer's device:** Same dove with Hebrew Tetragrammaton (יהוה) above (shared with Pars I).
- **Imprint:** *Cum Gratia & Priuilegio Imperiali & Electoris Saxoniae ad decennium. FRANCOFVRTI AD MOENVM. M.D.LXXVII.* (Note stronger privilege — Imperial *and* Saxon Electoral — than Pars I's simple decennial privilege.)
- **VD16 identifier:** S 5626 (same number as Pars I — the two parts share one VD16).
- **Physical description:** 587 printed pages (630 BSB IIIF canvases), octavo, BSB Munich shelfmark Dogm. 926-2. BSB MDZ ID `bsb10175497`. Downloaded 2026-10-23.

## Suggested T1 opening (Pars I)

Follow Institutio Pars II's opening structure exactly, re-writing every prose paragraph fresh for this volume. The half-title / title-page / colophon `{=openxml}` blocks can be adapted (change the title to *Christian Paedagogy, Part One: Exposition of the Decalogue*, the imprint line to *Frankfurt am Main · Nicolaus Bassaeus · 1577*, and the sub-caption appropriately).

The Translator's Note for Pars I should:
- Situate this as Selnecker's catechetical scaffold for the Latin-school curriculum, complementary to (not duplicating) the university-level *Institutio* already in English;
- Flag the "denuo et ultimo auctae" authorial self-designation of 1577 — this is Selnecker's own definitive text;
- Explain that the Latin Paedagogia is a two-part work (Decalogue + Creeds), not three; the three-part division is a feature of the German translation only;
- Flag the overlap with the already-shipped Institutio Pars I *De Lege* and (eventually) Institutio Pars III Decalogi Explicatio — explain that the three treatments operate at three different pedagogical registers (Loci / schoolbook / paedagogical scaffold) and that reading all three lets the modern reader see Selnecker's catechetical thought move between registers;
- Reiterate the Bible-citation and Latin-original-preservation policies (verbatim from Institutio Pars II — those paragraphs are not volume-specific).

## Suggested T1 opening (Pars II)

Shorter Translator's Note than Pars I — cross-reference the Pars I note for the policy boilerplate. Add:
- Flag of overlap with the already-shipped *Symbolorum Exegesis 1577* (same author + same decade + same Three Creeds + different pedagogical register — Symbolorum is polemical-exegetical for synod; Paedagogia Pars II is catechetical for the schoolroom);
- Positioning as the completion of the Paedagogia set.

## When you are done

Run the parallel-agent audit at the end of each Pars (Pars II T-audit-1 methodology): spawn 3–4 `Explore` subagents in parallel to audit different portions of the facsimile (JPG ranges) against the English translation. Each agent reads a block of JPGs and the corresponding MD section and reports any paragraph-level or Scripture-reference drop. Each prior volume cleared the "no substantive gaps" bar with four agents.

Then commit the final `.pdf`s alongside the working MDs and push to `origin/master`. The user has been running with a solo-master workflow; no PR gate.

## Git / repo etiquette carried from Pars II

- Commit messages format: `Selnecker Paedagogia {I|II} T{N}{letter}: <what-was-done> (JPGs pNNNN-pNNNN, ~<lines>) — <one-line-narrative>` — see Institutio Pars II git log for the pattern.
- Do not push directly to shared remotes without the user's OK. Solo workflow so far, but confirm.
- Never `git add -A` — always add specific files by name.

Good luck. Everything is in place — both PDFs are assembled, the JPGs are staged for vision OCR, the build script is ready for Pars I. All that remains is the translation itself.
