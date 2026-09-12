# Scholastic Lutherans — End-to-End Translation Pipeline

The whole workflow for taking a 16th–18th-century Latin work from "we heard this
book exists" to "printable, distributable English edition." Every volume in the
repo follows these five stages.

```
┌─────────────┐   ┌──────────────┐   ┌─────────────┐   ┌───────┐   ┌───────────┐
│ 1. SOURCE   │ → │ 2. EXTRACT   │ → │ 3. TRANSLATE│ → │4.AUDIT│ → │5. FORMAT  │
│  identify + │   │  OCR + clean │   │  faithful   │   │  vs.  │   │  house    │
│   acquire   │   │  + structure │   │  line-by-line│   │  sources│   │  spec + PDF│
└─────────────┘   └──────────────┘   └─────────────┘   └───────┘   └───────────┘
```

Companion documents:
- `shared/formatting-standard.md` — stage 5 spec (house print format)
- Memory `reference-scholastic-lutherans-workflow` — stage 3 mechanics
- Per-volume `notes.md` / `HANDOFF.md` — resume state for each stage

---

## Stage 1 — Source identification & acquisition

**Goal:** confirm a specific print exists, is in the public domain, and can be
sourced as a scannable / OCRable file.

**Steps:**

1. **Deep search** for the author and work:
   - Google Books (`site:books.google.com <author> <work> <year>`) — often has
     scanned copies of 16th–18th c. printings.
   - VD16 / VD17 / VD18 (Verzeichnis der Drucke) — the German national bibliography
     of early printed works (`https://www.vd16.de` etc.).
   - HAB Wolfenbüttel, BSB München, Herzog August Bibliothek digital collections.
   - Post-Reformation Digital Library (`prdl.org`) — curated Lutheran / Reformed
     scholastic works with links to online scans.
   - Internet Archive, HathiTrust (US-side reprints, some open).
   - CERL Thesaurus for authoritative author-name variants (many early moderns
     have three or more Latinized/German name forms).

2. **Manual verification** — before spending time on OCR:
   - Confirm the edition is the one you want (first edition vs posthumous
     augmented reprint — Kirchner's *Methodica* had both; Selnecker's *Institutio*
     had multiple).
   - Confirm the scan is complete (pages not missing, foldouts captured).
   - Confirm text-layer quality: many Google Books scans have decent enough
     pdftotext output; others are image-only and need OCR.
   - Note the printer + year + city — these go on the title/copyright page.

3. **Acquire**:
   - Download the highest-quality PDF/JP2 available. Store in
     `<volume>/sources-original/`.
   - The `sources-original/` directory is **git-ignored** (see `.gitignore`) —
     large binary scans stay local, only text derivatives get committed.

