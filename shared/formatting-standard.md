# Scholastic Lutherans — Print Formatting Standard

House format for all English translations. Reedsy-inspired, adapted from studying
Jordan Cooper's typeset Lutheran-translations line (Melanchthon *Epitome
Philosophiae Moralis* STANDARD, Meisner *De Summo Bono* TRADE-PRINT-READY).
Both are `Producer: Typeset by Reedsy`; both use `Crimson Text 11 pt` body and
share the front-matter / running-head / recto-chapter conventions below.

## 1. Trim & margins

| Use | Trim | Notes |
|-----|------|-------|
| **Trade hardback** (default for dogmatics / running-prose volumes) | **6.14 × 9.21 in** (US Royal / KDP hardback) | Kirchner uses this. |
| Pocket / short work | 5 × 8 in | Melanchthon *Epitome* uses this. |
| Alt trade | 6 × 9 in | Meisner *De Summo Bono*; also valid. |

**Mirror margins** (print binding — inside larger for gutter):

| Position | Twips | Inches |
|----------|------:|-------:|
| Top | 792 | 0.55 |
| Bottom | 936 | 0.65 |
| Inside (left on recto) | 1152 | 0.80 |
| Outside (right on recto) | 835 | 0.58 |
| Header (from top edge) | 432 | 0.30 |
| Footer (from bottom edge) | 504 | 0.35 |
| Gutter | 0 | 0.00 |

Set `<w:mirrorMargins/>` in `word/settings.xml`. In `<w:pgMar>` use `w:left` = inner,
`w:right` = outer — Word swaps them per side automatically once mirrorMargins is on.

## 2. Type

