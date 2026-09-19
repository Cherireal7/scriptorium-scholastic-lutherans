# Notes — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

## Bibliographic

- **Title (as printed):** *Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, De Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae, summo studio elaboratus, à Friderico Balduino, S.S. Theolog. Doctore et Professore.*
- **Imprint (title-page):** *Wittenbergae, Sumptibus Pauli Helvvigii Bibliop. Anno M.DC.XXVIII.* (Wittenberg: Paul Helwig, 1628)
- **Actual printer (colophon, p. 1191):** *Imprimebatur Francofurti ad Moenum* — printed at Frankfurt am Main; Helwig's Wittenberg imprint is the publisher/bookseller line.
- **VD17:** 3:307763U
- **Physical:** 1198-page octavo. Roman-numeral front matter (physical pp. 1–30) + Arabic-numbered body (physical pp. 31–1109; body-page numbering runs 1–957, with irregular gaps caused by unpaginated blanks/plates — see note below) + 3 back-matter indexes (physical pp. 1110–1189) + FINIS + colophon (physical pp. 1190–1191) + trailing blanks.
- **Digital source:** Internet Archive `bub_gb_us9YzllXDMsC` (Google-Books mirror). **Complete PDF is 90.5 MB / 96,443,596 bytes.** Stage 1's initial download had aborted at ~6.2 MB (missing xref table + trailer + all pages after physical p. 931); Stage 2 resume-download recovered the remaining 84 MB and enabled full extraction.
- **Posthumous dedication:** signed at Wittenberg, 1 July 1628, by Balduin's widow/heirs, to Landgrave Georg of Hesse.

**Body-page pagination caveat.** The physical-to-body-page offset varies (30 pages at Liber I start, 146 pages by physical p. 931) because the original print interleaves unnumbered plates/blanks/section-openers. Trust physical pages (OCR PDF page markers) as the primary anchor; body-page numbers below are approximate spot-check values pulled from running headers.

## Structural scheme

Balduin organizes on a **fourfold division by object of human action** (not Decalogue-ordered, as HANDOFF originally guessed):

| Liber | Latin subtitle | English gloss |
|-------|---------------|---------------|
| **I** | De Conscientia, & ejus casibus in genere | On conscience itself and cases in general |
| **II** | De actionibus hominis circa Deum & religionem | Actions toward God and religion |
| **III** | De actionibus hominis circa spiritus coelestes | Actions toward celestial spirits (angels, demons, astrology, magic, divinations) |
| **IV** | De actionibus hominum circa res humanas | Actions toward human affairs (body, soul, fortune, vocation) |

Each Liber opens with a *Continuatio* (transition), then divides into *Capita*, each Caput into numbered *Casus* (each Casus begins with a *Prooemium* and works case-argument style).

## Structural anchors — OCR line ↔ physical page ↔ body page

| Section | OCR line | Physical p. | Body p. |
|---------|---------:|------------:|--------:|
| Cover / half-titles | 1 | 1 | — |
| Dedicatoria (signed Wittenberg 1 Jul 1628, widow/heirs → Landgrave Georg) | 197 | 15 | — |
| Praefatio (Wittenberg Theological Faculty) | 289 | 18 | — |
| **LIBER PRIMUS** — *De Conscientia et ejus casibus in genere* | **739** | **31** | **1** |
| **LIBER SECUNDUS** — *De actionibus hominis circa Deum & religionem* | **5308** | **99** | ~69 |
| **LIBER TERTIUS** — *De actionibus hominis circa spiritus coelestes* | **29354** | **472** | ~442 |
| **LIBER QUARTUS** — *De actionibus hominum circa res humanas* | **47120** | **741** | ~711 |
| Body ends (AMEN, doxology closing Liber IV Cap. XVII) | 69119 | 1109 | ~957 |
| **INDEX I — Dictorum Sacrae Scripturae** (Scripture citations) | 69121 | 1110 | — |
| **INDEX II — Patrum et Autorum** (Fathers & authors cited) | 71444 | ~1146 | — |
| **INDEX III — Rerum et Verborum** (subject index) | 72166 | ~1154 | — |
| **FINIS** | 75365 | 1190 | — |
| Colophon: *Imprimebatur Francofurti ad Moenum* | 75369 | 1191 | — |
| Trailing blank / decorative back leaves | 75373 | 1192–1198 | — |

