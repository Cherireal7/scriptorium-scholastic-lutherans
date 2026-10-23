# Selnecker · Institutio Christianae Religionis · Pars Tertia · Working Notes

## Source

**Bibliographic authority:** VD16 **S 5567** — Jena, Jakob Tröster, 1579.

**Full title (as reported by BSB catalog):**
*Institvtionis Christianae Religionis Pars … 3, Continens Doctrinam Catecheticam: Catechismum D. D. Lutheri Græcè & Latinè: Decalogi Explicationem: & Quaestiones Catecheticas, accomodatas ad vsum Scholarum.*

**Working text-base:** BSB Munich digital facsimile — `bsb10175492`.
- Landing page: <https://www.digitale-sammlungen.de/en/view/bsb10175492>
- IIIF manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10175492/manifest`
- Per-canvas image URL pattern: `https://api.digitale-sammlungen.de/iiif/image/v2/bsb10175492_{NNNNN}/full/full/0/default.jpg`
- Manifest canvas count: **346** (verified against last-canvas probe).

**Local source files:** `sources-original/`
- `selnecker-institutio-pars-iii-1579.pdf` (178 MB, 346 pages) — assembled locally from BSB IIIF JPGs at 1600px width via `download-and-assemble.py`.
- `jpg/p00001.jpg` … `jpg/p00346.jpg` — raw IIIF images, retained for Claude-vision OCR per-page.

**OCR note:** The assembled PDF is **image-only — no text layer**. Unlike Pars I and Pars II (which had Google-Books text-layer OCR as a starting draft), the catechetical Pars III has no Google-Books text-layer witness available. The project's documented best practice is Claude-vision OCR on BSB JPGs per-page anyway — cleaner than Tesseract for 16th-c. Antiqua Latin, and essential for this volume because of the heavy Antiqua-Greek interleaving (Luther's Small Catechism printed Græcè & Latinè in parallel). Translator should feed JPGs page-by-page to the Claude vision pipeline as each tranche advances.

## Author

Nikolaus Selnecker (1530–1592) — see Pars I and Pars II notes for full biographical sketch.

## Work: structure and scope

Pars III is the **catechetical capstone** of the Institutio corpus. From the title page, its three major sections are:

1. **Catechismus D. D. Lutheri Græcè & Latinè** — Luther's Small Catechism, printed in parallel Greek-Latin columns. A paradigm Lutheran-humanist product: the Small Catechism rendered into Attic-Hellenistic Greek for the Latin-school curriculum. Selnecker (or Melanchthon-circle) is doing for the Small Catechism what Melanchthon did for the Augustana Græca and for Nazianzen-style Christological language.
2. **Decalogi Explicatio** — Exposition of the Ten Commandments. Overlaps with *Paedagogia Christiana* Pars I (also Decalogue exposition); the overlap is a reason to translate both and let the comparison stand.
3. **Quaestiones Catecheticae accomodatas ad usum Scholarum** — Catechetical question-and-answer apparatus arranged for school use. The medium is the message: this is a schoolbook, not a disputational Loci.

The composite format — bilingual catechism + Decalogue-exposition + schoolroom Q&A — is distinctive. It is a *paedagogical* product in the same genre family as *Paedagogia Christiana*, but it is not the same text. The *Paedagogia* is a two-part Loci-style corpus (Decalogue + Three Creeds); Pars III is a schoolbook with Luther's SC as its spine.

## Why this volume completes the Selnecker programme

The three-part Jena 1579 Institutio is a canonical set:
- **Pars I 1579** (VD16 S 5565) — fundamentals (Verbo Dei → God → Creation → Angels → Man → Sin → Law → Cross → Consolatio). SHIPPED.
- **Pars II 1579** (VD16 S 5566) — ordo salutis + Church + Sacraments + Christian life (Iustificatio → Poenitentia → Libertas → Ecclesia → Sacramenta → Vita). SHIPPED.
- **Pars III 1579** (VD16 S 5567) — catechetical schoolroom distillation (Luther SC Gr+Lat + Decalogue + Quaestiones). **This volume.**

Pair this with the already-shipped standalone *Symbolorum Exegesis 1577* and the (next-to-stage) *Paedagogia Christiana* 1577, and the Scholastic-Lutherans Selnecker programme becomes a comprehensive four-volume corpus covering his mature dogmatic + catechetical + paedagogical output.

## Structural map (preliminary — refine after first full read)

