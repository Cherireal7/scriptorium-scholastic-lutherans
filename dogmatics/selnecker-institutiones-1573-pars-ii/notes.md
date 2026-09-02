# Selnecker · Institutio Christianae Religionis · Pars Secunda · Working Notes

## Source

**Bibliographic authority:** VD16 S 5566 — Jena, Jakob Tröster, 1579.

**Working text-base:** Google-Books scan of the Bayerische Staatsbibliothek München copy (shelfmark Dogm. 11-2 by the BSB Staatsbibliothek stamp on p. 5 of the scan; scan-hash `36616453470017`). Google-Books ID `xRE8AAAAcAAJ` is the same copy; direct PDF download from Google Books is captcha-gated, so the working copy is the BSB scan already on disk from the Pars I sourcing session (2026-08-31), renamed to `selnecker-pars-ii-1579.pdf` (30.6 MB / 695 pages) in this volume's `sources-original/`.

**OCR extraction:** `pdfplumber` layout-extraction cached at `sources-original/pars2-full.txt` (24,003 lines / 1,056 KB). Extraction quality is generally good for 16th-c. Antiqua Latin but with the characteristic no-space run-together of ligatures and long-*ſ*; also with sporadic Greek transliteration corruption where the Antiqua Greek types were confused with Latin. Cross-check every substantive Greek passage against the JPG facsimile.

## Structural map (2026-09-02 survey)

