# Flacius, *Catalogus Testium Veritatis* (1556) — Working Notes

Scholastic Lutherans working file. This is the operational scratchpad for the translation; the reader-facing Translator's Note lives at `review/flacius-catalogus-testium-1556.md`.

## The source, in one sentence

Matthias Flacius Illyricus, *Catalogus testium veritatis, qui ante nostram aetatem reclamarunt Papae*, Basel: Johannes Oporinus, 1556 — the *editio princeps* (1r folio), our chosen text-base to the exclusion of later expansions.

## Full title (from the 1556 title page — to be verified at source sighting)

*Catalogus testium veritatis, qui ante nostram aetatem reclamarunt Papae. Opus varia rerum, hoc praesertim tempore scitu dignissimarum, cognitione refertum, ac lectu cum primis utile atque necessarium.*

("A Catalogue of Witnesses to the Truth, who before our age spoke against the Pope. A work stocked with the knowledge of many things — chiefly, at this time, most worthy of being known — and above all useful and necessary to read.")

Authorship note: while Flacius signs the volume, much of the source-hunting through cathedral and monastery libraries was done by his collaborator **Marcus Wagner**. This is a fact to acknowledge in the Translator's Note under "what the author supplies" — we do not silently overwrite it.

## Why the 1556, not the 1562 / 1608 / 1666 recensions

- **1556 Basel (Oporinus)** — Flacius's own composition. Our base.
- **1562 Strasbourg / Basel reprint** — cosmetic.
- **1597 Frankfurt (Simon Goulart)** — Reformed hands. Adds anti-papal witnesses of Goulart's own selection; the book acquires a Reformed edge Flacius never gave it.
- **1666–67 Frankfurt (2 vols)** — most-cited historically, but by then the book is a Goulart–Wittenberg palimpsest three editors removed from Flacius.

We translate **Flacius**, not the tradition of the book. That means the *editio princeps*.

## Digital sources — to consult and verify before first-chapter work

Candidates (URLs and identifiers to be resolved when online):

| Repository | What to look for | Notes |
|:---|:---|:---|
| Internet Archive | search `catalogus testium veritatis 1556` and `Flacius` | Expect several scans; check OCR completeness and scan resolution before committing. |
| BSB Munich | VD16 lookup for the 1556 Basel imprint | Often the best-scanned facsimile for 16th-c. German-region Latin folios. |
| VD16 | Flacius Illyricus → *Catalogus testium* | The German bibliographic registry for 16th-c. imprints; will supply canonical shelf-marks. |
| PRDL | Flacius Illyricus, Matthias | The Post-Reformation Digital Library aggregates several scans by author. |
| HAB Wolfenbüttel | Flacius Illyricus catalog | HAB often holds the cleanest Reformation-era Latin scans. |
| Google Books | `catalogus testium veritatis 1556` | Frequently the fastest to search full-text against, though scan quality varies. |

**Do not begin body-text drafting until at least one scan is in `sources-original/` and paired with its OCR (`_djvu.txt`, or extracted to `.txt`).** Praetorius rule ([[reference-scholastic-lutherans-workflow]] · "Never fabricate"): every English claim must trace to a source paragraph.

## OCR expectations

- **Format:** 1556 Basel folio, printed in Antiqua Latin.
- **Expected OCR quality:** high (≥95% for 17th-c. Antiqua per workflow rubric; 1556 Antiqua slightly earlier but comparable). No Fraktur.
- **Complications:** printer's abbreviations (`q̃ = quam`, macrons for `n`/`m`, `p̄ = per`), long-*s* (silently modernised per convention), some early-modern `v/u` and `i/j` variation (normalised per convention). Greek quotations (from Chrysostom et al.) may be handled poorly by OCR — verify by eye.

## Structural knowns and unknowns

**Known (general shape, from historical description — to be verified at source sighting):**
- A preface / *Praefatio* by Flacius.
- Possibly a dedication (the *editio princeps* dedications need to be sighted; the 1562 and later editions carry different paratexts).
- The body: several hundred named "witnesses" (individuals, groups, councils, texts) who anticipated Reformation critique of Rome, arranged broadly chronologically from the sub-apostolic era through the mid-fifteenth century.
- An index / *Index rerum et personarum* at the end.

