# Große, *Die alten Tröster* (1900) — Working Notes

Scholastic Lutherans working file. This is the operational scratchpad for the translation; the reader-facing Translator's Note lives at `review/grosse-alten-troester-1900.md`.

**Session log:** kick-off scaffold + source sighting 2026-08-30 (single session).

## Two corrections to the coordination memo

The parallel-work memo ([[scholastic-lutherans-parallel-work-2026-08]]) named this work as **Alexander Grosse, *Die alten Tröster* (1614)** — a "patristic-consolation anthology, pastoral in tone." At the source-sighting stage this session both the author and the year turned out to be wrong. Corrected against the primary bibliographic record (Enzyklothek entry `4cc90c2c-442a-4744-9b3f-1427b4428440`; GND authority `101703465`; IA holding, below):

- **Author:** **Constantin Große** (not Alexander Grosse). Constantin Große was a late-19th-century Lutheran pastor and bibliographer. Alexander Grosse (1596–1654), the name in the memo, was an English Puritan divine — a different person, different confession, different language, wrong century for a German-language Fraktur imprint.
- **Year:** **1900** (not 1614). The book is a modern scholarly guide *to* the devotional literature of the 16th–18th centuries — Große's own century-of-composition is 1900, though his subject-matter runs from the 16th century forward. The "1614" of the memo appears to have taken the earliest date of the subject-matter for the imprint date of the work itself.
- **Genre:** **Wegweiser** — a scholarly *guide* / bibliographic-and-biographical survey of Lutheran devotional literature. Not a patristic-consolation anthology. This shifts the work from primary-source to secondary-source, which has consequences for tranche design and (possibly) for repo categorisation — see "Categorisation question" below.

The directory has been renamed from `grosse-alten-troester-1614/` to `grosse-alten-troester-1900/` in this same commit; the README has been updated to match.

## The source, in one sentence

Constantin Große, *Die alten Tröster: Ein Wegweiser in die Erbauungslitteratur der evangelisch-lutherischen Kirche des 16. bis 18. Jahrhunderts*, Hermannsburg: in Kommission bei der Missionshandlung, 1900 — a ~700-page Lutheran-confessional survey of three centuries of Evangelical-Lutheran devotional literature, published from the Hermannsburg mission-house and squarely within the 19th-century Missouri/Hermannsburg confessional-revival orbit.

## Full title (as printed on the 1900 title page — to be verified verbatim against `sources-original/ia-1900/` scan)

*Die alten Tröster: Ein Wegweiser in die Erbauungslitteratur der evangelisch-lutherischen Kirche des 16. bis 18. Jahrhunderts.*

("The Old Comforters: A Guide to the Devotional Literature of the Evangelical-Lutheran Church of the 16th through 18th Centuries.")

## Why the 1900, and no other edition

The 1900 Hermannsburg imprint is Große's own first — and, to the best of the bibliographic record, only — edition. There is no expanded second edition, no posthumous recension, no editorial tradition analogous to the Flacius *Catalogus* problem. The text-base question is therefore trivial: translate the 1900.

## Digital sources — sighted 2026-08-30

### Primary text-base: Internet Archive holding of the 1900 Hermannsburg imprint

**Identifier:** `diealtentroeste00grosgoog` (Google-Books-derived scan, `_goog` suffix)

**Detail page:** `https://archive.org/details/diealtentroeste00grosgoog`

**Bibliographic record (from IA metadata):**

- Title: *Die alten Tröster: ein Wegweiser in die Erbauungslitteratur der evang.-luth. Kirche des 16. bis 18. Jahrhunderts*
- Creator: Grosse, Constantin
- Date: 1900
- Publisher: Hermannsburg : in Kommission bei der Missionshandlung
- Collation: vi + [2] + 700 pp + [1] leaf of folding table
- Total scan pages: 740

**Format availability:**

- **PDF** (facsimile, ~41.8 MB)
- **PDF with searchable text layer** (~16 MB)
- **EPUB**
- **Plain text** (Tesseract 5.0.0 OCR, ~1.1 MB)
- **JP2 images** (~47.1 MB)
- **CHOCR / HOCR** (page-coordinate OCR, ~15/28 MB)

