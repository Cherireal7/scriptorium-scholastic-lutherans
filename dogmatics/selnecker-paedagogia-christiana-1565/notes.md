# Selnecker · Paedagogia Christiana · Working Notes

## Bibliographic note on the folder name

Our folder is named `selnecker-paedagogia-christiana-1565` — honoring the **editio prima** (Peter Brubach, Frankfurt 1565) following the convention of our sibling `selnecker-institutiones-1573` (which honors the Frankfurt 1573 editio prima even though the translation uses the Jena 1579 reissue).

**The translation text-base is NOT the 1565 editio prima.** It is the **mature authorial reissue of 1577** (Nicolaus Bassaeus, Frankfurt am Main) — explicitly titled *Pædagogiæ Christianae, DENVO ET VLTIMO AVCTAE, ita vt eius recognitione deinceps non opus sit amplius* ("newly and finally expanded, such that no further revision will henceforth be needed"). Selnecker himself declares the 1577 reissue to be his definitive word on the Paedagogia — exactly the kind of authorial self-ratification that makes it the right text-base over the 1565 editio prima.

## Source

**Bibliographic authority:** VD16 **S 5626** — Frankfurt am Main, Nicolaus Bassaeus, 1577.

**Full composite title (verbatim from Pars I title page, p00001.jpg):**
*D. Nicolai Selnecceri PÆDAGOGIÆ CHRISTIANAE, DENVO ET VLTIMO AVCTAE, ita, vt eius recognitione deinceps non opus sit amplius, profuturæ tàm docentibus, quàm discentibus veritatem doctrinæ cœlestis. PARS PRIMA. Cum Indice rerum & verborum locupletissimo.* [printer's device: dove with Hebrew Tetragrammaton יהוה] *IOAN. XVIII. Si malè locutus sum, testificare de malo: sin verò bene, cur me verberas? Cum gratia & priuilegio ad decennium. FRANCOFVRTI AD MOENVM. M.D.LXXVII.*

**Full composite title (verbatim from Pars II title page, p00001.jpg):**
*D. Nicolai Selnecceri PÆDAGOGIAE CHRISTIANAE, CONTINENTIS CAPITA ET LOCOS doctrinae Euangelicae, forma & serie catechetica, ad vsum docentium & discentium doctrinam Filij Dei scriptae, & multis in locis auctae. PARS SECVNDA. Cum Indice rerum & verborum locupletissimo.* [same dove + Tetragrammaton device] *Cum Gratia & Priuilegio Imperiali & Electoris Saxoniae ad decennium. FRANCOFVRTI AD MOENVM. M.D.LXXVII.*

Note: Pars II carries a stronger privilege formula (*Imperiali & Electoris Saxoniae* — both Imperial and Saxon Electoral) vs. Pars I's simple *cum gratia & priuilegio ad decennium*. Pars II also drops the John 18:23 motto. Pars II's title-descriptor ("containing the chapters and loci of Evangelical doctrine, in catechetical form and sequence, written for the use of teachers and learners") is a programmatic self-description of the Paedagogia project.

**IMPORTANT bibliographic finding (2026-10-23 research sweep):**
The **Latin Paedagogia Christiana is a TWO-part work only.** VD16 S 5626 is a single VD16 number covering both volumes of the 1577 Bassaeus reissue:

- **Pars Prima** — *Explicatio Decalogi* (Exposition of the Ten Commandments). ~396 pp.
- **Pars Secunda** — *Explicatio Trium Symbolorum* (Exposition of the Three Creeds: Apostles' + Nicene + Athanasian). ~587 pp.

**There is no Latin Pars III.** The three-part division ("Prayer + Sacraments" as Pars III) exists only in the **German translation by Lucas Maius** (Jakob Bärwald, Leipzig 1569 and Feyerabend, Frankfurt 1570 — VD16 S 5629 covers the German Pars III). Selnecker did not issue a separate Latin Pars III on prayer and sacraments; the prayer/sacraments material went into *Institutio Christianae Religionis* Pars II (where *De Oratione* appears as an appendix to the Ecclesia locus and *De Sacramentis* + *De Baptismo* + *De Coena Domini* are major loci), and into *Institutio* Pars III (which is the catechetical schoolbook with Luther's Small Catechism + Decalogue + Quaestiones).

So the Scholastic-Lutherans translation of the Latin *Paedagogia Christiana* is a two-volume English edition (Decalogue + Three Creeds). Do not seek a Latin Pars III.

**Working text-base:** BSB Munich digital facsimiles.
- **Pars I:** `bsb10175496` (BSB shelfmark Dogm. 926-1, scanned 2009). IIIF manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10175496/manifest`. Canvas count: **432.** PDF assembled locally: `sources-original/paedagogia-pars-i-1577.pdf` (206 MB, 432 pages).
- **Pars II:** `bsb10175497` (same shelfmark set Dogm. 926-2). IIIF manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10175497/manifest`. Canvas count TBD (download in flight at time of this file's drafting).

**Alternative BSB copies** (same edition, different shelfmark set — use if primary scans have unusable pages):
- Pars I: `bsb10174425` (Catech. 591-1)
- Pars II: `bsb10174426` (Catech. 591-2)

**Google Books witnesses** (BSB-sourced same scans):
- Pars I: `YiE8AAAAcAAJ` (396 pp. in GB count)
- Pars II: `biE8AAAAcAAJ` (587 pp.)

**Rebart Jena 1568 alternative** (prior Latin reissue; VD16 ZV 16908):
- Pars I: `bsb10174477` (Catech. 828 c-1), GB `okA8AAAAcAAJ`
- Pars II: `bsb10174478` (Catech. 828 c-2), GB `tUA8AAAAcAAJ`

**OCR note:** The assembled PDFs are **image-only — no text layer**. No Google-Books text-layer witness has been staged. Use **Claude vision OCR per-page** on the JPGs in `sources-original/jpg-bsb10175496/` and `sources-original/jpg-bsb10175497/`. This matches the project's documented best practice (cleaner than Tesseract for 16th-c. Antiqua Latin).

## Author

Nikolaus Selnecker (1530–1592) — see Pars I / Pars II notes for full biographical sketch. Reuse the sketch verbatim; this is a reissued catechetical-paedagogical work from the same decade (1577 is the year of the Formula of Concord, which Selnecker co-authored).

## Work: structure, scope, and relationship to the Institutio + Symbolorum

The *Paedagogia Christiana* is Selnecker's **catechetical scaffold** for the Lutheran-humanist school curriculum — teaching the Catechism "non obiter aut cursim, sed accuratius" (not casually or in passing, but with greater care). Where the *Institutio* is Loci-style systematic dogmatic for university-level theology students, the *Paedagogia* is for *docentibus & discentibus* — teachers and learners — of the celestial doctrine, with repetitive catechetical structure, worked examples, and a copious index.

**Overlap with already-shipped volumes — translate anyway:**

The user has explicitly directed: "I kinda think we should translate the whole Paedagogy, even if it's overlapping — sometimes it's useful to see development in thought." So:

1. **Paedagogia Pars I (Decalogue)** overlaps with *Institutio Pars I* Locus 7 (*De lege*) and with *Institutio Pars III* Decalogi Explicatio. Each handles the Decalogue at a different pedagogical register — the Institutio Pars I lays out the Law *theologically* (as Second Use + Third Use), the Pars III explicates it *catechetically* (for the schoolroom), and the Paedagogia explicates it *paedagogically* (for teachers and learners, with repetitive scaffolding). Translating all three lets the reader see Selnecker's catechetical thought develop from one register to another.

2. **Paedagogia Pars II (Three Creeds)** overlaps with *Symbolorum Exegesis 1577* (already shipped). This is the richer overlap — same author, same creeds, same decade. The Symbolorum is a mature polemical creed-exposition with the Communicatio Idiomatum doctrine and the Heidelberg 1560 Disputation appendix; the Paedagogia Pars II is the pedagogical-catechetical creed-exposition for school use. Compare them side-by-side as mature-period Selnecker thinking from two different genres on the same material.

## Structural map (preliminary — refine after first full read)

Approximate ranges will be filled in during T1 after translator inspects the facsimile.

### Pars I — Explicatio Decalogi

| Section | Expected scope | Approx print pp |
|---|---|---|
| Front matter | Title page + Dedication + Preface + poem to Christ | 1–20 |
| General Prolegomena | Scope + method + Decalogue as universal moral law | ~20–60 |
| **Commandment I** | *Non habebis deos alienos* — doctrine of God + first table | ~60–100 |
| **Commandment II** | *Non assumes nomen Dei tui in vanum* | ~100–140 |
| **Commandment III** | *Memento sanctificare diem Sabbathi* | ~140–180 |
| **Commandment IV** | *Honora patrem et matrem* — household + magistracy | ~180–230 |
| **Commandment V** | *Non occides* | ~230–260 |
| **Commandment VI** | *Non moechaberis* | ~260–290 |
| **Commandment VII** | *Non furtum facies* | ~290–320 |
| **Commandment VIII** | *Non loqueris testimonium falsum* | ~320–340 |
| **Commandments IX + X** | *Non concupisces* | ~340–370 |
| Index rerum + Finis | | ~370–396 |

Total expected: ~396 printed pages (432 IIIF canvases include blank versos + scanner boilerplate).

### Pars II — Explicatio Trium Symbolorum

Structural survey to be done in flight; expected ranges:

| Section | Expected scope | Approx print pp |
|---|---|---|
| Front matter | Title page + preface | 1–20 |
| General Prolegomena on the creeds | | ~20–60 |
| **Apostolicum Symbolum** (12 articles) | | ~60–230 |
| **Nicaeno-Constantinopolitanum** | | ~230–380 |
| **Athanasianum (Quicumque)** | | ~380–530 |
| Index + Finis | | ~530–587 |

Total expected: ~587 printed pages.

## Tranche plan (preliminary)

### Pars I

- **T1**: Translator's Note + Biographical Sketch + Title page + Dedication + Preface + Prolegomena.
- **T2**: Commandments I–II (first table).
- **T3**: Commandment III (Sabbath — pastoral + anti-Sabbatarian substance).
- **T4**: Commandment IV (second table opener — household + magistracy; heavy *Haustafel* material).
- **T5**: Commandments V–VI.
- **T6**: Commandments VII–VIII.
- **T7**: Commandments IX–X + Index rerum + colophon + volume PDF build.

### Pars II

- **T1**: Translator's Note (brief, cross-referencing the Pars I volume) + Title page + Preface + Prolegomena.
- **T2**: Apostolicum — Articles I–IV (Father / Son's generation / Spirit opener).
- **T3**: Apostolicum — Articles V–VIII (Suffered / died / rose / ascended).
- **T4**: Apostolicum — Articles IX–XII (Judge / Spirit / Church / Last things).
- **T5**: Nicaeno-Constantinopolitanum — in full (shorter than Apostolicum because theses mostly cross-referenced).
- **T6**: Athanasianum (Quicumque) in full — the Trinity + Christology blocks are substantial.
- **T7**: Index + colophon + volume PDF build.

Each volume gets its own tranche-N sequence; commit messages distinguish `Paedagogia I T1`, `Paedagogia II T1`, etc.

## Volume architecture decision

Two options for shipping:

A. **Two separate PDFs** — one Pars I, one Pars II. Mirrors the Jena 1579 Institutio Pars I + Pars II format (two separate review PDFs). Keeps each book shippable on its own.

B. **One combined PDF** — Pars I + Pars II under a single master-TOC "Paedagogia Christiana" cover. Matches the author's intent (two parts of one work).

**Recommendation: A** (two separate PDFs). It matches our existing Institutio Pars I + II handling, keeps the file sizes manageable, and lets each part be read independently. The build-shareable.ps1 is pre-populated for Pars I; Pars II gets a parallel script (`build-shareable-pars-ii.ps1`) when it's ready to build.

## Non-negotiable conventions

Carried over from Pars I / Pars II / Symbolorum / Institutio Pars III. Do not silently drop. See `HANDOFF.md` for the full list.

Volume-specific extras:
1. **Catechetical register.** Target reader is a Latin-school student or a teacher — not a university theologian. Translate for *accessible plainness* rather than for Loci-style technicality. Where the *Institutio* and *Symbolorum* English translations use high register, the *Paedagogia* English should be a step more plain-spoken.
2. **Scripture catena preservation.** The Paedagogia is dense with Scripture catenae — short OT and NT quotations clustered under each exegetical point. Preserve the catena structure (do not consolidate; do not drop). Each citation is Selnecker's own Latin rendering; translate from the Latin verbatim.
3. **Index rerum.** Both Pars I and Pars II end with a *Cum Indice rerum & verborum locupletissimo* ("with a very ample index of things and words"). This is a load-bearing paratext for a schoolbook — translate it, don't drop it. Follow the Pars II (Institutio) index precedent for structure.

## Methodology

Follow the Praetorius-Chytraeus-Kirchner-Große-Selnecker standard workflow ([[reference-scholastic-lutherans-workflow]]):
- Claude vision on BSB JPGs *first* for every page.
- Every paragraph in the English body traces to a specific JPG page.
- Modern-critical citation apparatus in the endnotes only.
- Editorial ornament: `— ❦ —` (aldus leaf).
- No `Co-Authored-By: Claude` trailers.

## Related

- [[selnecker-institutio-editions-and-parts]] — the full Selnecker edition map (corrected 2026-10-23).
- [[reference-symbolorum-1577-handoff-2026-09-08]] — Symbolorum Exegesis 1577, the dogmatic companion to Paedagogia Pars II.
- [[reference-scholastic-lutherans-workflow]] — Pandoc + LibreOffice pipeline.
- [[reference-scholastic-lutherans-glossary]] — Lutheran-orthodoxy vocabulary + editorial conventions.
- [[handoff-file-convention]] — this file + HANDOFF.md pattern.
