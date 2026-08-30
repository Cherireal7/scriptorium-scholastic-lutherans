# Scholastic Lutherans — Translation Corpus

*Private working repository. All rights reserved.*

The Scholastic Lutherans team's translation program of the 22-work Lutheran-orthodoxy corpus (~1550–1760). Sole author: Cherinet, working under the "Scholastic Lutherans" team name.

The completed [Praetorius *Syntagma Musicum* trilogy](https://github.com/Cherireal7/syntagma-musicum) (elsewhere) is the reference implementation of every workflow convention used here.

## Repository layout

```
scholastic-lutherans/
├── shared/
│   ├── reference-custom.docx       ← locked Hülsemann-style DOCX template
│   ├── terms.yaml                   ← master glossary (all works)
│   ├── build.ps1                    ← pandoc + LibreOffice one-shot
│   └── editions.md                  ← modern-critical editions registry
├── study-bibles/
│   ├── weimar-1640/
│   └── hirschberg-1728/
├── dogmatics/
│   ├── selnecker-institutiones-1573/
│   ├── musculus-loci-communes/
│   └── baumgarten-glaubenslehre-1759/
├── polemics/
│   ├── dannhauer-hodomoria-1655/
│   ├── dannhauer-mysterium-syncretismi-1648/
│   └── flacius-catalogus-testium-1556/
├── pastoral/
│   ├── balduin-casibus-conscientiae-1628/
│   └── grosse-alten-troester-1614/
├── catechetical/
│   ├── chytraeus-catechismus-1594/
│   └── andreae-disputationes/
├── philosophy/
│   ├── veltheim-institutiones-metaphysicae/
│   └── hebenstreit-philosophia-prima/
├── encyclopedias/
│   ├── walch-streitigkeiten/
│   ├── walch-bibliotheca-theologica-1757/
│   ├── buddeus-isagoge-1727/
│   ├── quenstedt-exercitationes/
│   ├── calixt-apparatus-1628/
│   └── pfaff-introductio-1724/
└── secondary/
    └── wallmann-theologiebegriff-1961/
```

Each per-work directory follows the Praetorius pattern:

```
<work-slug>/
├── sources-original/     ← OCR / facsimile / typescript source
├── review/<work>.md      ← master translation file
├── latex/                ← optional
└── notes.md              ← work-specific gotchas
```

## Workflow

See the private memory files:
- `~/.claude/projects/C--Users-hp/memory/reference_scholastic-lutherans-workflow.md`
- `~/.claude/projects/C--Users-hp/memory/reference_scholastic-lutherans-glossary.md`
- `~/.claude/projects/C--Users-hp/memory/project_scholastic-lutherans-program.md`

## Current status

**Kick-off work:** Chytraeus 1594 Catechism (`catechetical/chytraeus-catechismus-1594/`).
