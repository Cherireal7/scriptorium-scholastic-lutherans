# Selnecker · Institutio Christianae Religionis · Working Notes

## Bibliographic correction

The corpus row in [[scholastic-lutherans-program]] indexes this work as *Institutiones (1573).* Preliminary source-hunt (2026-08-31) confirms:

- The full title is ***Institutionis Christianae Religionis*** — from *institutio* (singular), not *institutiones* (plural). The plural spelling appeared on some intermediate title-pages but the standard bibliographic form is the singular *Institutio.*
- The work is a **three-part Loci-style dogmatic corpus** issued in Jena by **Jakob Tröster** in the late 1570s, not a single 1573 imprint.
- **Pars I** — the source Cheri downloaded on **2026-08-31**: **1579** imprint, 489 pages in the Google-Books PDF (`sources-original/Institutio_Christianae_Religionis.pdf`, 21 MB). Cover-title: ***INSTITUTIONIS CHRISTIANAE RELIGIONIS PARS PRIMA, CONTINENS SINCERAM DOCTRINAM Ecclesiae Christi de verbo Dei, de Deo, Creatione, Angelis, hominibus, peccato, lege, cruce, consolatione: ita scripta, & recognita, vt magistris & discipulis vsui esse possit. AUTORE D. NICOLAO SELNECCERO. Praemissa est explicatio & commonefactio de quibusdam controversis articulis. Cum Gratia & Privilegio ad decennium. Anno M. D. LXXIX.*** Source-copy from the **Bayerische Staatsbibliothek Munich** (StaBibl München stamp on the frontispiece; Dogm. 924-1). Google-Books scan-hash 36616462510015.

**Pars II** — the previously-identified BSB Munich digital facsimile: **Jena 1579** (Jakob Tröster), VD16 S 5566, 666 pp + 14 leaves 8vo, HAB signature 577 Theol., under `bsb11295447`. IIIF manifest reports 107 canvases; **true extent is 696 canvases** (BSB manifest-underreport bug — cf. [[feedback_iiif-manifest-verify]]).

The corpus-row date "1573" is therefore adjusted to "1579" (or "c. 1573–1580" for the three-part span) in the working translation frontmatter.

## Source authority

**Primary:** BSB Munich digital facsimile for Pars II:
- Landing page: <https://www.digitale-sammlungen.de/view/bsb11295447>
- IIIF manifest: `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11295447/manifest`
- Per-canvas image URL pattern: `https://api.digitale-sammlungen.de/iiif/image/v2/bsb11295447_{NNNNN}/full/full/0/default.jpg`

**Manifest under-report bug** (compare [[feedback_iiif-manifest-verify]]): the IIIF manifest reports **107 canvases** but per-canvas HEAD-probing (binary search 2026-08-31) confirms the true extent is **696 canvases** ending at `bsb11295447_00696` (canvas 697 returns 404). This matches the bibliographic 666 pp + 14 leaves + front-matter estimate.

**Bibliographic authority:**
- **VD16 identifier:** S 5566 (Pars II)
- **Controversia et Confessio:** entry `fa69041c-1638-4246-99e4-4be5c37a1710`
- **Publication:** Jena, Jakob Tröster, 1579

**Google Books alternate scans** (probably OCR-superior for text-mining):
- Pars II (Iustificatio/Poenitentia/Libertas/Ecclesiae potestas/Sacramenta/vitae hominis ratio): `oeBoAAAAcAAJ` and `xRE8AAAAcAAJ` (two copies)
- Pars III (Authoritate et Certitudine Verbi Divini): `E6VoAAAAcAAJ`
- ["Continens Sinceram Doctrinam Ecclesiae"]: `hBE8AAAAcAAJ`
- Google Books PDF download pattern: `https://books.google.com/books/download/Institutionis_Christianae_Religionis_Par.pdf?id={GBID}&output=pdf`

**Pars I:** not yet identified in a digitised copy. Sourcing task: search PRDL, HAB Wolfenbüttel, VD16.de for VD16 S 5565 (probable identifier).

## Author

**Nikolaus Selnecker** (also *Selneccer, Schellenecker*)
- **Born:** 5 December 1530, Hersbruck (near Nürnberg)
- **Died:** 24 May 1592, Leipzig
- **Formation:** Wittenberg (Melanchthon-student), *Magister* 1554
- **Career highlights:**
  - Court-preacher at Dresden 1565–1568 under Kurfürst August of Saxony
  - Professor at Leipzig from 1568 (with interruptions 1570–1574 during the Crypto-Calvinist controversy)
  - Superintendent at Braunschweig-Wolfenbüttel from 1571
  - Professor at Jena 1571–1574
  - Return to Leipzig 1574 onward as *Superintendent* and *Pfarrer* at St. Thomas
- **Confessional-Lutheran significance:** One of the **six co-authors of the Formula of Concord (1577)** — alongside Jakob Andreä, Martin Chemnitz, David Chytraeus, Andreas Musculus, and Christoph Körner. Selnecker's specific contribution was the *Solida Declaratio* Article XI (Predestination).
- **Hymn-writer:** Author of the paradigm-Lutheran ***"Ach bleib bei uns, Herr Jesu Christ"*** (*EG* 347), and dozens of other confessional-Lutheran hymns still in the modern German-Protestant Gesangbuch.
- **Musicological:** Wrote and edited several Lutheran hymn-books; his ***Christliche Psalmen*** (1587) is one of the paradigm confessional-Lutheran hymn-collections of the whole *Concord* generation.

