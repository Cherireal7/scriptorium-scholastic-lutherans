# Quenstedt, *Exercitationes de theologia in genere* — Working Notes

Scholastic Lutherans working file. This is the operational scratchpad for the translation; the reader-facing Translator's Note lives at `review/quenstedt-exercitationes.md`.

**Session log:**
- **2026-08-30 · kick-off scaffold** (commit `55e15d6`). Source-registry, TN, terms.yaml seed.
- **2026-08-30 · Tranche 0.5 source-sighting + Tranche 1 Part A** (commit `af9c440`). BSB Munich `bsb11205336` (1691 Wittenberg 2nd ed., Vol. 1) confirmed as workable text-base with per-page hOCR served by MDZ. Sibling manifests `bsb11205337` (Vol. 2) and `bsb11205338` (Vol. 3) also resolve. **Praefatio ad Lectorem** (canvases 15–18) fully translated into English scholarly prose. **Cap. I §§ Ι–ΙΙΙ** (canvases 19–~22, folio pp 1–~4) translated. Thirteen endnotes added. **Discovery — CAPITA I. PARTIS on canvas 18 shows Pars I has *fourteen* chapters, not four:** see "Scope correction" below.
- **2026-08-30 · Tranche 1 Part B + Tranche 2 combined — Cap. I COMPLETE** (commit `ff1a0e0`). All remaining theses IV–XXXIX of Sectio I Didactica translated + full Sectio II Polemica three Quaestiones (An detur / An revelata sit necessaria / An sit habitus θεόσδοτος practicus).
- **2026-08-30 · Endnotes expansion + Cap. II–IV translation** — commits `37190e4` (endnotes 13→55) + `7150e8f` (Cap. II + III + IV Vol.1 + volume PDF build). Details: 42 new endnotes covering the whole scholastic-orthodox-Reformed citation apparatus for Sectio I §§ IV–XXXIX and Sectio II Polemica of Cap. I; full Cap. II *De Religione* (5 Sectio-I theses + 3 Sectio-II Quaestiones); full Cap. III *De Principio Theologiae* (essendi/cognoscendi/externum/internum + polemic against Papists / Enthusiasts / Reformed / Socinians); Cap. IV *De Sacra Scriptura* opening (thesis + author + composition + uniform divinity + Sectio II Q.I–VII).
- **2026-08-30 · Vol.1 source-cutoff verified + Cap. IV Q.VI-VII enriched + Colophon + mid-final build 1.02MB** (commit `86c8ddb`). Q.VI Style + Q.VII Authority enriched. Colophon written.
- **2026-08-30 · CORRECTION — 1691 Wittenberg set is FOUR volumes not three; Vol.4 = Pars IV *De Mediis Salutis*** (this revision). Discovery: `bsb11205339` is Vol. 4 of the 1691 Wittenberg set, containing **704 canvases** — by far the largest of the set — labelled in the BSB IIIF manifest as *"Theologia didactico-polemica ... 4"* with navDate 1691-01-01. Vol. 4 opens with **PARS QVARTA. DE MEDIIS SALUTIS. CAPUT I. DE VERBO DEI, & nominatim DE LEGE. SECTIO I DIDACTICA. Θέσις Ι** and proceeds through the systematic-soteriological doctrine of the Word (49+ theses of Cap. I *De Lege* in the first 15 canvases alone — a massive Law-and-Gospel + Sacraments treatment). Cap. III *De Sacramentis* is at canvas ~80; Cap. IV *De Circumcisione* at canvas ~100; Cap. V *De Baptismo* at canvas ~107 and continuing. This is a **cognate but structurally-distinct treatment** — Vol. 4 treats the Word of God under its *soteriological* aspect (as *medium salutis*), whereas Pars I Cap. IV was treating it under its *encyclopedic* aspect (as *principium theologiae*). The Church-and-Scripture question opened at Vol.1 canvas 107 remains genuinely-not-continued in the 1691 arrangement — that content belongs to the expanded 1685 editio princeps and 1715 Leipzig re-edition. **Source-cutoff note in review/*.md updated** to reflect the correct 4-vol set, Vol.4's soteriological content, and to flag Vol.4 as the natural "Quenstedt Vol. II" sequel-volume for the Scholastic Lutherans program (*De Verbo Dei ut Medio Salutis*, translating Vol. 4 Cap. I + Cap. II, ~50–60 folio pages). **Final rebuild** — third build (exceeds 2-build discipline; Cheri authorised "finish"). No new translation content beyond the source-note enrichment; the volume as an artefact honours the corrected bibliographic identification.

## The source, in one sentence

Johann Andreas Quenstedt's theological-encyclopedic prolegomena — traditionally cited as *Exercitationes de theologia in genere ejusque principio sancta scriptura* — as it stands consolidated in **Pars Prima** of the *Theologia didactico-polemica sive systema theologicum*, Wittenberg: Heirs of Simon Fincelius (Matthaeus Henckel), 1685 (**editio princeps** in 2 vols folio), and reprinted Leipzig: Thomas Fritsch, 1715 (the widely-cited 4th edition; our operational text-base pending sight of the 1685).

## What "Exercitationes de theologia in genere" actually names

An ambiguity to fix at kick-off, before the working translation carries the burden of it:

- The phrase **"Exercitationes de theologia in genere"** is used, in the older bibliographic tradition, to name Quenstedt's academic disputation cycle on the prolegomena of theology, presided at Wittenberg in the 1650s–1670s. Search of the general bibliographic record (VD17, Open Library, Deutsche Digitale Bibliothek) does not surface a discrete Wittenberg imprint of that exact title as a standalone volume in the 1670s — the standard catalogue entries for Quenstedt's shorter Wittenberg works are the *Dialogus de patriis illustrium doctrina et scriptis virorum* (1654), *Sepultura veterum* (1648/1660), *Ethica pastoralis et instructio cathedralis* (1678), *Antiquitates biblicae et ecclesiasticae* (1688 posth.), and the various dissertations *De lectione Scripturae Sacrae laicis concedenda* (1676) / *De peccato post baptismum* / *De redemptione generis humani* (1678).
- The scholarly consensus is that the **prolegomena-material later gathered as Pars Prima of the *Theologia didactico-polemica*** (Wittenberg 1685) *is* the mature form of Quenstedt's theological-encyclopedic exercitationes — the four chapters **De Theologia in genere → De Objecto Theologiae generali, Religione → De Theologiae Principio → De Sacra Scriptura**, running to approximately 348 folio pages in the Leipzig 1715 collation. Twentieth-century English partial translations by Luther Poellot (*The Nature and Character of Theology*, CPH 1986) and the Lutheran Legacy / Emmanuel Press *Fathers of Lutheran Orthodoxy* series draw on this same Pars Prima. The 1986 Poellot volume in particular renders Chapter I *De Theologia in genere* with facing Latin — a modern partial-comparanda for the first quarter of our text.

**Working decision.** We translate **Pars Prima of the *Theologia didactico-polemica*** as the *Exercitationes de theologia in genere*, disclosing the identification in the Translator's Note. If a discrete 1670s Wittenberg *Exercitationes* imprint surfaces in Tranche 0.5 source-sighting (VD17 hard-search, HAB Wolfenbüttel, Wittenberg university-archive catalogues), we re-open the question, sight the imprint, and — if materially different from Pars Prima — cross-check paragraph by paragraph and disclose the divergence in the TN. Until then, Pars Prima of the 1685 editio princeps is the text-base.

## Scope correction — Pars I has 14 chapters, not 4 (discovered 2026-08-30)

The IA Leipzig 1715 collation surfaced at Tranche 0 sighting reported Pars Prima as four chapters (De Theologia in genere / De Objecto / De Principio / De Sacra Scriptura, pp 1–347). But the 1691 Wittenberg BSB imprint — an earlier and structurally-authoritative witness — plainly gives, at the close of the *Praefatio ad Lectorem* (canvas 18), the following **CAPITA I. PARTIS**:

I. De Theologia in genere. · II. De Theologia objecto generali, videl. Religione. · III. De Theologia principio. · IV. De S. Scriptura. · V. De Articulis Fidei. · VI. De DEO, Ejusque naturali notitia. · VII. De Cognitione DEI revelata, & primo de DEI Nominibus. · VIII. De essentia Dei absolutè consideratâ. · IX. De DEO relativè spectato, sive de SS. Trinitate. · X. De Actionibus DEI in genere & in Specie de Creatione. · XI. De Angelis. · XII. De Homine. · XIII. De Providentia. · XIV. De fine Theologiae formali, quae est Fruitio Dei, & Vita aeterna, Deque ejus oppositô, Morte aeterna.

**What this means.** Cheri's coordination-memo characterisation of the *Exercitationes de theologia in genere* as a "shorter theological-encyclopedic tract, ~300 pp" is best read as pointing to **Cap. I alone** (folio pp 1–19 in the 1691, ~19 pp), or at most the classical prolegomena-cluster **Cap. I–IV** on theology, religion, principle, and Scripture — not the whole of Pars I. The IA 1715 collation apparently consolidated the material differently (or the "pp 1–347" range covered all fourteen chapters of Pars I under the header "Pars Prima," not just the four the excerpt showed). At any rate: **the 1691 witness is authoritative on the internal division**, and the *Exercitationes* — for the purposes of this working translation — comprise Cap. I *De Theologia in genere* alone unless Cheri decides otherwise. Chapters V–XIV are their own volumes' worth of Pars I material (loci on faith-articles, on the divine essence, on the Trinity, on creation, angels, man, providence, eschatology) and belong to a subsequent volume, or to the wider Pars-I project if Cheri chooses to expand scope.

**Provisional working decision.** *Exercitationes de theologia in genere* = **Cap. I of Pars I** (folio pp 1–19, canvases 19–37 in `bsb11205336`). The tranche plan is re-cut accordingly (see below). Cheri to confirm scope at review of this session; if expansion to Cap. I–IV or Cap. I–XIV is intended, the plan re-cuts again.

## Full title and paratexts of the 1685 editio princeps (to be transcribed at source sighting)

*Theologia Didactico-Polemica, Sive Systema Theologicum, In Duas Sectiones, Didacticam Et Polemicam, Divisum, In quarum prima: Omnes & singuli fidei Christianae articuli iuxta causarum seriem, perspicuè traduntur ... In secunda sectione: In quavis controversia I. Verus quaestionis status, remotis falsis statibus, ritè formatur; II. Orthodoxa sententia verbis simplicibus proponitur ...*

Author line as printed: **Johanne Andrea Quenstedio, SS. Theol. D. & Prof. Publ. in Academiâ Wittenbergensi.**

Imprint: **Wittebergae, Sumtibus Haeredum Simonis Fincelii. Typis Matthaei Henckelii. Anno M.DC.LXXXV.**

(Above reconstructed from bibliographic descriptions; to be replaced with the sighted title-page text-face at Tranche 0.5.)

## Digital sources — sighted 2026-08-30

### **PRIMARY OPERATIONAL TEXT-BASE (as of Tranche 0.5, 2026-08-30): BSB Munich, Wittenberg 1691 second edition**

- **Base URL scheme:** `https://api.digitale-sammlungen.de/iiif/image/v2/bsb11205336_NNNNN/full/full/0/default.jpg` for images; `https://api.digitale-sammlungen.de/ocr/bsb11205336/NN` for per-canvas hOCR text.
- **Manifest:** `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11205336/manifest`
- **Volume set:** three volumes — `bsb11205336` (Vol. 1), `bsb11205337` (Vol. 2), `bsb11205338` (Vol. 3). Each ~107 canvases at folio-opening resolution.
- **Front matter:** Title page (canvas 1), *Praefatio ad Lectorem* (canvases 15–18), *Capita I. Partis* table (end of canvas 18).
- **Cap. I *De Theologia in genere*:** canvases 19–37 (folio pp 1–19). Sectio I Didactica: canvases 19–30 (folio pp 1–12). Sectio II Polemica: canvases 31–37 (folio pp 13–19).
- **Cap. II opens** at canvas 38 (folio p. 20).
- **OCR quality:** clean Antiqua Latin at ≥95% word accuracy per MDZ hOCR. Two-column layout produces occasional column-interleaving in the extracted text that must be reconstructed at translation-time by paragraph-boundary recognition. Long-*s* (ſ) mostly resolved correctly; Greek preserved in polytonic script with occasional garbling that must be verified against the image. Marginal apparatus (biblical loci, cross-refs to König, Calov, Chemnitz, Gerhard) preserved.
- **Local archive:** `sources-original/bsb-1691/` contains, at Tranche 0.5 close: canvases 15–35 + samples of 36–70 hOCR (~30 files), plus `praefatio-raw.txt` and `cap-01-raw.txt` (concatenated raw OCR text). Gitignored via `**/sources-original/`.
- **Advantages over the IA 1715:** IIIF/hOCR served at page level → no 1.2 GB PDF download needed; earlier edition (closer to the 1685 editio princeps in every substantive way); MDZ metadata resolves reliably; per-canvas access rules out any bulk-transfer bottleneck.

### Fallback text-base: Internet Archive, Leipzig 1715 reprint

- **URL:** `https://archive.org/details/TheologiaDidactico`
- **Edition:** Leipzig 1715, "first print Wittenberg 1685" per IA metadata. Full one-piece PDF (~1.2 GB).
- **Pars Prima structure — sighted from IA:**
  | Chapter | Latin heading | Pages | Approx. pp |
  |:---|:---|:---|---:|
  | Cap. I | De Theologia in genere | 1–27 | 27 |
  | Cap. II | De Objecto Theologiae generali, Religione | 28–45 | 18 |
  | Cap. III | De Theologiae Principio | 46–76 | 31 |
  | Cap. IV | De Sacra Scriptura | 77–347 | 271 |
  | **Total** | **Pars Prima** | **1–347** | **~347** |

  Chapter IV *De Sacra Scriptura* dominates the volume — Quenstedt's doctrine of Scripture is the substance of what the 17th c. would have called his *theologia in genere*. Chapters I–III are the shorter architectural essays; Chapter IV is the theological-encyclopedic pay-off.

