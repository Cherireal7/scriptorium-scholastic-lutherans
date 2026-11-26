# Audit brief — Selnecker, Institutio Pars III (1579), English translation

You are the second reader. Someone else translated this part; you compare it with the print, page by page, and correct it. Read `TRANSLATOR-BRIEF.md` in the volume folder first (format, register, the Scripture rule).

Latin and Greek: `sources-original/jpg/pNNNNN.jpg` (page image = authority) and `sources-original/txt/pNNNNN.txt` (OCR, aid only; its Greek is unreliable).

Printed page ↔ image (the page marks `<!-- p.N -->` in the files carry the PRINTED number):

| Printed page | Image |
|---|---|
| 1–13 | page + 6 (images 20–21 repeat pp. 12–13; ignore them) |
| 14–207 | page + 8 |
| 209, 210 | 216, 217 (the printer skipped 208) |
| 212–322 | page + 6 (the printer skipped 211) |
| indexes | images 329–340 |

## What to do
1. Go through EVERY page of your part. For each page read the image and the English between its page mark and the next; compare sentence by sentence (verse and lists: line by line, item by item).
2. Correct real errors directly in the part file with the Edit tool: a sentence, clause, item, heading or reference left out; anything added; a misread word; a mistranslation (wrong sense, case, tense, person, subject/object, a lost negation); a wrong number; a page mark in the wrong place.
3. **Greek.** Check every Greek word against the image letter by letter (ligatures resolved, accents and breathings as the print has them). Correct misreadings. Where the earlier reader put `[?]`, look hard yourself: resolve it if you can read it with confidence, otherwise leave it.
4. **Scripture.** Programme standard: quotations conform to the King James Version (1611) where Selnecker's Latin agrees in sense; where his Latin plainly differs, the English follows his Latin. If your part was translated under the older rule (the task says so), bring its Scripture quotations to KJV wording wherever the Latin agrees. Keep his references as printed.
5. **Endnotes.** Each endnote must be true. For a source identification (a classical author, a Father, Luther, Melanchthon) keep it only if you are confident it is right; if you cannot stand behind it, soften it to what is certain ("a line of Juvenal") or delete the note and its mark. For a note on a misprint, confirm on the image that the print reads as the note says.
6. Do NOT restyle. Leave a rendering alone if it is defensible. Keep the Markdown format, the heading levels, the page marks and the endnote keys.

## Log
Write every change to the log file named in your task, one line each:
`- p.N (img NNN) — print: "…" — was: "…" — now: "…" — kind: omission | addition | misreading | mistranslation | greek | scripture | endnote | mark`
Then `## Doubtful, not changed`, and a last line `Pages checked: N of N`.

## Report (short)
Pages checked; corrections by kind; the three most serious; endnotes cut or softened; anything you could not check; one sentence on the part's faithfulness.
