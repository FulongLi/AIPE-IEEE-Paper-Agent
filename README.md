# IEEE Paper Agent

A modular IEEE paper-production agent for turning a research idea into an
evidence-linked paper plan and a real venue-specific LaTeX manuscript workspace.
Python 3.10+ is sufficient for all repository tools and tests; no Python packages
are required. A LaTeX distribution is needed separately for PDF compilation.

## Five Layers

1. **Core IEEE paper-production engine** — `core/SKILL.md`, `core/workflows/`, and
   `core/policies/` are the single maintained instruction layer. Writing guidance,
   research reasoning, citation rules, and reviewer-response procedures live here.
2. **Venue profiles and LaTeX templates** — `venues/<id>/profile.json` identifies
   the actual entry file, document class/options, required front matter, and
   normalization rules. Official files live in `venues/<id>/template/`.
3. **Optional domain packs** — `domains/power-electronics/` contains curated
   knowledge, terminology, and literature-maintenance guidance. Generic papers
   work without a domain pack. The existing library remains in `PE_IEEE_reference/`.
4. **Planning/artifact templates** — `artifacts/` contains idea briefs, paper plans,
   evidence matrices, figure/table plans, and citation-audit/verification records.
5. **Tools and validation** — `scripts/` initializes manuscripts, indexes references,
   audits citations and venue structure, and builds portable releases; `tests/`
   guards these contracts with standard-library Python tests.

```text
AIPE-IEEE-Paper-Agent/
├── AGENTS.md
├── core/
│   ├── SKILL.md
│   ├── policies/
│   ├── workflows/
│   └── agents/openai.yaml
├── venues/
│   ├── ieee-conference/{profile.json,template/}
│   ├── ieee-transactions/{profile.json,template/}
│   ├── ieee-access/{profile.json,template/}
│   ├── ieee-ojpel/{profile.json,template/}
│   ├── ieee-tai/{profile.json,template/}
│   ├── ieee-ojcsys/{profile.json,template/}
│   └── archive/
├── domains/power-electronics/{knowledge/,terminology/,literature/}
├── PE_IEEE_reference/
├── artifacts/
├── scripts/
├── tests/
└── dist/                         # generated, ignored by Git
```

## Start With a Research Idea

Open the repository and use:

```text
Follow AGENTS.md and core/workflows/idea-to-paper.md. My research idea is:
<paste idea>. Develop a paper plan with testable questions and evidence gaps.
```

The execution path is: research idea → Problem/Gap/Idea/Evidence/Impact spine →
research questions → 2–4 verifiable contribution claims → evidence and figure/table
plan → paper plan → venue profile → real template initialization → optional domain
knowledge → evidence-based drafting → citation verification → LaTeX/venue audit →
publication-readiness review.

Each important question maps to an experiment, figure, table, derivation, theorem,
simulation, or other evidence. Missing evidence is blocking, important, or optional.
Draft Method → Experiment setup → Results → Introduction → Related Work → Abstract
→ Conclusion where appropriate. Never invent results or reference metadata.
Detailed writing and revision guidance remains in the canonical core workflows.

## Create a Manuscript

```bash
python scripts/create-manuscript.py --list-venues
python scripts/create-manuscript.py my-paper --venue ieee-transactions --title "Working Title"
python scripts/create-manuscript.py converter-paper --venue ieee-ojpel --domain power-electronics
```

Supported IDs are `ieee-conference`, `ieee-transactions`, `ieee-access`,
`ieee-ojpel`, `ieee-tai`, and `ieee-ojcsys`. See `venues/README.md` for details.
If omitted, `--venue` defaults explicitly to `ieee-conference`.
`--root <directory>` changes output, not the location of bundled assets.
`--title` accepts plain text and escapes LaTeX special characters.