- **OCR quality:** IA typically ships hOCR alongside a full PDF for 18th-c. Antiqua Latin; expected accuracy ≥95%. To be verified at Tranche 1 with a paragraph pass.
- **Local archive at kick-off:** none yet. Pull the IA PDF at Tranche 1 kick-off into `sources-original/ia-leipzig-1715/theologia-didactico-polemica.pdf` (gitignored via `**/sources-original/`).

### Cross-check text-base: 1685 Wittenberg editio princeps

- **Status:** not yet localised to a specific digital scan. Standard candidates:
  - **BSB Munich MDZ** (`digitale-sammlungen.de`) — search `Quenstedt Theologia Didactico Polemica Wittenberg 1685`.
  - **HAB Wolfenbüttel** (`diglib.hab.de`) — significant orthodoxy holdings.
  - **SLUB Dresden** (`digital.slub-dresden.de`) — holds the *Theologia didactico-polemica*; a Dresden entry surfaced in initial searches but the workview URL is currently gated behind an Anubis bot-challenge and could not be resolved at kick-off. To retry manually.
  - **VD17** — the definitive registry for 17th-c. German prints; direct catalogue access at kxp.k10plus.de is intermittent from headless fetch and to be retried by browser.
- **Function in this project:** the 1685 is the theologically-strict text-base; the 1715 is our operational OCR/text-base for speed. Where the two diverge on any theologically substantive reading, the 1685 governs and the divergence is disclosed in an endnote.

