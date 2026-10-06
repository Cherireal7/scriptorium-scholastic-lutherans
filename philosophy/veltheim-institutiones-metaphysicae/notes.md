# Veltheim, *Institutiones Metaphysicae* (Jena 1680) — Working Notes

Scholastic Lutherans working file. Operational scratchpad for the translation; the reader-facing Translator's Note lives at `review/veltheim-institutiones-metaphysicae.md`.

## Bibliographic record

- **Author:** Valentin Veltheim (Valentinus Veltheim), Hallensis Saxo — Lecturer in Logic and First Philosophy (Logices et Philosophiae Primae Professor Publicus Ordinarius) in the University of Jena.
- **Full title:** ***Institutiones Metaphysicae, Continuis Exemplis Inprimis Theologicis, Iuridicis, Moralibus, Politicis Illustratae, ut omnium Facultatum ac disciplinarum Studiosis eorumque usibus apprime serviant*** — *"Institutes of Metaphysics, illustrated with continuous examples drawn chiefly from theology, jurisprudence, morals, and politics, so that they may suitably serve students of all faculties and disciplines and their uses."*
- **Place / year:** Jena, Anno Orbis Redempti MDCLXXX (1680).
- **Printer:** *Sumtibus Autoris, Typis Wertherianis* — at the author's expense, from the press of the Werthers.
- **Format:** Octavo (8°).
- **Collation:** [16] Bl., 1896 S., [60] Bl. — i.e. 16 unnumbered leaves of front matter + 1896 numbered pages of body + 60 unnumbered leaves of indexes/colophon.
- **License:** Public Domain Mark 1.0.
- **Source copy:** Universitätsbibliothek Kiel, shelfmark K 2791-1; K 2791-2.
- **PI resolver:** https://schriftgut.sh/viewer/piresolver?id=PPN72572448X

## Source acquisition — Stage 1

Seth's pointer: `schriftgut.sh viewer PPN72572448X`.

- IIIF manifest: `https://schriftgut.sh/viewer/api/v1/records/PPN72572448X/manifest/` — 2060 canvases, label *Institutiones Metaphysicae*.
- Plaintext endpoint: `https://schriftgut.sh/viewer/api/v1/records/PPN72572448X/plaintext/` — serves the full OCR'd Latin as one UTF-8 stream (2.59 MB, 67,379 lines). This is what we work from.
- ALTO endpoint: `https://schriftgut.sh/viewer/api/v1/records/PPN72572448X/alto/` — per-page positional OCR, available if we need coordinate-level verification during Stage 4 audit.
- PDF endpoint (`/pdf/`) is gated behind the schriftgut.sh Anubis anti-bot proof-of-work and did not resolve from scripted fetch. The plaintext is sufficient to proceed; images can be pulled individually via the IIIF `files/images/<zero-padded>.tif/full/<w>,/0/default.jpg` pattern when needed for audit (e.g. for the printed title-page or any passage where the OCR is unrecoverable).

Local file (git-ignored per repo `.gitignore` `**/sources-original/`):
- `sources-original/veltheim-1680.txt` — bulk OCR, 2.59 MB, 67,379 lines.

**OCR quality notes.** The OCR is mid-grade for a 1680 octavo Fraktur-adjacent Latin. Typical mangling to correct silently:

- Long-*s* → *f*: *subdividenda* → *fubdividenda*, *fuit* → *füit*, *efficacia* → *efficaciae*, etc.
- Digit substitutions in all-caps display lines: `THEOLOGIC1S`, `polit1cis`.
- Dropped / split chapter headers at page breaks: `CAPUT NON UM` for *CAPUT NONUM*; `Caput Decimum Ter'tium`; occasional stray floor-paragraph markers (`JJjJ`, `d<`, `í`, etc.) at line-ends.
- Mangled diacritics in the title page (`VALENTIÑd^d^em/`) — these are strictly cosmetic and the title-page image can be consulted directly.
- Running headers / signatures intermittently flowed into body text at page boundaries.

None of this blocks translation; it needs quiet correction in the T-pass against the sense of the surrounding Latin.

## Structural map — Stage 2

**Top-level structure:** no *Libri* or *Partes*. The body is a single sequence of chapters: one *Caput Praeliminare* on the nature, constitution, and use of metaphysics, followed by 49 numbered *Capita*. An *Index Capitum* and *Index Rerum* follow at the back.