**OCR quality (as reported by IA metadata):** Tesseract 5.0.0 with Fraktur script detection; German-Fraktur confidence **0.9596**; page-number confidence 0.9142. This is at the high end of Fraktur OCR quality — clean 20th-century printing of Fraktur is considerably better than 17th-century Fraktur imprints. Even so, the workflow rule holds: **verify paragraph by paragraph against the JP2 image before committing English prose.** OCR ≠ text.

### Secondary bibliographic references

- **Google Books** scan: `books.google.com/books?id=s9cMAAAAIAAJ` (same underlying scan as the IA `_goog` item; IA is the working handle).
- **Enzyklothek** entry (a specialist bibliography of encyclopaedic / reference works): `https://enzyklothek.de/en/werk/grose-1900-%E2%80%93-die-alten-troster-4cc90c2c-442a-4744-9b3f-1427b4428440/`. Cites the work as a devotional-literature bibliography, cross-references John Lassenius.
- **GND** authority record: `101703465` (Deutsche Nationalbibliothek).
- **VD17 / VD18** — not applicable (1900 imprint; VD17 covers 1601–1700; VD18 covers 1701–1800).

## Structure of the 1900 — SIGHTED 2026-08-30 against IA OCR text

Sighted against the IA plain-text OCR of the 1900 imprint (`sources-original/ia-1900/diealtentroeste00grosgoog_djvu.txt`) at the volume's back-of-book Inhaltsverzeichnis. The book's arrangement is **chronological by three great periods (Zeitalter), with biographical-portrait entries on the individual writers within each period-and-region.** Detailed structure:

