# Selnecker · Symbolorum Apostolici, Niceni, et Athanasiani Exegesis · 1577 · Working Notes

## Volume placement

This is the third volume in the Scholastic-Lutherans Selnecker programme, following:

- **Vol I** — *Institutionis Christianae Religionis Pars I* (Jena, Tröster, 1573; reissued 1579) — complete.
- **Vol II** — *Institutionis Christianae Religionis Pars II* (Jena, Tröster, 1579) — complete (commit `faa50ef`).
- **Vol III (this)** — *Symbolorum Apostolici, Niceni, et Athanasiani Exegesis* (Leipzig, Rhamba, 1577).

There is no *Institutio Pars III*. The *Institutio* is a two-part work. The creedal / Christological material that a modern reader would expect as "volume III" was published by Selnecker as **this** standalone exposition. It is the natural continuation of the Institutio's dogmatic arc because it (a) takes up the mature Lutheran Christology (Communicatio Idiomatum, Majesty of the Son of Man, ubiquity) that Pars II only touched on inside its Coena-Domini locus, and (b) reprints Selnecker's own 1560 Heidelberg disputation on the Real Presence, cementing his standing as an FC VII/VIII-lineage co-author.

## Source

**Bibliographic authority:** Google-Books ID `hyfSeau9q60C`. Scanned copy of the Bayerische Staatsbibliothek München exemplar (BSB shelfmark stamp `00021305` visible on the verso of every folio in the scan). The 1577 imprint is the **enlarged reissue** of the 1575 first edition (Google-Books `QyE8AAAAcAAJ`, also BSB); the enlargement carries forward the original 1575 dedication (dated *Lipsiæ Mense Aprili cIɔIɔ.LXXV*) without alteration.

**Title-page text (as printed):**

> SYMBOLORVM APOSTOLICI, NICENI, ET ATHANASIANI EXEGESIS, fideliter repetens doctrinam perpetuam Ecclesiæ DEI de præcipuis Capitibus & Articulis Christianæ Fidei, inprimis de Diuinitate æterna Filij Dei, de Vnione hypostatica duarum naturarum in Christo, de Maiestate Filij hominis, de Communicatione idiomatum: de Cœna Domini &c. CONTRA RECENTES HORVM temporum blasphemias. SCRIPTA ET EDITA AVTORE Nicolao Selneccero D. Electorali Professore in Academia Lipsica. — LIPSIÆ, Iohannes Rhamba excudebat. M.D.LXXVII.

**Motto (Augustine, epist. 7):** *Nimis peruersè seipsum amat, qui & alios errare vult, ut error ipsius lateat.*

**Working PDF:** `sources-original/selnecker-symbolorum-1577.pdf` (41.3 MB / 399 PDF-pages / 368 printed pages of book text). Downloaded fresh 2026-09-08 via the standard Google-Books direct-PDF URL — no captcha for this ID at this time.

**OCR extraction:** `pdfplumber` layout-extraction at `sources-original/symbolorum-full.txt` (13,340 lines / ~500 KB). Same extraction pipeline as Pars I & II (see `sources-original/extract.py`). OCR quality is consistent with Pars II — good on Antiqua Latin but with the characteristic no-space run-together of ligatures and long-*ſ*, and sporadic Greek transliteration corruption in the Greek code-switching passages (which are frequent in this volume — Selnecker embeds Chalcedon-formula Greek in the Communicatio Idiomatum section verbatim). Cross-check every substantive Greek passage against the JPG facsimile.

## Structural map (2026-09-08 survey)