**Front matter (OCR lines ~1–810):** title page; dedication to the Rector Magnificus and Senate of the University of Jena (*Illustris. Academiae Jenensis Rectori Magnifico*); *Prolegomena* / *Praefatio ad Lectorem*; printer's/compositor's errata if any.

### Chapter table (with OCR anchor lines)

| § | Caput | OCR line |
|---|---|---|
| — | **Caput Praeliminare** — *De Metaphysices Natura, Constitutione ac Usu* | 811 |
| I | *Caput Primum* | 2372 |
| II | *Caput Secundum* | 8558 |
| III | *Caput Tertium* | ~9000 (header OCR'd as plain line) |
| IV | *Caput Quartum* | 9672 |
| V | *Caput Quintum* | 13378 |
| VI | *Caput Sextum* | 14932 |
| VII | *Caput Septimum* | ~16500 |
| VIII | *Caput Octavum* | 17821 |
| IX | *Caput Nonum* | 18930 |
| X | *Caput Decimum* | ~21000 |
| XI | *Caput Undecimum* | 23504 |
| XII | *Caput Duodecimum* | 24938 |
| XIII | *Caput Decimum Tertium* | 25964 |
| XIV | *Caput Decimum Quartum* | 26216 |
| XV | *Caput Decimum Quintum* | 29264 |
| XVI | *Caput Decimum Sextum* | 30455 |
| XVII | *Caput Decimum Septimum* | 31484 |
| XVIII | *Caput Decimum Octavum* | 31872 |
| XIX | *Caput Decimum Nonum* | 32556 |
| XX | *Caput Vigesimum* — *De Libertatis Definitione* | 32929 |
| XXI | *Caput Vigesimum Primum* | 33618 |
| XXII | *Caput Vigesimum Secundum* | 34092 |
| XXIII | *Caput Vigesimum Tertium* | ~34700 |
| XXIV | *Caput Vigesimum Quartum* | 35113 |
| XXV | *Caput Vigesimum Quintum* | 36754 |
| XXVI | *Caput Vigesimum Sextum* | ~38000 |
| XXVII | *Caput Vigesimum Septimum* | 39907 |
| XXVIII | *Caput Vigesimum Octavum* | 44693 |
| XXIX | *Caput Vigesimum Nonum* | 48536 |
| XXX | *Caput Trigesimum* | 51342 |
| XXXI | *Caput Trigesimum Primum* | 53018 |
| XXXII | *Caput Trigesimum Secundum* | 53686 |
| XXXIV | *Caput Trigesimum Quartum* | 55775 |
| XXXV | *Caput Trigesimum Quintum* | 55966 |
| XXXVI | *Caput Trigesimum Sextum* | 56421 |
| XXXVII | *Caput Trigesimum Septimum* | 57010 |
| XXXVIII | *Caput Trigesimum Octavum* | 57794 |
| XXXIX | *Caput Trigesimum Nonum* | 58234 |
| XLI | *Caput Quadragesimum Primum* | 58885 |
| XLV | *Caput Quadragesimum Quintum* | 59963 |
| XLIX | *Caput Quadragesimum Nonum* | 60877 |
| — | **Index Capitum** | 62624 |
| — | **Index Rerum** | 62795 |

OCR anchors are approximate: a few chapter headers (3, 7, 10, 23, 26, 33, 40, 42, 43, 44, 46, 47, 48) got absorbed into their running pages and need to be relocated by sense when their tranche comes up. The chapter count is **49 + Praeliminare = 50**, consistent with the TOC at line 62624.

**Paragraph granularity.** Every chapter is subdivided into numbered §§, usually 10–40 per chapter, in the characteristic late-17c scholastic exposition style (definition → corollary → example drawn from theology / jurisprudence / morals / politics, as the title promises). Numbering restarts at §1 at the head of each chapter.

### Tranche plan

Because the work is a 50-chapter, ~2000-page octavo, this is a multi-chat volume. One chapter ≈ one tranche is unworkable — some chapters are 100+ pages. The working plan:

- **T1** — Front matter (dedication, prolegomena/prooemium, errata) + *Caput Praeliminare* in full. One chat.
- **T2 – T?** — one tranche per *Caput* for the shorter chapters (say ≤ 1,500 OCR lines) and one per logical section (half-chapter) for the longer ones. Expect roughly 60–80 tranches to close the body, plus a tranche for each index.

Progress is tracked by prepending **"Latest addition:"** entries to this file in the pattern used by Flacius `notes.md` and Balduin `notes.md`.

## Companion / cross-reference

- Google Books also holds digitisations of the same 1680 Jena edition (ids `fyVfAAAAcAAJ` and `XAYF5BKhy4wC`) — useful for cross-checking the title page or any passage where Kiel's OCR is unrecoverable. No modern critical edition is known.
- Veltheim (1645–1700) was Logices et Metaphysices Professor at Jena from 1679; the *Institutiones Metaphysicae* is his inaugural textbook for the Jena chair and dates one year into his tenure. See *ADB* 39:598.
- No English or German translation is known. This appears to be the first.

## Latest addition

**2026-10-06 — T10 shipped.** The Grotius-citation twist in the Abusus Practicus of Axioma I. The opponent weaponises *De Jure Belli ac Pacis* I.1.10 ("acts concerning which the natural law is conversant are understood to be necessarily either enjoined or forbidden by God") against Grotius himself and the common view. Veltheim's four numbered responses: (1) *Where in Grotius does this blasphemous consequence stand or follow?* — challenge to produce textual evidence; (2) the "subdued God" slur unpacked; (3) the opponent's hypothetical-necessity escape forces him either into agreement with the common view or into self-contradiction (his own three-penny-sophist example of fire-is-hot and adultery-is-base undermines his thesis); (4) the opponent's substituted question (necessity "in order to God" vs. "in order to man" vs. the natural/moral-genus distinction) is itself fine, but his claim that the two genera differ in presupposing only creation vs. creation+law is false — absolutely-necessary agreement with rational nature is prior to and the foundation of law-imposition. T11 picks up the Fifthly ("miserable Sophist") response + *etiamsi daremus non esse Deum* defence of Grotius.

**2026-10-06 — T9 shipped.** Second horn of the moral-law example (**II.**). Morality of per-se-honest/base acts even considered *as actually given* stands antecedent to divine will — because the operative necessity is absolute, and absolute-necessity acts fall under God's *necessary* (not free) will. Covers: (a) opponent's hypothetical-necessity objection (if-he-runs-he-is-moved model); (b) Veltheim's syllogistic reduction; (c) the crucial *necessitas existentiae/exercitii/contradictionis* vs. *necessitas essentiae/speciei/contrarietatis* distinction — opponent's argument hits only the straw-man first kind; (d) the fire-is-hot example (God freely creates fire, but existing fire is hot by absolute necessity of essence; a cold fire would be a different thing of a different essence); (e) parallel application to the moral case. T10 picks up the Grotius-citation twist and the defence of *etiamsi daremus non esse Deum*.

**2026-10-06 — T8 shipped.** Veltheim's constructive possible-nature argument (first horn of moral-law example completed). Covers: (a) the syllogism (whatever God knew before all free decree stands antecedent to His will; but He so knew the possible nature of per-se-honest/base acts; therefore their morality qua possible stands antecedent to His will); (b) the possible nature grounded in God's *scientia simplicis intelligentiae / naturalis*; (c) the opponent's half-concession ("morality objectively in divine intellect from eternity") followed by stupor-simulating denial; (d) Veltheim's exposure of the opponent's conflation of divine knowledge of *possibles* with divine knowledge of *futures* — possibility presupposes God only as being + being-able, futurition additionally as willing-to-produce; (e) the twofold rule of sin (rational nature as rule of moral evil; law of God as rule of ἁμαρτία καὶ ἀνομία). T9 picks up the second horn (**II.** — morality considered as given in act), the hypothetical-necessity objection, and the fire-is-hot example.

**2026-10-06 — T7 shipped.** Stoic-Fate objection and Veltheim's two-sense distinction (Mode 1 impious = God bound by absolute necessity to constitute rational nature; Mode 2 orthodox = God freely chose to constitute, but acts then necessarily agree or disagree with the chosen rational nature); the opponent's re-raising of Stoic-Fate; Veltheim's "not learning but fabricating" retort — *fighting with your own masks and vomiting smoke for fire*; the sarcastic restatement of the opponent's would-be blasphemous chain of consequences, culminating in the mocking substitution ***Fiat, quae per se et sua natura sunt necessaria*** for the orthodox *Fiat voluntas tua*. T8 picks up Veltheim's constructive possible-nature argument (morality grounded in God's *scientia simplicis intelligentiae / naturalis*).

