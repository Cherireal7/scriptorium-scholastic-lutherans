# Flacius, *Catalogus Testium Veritatis* (1556) — Working Notes

Scholastic Lutherans working file. This is the operational scratchpad for the translation; the reader-facing Translator's Note lives at `review/flacius-catalogus-testium-1556.md`.

**Session log:** kick-off scaffold 2026-08-30 (commit `9c1eb56`) · source sighting 2026-08-30 (commit `caa5c62`) · Tranche 1a paratexts translated 2026-08-30 (this file's current revision).

## The source, in one sentence

Matthias Flacius Illyricus, *Catalogus testium veritatis, qui ante nostram aetatem reclamarunt Papae*, Basel: Johannes Oporinus, 1556 — the *editio princeps* (folio), our chosen text-base to the exclusion of all later expansions.

## Full title (as printed on the 1556 title page — text-face to be transcribed verbatim from `sources-original/camena-1556/avl0001.jpg`)

*Catalogus testium veritatis, qui ante nostram aetatem reclamarunt Papae. Opus varia rerum, hoc praesertim tempore scitu dignissimarum, cognitione refertum, ac lectu cum primis utile atque necessarium.*

("A Catalogue of Witnesses to the Truth, who before our age spoke against the Pope. A work stocked with the knowledge of many things — chiefly, at this time, most worthy of being known — and above all useful and necessary to read.")

Authorship note: while Flacius signs the volume, much of the source-hunting through cathedral and monastery libraries was done by his collaborator **Marcus Wagner**. This is a fact to acknowledge in the Translator's Note under "what the author supplies" — we do not silently overwrite it.

## Why the 1556, not the 1562 / 1597 / 1666 recensions

- **1556 Basel (Oporinus)** — Flacius's own composition. Our base.
- **1562 Strasbourg / Basel reprint** — modest reprint; BSB shelfmark `bsb11203912` is a 1562 imprint (per IIIF manifest `navDate=1562-01-01`), NOT the 1556. Do not confuse.
- **1597 Geneva (Antoine Blanc)** — Simon Goulart's expanded recension in Reformed hands. Adds anti-papal witnesses of Goulart's own selection; the book acquires a Reformed edge Flacius never gave it. e-rara scan at `http://www.e-rara.ch/zup/content/titleinfo/1752559` (do not use as text-base).
- **1666–67 Frankfurt (2 vols)** — most-cited historically, but by then the book is a Goulart–Wittenberg palimpsest three editors removed from Flacius.

We translate **Flacius**, not the tradition of the book. That means the *editio princeps*.

## Digital sources — sighted 2026-08-30

### Primary text-base: CAMENA Mannheim (1556 Basel Oporinus)

**Base URL:** `http://mateo.uni-mannheim.de/camenahist/flacius1/jpg/`

**HTML index of the volume:** `http://mateo.uni-mannheim.de/camenahist/autoren/flacius_hist.html` (linked entry-list runs to `s1094`, i.e. 1,094 body pages after paratexts).

**URL scheme (sighted and downloaded 2026-08-30):**
- Paratexts: HTML page `as####.html` → image `avl####.jpg`. Range **`avl0001`–`avl0032`** (32 unnumbered folio pages of front matter).
- Body: HTML page `s####.html` → image `vl####.jpg`. Range **`vl0001`–`vl1094`** (1,094 numbered folio pages).
- Body-page HTML `s0001.html` navigates *from* `as0032.html` (its `prev` link), confirming the paratexts run exactly to `avl0032` and the body begins at `vl0001`.

**Local archive:** `sources-original/camena-1556/` contains 32 paratext JPGs (`avl0001.jpg`–`avl0032.jpg`) + one body sample (`vl0001.jpg`, the first page of the entry on St Peter), ~13 MB, all fetched with HTTP 200 and non-trivial file sizes. See "Body-download decision" below on whether/when to pull the full 1,094-page body.

**Format:** JPG facsimile images only. **CAMENA does not serve OCR text.** Extraction of Latin text from the JPGs (Tesseract, or manual paragraph-by-paragraph transcription against the image) is Tranche-1's first task.

### Secondary references

- **BSB Munich (Bayerische Staatsbibliothek), MDZ:** `bsb11203912` — this is the **1562** reprint (per IIIF manifest `navDate`), 107 canvases. Useful as a comparanda-witness for text-critical decisions, but *not* the *editio princeps*. IIIF manifest at `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb11203912/manifest`; per-page OCR (hOCR) available at `https://api.digitale-sammlungen.de/ocr/bsb11203912/<page>`.
- **HAB Wolfenbüttel:** holds a digitised 1556 copy at `http://diglib.hab.de`. One HAB physical copy is noted in scholarship as bearing **Flacius's own handwritten dedication to his patron Joachim von Alvensleben** — a copy-specific fact, not evidence about the *printed* dedicatee. Look up exact shelfmark and add to this file when confirmed.
- **PRDL** (`https://www.prdl.org/author_view.php?a_id=554`) — lists 220 titles of Flacius; the *Catalogus* entry there points primarily to the 1597 e-rara scan.
- **WorldCat OCLC 867400599** — bibliographic control number for the 1556 (`https://search.worldcat.org/title/catalogus-testium-veritatis/oclc/867400599`).

## Structure of the 1556 — sighted from CAMENA index

The 1556 is a **single running catalogue**, not divided into books or centuries. Its architecture:

| Segment | CAMENA HTML | CAMENA image | Approx. folio pp | Content |
|:---|:---|:---|---:|:---|
| Title page | `as0001.html` | `avl0001.jpg` | 1 | Full title, printer, year |
| Epistola Nuncupatoria (dedicatory epistle) | `as0003.html` | `avl0003.jpg` | 13 | Dedicatee to be transcribed |
| Praefatio (Flacius to the reader) | `as0016.html` | `avl0016.jpg` | 9 | The theological argument of the whole |
| Index rerum et personarum | `as0025.html` | `avl0025.jpg` | 8 | ~300+ indexed entries |
| **Body — the catalogue proper** | `s0001.html` – `s1094.html` | `vl0001.jpg` – `vl1094.jpg` | **1,094** | Single chronological run |

**Body sample points (from CAMENA link index):**
- `s0001` · **St Peter** (apostolic — Flacius begins with the Petrine primacy-refusal texts)
- `s0046` · Council of Nicaea (325 AD)
- `s0846` · **John Wycliffe** (†1384)
- `s0988` · **Girolamo Savonarola** (†1498)
- `s1094` · end of body (late 15th c. — details to sight)

**Witness count.** Contemporary bibliography reports **443 witnesses** (Tasca, "Il profilo biblico di Valdo di Lione…"; other sources round to "more than 400"). CAMENA's own indexed table lists ~300+ — the smaller number is because CAMENA indexes individual named entries, not sub-witnesses grouped under a single heading (e.g. a "Waldensian testimonies" run collates many).

**No visible internal division into books, centuries, or parts.** Flacius runs the material as one chronological stream. This is the shape of the *editio princeps*; the later Goulart recensions impose bookish superstructure that is not native to Flacius.

## Structural facts still to be transcribed from the images

Because CAMENA is images-only and the JPGs have not yet been OCR-ed, the following remain to be extracted verbatim in Tranche 1:

1. **Title page text-face** — the exact typography, ordering, printer's colophon phrasing (*Basileae, per Ioannem Oporinum, Anno M.D.LVI*, or a variant), any printer's device motto. Currently the working translation carries a plausible reconstruction; replace it with the sighted text.
2. **Epistola Nuncupatoria dedicatee.** The scholarship on the physical HAB copy names **Joachim von Alvensleben** as the recipient of Flacius's handwritten dedication in that specific copy — but the **printed** dedicatee could well be a different figure (a Duke of Saxony, an Elector, a Braunschweig prince — Flacius's patronage network in 1556 was broad). Do not assert Alvensleben as the printed dedicatee without sighting the salutation on `avl0003.jpg`.
3. **Epistola date and place.** The paratexts of the 1556 were signed at Magdeburg (where Flacius was based during the Centuries project) — but this needs sighting, not assumption.
4. **Praefatio structure** — whether it runs continuously or breaks into numbered sections.
5. **The Index** — its exact alphabetic vs chronological ordering, and whether it includes sub-entries under group-witnesses (Waldensians, Cathars, Fraticelli).
6. **Body-page 1094** — how the volume terminates. Colophon? Errata? Register of sheets?