| Section | OCR ln range | Approx pp | Content |
|---|---|---|---|
| Google/BSB boilerplate | 1-51 | 1-7 | scanner-inserted preface + title-page (p 6) + BSB stamp (p 7) |
| **Proem: De Evangelio** | 52-1130 | 8-37 | Sion-prophecy meditation → Gospel-word etymology → definition of the Gospel + 4-fold cause-analysis (efficient / impulsive / instrumental / material) → the Two Testaments distinction. Preamble to the six announced Loci. |
| **Locus 1 — De Iustificatione hominis coram Deo** | 1131-6654 | 38-192 | 5,520 lines. Three-fold *iustitia* → definition of *iustitia fidei* → *forensic* character of *iustificari* → three passive uses → *sola fide* → argumenta pro *iustificatione* → against Osiander → against Trent → *Cur pia opera necessaria sint* → *Consolationes* for the tempted. Ends with a Latin Christ-hymn against heretics. |
| **Locus 2 — De Poenitentia** | 6655-10963 | 193-313 | 4,309 lines. 8-question schema (What is penitence? · From Law or Gospel? · Its parts · Daily causes · Examples of divine punishment · The true manner of penitence · The adversaries' errors · Absolution + the Cross of the Church). Includes sub-Loci **De Regno Christi** (ln 8041), **De Bonis Operibus** (ln 8265), **De Libero Arbitrio** (ln 9885). |
| **Locus 3 — De Libertate Christiana** | 10964-11079 & related | 314-321 | Manumissio spiritualis: four grades of Christian liberty (Gratia / Donum per Gratiam / etc.). |
| **[extra] De Praedestinatione** | 11080-12238 | 322-353 | Follows Libertas Christiana. Selnecker's own *Solida Declaratio* FC XI Article material carried into the *Institutio*. |
| **Locus 4 — De Ecclesia** ["Ecclesiæ potestas" of the title page] | 12239-13455 | 354-390 | Doctrine of the Church → before and after the Fall → note vs. attributes → true and false Church → power of the keys. |
| **[extra] De Oratione** | 13456-15254 | 391-437 | On Prayer. |
| **Locus 5 — De Sacramentis** | 15255-16186 | 438-465 | General definition + number → against Papist septenary. |
| **De Baptismo** | 16187-17133 | 466-495 | Baptism proper. |
| **De Coena Domini** | 17134-21877 | 496-616 | The Supper — extensive, > 4,700 lines. Includes exegesis of the Verba, refutation of the Sacramentarian and Reformed *extra Calvinisticum*, the *manducatio oralis / impiorum* debate, and the FC VII interface material. |
| **Locus 6 — De Vita Hominis** (Loci Quintus + Sextus + De Resurrectione) | 21878-23158 | 617-657 | Two closing Loci ("De Quinto Loco" / "De Sexto") on the *ratio vitae hominis* + On the Resurrection of the flesh. |
| **Verba Piorum ex Hac Vita in Aeternam Vitam Decedentium** | 23162-23310 | 658-679 | Closing meditation: extract from *M. Johann Rosa*'s oration on the Christian's death, in Selnecker's *pia beata memoria* framing. |
| **FINIS SECVNDÆ PARTIS** | 23159 | 657 | End-of-Part rubric. |
| **Elenchus Locorum + Index** | 23311-end | 680-695 | Alphabetical scripture-loci elenchus + subject index. |

## Six-domain announcement (from title page) mapped to actual Loci

| Title-page domain | Rendered Locus |
|---|---|
| Iustificatio hominis coram Deo | Locus 1 (with De Evangelio as proem) |
| Poenitentia | Locus 2 (with sub-Loci De Regno Christi, De Bonis Operibus, De Libero Arbitrio) |
| Libertas Christiana | Locus 3 (with De Praedestinatione appended) |
| Ecclesiæ potestas | Locus 4 De Ecclesia (with De Oratione appended) |
| Doctrina de Sacramentis | Locus 5 (with De Baptismo + De Coena Domini) |
| Vitæ hominis ratio | Locus 6 (with the two internal sub-Loci and De Resurrectione + Verba Piorum meditation) |

## No separate dedicatory epistle

The 1579 Pars II imprint proceeds directly from the title page (p 6) — via the BSB shelfmark stamp on p 7 — into the Proem *De Evangelio* on p 8. There is no separate dedicatory letter. This differs from Pars I 1579 (which carries a dedication *To the Consuls and Senators of the Republic of Leipzig,* dated May 1579). The absence of a Pars II dedication is documented transparently in the Translator's Note; a paragraph-by-paragraph audit at close (per [[iiif-manifest-verify]]) will re-confirm this.

## Tranche plan (Pars II — active)

- **T0** (2026-09-02): Source acquired + directory created + OCR extracted + structural survey.
- **T1** (this commit): Translator's Note + Biographical Sketch (reused from Pars I) + Title-page-as-printed + note on absence of dedication + paginated TOC skeleton + opening of *De Evangelio* proem + opening of *Locus I De Iustificatione* (through the three uses of *iustitia*).
- **T2**: Remainder of *De Evangelio* proem (Gospel definition + 4-fold cause-analysis + Two-Testaments distinction).
- **T3a** (2026-09-02 ✅): *Locus I De Iustificatione* §§3-15 (OCR 1180-3287, ~2,100 lines): Bernard's Four-Sisters meditation on Ps 85 + sixfold denial + Quid sit Imputatio with Anselm's *Domine mortem obiecio* + How-just-by-imputation-when-not-*res positiva* + Whether-God-unjust-reputing-just + Whether-just-by-imputation-or-*inchoatio* + anti-Osiander *iustitia essentialis* + *Sedes doctrinae* with Romans 4 ten-arguments + Rom 9 Rachel/Leah/Jacob/Esau + Pharaoh-hardening philology + Luther's Swan-Song prophecy + 16 Galatians arguments + Faith definition + Faith causes + Synergon controversy + Melanchthon+Spalatinus verse-mnemonics.
- **T3b** (2026-09-02 ✅): *Locus I De Iustificatione* §§16-22 (OCR 3287-4148, ~860 lines): Sola-Fide 4 reasons (honos Christi/certitudo/vera invocatio/discrimen Legis-Ev) + patristic *sola fide* testimonies (Chrysostom/Basil/Nazianzus/Photius Sirmiensis (properly Constantinopolitanus)/Origen/Ambrose (properly Ambrosiaster)/Athanasius/Hilary + Victor Poeta's Alethia couplet) + Trent Sess VI Canon 9 fulmen rebuttal with 15-equipollent-terms proof + Luther's *ring/gem* metaphor from Antilatomus + De vocabulo Gratiae (Ambrosian Chen/charis/Gratia/Gnad) with Pauline gratia-vs-donum distinction (Rom 5:15) + Augustinian general-vs-special grace + Pelagian history + Scholastic gratia-gratum-faciens-vs-gratis-data + Augustinian operating-vs-cooperating + Contra dubitationem Monachorum with 3 Papist grounds rebutted + Isa 26 *yēṣer sāmûk* firm-cogitation-of-faith with D. Forster Hebrew analysis + 4-token weak-faith framework + Trent Sess VI Canon 13 certitude-anathema rebutted with 8 firm arguments (nature-of-promise + nature-of-faith + Spirit's arrhabōn + Abraham's example + effects of faith + Sacraments-as-seal + Gospel-commands-luctari-contra-dubitationem + Law-Gospel discrimen) + 8 Papist objections rebutted (Ecclesiastes 9 / Sirach 5 / Jonah 3 / karidognōstēs / Phil 2 filial-vs-servile fear / perseverance / temptation / humility-vs-confidence / abuse-arg / weakness-arg).
- **T3c**: *Locus I De Iustificatione* §§23-end (OCR 4148-6654, ~2,510 lines): 4-grades-of-necessity analysis with Augustine + Chrysostom rebutting Stoic *necessitas absoluta* + Luther-*De-Servo-Arbitrio*-limits + 4-necessity-grades + De Secundo Vocabulo iustificationis + De Tertio Vocabulo + anti-Osiander *iustitia essentialis* full section + Rom 5 new obedience proper + De Sexto (6 causes of iustificatio: efficient/impulsive/material/formal/instrumental/final) + Cur pia opera necessaria sint + Consolationes for the tempted + closing Christ-hymn against heretics.
- **T4**: *Locus II De Poenitentia* + sub-loci (De Regno Christi, De Bonis Operibus, De Libero Arbitrio).
- **T5**: *Locus III De Libertate Christiana* + De Praedestinatione appendix.
- **T6**: *Locus IV De Ecclesia* + De Oratione appendix.
- **T7**: *Locus V De Sacramentis* opening + *De Baptismo*.
- **T8**: *De Coena Domini* (large — >4,700 OCR lines; may split into T8a/T8b).
- **T9**: *Locus VI De Vita Hominis* (Loci Quintus + Sextus + De Resurrectione) + *Verba Piorum* closing meditation.
- **T10**: Back matter — FINIS + Elenchus Locorum + Index Rerum + Colophon + audit-at-close (paragraph-by-paragraph via parallel Explore agents, per Pars I methodology) + endnote apparatus finalisation + volume PDF build.

## Methodology

Follow the Praetorius-Chytraeus-Kirchner-Große-Selnecker-Pars-I standard workflow ([[reference-scholastic-lutherans-workflow]]):
- Claude vision on Google-Books JPG facsimile pages where OCR ambiguity is material (Antiqua Greek passages, run-together long-*ſ* words in citation-formulas).
- Every paragraph in the English body traces to a specific OCR line-range in `pars2-full.txt`.
- Modern-critical citation apparatus in the endnotes only: WA/LW for Luther, CR/MSA for Melanchthon, BSLK/*Kolb-Wengert* for the confessions, PL/PG/CCSL/SC for the Fathers, Formula-of-Concord cross-references throughout (Selnecker was co-author of FC Art. XI).
- Editorial ornament: `— ❦ —` (aldus leaf), per the divider convention from Chytraeus onward.
- No `Co-Authored-By: Claude` trailers; no personal-information in rendered files; byline = "The Scholastic Lutherans translation team".

## Related

- [[project-selnecker-institutiones-1573]] — Pars I project record (COMPLETE) — the template for this volume.
- [[reference-selnecker-pars-ii-kickoff]] — the kickoff memory that launched this volume; delete once Pars II is complete.
- [[reference-scholastic-lutherans-workflow]] — Pandoc + LibreOffice pipeline.
- [[reference-scholastic-lutherans-glossary]] — Lutheran-orthodoxy vocabulary + editorial conventions.
- [[iiif-manifest-verify]] — verify manifest canvas-count vs true extent before claiming coverage-complete.