### Modern partial-comparanda (not text-base)

- **Luther Poellot, *The Nature and Character of Theology: An Introduction to the Thought of J. A. Quenstedt from Theologia Didactico-Polemica*** (Concordia Publishing House, 1986). Facing-Latin English rendering of Cap. I *De Theologia in genere*. Comparanda for the first 27 pages of Pars Prima; use for terminology-sanity checks, cite in endnotes on first divergence per section.
- **Robert D. Preus, *The Theology of Post-Reformation Lutheranism*, Vol I** (CPH 1970). Book-length modern treatment of Quenstedt on theology-in-genere, principium, and Scripture. Reference and endnote source; not a text.
- **Lutheran Legacy / Emmanuel Press, *Fathers of Lutheran Orthodoxy: Theologia Didactico-Polemica, Sive Systema Theologicum, Pars I*** (POD). Latin-only reprint of Pars Prima. Useful as a page-controlled physical typescript when comparing collations; not a text-base.

## OCR expectations

- **Format:** 1715 Leipzig folio, printed in Antiqua Latin with heavy scholastic apparatus (marginalia, cross-references, biblical citations in the margin, numbered thesis-antithesis-refutation blocks).
- **Expected OCR quality on IA hOCR:** high (≥95% for late-17th / early-18th c. Antiqua when scan resolution is good — IA typically re-scans at 300 DPI or better). No Fraktur.
- **Complications:**
  - Printer's abbreviations (`&c.`, `qū` for *quum/quam*, macron for `n`/`m`, `p̄` for *per/prae*).
  - Long-*s* (silently modernised per convention).
  - Sixteenth-/seventeenth-century `v/u` and `i/j` variation (normalised in citation).
  - Greek quotations, especially in the *De Sacra Scriptura* chapter (from LXX, NT MSS, patristic quotation-chains) — Greek OCR is unreliable, verify by eye.
  - Marginal apparatus (biblical loci, cross-refs to Chemnitz / Gerhard / Hollaz-precursors, patristic edition citations) — these must be preserved as *the author's own citations*, not stripped. Where the marginal is a bare biblical locus, absorb into the running English text with parenthetical citation; where it names a source (e.g. "Gerh. loc. I §174" or "Chemn. Ex. Conc. Trid. IV"), preserve verbatim.
