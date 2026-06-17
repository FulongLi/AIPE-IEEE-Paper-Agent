# IEEE Paper Agent

Current version: `0.1.0`

A LaTeX template and writing-skill repository for planning, drafting, organizing, and reviewing IEEE-style research papers.

This repository helps authors turn research ideas into paper plans first, then into IEEE/Overleaf-ready LaTeX manuscript workspaces with explicit evidence and citation checks.

## Start With Codex

Open this repository in Codex and use this prompt:

```text
Use this repository as an IEEE paper-writing assistant. Follow AGENTS.md and workflows/idea-to-paper.md. My research idea is: <paste idea>. Help me turn it into a publishable paper plan.
```

Codex should use:

- `AGENTS.md` for repository-level operating instructions
- `skills/ieee-paper-latex-writing/SKILL.md` for the core writing and LaTeX workflow
- `workflows/idea-to-paper.md` for idea-to-paper planning
- `knowledge-base/power-electronics-foundations/` for power electronics terminology and concept notes
- `PE_IEEE_reference/` for repository-local power electronics reference candidates
- `templates/` for reusable idea briefs and paper plans

## Install as a Skill or Plugin

For installation instructions, see:

```text
INSTALL.md
```

The short version:

- Codex source skill: install `skills/ieee-paper-latex-writing` from this GitHub repository.
- Codex full package: use `ieee-paper-latex-writing-codex-skill-v<version>.zip` from a release.
- Codex plugin package: use `aipe-ieee-paper-agent-codex-plugin-marketplace-v<version>.zip` from a release.
- Claude skill package: use `aipe-ieee-paper-agent-claude-skill-v<version>.zip` from a release.

Maintainers can generate all release packages with:

```bash
python scripts/package-release.py
```

## What This Repository Does

- Collects common IEEE LaTeX templates, including conference, Transactions/journal, IEEE Access, TAI, OJCSYS, and OJPEL formats.
- Provides a reusable Codex Skill, `ieee-paper-latex-writing`, for IEEE paper planning, LaTeX manuscript generation, citation verification, pre-submission checks, and reviewer-response preparation.
- Organizes practical research-writing knowledge into executable workflows: paper storyline, Introduction, Related Work, Method, Experiments, Figures/Tables, and LaTeX submission checks.
- Supports two usage modes: a full repository mode with templates and knowledge bases, and a packaged skill mode for reuse in other Codex workspaces.

## Repository Structure