4. **Companion checks** — is there:
   - A German counterpart (Kirchner's Latin *Methodica* had a German
     *Enchiridion*)? If yes, note it for cross-reference audit in stage 4.
   - A modern critical edition (rare for scholastic Lutherans, but Chemnitz,
     Gerhard, and a few others have partial ones)?
   - Existing translations, complete or partial (usually none — this repo exists
     because they don't)?

**Output:** a raw scan in `sources-original/`, a note in `notes.md` recording
edition details, printer, city, year, and companion-work pointers.

---

## Stage 2 — Extraction & data collection

**Goal:** produce a plain-text working copy of the Latin source that a translator
can read alongside the target.

**Steps:**

1. **OCR / text extraction** — for Google Books PDFs, `pdftotext` from Poppler
   usually suffices:
   ```bash
   pdftotext -layout <volume>/sources-original/<work>.pdf \
             <volume>/sources-original/<work>.txt
   ```
   For image-only scans, run Tesseract with a Latin language pack. Optionally
   fine-tune with Google Cloud Vision for polytonic Greek passages.

2. **Structural map** — skim the Latin. Identify:
   - Top-level structure (Loci, Books, Parts, Disputationes, Chapters).
   - Question / Objection count per major section.
   - Any appendices (biographical vitae, indexes, colophons).
   - OCR line ranges per Locus so tranches can be planned. Grep `LOCVS` /
     `CAPVT` / `SECTIO` / Latin section titles.

3. **Extraction sanity check** — spot-check a few paragraphs for common OCR
   errors: `s→f` (long-s), `c→e`, missing spaces, dropped ligatures, marginal
   notes bleeding into main-text columns. Note them so the translator can
   silently correct.

4. **Notes doc** — write `<volume>/notes.md` with:
   - Full title (Latin), printer, year, place.
   - Structural breakdown with OCR line ranges.
   - Tranche plan (topical chunks of ~6–12 Q or ~6–10 Obj).
   - Anything unusual (missing pages, mid-doc language switches, hidden
     apparatus).

**Output:** `sources-original/<work>.txt` (git-ignored if huge; committed if
manageable), `<volume>/notes.md` with structural map.

---

## Stage 3 — Translation

**Goal:** produce a faithful English rendering of every question, every
objection, every sub-point.

Full mechanics live in memory `reference-scholastic-lutherans-workflow` — the
short version:

- **Faithful line-by-line, all Q + all Obj, no summary mode.** Non-negotiable.
- One MD file per volume at `<volume>/review/<volume>.md`. Append to it; never
  split.
- Commit per tranche (T1, T2, ...). Terse commit titles — see
  `[[feedback-token-budget-discipline]]`.
- Early modern English theological register. Preserve Latin technical vocabulary
  in italics where semantic weight requires (*iustitia*, *propter Christum*,
  *ergo*, *per se*).
- Front-matter openxml blocks (half-title, full title, copyright) written
  directly into the MD as `{=openxml}` fenced code blocks — follow the front-
  matter template in [[reference-print-formatting-standard]] §5.

**Output:** `<volume>/review/<volume>.md` — the complete translation with front
matter, TOC placeholder, every Locus/Chapter, every appendix.

---

## Stage 4 — Post-translation audit

**Goal:** every claim in the translation traces back to a source. Every
Scripture citation matches a modern translation. Every structural element
matches the printed original.

Two orthogonal passes, run in either order:

### 4a. OCR-faithfulness audit

Walk the OCR line-by-line against the MD to confirm the translation covers
everything. Catches:

- Dropped questions or objections (e.g. Kirchner Locus XII was missing Q25 + Objs
  XIX & XX until an audit-pass caught it — commit `9fc3008`).
- Malformed Greek (e.g. Kirchner Locus II Q20 `συρισάμενος` → `ὑφιστάμενον`).
- Structural miscounts vs. HANDOFF-declared totals.

**Output:** a per-Locus audit note in `HANDOFF.md` recording Q-counts and Obj
clusters verified, plus any gap-fill commits.

### 4b. Scripture-conformance audit

Every quoted Scripture citation in the MD gets checked against a modern
translation and rewritten where the Vulgate-idiom English materially differs.

For our line: **NKJV pass** — see the Kirchner Methodica log for canonical
mechanics (memory `reference-methodica-1595-handoff-2026-09-08`). Short version:

1. Grep MD for `\*\*<Book>\.\s*<Ch>:` to enumerate all citations in each chapter.
2. WebFetch NKJV per chapter via
   `https://www.biblegateway.com/passage/?search=<Book>+<Ch>%3A<v1>%3B+<Ch>%3A<v2>&version=NKJV`
   (small verse ranges — full chapters get refused for copyright).
3. Compare each quoted citation (italic `*"..."*` form) to NKJV. Skip pure
   references (no quoted text). Skip Kirchner's paraphrases-into-prose (bold but
   not italic-quoted).
4. Edit to NKJV wording where materially different. Preserve stylistic
   capitalization of Law / Gospel / Sacred Scripture.
5. Where the quoted text spans more verses than the label, expand the label.
6. Commit per book with terse message: `<Volume> NKJV pass — <book>`.