**2026-10-06 — T6 shipped.** Response 3 of the moral-law example in Abusus Practicus of Axioma I. The fourfold way of taking the natural law (abstract from divine/human; common to both; God's; man's); three examples of *lex Deo cum hominibus communis* (self-love of God, promise-keeping, metaphysical impossibility of divinely-moved adultery); the governing principle *truth of judgment depends on truth of object* (so morality is objectively prior to practical judgment); the "Our author forgot we speak of God" objection resolved by the simple-intelligence/vision + natural/free distinction in God's knowledge; the "Scholastic darkness" dismissal reflected back via Justin, Lactantius, Augustine, Cicero, Plato. T7 takes up the Stoic-Fate objection.

**2026-10-06 — T5 shipped.** First worked example of the Abusus Practicus of Axioma I: the opponent attacking the common Grotius/Theologian/Jurist/Philosopher view that human acts can be considered as moral (honest or base) apart from reference to law. Covers (a) the opponent's syllogism (Major: not-indifferent → reference-to-law; Minor: some physical motion apart from law is not indifferent; Conclusion violating non-contradiction); (b) Veltheim's three-fold reply announcement; (c) Response 1 (the common view speaks of acts honest/base to God *and* to man — acts per se agreeing with God cannot "reference the decree of a superior binding a subject"; the formal/material concept distinction preserves divine-human communality); (d) Response 2 (the syllogism is formally vicious; parallel *docilis/indocilis* syllogism exposes the fallacy; different mode of considering does not take away the thing itself). T6 takes up Response 3 — the four modes of taking the natural law + the Stoic-Fate objection.

