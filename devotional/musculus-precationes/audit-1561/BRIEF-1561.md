# Brief — making the strict 1561 edition (Musculus, Precationes, Frankfurt on the Oder 1561)

An English translation of the enlarged Leipzig 1573 edition exists and has been audited. The 1561 edition has the same eighteen sections and the same prayers in the same order, but lacks 94 pieces that 1573 added, and differs here and there by a word or two. Your job is to turn one part of the 1573 English into a strict translation of the 1561 print.

Read first:
- `/Users/cheri/Documents/Scholastic-Lutherans/work/musculus-precationes/CONVENTIONS.md` (style, agreed terms, Markdown format)
- `/Users/cheri/Documents/Scholastic-Lutherans/work/musculus-precationes/audit/collation-1561-1573.md` (part A: where sections begin in both editions; part B: the pieces found only in 1573, section by section; part D: known wording variants)

Latin of 1561: `/Users/cheri/Documents/Scholastic-Lutherans/sources/musculus-precationes/bsb-1561/img/NNNN.jpg` (page image = authority) and `txt/NNNN.txt` (OCR, aid only; long s reads as f, abbreviations lost). The book is foliated: leaf n recto = image 13+2n, leaf n verso = image 14+2n (leaf 1r = image 0015, leaf 139r = image 0291). Ignore all handwriting (owners' notes, underlining, marginal jottings).

English of 1573 to start from: the file named in your task, in `/Users/cheri/Documents/Scholastic-Lutherans/work/musculus-precationes/translation/`. Do NOT edit that file. Copy what you need into your new file.

## What to do
1. Go through EVERY 1561 page image of your range, in order, with the 1573 English beside it.
2. Keep only what the 1561 print has. Leave out every piece that is not on the 1561 pages (the collation part B lists them; trust the 1561 image over the list).
3. Compare sentence by sentence (verse: line by line). Where the 1561 Latin reads differently from what the English says — a different word, an added or missing phrase, a different heading or attribution, a different chapter or psalm number — make the English follow 1561. If the difference is more than spelling, add a short footnote: `[^n]: The 1573 edition reads “…”.` Do not footnote mere misprints of 1573 that the old footnotes mention; drop old footnotes that speak only about the 1573 print, and keep or adapt those that are still true of 1561 (check each on the 1561 image). If 1561 itself has an obvious misprint, translate the right reading and footnote the printed one.
4. Replace the page markers. Remove every `{p.N}`. Put `{f.12r}` / `{f.12v}` at the exact point in the English where that 1561 page begins (same rules as before: between words, never inside a heading; when a page begins with a heading, at the start of the text that follows).
5. Headings: keep the English heading style of the 1573 file. `# ` section headings keep the numerals I–XVIII (even where 1561 prints no numeral) and the Latin title line in italics as 1561 prints it.
6. Do not restyle sound English. Change only what 1561 requires or what is a real error.
7. Footnotes numbered from 1 in your file, definitions at the end.

## Log
Write to the log file named in your task:
- `## Left out` — each 1573 piece omitted (heading, incipit).
- `## Variants` — each place changed to follow 1561: leaf, 1561 Latin, 1573 English, new English.
- `## Doubtful` — anything unsure.
- last line: `Leaves checked: first–last, N pages of N`.

## Report (short)
Leaves covered and pages checked; number of pieces left out; number of wording variants and the three most notable; anything in 1561 that 1573 lacks; anything you could not determine.