| Segment | Approx. pp | Content |
|:---|---:|:---|
| Title page | — | Die Alten Tröster / Ein Wegweiser… / Herausgegeben von Constantin Große, Pastor in Sora b[ei] [place — Fraktur OCR unclear, likely a Saxon village near Ostrau/Oschatz/Nossen; to sight against JP2] / Hermannsburg 1900 / in Kommission bei der Missionshandlung |
| Vorwort (Author's foreword) | iii–vi | Große's account of the book's genesis in a 1896 exchange in the *Sächsisches Kirchen- und Schulblatt* (Nr. 45, 47, 49) with Diakonus P. König of Hirschfelde, and the widening of the initial *Verzeichnis der Gebetslitteratur unserer Alten* into a proper Wegweiser. Signed "Der Verfasser" |
| External Preface | [vii–viii] | Preface by **D. Fr. Hashagen** of Rostock, signed *am Reformationsfeste 1899* — endorses the volume as a "lebenswarme Einführung in die Erbauungsliteratur". D. Fr. Hashagen was a Rostock churchman |
| **Einleitung** | 1–18 | Große's introduction to the concept of *Alte Tröster* — who the "old comforters" are, why they matter, the definition of *Erbauungsliteratur*, the chronological cut-off at ~1800 (rationalism), the biographical-and-generic method of the survey, cross-references to Delitzsch, Beck, Franke on the value of the tradition |
| **I. Das Reformationsjahrhundert 1500–1550** | 19–85 | *The Reformation Century.* |
| &nbsp;&nbsp;&nbsp;a) Die Reformationszeit (Allgemeiner Überblick) | 19– | General overview |
| &nbsp;&nbsp;&nbsp;2. Luther und seine Bedeutung für die Erbauungslitteratur | 19–65 | *Luther and his Significance for Devotional Literature* — the largest single entry in the volume; Luther's writings pp. 38–65 |
| &nbsp;&nbsp;&nbsp;3. Die Mitarbeiter Luthers und die Frömmigkeit | 65– | Luther's fellow-workers |
| &nbsp;&nbsp;&nbsp;4. Urbanus Rhegius | ~72 | |
| &nbsp;&nbsp;&nbsp;5. Johannes Brießmann | ~76 | |
| &nbsp;&nbsp;&nbsp;6. Veit Dietrich | ~77 | |
| &nbsp;&nbsp;&nbsp;7. Johann Spangenberg + [excursus: Jakob Andreä pp. 84–85] | 78–85 | |
| **I b) Die nachreformatorische Zeit 1550–1600** | 86–132 | *The post-Reformation era.* |
| &nbsp;&nbsp;&nbsp;1. Allgemeines / 2. Zur Frömmigkeit | 86–88 | |
| &nbsp;&nbsp;&nbsp;3. Girolamo Savonarola | 89–90 | Note: Große includes Savonarola (†1498) despite lying just before his chronological window, presumably as a witness read across Lutheran devotional lines |
| &nbsp;&nbsp;&nbsp;4. Stephan Praetorius | 90–92 | Not the *Syntagma Musicum* Praetorius; the Braunschweiger devotional writer (~1536–1603) |
| &nbsp;&nbsp;&nbsp;5. Andreas Musculus | 93–106 | The Brandenburg Lutheran (†1581) — cross-refs to the corpus [[scholastic-lutherans-program]] Musculus *Loci Communes* entry |
| &nbsp;&nbsp;&nbsp;6. Johann Habermann | 106–122 | Author of the widely-printed *Betbüchlein* (1567) |
| &nbsp;&nbsp;&nbsp;7. Betbuch Christiani | 122–123 | |
| &nbsp;&nbsp;&nbsp;8. Münsinger von Frundeck | 124– | |
| &nbsp;&nbsp;&nbsp;9. Michael Sachs et al. | 124–132 | |
| **II. Das Zeitalter der luth. Orthodoxie und des sich innerhalb ihrer beginnenden Pietismus** | 133–322 | *The age of Lutheran Orthodoxy and of pietism beginning within it.* |
| &nbsp;&nbsp;&nbsp;a) 1600–1648 (die luth. Orthodoxie) | 133–218 | |
| &nbsp;&nbsp;&nbsp;&nbsp;1. Allgemeines / 2. Zur Frömmigkeit | 133–140 | |
| &nbsp;&nbsp;&nbsp;&nbsp;3. Philipp Nicolai (1556–1608) | 141– | |
| &nbsp;&nbsp;&nbsp;&nbsp;4. Georg Dedeken | | |
| &nbsp;&nbsp;&nbsp;&nbsp;5. Valentin Wudrian | 148–150 | |
| &nbsp;&nbsp;&nbsp;&nbsp;6. Martin Statius | 151–155 | *Mark Brandenburg region* |
| &nbsp;&nbsp;&nbsp;&nbsp;7. Johannes Kolerus | | *Posen, Silesia region* |
| &nbsp;&nbsp;&nbsp;&nbsp;8. Valerius Herberger | 156–171 | |
| &nbsp;&nbsp;&nbsp;&nbsp;9. Johann Heermann | 172–176 | *Mitteldeutschland region* |
| &nbsp;&nbsp;&nbsp;&nbsp;10. Johann Arndt + [excursus: Jakob Böhme] | 177–197 | *Sachsen, Thüringen region* — the Arndt entry is Große's second-largest after Luther |
| &nbsp;&nbsp;&nbsp;&nbsp;11. Johann Gerhard | ~197–211 | |
| &nbsp;&nbsp;&nbsp;&nbsp;12. Johann Matthäus Meyfart | 212–218 | |
| &nbsp;&nbsp;&nbsp;b) Die Blütezeit der lutherischen Erbauungslitteratur 1648–1680 | 218–306 | *The flowering of Lutheran devotional literature.* |
| &nbsp;&nbsp;&nbsp;&nbsp;A. Die Großen (Lütkemann, Müller, Scriver et al.) | 220–284 | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Joachim Lütkemann | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Heinrich Müller | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Christian Scriver | 252–277 | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6. Johannes Lassenius (1636–1692) | 277–284 | Danish-German pastor — the Enzyklothek keyword |
| &nbsp;&nbsp;&nbsp;&nbsp;7. Georg Fibicius (?) | | Vertreter der Erklärer (Bible commentators) |
| &nbsp;&nbsp;&nbsp;&nbsp;8. Württemberger Summarien / Anker & Bibel | 288–291 | Vertreter der Bibelwerke |
| &nbsp;&nbsp;&nbsp;&nbsp;B. Vertreter der Erbauungsschulantien / Gärtner et al. | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9. Johann Rittmeyer | 291–297 | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10. Johann Quirsfeld | 297–301 | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;11. August Pfeiffer | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;12. Johann Michael Dilherr | 302–306 | |
| &nbsp;&nbsp;&nbsp;c) Der Ausgang der nüchternen luth. Erbauungslitteratur und Anfang der pietistischen Heiligungslitteratur 1680–1700 | 306–322 | |
| &nbsp;&nbsp;&nbsp;&nbsp;1. Allgemeines / 2. Frömmigkeit im Anfang des Pietismus | | |
| &nbsp;&nbsp;&nbsp;&nbsp;3. Philipp Jakob Spener | | |
| &nbsp;&nbsp;&nbsp;&nbsp;4. Johann Kaspar Schade | 317– | |
| **III. Das Zeitalter der Blüte des Pietismus, der zu Ende gehenden orthodoxen Erbauungslitteratur, und des Übergangs zur rationalistischen Litteratur** | 322–597 | *The age of pietism's flowering, the ending of orthodox devotional literature, and the transition to rationalist literature.* |
| &nbsp;&nbsp;&nbsp;a) Die Blüte der pietistischen Heiligungslitteratur 1700–1750 | 322– | |
| &nbsp;&nbsp;&nbsp;&nbsp;1–3. Allgemeines / Charakter des Pietismus / Frömmigkeit der letzten Orthodoxen | | |
| &nbsp;&nbsp;&nbsp;&nbsp;A. Die kirchlich gerichteten Pietisten | 336–360 | *Church-oriented pietists* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Johann Friedrich Starck / 5. Fresenius / 6. Rambach / 7. Christoph Starke / 8. Basler Bibel (reformiert) | | |
| &nbsp;&nbsp;&nbsp;&nbsp;B. Die Halle-Gruppe (Franckesche) | 361–391 | *The Halle circle around A. H. Francke* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9. Francke / 10. Bogatzky / 11. Steinmetz / 12. Reuß / 13. Porst | | |
| &nbsp;&nbsp;&nbsp;&nbsp;C. Radikale / Separatisten (Kreuzberg, G. Arnold) | | |
| &nbsp;&nbsp;&nbsp;&nbsp;D. Die Brüdergemeinde (Herrnhut): Zinzendorf, Spangenberg, Gerhard, Cochius | | |
| &nbsp;&nbsp;&nbsp;&nbsp;E. Die Württemberger Pietisten 1700–1900 | 419–481 | Hedinger, Cramlich, Urlsperger, Rieger, Bengel, Steinhofer, Baumann, von Ottenhein, Hiller, Burk, Brastberger, Roos, Storr |
| &nbsp;&nbsp;&nbsp;&nbsp;F. Terstegen (Zerniers Anhang) | 519–527 | *Cross-referenced by Große to note that Terstegen, though Reformed, was received across confessional lines* |
| &nbsp;&nbsp;&nbsp;&nbsp;G. Vertreter der luth. Orthodoxie [im Pietismus-Zeitalter] | 530–572 | Neumann, Schmolck, Cober, Woltersdorf, Nathanael, Vlock, Schinmeyer, Schauberger |
| &nbsp;&nbsp;&nbsp;b) Der Ausgang der Erbauungslitteratur, letzte Ausläufer der Iuth. Orthodoxie, Übergang zum Rationalismus, Rationalismus selbst 1750–1800 | 490–597 | |
| &nbsp;&nbsp;&nbsp;&nbsp;A. Letzte Ausläufer der luth. Orthodoxie | 490–503 | Goeze, Erhardt, Claudius |
| &nbsp;&nbsp;&nbsp;&nbsp;B. Supranaturalisten | 503–585 | Lavater, Nies, Stillings *Chatelein* (?) |
| &nbsp;&nbsp;&nbsp;&nbsp;C. Die Rationalisten | 585–597 | J.J. Zollikofer, Zschokke, Witschel |
| &nbsp;&nbsp;&nbsp;8. Abschließende Betrachtungen und Ausblick in das 19. Jahrhundert | 597– | *Closing reflections and outlook onto the 19th century* |
| **Anhang I — Ausländisches und Mittelalterliches** | ~600–650 | *Appendix 1.* |
| &nbsp;&nbsp;&nbsp;I. Englische Erbauungsschriften: Rutherford, Baxter, Bunyan, Wilcox, Drelincourt | | |
| &nbsp;&nbsp;&nbsp;II. Mittelalterliche Postillenliteratur bei den Lutheranern: Tauler, Ruusbroec, *Theologia deutsch*, Thomas à Kempis | | |
| &nbsp;&nbsp;&nbsp;III. Sammlungen alter asketischer Stücke, bes. Gebete in Gebetbüchern | | |
| **Anhang II — Tabellarische Übersichten** | ~660–680 | I. Overview of newly-issued Erbauungsschriften by subject; II. Zeittafel — the folding-leaf chronology of the most important devotional books |
| **Nachträge und Berichtigungen** | ~688– | Author's addenda and corrections |
| **Inhaltsverzeichnis** | ~700 | Table of contents at back |