| Section | OCR ln range | PDF pp | Print pp | Content |
|---|---|---|---|---|
| Google/BSB scanner boilerplate | 1-8 | 1 | — | Google-Books preservation notice |
| **Title page** | 9-30 | 2 | (unnumbered) | *Symbolorum … Exegesis* — Rhamba 1577 Leipzig |
| BSB shelfmark stamp | 31 | 3 | — | `00021305` |
| **Dedicatory Epistle to Johann Günther, Count of Schwarzburg-Arnstadt-Sondershausen-Leutenberg** | 32-882 | 4-31 | (unnumbered) | Selnecker introduces the volume as the enlarged expansion of his earlier Greek-Latin *Catechesis Minor* + additional catechetical questions on the *præcipua Doctrinæ Christianæ capita*; polemic against detractors of doctrinal writing; heavy citation of Luther *ad Ducem Georgium* (1533), Augustine, and Nazianzen. Dated *Lipsiæ, Mense Aprili, cIɔIɔ.LXXV* (April 1575 — original dedication carried into the 1577 imprint verbatim). |
| **The Three Creeds printed together** | 888-1471 | 32-49 | 1-18 | Verbatim Latin text of **Symbolum Apostolicum** (890-908), **Symbolum Nicenum** (Nicene-Constantinopolitan, filioque included) (909-945), **Symbolum Athanasii** (Quicunque vult) (946-1466). Closes with a Selnecker Latin distich signed *anno 1573*. |
| **General Prolegomena — ENARRATIO SYMBOLI APOSTOLICI, NICENI, ET ATHANASIANI** | 1477-2376 | 50-74 | 19-43 | Why we recite creeds in the Church; role of ecumenical synods (four causes God ordains them); how synods do not create new dogmata but witness to Prophetic + Apostolic teaching; *Usitata divisio Symbolorum* — the standard triadic division (Creation / Redemption / Sanctification); the subdivision of Article II into 6 sub-articles and Article III into 5, per the twelve-Apostles tradition. |
| **ARTICVLVS PRIMVS — Credo in Deum Patrem Omnipotentem** | 2377-6498 | 75-195 | 44-164 | Five-part exposition: **(I)** *Quid fit Credere* — historical vs justifying fides; *credere Deum / in Deum / Deo* distinctions. **(II)** *De vna Dei essentia et tribus personis* — Trinitarian metaphysics; essence / person / hypostasis vocabulary; anti-Sabellian and anti-Arian polemic. **(III)** *De prima Trinitatis persona* iuxta the creed's words. **(IV)** *De Creatione* — creation ex nihilo; grades of creatures; angels; man; *imago Dei*; the four states of man. **(V)** *De providentia, contingentia, lapsu, libero arbitrio, peccato, Lege* — Providence, contingency, the Fall, free will, sin, and the Law, culminating in the Law-Gospel discrimen (six-fold distinction 6480-6498) that transitions into Article II. |
| **ARTICVLVS SECVNDVS — Credo in Iesum Christum Filium Dei** | 6499-10579 | 196-317 | 165-286 | Christology proper: **Persona / Divinitas / Incarnatio / Officium Christi.** The Redeemer's eternal generation from the Father; the *arcanum consilium Trinitatis* to send the Second Person as Mediator; anti-Nestorian and anti-Eutychian formulations; the exegesis of each clause of the Nicene article (*Deum de Deo, lumen de lumine, genitum non factum, consubstantialem Patri, per quem omnia facta sunt*). Includes the passion / crucifixion / descensus / resurrection sub-articles. Closes with the transition into the Christological *Doctrina* proper. |
| **DOCTRINA DE COMMVNICATIONE IDIOMATVM** | 10580-11000 | 317-329 | 286-298 | The mature-Lutheran Christological doctrine appended as an amplification of Article II. Chalcedonian formula quoted in Greek verbatim (10603-10604 *ἑκάστης φύσεως εἰς μίαν ὑπόστασιν συντρεχούσης*); the three *genera communicationis* (idiomatum in concreto, apotelesmaticum, majestaticum) implicitly followed. Heavy anti-Reformed *extra Calvinisticum* polemic. |
| **Articulus Ascensionis** | 11001-11257 | 329-337 | 298-306 | The Ascension article expounded not as mere local translation to a physical heaven, but as the exaltation of Christ's human nature *super omnes cælos ad dexteram Dei*. |
| **An Christus sit omnipræsens etiam secundum humanam naturam** | 11258-11578 | 337-348 | 306-317 | The **ubiquity question** proper — the mature Lutheran defense of the human nature's omnipresence, *secundum genus maiestaticum communicationis idiomatum*. Anti-Reformed polemic on the *finitum non capax infiniti* axiom. |
| **De Sessione ad Dexteram Dei** | 11579-~12300 | ~348-~370 | ~317-~339 | *Sedet ad dexteram* — the dextra Dei as universal dominion, not a physical location; the sessio as the office-formal ground for the ubiquity of Christ's human nature. |
| **De Adoratione Christi + De Judicio venturo** | ~12300-12623 | ~370-377 | ~339-346 | The adoration of the incarnate Christ; the *Veni Domine Iesu* longing for the return; the last judgment as the vindication of Christ's regnum. Ends with *Veni Domine Iesu, Amen.* |
| **ARTICVLVS TERTIVS — Credo in Spiritum Sanctum + Ecclesiam + Communio Sanctorum + Remissio + Resurrectio + Vita Æterna** | 12624-12754 | 378-382 | 347-351 | The Third-Article opening: **Spiritus Sanctus** as *Dominus et vivificans*, the five *beneficia Spiritus Sancti* (docere / renovare-sanctificare / iuvare / obsignare / arrhabo); the **Ecclesia** as *vbicunque sonat vox Evangelii*; Epiphanius Greek Creed-fragment quoted verbatim. Comparatively brief; the Sacrament exposition is treated as the natural continuation via the following section. |
| **PROPOSITIONES … VERA DE COENA DOMINI SENTENTIA (Heidelberg Disputation, 3-4 June 1560)** | 12755-13229 | 382-396 | 351-365 | **Significant documentary piece.** Verbatim reprint of Selnecker's own 1560 Heidelberg disputation-theses on the Real Presence, defended *iuxta Confessionem Augustanam adversus quorundam certamina* at the Academia Heidelbergensis under Frederick III (just before Frederick's turn Reformed and Selnecker's departure). Numbered propositional theses covering: substantial presence, distinction from the Reformed *nuda signa* and *virtute-non-substantia* positions, the *cum-in-vel-sub pane* formula, oral-manducation, distribution to worthy and unworthy alike. Historically important early witness of the Lutheran Real-Presence position that will later become FC VII. |
| **DE IVDA ACCIPIENTE CORPVS ET SANGVINEM CHRISTI (manducatio impiorum patristic catena)** | 13230-13337 | 396-399 | 365-368 | Extensive patristic catena on Judas receiving the body-and-blood of Christ (the *manducatio indignorum / impiorum* controversy). Cited: Augustine *De baptismo contra Donatistas* lib. 5 cap. 8 (Tom. 7), Augustine *contra Donatist.* lib. 9 (via Fulgentius), Bernard *de modo bene vivendi ad sororem* serm. 28, Jerome *in Esaiam*, Oecumenius. Closes with the *Regula* on how the Fathers' language about the wicked *not eating* is properly understood of the *manducatio spiritualis* per John 6, not the sacramental *res sacramenti*. |
| **Colophon** | 13333-13337 | 399 | 368 | LIPSIÆ Iohannes Rhamba excudebat Anno M.D.LXXVII. |
| BSB stamp | 13339-13340 | 399 | — | BSB MÜNCHEN |

