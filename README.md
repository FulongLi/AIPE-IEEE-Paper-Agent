# AIPE — IEEE Paper Agent

AIPE IEEE Paper Agent is the research-writing agent of **AI for Power Engineering**: a modular IEEE
paper-production engine that turns a research idea into an evidence-linked paper plan and a real,
venue-specific LaTeX manuscript workspace. The maintained instruction layer (`core/`) carries the writing,
citation and reviewer-response rules; venue profiles wrap the official IEEE templates; an optional
power-electronics domain pack and the `PE_IEEE_reference/` library add curated knowledge. Within AIPE it
consumes Core engineering evidence and produces manuscript plans, workspaces and audit reports; it never
invents results or reference metadata.

## Features

- Idea-to-paper workflow: Problem/Gap/Idea/Evidence/Impact spine, research questions, 2–4 verifiable
  contribution claims, evidence and figure/table plan
- Six venue profiles with official templates (`ieee-conference`, `ieee-transactions`, `ieee-access`,
  `ieee-ojpel`, `ieee-tai`, `ieee-ojcsys`); older variants archived
- Manuscript generator that preserves each template's preamble, class options and front-matter order and
  inserts section files with explicit TODOs
- Reference index of the bundled BibTeX/Markdown/HTML collection, citation audit and static LaTeX/venue
  audit
- Portable Codex skill, Codex plugin marketplace and Claude skill packages built from the canonical
  workflows with provenance checksums
- Standard-library Python 3.10+ tools and tests; a LaTeX distribution is needed only for PDF compilation

## Installation

No Python packages are required. Open the repository in Codex or Claude and start with `AGENTS.md` and
`core/SKILL.md`, or build the self-contained packages:

```sh
python scripts/package-release.py
```

[INSTALL.md](INSTALL.md) covers repository mode, release packages and host-specific installation.

## Usage

```sh
python scripts/create-manuscript.py --list-venues
python scripts/create-manuscript.py my-paper --venue ieee-transactions --title "Working Title"
python scripts/check-latex.py manuscripts/my-paper
python scripts/check-citations.py manuscripts/my-paper --write-audit
python -m unittest discover -s tests -v
```

Upload the workspace to Overleaf with `main.tex` as the main document, or run `latexmk -pdf main.tex`
with a TeX distribution. Initialisation leaves explicit TODOs; it is not a submission-ready paper. For a
research idea, ask your agent to follow `AGENTS.md` and `core/workflows/idea-to-paper.md`.

## Project Information

- Version: 0.1.0 (`VERSION`)
- Status: Alpha (`aipe.yaml`: status `active`, maturity `usable`)
- Developer: Fulong Li
- Organisation: Spirit Connect / AIPE Labs
- License: not declared at repository level (`aipe.yaml`: `NOASSERTION`; no LICENSE file).
  `release-config.json` sets `MIT` in the generated package manifests; the official IEEE templates under
  `venues/` and the assets in `PE_IEEE_reference/` retain their own rights

## Documentation

- [Architecture: five layers, repository map, execution path, migration and compatibility](docs/architecture.md)
- [Usage: research ideas, manuscript creation, reference audits, portable packages](docs/usage.md)
- [INSTALL.md](INSTALL.md) · [AGENTS.md](AGENTS.md) · [core/SKILL.md](core/SKILL.md)
- [Venue profiles and templates](venues/README.md) ·
  [Power-electronics domain pack](domains/power-electronics/README.md)
- [AIPE integration and Core evidence mapping](docs/aipe-integration.md) · [Capability manifest](aipe.yaml)
