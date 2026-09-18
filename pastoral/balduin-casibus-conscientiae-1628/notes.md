# Notes — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

## Bibliographic

- **Title (as printed):** *Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, De Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae, summo studio elaboratus, à Friderico Balduino, S.S. Theolog. Doctore et Professore.*
- **Imprint:** *Wittenbergae, Sumptibus Pauli Helvvigii Bibliop. Anno M.DC.XXVIII.* (Wittenberg: Paul Helwig, 1628)
- **VD17:** 3:307763U
- **Physical:** 1198-page octavo; Roman-numeral front matter (pp. i–xxx approx.) + Arabic-numbered body (pp. 1–785+) + back-matter index (missing, see §Extraction status).
- **Digital source:** Internet Archive `bub_gb_us9YzllXDMsC` (Google-Books mirror). Downloaded PDF: 6.20 MB. Title-page and dedicatoria confirm; posthumous edition, dedicated by Balduin's widow/heirs (signed Wittenberg, 1 July 1628) to Landgrave Georg of Hesse.

## Actual structural scheme (correction to HANDOFF)

HANDOFF.md guessed a Decalogue-ordered fourfold division. The 1628 print actually organizes on a different fourfold basis — **by object of the human action**:

| Liber | Latin subtitle | English gloss |
|-------|---------------|---------------|
| **I** | De Conscientia, & ejus casibus in genere | On conscience itself and cases in general |
| **II** | De actionibus hominis circa Deum & religionem | Actions toward God and religion |
| **III** | De actionibus hominis circa spiritus coelestes | Actions toward celestial spirits (angels, demons, astrology, magic, divinations) |
| **IV** | De actionibus hominum circa res humanas | Actions toward human affairs (body, soul, fortune, vocation) |

Each Liber opens with a *Continuatio* (transition), then divides into *Capita*, each Caput into numbered *Casus* (each Casus begins with a *Prooemium* and works case-argument style).

## Structural anchors — OCR line ↔ physical page ↔ body page

Physical pages are the PDF page numbers; body pages are the printed Arabic numerals on each leaf (front matter is Roman-paginated + unpaginated).

| Section | OCR line | Physical p. | Body p. |
|---------|---------:|------------:|--------:|
| Cover / half-titles / dedications | 1 | 1 | — |
| Dedicatoria (signed Wittenberg 1 Jul 1628) | 197 | 15 | — |
| Praefatio (Wittenberg Theological Faculty) | 289 | 18 | — |
| **LIBER PRIMUS — De Conscientia** | **739** | **31** | **1** |
| **LIBER SECUNDUS — De actionibus … circa Deum** | **5308** | **99** | **69** |
| **LIBER TERTIUS — De actionibus … circa spiritus coelestes** | **29354** | **472** | **442** |
| **LIBER QUARTUS — De actionibus … circa res humanas** | **47120** | **741** | **711** |
| Body extraction terminates (mid-quote, Liber IV Cap. VII, *Officium Concionatorum*) | 58425 | 931 | 785 |

**Per-Liber sizes (extracted):**
- Liber I: 4,569 OCR lines / physical pp. 31–98 / body pp. 1–68 (**~68 pp**)
- Liber II: 24,046 OCR lines / physical pp. 99–471 / body pp. 69–441 (**~373 pp** — dominant)
- Liber III: 17,766 OCR lines / physical pp. 472–740 / body pp. 442–710 (**~269 pp**)
- Liber IV: 11,305 OCR lines / physical pp. 741–931+ / body pp. 711–785+ (**~75+ pp extracted; truncated**)

## Extraction status — CAVEAT

Source PDF's xref table + trailer are damaged. `pdftotext -layout` (xpdf 4.00) refused the file entirely; **PyMuPDF (fitz 1.28.0) succeeded on physical pp. 1–931 but returned zero blocks / zero characters for pp. 932–1198** (267 pages, ~22% of the physical volume). The final extracted line ends mid-sentence inside a quotation ("… inquit ") on body p. 785, Liber IV Cap. VII (*Officium Concionatorum*) — clearly not a natural terminus.

Two hypotheses:
1. **Truncated download.** The PDF trailer/xref block is missing; PyMuPDF reconstructs what it can but stops when object streams fail. Consistent with a partial IA download.
2. **Damaged source scan.** Google-Books scan may have been ingested to IA with corrupted object streams for the trailing pages.

