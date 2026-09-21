# Handoff — Balduin, *Tractatus Posthumus de Casibus Conscientiae* (Wittenberg, 1628)

**Read this first.** Self-contained brief for whoever picks up the volume in a fresh chat. **Stages 1+2 and Stage 3 T1 through T30 are done — Liber I is COMPLETE, Liber II is COMPLETE, Liber III is COMPLETE, and Liber IV Cap. I–IX are COMPLETE (~88% of volume body).** The next tranche is T31 (Liber IV Cap. X *De clavium usu* through end; ~130 pp remaining, ~1-2 tranches to volume-close). T2–T30 detail is in the git log (`git log --oneline`) — each Balduin-Casibus commit narrates one full chapter. Everything needed to pick up at T31 is here or in the paths named here.

## What this project is

Translating **Friedrich Balduin** (1575–1627) · ***Tractatus Luculentus, Posthumus, Toti Reipublicae Christianae Utilissimus, de Materiâ rarissimè antehac enucleatâ, Casibus nimirum Conscientiae*** (Wittenberg: Paulus Helwigius, 1628) from Latin into modern English.

**Historical significance.** This is the **first single-author Lutheran casuistry** — Balduin (Hutter's successor at Wittenberg, †1627) is the first Protestant to work moral theology in the form of *cases of conscience* in a serious systematic manner. The *Tractatus* was published posthumously the year after his death and was repeatedly reprinted through the 17th century. It fills a genre gap in our library: we have Wittenberg dogmatic (Selnecker, Kirchner), catechetical (Kirchner Enchiridion, Chytraeus), and polemical work, but no pastoral-casuistry.

## Volume status — quick view

| Book | Scope | Status |
|------|-------|--------|
| Front matter | Dedicatoria + Faculty Praefatio + Buchner epigram | ✅ T1 |
| Liber I | Conscience *in genere* (16 Capita + Steuber Additamentum) | ✅ T2–T3 |
| Liber II | God + religion (18 Capita) | ✅ T4–T15 |
| Liber III | Celestial spirits: angels, demons, magi, divination, specters (7 Capita) | ✅ T16–T22 |
| Liber IV Cap. I | *De corpore hominis* (body, 15 Casus) | ✅ T23 |
| Liber IV Cap. II | *De cultu animi* (soul-cultivation, 9 Casus) | ✅ T24 |
| Liber IV Cap. III | *De bonis fortunae* (wealth, 9 Casus) | ✅ T25 |
| Liber IV Cap. IV | *De vitae generibus* (kinds of life/calling, 10 Casus) | ✅ T26 |
| Liber IV Cap. V | *De vocatione ad ministerium verbi* (Word-ministry vocation, 12 Casus) | ✅ T27 |
| Liber IV Cap. VI | *De ordinatione ministrorum* (ordination of ministers, 7 Casus) | ✅ T28 |
| Liber IV Cap. VII | *De officio concionatorum* (preachers' office, 6 Casus) | ✅ T29 |
| Liber IV Cap. VIII | *De administratione baptismi* (baptism, 10 Casus) | ✅ T30 |
| Liber IV Cap. IX | *De administratione coenae Dominicae* (Lord's Supper, 8 Casus) | ✅ T30 |
| Liber IV Cap. X–end | Keys/absolution, magistrate, subjects, marriage, family, death | ⏳ T31 |

**~130 physical pages remain / ~1-2 tranches to volume close. Overall progress: ~88%.**

## Immediate resume point (T31)

Open OCR at **`sources-original/balduin-casibus-1628.txt`** line **61058** (physical page 979). The `CAPUT X.` header starts Cap. X *De casibus conscientiae circa usum clavium* (use of the keys — binding + loosing = absolution + confession + discipline). Cap. XI (subjects/subditis) appears at ln 62506 (physical p. 995); Cap. XII (spouses) at ln 63188; Cap. XV (children/parents/servants) at ln 65070; Cap. XVI (death/burial) at ln 67595. Body ends ~ln 69119 with AMEN doxology.

**Note on chapter numbering**: original book skips from Cap. XII to Cap. XV (Cap. XIII-XIV do not exist or are unlabeled), and skips Cap. XI in some places — verify by content, not by header numbers.

**Preamble to note (Cap. X):** Keys of Church = power which Lord conceded to his ministers in Church for blessing + cursing men (Deut 30:19 proposing life/death/blessing/curse); two contrary effects of ministry (benediction + malediction); two-fold keys — one *of loosing* (Matt 16:19), other *of binding* (Matt 18:18) — committed not only to Apostles but to whole Church, exercised through ministers of the word.

## Remaining tranche plan

- **T31** — Cap. X *De clavium usu* + Cap. XI *De subditis* + Cap. XII *De officio conjugum* + Cap. XV *De liberis+parentibus+servis* + Cap. XVI closing death chapter (ln 61058–69119, ~130 pp — LARGE; may split into T31a + T31b if unwieldy; consider T31a = Cap. X + XI ~35pp, T31b = Cap. XII + XV + XVI ~95pp)

Chapter titles in remaining book (approximate, from running headers + content):
- Cap. VI — Ordination of ministers (ln 57534)
- Cap. VII/VIII — Office of ministers (ln 58788 area)
- Cap. X — *De magistratu politico* (political magistrate, ln 61058)
- Cap. XI — *De subditis* (subjects, ln 62506)
- Cap. XII — *De officio conjugum* (spouses, ln 63188)
- Cap. XV — *De liberis + parentibus + servis* (children, parents, servants, ln 65070)
- Cap. XVI — Closing chapter, likely death/burial/last-things (ln 67595)

Book ends at ~ln 69119 with **AMEN body-doxology** on physical p. 1109. Back matter (INDEX I Scripture + INDEX II Fathers + INDEX III Rerum) pp. 1110–1189 is **DEFERRED** per plan — regenerable from finished English MD if wanted.

## Where the files are

- **OCR source**: `sources-original/balduin-casibus-1628.txt` (75,390 lines from PyMuPDF extraction; use `sources-original/extract.py` to re-extract if ever needed).
- **Translation MD** (append here): `review/balduin-casibus-conscientiae-1628.md` — currently ~T30 in length (~11,700 lines). Append T31 by replacing the *[T30 pickup / VOLUME REMAINING]* placeholder block at the end.
- **Build machinery** (for Stage 5): `build-shareable.ps1`, `update-fields.py`, `reference-balduin-casibus.docx` — Kirchner-precedent pipeline.
- **Notes**: `notes.md` (source-plan, tranche-plan, structural map).

## Watch out for — OCR anomalies

This book has **multiple re-set signature reprints**. Confirmed duplicates so far:
- Liber I pp. 54–64 (reprints Liber I Cap. XII material)
- Liber II Cap. I pp. 87–98 (partial re-print of Cap. I Casus I–VI)
- Liber II Cap. IX pp. 309–318 (reprints oath-chapter mid-section)
- Liber III Cap. VII pp. 707–718 (reprints Cap. VII preamble + Casus I–III)
- Liber IV Cap. II pp. 793–805 (reprints Cap. II Casus VII–IX = fear/joy/liberal-arts)
- Liber IV Cap. III pp. 837–850ish (reprints Cap. II Casus IX tail + Cap. III preamble + early Casus)
- Liber IV Cap. V (OCR ln 57156–57256) has another duplicate of Cap. V Casus VIII–IX region
- Liber IV Cap. VI OCR Casus numbering is **corrupt** — visible Casus labels read I, II (as "IK"), III (embedded), V, VI, VII (as "PASUS"), VIII — jumping directly from III to V and mis-labeling; content-analysis shows **7 true Casus** (I-VII sequential). Anchor on content, not on Roman-numeral labels.

**Rule:** Always compare content when Casus numbers seem to jump or repeat. Skip the duplicate, anchor on the authoritative first-print portion.

**OCR Casus/Caput number errors** — many `CASUS III` labels appear as `CASUS IH`, `CASUS IIX` (VIII), `CAPUT IIX` (VIII), Roman-numeral transpositions like `IV` where the printer set `VI`. Verify by content when in doubt.

## Style / workflow conventions

- **One tranche = one Cap. entirely**, if manageable (~30–40 pp). Larger chapters may split.
- **Faithful line-by-line English**, preserving Balduin's scholastic structure: *Reply*, numbered rationes, 3-fold/5-fold enumerations, patristic citations, biblical proofs. Rewrite through OCR corruption silently. Preserve Latin phrases only where they carry technical weight (e.g., *sacerdotium*, *jus patronatus*, *nutritius*, *symmista*).
- **Markdown structure**: `## Chapter N. Title` + optional *De casibus...* italic subline + `### Casus N. Question` + `*Reply.*` prose. Page-break before each new Cap. via ```` ```{=openxml} `<w:br w:type="page"/>` ```` block (see prior Cap. openings).
- **KJV Bible citations** — deferred to Stage 4 (Kirchner-style batch pass at end).
- **Commit format**: `Balduin Casibus T{N}: Liber IV Cap. {X} {Title} entirely (N Casus, OCR ln XXX-XXX / phys pp. XXX-XXX). <brief description>. <OCR duplicate note if relevant>.`
- **Token discipline** (from memory `feedback-token-budget-discipline.md`): one volume-arc per chat, terse commits (<150 chars), no gratuitous file reads, `/compact` when needed, no subagents for solo work.

## Memory files to consult first (in new chat)

1. **`~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-balduin-casibus-handoff-2026-09-18.md`** — comprehensive T2–T27 summaries + all structural notes + OCR-anomaly catalog. **Read this first.**
2. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/feedback-token-budget-discipline.md` — token discipline.
3. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-scholastic-lutherans-workflow.md` — stage-3 translation mechanics.
4. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-methodica-1595-handoff-2026-09-08.md` — Kirchner canonical build-pipeline reference (closest precedent).
5. `~/.claude/projects/C--Users-hp-documents-github-scholastic-lutherans/memory/reference-symbolorum-1577-handoff-2026-09-08.md` — most recently closed Wittenberg-orthodoxy volume.

## First actions in new chat

1. Read the memory `reference-balduin-casibus-handoff-2026-09-18.md` for full T2–T30 context.
2. Read the last ~50 lines of `review/balduin-casibus-conscientiae-1628.md` to see the T30 close + T31 placeholder block.
3. Read OCR `sources-original/balduin-casibus-1628.txt` ln 61058 onward to identify Cap. X-XVI Casus boundaries (whole rest of body).
4. Draft T31 (Cap. X through XVI, ~130 pp) — may split into T31a + T31b if unwieldy — replace T31 placeholder, commit with terse message.
5. Update handoff memory `reference-balduin-casibus-handoff-2026-09-18.md` with T31 summary. If T31 closes body: mark VOLUME BODY COMPLETE and move to Stage 4 (KJV audit pass) + Stage 5 (Reedsy build).

**Volume estimate to close:** 1-2 more tranches (T31 alone or T31a+T31b) then Stage 4 (KJV audit pass) + Stage 5 (Reedsy build). Follow **Symbolorum 1577** (most recent close) and **Methodica 1595** (canonical build pipeline) as closest precedents.

## Source metadata

- VD17: **3:307763U**
- Internet Archive: `bub_gb_us9YzllXDMsC` → `https://archive.org/download/bub_gb_us9YzllXDMsC/bub_gb_us9YzllXDMsC.pdf`
- PRDL author entry: `http://www.prdl.org/author_view.php?s=250&limit=10&a_id=531`
- No German counterpart, no modern critical edition, no known existing translation.
- Colophon (p. 1191): *Imprimebatur Francofurti ad Moenum* — actual printing done at Frankfurt am Main, though publisher/bookseller line names Wittenberg (Helwigius).
