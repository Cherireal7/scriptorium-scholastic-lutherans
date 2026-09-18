# Handoff — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

**Read this first.** Self-contained brief for whoever picks up the volume in a fresh chat. Everything to start Stage 2 (OCR extraction) is here or in the paths named here.

## What this project is

Translating **Friedrich Balduin** (1575–1627) · ***Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, de Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae*** (Wittenberg: Paulus Helwigius, 1628) from Latin into modern English.

**Historical significance.** This is the **first single-author Lutheran casuistry** — Balduin (Hutter's successor at Wittenberg, †1627) is the first Protestant to work moral theology in the form of *cases of conscience* in a serious systematic manner. The *Tractatus* was published posthumously the year after his death and was repeatedly reprinted through the 17th century. It fills a genre gap in our library: we have Wittenberg dogmatic (Selnecker, Kirchner), catechetical (Kirchner Enchiridion, Chytraeus), and polemical work, but no pastoral-casuistry.

## Where everything lives

Working directory: `pastoral/balduin-casibus-conscientiae-1628/`

```
balduin-casibus-conscientiae-1628/
├── HANDOFF.md                                 # this file
├── sources-original/
│   └── balduin-casibus-1628.pdf              # Wittenberg 1628, from Internet Archive
├── review/                                    # (empty; create balduin-casibus-conscientiae-1628.md here)
```

## Source

- **Bibliographic authority:** VD17 3:307763U.
- **Digital source:** Internet Archive item `bub_gb_us9YzllXDMsC` (mirrored from a Google-Books scan of a European library copy) → `https://archive.org/details/bub_gb_us9YzllXDMsC`. Direct PDF URL: `https://archive.org/download/bub_gb_us9YzllXDMsC/bub_gb_us9YzllXDMsC.pdf`.
- **Google Books identifier** (alternate route, needs manual download to bypass CAPTCHA): `-X9JAAAAcAAJ`.
- **PRDL author entry:** `http://www.prdl.org/author_view.php?s=250&limit=10&a_id=531` (Balduin has 257 titles / 216 vols catalogued — many other Balduin works available if needed for cross-reference).
- **Title-page text (as printed):** *Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, De Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae, summo studio elaboratus, à Friderico Balduino, S.S. Theolog. Doctore et Professore. Wittenbergae, Sumptibus Pauli Helvvigii Bibliop. Anno M.DC.XXVIII.*

## Author

**Friedrich Balduin** (Balduinus; also Bad., Baldo. — b. **17 November 1575 at Dresden**; d. **1 May 1627 at Wittenberg**). Studied at Wittenberg under **Aegidius Hunnius** and **Polykarp Leyser**; MA 1598, D. theol. 1607. Professor of Theology at Wittenberg from 1604, succeeding **Leonhard Hutter** in the senior chair after Hutter's death in 1616. General-Superintendent of the Saxon Electorate from 1614. One of the *Wittenberg orthodoxy* generation between Chemnitz and Gerhard, most closely associated with **Hunnius, Leyser, Hutter, and the young Johann Gerhard** (whose *Loci* Balduin knew). Known also for a *Commentarius in omnes epistolas Beati Pauli* (14 vols, published 1608–1623) which was one of the standard Wittenberg-Lutheran Pauline commentaries of the 17th century.

## Stage 1: source acquisition — DONE

Source PDF at `sources-original/balduin-casibus-1628.pdf` (90.5 MB / 96 MB). **Note:** Stage 1's initial download aborted at 6.2 MB (missing xref/trailer); Stage 2 completed the download. If ever missing again, resume via:

    curl -L --retry 10 --retry-delay 5 --continue-at - \
      -o sources-original/balduin-casibus-1628.pdf \
      -A "Mozilla/5.0" \
      "https://archive.org/download/bub_gb_us9YzllXDMsC/bub_gb_us9YzllXDMsC.pdf"

## Stage 2: OCR extraction + structural map — DONE

Full details in `notes.md`. Summary:
- Extraction: `sources-original/extract.py` (PyMuPDF; `pdftotext` refused the file). 75,390 OCR lines / 3.32 MB across all 1198 pages.
- Structural map: **fourfold by object of action** (I=conscience, II=God, III=spirits, IV=human affairs — NOT Decalogue-ordered as this HANDOFF originally guessed).
- Body ends naturally with AMEN + doxology on physical p. 1109; 3 back-matter indexes (Scriptura / Patres / Rerum) fill pp. 1110–1189; FINIS on p. 1190; Frankfurt colophon on p. 1191.
- OCR quality: heavier long-s/ligature drift than Selnecker/Kirchner but tractable — see `notes.md §OCR quality`.
- Tranche plan: 25 body tranches + 1 front-matter tranche.
- Bible-citation policy: KJV pass (Kirchner precedent) — see `notes.md §Bible-citation policy`.

## Stage 3: translation — IN PROGRESS

**T1 front matter (physical pp. 1–30) — DONE (T1a scaffold + T1b Dedicatoria + T1c Praefatio + Buchner Epigram).** Half-title, full title, copyright, Translator's Note (4 sections), auto-TOC, no-header front-matter sectPr, recto oddPage sectPr openers before Dedication / Preface / Liber I–IV headings all in place at `review/balduin-casibus-conscientiae-1628.md`.

**Next: T2 — Liber I part 1 (OCR ln 739–3000, physical pp. 31–~62).** Liber I is *De Conscientia et ejus casibus in genere* — Balduin's foundational treatment of the conscience itself before the case-material proper. Cap. I opens with **An sit Conscientia** (Whether conscience exists), proving conscience by (I) Scripture, (II) the lament of the pious, (III) the joys of the pious, (IV) the terrors of the impious after crime, (V) daily experience (Rom. 2:15's *"testimonio reddente illis conscientia ipsorum"*), (VI) pagan witnesses (Cicero *pro Milone*, Isocrates *ad Demonicum*, Seneca *ep.* 97, Ovid *Fasti* — *conscia mens...*). Then De nomine (Latin *conscientia* from *sciendo*, Greek *συνείδησις*, Hebrew *lev* = cor / cordis scientia, Syriac *rea*, three etymological accounts including the syllogism-of-conscience *concludens scientia* pattern). Continues through Cap. II onwards on the nature, seat, division, offices of conscience — the theoretical foundation for Books II–IV's case-material.

