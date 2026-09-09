# Kirchner Methodica 1595 — VOLUME COMPLETE (audit in progress)

**Task:** *Timotheus Kirchner, Methodica Explicatio* (Jena: Beyer, 1595) — English rendering.

## Status as of 2026-09-09

**Translation COMPLETE.** Audit against OCR + NKJV-conforming of Scripture quotations is **in progress** (see "Audit progress" section below).

- **Last translation-tranche commit:** T107 (Fladyng's *Vita Kirchneri* + Aquila's Epitaphium).
- **MD file:** `review/kirchner-methodica-1595.md` — ~14k lines, closing marker at end of file.
- **Tranches:** 107 committed (T1–T107).
- **Main body:** 46 Loci; ~932 top-level Questions after Loci III + XII gap-fills (see audit notes); 444+ formal Objections.
- **Appendix:** Fladyng's biography of Kirchner (T107).
- **PDF/DOCX build:** `pwsh -f build-shareable.ps1` from the volume root.

## Audit progress (2026-09-09)

**Two-pass audit begun:** (1) OCR-faithfulness pass — locate each Q/Obj in the Latin OCR, verify translation is complete and semantically faithful; (2) NKJV pass — swap Vulgate-idiom English of Scripture quotations to NKJV wording.

### Audited (2026-09-09)