The arrangement is now fixed. **Große treats ~90 individually-portrayed writers and multiple additional collective entries, arranged in three great chronological periods with sub-periods, with regional sub-groupings within each sub-period.** The volume's total scale corresponds to a Loci-length primary source (~700 pp), but its per-entry granularity is high — most biographical portraits are 3–20 pp — which allows tranche cuts at natural section joins.

## What kind of book is this — in relation to the corpus

**A Wegweiser.** A guide. Not a primary source but a scholarly companion to the primary sources — biographical sketches, bibliographic notices, generic classifications, and evaluative-confessional commentary on the writers whose works the *Scholastic Lutherans* program itself is translating. Große surveys, from Hermannsburg in 1900, the very tradition of which the corpus is now — in this program — the working translator.

This has two consequences for how the volume functions inside the 22-work corpus:

1. **As a translation target it is genre-different.** The English of a Wegweiser is expository, biographical, evaluative — not the doctrinal register of Chytraeus, not the anthology-and-frame register of Flacius, not the systematic register of Quenstedt. Register: measured 19th-century scholarly-German brought into scholarly modern English; not "reverent-but-not-archaising" (which is the primary-source rule) but "accurate-and-clear" for a survey / reference volume.
2. **As reference material it doubles the corpus.** For every primary Lutheran devotional writer the corpus already touches — Musculus in Dogmatics, Balduin in Pastoral, Selnecker in Dogmatics, and any Arndt / Gerhard *devotional* material that comes into range as the program advances — Große's entry on that writer becomes a ready secondary-source pointer, addressable by page-number.