**Action required before Stage 3.** Attempt a fresh download from IA (curl -C - resume, or manual browser download). See HANDOFF.md §Stage 1 for the URL. If the redownloaded file still ends at ~physical p. 931, we accept the loss and proceed; the loss is likely: (a) the tail of Liber IV Cap. VII, (b) possibly one or two further Capita of Liber IV, (c) the back-matter *Index Rerum* / *Index Locorum Sacrae Scripturae* (~200-250 pages of indexing was standard for Wittenberg casuistic prints of this size). The indexes are recoverable (they're regenerable from the body); Liber IV's tail is not.

## Casus / Caput count (as detected in OCR)

Very approximate because OCR corruption swallows many CAPUT/CASUS markers. Raw grep counts on the extracted portion:

- CAPUT / CAPVT variants: **~24 detected** (true count likely 40+)
- CASUS / Casus variants: **~166 detected** (true count likely 200+)
- No FINIS or Index marker in extracted portion (both would be in the truncated tail)

Case-count-per-Liber will be firmed up during Stage 3 tranche processing.

## OCR quality

**Substantially worse** than Selnecker Symbolorum or Kirchner Methodica. Typical corruption patterns observed on random-sampled pages:

- **long-s → f** throughout (as expected for 17th-c. Wittenberg fount): *feperari* for *separari*, *fiudium* for *studium*, *confcientiae* for *conscientiae*
- **u ↔ n** ligature drift: *nianu* / *manu* / *manii* interchangeable
- **ct / æ / ff ligatures** corrupted to punctuation: *pra:cepta* for *praecepta*, *poffint* rendered variably
- Line-terminal words often broken with `-` (typesetter's hyphenation preserved, plus OCR-invented breaks)
- Occasional cross-column bleed (running headers merging with body): e.g. line 7061 "pioccflionibus intcrcllc, coram a:- CAPUT VL," (running header intrudes mid-body-line)
- Marginal citations extract as inline body text, sometimes fragmented: *Rom. 14, 22* rendered as *Rem. 14, 22* or *R^m. 14. tt*

Implication for Stage 3: **expect much heavier line-by-line proof-reading during translation than in prior volumes**. The base translation prompt should include an explicit note to read *through* long-s and ligature corruption without flagging every instance.

## Bible-citation policy (decision)

Balduin cites Scripture on nearly every Casus — often with clustered marginal citations. Two candidates from prior volumes:

- **KJV pass** (Kirchner Methodica precedent, 577 changes / 57 books). Well-fit for Scripture-argued dogmatics/casuistry: the passages are direct references, not embedded in patristic prose.
- **Own English rendering** (Selnecker Symbolorum precedent). Preferred when Scripture is entangled inside patristic quotation.

**Decision: KJV pass.** Balduin's citation habit is scholastic-marginal (chapter:verse tags in the outer margin), not homiletic. Once translated, running the Kirchner-style KJV-pass script over the finished MD will produce authoritative English quotes for each margin-cited verse. Precise citations are recoverable via marginal reference reconciliation during audit.

## Reference DOCX + build pipeline

Copy Kirchner Methodica's build machinery as canonical template (per HANDOFF §Stage 3–5):

- `catechetical/kirchner-methodica-1595/reference-kirchner-methodica.docx` → adapt title-page + copyright fields for Balduin
- `catechetical/kirchner-methodica-1595/update-fields.py` → copy verbatim
- `catechetical/kirchner-methodica-1595/build-shareable.ps1` (or equivalent) → copy, adjust output stem

Shareable-name PDF stem: `Friedrich-Balduin-Tractatus-Posthumus-de-Casibus-Conscientiae-1628-English-Scholastic-Lutherans.pdf`

## Tranche plan (Stage 3 draft)

Target ~2,500 OCR lines per tranche → ~24 tranches. Group by CAPUT boundaries where OCR allows, otherwise by fixed line-count. Book II is dominant and will absorb the most tranches.

| # | Section | OCR lines | ~Body pp. |
|---|---------|-----------|-----------|
| T1 | Front matter (cover / dedication / preface) | 1–738 | i–xxx |
| T2 | Liber I (conscience in general) — pt. 1 | 739–2900 | 1–35 |
| T3 | Liber I — pt. 2 (conclusion) | 2900–5307 | 35–68 |
| T4–T11 | Liber II (God & religion) — 8 chunks × ~3000 lines | 5308–29353 | 69–441 |
| T12–T16 | Liber III (celestial spirits) — 5 chunks × ~3550 lines | 29354–47119 | 442–710 |
| T17–T19 | Liber IV (human affairs) — 3 chunks × ~3800 lines | 47120–58425 | 711–785 |
| T20 | Liber IV recovered tail (subject to redownload) | 58426–? | 786–? |

Tranche breakpoints will be refined against detected CAPUT/CASUS markers at each tranche's start (aim for a clean CASUS boundary).

## Companion / cross-reference

- No German counterpart (this is a Latin-only academic work).
- No modern critical edition; reprinted through 1706 without scholarly revision.
- No known existing English translation.
- Related Balduin works (PRDL): *Commentarius in omnes epistolas Beati Pauli* (14 vols, 1608–1623) — his major Pauline commentary; possible cross-reference resource if Balduin cites Paul heavily on a case-of-conscience and his own commentary is definitive.

## Immediate next actions

1. **Attempt PDF redownload** (`curl -L --retry 10 --retry-delay 5 --continue-at - -o sources-original/balduin-casibus-1628.pdf ...`) — recover Liber IV tail + back-matter indexes if the current file is truncated.
2. If redownload succeeds, re-run `sources-original/extract.py` and update the "extraction terminates" anchor + Liber IV size in this file.
3. Copy Kirchner Methodica reference DOCX + update-fields.py + build script into this volume as templates.
4. Create `review/balduin-casibus-conscientiae-1628.md` skeleton with front-matter YAML and empty per-Liber headings, ready for T1.
5. Begin Stage 3 at T1 (front matter — cover, dedication, preface).
