# Scriptorium — Scholastic Lutherans Translation Corpus

An ongoing English-translation programme of the 22-work Lutheran-orthodoxy corpus (c. 1550–1760). Sole translator: Cherinet, working under the "Scholastic Lutherans" team name.

*"Scriptorium"* — the medieval monastic writing-room where Latin texts were copied, edited, and rendered fresh for a new audience. Same idea, seven centuries later.

## Programme

The corpus is drawn from a canonical priority list from Seth Kasten (Aug 2026) plus a handful of companion works added along the way. Everything is translated from the original Latin (or occasionally early modern German), with faithful line-by-line English rendering — no summary mode, no paraphrase — and typeset for print in a house format modelled on Reedsy's hardback standard.

The completed [Praetorius *Syntagma Musicum* trilogy](https://github.com/Cherireal7/syntagma-musicum) (elsewhere) is the reference implementation of every workflow convention used here.

## Status

**Volumes closed (translation + Scripture-conformance pass + print-ready PDF):**

- Kirchner, *Methodica Explicatio* (Jena 1595) — closed 2026-09-12
- Selnecker, *Symbolorum … Exegesis* (Leipzig 1577) — build complete 2026-09-18
- Balduin, *Tractatus … de Casibus Conscientiae* (Wittenberg 1628) — closed 2026-09-21

**Volumes shipped as translation + PDF (some passes deferred):** Chytraeus 1594 Catechism, Selnecker *Institutes* Pars I + II, Grosse *Die alten Tröster*, Andreae *Disputationes*, Quenstedt *Exercitationes*, Kirchner *Enchiridion*.

**In progress:** Flacius, *Catalogus Testium Veritatis* (~58%).

**Queued:** Weimar Bible (1640), Hirschberg Bible (1728), Walch *Streitigkeiten*, Dannhauer *Hodomoria* + *Mysterium Syncretismi*, Musculus *Loci Communes*, Baumgarten *Glaubenslehre*, Buddeus *Isagoge*, Calixt *Apparatus*, Walch *Bibliotheca Theologica*, Pfaff *Introductio*, Veltheim + Hebenstreit (philosophy), Wallmann *Theologiebegriff* (secondary).

## Repository layout

```
shared/                          shared tooling and specifications
├── translation-pipeline.md      end-to-end 5-stage workflow spec
├── formatting-standard.md       house print format (trim, fonts, front matter)
├── reference-custom.docx        locked pandoc reference DOCX
├── terms.yaml                   master glossary across volumes
├── build-indices.py             Scripture + Fathers + Rerum index builder
├── apply-kjv-pass.py            Scripture-conformance pass helper
└── fonts/                       bundled IM Fell English (SIL OFL 1.1)

study-bibles/       weimar-1640, hirschberg-1728
dogmatics/          selnecker-institutiones (Pars I + II), selnecker-symbolorum-1577,
                    musculus-loci-communes, baumgarten-glaubenslehre-1759
polemics/           dannhauer-hodomoria-1655, dannhauer-mysterium-syncretismi-1648,
                    flacius-catalogus-testium-1556
pastoral/           balduin-casibus-conscientiae-1628, grosse-alten-troester-1900
catechetical/       chytraeus-catechismus-1594, andreae-disputationes,
                    kirchner-enchiridion, kirchner-methodica-1595
philosophy/         veltheim-institutiones-metaphysicae, hebenstreit-philosophia-prima
encyclopedias/      walch-streitigkeiten, walch-bibliotheca-theologica-1757,
                    buddeus-isagoge-1727, quenstedt-exercitationes,
                    calixt-apparatus-1628, pfaff-introductio-1724
church-orders/      sehling (Kirchenordnungen)
secondary/          wallmann-theologiebegriff-1961
```

Each per-work directory follows a consistent pattern:

```
<work-slug>/
├── sources-original/           OCR / facsimile / typescript source (git-ignored if large)
├── review/<work-slug>.md       master translation file
├── notes.md                    work-specific gotchas + tranche plan
├── HANDOFF.md                  self-contained brief for a fresh translator chat
├── build-shareable.ps1         pandoc → DOCX → LibreOffice → PDF build
└── reference-<slug>.docx       volume-specific pandoc reference (running headers, TOC)
```

## Workflow

The full end-to-end pipeline — source identification, OCR extraction, translation mechanics, post-translation Scripture-conformance audit, and print typesetting — is documented in [`shared/translation-pipeline.md`](shared/translation-pipeline.md). The house print-format spec (trim, margins, fonts, front-matter templates) lives in [`shared/formatting-standard.md`](shared/formatting-standard.md).

## License

- **Original Latin/German sources**: public domain.
- **English translations, editorial apparatus, and typesetting in this repository**: Copyright © 2026 Scholastic Lutherans / Cherinet Demeke, released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- **IM Fell English fonts** in `shared/fonts/`: SIL Open Font License 1.1 (see bundled `OFL.txt`).