This second function is the strategic value of the volume for the whole program, independent of "Tier 1 short and high-utility" reasoning that put it here in the sequencing. Große's 700-page guide is the corpus's own reference companion, translated into the corpus's own working English.

## Categorisation question — open, for Cheri to decide

The book is currently at `pastoral/grosse-alten-troester-1900/` because that is where the parallel-work coordination memo placed it. On the corrected identification, it may belong better under `secondary/` — alongside Wallmann's 1961 *Der Theologiebegriff bei Gerhard und Calixt* — since both are modern scholarly guides *to* Lutheran tradition rather than primary-source Lutheran works. Left in `pastoral/` for now (unchanged directory move-of-category would cascade through the README table, the program-memory Tier list, and the coordination memo); flagged here for a small follow-up decision.

**If moved:** re-slug `pastoral/grosse-alten-troester-1900/` → `secondary/grosse-alten-troester-1900/`, update README table, update program memory Tier 1 list to promote Balduin or another Tier 2 candidate into Tier 1's third-slot.

**If kept:** the argument for `pastoral/` is that a survey of devotional literature is still, thematically, pastoral in orientation — its subject is *Trost*, *Andacht*, *Trostgebete*, the work of consolation. A librarian might well shelve it either way.

## OCR expectations

- **Format:** 1900 Hermannsburg imprint. German Fraktur, but late — twentieth-century-quality typography, well-set, no archaic printer-abbreviation apparatus of the 17th-century sort.
- **Expected OCR quality (Tesseract 5.0.0 Fraktur mode as run by IA):** high. IA reports German-Fraktur confidence 0.9596 for this item — meaningfully higher than the 60–80% floor the workflow assumes for older Fraktur imprints.
- **Complications:**
  - **Long-*s*** (ſ) — silently modernised to round *s* per the master convention.
  - **Umlauts:** preserved in German quotations, standard modern spelling in citation.
  - **ß** preserved in German source citations, not in English body.
  - **Fraktur-*k* vs Antiqua-*k***, **Fraktur-*w*** — should be OCR-clean at 96% but eye-verify at each Latin quotation, where the OCR is likelier to have switched-mode errors.
  - **Latin quotations** from patristic and Reformation-era sources — inside a Fraktur setting these often print in Antiqua, and the OCR sometimes misreads the type-shift. Verify carefully.
  - **Proper-name spelling variance** — 1900 spelling conventions for 16th–17th-century proper names may differ from modern editorial convention (Große spells *Chytraeus* as *Chyträus*, etc.). Preserve his form on first citation; modern form in English body per master convention.