## Work: structure and scope

*Institutio Christianae Religionis* is Selnecker's mature systematic-dogmatic Loci-work — parallel in genre to Melanchthon's *Loci communes* (1521 → 1543 → 1555), Chemnitz's *Loci theologici* (1591 posth.), and Gerhard's later *Loci theologici* (1610–1622). Selnecker structures the work in *three Parts*, each covering a set of Loci. From the sighted Pars I title-page:

- **Pars I** — the confirmed Loci-sequence: ***De verbo Dei*** (Word of God) · ***De Deo*** (Doctrine of God) · ***De Creatione*** (Creation) · ***De Angelis*** (Angels) · ***De hominibus*** (Man / Anthropology) · ***De peccato*** (Sin) · ***De lege*** (Law) · ***De cruce*** (Cross) · ***De consolatione*** (Consolation). Preceded by ***Praemonitio de nonnullis controversis articulis*** — a paradigm-***anti-Flacian*** ***commonefactio*** on the substance-vs-accident debate over original sin (immediately interfacing with **Formula of Concord Article I** of 1577, which Selnecker himself had helped draft).
- **Pars II** — *De Iustificatione hominis coram Deo* + *De Poenitentia* + *De Libertate Christiana* + *De Ecclesiae potestate* + *De Sacramentis* + *De vitae hominis ratione* (paradigm Reformation-era *ordo salutis* + ecclesiology + sacraments + Christian ethics)
- **Pars III** — *De Novissimis* (Last Things) + *De Antichristo* + closing controversies

Pars I is the natural first-volume target because Cheri already has the source: the paradigm ***De verbo Dei*** opens the whole *Institutio,* the anti-Flacian *Praemonitio* is one of the paradigm early-*Formula*-adjacent polemical texts, and the sequence Word→God→Creation→Angels→Anthropology→Sin→Law→Cross→Consolation is a paradigm Reformation-era *loci-order* (compare Melanchthon's *Loci communes,* Chemnitz's *Loci theologici,* and Gerhard's *Loci theologici*).

## Tranche plan (Pars I — active)

- **T0**: Source acquired 2026-08-31 (Cheri's download). PDF at `sources-original/Institutio_Christianae_Religionis.pdf`, 489 pages, 21 MB. pdftotext extraction cached at `ia-1579-pars1-full.txt` (28,024 lines).
- **T1**: Front-matter + Translator's Note + Title-page + Dedicatio ad Consules Senatoresque Reipublicae Lipsensis + **Praemonitio de nonnullis controversis articulis** (paradigm-anti-Flacian original-sin-as-accident treatment, FC I). Pages 6–30.
- **T2**: Locus 1 — ***De verbo Dei*** (Word of God) — paradigm Reformation *sola scriptura* dogmatic-locus.
- **T3**: Locus 2 — ***De Deo*** (Trinitarian doctrine of God).
- **T4**: Locus 3 — ***De Creatione*** + Locus 4 ***De Angelis***.
- **T5**: Locus 5 — ***De hominibus*** (Anthropology).
- **T6**: Locus 6 — ***De peccato*** (Sin — including detailed FC I anti-Flacian polemic).
- **T7**: Locus 7 — ***De lege*** (Law — with FC V–VI Law-Gospel + Third Use interfaces).
- **T8**: Locus 8 — ***De cruce*** (Cross — theologia crucis + Kreuz-Frömmigkeit).
- **T9**: Locus 9 — ***De consolatione*** (Consolation — paradigm closing pastoral-dogmatic locus) + Colophon + Register + volume-final PDF build.

For **Pars II** (BSB `bsb11295447`) and **Pars III** (Google Books `E6VoAAAAcAAJ`): separate future volumes.

## Methodology

Follow the **Praetorius-Chytraeus-Kirchner-Große** standard workflow ([[reference-scholastic-lutherans-workflow]]):
- **Claude vision on BSB JPGs first** (established best-practice from Flacius *Catalogus* 1556 CAMENA methodology) — cleaner than Tesseract for 16th-c. Antiqua Latin.
- Verify page-by-page against the JPG facsimile.
- All endnotes in the back matter; body text is Selnecker only.
- Modern editions in endnotes: WA/LW for Luther, CR/MSA for Melanchthon, BSLK/*Kolb-Wengert* for confessional documents, PL/PG for church fathers.
- Formula of Concord references cross-linked to *Kolb-Wengert* (Fortress, 2000).

## Related

- [[scholastic-lutherans-program]] — Tier 2 opener
- [[reference-scholastic-lutherans-workflow]] — pipeline
- [[reference-scholastic-lutherans-glossary]] — Lutheran-orthodoxy vocabulary
- [[feedback_iiif-manifest-verify]] — the manifest-underreport rule (confirmed here again: 107 vs 696)
- [[chytraeus-catechismus-1594]] — parallel Formula-of-Concord-generation Latin catechetical work
- [[kirchner-enchiridion]] — parallel Concord-generation German-language catechetical handbook
