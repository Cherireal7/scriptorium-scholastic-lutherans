# Musculus, Precationes (Leipzig 1573) — translation conventions

Working English edition for the Scholastic Lutherans translation programme.

## Source

- Andreas Musculus, *Precationes ex veteribus orthodoxis doctoribus, ex Ecclesiae hymnis et canticis, ex Psalmis denique Davidis collectae, et nunc recens recognitae et auctae*, Leipzig: Andreas Schneider, typis Voegelianis, 1573 (VD16 M 7192).
- Scan: Bayerische Staatsbibliothek, Asc. 5554 s, digital id `bsb00019110` (public domain mark), 356 images.
- Local copy: `sources/musculus-precationes/bsb-1573/`
  - `img/NNNN.jpg` — the page image. **This is the authority.**
  - `txt/NNNN.txt` — the library's OCR, one line per printed line. An aid only: it confuses long s with f, drops abbreviation marks, garbles headings and small capitals, and mixes running heads and page numbers into the text.
- Image number = printed page number + 58 for the body (printed p. 1 = image 0059, p. 262 = image 0320).

## How to work

1. Read every page image in your range, with the OCR text beside it. Where they disagree, the image wins.
2. Expand the printer's abbreviations silently (`q;` = que, a stroke over a vowel = m/n, `ę` = ae, `&` = et, and so on).
3. Translate everything printed in your range: headings, attributions, prayers, psalms, hymns, versicles, rubrics. Skip only running heads, page numbers, signature marks, catchwords and library stamps. Skip handwriting.
4. Do not shorten, summarise or skip. A prayer that is long in Latin is long in English.
5. If a word cannot be read on the image, translate your best reading and put `[?]` straight after it. List every such place in your final report with image number.

## English style

- Traditional devotional English that sits beside the King James Version: *thou, thee, thy, thine*, verb forms *-est / -eth* (hast, art, dost, givest, liveth). Keep it readable; no invented archaisms.
- Faithful, close translation. Keep the Latin sentence's order of thought where English allows; break up a period only where English would be unreadable.
- Capitalise names and titles of God (Father, Son, Holy Ghost, Trinity, Lord, Saviour, Redeemer). Pronouns for God stay lower case, as in the KJV (thou, he, his).
- "Spiritus Sanctus" = "Holy Ghost" (KJV usage); "paracletus" = "Comforter"; "Deus" in small capitals = "GOD"; "DOMINE" in small capitals = "LORD".
- "Synaxis" = "the holy Supper" on first use with "(Synaxis)", after that "the holy Supper".
- "Amen" as printed.
- British/KJV spellings: Saviour, honour, favour.

## Scripture

- Where the text is a psalm or another Bible passage, conform the wording to the King James Version (1611), as the programme does in all its volumes. Where the Latin clearly says something different from the KJV (the Vulgate often does), translate the Latin and do not force the KJV.
- The 1573 book numbers the Psalms the Hebrew/KJV way and uses a newer Latin Psalter, not the Vulgate: give the printed number alone. (Only if a number differs from the KJV: printed number first, KJV number in square brackets.)
- Capitals of a prayer's opening words are display type: do not render them as LORD/GOD. Small capitals inside the text are.
- Agreed terms: *pietas* (of God) = lovingkindness; *charitas* = charity; *per omnia secula seculorum* = world without end; *Alia* = Another; *Oratio* over a collect = Collect; Amen in ordinary type.
- Add a reference in square brackets only where it is certain: `[John 14:6]`.

## Attributions

- Keep each attribution as a heading in English, with the short Latin form after it in italics on the heading line when it is not obvious: `## Augustine, Meditations, chapter 12`.
- Usual names: Augustinus = Augustine, Bernhardus = Bernard, Hieronymus = Jerome, Ambrosius = Ambrose, Cyprianus = Cyprian, Gregorius = Gregory, Chrysostomus = Chrysostom, Anselmus = Anselm, Hilarius = Hilary, Prudentius, Sedulius, Fulgentius, Ephraem = Ephrem, Basilius = Basil, Ecclesia = "The Church" (prayers, hymns and collects of the Church).
- "Meditat." = Meditations; "Solil." = Soliloquies; "Manual." = Manual; "Confess." = Confessions.
- Do not add an identification of your own in the text. If you are sure of a source the book does not name (for example a hymn's usual title or author), put it in a footnote.

## Markdown format (strict — a script turns these files into the book)

```
# I. Forms of Invoking the Holy Trinity
*Formulae invocandi Sanctam Trinitatem*

## Augustine, Meditations, chapter 12

{p.1} O highest Trinity, one power and undivided Majesty, our GOD ... most secret {p.2} in thy thoughts, true in thy words ...

## The Church
### Hymn
*O lux beata Trinitas*

| O Trinity, blessed light,
| and principal Unity,
| now that the fiery sun departeth,
| pour light into our hearts.

| (next stanza, blank line between stanzas)
```

- `# ` only for the book's numbered main sections (I–XVIII) and for front matter parts (Title Page, Calendar, Preface, Index). Put the Latin title in italics on the next line.
- `## ` for each attribution or prayer heading. `### ` for a sub-heading under it (Hymn, Collect, Psalm 50 [51], Thanksgiving, Verse, Response, ...).
- If the book numbers the prayers inside a section (I, II, III ...), keep the number at the start of the heading: `## II. Augustine, Meditations, chapter 32`.
- Page markers: `{p.N}` at the exact point in the English where printed page N begins (N is the printed page number, not the image number). Put it between words, never inside a word. In the unnumbered front matter use the image number: `{img.47}`.
- Verse (hymns, metrical pieces, month verses): one line per Latin line, each starting with `| `; a blank line between stanzas. Translate line for line, plainly, without rhyme or metre.
- Psalms: prose paragraphs, one verse per paragraph is not needed; follow the paragraphing of the print.
- Printed marginal notes: `[margin: text]` at the point they stand beside.
- Footnotes (sparingly): `[^1]` in the text and `[^1]: text` at the end of the file. Number them from 1 in each file. Use them for: a reading that departs from the print because of an obvious misprint; a source you are sure of; a Latin term a reader needs. Not for commentary.
- Italics `*...*` for Latin words kept in the text and for Latin incipits. No bold. No HTML. No tables except in the calendar part. No horizontal rules.
- Plain typographic punctuation is fine (’ “ ” — ). One blank line between blocks.

## Final report (keep it short)

1. File written, printed pages covered, number of prayers/pieces.
2. Every `[?]` place with image number and what the difficulty is.
3. Anything in the range you did not translate, and why.
4. Any term you had to decide that other parts of the book will meet too (so the whole book can be made to agree).