- **Body:** `Palatino Linotype` 11 pt (or `Crimson Text` 11 pt for pure Reedsy match).
- **Title font (cover / half-title):** `IM Fell English` — free OFL revival of late-17th-century Oxford types. Reads as "ancient" and works well against the dense post-Reformation Latin style.
- **Greek/multiscript fallback:** `Kurinto Text Regular` (used by Reedsy for polytonic Greek). Only needed if the volume has heavy Greek/Hebrew and Palatino's Greek doesn't cover.
- **Heading 1** (chapter/Locus/Book): 26 pt Palatino Bold, colour `B71C1C` (deep red), centered, `keepNext keepLines`, `spacing before=600 after=360`, `pageBreakBefore`.
- **Heading 2** (Question): 14 pt Palatino Bold, colour `B71C1C`, centered.
- **Heading 3** (Objection): 12 pt Palatino Bold Italic, colour `B71C1C`.
- **Justified body**, first-line indent ~1 em (via Word's default paragraph indent, or explicit `<w:ind w:firstLine="360"/>`).

## 3. Running head

Small-caps centered chapter title via a `STYLEREF "Heading 1"` field.

`word/header1.xml` run properties: `<w:rPr><w:smallCaps/><w:sz w:val="20"/><w:spacing w:val="20"/></w:rPr>`.

Long chapter titles that wrap: shorten the Heading-1 text itself (e.g. strip Latin
parenthetical) and put the removed part below as a separate italic subtitle
paragraph — see the [[latin-subtitle pattern]] below.

## 4. Page numbers

Centered `PAGE` field in `word/footer1.xml`. Body pagination is arabic starting at 1
on the first body page. Front matter is Roman (or suppressed entirely — Reedsy
suppresses on the title/copyright pages).

## 5. Front matter (in order)

1. **Half-title** (p.i, recto) — very simple: author name in SMALL CAPS, book title in roman, subtitle in italic. Massive top margin. No decoration.
2. **Blank verso** (p.ii).
3. **Full title** (p.iii, recto) — the full 1595-style / period-appropriate title, printer, date, subtitle, translator credit. Can span two pages if long.
4. **Copyright page** (verso of full title) — centered italic block:
   ```
   Copyright © YEAR The Scholastic Lutherans translation team

   Work Title. First edition, first printed at PLACE by PRINTER, YEAR.
   This working English rendering: First edition, YEAR.

   Translated from the SOURCE_EDITION Latin print,
   digitised by SOURCE, per-page OCR text extracted via TOOL,
   translated line-by-line and paragraph-by-paragraph
   following the author's own STRUCTURE.

   Companion to <related volumes if any>.

   Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
   ```
   Never leave the Reedsy "This book was professionally typeset on Reedsy" line if you started from a Reedsy template.
5. **Translator's Note** (recto) — arabic page 1 starts here. Heading 1.
6. **Table of Contents** (recto) — see [[toc-pattern]] below.
7. **Body** — Locus I / Chapter 1 opens on a recto page.

**Never let pandoc auto-render the title page.** Delete `title:` / `subtitle:` /
`author:` / `date:` from YAML frontmatter (keep only `lang:`) so pandoc doesn't
auto-generate a title page that duplicates your manual half-title / full-title
open-xml blocks.

## 6. Recto chapter openers (odd-page section break)

Every major section (chapter / Locus / Book / Part / Appendix) opens on a right-hand
(recto) page. Inject before each `# Heading 1` line in the master MD:

````
```{=openxml}
<w:p><w:pPr><w:sectPr><w:headerReference w:type="default" r:id="rId31"/><w:footerReference w:type="default" r:id="rId32"/><w:type w:val="oddPage"/><w:pgSz w:w="8842" w:h="13262"/><w:pgMar w:top="792" w:right="835" w:bottom="936" w:left="1152" w:header="432" w:footer="504" w:gutter="0"/></w:sectPr></w:pPr></w:p>
```
````

The `<w:type w:val="oddPage"/>` forces the next section to start on odd (recto).
Word/LibreOffice will insert a blank verso if needed. The `r:id` values must match
the header/footer relationships in the reference DOCX (`rId31` = header1, `rId32` =
footer1 in ours).

## 7. Latin (or subtitle) below the chapter title

Reedsy convention: chapter title is the English text only. Latin/original
sub-caption sits below as an italic paragraph — NOT part of Heading 1 (so it
doesn't bloat the running head and TOC entries).

**Master MD pattern:**
```markdown
# Locus II. Of God

*De Deo*

— ❦ —

## Question 1. ...
```

## 8. TOC pattern (avoid self-listing)

Pandoc's `#` heading for the TOC page bloats the TOC with a self-listing entry.
Use a raw openxml paragraph styled as Heading 1 (so STYLEREF running head still
picks up "Table of Contents" on TOC pages) with `outlineLvl` overridden — plus a
post-processor to strip the self-entry after LibreOffice expands the TOC field
(paragraph-level `outlineLvl` doesn't reliably override the Heading 1 style in
LibreOffice, so post-processing is the belt-and-braces path):

Master-MD:
````
```{=openxml}
<w:p>
  <w:pPr>
    <w:pStyle w:val="Heading1"/>
    <w:outlineLvl w:val="9"/>
  </w:pPr>
  <w:r><w:t>Table of Contents</w:t></w:r>
</w:p>
<w:p>
  <w:pPr><w:jc w:val="left"/></w:pPr>
  <w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>
  <w:r><w:instrText xml:space="preserve"> TOC \o "1-1" \h \z \u </w:instrText></w:r>
  <w:r><w:fldChar w:fldCharType="separate"/></w:r>
  <w:r><w:rPr><w:i/></w:rPr><w:t xml:space="preserve">Right-click the table and choose "Update Field" to populate page numbers, or open in Word / LibreOffice.</w:t></w:r>
  <w:r><w:fldChar w:fldCharType="end"/></w:r>
</w:p>
```
````

Post-processor in `update-fields.py`:
```python
enum = doc.getText().createEnumeration()
to_delete = []
while enum.hasMoreElements():
    para = enum.nextElement()
    s = para.getString().strip()
    if s.startswith('Table of Contents') and s != 'Table of Contents':
        style = getattr(para, 'ParaStyleName', '') or ''
        if style.startswith('Contents') or style.startswith('TOC'):
            to_delete.append(para)
for para in to_delete:
    para.getText().removeTextContent(para)
```

## 9. Drop caps (optional)

Reedsy uses them on running-prose treatises (Meisner *De Summo Bono*) but NOT on
Q&A / catechetical / scholastic texts (Melanchthon's *Epitome*, Kirchner's
*Methodica*). Drop-capping the first letter of a question (`H` of `How and whence
does God rightly will to be known?`) looks forced.

**Rule of thumb:** apply drop caps only to running-prose chapters. Skip on Q&A.

**Tool:** `shared/apply-drop-caps.py <docx> [--skip N] [--size PT] [--lines N]
[--skip-headings "T1,T2,..."]`

Run after LibreOffice's field refresh, before final PDF export. Idempotent.

## 10. Style-level DOCX modifications (reference DOCX)

Applied via python-zipfile+regex in the build pipeline. The reference DOCX for each
volume can be copied from `shared/reference-custom.docx` and then patched.

**Body font size (docDefaults):** ensure only ONE `<w:sz w:val="22"/>` (11 pt) in
`<w:docDefaults><w:rPrDefault><w:rPr>` — if pandoc's base reference has an existing
`<w:sz w:val="24"/>` line, remove it or Word will use the larger value.

**Heading 1 pPr:** add `<w:pageBreakBefore/>` for safety (redundant with our
odd-page section breaks but harmless).

**Body sectPr** (single sectPr at end of `word/document.xml`): must include
`<w:pgSz>`, `<w:pgMar>`, `<w:headerReference>`, `<w:footerReference>`, plus
`<w:pgNumType w:start="1"/>`.

**settings.xml:** must have `<w:mirrorMargins/>` for mirror-margin behaviour.

**header1.xml:** STYLEREF run properties include `<w:smallCaps/>` and appropriate
`<w:sz>` and letter-`<w:spacing>`.

## 11. Cleanup before final build

- Remove any leftover audit-notes from the master MD (bracket-italic lines like
  `*[Locus XX ... is TRULY COMPLETE ...]*`). Grep pattern:
  `^\*\[.*(COMPLETE|rendered in \d+ tranch|follows in T\d+).*\]\*\s*$`.
- Verify no working-notes, `TODO`, `TKTK`, or `[Draft]` markers remain.
- Body font check: measure a body page with PyMuPDF (`d[N].get_text('dict')`) —
  should show `PalatinoLinotype-Roman 11.0`, not 12.0.
- Recto check: for each chapter opener, printed page number should be odd. See
  the verification snippet in `shared/verify-build.py` (if present).

## 12. What Reedsy does that we do NOT copy

- The `Producer: Typeset by Reedsy` PDF metadata — LibreOffice-Writer replaces
  this naturally when we export.
- The `This book was professionally typeset on Reedsy / Find out more at reedsy.com`
  copyright-page line — replaced with our own Scholastic Lutherans line.
- LaTeX-with-hyperref as producer — we go via LibreOffice, which produces
  different PDF internals but the visual result is equivalent.

## 13. Build pipeline (per-volume)

Each volume has:
- `<volume>/build-shareable.ps1` — pandoc → DOCX → LibreOffice-UNO field refresh → PDF
- `<volume>/reference-<name>.docx` — the volume-specific reference DOCX, patched with our formatting settings
- `<volume>/update-fields.py` — LibreOffice-Python-UNO helper that refreshes fields (TOC, PAGE, STYLEREF) and applies the TOC-self-entry post-process
- `<volume>/review/<name>.md` — the master Markdown with all the front-matter openxml blocks

To style a NEW volume, copy an existing volume's `reference-*.docx`, `update-fields.py`,
and `build-shareable.ps1`, adjust paths, and follow the front-matter template in
section 5 above.

The Kirchner Methodica 1595 build is the canonical reference implementation for
this standard as of 2026-09-12.