- **Practical:** pull IA PDF at Tranche 1 kick-off, extract per-chapter text via `pdftotext` (or lift the hOCR layer directly), cross-check paragraph-by-paragraph against the image before committing English prose, verify Greek and marginalia visually. As with Praetorius Vol III and Flacius, **do not commit body prose the OCR of which has not been eye-verified.**

## Text-base download decision

The full IA PDF is ~1.2 GB. Two options:

- **(A) Full download now, once.** One `wget` of the PDF into `sources-original/ia-leipzig-1715/`. Enables offline OCR immediately for all seven tranches without repeated large fetches. Storage cost material but manageable — repo tracks nothing under `sources-original/` per `.gitignore`.
- **(B) Page-range extraction per tranche.** IA supports per-page image URLs (`https://archive.org/download/TheologiaDidactico/page/nNNN`). Extract only the pages of the current tranche's chapter. Keeps disk lean; more fetch overhead.

**Recommendation:** (A). This is a single work in one PDF — pull once, extract per-tranche, discard the PDF at volume-final. Different from Flacius (where the source is 1,094 discrete JPGs on a fragile facsimile server); here IA is stable and one file is simpler.

## Tranche plan — revised against 1691 sighted structure (14-chapter Pars I; Exercitationes = Cap. I alone)

