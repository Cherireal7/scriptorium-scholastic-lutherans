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

## Structure of the 1900 — provisional, from bibliographic description

Awaiting sighting of the actual title-page and table of contents against `sources-original/ia-1900/` scan. From the bibliographic collation (vi + [2] + 700 pp + folding table) and the work's stated scope (three centuries of Lutheran devotional literature), the *provisional* internal architecture is:

| Segment | Approx. pp | Content (to be confirmed at Tranche 1 sighting) |
|:---|---:|:---|
| Front matter — title, dedication, Vorwort | 8 (roman i–vi + [2]) | Author's preface, dedication, statement of purpose |
| Introduction — the tradition of Erbauungslitteratur | ? | Große's own account of what "devotional literature" means, why he surveys 16th–18th c., his organising principle |
| 16th-century writers | ? | Luther, Musculus, Selnecker, Herberger — the confessional-formation era |
| 17th-century writers | ? | Arndt, Gerhard, Heermann, Rist, Scriver, Lassenius — the flowering of Lutheran devotion; the pietist prelude |
| 18th-century writers | ? | Rambach, Bogatzky, Zinzendorf-adjacent — into the pietist century, with confessional-Lutheran boundary-drawing |
| Folding table | 1 leaf | Chronology / genealogy of the tradition — the map of the terrain |
| Index (Register) | ? | Alphabetical proper-name and topic index |

Große's arrangement — chronological by century, or thematic by devotional-genre (prayer-books, hymn-collections, meditations, funeral-consolations, catechetical exposition), or biographical-portrait-by-author — is the first structural question Tranche 1 must resolve against the sighted table of contents.

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

## Provisional tranche plan (to be revised against sighted structure)

Total: ~700 pp of body + ~8 pp front matter + folding table.

- **Tranche 0 — Kick-off + source sighting** (2026-08-30, this commit). Scaffold, notes with two corrections, TN draft, terms.yaml seed. Directory rename. README update. ✅
- **Tranche 1 — Front matter + Große's introduction.** Pull the IA text + PDF. Verify title page verbatim against JP2. Translate: dedication (if present), Vorwort, and the introductory chapter setting out Große's understanding of *Erbauungslitteratur* and his organising principle for the whole survey. Mid-checkpoint build (build #1 of 2). Deliverable: structural sighting complete, front matter finalised, tranche plan re-cut to Große's actual arrangement.
- **Tranches 2–N — Body, by Große's own sections.** Cut against his own arrangement once sighted. If chronological-by-century: three tranches (16th c., 17th c., 18th c.). If thematic-by-genre: cut per genre. If biographical-portrait-by-author: cut by author-block (probably 5–7 tranches given ~700 pp ÷ ~120 pp/tranche).
- **Final tranche — Folding table + Register (Index) + closing apparatus.** The folding-table chronology is the map of the whole tradition; translate its Fraktur inscription verbatim + build a matching modern-typeset English facing table for the final volume. Final build (build #2 of 2). Deliverable: volume-final PDF.

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
