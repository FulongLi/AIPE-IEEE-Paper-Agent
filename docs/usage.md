# Usage: research ideas, manuscript creation, reference audits and portable packages

Python 3.10+ is sufficient for all repository tools and tests; no Python packages are
required. A LaTeX distribution is needed separately for PDF compilation.

## Start with a research idea

Open the repository and use:

```text
Follow AGENTS.md and core/workflows/idea-to-paper.md. My research idea is:
<paste idea>. Develop a paper plan with testable questions and evidence gaps.
```

The agent follows the execution path described in [architecture.md](architecture.md):
research idea → research questions → verifiable contribution claims → evidence plan →
paper plan → venue profile → template initialization → drafting → citation verification →
LaTeX/venue audit → publication-readiness review.

## Create a manuscript

```bash
python scripts/create-manuscript.py --list-venues
python scripts/create-manuscript.py my-paper --venue ieee-transactions --title "Working Title"
python scripts/create-manuscript.py converter-paper --venue ieee-ojpel --domain power-electronics
```

Supported IDs are `ieee-conference`, `ieee-transactions`, `ieee-access`,
`ieee-ojpel`, `ieee-tai`, and `ieee-ojcsys`. See [`venues/README.md`](../venues/README.md) for details.
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

## Reference collection and audits

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

For domain work, see [`domains/power-electronics/README.md`](../domains/power-electronics/README.md).
Curated chapter notes, concept map, language bank, source manifest, and MinerU
instructions are preserved. Raw book conversions, private caches, and `books/` stay
out of releases.

## Portable packages and validation

```bash
python -m unittest discover -s tests -v
python scripts/package-release.py
```

Packaging builds Codex skill, Codex plugin marketplace, and Claude skill ZIPs in
`dist/`. `references/` is generated from canonical core workflows/policies with
portable paths; `generated-sources.json` records provenance and checksums. There
is no separately maintained portable workflow tree. Runtime assets/scripts are
inside each skill, including the plugin's skill. See [`INSTALL.md`](../INSTALL.md).

For a smaller generic package:

```bash
python scripts/package-release.py --without-domain --venue ieee-transactions --dist dist/generic
```