The generator reads the selected template's actual entry, preserves its preamble,
class and front-matter order, replaces sample metadata with TODOs, and inserts
section files in place of sample prose. Transactions uses `[lettersize,journal]`;
Access keeps its specialized class, author/address macros, abstract placement,
font setup, and EOD; OJPEL keeps its logo, dates, and affiliation structure. TAI's
impact statement and OJCSYS's editor/category structure also survive normalization.

Generated workspaces contain `main.tex`, `sections/`, `figures/`, `tables/`, `refs/`,
`styles/`, `notes/`, and `build/`. Official support files stay at their original
relative locations beside `main.tex`; this preserves internal class/font/logo
lookups on Overleaf. `styles/` is available for author-owned support files. The
abstract fragment is text only; its environment remains in the real venue entry.
`notes/venue-profile.json` records the selected configuration.

Upload the workspace to Overleaf with `main.tex` as the main document, or run
`latexmk -pdf main.tex` from the workspace with a suitable TeX distribution.
Initialization leaves explicit TODOs and is not a submission-ready paper. Replace
metadata, add evidence and references, check current venue requirements, and remove
unused sample assets before submission. Source templates are never modified.

## Reference Collection and Audits

All original BibTeX, Markdown, HTML, and reference assets remain in
`PE_IEEE_reference/`. The index records keys, titles, authors, years, venues,
DOI/URL fields, source files, topics, duplicate keys, and metadata status.
`doi-present` and `url-present` do not mean external verification succeeded.

```bash
python scripts/build-reference-index.py
python scripts/check-citations.py manuscripts/my-paper --write-audit
python scripts/check-latex.py manuscripts/my-paper
```

The index builder also accepts `--ref-dir <directory> --output <file>` for another
collection. Defaults resolve relative to the installed script's assets, so these
tools work outside the repository current directory. The citation checker returns
nonzero for missing entries or duplicate keys. Its generated report is separate
from manual source verification in `notes/citation-verification.md`.

The LaTeX checker verifies static structure, relative paths, required venue
commands, and unchanged official assets. PDF compilation, visual inspection,
external citation verification, and scientific review remain separate checks.

For domain work, see `domains/power-electronics/README.md`. Curated chapter notes,
concept map, language bank, source manifest, and MinerU instructions are preserved.
Raw book conversions, private caches, and `books/` stay out of releases.

## Portable Packages and Validation

```bash
python -m unittest discover -s tests -v
python scripts/package-release.py
```

Packaging builds Codex skill, Codex plugin marketplace, and Claude skill ZIPs in
`dist/`. `references/` is generated from canonical core workflows/policies with
portable paths; `generated-sources.json` records provenance and checksums. There
is no separately maintained portable workflow tree. Runtime assets/scripts are
inside each skill, including the plugin's skill. See `INSTALL.md`.

For a smaller generic package:

```bash
python scripts/package-release.py --without-domain --venue ieee-transactions --dist dist/generic
```

## Migration and Compatibility

- The two editable workflow/reference trees were consolidated into `core/`.
  Source skill installation is replaced by repository mode or generated packages.
- Official venue templates moved into `venues/<id>/template/`; older conference
  and supplementary IEEEtran variants are retained under `venues/archive/`.
- Curated power-electronics content moved into the optional domain pack; planning
  templates moved into `artifacts/`. Original scientific content is preserved.
- `scripts/` command locations and `PE_IEEE_reference/` are unchanged.
- Manuscript initialization now takes `--venue`; the old `--template` switch exits
  with migration guidance instead of silently generating the wrong venue.
- `--no-clean` remains accepted by the packager; only its named generated package
  trees are replaced, and unrelated files under the output root are preserved.

Semantic/RAG literature search, web synchronization of venue rules, automatic
experimental results, advanced paper scoring, and multi-agent orchestration are
outside this architecture consolidation.

## AIPE ecosystem

[Capability manifest](aipe.yaml) and [Core evidence mapping](docs/aipe-integration.md) make this research agent discoverable without changing the paper-production engine or venue templates.