**Per-Liber sizes (complete):**
- Liber I: 4,569 OCR lines / physical pp. 31–98 (**~68 pp**) — smallest liber
- Liber II: 24,046 OCR lines / physical pp. 99–471 (**~373 pp**) — largest
- Liber III: 17,766 OCR lines / physical pp. 472–740 (**~269 pp**)
- Liber IV: 22,001 OCR lines / physical pp. 741–1109 (**~369 pp**) — comparable to Liber II
- Total body: ~68,382 OCR lines / physical pp. 31–1109 (~1,079 pp)
- Back-matter indexes: ~6,244 OCR lines / physical pp. 1110–1189 (~80 pp)

## Casus / Caput count (raw OCR detection)

Raw grep on cleaned OCR; OCR corruption still swallows some markers. Approximate true counts will be firmed up during Stage 3 tranche processing.

- CAPUT / CAPVT variants: **31 detected** across all 4 Libri (true count likely 45–55)
  - Liber I: 3+ (I, II, III visible in scan; possibly more)
  - Liber II: ~10 (through CAPUT XIV visible)
  - Liber III: ~7 (through CAPUT VII visible)
  - Liber IV: ~17 (through CAPUT XVII visible — last CASUS in the body is XVIII, on lying/mendacium)
- CASUS / Casus variants: **204 detected** total (true count likely 250+)

## Extraction status

**Complete.** PyMuPDF (fitz 1.28.0) successfully extracted all 1198 pages after Stage 2's resume-download recovered the 84 MB tail. Output: `sources-original/balduin-casibus-1628.txt` — 75,390 lines / 3.32 MB. No truncation; body terminates naturally with AMEN + doxology; back-matter indexes intact; FINIS marker present.

## Source-scan duplications (two ranges)

The Google-Books scan of the 1628 physical copy has **two duplicate page ranges** — apparently signatures that were re-set and re-bound, resulting in the scan containing partial earlier printings of Liber I and Liber II openings:

- **Liber I duplicate:** physical pp. 54–64 (OCR ln 2298–~3042) re-print the content of pp. 42–53 (Cap. VII *Erronea* through mid-Cap. XI *Bona et Mala*). Novel content resumes at p. 65 with Cap. XII (chapter header swallowed by OCR); Cap. XIII explicitly marked p. 66.
- **Liber II duplicate:** physical pp. 87–98 (OCR ln 4514–5307) is a **partial** earlier printing of Liber II Cap. I Casus I–VI. It stops at Casus VI, and p. 98 sweeps in the tail of Liber I's Steuber Additamentum Q2 (Susanna/Apostles/Joseph exempla) under a stray "LIB. I. DE CONSCIENT." running header. The authoritative printing begins fresh on p. 99 (OCR ln 5308) with the full Cap. I text and continues past Casus VI into Casus VII (p. 110) and beyond.

Both anomalies confirmed by `page.get_text('text')` returning identical body-text for the paired ranges. **Skip both duplicate ranges when translating; anchor on the authoritative range each time.**

## OCR quality

Heavier corruption than Selnecker Symbolorum or Kirchner Methodica but still tractable. Typical patterns:

