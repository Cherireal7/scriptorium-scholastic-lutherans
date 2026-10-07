# Veltheim, *Institutiones Metaphysicae* (Jena 1680) — HANDOFF

**Status (as of 2026-10-07):** Stage 3 translation in progress, 49 tranches shipped. Resume at **T50**.

## What is being translated

- **Author:** Valentin Veltheim, Logices et Philosophiae Primae Professor Publicus Ordinarius, University of Jena.
- **Full title:** *Institutiones Metaphysicae, Continuis Exemplis Inprimis Theologicis, Iuridicis, Moralibus, Politicis Illustratae* (Jena, 1680; octavo; *Sumtibus Autoris, Typis Wertherianis*).
- **Format of the body:** Caput Praeliminare + 49 numbered Capita (no Libri or Partes); subdivided into numbered §§.
- **No English or German translation known.** This is the first.
- **Source:** Universitätsbibliothek Kiel plaintext via `schriftgut.sh viewer PPN72572448X`. Local file: `sources-original/veltheim-1680.txt` (2.59 MB, 67,379 lines).

## Where things stand

| Metric | Value |
|---|---|
| OCR body lines covered | ~17,100 / ~62,000 = **~27.6%** |
| Tranches shipped | **49** of planned ~80 = **~61%** |
| Chapters closed | **7** of 50 (Praeliminare + Capita I–VI) |
| Current chapter | **Caput VII** opened, through § 3 (first requisite of principle) |
| Translation file | `review/veltheim-institutiones-metaphysicae.md` (~2000+ lines) |
| Working notes | `notes.md` (tranche log + bibliographic record + structural map) |

## Resume point: T50

T49 (just-committed) opened Caput VII with:
- § 1 (Principium = whence something proceeds; shoemaker/shoe + body/soul/man)
- § 2 (Principiatum = what proceeds from elsewhere)
- Four Notes on *principiare/principiari* Scholastic coinages, the axiom ***POSITO PRINCIPIO PONITUR PRINCIPIATUM***
- § 3 opened with the **first requisite of principle = *habitudo* of principle to principiatum = *relatio originis***

**T50 picks up:** second requisite of principle + the full classification of principles (per se / per accidens; interna / externa; etc.) + the doctrine that cause is a species of principle. Latin source at OCR line ~16998 onward (**read from line 16998**).

## Translation stage + conventions

This is **Stage 3** of the standard 5-stage pipeline (source ID → extract → translate → audit → format). Follow:

- **[reference-translation-pipeline](../../../../.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-translation-pipeline.md)** for pipeline overview
- **[reference-scholastic-lutherans-workflow](../../../../.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-scholastic-lutherans-workflow.md)** for Stage 3 mechanics (faithful line-by-line, all Q + all Objs, MD style, OCR handling, git conventions)
- **[feedback-autonomous-tranche-batching](../../../../.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/feedback-autonomous-tranche-batching.md)** — chain 2–4 tranches per response; don't wait for per-tranche "continue"
- **[feedback-token-budget-discipline](../../../../.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/feedback-token-budget-discipline.md)** — one volume-arc per chat, terse commits <150 chars, no gratuitous file reads, /compact when needed, no subagents for solo work

### Tranche format (what makes a T)

Each tranche:
1. **Translates a coherent block** of OCR source (typically 300–600 lines of OCR, one § or one Note cluster)
2. Written as a continuous addition to `review/veltheim-institutiones-metaphysicae.md`
3. Ends with `— ❦ —` flourish + a long `*[T<N> closes: ... T<N+1> picks up ...]*` summary note (italicized, in square brackets)
4. Followed by one `notes.md` entry prepended to **Latest addition** section (keeps most-recent-first)
5. Committed with a single-sentence commit message like: `Veltheim Institutiones Metaphysicae 1680 T50: Caput VII § 3-§ N — second requisite of principle + classification`

### House-style decisions already established

- **English translation with Latin terms kept in italics** for technical vocabulary (*ratio formalis*, *ens*, *subsistentia*, *proprietas essentialis*, etc.)
- **Scripture citations** retained in standard form (**John 20:31**, **Rom. 8:29**, **Ezekiel 18:4**)
- **Juridical citations** retained in standard form (**L. si fundum** 2 C. *de pactis*, **D. 50.17** etc.)
- **Scholastic terminology** retained with Greek originals where Veltheim uses them (***ὑπόστασις***, ***ἀναλογία***, ***ἐντελέχεια***, ***αὐτεξούσιον***, ***ἀπαιδευσία***, ***πρὸς μίαν φύσιν***, ***δευτέρως***)
- **Veltheim's polemical voice preserved** — he writes against named opponents (Zwicker, Becanus, Socinus, Scotus, Vazquez, Thomas Vio Cajetanus, unnamed novatores) and his sarcasm, rhetorical questions, and Horatian/classical quotations should come through
- **Section headings use `####`** for sub-sections within chapters, `###` for chapters, `##` for parts/divisions (Caput)
- **Numbered Notes** inside sections rendered as `**I.**`, `**II.**`, etc.
- **Veltheim's own cross-references** to his *Introduction to Grotius De Jure Belli et Pacis*, *Jus Imperii Quaesitum*, *Formale Virtutis*, *Sceptrum Directivum*, *Jurisprudentia Moralis* — all retained verbatim
- **Three ❦ flourishes between tranches**, not a chapter break

