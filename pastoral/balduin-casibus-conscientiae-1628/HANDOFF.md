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

Source PDF downloaded to `sources-original/balduin-casibus-1628.pdf`. If the download aborted mid-way, retry via:

    curl -L --retry 10 --retry-delay 5 --continue-at - \
      -o sources-original/balduin-casibus-1628.pdf \
      -A "Mozilla/5.0" \
      "https://archive.org/download/bub_gb_us9YzllXDMsC/bub_gb_us9YzllXDMsC.pdf"

Or download manually via a browser from the archive.org details page and place at that path.

## Stage 2: OCR extraction + structural map — TODO

**Step 1:** Extract text.

    pdftotext -layout sources-original/balduin-casibus-1628.pdf \
      sources-original/balduin-casibus-1628.txt

If text-layer quality is poor (common for 17th-c. Wittenberg prints with heavy long-s + ligatures), fall back to Tesseract with Latin language pack, or use `pdfplumber` as the Selnecker Symbolorum volume did (see `dogmatics/selnecker-symbolorum-1577/sources-original/extract.py` as template).

**Step 2:** Skim the OCR to identify structure:
- Balduin's *Tractatus* is organized into **four books** (Libri), following the Decalogue structure — Book 1 (Duties toward God / Table I), Book 2 (Duties toward superiors, self, neighbour / Table II), Book 3 (specific vocation-cases: magistrate, minister, householder), Book 4 (adiaphora and residual cases). Each book divides into *Capita* (chapters), each chapter into numbered *Casus* (cases of conscience).
- Grep the OCR for `LIBER`, `CAPUT`, `CASUS`, `Quaestio` markers.
- Note the total case-count per Liber for the tranche plan.

**Step 3:** Write `notes.md` with:
- Full title (Latin), printer, year, place.
- Structural breakdown with OCR line ranges per Liber / Caput.
- Tranche plan (Balduin cases are typically shorter than Kirchner Q&A — group ~10–15 cases per tranche).

## Stage 3–5: translation, audit, build — TODO

Follow `shared/translation-pipeline.md` and `shared/formatting-standard.md`. Key policies to carry forward from the recently-closed Selnecker Symbolorum volume:

**From [[reference-print-formatting-standard]] + [[feedback-front-matter-formatting]]:**
- English-only H1s + Latin italic sub-caption below (short chapter labels, not full sentences — running head must fit in small-caps at the top of every page).
- Never `# Front Matter` as a heading — use `# Dedication`, `# Preface`, etc.
- Front-matter sectPr (cover / title page / copyright) must OMIT `<w:headerReference>` and `<w:footerReference>`.
- Auto-populated TOC via `TOC \o "1-1" \h \z \u` openxml field.
- Recto (oddPage) chapter openers via `{=openxml}` sectPr injection before each body H1.
- Strip Latin blockquotes from body (Kirchner English-only precedent).
- KJV Scripture pass per `shared/translation-pipeline.md` §4b (Balduin will cite Scripture heavily on each case).

**Bible-citation policy for this volume:** unclear yet — Balduin's *Casibus* is heavily Scripture-argued for each case-of-conscience. Depending on citation density, either the KJV-pass approach (Kirchner precedent, 577 changes) or the own-rendering approach (Selnecker Symbolorum precedent, patristic-heavy volumes) will fit. Decide after Stage 2 survey.

**Reference DOCX + build pipeline:** copy from Kirchner Methodica (`catechetical/kirchner-methodica-1595/reference-kirchner-methodica.docx` + `update-fields.py`) as the canonical Cooper/Reedsy-standard implementation. Adjust paths for this volume and set the shareable-name PDF stem to something like `Friedrich-Balduin-Tractatus-Posthumus-de-Casibus-Conscientiae-1628-English-Scholastic-Lutherans`.

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