Total: **3 tranches, ~19 folio pp of source** (Cap. I of the 1691 Wittenberg 2nd ed. only). This scopes the working translation as a genuinely *short* theological-encyclopedic tract, matching Cheri's original memo characterisation. Should Cheri decide to expand scope to Cap. I–IV (the classical prolegomena quartet — theology, religion, principle, Scripture, ~pp 1–76) or to the whole 14-chapter Pars I, the tranche plan re-cuts.

- **Tranche 0 — Kick-off** (2026-08-30, commit `55e15d6`). Notes, TN draft, terms.yaml seed. ✅
- **Tranche 0.5 — Source sighting + text-base swap** (2026-08-30, this session). MDZ Munich `bsb11205336` (1691 Wittenberg Vol. 1) adopted as primary text-base after the IA Leipzig-1715 PDF proved impractical (1.2 GB, no OCR derivatives, network fetch fell to ~30 KB/s). BSB serves per-canvas hOCR reliably; Cap. I boundaries confirmed (canvases 19–37, folio pp 1–19); Cap. II opens at canvas 38. **CAPITA I. PARTIS transcribed → discovered Pars I has 14 chapters not 4** (see "Scope correction" above). ✅
- **Tranche 1 Part A — *Praefatio ad Lectorem* + Cap. I §§ I–III** (2026-08-30, this session). Full Praefatio translated (Quenstedt's honour-roll of predecessors — Luther, Melanchthon, Chemnitz, Hutter, Gerhard, Calov, Brochmand — his motivation, and his 8-step Polemic method); Cap. I Thesis I *definition of theology* + 10 Notae, Thesis II *double homonymy* + 8 Notae on false theologies (Ethnic, Talmudic, Muhammedan, Samaritan, Pseudo-Christian, Heretical, Scholastic, Syncretistic, Sceptic), Thesis III *archetypa / ectypa* + 2 Notae. 13 endnotes seeded. Terms.yaml extended. No build yet (build budget preserved). ✅
- **Tranche 1 Part B — Cap. I §§ IV–XXVIII (Sectio Prima Didactica completion)** (next session). Theses IV–VI (archetypa in the Trinity; archetypa communicated to Christ *θεάνθρωπος*; Christ's *theologia humanae naturae* — connata, infusa, acquisita, δόκησις); VII–VIII (theology of good Angels — concreated, intuitive, experimental); IX (theology of viatorum vs. comprehensorum); X–XI (Paradisiac theology, concreated and revealed); XII–XIII (theology of viatores after the Fall — natural, ἔμφυτος / ἐπίκτητος); XIV (supernatural theology — immediate revelation vs. mediate manifestation); XV onward (didactic-catechetic distinction; theology as *habitus practicus*, thesis XXXII and following, the practical/theoretical debate against the Scotists); through the end of Sectio I. Deliverable: Cap. I Sectio I complete.
- **Tranche 2 — Cap. I Sectio Secunda Polemica** (canvases 31–37, folio pp 13–19). Polemic against the Roman-Catholic doctrine that theology is a *habitus speculativus* subordinate to metaphysics; against the Scotist reduction of theology to a *habitus affectivus*; against the Reformed doctrine that non-regenerate persons cannot properly be called theologians. Deliverable: Cap. I complete. Mid-checkpoint DOCX/PDF build (build #1 of 2).
- **Tranche 3 — Final polish, glossary consolidation, volume-final build** — front matter (title page cross-checked against 1691 canvas 1); Contents finalised; Notes numbered afresh across the volume; Glossary rendered from `shared/terms.yaml`; back matter and colophon per the Chytraeus reference-implementation. Deliverable: volume-final PDF (build #2 of 2).

Build budget: 2 builds total (Tranche 2 mid-checkpoint, Tranche 3 volume-final) per the workflow discipline.

**Note on scope expansion.** If Cheri decides at any tranche-review to widen the *Exercitationes* to include Cap. II *De Religione* and Cap. III *De Principio* (adding pp 20–~50, ~30 more folio pp), that adds two tranches. Including Cap. IV *De Sacra Scriptura* (which in the 1691 is likely to be the volume's dominant chapter, as it is in the 1715) would add another 5–8 tranches — the ~130-page bibliology chapter is the natural fault-line, and if included, the "*Exercitationes*" volume becomes essentially the classical Lutheran-orthodox prolegomena in the manner of Gerhard's *Loci* I.

## Editorial notes specific to this work

- **The Poellot 1986 factor.** A modern English translation of Chapter I already exists (Concordia Publishing House, out of print but findable). Our English rendering must be genuinely fresh — not paraphrased from Poellot — and where our reading of the Latin diverges from his (on technical terms like *theologia archetypa*, *modus adhaesionis*, *principium fidei*, or the practical–theoretical division), the divergence is noted in an endnote with reasoning. Do not silently harmonise to Poellot's choices; do not silently depart from them either.
- **Late-orthodox register.** Quenstedt is the *last* great voice of Lutheran scholasticism. His style is the mature form of the discipline: definition (*definitio*), division (*distinctio*), thesis (*thesis*), objection (*obiectio*), refutation (*confutatio* / *responsio*), corollary (*corollarium*). Preserve the scholastic apparatus visibly in the English — do not smooth into narrative paragraphs. Numbered §§ within each chapter (Quenstedt's own) are preserved as §§; sub-divisions preserved as their marginal letters (a/b/c) where present.
- **The scholastic technical vocabulary.** Quenstedt's Pars Prima is a lexicon of late-orthodox theological-encyclopedic terms — *theologia*, *religio*, *principium essendi / cognoscendi / externum / internum*, *articulus fundamentalis / non-fundamentalis*, *analogia fidei*, *sensus literalis / mysticus*, *auctoritas / perfectio / perspicuitas / efficacia Scripturae*. Every one of these gets a `shared/terms.yaml` entry with a first-use anchor, an English rendering, a note on Quenstedt's specific usage (which may differ from Gerhard's or Hollaz's), and cross-references. This is the encyclopedia work — treat the vocabulary itself as part of the translation.
- **Marginal citations preserved.** Quenstedt's marginals cite Chemnitz, Gerhard, Calov, Hutter, Hunnius, Meisner, Balduin, and the older scholastics; the polemical marginals cite Bellarmine, Becanus, Suárez on the Roman side, and Calvin, Beza, Junius, Amesius, Cocceius on the Reformed side. All preserved as *the author's own citations* in the body, augmented in endnotes with modern edition standards per the [[reference-scholastic-lutherans-glossary]] (BSLK, WA, MSA, PL, PG, and — for the 17th-c. authors — the standard Wittenberg/Leipzig imprint plus PRDL identifier).
- **No sola-scriptura polemic drift.** Cap. IV runs to 271 pages precisely because Scripture is the whole *principium* of theology. The temptation to compress the anti-Roman polemic on tradition or the anti-Reformed polemic on the internal testimony of the Spirit into a paragraph *must be resisted* — Quenstedt argues position by position, and the translation must give each argument at length.
- **Cross-reference with Flacius.** Quenstedt on the authority of Scripture cites Flacius's *Clavis Scripturae Sacrae* (1567) — Flacius the hermeneutician, not the *Catalogus*-Flacius under translation elsewhere in this program. Endnotes flag the cross-reference; the two Flacian works are kept distinct in the terminology entries and in the endnote apparatus.

## Coordination with parallel Scholastic Lutherans chats

- **Chytraeus 1594** — COMPLETE + POLISHED as of 2026-08-30 (per [[scholastic-lutherans-program]] table). Pushed to `Cherireal7/scholastic-lutherans` (private). No further coordination needed; catechetical vocabulary is stable.
- **Flacius *Catalogus Testium* (1556)** — in flight in a separate chat since 2026-08-30 (`caa5c62` on same private repo). Different category (`polemics/`); no file collisions. Vocabulary lives under `shared/terms.yaml` `# ─── POLEMICS — Flacius, Catalogus Testium Veritatis (1556) ───` section, closed by a `# FLACIUS 1556 — KICK-OFF` end-marker.
- **Grosse *Die alten Tröster* (1614)** — parallel Chat B, pastoral category. No file collisions.
- **`shared/terms.yaml`** — shared. This work's entries live in a new dedicated `# ─── ENCYCLOPEDIAS — Quenstedt, Exercitationes de theologia in genere ───` section appended *below* the Flacius end-marker. Tranche-1-and-later entries append below a matching `# QUENSTEDT — KICK-OFF` end-marker so parallel chats' appends do not interleave.
- **`shared/reference-custom.docx`** and **`shared/build.ps1`** — DO NOT modify from this chat. Locked at repo-init state.
- **`shared/editions.md`** — modern-critical-edition registry only. The Poellot 1986 CPH English partial translation is registered here on first use (Tranche 1); PRDL Quenstedt identifiers likewise.

## Immediate next actions (Tranche 0.5 → Tranche 1 session)

1. Retry BSB Munich, SLUB Dresden, and HAB Wolfenbüttel for the **1685 Wittenberg editio princeps**. If a scan is found, note shelfmark + URL scheme in this file and confirm 1715 collation vs. 1685 for Cap. I paragraph by paragraph on a spot-check.
2. Pull the IA Leipzig-1715 PDF (~1.2 GB) into `sources-original/ia-leipzig-1715/theologia-didactico-polemica.pdf`. Verify hOCR is present (`pdftotext -f 1 -l 30 -layout ...`) and OCR accuracy on pp 1–30 is ≥95%.
3. Extract pp 1–27 (Cap. I *De Theologia in genere*). Read paragraph-by-paragraph against the PDF image; correct OCR against the image; commit clean Latin text into `sources-original/latin/cap-01.txt` (gitignored).
4. Locate a copy (physical or PDF) of **Poellot 1986** for Cap. I comparanda. Read Poellot's Introduction to identify his edition-choice (likely Leipzig 1715 or 1702) and his editorial conventions; note any English-term choices worth adopting or worth explicitly declining.
5. Translate front matter (title page + Translator's Note — already scaffolded, verify against sighted paratexts) and Cap. I §§ 1–end. Insert into `# Chapter I. Of Theology in General` in `review/*.md`.
6. Extend `shared/terms.yaml` under the Quenstedt section with the Ch. 1 vocabulary as it accrues (*theologia archetypa / ectypa*, *theologia viatorum / comprehensorum*, *theologia irregenitorum / regenitorum*, *modus subjecti / attributionis / adhaesionis*, *habitus practicus / theoreticus / mixtus*, etc.).
7. Mid-checkpoint DOCX + PDF build (build #1 of 2). Verify page discipline (recto/verso, chapter openings on recto, raw-OOXML page breaks between paratexts / TN / Ch. 1). Commit.

## Related

- [[scholastic-lutherans-program]] · corpus index (this work: Tier 1 encyclopedia, ~300 pp Latin)
- [[scholastic-lutherans-parallel-work-2026-08]] · Grosse concurrent; Flacius in flight
- [[reference-scholastic-lutherans-workflow]] · pipeline, conventions, "never fabricate"
- [[reference-scholastic-lutherans-glossary]] · master glossary conventions
- [[scholastic-lutherans-praetorius]] · reference implementation
- [[chytraeus-catechismus-1594]] · completed reference volume in this program; the Chytraeus TN structure is copied verbatim here
- [[flacius-catalogus-testium-1556]] · in-flight polemical volume; Quenstedt cites the Flacian *Clavis* in Cap. IV — endnote cross-reference
- [[lutheran-hermeneutics-paper]] · student paper on Lutheran hermeneutics; Quenstedt on Scripture is a source there