**Explicitly unknown until the scan is in hand:**
- Whether the 1556 divides the material into books / *libri*, chronological centuries, or a single running catalogue. (Later expanded editions impose more elaborate divisions; the 1556's own scheme must be read off the source, not assumed.)
- Total folio-page count for this specific imprint.
- Whether the 1556 carries a dedicatee, and to whom.
- Whether Flacius's paratexts include a *Praefatio ad lectorem* separate from a dedication.

Do not fill these in from later editions. Read them off the 1556 title-page and preface pages when sighted.

## Provisional tranche plan (subject to structural revision on source sighting)

At ≈1,200 folio pages, this work is not a single volume. Plan for a multi-tranche release:

- **Tranche 0 — Kick-off (this session).** Notes, review scaffold, Translator's Note skeleton, glossary hook in `terms.yaml`. No body prose. MD-only, no build.
- **Tranche 1 — Paratexts.** Title page, dedication (if any), *Praefatio*, address to the reader. Roughly 40–80 folio pages equivalent. Ends with a mid-checkpoint build (build #1 of 2).
- **Tranche 2 — Ancient witnesses (sub-apostolic through Gregory the Great).** Witnesses from ca. 100–600 AD. Chrysostom against papal titles, Gregory against *universalis episcopus*, and the smaller patristic voices.
- **Tranche 3 — Early medieval witnesses (600–1000).** Bede, Alcuin, Claudius of Turin, and the surrounding voices.
- **Tranche 4 — High medieval witnesses (1000–1250).** Berengar of Tours, the Investiture-controversy voices, the twelfth-century critics.
- **Tranche 5 — Dissenting movements (1150–1350).** Waldensians, Cathars (Flacius's inclusion — a case that must be preserved and glossed, not silently excised), Fraticelli.
- **Tranche 6 — Late medieval to Reformation eve (1350–1500).** Wyclif, Hus, the Hussite circle, the fifteenth-century voices.
- **Tranche 7 — Index and final apparatus.** Final build (build #2 of 2). Ends the volume.

Tranches 2–6 are chronological *approximations*. Once the 1556 scan is in hand and Flacius's own division is legible, this plan is re-cut to match.

## Editorial notes specific to this work

- **The Cathar problem.** Flacius includes groups later confessional consensus (both Lutheran and Roman Catholic) regards as heterodox. He does so because his standard is *"reclamarunt Papae"* — spoke against the Pope — not doctrinal orthodoxy. Preserve his inclusion, translate faithfully, and gloss the confessional problem in an endnote at first appearance. Do not silently drop groups whose theology embarrasses.
- **Register of critique.** The book is polemical *and* historical. The tone in the paratexts is confessional-Lutheran; the tone inside individual witness-entries is closer to source-anthology (long Latin excerpts from the witness's own writings, framed by short Flacian introductions). Preserve both registers.
- **Marcus Wagner.** Acknowledge his collection-work on first mention in the Translator's Note. He is not the author, but he is the researcher.
- **Cross-reference with the hermeneutics paper.** Flacius's *Clavis Scripturae Sacrae* (1567) — his hermeneutical manual — is a separate work. This *Catalogus* is his historical–polemical work. The two are complementary but distinct. Endnotes may point to *Clavis* where relevant, but the *Catalogus* is the book in hand.

## Coordination with the parallel Chytraeus chat

- The Chytraeus catechism translation runs in a separate session in this same mega-repo.
- **No overlap in per-work files** — different category (`catechetical/` vs `polemics/`) and different work-slugs.
- **`shared/terms.yaml`** — shared. Both chats append. To keep merges clean, this work's entries append at the end of the file under a dedicated `# ─── POLEMICS — Flacius, Catalogus Testium (1556) ───` divider, well below wherever the Chytraeus chat is currently editing.
- **`shared/reference-custom.docx`** and **`shared/build.ps1`** — DO NOT modify from this chat. They are locked at repo-init state.
- **`shared/editions.md`** — modern-critical-edition registry only. Flacius's *editio princeps* is a *primary* source and is documented here in `notes.md` and in the review-file's Translator's Note, not in `editions.md`.

## Immediate next actions (post-kick-off session)

1. Locate and download the 1556 Basel Oporinus scan into `sources-original/` (PDF + `.txt` OCR).
2. Read the title page, dedication (if any), and *Praefatio* into the review file. Update the Translator's Note "text base" section with exact IA / VD16 identifiers.
3. Read off the internal division of the 1556 and revise the tranche plan in this file.
4. Begin Tranche 1 (paratexts) proper.

## Related

- [[scholastic-lutherans-program]] · corpus index (this work: Tier 3 polemic)
- [[reference-scholastic-lutherans-workflow]] · pipeline, conventions, "never fabricate"
- [[reference-scholastic-lutherans-glossary]] · master glossary conventions
- [[scholastic-lutherans-praetorius]] · reference implementation
- [[lutheran-hermeneutics-paper]] · student paper; Flacius appears there — *Clavis* not *Catalogus*, but the same author