```text
IEEE-Paper-Agent/
├── IEEE paper Template/
│   ├── IEEE-conference-template-062824/
│   ├── Conference-LaTeX-template_10-17-19/
│   ├── IEEE-Transactions-LaTeX2e-templates-and-instructions/
│   ├── ACCESS_latex_template_20240429/
│   ├── TAI_LaTex_Template/
│   ├── OJCSYS_template_Latex/
│   ├── IEEE-ojpel-latex-template/
│   └── Transactions_win_or_mac_LaTeX2e_style_file/
├── knowledge-base/
│   └── power-electronics-foundations/
├── workflows/
├── templates/
└── skills/
    └── ieee-paper-latex-writing/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## How to Use the LaTeX Templates

1. Choose a template based on the target venue:
   - IEEE conference: start with `IEEE paper Template/IEEE-conference-template-062824/`
   - IEEE Transactions / journal: start with `IEEE paper Template/IEEE-Transactions-LaTeX2e-templates-and-instructions/`
   - IEEE Access: use `IEEE paper Template/ACCESS_latex_template_20240429/`
   - TAI / OJCSYS / OJPEL: use the corresponding template directory

2. Copy the selected template directory and use the copy as your paper workspace.

3. Edit the `.tex` file, figures, and BibTeX files inside your copied workspace. Do not modify official `.cls` files unless the target venue explicitly requires it.

4. Compile the paper with your local LaTeX environment, for example:

```bash
latexmk -pdf main.tex
```

If the template uses a different `.tex` filename, replace `main.tex` with the correct file name.

## How to Use the Writing Skill

The skill is located at:

```text
skills/ieee-paper-latex-writing/
```

It is useful for:

- Generating an IEEE paper outline from a research idea
- Turning an approved paper plan into an IEEE LaTeX manuscript workspace
- Rewriting abstracts, introductions, related work, methods, and experiment sections
- Checking whether the paper contributions are clear and defensible
- Reviewing whether a LaTeX manuscript follows IEEE submission practices
- Checking figures, tables, equations, citations, and references
- Organizing reviewer comments and preparing rebuttal / response letters

Example Codex prompt:

```text
Use the skill at skills/ieee-paper-latex-writing to review my IEEE paper draft.
```

Another example:

```text
Use ieee-paper-latex-writing to help me rewrite the abstract and introduction for an IEEE Transactions paper.
```

## Core Skill Materials

- `SKILL.md`: Main workflow that explains when to use the skill and how to approach IEEE writing and LaTeX review.
- `references/writing-playbook.md`: Writing guidance for IEEE research papers, including titles, abstracts, Introduction, Related Work, Methods, Experiments, figures, tables, and tone.
- `references/latex-submission-checklist.md`: IEEE LaTeX pre-submission checklist.
- `references/reviewer-response.md`: Reviewer-response and revision workflow.
- `references/article-generation-workflow.md`: Plan-to-manuscript workflow for generating article scaffolds and drafts.
- `references/manuscript-workspace-standard.md`: Overleaf-compatible manuscript folder standard.
- `references/figure-generation-workflow.md`: AI figure generation workflow for framework diagrams and paper illustrations.
- `references/citation-verification-policy.md`: Rules for traceable citations and BibTeX entries.
- `references/reference-collection-maintenance.md`: Workflow for maintaining author/topic reference collections under `PE_IEEE_reference/`.

## Power Electronics Knowledge Base

The repository includes a curated knowledge base at:

```text
knowledge-base/power-electronics-foundations/
```

It provides domain vocabulary, concept maps, IEEE-style sentence patterns, and a MinerU workflow for authorized local PDF parsing. Raw full-book PDF conversions are intentionally ignored by Git to avoid committing copyrighted or very large extracted content.

## Reference Index

Repository-local reference candidates live under `PE_IEEE_reference/`. The machine-readable index is:

```text
PE_IEEE_reference/references-index.json
```

Regenerate it after adding, removing, or editing BibTeX files:

```bash
python scripts/build-reference-index.py
```

The index records citation keys, titles, authors, years, venues, DOI/URL fields, source `.bib` files, inferred topics, duplicate keys, and verification status. Use it for retrieval and citation audit, then copy verified BibTeX entries into the manuscript-local `refs/references.bib`.

To add or update an author/topic collection from IEEE Xplore, DOI records, publisher pages, or user-provided source lists, follow:

```text
workflows/reference-collection-maintenance.md
```

### Included Reference Collections

The current `PE_IEEE_reference/` library includes curated BibTeX collections for several influential power electronics researchers and topics:

| Collection | BibTeX File | Records |
| --- | --- | ---: |
| Fred C. Lee | `PE_IEEE_reference/fred_c_lee_reference.bib` | 1051 |
| Johann W. Kolar | `PE_IEEE_reference/johann_w_kolar_reference.bib` | 839 |
| Xiangning He | `PE_IEEE_reference/xiangning_he_reference.bib` | 481 |
| Dragan Maksimović | `PE_IEEE_reference/dragan_maksimovic_reference.bib` | 431 |
| Scott D. Sudhoff | `PE_IEEE_reference/scott_d_sudhoff_reference.bib` | 164 |
| Robert W. Erickson | `PE_IEEE_reference/robert_w_erickson_reference.bib` | 116 |
| R. D. Middlebrook | `PE_IEEE_reference/r_d_middlebrook_reference.bib` | 47 |
| Thomas Guillod | `PE_IEEE_reference/Thomas_Guillod_reference.bib` | 45 |
| Tim C. Green | `PE_IEEE_reference/tim_c_green_reference.bib` | 47 |
| Barry W. Williams | `PE_IEEE_reference/barry_w_williams_reference.bib` | 299 |
| Daniel Rothmund | `PE_IEEE_reference/daniel_rothmund_reference.bib` | 19 |
| Kolar/Guillod converter optimization topic set | `PE_IEEE_reference/kolar_guillod_converter_optimization.bib` | 17 |
| AI paper-agent background references | `PE_IEEE_reference/AIPE_added_refs.bib` | 3 |

These collections are reference candidates, not automatic endorsements. Manuscripts should still cite only sources that are relevant to the claim being made, and uncertain entries should be verified through DOI records, IEEE Xplore, publisher pages, or author-provided sources before submission.

## Workflows and Templates

Use these files when turning an early idea into a paper:

- `workflows/idea-to-paper.md`: raw idea to research spine, contributions, outline, and evidence plan
- `workflows/paper-production.md`: paper plan to LaTeX manuscript workflow
- `workflows/manuscript-workspace-standard.md`: standard folder layout for each generated paper
- `workflows/figure-generation.md`: AI figure-generation workflow for diagrams saved into `figures/`
- `workflows/reference-verification.md`: citation and BibTeX verification workflow
- `workflows/reference-collection-maintenance.md`: workflow for adding/updating `PE_IEEE_reference/` author and topic collections
- `workflows/prompt-library.md`: copy-ready prompts for Codex
- `templates/research-idea-brief.md`: input template for a new idea
- `templates/paper-plan.md`: structured output template for a paper plan

## Automation Helpers

Lightweight scripts live in `scripts/`:

- `scripts/create-manuscript.py`: create the standard `manuscripts/<paper-slug>/` workspace with section, figure, reference, style, note, and build folders.
- `scripts/build-reference-index.py`: rebuild `PE_IEEE_reference/references-index.json` from repository BibTeX files.
- `scripts/check-citations.py`: compare LaTeX `\cite{...}` keys against local `.bib` entries and optionally write `notes/citation-audit.md`.

These scripts are guardrails for repeatable project setup and citation hygiene. They do not generate experimental results or verified references.

## Recommended Workflow

1. Start with a paper plan, not a full draft.
2. Use the skill to clarify the paper spine:
   - What is the research problem?
   - What gap exists in current methods?
   - What is the core method or idea?
   - What are the main contributions?
   - What experiments, theory, or evidence support those contributions?
3. Choose the target IEEE venue and template.
4. Create a manuscript workspace using `workflows/manuscript-workspace-standard.md`.
5. Generate or plan required framework diagrams with `workflows/figure-generation.md` and save all figure assets in `figures/`.
6. Draft the method, evidence, results, introduction, related work, abstract, and conclusion in evidence order.
7. Verify references with `workflows/reference-verification.md`.
8. Compile the PDF and use the LaTeX checklist to review formatting, citations, figures, equations, and page limits.
9. Run a publication-readiness review before submission.

## Who This Is For

- Students and researchers writing IEEE conference papers
- Authors preparing IEEE Transactions or journal submissions
- Research teams that want to standardize LaTeX templates, writing workflows, and submission checks
- Anyone using an AI agent to support research writing, rewriting, and reviewer-response preparation

## Notes

- This repository provides templates and writing workflows; it does not replace the latest author guidelines from the target conference or journal.
- Before submission, always check the target venue website for page limits, anonymization rules, copyright requirements, bibliography style, and supplementary-material rules.
- Do not change official IEEE class files, margins, fonts, or line spacing just to reduce page count.
- The writing skill does not generate real experimental results, citations, or data. All scientific claims must be supported by your experiments, theory, or credible literature.
- If a citation cannot be verified from user-provided sources, repository references, IEEE Xplore/DOI records, or another trusted source, keep it as a placeholder instead of inventing a reference.