- **long-s → f** throughout (as expected for 17th-c. Wittenberg fount): *feperari* for *separari*, *fiudium* for *studium*, *confcientiae* for *conscientiae*
- **u ↔ n** ligature drift: *nianu* / *manu* / *manii* interchangeable
- **ct / æ / ff ligatures** occasionally corrupted to punctuation: *pra:cepta* for *praecepta*
- Line-terminal words often broken with `-` (typesetter's hyphenation, plus OCR-invented breaks)
- Occasional cross-column bleed: running headers intrude mid-body-line (e.g. line 7061 "pioccflionibus intcrcllc, coram a:- CAPUT VL,")
- Marginal citations extract as inline body text, often fragmented: *Rom. 14, 22* → *Rem. 14, 22* / *R^m. 14. tt*

Implication for Stage 3: **base translation prompt should explicitly note that the translator must read *through* long-s and ligature corruption silently, not flag every instance**. Line-by-line prose-flow judgment will be the main task.

## Bible-citation policy (decision)

Balduin cites Scripture on nearly every Casus — clustered marginal citations, chapter:verse style. Two candidates from prior volumes:

- **KJV pass** (Kirchner Methodica precedent — 577 changes / 57 books): well-fit for Scripture-argued casuistry where passages are direct margin-cited references, not embedded in patristic prose.
- **Own English rendering** (Selnecker Symbolorum precedent): preferred when Scripture is entangled inside patristic quotation.

**Decision: KJV pass.** Balduin's citation habit is scholastic-marginal (chapter:verse tags in outer margin), not homiletic-paraphrastic. Once the body is translated with placeholder renderings, the Kirchner-style KJV-pass script will replace them with authoritative English text.

## Back-matter indexes — Stage 5 policy

Do not translate the 3 Latin indexes verbatim. Instead:

- **INDEX I (Scriptural citations)** — regenerable from finished MD by scanning `\((?:Gen|Exod|…)\s+\d+[:.]\d+\)`-style tags. Optional: build automatically at Stage 5 if useful.
- **INDEX II (Patrum et Autorum)** — regenerable via pattern-scan on author names (Augustinus, Chrysostomus, Cyprianus, etc.).
- **INDEX III (Rerum et Verborum)** — the subject index is authoritative reference for what Balduin himself considered topically important; skim during Stage 3 for structural cues, but the generated English edition will not include a translated Latin subject index. If a topical index is wanted for the English edition, generate it fresh in English.

## Reference DOCX + build pipeline

Copy Kirchner Methodica's build machinery (canonical Cooper/Reedsy-standard implementation) as this volume's template:

- `catechetical/kirchner-methodica-1595/reference-kirchner-methodica.docx` → adapt title-page + copyright fields for Balduin
- `catechetical/kirchner-methodica-1595/update-fields.py` → copy verbatim
- `catechetical/kirchner-methodica-1595/build-shareable.ps1` (or equivalent) → copy, adjust output stem

Shareable-name PDF stem: `Friedrich-Balduin-Tractatus-Posthumus-de-Casibus-Conscientiae-1628-English-Scholastic-Lutherans.pdf`

## Tranche plan (Stage 3)

Target ~2,500–3,000 OCR lines per tranche → **~25 body tranches** plus 1 front-matter tranche. Group by CAPUT boundaries where OCR allows, otherwise by fixed line-count. Refine breakpoints at each tranche's start to land on a clean CASUS boundary.

| # | Section | OCR lines | Physical pp. |
|---|---------|-----------|--------------|
| T1 | Front matter (cover, dedicatoria, praefatio) | 1–738 | 1–30 |
| T2 ✓ | Liber I Cap. I–XI | 739–2296 | 31–53 |
| T3 ✓ | Liber I Cap. XII–XVI + Steuber Additamentum (skip pp. 54–64 duplicate) | 3086–4510 | 65–86 |
| T4 ✓ | Liber II Cap. I (skip pp. 87–98 duplicate) | 5308–7060 | 99–125 |
| T5 ✓ | Liber II Cap. II–III (essence + persons + Trinity + Christology + Spirit + attributes) | 7061–8819 | 125–154 |
| T6–T11 | rest of Liber II — 6 chunks × ~3400 lines | 8820–29353 | 155–471 |
| T12–T17 | Liber III (celestial spirits) — 6 chunks × ~3000 lines | 29354–47119 | 472–740 |
| T18–T25 | Liber IV (human affairs) — 8 chunks × ~2750 lines | 47120–69119 | 741–1109 |
| — | Back-matter indexes (deferred — regenerable) | 69121–75365 | 1110–1190 |

## Companion / cross-reference

- No German counterpart (Latin-only academic work).
- No modern critical edition; reprinted through 1706 without scholarly revision.
- No known existing English translation.
- Related Balduin works (PRDL): *Commentarius in omnes epistolas Beati Pauli* (14 vols, 1608–1623) — his major Pauline commentary; possible cross-reference resource if Balduin heavily cites Paul on a case-of-conscience and his own commentary is authoritative.

## Immediate next actions

1. Copy Kirchner Methodica reference DOCX + `update-fields.py` + build script into this volume as templates.
2. Create `review/balduin-casibus-conscientiae-1628.md` skeleton with front-matter YAML and per-Liber H1 headings, ready for T1.
3. Begin Stage 3 at T1 (front matter: cover, dedicatoria, praefatio).