**Notes:**
- **No back-matter apparatus.** Unlike Pars II, this edition has no *Elenchus locorum Scripturae*, no *Patrum Sententiae* index, and no *Index rerum et verborum memorabilium*. The book runs straight from the Third-Article Coena-Domini appendix to the printer's colophon. If a comprehensive subject index is desired for the English edition, the translator will need to construct one from scratch, following the Pars II precedent (T10b-c).
- **No preface separate from the Dedicatory Epistle.** The 1575 Dedication to Count Johann Günther of Schwarzburg does double duty as introduction.
- **Print-page numbers** run from p. 1 (start of the three creeds, PDF p. 32) to p. 368 (colophon, PDF p. 399). The dedication is unpaginated. Add 31 to the printed page number to get the PDF-page number (approximately).

## Six-domain announcement (from title page) mapped to actual sections

| Title-page announced topic | Rendered in section |
|---|---|
| *Divinitate æterna Filij Dei* | Article II (6499-10579) and *De vna Dei essentia* within Article I (2388ff) |
| *Unione hypostatica duarum naturarum in Christo* | Article II + *Doctrina de Communicatione Idiomatum* (10580ff) |
| *Maiestate Filij hominis* | *De Communicatione* + Ubiquity section (11258ff) |
| *Communicatione idiomatum* | Named section 10580-11000 |
| *De Cœna Domini &c.* | 1560 Heidelberg Disputation (12755-13229) + *De Iuda accipiente* (13230-13337) |