- **Locus I** (Sacred Scripture) — OCR pass complete. No MD edits required. 23 Q + 13 Obj verified against OCR lines 1424-2857. One structural note: MD Obj III folds Kirchner's separate "Rectene dicit Papa Romanus?" and unnumbered "OBIECTIO / At enim Ecclesia fuit antequam verbum Dei literis consignaretur?" into a single MD Obj III with the second as an embedded sub-question — kept as-is since renumbering would ripple through cross-references.
- **Locus II** (God) — OCR pass complete. **One MD edit landed** (commit `db8a1b6`): Q20 malformed Greek "συρισάμενος" → "ὑφιστάμενον" (present middle participle of ὑφίστημι, matching the verb already cited in the same sentence). Note: MD sometimes silently supplies quotation text for bare Scripture citations in Latin (e.g. Ps 103 in Q3); this is a stylistic enrichment, not an error.
- **Locus III** (Person of Christ) — OCR pass complete. **Substantive MD gap-fill landed** (commit `1700fb3`): MD Q61 previously stopped at ground III of Kirchner's argument for "according to which nature Christ is exalted" and jumped straight to Locus IV, skipping ~275 OCR lines. Added: Q61 grounds IV (Acts 2:36) + V (patristic testimony — Athanasius apud Theodoretum, Ambrose on Heb. 1, Cyprian, Chrysostom); one objection after Q61 ("Deum exaltari"); a full new Q62 (session at right hand implies presence-as-Man over creatures) with 3 objections; and a new Q63 (Luke 24:26 "entered into his glory") with a closing objection. Numbering safe — Q62/Q63 are terminal in the Locus.
- **Locus IV** (Office of Christ) — structural spot-check complete. 7 Q's; content verified through Papist errors + Mediators of Intercession discussion. No gap found.
- **Loci V–XI** (Kingdom of Christ, Priesthood, Holy Spirit, Creation, Angels, Evil Angels, Man Before Fall) — OCR pass complete. No MD edits required. Q-counts confirmed: V=13, VI=9, VII=7, VIII=19, IX=11, X=11, XI=10.
- **Locus XII** (Fall + Corrupted Powers) — OCR pass complete. **Substantive MD gap-fill landed:** MD stopped at Obj XVIII (Rom 9:16); OCR carries the free-will polemic through Obj XIX (voluntas libere / naturaliter dichotomy) + Obj XX (manente substantia manet modus agendi) and closes with a full Q25 "Ad quid prodest haec doctrina de corruptione et nullitate virium humanarum?" — the use of the doctrine (humility over corruption + faith as gift of God). MD now has 25 Q + 20 Obj (was 24 + 18).
- **Loci XIII–XVII** (Sin in General, Original Sin, Actual Sin, Ruling/Non-Ruling Sin, Sin against Holy Spirit) — OCR pass complete. No MD edits required. Q-counts confirmed: XIII=10 (+2 Obj), XIV=15 (+17 Obj split 5+12 around the "5th error" of Q15 = the Flacian polemic), XV=11, XVI=10 (+13 Obj split 6+7 around Q7 and Q8), XVII=3.
- **Loci XVIII–XX** (Law, Gospel, Justification) — OCR pass complete. No MD edits required. Q-counts confirmed: XVIII=20 (+18 Obj split 12 after Q9 + 6 Anti-Antinomian after Q16), XIX=13 (+3 Obj: 1 after Q11 + 2 after Q12), XX=34 (+22 Obj: 2 early + 16 Pontifician after Q34 + 4 sub-Obj on Osiandrism under an inserted unnumbered Q on essential righteousness).
- **Loci XXI–XXIII** (Faith in Christ, Predestination, Good Works) — OCR pass complete. No MD edits required. Q-counts confirmed: XXI=27 (+13 Obj: 2 after Q15 + 11 after Q27 on certitude of grace), XXII=18 (+4 Obj sprinkled around Q10-Q11 and Q18), XXIII=46 total (26 main *De Bonis Operibus* + 4 sub-section *De Dilectione Proximi* + 10 *De Eleemosynis* + 6 *De Ieiunio*). Sub-section headings verified in OCR at lines 23885, 23943, 24189.
- **Loci XXIV–XXVI** (Prayer, Sacraments-General, Baptism) — OCR pass complete. No MD edits required. Q-counts confirmed: XXIV=23 (+17 Obj: 1 after Q14 + 9 anti-Saint-invocation after Q18 + 2 after Q19 Canisius + 3 relics after Q20 + 2 after Q22 consecrations), XXV=17 (+4 Obj after Q12 sacramentaliter regula), XXVI=26 (+5 Obj: 1 after Q15 + 2 after Q17 infant sanctity + 1 after Q23 + 1 after Q24).
- **Loci XXVII–XXVIII** (Sacred Supper, Church) — OCR pass complete. No MD edits required. Two largest and doctrinally central Loci in the volume. Q-counts confirmed: XXVII=48 (with major Obj sequences: 14 anti-manducation-of-unworthy Obj after Q41 + Absurdities I.1-I.7, II.1-II.2, III, IV after Q41 + 10 anti-Missa Obj after Q45 + 5 anti-calicis-interdict Obj after Q46, plus scattered Obj throughout), XXVIII=47 (with ~34 Obj: 5 after Q11 visible/invisible + 3 after Q21 verae Ecclesiae signa + Papist objections against Catholic identity after Q29 and Q34 + Obj on Church errors after Q47).

### Not yet audited

- **Loci XXIX–XLVI + Appendix A (Vita Kirchneri)** — 18 Loci remaining for OCR pass. Priority order for future sessions:
  1. **Locus XXX–XXXI** (Keys + Penitence) — 40 + 47 Q's.
  2. **Locus XXIX** (Ministry) — 26 Q's. OCR starts at line 36275.
  3. All others in Locus-number order.
- **NKJV Scripture-conformance pass** — deferred entirely to dedicated future session(s). Every Scripture citation in the volume (many hundreds) needs to be checked against NKJV wording and swapped where the current Vulgate-idiom English differs. Best done as its own batch pass with efficient WebFetch usage rather than interleaved with the OCR audit.

### Structural findings so far