**2026-10-06 — T4 shipped.** Opening of Abusus Practicus of Axioma I: the broadside against the "modern Fanatici" (Cartesian school of universal doubt). Covers (a) the Cartesian Meditations method of doubting even first principles, including the deceiving-God hypothesis + the "mushrooms sprung from the earth" formulation; (b) the extension of this method to Moral Philosophy and Theology, which Veltheim judges opens gates "to the overthrow of what they call Christianity"; (c) the correction of Mendoza's claim that no one ever denied the axiom (the ancient Sceptics did, and the modern innovators are their ash-born revival). T5 begins the first extended example — the opponent who feigns a self-contradiction in Grotius and the common view that human acts can be considered morally apart from law.

**2026-10-05 — T3 shipped.** Axioma I of Caput I — the principle of non-contradiction — through Sensus, Confirmatio, Demonstratio per Absurdum (Aristotle *Met.* IV.4's three sorts of deniers; Mendoza's "club rather than reason" quip at *Disp. Metaph.* III.21; the three methods of self-refutation), and Usus Practicus (resolving every solid doctrine into non-contradiction; the Rom. 11:6 passage as the Holy Spirit's own axiomatic use). Abusus Practicus will span T4–T? (~3000 OCR lines of Cartesian / "Fanatic" doubt-method polemic).

**2026-10-05 — T2 shipped.** Caput I §§ 1–14 (ens / non ens / ens per accidens definitions and the three classes of entia per accidens; Reale and Positivum as synonyms of being). Caput I's four Axioms will each be their own tranche (T3–T6). Axioma I (*Impossibile est idem simul esse et non esse*) is next.

**2026-10-05 — T1 shipped.** Front matter (title/copyright/Translator's Note), Dedicatory Epistle to the Jena Rector and Senate, Preface to the Reader, List of 97 Auditors, and *Caput Praeliminare* in full (50 §§: nature, constitution, and use of metaphysics; abstractio rationis vs. realis; general + special use in Theology, Jurisprudence, Ethics, Politics; the Reeb-vs-Ames defence of metaphysics against the Ramist detractors). Caput I next.

**2026-10-04 — Stage 1 + Stage 2 complete.** Source acquired via Kiel plaintext endpoint; structural map above; tranche plan drafted. Moving to T1 (front matter + Caput Praeliminare).