**Book-name normalization at end of pass:** `Apoc.`→`Rev.`, `Ex.`→`Exod.`,
`1 Peter`→`1 Pet.`, `Malachi`→`Mal.`, `Micah`→`Mic.`, `Daniel`→`Dan.`,
`Ecclesiastes`→`Eccles.`, `3 Kings`→`1 Kings` (Vulgate 1–2 Kings = Protestant
1–2 Samuel; verify each). Skip apocrypha (Wisd., Sirach/Ecclus., Tob.,
Jud.[= Judith]) — NKJV omits.

**Wrinkle:** Psalm-numbering — Vulgate/LXX Ps 9 = KJV/NKJV Ps 9+10, so his
Ps 10–147 are off-by-one from NKJV Ps 11–148. Also many Psalms count the title
as v.1, so his 51:19 = NKJV 51:17. Update the label where the verse-numbers
shifted.

### Optional: cross-edition audit

If a modern critical edition or a period-companion (e.g. the German *Enchiridion*
alongside the Latin *Methodica*) exists, spot-check questionable passages
against it. Rarely comprehensive; use for adjudicating hard cases.

**Output:** all citations conform to the target modern translation; all
book-names normalized; per-book commits in git log.

---

## Stage 5 — Formatting

**Goal:** produce a professionally-typeset PDF (and DOCX) suitable for print
distribution.

Full spec: `shared/formatting-standard.md` and memory
`[[reference-print-formatting-standard]]`. Short version:

- Copy an existing volume's `reference-<name>.docx`, `update-fields.py`, and
  `build-shareable.ps1` as templates (canonical reference:
  `catechetical/kirchner-methodica-1595/`).
- Adjust title / author / dates / license in the MD front-matter openxml blocks.
- Trim: **6.14 × 9.21 in** (US Royal / KDP hardback) default. Mirror margins.
- Body: Palatino Linotype 11 pt. Titles: IM Fell English. Small-caps STYLEREF
  running head. Red-Palatino headings (H1 26pt, H2 14pt, H3 12pt).
- Every chapter/Locus opens on a right-hand (recto) page via odd-page
  section breaks.
- Copyright page: Scholastic Lutherans block + CC BY-NC-SA 4.0.
- Drop caps: skip for Q&A/scholastic texts; apply for running-prose treatises
  via `shared/apply-drop-caps.py`.

**Pre-final-build cleanup:**
- Remove leftover audit-notes:
  `^\*\[.*(COMPLETE|rendered in \d+ tranch|follows in T\d+).*\]\*\s*$`.
- Strip YAML `title:` / `subtitle:` / `author:` / `date:` from frontmatter so
  pandoc doesn't auto-render a duplicate title page.
- Verify no `TODO`, `TKTK`, `[Draft]` markers remain.

**Build:** `pwsh -f build-shareable.ps1` from the volume root. Output goes to
`<volume>/review/<work-slug>.pdf` and `.docx` (both git-ignored).

**Verification:** measure body font (should be 11 pt Palatino), check trim
(6.14 × 9.21 in), confirm each Locus opener's printed page number is odd.

**Output:** print-ready PDF + editable DOCX.

---

## Cross-cutting concerns

**Git etiquette:** one commit per tranche in stages 3–4; feature-scoped commits
in stages 1–2 and 5. Never `--no-verify`, never amend published commits, always
include the `Co-Authored-By: Claude Opus 4.7 ...` trailer.

**Memory hygiene:** each volume should have a `reference-<work>-handoff-<date>`
memory pointing to its resume state. Update on major milestones. Close on
volume completion.

**Handoff between chats:** if a volume is mid-stage and needs to resume in a
fresh chat, drop a `HANDOFF.md` at the volume root — see memory
`[[handoff-file-convention]]`.

**Companion pairing:** German-Latin sibling volumes (e.g. Kirchner
*Enchiridion* + *Methodica*) should cross-reference each other's copyright
pages and share bibliographic anchors.

**License:** default CC BY-NC-SA 4.0 for our translations. The source text is
public domain; our translation is separately copyrighted.
