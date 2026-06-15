# Codex Instructions for IEEE Paper Agent

This repository is a writing assistant workspace for IEEE-style research papers. When a user opens this repo in Codex and asks for help writing, planning, revising, or reviewing a paper, treat the repo as a reusable paper-production system rather than a generic file collection.

## Start Here

1. Read `README.md` for the repository map.
2. Use `skills/ieee-paper-latex-writing/SKILL.md` as the primary writing and LaTeX review workflow.
3. For power electronics topics, use `knowledge-base/power-electronics-foundations/` before drafting domain-specific language.
4. For idea-to-paper work, follow `workflows/idea-to-paper.md`.
5. For plan-to-manuscript production, follow `workflows/paper-production.md` and `workflows/manuscript-workspace-standard.md`.
6. For citations and BibTeX, follow `workflows/reference-verification.md`.
7. For prompt examples and reusable interactions, read `workflows/prompt-library.md`.

## Expected Behavior

When the user provides only a research idea, turn it into:

- a problem statement,
- a research gap,
- a candidate thesis,
- 2-4 contribution claims,
- a paper outline,
- an evidence plan,
- a figure/table plan,
- recommended IEEE venue/template direction,
- next actions for experiments, writing, and LaTeX setup.

Do not invent experimental results, datasets, citations, or numerical claims. Mark missing evidence explicitly and convert vague ideas into testable research questions.

When the user already has a paper plan, create or update an Overleaf-compatible manuscript workspace before drafting full paper text. Use the standard layout in `workflows/manuscript-workspace-standard.md` unless a target venue template requires a different structure.

## Writing Style

Use polished IEEE-style academic English. Prefer specific, evidence-linked claims over generic phrases. For power electronics papers, use the vocabulary and language bank in:

- `knowledge-base/power-electronics-foundations/domain-vocabulary.md`
- `knowledge-base/power-electronics-foundations/paper-language-bank.md`
- `knowledge-base/power-electronics-foundations/chapter-notes/chapter-index.md`

## LaTeX Handling

Use the existing IEEE templates under `IEEE paper Template/`. Preserve official class files, margins, fonts, column widths, and bibliography styles unless the user provides venue-specific instructions requiring changes.

When creating or editing a manuscript, prefer a copied template workspace instead of modifying the source templates directly.

Keep figures in `figures/`, BibTeX files in `refs/`, template support files in `styles/`, article body files in `sections/`, and planning/audit notes in `notes/` when creating new manuscript workspaces.

## Citation Handling

Every reference must be traceable to user-provided sources, manuscript-local BibTeX, `PE_ref/`, IEEE Xplore/DOI records, or another trusted source. Do not fabricate BibTeX entries. If a reference cannot be verified, mark it in `notes/citation-audit.md` or leave a citation placeholder.

## Copyright and Knowledge Base Boundary

The `books/` directory is for local private reference only. Do not commit full converted textbook Markdown, extracted figures, or page-by-page text. Use curated notes and original summaries under `knowledge-base/`.