## Body-download decision

The full 700-page IA scan at 41.8 MB (facsimile PDF) is manageable. The JP2 image set (47.1 MB) is our reference layer against which OCR is verified. Options:

- **(A) Full download at kick-off.** Pull the searchable-text PDF (~16 MB) and the plain-text OCR (~1.1 MB) into `sources-original/ia-1900/`; leave the JP2s as a lazy-fetch for Tranche 1. Gitignore the binaries.
- **(B) Tranche-by-tranche.** As with Flacius, pull each tranche's slice at that tranche's kick-off.

**Recommendation:** (A) for the searchable PDF and the plain-text OCR (they are lightweight and enable structural scan-through immediately); (B) for the JP2 image layer per tranche. Add `sources-original/**/*.pdf`, `*.jp2`, `*.txt`, `*.epub` to `.gitignore` before pulling.

## Tranche plan — re-cut against sighted structure 2026-08-30

Total: ~700 pp body + ~8 pp front matter + folding table. Re-cut into **nine tranches** by Große's own three-period × sub-period × regional-group arrangement. Page-ranges are from the sighted Inhaltsverzeichnis.

- **Tranche 0 — Kick-off + source sighting** (2026-08-30, commit `82b8356` + subsequent). Scaffold, notes with two corrections, TN, terms.yaml seed, directory rename, README update. IA OCR pulled to `sources-original/ia-1900/`. Structure sighted against IA OCR at back-of-book Inhaltsverzeichnis. ✅
- **Tranche 1 — Front matter + Einleitung** (this session, in progress). Title page verbatim. Vorwort by Große. External preface by D. Fr. Hashagen. Einleitung pp. 1–18 — Große's account of who the *alten Tröster* are, why they matter, definition of *Erbauungslitteratur*, method-and-scope statement. Mid-checkpoint build not spent yet (preserve for Tranche 4 or 5). Deliverable: reader can pick up the volume and understand what Große is doing.
- **Tranche 2 — I. Das Reformationsjahrhundert 1500–1550 (pp. 19–85).** Luther (pp. 19–65, the largest single entry) + Luther's fellow-workers (Rhegius, Brießmann, Dietrich, Spangenberg, Andreä-excursus). ~67 pp source, likely ~40–50 pp English.
- **Tranche 3 — I b) Die nachreformatorische Zeit 1550–1600 (pp. 86–132).** Savonarola, Stephan Praetorius, Musculus, Habermann, Betbuch Christiani, Münsinger, Michael Sachs. ~46 pp source. Cross-refs to the corpus Musculus target.
- **Tranche 4 — II a) Die luth. Orthodoxie 1600–1648 (pp. 133–218).** Nicolai, Dedeken, Wudrian, Statius, Kolerus, Herberger, Heermann, Arndt (pp. 177–197, second-largest entry), Böhme-excursus, Gerhard, Meyfart. ~86 pp source. **Mid-checkpoint build (build #1 of 2)** — natural pause at the mid-century.
- **Tranche 5 — II b) Die Blütezeit 1648–1680 (pp. 218–306).** The great four: Lütkemann, Müller, Scriver, Lassenius; then Fibicius, Württemberger Summarien, Rittmeyer, Quirsfeld, Pfeiffer, Dilherr. ~88 pp source. The Lassenius entry is the one Enzyklothek highlighted.
- **Tranche 6 — II c) Der Ausgang der luth. Erbauungslitteratur & III a) opening 1680–1750 (pp. 306–420).** Spener, Schade — the pietism inflection point. Then III a) opens: the church-oriented pietists (Starck, Fresenius, Rambach, Ch. Starke, Basler Bibel) and the Halle circle (Francke, Bogatzky, Steinmetz, Reuß, Porst). ~115 pp source. **The pietism boundary — Große draws his sharpest confessional-Lutheran judgements here.** Preserve his placement, endnote modern re-assessments.
- **Tranche 7 — III a) continued: Radikale + Herrnhut + Württemberger + Terstegen + luth. Orthodoxie im Pietismus-Zeitalter (pp. 419–572).** Kreuzberg, G. Arnold, Zinzendorf, Spangenberg; the Württemberger pietists (Hedinger through Storr — 13 portraits); Terstegen (Reformed, received across confessional lines — noteworthy editorial-caution); and the confessional-Lutheran remnant (Neumann, Schmolck, Cober, Woltersdorf, et al.). ~150 pp source.
- **Tranche 8 — III b) Der Ausgang 1750–1800 (pp. 490–597).** Goeze, Erhardt, Claudius — the last confessional Lutherans; Lavater, Nies — the Supranaturalists; Zollikofer, Zschokke, Witschel — the Rationalists; Große's closing reflections and 19th-c. outlook. ~107 pp source. **The confessional endpoint of the book.** Große's own century is the reception-context of every judgement here.
- **Tranche 9 — Anhang I + Anhang II + Nachträge + apparatus (pp. ~600–700).** English devotional literature (Rutherford, Baxter, Bunyan, Wilcox, Drelincourt); medieval Postillen-literature received across Lutheran lines (Tauler, Ruusbroec, *Theologia deutsch*, Thomas à Kempis); miscellaneous collections; Anhang II tabular overviews; Nachträge und Berichtigungen; the folding-leaf chronology-table (translate verbatim + build modern-typeset English facing table); Register (rebuilt from the master `terms.yaml` proper-name gazetteer accumulated over Tranches 2–8). **Final build (build #2 of 2).** Deliverable: volume-final PDF.

**Build cadence check:** ≤2 builds per work per workflow. Build #1 at end of Tranche 4 (~pp. 218 mid-Orthodoxie). Build #2 at end of Tranche 9 (volume-final).

## Editorial notes specific to this work

- **Fidelity to Große's own confessional stance.** Große writes from an explicitly Lutheran-confessional standpoint (Hermannsburg 1900 = late-19th-century confessional-Lutheran revival, missional, sympathetic to the American Missouri-Synod trajectory). His evaluations of individual writers — who is "sound," who "already inclines to pietism," who "veers toward mysticism" — are theologically located, not neutral. **Preserve his evaluations as his own.** The translator's voice does not adjudicate on his adjudications. If a note is warranted to flag a modern re-assessment, it lives in an endnote, flagged as our editorial addition — never inline.
- **The pietism boundary.** Große writes across the 16th–18th-century boundary at which Lutheran devotional literature debouches into pietism. He draws the boundary in specific places — Arndt (in?), Rambach (in?), Zinzendorf (out?). His placement of each writer is itself a theological argument. Translate the placement verbatim; note the modern historiographical position, where it differs, in an endnote.
- **Cross-reference with corpus works.** Where Große treats a writer whose own work is a Scholastic Lutherans translation target — Musculus (dogmatics), Balduin (casuistry), any Selnecker devotional — cross-reference the corpus entry in an endnote (`Cf. Musculus *Loci Communes*, translated in the Scholastic Lutherans dogmatics volume`). This is the volume's function-as-reference-companion made explicit.
- **John Lassenius.** The Enzyklothek record notes Lassenius (1636–1692, Danish-German Lutheran pastor and devotional writer) as a keyword — likely because Große devotes substantial attention to Lassenius in his 17th-century section. Lassenius is not currently in the 22-work corpus but is a candidate for future addition; note if Große's treatment of him warrants promotion.
- **Missional voice.** The Hermannsburg-Missionshandlung imprint is not incidental. Große writes as a churchman engaged in the missional-confessional Lutheran project of his own century — Louis Harms's Hermannsburg-Mission, sending Lutheran pastors to the Boer Republic and to India. The devotional writers he surveys are, for him, the theological ancestry of that missional project. His register is missional-pastoral, not academic-neutral. Preserve.

## Cross-references to sibling works in the corpus

- **[[chytraeus-catechismus-1594]]** — the just-completed Locus IX §9 (*duodecim consolationes Christianae*) is a direct thematic ancestor of Große's whole subject: Chytraeus's twelve Christian consolations are precisely the kind of devotional-consolation piece that Große surveys. Große likely discusses Chytraeus's *Catechesis* somewhere in his 16th-century section.
- **[[flacius-catalogus-testium-1556]]** (in-flight, polemics) — Flacius's *Catalogus* and Große's *Wegweiser* are structural cousins: both are Lutheran surveys arranging authors by chronological order under a confessional criterion. Flacius arranges witnesses against Rome; Große arranges witnesses of Lutheran consolation. The formal comparison is worth an endnote.
- **[[scholastic-lutherans-praetorius]]** — reference implementation for the whole workflow (typography, endnote style, Translator's Note schema).

## Coordination with parallel Scholastic Lutherans chats

- **Chytraeus** — COMPLETE + POLISHED 2026-08-30 (commit `2658f99` on `Cherireal7/scholastic-lutherans` private).
- **Flacius** — kick-off + source sighting 2026-08-30 (commits `9c1eb56` + subsequent). Different category (`polemics/`), different language (Latin), no per-work file collisions.
- **Quenstedt *Exercitationes*** — new parallel chat opening (per [[scholastic-lutherans-parallel-work-2026-08]]). Different category (`encyclopedias/`), different language (Latin), no per-work file collisions.
- **`shared/terms.yaml`** — shared. This work's entries live in a dedicated `# ─── PASTORAL / SECONDARY — Große, Die alten Tröster (1900) ───` section below the Flacius section-end marker; new tranche entries append below the Große section-end marker so parallel chats' additions do not interleave.
- **`shared/reference-custom.docx`** and **`shared/build.ps1`** — DO NOT modify from this chat. Locked at repo-init state.
- **`shared/editions.md`** — modern-critical-edition registry only. Große's 1900 Hermannsburg imprint is the work itself, not a modern re-edition of an earlier work, and therefore is documented here and in the TN, not in `editions.md`.

## Immediate next actions (Tranche 1 session)

1. Pull the IA searchable PDF and plain-text OCR into `sources-original/ia-1900/`. Add `sources-original/**/*.pdf`, `*.jp2`, `*.txt`, `*.epub` to `.gitignore` first.
2. Read the title page from the IA JP2 → verify the exact title-face and imprint. Replace the placeholder title-page in `review/*.md`.
3. Sight the table of contents. Cut the tranche plan (Tranches 2–N) to Große's own arrangement — chronological, thematic, or biographical.
4. Translate: Vorwort, dedication (if present), and Große's introduction of the *Erbauungslitteratur* concept.
5. Mid-checkpoint DOCX + PDF build (build #1 of 2). Commit.
6. Raise the [[scholastic-lutherans-parallel-work-2026-08]] correction with Cheri: the memo's Alexander-Grosse-1614-patristic-anthology identification needs updating to Constantin-Große-1900-Wegweiser. Also raise the categorisation question (`pastoral/` vs `secondary/`).

## Related

- [[scholastic-lutherans-program]] — corpus index (this work: was Tier 1 pastoral; may become secondary reference)
- [[scholastic-lutherans-parallel-work-2026-08]] — parallel-work coordination; **needs correction — author was Alexander, is Constantin; year was 1614, is 1900; genre was patristic-consolation anthology, is Wegweiser to Lutheran devotional literature**
- [[reference-scholastic-lutherans-workflow]] — pipeline, conventions, "never fabricate"
- [[reference-scholastic-lutherans-glossary]] — master glossary conventions
- [[scholastic-lutherans-praetorius]] — reference implementation
- [[chytraeus-catechismus-1594]] — reference implementation for a completed Scholastic-Lutherans volume
- [[flacius-catalogus-testium-1556]] — in-flight parallel work