## What is in the translation file today

The already-translated content covers:
- Full **front matter** (title/dedication/preface/auditors)
- **Caput Praeliminare** (50 §§: metaphysics' nature, constitution, use)
- **Caput I** complete with its 4 Axiomata (non-contradiction + excluded middle + non-entis-nulla-praedicata + Veltheim's own *a reali ad ens reale non valet consequentia*), each with Sensus/Confirmatio/Demonstratio/Usus Practicus/Abusus Practicus structure. Major polemical passages: the massive Grotius-controversy defence; the Zwicker *Compelle Intrare* refutation; the Socinian denial of original sin refuted by 1 John 3:4 ἀνομία; the anti-Manichaean two-first-principles passage; Veltheim's polemic against the Weigelian/Pufendorfian *entia moralia* nomenclature.
- **Caput II** *De Existentia et Absentia* — six § with notes; Thomas-vs-Scotus *actus entitativus*; 11 senses of ***nihil*** including Papist Purgatory/Limbus refutation; resurrection of same-numerical-flesh (Tertullian + Augustine).
- **Caput III** *De Essentia Ratione Formali* — conceptus formalis vs objectivus; three requisites of primus conceptus; ratio formalis wider than essentia.
- **Caput IV** *De Notione FORMALITER* — massive chapter covering six significations (per rei existentiam; eminenter/virtualiter; tota ratio formalis with the full predestination/retrovenditio/poena essential-definition examples; essential-difference most-proper vs not-proper; essential property with the vita-aeterna Theological example); the Bellarmine/Becanus salvation-certainty controversy with the full ***revelatio formalis vs virtualis*** apparatus; the Chemnitz 8-conditions-of-sacrament anti-Trent exposition; the Jena Stahl/Sennert-honoring anti-syllogistics-dismissers polemic.
- **Caput V** — five more significations (in-recto vs in-obliquo with *hic homo* Christological predications; *nostro modo concipiendi*; *in actu signato/exercito*; *in sensu composito/diviso*). Note the autobiographical Majestas controversy (Veltheim defending his *Introduction to Grotius DJBP* position against a Jena-disciple-dispute distortion).
- **Caput VI** *De Communibus Ad Unum h.e. Analogis* — three species of commons-to-one; the Scotus/Rada denial-of-middle rebutted; Aristotle's καθ' ἓν φύσιν vs πρὸς μίαν φύσιν distinction; the vast creation/generation example with Musaeus's πρώτως/δευτέρως resolution; the grand *promissionum* three-genera example.

## Structural map (chapter line anchors in OCR)

See `notes.md` for the full table. Key landmarks:

| § | Caput | OCR line | Status |
|---|---|---|---|
| — | Caput Praeliminare | 811 | ✅ closed (T1) |
| I | Caput Primum | 2372 | ✅ closed (T2–T14) |
| II | Caput Secundum | 8558 | ✅ closed (T25–T26) |
| III | Caput Tertium | ~9325 | ✅ closed (T27) |
| IV | Caput Quartum | 9672 | ✅ closed (T28–T38) |
| V | Caput Quintum | 13378 | ✅ closed (T40–T45) |
| VI | Caput Sextum | 14932 | ✅ closed (T46–T48) |
| VII | Caput Septimum | 16862 | 🟡 opened (T49), resume at line ~16998 |
| VIII | Caput Octavum | 17821 | ⏳ pending |
| IX | Caput Nonum | 18930 | ⏳ pending |
| X | Caput Decimum | ~21000 | ⏳ pending |
| XI | Caput Undecimum | 23504 | ⏳ pending |
| ... | (49 Capita total) | ... | ⏳ pending |
| L | — Index Capitum | 62624 | ⏳ pending |
| L | — Index Rerum | 62795 | ⏳ pending |

## Veltheim's recurring themes to track

- **Anti-Socinian / anti-Antitrinitarian polemic** (Zwicker, Enjedinus, Socinus/Socinians)
- **Anti-Scholastic-Thomist / anti-Jesuit polemic** (Thomas de Vio Cajetanus; Becanus; the *analogum analogans/analogata* confusion)
- **Anti-Scotist polemic** (Scotus, Johannes de Rada Aragonius)
- **Anti-Papist polemic** (Bellarmine on Purgatory/Limbus; sacrament-number dispute via Chemnitz; Vazquez)
- **Anti-Nominalist / anti-Novator polemic** (Weigelian/Pufendorfian *entia moralia* nomenclature; the anti-syllogistics mathematical-method dismissers)
- **Pro-Grotius defence**: Veltheim is a consistent Grotius-partisan against an unnamed Celebrated Theologian-adversary; his *Introduction to Grotius De Jure Belli et Pacis* is referenced throughout
- **Jena-honouring**: memory of Stahl and Sennert; defence of the *Salana* (the Jena university)
- **Lutheran-Theologian authorities** cited: Chemnitz (*Examen Concilii Tridentini*), Johann Gerhard (*Loc. Theol.*; *Confessio Catholica*; *Exegesis*), Johann Musaeus, Albert Gravver, Jerome Kromayer, Johann Felwinger, Heinrich Hopfner, Friedemann Bechmann, Melchior Zeidler, Hermann Conring
- **Grotius citations**: *De Jure Belli et Pacis* throughout (Prolegomena; I.1 §§10-11; II.4 §10 on unborn; II.5 §17 on majority rule; II.11 on promises; II.13 on transit; II.14 §2 on Prince's acts; Introductions)
- **Scripture densely cited**: John 20:31 + 5:39 + 3:16 + III.4 + VI.10 + I.3 (ἀνομία, perspicuity); Rom. 5:12 + 6:18-22 + 8:29ff.; Hebr. 2:14 + 3:7-9 + 6:18; 1 Cor. 7:19 + 8:4 + 13:2 + 15:55-57; Acts 5:3-4 + 5:29 + 13:38, 48 + 10:43; Eph. 1:4-5 + 2:3-7; Ezek. 18 + 33:11; Matt. 7:13-14 + 13:12, 15 + 20:16 + 22:14 + 25:21; Isa. 6:10 + 35:10; Luke 2:11, 21; Jer. 31:18; Gal. 4:6; 1 John 2:2 + 3:4

## Open structural decisions

- **Front-matter formatting standard** is already applied per the memory conventions (no running header on cover/title/copyright; English-only H1 with Latin sub-caption; TOC English-only).
- **Grotius references** retained in the Latin style Veltheim uses (`DJBP` or expanded as `De Jure Belli & Pacis`); the volume should probably standardize at Stage 5 formatting.
- **Scholastic Latin terminology** (**ratio formalis / formale consequens / ens potentia / entelecheia / etc.**) retained in italics on first use in each chapter; this policy should hold.

## What to do next (literal step-by-step)

1. **Open** `review/veltheim-institutiones-metaphysicae.md` and scroll to the final `[T49 closes: ... T50 picks up ...]` marker.
2. **Read** `sources-original/veltheim-1680.txt` lines **~16998 onward** (just past where T49 ended at § 3's first-requisite statement).
3. **Translate T50** covering § 3's second-requisite + classification of principles (OCR-source will reveal the structure). Target: 300–600 lines of OCR per tranche. If the content is dense (e.g., Theological controversy), the tranche may be shorter; if purely theoretical (schema + brief Notes), it may be longer.
4. **Append the T50 content** right after the T49 close-marker in `review/veltheim-institutiones-metaphysicae.md`, ending with `— ❦ —` and a `*[T50 closes: ... T51 picks up ...]*` summary.
5. **Prepend a T50 entry** to `notes.md`'s **Latest addition** section (keep terse, under ~400 words).
6. **Commit** with a terse message naming the tranche + chapter + topic.
7. **Chain T51 if context budget allows** (per the autonomous-batching feedback). Give a progress snapshot every few tranches.

## Risk flags

- **Caput VII will likely feed into Caput VIII–X doctrine on causes**, which (given Veltheim's style) will carry forward the predestination + Trinity + original-sin applications already seen. Watch for continuation of the Musaeus / Gerhard / Gravver / Kromayer / Felwinger citation chain.
- **The volume is 50 chapters total**, and progress is proportionate: OCR-line % and tranche-count % should track together. If they diverge (e.g., a chapter runs 3× the average OCR lines without a tranche-count surge), that's a signal to break larger chapters more aggressively or compress worked examples.
- **Veltheim's late chapters** (XX *De Libertatis Definitione* onwards) carry significant Reformed-vs-Lutheran polemic. Expect dense citations and extended expository passages.
