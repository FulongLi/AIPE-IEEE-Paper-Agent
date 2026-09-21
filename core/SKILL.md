---
name: ieee-paper-latex-writing
description: Plan, draft, revise, and audit IEEE research papers using evidence-linked writing workflows, venue-specific LaTeX templates, citation checks, and reviewer responses.
---

# IEEE Paper Production

In repository mode, resolve instruction and command paths from the repository
root containing this `core/` directory. In a generated portable package, resolve
them from the skill directory containing `SKILL.md`; asset paths are rewritten at
build time. Run bundled scripts using their absolute location when the current
working directory is elsewhere. `--root` chooses manuscript output, not assets.

## Route the Task

Load only the workflow needed for the request:

- Raw idea: `core/workflows/idea-to-paper.md`; use `artifacts/research-idea-brief.md`
  and `artifacts/paper-plan.md` for the resulting plan.
- Plan to paper: `core/workflows/paper-production.md`, then
  `core/workflows/manuscript-generation.md` and
  `core/workflows/manuscript-workspace-standard.md` for initialization.
- Section drafting or rewriting: `core/workflows/writing-playbook.md`. Preserve
  the author's technical meaning and draft only against available evidence.
- Citation audit: `core/workflows/citation-verification.md`.
- Submission review: `core/workflows/publication-audit.md`.
- Reviewer responses: `core/workflows/reviewer-response.md`.
- Prompt examples: `core/workflows/prompt-library.md`.

## Policies and Configuration

`core/policies/scientific-integrity.md` governs claims and missing evidence.
Use `core/policies/citation-policy.md` for references,
`core/policies/latex-policy.md` for template/layout decisions, and
`core/policies/figure-policy.md` for figure planning and generation.

Identify the venue before initialization. Inspect `venues/<id>/profile.json` and
use `scripts/create-manuscript.py --venue <id>` to adapt that real template.
The default is explicitly `ieee-conference`; journal work must choose its profile.
See `venues/README.md` for the schema and supported templates.

Load a domain pack only when the topic calls for it and the pack is available.
`domains/power-electronics/README.md` routes power-electronics tasks to its
knowledge, terminology, and literature. Other IEEE papers use core and venue
assets alone. Domain knowledge never supplies missing experimental evidence.

## Output

For a raw idea, return the research spine, research questions, 2–4 verifiable
contributions, evidence and figure/table plans, outline, venue direction, and
next actions. For a manuscript request, initialize the workspace, draft supported
sections, and track evidence gaps and citation/LaTeX work in `notes/`.

For audits, lead with blockers, then important improvements, then optional
polish. Report which checks actually ran. Static script success does not mean
that references are externally verified or that the paper is ready to submit.