## OCR expectations

- **Format:** 1556 Basel folio, printed in Antiqua Latin.
- **Expected OCR quality on a fresh Tesseract pass over the CAMENA JPGs:** high (≥95% for 16th-c. Antiqua when scan resolution is good — CAMENA's ~300-400 KB JPG per page is acceptable resolution). No Fraktur.
- **Complications:** printer's abbreviations (`q̃ = quam`, macrons for `n`/`m`, `p̄ = per`), long-*s* (silently modernised per convention), some early-modern `v/u` and `i/j` variation (normalised in citation), Greek quotations (from Chrysostom, Gregory the Great, etc.) — Greek OCR is unreliable, verify by eye.
- **Practical:** run Tesseract with `-l lat` on each JPG in `sources-original/camena-1556/`, cross-check against BSB 1562 OCR (hOCR available) for text-critical checkpoints, and — as with Praetorius Vol III — verify paragraph by paragraph against the image before committing English prose. Do not commit body prose the OCR of which has not been eye-verified.

## Body-download decision

The full 1,094-page body at ~350 KB per JPG is ~380 MB of image data. Options:

- **(A) Full download now.** One large batch pull into `sources-original/camena-1556/`. Enables offline OCR immediately. Storage cost material but manageable in a private repo (do not commit binaries — add `sources-original/**/*.jpg` to `.gitignore` when full pull happens).
- **(B) Tranche-by-tranche download.** Pull the JPGs for the segment about to be translated (e.g. the ancient witnesses, `vl0001`–`vl~150`) at the start of each Tranche session. Keeps the repo lean; requires online access at each tranche kick-off.
- **(C) IIIF-tile ingestion via a smarter fetcher.** Not applicable — CAMENA does not serve IIIF, only static JPG.

**Recommendation:** (B). Pull each tranche's slice at that tranche's kick-off, OCR and verify against image, translate, commit MD, discard JPGs at tranche-end (leaving only paratexts + a small reference set permanently archived). This mirrors the Praetorius workflow's discipline of not accreting binary source-material into the repo when the translation itself is the artefact.

## Provisional tranche plan (revised 2026-08-30 against sighted structure)

Total: 7 tranches, ~1,126 folio pages of source (32 paratexts + 1,094 body).

- **Tranche 0 — Kick-off** (2026-08-30, commit `9c1eb56`). Scaffold, notes, TN draft, terms.yaml seed. ✅
- **Tranche 0.5 — Source sighting** (2026-08-30, this revision). CAMENA URL scheme confirmed, paratexts locally archived. ✅
- **Tranche 1 — Paratexts** (`avl0001`–`avl0032`, ~32 pp). OCR + transcribe + translate title page, Epistola Nuncupatoria, Praefatio, and Index-header. Mid-checkpoint DOCX/PDF build (build #1 of 2). Deliverable: front matter ready for volume-final assembly.
- **Tranche 2 — Ancient witnesses** (`vl0001`–`vl~100`, roughly). Sub-apostolic through Gregory the Great. Peter, the earliest Fathers refusing papal titles, Chrysostom, Augustine on the keys, Leo I, Gregory I on *universalis episcopus*.
- **Tranche 3 — Early medieval witnesses** (~`vl100`–`vl~300`). Bede, Alcuin, Claudius of Turin, the Carolingian voices, the eastern comparanda where Flacius includes them.
- **Tranche 4 — High medieval witnesses** (~`vl300`–`vl~550`). Berengar of Tours, the Investiture-controversy voices, twelfth-century critics (Bernard where Flacius reads him against Rome, the schools).
- **Tranche 5 — Dissenting movements** (~`vl550`–`vl~800`). Waldensians, Cathars (Flacius's inclusion — preserved and glossed, per the editorial note), Fraticelli, and the fringe voices.
- **Tranche 6 — Late medieval to Reformation eve** (~`vl800`–`vl1094`). Wyclif (`vl846`), Hus, the Hussite circle, Savonarola (`vl988`), and closing witnesses. Final DOCX/PDF build (build #2 of 2). Deliverable: volume-final PDF.
- **Tranche 7 — Index and any closing apparatus.** The Index rerum et personarum is at `avl0025` in the printing (front-of-book), but is translated last as a rendered subset of the master `terms.yaml` polemics entries plus a proper-name gazetteer built during Tranches 2–6.

Page-boundaries are approximate. Sight the exact chronological turn-points from CAMENA and re-cut at each tranche kick-off.

## Editorial notes specific to this work

- **The Cathar problem.** Flacius includes groups later confessional consensus (both Lutheran and Roman Catholic) regards as heterodox. He does so because his standard is *"reclamarunt Papae"* — spoke against the Pope — not doctrinal orthodoxy. Preserve his inclusion, translate faithfully, and gloss the confessional problem in an endnote at first appearance. Do not silently drop groups whose theology embarrasses.
- **Register of critique.** The book is polemical *and* historical. The tone in the paratexts is confessional-Lutheran; the tone inside individual witness-entries is closer to source-anthology (long Latin excerpts from the witness's own writings, framed by short Flacian introductions). Preserve both registers.
- **Marcus Wagner.** Acknowledge his collection-work on first mention in the Translator's Note. He is not the author, but he is the researcher.
- **Cross-reference with the hermeneutics paper.** Flacius's *Clavis Scripturae Sacrae* (1567) — his hermeneutical manual — is a separate work. This *Catalogus* is his historical–polemical work. The two are complementary but distinct. Endnotes may point to *Clavis* where relevant, but the *Catalogus* is the book in hand.
- **Petrine opening.** Flacius begins the catalogue with **St Peter** (`vl0001`) — a deliberate choice. The apostle whom Rome claims as its first pope becomes, in Flacius's arrangement, the first witness *against* the papal claim. Preserve the polemical weight of this positioning; do not soften the framing.

## Coordination with parallel Scholastic Lutherans chats

- **Chytraeus** — COMPLETE + POLISHED as of 2026-08-30 (per [[scholastic-lutherans-program]] table). Pushed to `Cherireal7/scholastic-lutherans` (private). No further coordination needed.
- **Quenstedt** *Exercitationes* and **Grosse** *Die alten Tröster* — new parallel chats opening (per [[scholastic-lutherans-parallel-work-2026-08]]). Different categories (`encyclopedias/` and `pastoral/`); no per-work file collisions.
- **`shared/terms.yaml`** — shared. Both other chats will append. This work's entries live in a dedicated `# ─── POLEMICS — Flacius, Catalogus Testium (1556) ───` section below the Chytraeus completion marker; new tranche entries append below the Flacius section-end marker so parallel chats' additions do not interleave.
- **`shared/reference-custom.docx`** and **`shared/build.ps1`** — DO NOT modify from this chat. Locked at repo-init state.
- **`shared/editions.md`** — modern-critical-edition registry only. Flacius's *editio princeps* is a *primary* source and is documented here and in the TN, not in `editions.md`.

## Tranche 1a — done 2026-08-30

Achieved without Tesseract by reading the CAMENA JPGs directly with Claude's vision (Read tool on the local JPG). This route is **markedly cleaner** for 16th-c. Antiqua than a Tesseract pass would be — no long-*s* / *v-u* / *i-j* / macron corruption, ligatures preserved, ornamental initials handled sensibly. Tesseract is not needed for CAMENA paratexts, and probably not for the body either.

- **Title page** (`avl0001.jpg`) — transcribed verbatim into `review/*.md`. Confirmed: no printed year on title-face (year 1556 sourced from colophon per bibliographic registers); scripture epigraph = 3 Reg 19 (= 1 Kings 19:18) paired with Rom 11:4 (the 7,000 who did not bow to Baal); "Cum Praefatione Mathiae Flacii Illyrici" line preserved.
- **Provenance stamps** noted on `avl0001` and `avl0002`: MS "Coll. Soc. Iesu Molshem" (Jesuit College of Molsheim, Alsace) + purple stamps "Grossherzogliche Gymnasiums-Bibliothek" and "BIBLIOTHEK DESBILLONS MANNHEIM" (Bibliothek Desbillons of the Bibliotheca Palatina, Mannheim — CAMENA's own provenance). The Molsheim ownership is a nice historical irony: an anti-papal Flacius in a Jesuit college library.
- **Epistola Nuncupatoria** (`avl0003`–`avl0015`, 13 pp) — dedicatee **CONFIRMED as the three Ernestine Dukes of Saxony**: John Frederick II "the Middler" (†1595), John William (†1573), John Frederick III "the Younger" (†1565), the sons of the deposed Elector John Frederick I "the Magnanimous" (†1554). No date or place at the subscription — unusual for a 16th-c. dedication; noted as such in endnote 16. Opening 5 pp (`avl0003`–`avl0007`) + closing 2 pp (`avl0014`–`avl0015`) translated in full; middle 6 pp (`avl0008`–`avl0013`) explicitly gap-marked and deferred to **Tranche 1b**.
- **Praefatio** (`avl0016`–`avl0024`, 9 pp) — **translated in full**. Theological arc identified: Elijah typology (avl0016) → the "sifting" for perpetual consolation (avl0017) → the Roman continuity-sophism stated verbatim (avl0017) → OT and NT parallels of the "novelty" charge (avl0018–0019) → the auditory definition of the true Church via John/Luke catena (avl0020) → the doctrinal reply against Rome's word-despite (avl0021) → the historical schema (200 pure / 300 gradually corrupting / 600 as terminus at which papal system settles) with critical use of the great Fathers (avl0022) → programmatic thesis (avl0023) → closing crowd-source appeal to correspondents to submit further witnesses from local archives (avl0024). The crowd-source mechanism is the ancestor of the 1562 / 1597 enlargements.
- **Index rerum et personarum** (`avl0025`–`avl0032`, 8 pp) — structure sighted (alphabetical, two columns per folio, source-witness page-numbers keyed to body pagination). A representative first-column run of A-entries transcribed into the review file; index proper is a Tranche 7 build-out from the accreted master glossary and proper-name gazetteer.
- **Endnotes** — 40 endnote entries added to the `# Notes` section covering: scripture citations (Vulgate + English, with Rom 11's use of 1 Kings 19), the three dedicatees identified (with the University of Jena 1558 sequel), all patristic references keyed to PL/PG, Luther's title *Doctor Martinus piae memoriae*, the Interim horizon, the Trent parallels (Session IV on Scripture-and-Tradition; the Index Librorum Prohibitorum), the Smalcald Articles' identification of the Papacy with Antichrist, the Magdeburg Centuries connection.
- **Glossary** — 8 new lemmas added to `shared/terms.yaml` under the Flacius POLEMICS section (`romani_baalis`, `septem_millia`, `sanctus_helias`, `cribratio`, `anathema_maranatha`, `desolationum_abominationes`, `interim`, `piae_memoriae`). Original 10 seed lemmas' `first_use` fields updated against sighted attestations; `universalis_episcopus` moved to "body — Gregory the Great entry (Tranche 2)" since it does not occur in the paratexts.

## Tranche 1b — outstanding

1. Read `avl0008.jpg` through `avl0013.jpg` (six pages, dedication middle). Translate. Splice into the `## The Epistola Nuncupatoria` section of `review/*.md`, replacing the current `[Editorial note. The following six folio pages…]` gap-marker.
2. Sight the volume colophon (last body page, at or near `vl1094`) → confirm the printed year *1556* and the exact colophon-face wording; update endnote 2 accordingly.
3. Read the full Index `avl0025.jpg`–`avl0032.jpg`. Extract the full alphabetical roster of witnesses with their source-page-numbers. Save as `sources-original/camena-1556/index-transcript.md` (gitignored under `**/sources-original/`). This roster is the working spine for Tranche 2's chronological re-ordering.
4. Mid-checkpoint DOCX + PDF build (build #1 of 2). Commit.

## Immediate next actions (post-Tranche 1a session)

**For the very next session** — either (a) Tranche 1b as above, or (b) begin Tranche 2 body work (ancient witnesses, `vl0001` onward, starting with St Peter and running through Gregory the Great). The Praefatio's theological framework is now in hand; Tranche 2 body work is unblocked. Choice depends on how much cleanup vs new work Cheri prefers per session.

## Related

- [[scholastic-lutherans-program]] · corpus index (this work: Tier 3 polemic)
- [[scholastic-lutherans-parallel-work-2026-08]] · Quenstedt + Grosse concurrent
- [[reference-scholastic-lutherans-workflow]] · pipeline, conventions, "never fabricate"
- [[reference-scholastic-lutherans-glossary]] · master glossary conventions
- [[scholastic-lutherans-praetorius]] · reference implementation
- [[lutheran-hermeneutics-paper]] · student paper; Flacius appears there — *Clavis* not *Catalogus*, but same author
