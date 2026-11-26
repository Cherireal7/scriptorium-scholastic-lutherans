# Audit brief — Selnecker, Paedagogia Christiana, Pars Prima (1577), English translation

You are the second reader. Others translated these parts; you compare them with the print, page by page, and correct them. Read `TRANSLATOR-BRIEF.md` in the volume folder first (format, register, Scripture rule).

Latin: `../sources-original/jpg-bsb10175496/pNNNNN.jpg` (page image = authority) and `../sources-original/txt-bsb10175496/pNNNNN.txt` (OCR, aid only; its Greek is unreliable, and it picks up a later reader's HANDWRITTEN marginal notes as if printed — those are not part of the book). Printed page number = image number. Page marks `<!-- p.N -->` in the part files carry the printed number.

## What to do
1. Go through EVERY page of your parts. For each page read the image and the English between its page mark and the next; compare sentence by sentence (verse and lists: line by line, item by item).
2. Correct real errors directly in the part file with the Edit tool: a sentence, clause, item, heading or reference left out; anything added; a misread word; a mistranslation (wrong sense, case, tense, person, subject/object, a lost negation); a wrong number; a page mark in the wrong place.
3. Greek: check every Greek word against the image letter by letter; it stays as the print has it (ligatures resolved). Where the translator put `[?]`, look hard yourself: resolve it if you can read it with confidence, otherwise leave it.
4. Scripture: KJV wording where Selnecker's Latin agrees in sense; where his Latin plainly differs, the English follows his Latin. His references stay as printed.
5. Endnotes: each must be true. A note on a misprint: confirm on the image that the print reads as the note says. A source identification: keep only if you are confident; otherwise soften it to what is certain or delete note and mark.
6. Do NOT restyle defensible renderings. Keep the Markdown format, heading levels, page marks and endnote keys. English only: do not add Latin transcriptions.
7. Work economically: read each image once at normal size; enlarge (crop) only lines where a reading is in doubt.

## Log
Write every change to the log file named in your task, one line each:
`- p.N — print: "…" — was: "…" — now: "…" — kind: omission | addition | misreading | mistranslation | greek | scripture | endnote | mark`
Then `## Doubtful, not changed`, and a last line `Pages checked: N of N`.

## Report (short)
Pages checked; corrections by kind; the three most serious; endnotes cut or softened; every `[?]` left; one sentence on faithfulness.
