# Kirchner Methodica 1595 — Handoff to fresh chat

**Task:** Finish rendering Timotheus Kirchner's *Methodica Explicatio* (Jena: Beyer, 1595) into English.

## Read these memories first (in order)

1. `feedback-token-budget-discipline` — **non-negotiable.** One volume-arc per chat, terse commits (<150 chars), no gratuitous file reads, `/compact` when context hits ~50%, no subagents.
2. `reference-scholastic-lutherans-workflow` — MD style, OCR handling, git etiquette.
3. `reference-methodica-1595-handoff-2026-09-08` — full running state, Q/Obj counters, all completed loci with tranche numbers.

## Current state (verified 2026-09-08)

- **Last commit:** `ec5f8e8` T89 = Locus XXXI De Poenitentia Part 5 (closing).
- **MD file:** `review/kirchner-methodica-1595.md` — ~11.5k lines. Loci I–XXXI complete. **Do not Read this file whole.** Use `git show HEAD:catechetical/kirchner-methodica-1595/review/kirchner-methodica-1595.md | tail -30` or `Read` with `offset` + small `limit` to see the end-of-file marker.
- **89 tranches committed this volume.**
- **PDF/DOCX build:** `pwsh -f build-shareable.ps1` from the volume root.

## Resume point

- **Next tranche:** T90.
- **Next locus:** XXXII De Libertate Christiana.
- **OCR line:** 40006 in `sources-original/Kirchner_Methodica_1595_Beyer.txt`.

## Remaining scope

### Main body (15 loci, OCR 40006–48728)

| Locus | OCR lines | Est. tranches |
|---|---|---|
| XXXII De Libertate Christiana | 40006–40521 | 1 |
| XXXIII | 40522–40956 | 1 |
| XXXIV | 40957–41415 | 1 |
| XXXV | 41416–42358 | 2 |
| XXXVI | 42359–42832 | 1 |
| XXXVII | 42833–43369 | 1 |
| XXXIIX (=XXXVIII) | 43370–44193 | 2 |
| XXXIX | 44194–44717 | 1 |
| XL | 44718–44938 | 1 |
| XLI | 44939–45497 | 1 |
| XLII | 45498–45616 | 1 |
| XLIII | 45617–46218 | 1 |
| XLIV | 46219–46562 | 1 |
| XLV | 46563–46921 | 1 |
| XLVI | 46922–48728 | 3 |

**Main-body total: ~21 tranches.**

### Appendix / short-form second cycle (OCR 48729–end, ~2700 lines)

Fresh sequence starting "Locus I." through "XXIV." — appears to be a compressed catechetical index/summary. Estimate 6–10 tranches. Treat as its own sub-arc — decide with user whether to include before starting.

## First-tranche checklist (T90)

1. Confirm resume: `git log --oneline -1` should show `ec5f8e8`.
2. Read only the last ~30 lines of the MD file to see the closing marker.
3. Read OCR lines 40006–40521 (Locus XXXII) — that's ~500 lines, one Read call.
4. Append T90 by replacing the end-marker with the new locus content + a new end-marker.
5. Commit with title ≤150 chars: `Kirchner Methodica 1595 T90: Locus XXXII De Libertate Christiana` + Co-Authored-By trailer. No multi-paragraph tag summary.

## Style rules already established

- Locus header: `# Locus XXX. Of the [Topic]` + `### *De [Latin Title]*` on next line.
- Question header: `## Question N. [English question]` then body opens with the question repeated bold + Luther marginals `[*[T. 4/1, p. 397*]*]`.
- Objection header: `### Objection N. **[Latin syllogism translated]**` then `**Respondeo**: ...`
- Scripture always **bold**: `**Rom. 3:24**: *"Justified freely,"* etc.`
- Separator between Q/Obj units: `— ❦ —`
- End-of-tranche marker (last line of file): `*[Locus XXX Part N closes. Part N+1 (...) follows in TXX. XXX top-level Q + YYY Obj rendered so far.]*`

## When Locus XLVI closes

Ask the user whether to render the short-form appendix (OCR 48729+) in this chat, defer to a follow-up chat, or omit. Update `reference-methodica-1595-handoff-2026-09-08` memory to reflect final state either way.

## When to stop this chat

Per the token-budget discipline: if the context bar hits ~50%, run `/compact`. If it hits ~75% or session wall-time reaches 4 hours, stop cleanly at a locus boundary, update the handoff memory, and tell the user to open a fresh chat for the next arc.