Every announced topic is present in the body.

## Conventions carried forward from Pars I & II

- **Bible-citation policy.** Every scripture quotation in the body is the translator's own English rendering of Selnecker's own Latin citation. No copyrighted modern English Bible version (NKJV, NIV, ESV, or otherwise) is quoted anywhere. Selnecker's own numbering (which follows the Vulgate in some Psalms) is preserved and any divergence from Hebrew/English numbering is flagged inline. See Pars II Translator's Note for the full articulation.
- **Latin-original block preservation.** Verse-fragments, poetic distichs, Greek code-switching passages, and Chalcedon-formula Greek are quoted in the Latin/Greek original first, followed immediately by an English rendering. This is essential in this volume because the Communicatio Idiomatum section relies heavily on Greek fathers' formulae.
- **Endnote apparatus at volume end.** Numbered endnotes ¹ ² ³ … are collected in a single apparatus at the very end of the volume, immediately before any back-matter (there is no printed back-matter in this edition, so endnotes are the final section). Endnote convention: `¹ Description of the note.` with cross-references between endnotes marked `[[note-N]]`.
- **Structural section-header convention.** In the review Markdown, use `#` for the volume title, `##` for major creed articles + prolegomena + dedication + translator's note, `###` for sub-articles, `####` for scholia / questions / catenae subdivisions.
- **Reader-facing Translator's Note.** Volumes are shipped with a *Translator's Note* explaining source, editorial policy, Bible-citation policy, and known OCR limitations — **never** local paths, tranche-plan language, memory-link `[[...]]` syntax, or internal build details. The Pars II final Translator's Note (in `review/selnecker-institutiones-1573-pars-ii.md`) is the model.
- **Build pipeline.** `build-shareable.ps1` runs Pandoc → DOCX → LibreOffice → PDF. The shareable-name PDF stem for this volume is: `Nikolaus-Selnecker-Exposition-of-the-Apostles-Nicene-and-Athanasian-Creeds-1577-English-Scholastic-Lutherans`. The build script has been pre-populated with the correct stem and paths.

## Suggested tranche plan (Vol III — proposed)

Recommend the following tranche breakdown, modeled on the Pars I & II pattern (~700-1000 OCR lines per tranche for the dense-dogmatic sections, up to ~2000 lines for the more expository sections):

