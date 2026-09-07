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
- **T3c-1** (2026-09-07 ✅): *Locus I De Iustificatione* §§23-25 (OCR 4148-4767, ~620 lines): 4-grades-of-necessity analysis (absoluta / definitionis-et-demonstrationis / naturalis / consequentia) with Augustine-memoria-analogy + Chrysostom-in-Matt-18 + 3-anti-Stoic Wittenberg distichs + 3 more predestination objections rebutted (fides-est-donum + Si-Deus-vellet + particularitas-with-12-arguments-for-voluntas-antecedens-salvifica-universalis) + De fructibus fidei et iustitiae with 3-officia-Spiritus-Sancti + FC-VI triplex-usus-legis + anti-Antinomian-Poach-Otto on tertius usus + Snepfius pater-filiolus + Ambrose fides-radix. 13 endnotes ¹⁰³-¹¹⁵.
- **T3c-2** (2026-09-07 ✅): *Locus I De Iustificatione* §26 *Recapitulatio* Capita I-XLIV (OCR 4768-5745, ~980 lines): Luther articulus-stantis + 7+5-part outline + Capita IV-XVI De Iustitia (triplex-vsus verbi + Aristotle/Theognis + Hebrew Hizdiq/δικαιοῦν forum + relatio + Rom 4/5/8 sedes + iustitia-inhaerens vs imputata) + Capita XVII-XXIII De Gratia et Dono (synonym-cluster + Pelagian condemnation + Augustine gratia-praeveniens/subsequens) + Capita XXIV-XXXV De Fide (Cicero-fidei/Aquinas-implicit critique + firma-assensio-fiducia + Yezer-Samuch Isa 26 + Heb 11 hypostasis + Basil πληροφορία) + Capita XXXVI-XLIV De Particulis (4-fold gratis/sine lege/non ex operibus/sola fide + patristic catena + 4 causae + fides-not-alone-with-charitas + Luther fides-numquam-otiosa flame-analogy + tower-experience). 11 endnotes ¹¹⁶-¹²⁶.
- **T3c-3** (2026-09-07 ✅): *Locus I De Iustificatione* §26 Capita XLV-LXXXV + Christ-hymn + **FINIS LOCI PRIMI** (OCR 5746-6654, ~910 lines): Capita XLV-LII De Causis (efficient/impulsive/formalis/instrumentalis/final + 3 causae fidei + rejection of enthusiastic-raptus and stipes-truncus-lapis) + Capita LIII-LXV De Imputatione (2 significations + commutativa + iustitia = res-positiva-Christi + Luther tower-experience narrative + iustitia paßiva vs actiua + anti-Osiander iustitia essentialis + Piscator anti-active-obedience rebuttal via Rom 10 τέλος-νόμου + FC III integrum obedientiae Christi) + LXVI De Renovatione + LXVII-LXIX Ex operibus Legis Mosaicae + LXX-LXXIV OCR-gap flagged transparently (Ps 39 + 1 Tim 4) + LXXV-LXXIX FC-IV necessary-secundum-gradus-not-ad-salutem (anti-Major-Amsdorf) + Augustine candle-in-Solis-radio + LXXX-LXXXII Adversariorum errores with 14+ ill-wrested Scripture loci rebutted (Sirach 16/Heb 13/Prov 17/Matt 12/James 2/Jer 35 Rechabites/Luke 7 sinner-woman/Dan 4-Tob 4/Luke 6/Matt 19/1 Cor 13/Col 3/1 Pet 4/1 John 3) + Bernard sufficit-scire-non-sufficit-meritum + rejection of meritum congrui/condigni + LXXXIII-LXXXIV contra dubitationem Papisticam with 9-fold πληροφορία-basis + LXXXV closing prayer + 32-line Christe-Deus elegiac Christ-hymn (Latin verbatim + English) with Emmaus + caro-in-throno topoi. 9 endnotes ¹²⁷-¹³⁵.
- **T4a** (2026-09-07 ✅): *Locus II De Poenitentia* §§1-3 (OCR 6655-6905, ~250 lines): 8-question outline + Q1 Quid sit poenitentia (rejection of scholastic definitions + μετάνοια-vs-μεταμέλεια Wittenberg-Hebraist etymology with Shob/Teshuvah/Nicham + Ausonius epigrammatic Metanoea aside + Christian definition: conversio-hominis-ad-Deum via contritio+fides+nova-obedientia + 25-item catalog of practica-not-tantum-theorica requisita) + Q2 An ex Lege vel Euangelio (2 Cor 7 duplex-triftitia + Heb 10 nulla-hostia + ordo concionum + Petri-vs-Iuda paradigm with tears-furrows topos) + Q3 Partes (3-part Contritio/Fides/Nova obedientia + Ps 13/14/15/25 sedes + Luther-halbe-Buße + 4 German pedagogical proverbs). 4 endnotes ¹³⁶-¹³⁹.
- **T4b** (2026-09-07 ✅): *Locus II De Poenitentia* §§4-6 (OCR 6906-7435, ~530 lines): Q4 Causae (6 causes + 8+ modi Dei praemonet with 120/390/40-year spacio, Ps-Berosus Noah 78-yr ark, celestial signa, Amos 4 castigation, degeneratio omnium rerum, λιμὸν/λοιμὸν/πόλεμον + 6 causae longanimitatis with Jerome/Chrysostom/Clemens Alex/Augustine ad Macedonium/Gregory Moralia/Luther Genesin/Nazianzen quatrain + 2 additional causae: Augustine Tract 97 proclivitas naturae + Filius Dei fons longanimitatis) + Q5 Exempla poenarum (4 categories testified + Ps 7 + Sennacherib + Ixion + Mauritius) + Q6 Vera ratio (David Ps 38+51 + Adam Gen 3 + Manasses' pseudepigraphic prayer verbatim + Publican Luke 18 with Peter+Centurion parallels + 6-fold anti-despair regimen with verbatim Marchian anti-Devil mock-heroic Latin verses + Music-as-praetaste-of-eternity Luther Encomion musices). 11 endnotes ¹⁴⁰-¹⁵⁰.
- **T4c** (next): *Q7 De erroribus adversariorum* (OCR 7436-8571, ~1130 lines — long anti-Pontifical section on contritio-attritio, satisfactio, indulgentiae, purgatorium, aureal-fabula theology).
- **T4d**: Q5-renumbered [discrimen] (8571-8677) + Q6-renumbered [De vocabulo] (8677-8718) + Q7 continues (8718-9229) + Q8 An et quatenus (9229-9394) + Q10 Quae sit ratio (9394-?).
- **T4e-remainder**: sub-Locus **De Regno Christi** (~ln 8041).
- **T5**: sub-Locus *De Bonis Operibus* (~ln 8265).
- **T6**: sub-Locus *De Libero Arbitrio* (~ln 9885).
- **T7**: *Locus III De Libertate Christiana* + De Praedestinatione appendix.
- **T8**: *Locus IV De Ecclesia* + De Oratione appendix.
- **T9**: *Locus V De Sacramentis* opening + *De Baptismo*.
- **T10**: *De Coena Domini* (large — >4,700 OCR lines; may split into T10a/T10b).
- **T11**: *Locus VI De Vita Hominis* (Loci Quintus + Sextus + De Resurrectione) + *Verba Piorum* closing meditation.
- **T12**: Back matter — FINIS + Elenchus Locorum + Index Rerum + Colophon + audit-at-close (paragraph-by-paragraph via parallel Explore agents, per Pars I methodology) + endnote apparatus finalisation + volume PDF build.

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
