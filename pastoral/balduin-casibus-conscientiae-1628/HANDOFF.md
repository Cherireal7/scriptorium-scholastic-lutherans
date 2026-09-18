# Handoff — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

**Read this first.** Self-contained brief for whoever picks up the volume in a fresh chat. **Stages 1+2 and Stage 3 T1 + T2 are done — the next tranche is T3 (Liber I conclusion).** Everything needed to pick up at T3 is here or in the paths named here.

## What this project is

Translating **Friedrich Balduin** (1575–1627) · ***Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, de Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae*** (Wittenberg: Paulus Helwigius, 1628) from Latin into modern English.

**Historical significance.** This is the **first single-author Lutheran casuistry** — Balduin (Hutter's successor at Wittenberg, †1627) is the first Protestant to work moral theology in the form of *cases of conscience* in a serious systematic manner. The *Tractatus* was published posthumously the year after his death and was repeatedly reprinted through the 17th century. It fills a genre gap in our library: we have Wittenberg dogmatic (Selnecker, Kirchner), catechetical (Kirchner Enchiridion, Chytraeus), and polemical work, but no pastoral-casuistry.

## Where everything lives

Working directory: `pastoral/balduin-casibus-conscientiae-1628/`

```
balduin-casibus-conscientiae-1628/
├── HANDOFF.md                                 # this file
├── notes.md                                   # Stage 2 structural map + 26-tranche plan
├── build-shareable.ps1                        # Kirchner-standard build pipeline (adapted)
├── update-fields.py                           # LibreOffice UNO field-refresh (verbatim from Kirchner)
├── reference-balduin-casibus.docx             # reference DOCX (Cooper/Reedsy running-header + PAGE footer)
├── sources-original/
│   ├── balduin-casibus-1628.pdf              # Wittenberg 1628, IA (full 90.5 MB)
│   ├── balduin-casibus-1628.txt              # PyMuPDF extract (75,390 lines / 3.3 MB)
│   └── extract.py                             # extraction script (use this, not pdftotext)
└── review/
    └── balduin-casibus-conscientiae-1628.md  # T1 front matter DONE; T2+ H1 placeholders
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

**T2 Liber I Cap. I–XI (physical pp. 31–53, OCR ln 739–2296) — DONE (2026-09-18).** Foundational eleven chapters treating conscience *in genere* before the case-material proper: Cap. I *An sit Conscientia* (six proofs — impious themselves as unwilling witnesses, prayers of the pious per Ps 51 / Sir 23:2, joys of the pious under Bernard's *De interiori domo* encomium, terrors of the impious, daily experience per Rom 2:15, pagan witnesses Cicero / Isocrates / Seneca / Ovid); Cap. II *De Nomine* (Latin *conscientia < sciendo*, Hebrew *lev* per Hugh of St Victor + Bernard, Syriac *rea*); Cap. III *De Etymo* (three accounts — *cordis scientia* / *concludens scientia* with the Gen 9:6 syllogism / *scientia cum aliis* with the five-witnesses catalogue); Cap. IV *De Essentia et Natura* (voluntas-vs-intellectus debate, Bonaventure/Scotus/Durandus rejected in favour of Thomas, six-fold conscience-synderesis distinction); Cap. V *De Officio* (four offices — obligare, iudicare, dirigere, testificari — with the herald-of-the-law framing); Cap. VI *De Speciebus* + *Recta conscientia* (Word of God foundation + lex naturae + Bellarmine-contested Papist ecclesiastical-law extension); Cap. VII *Erronea* (twenty-page scholastic-dispute treatment — Thomas / Azor / Lorich / Becanus, Rom 14 doubtful-conscience principle, Anabaptist oath test-case, ignorance invincibilis vs vincibilis with alms-from-stolen-money exemplum, Bonaventure perplexed-conscience remedy, Biel/Altenstaig contra-lege absurdum, baptismal-re-administration case); Cap. VIII *Dubia* (practical vs speculative doubt, ignorantia iuris vs facti, safer-side rule with Prov 21:1 trust); Cap. IX *Opinabili* (eight forum-conscience rules — Paphnutius-vs-Nicaea Scripture-primacy, Col 2:16 vs custom-fasting, penal-mitigation, tie-breaking, Calvinist baptismal-liquid test-case, Exod 23:2); Cap. X *Scrupulosa* (seven causes + six remedies, Augustine *Confess.* IX c. 13, Luke 10:16 pastor-as-God's-voice); Cap. XI *Bona et Mala* (four offices each with the metonymy warning, Scripture vocables *kathara/kalē/aproskopon/eusyneidēsia*, Furies etymology Tisiphone/Alecto/Megaera via Tibullus / Apollonius / Silius *Punica* xiii, six species of evil conscience — cauterized, insensate, perverse, dangerous, too-narrow, perplexed — with the anti-monastic Vos-monachi distich preserved). Stops at OCR ln 2296 partway through the perplexed-species entry, matching the physical p. 53 break.

**Next: T3 — Liber I conclusion (~OCR ln 3000–5307, physical pp. 62–98).** Balduin continues with the general-conscience material through Cap. XII+ and into the transition to Liber II. Cap. XI's perplexed-species entry needs to be completed and the remaining evil-conscience closure rendered.

**⚠ OCR ANOMALY — physical pp. 54–63 (OCR ln 2298–~3000).** The PyMuPDF extraction has these ten pages containing content that duplicates (with variation) pages 42–53 rather than the novel pp. 54–63 body-text. Before starting T3 translation, verify against the source PDF whether pp. 54–63 contain novel Liber I content or are already covered by pp. 42–53 in the print. Two paths: (a) re-run `sources-original/extract.py` targeting pages 54–63 alone to diagnose; (b) view those pages directly in the PDF via `sources-original/balduin-casibus-1628.pdf` and translate any missing narrative before continuing T3 from OCR ln 3000+.

**Tranche schedule (from notes.md, revised):**
- ~~T2: Liber I pt 1 — OCR ln 739–3000 (~pp. 31–62)~~ ✓ DONE covering ln 739–2296 / pp. 31–53
- T3: Liber I conclusion — Cap. XI perplexed-species tail through end of Liber I, ~OCR ln 3000–5307 (physical pp. 62–98), plus pp. 54–63 OCR-gap resolution
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