- **T0** (2026-09-08 ✅): Source acquired + directory created + OCR extracted + structural survey. This document.
- **T1**: *Translator's Note* (fresh — one-volume-of-three closing note is different from Pars II's post-completion note) + *Biographical Sketch* (reuse from Pars I with the addition that this volume is Selnecker's dogmatic-catechetical intersection) + Title-page-as-printed + Dedicatory Epistle to Johann Günther of Schwarzburg (April 1575) + The Three Creeds printed together (Apostolicum, Nicaenum, Athanasianum — Latin + English).
- **T2**: *Enarratio Symboli* general prolegomena (OCR 1477-2376): Why we recite creeds, the four causes God ordains synods, *usitata divisio Symbolorum*, subdivision-into-12 tradition.
- **T3a**: *Articulus Primus* Part I (OCR 2377-~4000): *Quid fit Credere* — historical/justifying fides distinction — Trinity/essence/person vocabulary.
- **T3b**: *Articulus Primus* Part II (OCR ~4000-~5200): De prima Persona iuxta symbolum + De Creatione (creation, angels, man, imago Dei, four states).
- **T3c**: *Articulus Primus* Part III (OCR ~5200-6498): De providentia + contingentia + lapsu + libero arbitrio + peccato + Lege + Law-Gospel discrimen bridge to Article II.
- **T4a**: *Articulus Secundus* Part I (OCR 6499-~8000): Persona Christi + Divinitas + Officium — opening exposition + arcanum consilium Trinitatis + anti-Nestorian formulations.
- **T4b**: *Articulus Secundus* Part II (OCR ~8000-~9500): Incarnation + Nicene-clause exegesis (*Deum de Deo, Lumen de Lumine, genitum non factum, consubstantialem Patri*) + Passion/Descensus/Resurrection.
- **T4c**: *Articulus Secundus* Part III (OCR ~9500-10579): Closing exposition + transition into Communicatio Idiomatum.
- **T5**: *Doctrina de Communicatione Idiomatum* (OCR 10580-11000): Chalcedon-formula Greek exposition + three *genera communicationis* + anti-Reformed *extra Calvinisticum* polemic. **Critical Greek-passage cross-check against JPG facsimile mandatory.**
- **T6**: *Articulus Ascensionis + An Christus sit omnipræsens* (OCR 11001-11578): Ascension not-mere-local-translation + Ubiquity defense + *finitum non capax infiniti* rebuttal.
- **T7**: *De Sessione ad dexteram + De Adoratione + De Judicio* (OCR 11579-12623): Sessio as universal dominion + Adoration of the incarnate Christ + closing *Veni Domine Iesu*.
- **T8**: *Articulus Tertius* opener (OCR 12624-12754): Spiritus Sanctus + five beneficia + Ecclesia + Epiphanius Greek Creed-fragment.
- **T9**: **1560 Heidelberg Disputation** (OCR 12755-13229) — historically-significant standalone-document treatment recommended; consider a separate Translator's Introduction paragraph explaining the disputation's historical context (Frederick III, pre-Kryptocalvinist Heidelberg, Selnecker's subsequent departure to Jena).
- **T10**: *De Iuda accipiente* patristic catena (OCR 13230-13332) + Colophon + Endnote apparatus finalisation + Reader-facing back-matter (constructed TOC + optional subject index if desired).
- **Audit + Build**: Paragraph-by-paragraph parallel-agent audit (per Pars II T-audit-1 methodology) + PDF build.

## Working file locations

```
dogmatics/selnecker-symbolorum-1577/
├── notes.md                                         # this file
├── build-shareable.ps1                              # Pandoc + LibreOffice build (pre-populated)
├── sources-original/
│   ├── selnecker-symbolorum-1577.pdf                # 41.3 MB / 399 pp / BSB copy via Google Books hyfSeau9q60C
│   ├── extract.py                                   # pdfplumber extraction script
│   └── symbolorum-full.txt                          # 13,340 lines OCR
├── latex/                                           # (empty, reserved)
└── review/                                          # (empty at start; will hold the working .md + built .docx + .pdf)
    └── selnecker-symbolorum-1577.md                 # TO CREATE: main working translation file
```

## Related memory

- Pars I completion notes: `dogmatics/selnecker-institutiones-1573/notes.md`
- Pars II completion notes: `dogmatics/selnecker-institutiones-1573-pars-ii/notes.md` — read the full history of the Pars II tranche-plan for the pattern this volume should follow.
- Pars II Translator's Note (model for the reader-facing note): `dogmatics/selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md` opening section.
