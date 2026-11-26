# Translator brief — Selnecker, Institutio Pars III (1579), parallel parts

Several translators work on this volume at the same time, each on a fixed range of page images. Follow this brief exactly so the parts join without seams.

## Read first
- `HANDOFF.md` and `notes.md` in this folder (project conventions; where they speak of tranches T1–T9 and commits, ignore that — you write one part file and do not use git).
- About 150 lines of the finished Pars II as a model of register and layout:
  `../selnecker-institutiones-1573-pars-ii/review/selnecker-institutiones-1573-pars-ii.md`, lines 376–520.

## Source
`sources-original/jpg/pNNNNN.jpg` — page images of the Munich copy (bsb10175492). **The image is the authority.**
`sources-original/txt/pNNNNN.txt` — the library's OCR, an aid only: long s reads as f, abbreviations are lost, and its Greek is unreliable.
Printed page number = image number − 6 (image p00007 = printed p. 1; p00328 = printed p. 322).

Read every image of your range with the Read tool. For Greek, read the image itself, letter by letter; the print uses sixteenth-century ligatures (ου as ȣ, στ, καὶ, ται, and so on) — resolve them into ordinary polytonic Greek.

## Where your part starts and stops
- Start at the first new paragraph, heading or item that BEGINS on your first image. Skip the tail of a paragraph that runs over from the page before; the previous translator has it.
- At the end, finish the paragraph or item that is in progress at the foot of your last image by reading on into the next image.

## What to produce
Translate everything printed: headings, questions and answers, lists, tables, verse, marginal notes, Scripture references. Skip only running heads, page numbers, signature marks, catchwords, stamps and handwriting. No summarising, no skipping; a long answer stays long.

### Register
The English of Pars II: early modern theological English ("doth", "hath", "thou" in quoted Scripture and prayer), scholarly and close to the Latin. Keep Selnecker's numbered divisions and his question-and-answer form.

### Scripture
Programme standard (decision of 2026-09-12, confirmed by the editor on 2026-11-26): Scripture quotations are conformed to the **King James Version (1611)**, which is in the public domain. Where Selnecker's Latin (or Greek) agrees in sense with the KJV, use the KJV wording. Where his Latin plainly says something different (he often cites the Vulgate or paraphrases), translate his Latin and do not force the KJV. Use no other English Bible version. Keep his reference as printed, in bold (`Psal. 51.` → **Ps. 51**); where his Psalm number differs from the KJV number, add the KJV number once in square brackets: **Ps. 50 [51]**. Do not add verse numbers he does not give, except in an endnote.

### Markdown conventions (as in Pars II)
- Headings: `# ` for the major divisions named in your task; `## ` for the next level (a commandment, an article of the Creed, a titled section); `### ` for sub-sections and for each titled question. Give Latin titles in italics followed by `·` and the English: `## *De Primo Praecepto* · On the First Commandment`.
- A question printed as a heading: `### ` + the question in English. Short questions printed inside the run of the text: bold paragraph `**Question.**` … / answer as ordinary paragraphs.
- Names of authorities in bold on mention (**Augustine**, **D. Luther**, **Philip Melanchthon**, **Cicero**). Scripture references in bold (**Rom. 3**).
- Quotations: italic inside double quotation marks, `*"..."*`; a displayed quotation or a quoted Scripture verse set off by the print: a block quote line beginning `> `.
- Latin technical terms: italic on first occurrence in a section, with the English beside it.
- Verse: block-quote lines, one per printed line, each ending with two spaces (`> line  `).
- Numbered lists as printed (1. 2. 3.).
- Greek: keep every Greek word and phrase of the print in polytonic Greek, bold-italic (`***ὁμόνοια***`), followed by an English gloss in parentheses unless the print itself gives the Latin, in which case translate the Latin.
- Hebrew, if any: keep, with transliteration and gloss.
- Marginal notes: `*[Margin: …]*` at the point they stand beside.
- Ornament between major sections, exactly: a line containing only `— ❦ —`.
- Page marks: at the point where each printed page begins put an HTML comment, exactly `<!-- p.N -->` (N = printed page number), on its own line between paragraphs or inline between words. These are invisible in the book and are used for checking.
- Endnotes: sparingly, for (a) an identification of a source Selnecker cites (Luther, Melanchthon, a Father, a classical author) when you are sure of it, (b) a reading where you depart from an evident misprint, (c) a term a reader needs. Mark with `[^KEY-1]`, `[^KEY-2]` … where KEY is the part key given in your task, and put the definitions at the end of your file as `[^KEY-1]: text`. Do not invent references; if you are not sure of a citation, leave it without a note.
- A word you cannot read: best reading followed by `[?]`, and list it in your report.
- No raw HTML other than the page-mark comments. No `{=openxml}` blocks. No front matter.

## Report (short)
1. File written; printed pages covered; where exactly you started and stopped (first and last words).
2. The headings (`#`, `##`) you used, in order — the editor builds the contents from them.
3. Every `[?]` with its image number.
4. Decisions other parts will meet (a recurring term, a heading pattern).
5. Anything you did not translate, and why.