**Tranche schedule (from notes.md):**
- T2: Liber I pt 1 — OCR ln 739–3000 (~pp. 31–62)
- T3: Liber I pt 2 — OCR ln 3000–5307 (~pp. 62–98)
- T4–T11: Liber II — 8 tranches × ~3000 lines (pp. 99–471)
- T12–T17: Liber III — 6 tranches × ~3000 lines (pp. 472–740)
- T18–T25: Liber IV — 8 tranches × ~2750 lines (pp. 741–1109)
- Back-matter indexes deferred (regenerable from finished English MD).

Commit format: `Balduin Casibus T{N}{letter}: <content> (OCR ln <start>-<end>) — <narrative>`.

## Stage 4–5: audit, KJV pass, build — TODO

Follow `shared/translation-pipeline.md` and `shared/formatting-standard.md`. Key policies to carry forward from the recently-closed Selnecker Symbolorum volume:

**From [[reference-print-formatting-standard]] + [[feedback-front-matter-formatting]]:**
- English-only H1s + Latin italic sub-caption below (short chapter labels, not full sentences — running head must fit in small-caps at the top of every page).
- Never `# Front Matter` as a heading — use `# Dedication`, `# Preface`, etc.
- Front-matter sectPr (cover / title page / copyright) must OMIT `<w:headerReference>` and `<w:footerReference>`.
- Auto-populated TOC via `TOC \o "1-1" \h \z \u` openxml field.
- Recto (oddPage) chapter openers via `{=openxml}` sectPr injection before each body H1.
- Strip Latin blockquotes from body (Kirchner English-only precedent).
- KJV Scripture pass per `shared/translation-pipeline.md` §4b (Balduin cites Scripture heavily on each case).

**Reference DOCX + build pipeline:** copy from Kirchner Methodica (`catechetical/kirchner-methodica-1595/reference-kirchner-methodica.docx` + `update-fields.py` + build script) as the canonical Cooper/Reedsy-standard implementation. Adjust paths for this volume and set the shareable-name PDF stem to `Friedrich-Balduin-Tractatus-Posthumus-de-Casibus-Conscientiae-1628-English-Scholastic-Lutherans`.

**OCR-specific note for Balduin translator prompt:** long-s/f, u/n, and ct/æ/ff-ligature drift is heavier here than in Selnecker or Kirchner — the translator should read *through* corruption silently rather than flag each occurrence. See `notes.md §OCR quality` for typical patterns.

## Companion volumes / cross-reference

- **No German counterpart** — Balduin's *Casibus* has no *Enchiridion*-style German sibling; this is a stand-alone Latin work.
- **No modern critical edition** — has been repeatedly reprinted 1628–1706 but no scholarly critical edition exists.
- **Existing translations** — none known. This is a fresh English translation.
- **Related Balduin works** (from the PRDL catalogue, if any turn out to be needed): *Commentarius in omnes epistolas Beati Pauli* (1608–1623) — Pauline commentary; *Passio Christi* series — Christological sermons. Both are on PRDL under the same author entry.

## Git etiquette

Follow the pattern used across the repo:
- Commit format: `Balduin Casibus T{N}{letter}: <what-was-done> (OCR ln <start>-<end>) — <one-line-narrative>`
- Never `git add -A`; add specific files by name.
- Solo master workflow (no PR gate); don't push without user OK.

Good luck. The source is downloaded; the Cooper-standard formatting machinery is proven; the volume-arc discipline is one-volume-per-chat.
