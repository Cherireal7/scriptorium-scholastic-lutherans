# Handoff — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

**Read this first.** Self-contained brief for whoever picks up the volume in a fresh chat. **Stages 1+2 and Stage 3 T1 through T33 are done — VOLUME BODY COMPLETE ✅.** All 4 books (Liber I–IV) are fully translated, ending with the AMEN doxology at physical p. 1109. Back matter (Scripture/Fathers/Rerum indices pp. 1110–1189) is deferred per plan. The next tranche is **Stage 4** (KJV audit pass) + **Stage 5** (Reedsy build).

T2–T33 detail is in the git log (`git log --oneline`) — each Balduin-Casibus commit narrates one full chapter tranche.

## What this project is

Translating **Friedrich Balduin** (1575–1627) · ***Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, de Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae*** (Wittenberg: Paulus Helwigius, 1628) from Latin into modern English.

**Historical significance.** This is the **first single-author Lutheran casuistry** — Balduin (Hutter's successor at Wittenberg, †1627) is the first Protestant to work moral theology in the form of *cases of conscience* in a serious systematic manner. The *Tractatus* was published posthumously the year after his death and was repeatedly reprinted through the 17th century.

## Volume status — quick view

| Book | Scope | Status |
|------|-------|--------|
| Front matter | Dedicatoria + Faculty Praefatio + Buchner epigram | ✅ T1 |
| Liber I | Conscience *in genere* (16 Capita + Steuber Additamentum) | ✅ T2–T3 |
| Liber II | God + religion (18 Capita) | ✅ T4–T15 |
| Liber III | Celestial spirits: angels, demons, magi, divination, specters (7 Capita) | ✅ T16–T22 |
| Liber IV Cap. I–XI | Body, soul, wealth, callings, ministry, ordination, preaching, sacraments, keys, order | ✅ T23–T31 |
| Liber IV Cap. XII | *De magistratu politico* (political magistrate, 17 Casus incl. laws-binding, hunting, brothels) | ✅ T32 + T33 open |
| Liber IV Cap. XIII | *De conjugio* (marriage, 11 Casus) | ✅ T33 |
| Liber IV Cap. XIV | *De officiis parentum et liberorum* (parents/children, 13 Casus) | ✅ T33 |
| Liber IV Cap. XV | *De officiis fratrum, sororum et propinquorum* (brothers/sisters/kin, 4 Casus) | ✅ T33 |
| Liber IV Cap. XVI | *De officiis dominorum et servorum* (masters/servants, 5 Casus) | ✅ T33 |
| Liber IV Cap. XVII | *De conversatione cum proximo* (neighbor-conversation, 18 Casus) — closing with AMEN | ✅ T33 |

**VOLUME BODY COMPLETE ✅ — All ~1109 physical pages translated end-to-end. Back matter deferred.**

## Corrections applied in T33

- Cap. XII actually has 17 Casus, not 14 (OCR "CAPUT XV" at ln 65070 is really Casus XV of Cap. XII — running headers confirm "LIB. IV. CAP. XII" through phys p. 1046). T32's commit note said "14 Casus" but T33 covered the missing Casus XV (laws-binding-conscience), XVI (hunting), and XVII (brothels).
- Cap. XV starts around ln 67364 (phys p. 1080) — brothers/sisters/kin — a **short** chapter with just 4 Casus. Do not confuse with Cap. XVI (masters/servants) at ln 67595.

## Where the files are

- **OCR source**: `sources-original/balduin-casibus-1628.txt` (75,390 lines from PyMuPDF extraction).
- **Translation MD**: `review/balduin-casibus-conscientiae-1628.md` — **body complete, ~11,157 lines**. Ends with AMEN doxology.
- **Build machinery** (for Stage 5): `build-shareable.ps1`, `update-fields.py`, `reference-balduin-casibus.docx` — Kirchner-precedent pipeline.
- **Notes**: `notes.md` (source-plan, tranche-plan, structural map).

## Next steps

### Stage 4 — KJV audit pass

Following the **Kirchner Methodica 1595** precedent, do a batch pass replacing inline Scripture translations (currently a mix of direct-from-Latin and various English translations) with **KJV (1611/1769)** wording where verse identity is unambiguous. This ensures the volume matches the house style established by Kirchner and Symbolorum-1577 forerunners.

- Scope: full body of `review/balduin-casibus-conscientiae-1628.md`.
- Cite-preservation: keep parenthetical (Book chapter:verse) citations exactly.
- Deviation policy: if Balduin's Latin quotation deviates from KJV (unusual gloss, different rendering, or theological point), preserve the deviation with a footnote or bracketed note.

### Stage 5 — Reedsy build

Follow the **Kirchner Methodica 1595** and **Symbolorum 1577** precedents:

1. Front matter — cover, title, copyright, TOC. English-only H1 titles with Latin sub-caption. No running header on cover/title/copyright pages.
2. Body — Reedsy-inspired house format (trim 6×9″, standard margins, Georgia/Cormorant Garamond serif, Fira Sans headings). Drop caps at each Casus. Chapter openings on recto (page-break tags already in the MD).
3. Back matter — could be built from the finished English MD (regenerable Scripture/Fathers/subject indices) — but per plan, this is optional and deferred.

Build pipeline: `build-shareable.ps1` calls Pandoc on the MD → DOCX using `reference-balduin-casibus.docx` as template, then `update-fields.py` inserts TOC/updates page numbers. Output goes to a `build/` subdirectory.

## OCR anomalies (for future reference)

This book has **multiple re-set signature reprints**. Confirmed duplicates:
- Liber I pp. 54–64
- Liber II Cap. I pp. 87–98
- Liber II Cap. IX pp. 309–318
- Liber III Cap. VII pp. 707–718
- Liber IV Cap. II pp. 793–805
- Liber IV Cap. III pp. 837–850ish
- Liber IV Cap. V (OCR ln 57156–57256)

**OCR Casus/Caput number errors** are widespread — many III appear as `IH`, `IIX` for VIII, and transposed Roman numerals. Verify by content, not by OCR label.

## Style / workflow conventions

- **Faithful line-by-line English**, preserving Balduin's scholastic structure: *Reply*, numbered rationes, enumerations, patristic citations, biblical proofs. Preserve Latin phrases only where they carry technical weight.
- **Markdown structure**: `## Chapter N. Title` + optional *De casibus...* italic subline + `### Casus N. Question` + `*Reply.*` prose. Page-break before each new Cap. via ```` ```{=openxml} `<w:br w:type="page"/>` ```` block.
- **KJV Bible citations** — deferred to Stage 4.
- **Token discipline** (from memory `feedback-token-budget-discipline.md`): one volume-arc per chat, terse commits (<150 chars), no gratuitous file reads, `/compact` when needed, no subagents for solo work.

## Memory files to consult first (in new chat)

1. **`~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-balduin-casibus-handoff-2026-09-18.md`** — comprehensive T2–T33 summaries. **Read this first.**
2. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-methodica-1595-handoff-2026-09-08.md` — Kirchner canonical build-pipeline reference (closest precedent for Stage 4 KJV pass + Stage 5 Reedsy build).
3. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-symbolorum-1577-handoff-2026-09-08.md` — most recently closed Wittenberg-orthodoxy volume.

## Source metadata

- VD17: **3:307763U**
- Internet Archive: `bub_gb_us9YzllXDMsC` → `https://archive.org/download/bub_gb_us9YzllXDMsC/bub_gb_us9YzllXDMsC.pdf`
- PRDL author entry: `http://www.prdl.org/author_view.php?s=250&limit=10&a_id=531`
- No German counterpart, no modern critical edition, no known existing translation.
- Colophon (p. 1191): *Imprimebatur Francofurti ad Moenum* — actual printing done at Frankfurt am Main, though publisher/bookseller line names Wittenberg (Helwigius).