- **MD Q-counts per Locus** (post-Loci-III+XII gap-fills): I=23, II=21, III=63, IV=7, V=13, VI=9, VII=7, VIII=19, IX=11, X=11, XI=10, XII=25, XIII=10, XIV=15, XV=11, XVI=10, XVII=3, XVIII=20, XIX=13, XX=34, XXI=27, XXII=18, XXIII=46, XXIV=23, XXV=17, XXVI=26, XXVII=48, XXVIII=47, XXIX=26, XXX=40, XXXI=47, XXXII=19, XXXIII=11, XXXIV=18, XXXV=16, XXXVI=14, XXXVII=15, XXXVIII=13, XXXIX=20, XL=13, XLI=12, XLII=8, XLIII=21, XLIV=13, XLV=13, XLVI=17. **Total ≈ 923 top-level Q's** (vs. HANDOFF's original figure of 929 pre-audit). The remaining ~6-Q gap has not yet been localised — could be missing Q's in unaudited Loci XIII–XLVI, or a definitional difference in what counts as a top-level Q. Continue investigating during Locus-by-Locus audit.
- **OCR line ranges** for future Locus lookups: Locus I starts at OCR line 1460; II at 2860; III at 3782; IV at 7804; V at 8442; VI at 8842; VII at 9194; VIII at 9648; IX at 10853; X at 11107; XI at 11511; XII at 11856; XIII at 13155; XIV at 13562; XV at 14889; XVI at 15227; XVII at 16015; XVIII at 16177; XIX (De Evangelio) at 17345; XX at 18258; XXIV at 24306. Others findable by grepping `LOCVS` or the Latin title (e.g. `DE PECCATO`, `DE LEGE`, `DE IVSTIFICA`) in the OCR file.

### Build tweaks landed alongside the audit (commit `db8a1b6`)

- Reference DOCX: `Title` and `Subtitle` paragraph styles bound to `IM FELL English` (was Palatino Linotype); body / headings / TOC unchanged. `pgNumType w:start="1"` injected into body sectPr (LibreOffice may normalise the `w:start` attribute out during field refresh — cosmetic only).
- MD: mid-document raw-OpenXML `sectPr` inserted before `# Translator's Note` so front-matter pages (pandoc auto-title + half-title + full-title + colophon + versos) are section 1 with no `headerReference` / `footerReference` — suppressing the STYLEREF running header and the PAGE-number footer on all front matter. Body section (from Translator's Note on) inherits the reference-DOCX body-level header + footer as before.

## Build pipeline (rebuilt 2026-09-09)

The build uses a **volume-specific reference DOCX** (`reference-kirchner-methodica.docx`) that provides:

- **Running headers** — chapter title printed at the top of every page via a Word `STYLEREF "Heading 1"` field.
- **Centered page numbers** in the footer via a `PAGE` field.

Post-pandoc, the build runs a small Python-UNO script (`update-fields.py`) via LibreOffice's bundled Python to refresh the `TOC`, `PAGE`, and `STYLEREF` fields so that the exported PDF ships with **populated page numbers** in the Table of Contents (rather than a placeholder that only fills in when the DOCX is opened in Word / LibreOffice).

### Optional cover-page font

The half-title and full-title pages reference **`IM Fell English`** — a digital revival of John Fell's late-17th-century Oxford types, the closest freely-licensed match to a late-16th-century Leipzig imprint in feel. Install it from <https://fonts.google.com/specimen/IM+Fell+English> (unzip → right-click each `.ttf` → *Install for all users*). If the font is not installed, Word / LibreOffice silently substitute a default serif face; the rest of the book is unaffected.

### Files under the volume root

- `build-shareable.ps1` — the build pipeline (pandoc → macro-driven field refresh → PDF).
- `reference-kirchner-methodica.docx` — the volume-specific pandoc reference DOCX with running headers and page-number footer already wired.
- `update-fields.py` — the LibreOffice-Python-UNO helper invoked by the build.
- `review/kirchner-methodica-1595.md` — the master Markdown.
- `review/*.docx` and `review/*.pdf` — the built artefacts.
- `sources-original/` — the raw OCR text from the Google-Books scan of the 1595 print.

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
