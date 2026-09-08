# Kirchner Methodica 1595 — Handoff to fresh chat

**Task:** Finish rendering Timotheus Kirchner's *Methodica Explicatio* (Jena: Beyer, 1595) into English.

## Read these memories first (in order)

1. `feedback-token-budget-discipline` — **non-negotiable.** One volume-arc per chat, terse commits (<150 chars), no gratuitous file reads, `/compact` when context hits ~50%, no subagents.
2. `reference-scholastic-lutherans-workflow` — MD style, OCR handling, git etiquette.
3. `reference-methodica-1595-handoff-2026-09-08` — full running state, Q/Obj counters, all completed loci with tranche numbers.

## Current state (verified 2026-09-08 end of T99 second follow-up chat)

- **Last commit:** `2384598` T99 = Locus XXXIX De Morte COMPLETE.
- **MD file:** `review/kirchner-methodica-1595.md` — ~13.5k lines. Loci I–XXXIX complete. **Do not Read this file whole.** Use `git show HEAD:catechetical/kirchner-methodica-1595/review/kirchner-methodica-1595.md > /tmp/md.txt; tail -30 /tmp/md.txt` (bash) or `Read` with `offset` + small `limit` to see the end-of-file marker.
- **99 tranches committed this volume.**
- **PDF/DOCX build:** `pwsh -f build-shareable.ps1` from the volume root.

## Resume point

- **Next tranche:** T100.
- **Next locus:** XL De Sepultura.
- **OCR line:** 44718 in `sources-original/Kirchner_Methodica_1595_Beyer.txt`.

## Remaining scope

### Main body (7 loci, OCR 44718–48728)

| Locus | OCR lines | Est. tranches |
|---|---|---|
| XL De Sepultura | 44718–44938 | 1 |
| XLI | 44939–45497 | 1 |
| XLII | 45498–45616 | 1 |
| XLIII | 45617–46218 | 1 |
| XLIV | 46219–46562 | 1 |
| XLV | 46563–46921 | 1 |
| XLVI | 46922–48728 | 3 |

**Main-body total remaining: ~9 tranches.**

### Appendix / short-form second cycle (OCR 48729–end, ~2700 lines)

Fresh sequence starting "Locus I." through "XXIV." — appears to be a compressed catechetical index/summary. Estimate 6–10 tranches. Treat as its own sub-arc — decide with user whether to include before starting.

## First-tranche checklist (T100)

1. Confirm resume: `git log --oneline -1` should show `2384598`.
2. Read only the last ~30 lines of the MD file to see the closing marker.
3. Read OCR lines 44718–44938 (Locus XL De Sepultura) — that's ~220 lines, one Read call.
4. Append T100 by replacing the end-marker with the new locus content + a new end-marker.
5. Commit with title ≤150 chars: `Kirchner Methodica 1595 T100: Locus XL De Sepultura` + Co-Authored-By trailer. No multi-paragraph tag summary.

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