Approximate ranges will be filled in during T1 after translator inspects the facsimile. Expected sections:

| Section | Expected scope | Approx print pp |
|---|---|---|
| Front matter | Title page + Dedication (if any) + preface | 1–12 |
| **Luther Small Catechism Græcè et Latinè** | Decalogue + Creed + Pater Noster + Baptism + Confession + Supper in bilingual parallel | ~40–80 |
| **Decalogi Explicatio** | Expanded Latin exposition of each commandment with Scripture catena | ~80–140 |
| **Quaestiones Catecheticae ad usum Scholarum** | Numbered Q&A for school instruction | ~80–120 |
| Colophon / closing material | | 1–8 |

Total printed-page target ≈ 200–280 (within the 346 canvas budget, which includes blank verso leaves and scanner boilerplate).

## Tranche plan (preliminary)

- **T0** (2026-10-23): Source assembled from BSB IIIF (178 MB PDF + 346 JPGs). HANDOFF.md and notes.md staged. OCR deferred to per-page Claude vision in flight.
- **T1**: Translator's Note + Biographical Sketch (reused from Pars I/II with light update) + Title-page-as-printed + any Dedication + opening of Luther SC bilingual section. First structural survey from the facsimile → update this table.
- **T2–T3**: Luther Small Catechism Græcè & Latinè, full. Preserve the parallel-column format in the English edition — Greek text first, then Latin text, then English rendering below. The Greek is pedagogically load-bearing; do not elide it. This is the section most sensitive to Claude-vision verification (Antiqua Greek types easily confused with Latin by any mechanical OCR).
- **T4–T6**: Decalogi Explicatio — one tranche per block of commandments (I–III / IV–VI / VII–X), split as the material warrants.
- **T7–T8**: Quaestiones Catecheticae — one tranche per thematic block (likely matches the three Creeds and Sacraments).
- **T9**: Colophon + endnote apparatus + constructed TOC + volume-final PDF build.
- **Audit + Build**: Parallel-agent audit (per Pars II / Symbolorum methodology) + build-shareable.ps1.

## Non-negotiable conventions

Carried verbatim from Pars I / Pars II / Symbolorum. Do not silently drop. See `HANDOFF.md` for the full list.

Volume-specific extras:
1. **Bilingual Greek/Latin preservation.** This volume is unique in the Selnecker corpus for printing Luther's SC in Greek *and* Latin side-by-side. The English edition must preserve both originals (Greek first, then Latin, then English) — the parallel is the point of the book.
2. **Antiqua-Greek OCR via Claude vision only.** Do not trust mechanical OCR of any Greek passage in this volume. For every Greek word that appears in the translation, cross-check against the specific JPG page before committing. Use `sources-original/jpg/pNNNNN.jpg` directly.
3. **Pedagogical framing in the Translator's Note.** This is a schoolbook — flag that for the modern reader. The Decalogi Explicatio is not the same as Melanchthon's or Luther's own; it is Selnecker's own catechetical scaffold for Latin-school use, in the same decade as the Formula of Concord (1577) which he co-authored.

## Methodology

Follow the Praetorius-Chytraeus-Kirchner-Große-Selnecker-Pars-I-II-Symbolorum standard workflow ([[reference-scholastic-lutherans-workflow]]):
- Claude vision on BSB JPGs *first* for every page.
- Every paragraph in the English body traces to a specific JPG page.
- Modern-critical citation apparatus in the endnotes only: WA/LW for Luther, CR/MSA for Melanchthon, BSLK/*Kolb-Wengert* for the confessions, PL/PG/CCSL/SC for the Fathers, Formula of Concord cross-references throughout (Selnecker co-authored FC XI).
- Editorial ornament: `— ❦ —` (aldus leaf).
- No `Co-Authored-By: Claude` trailers; byline = "The Scholastic Lutherans translation team".

## Related

- [[selnecker-institutio-editions-and-parts]] — the memory that corrected the earlier "two parts only" mistake and documents the full edition map.
- [[reference-symbolorum-1577-handoff-2026-09-08]] — Vol III Symbolorum, model for front-matter + build pipeline.
- [[reference-scholastic-lutherans-workflow]] — Pandoc + LibreOffice pipeline.
- [[reference-scholastic-lutherans-glossary]] — Lutheran-orthodoxy vocabulary + editorial conventions.
- [[handoff-file-convention]] — this file + HANDOFF.md pattern.
