# Prompt Library

Copy these prompts into Codex when using this repository.

## Start From a Raw Idea

```text
Use this repository as an IEEE paper-writing assistant. Follow AGENTS.md and workflows/idea-to-paper.md.

My research idea is:
<paste idea>

Please produce a paper plan with a working title, research spine, research questions, contributions, outline, figure/table plan, missing evidence list, recommended IEEE template, and next actions.
```

## Improve an Existing Paper Plan

```text
Use skills/ieee-paper-latex-writing/SKILL.md to review this paper plan for novelty, contribution clarity, evidence strength, and IEEE suitability.

Paper plan:
<paste plan>
```

## Draft an IEEE Introduction

```text
Use the IEEE writing skill and, if relevant, the power electronics knowledge base.

Draft an IEEE-style Introduction from this paper plan:
<paste plan>

Make the structure: motivation, technical challenge, research gap, proposed idea, contributions, and paper organization. Do not invent results.
```

## Rewrite in Power Electronics Style

```text
Use knowledge-base/power-electronics-foundations/domain-vocabulary.md and paper-language-bank.md.

Rewrite this paragraph in precise IEEE power electronics style:
<paste paragraph>

Preserve the technical meaning and avoid adding unsupported claims.
```

## Build a Figure and Table Plan

```text
Follow workflows/idea-to-paper.md and create a figure/table plan for this paper idea:
<paste idea or outline>

For each figure or table, include purpose, expected content, evidence required, and where it belongs in the paper.
```

## Create a LaTeX Manuscript Plan

```text
Use workflows/paper-production.md.

Target venue/template:
<conference / Transactions / IEEE Access / unknown>

Paper plan:
<paste plan>

Recommend the template folder, manuscript workspace structure, section skeleton, and LaTeX TODO list.
```

## Generate a Manuscript Workspace From a Paper Plan

```text
Use skills/ieee-paper-latex-writing/SKILL.md, references/article-generation-workflow.md, and workflows/manuscript-workspace-standard.md.

Target venue/template:
<conference / Transactions / IEEE Access / unknown>

Paper plan:
<paste plan>

Create an Overleaf-ready manuscript workspace. Draft only the sections that are supported by the provided plan and evidence. Put missing experiments, missing figures, and unsupported claims into notes/evidence-checklist.md. Do not invent citations or numerical results.
```

## Generate Paper Figures

```text
Use workflows/figure-generation.md and the paper plan below.

Paper plan:
<paste plan>

Create notes/figure-plan.md, then generate the required framework diagrams with Image 2 or the available image-generation tool. Save final image assets in figures/ and add LaTeX figure snippets using relative paths. Do not invent measured plots or numerical results.
```

## Verify References Before Drafting Related Work

```text
Use workflows/reference-verification.md and skills/ieee-paper-latex-writing/references/citation-verification-policy.md.

Manuscript or paper plan:
<path or paste content>

Available reference sources:
<refs.bib / PE_ref / DOI list / IEEE Xplore links / unknown>

Audit the citations and produce notes/citation-audit.md. Mark missing or uncertain references instead of inventing BibTeX.
```

## Add an Author Reference Collection

```text
Use workflows/reference-collection-maintenance.md.

Author:
<author name>

Scope:
<IEEE Xplore / power electronics only / specific topic / full bibliography>

Create or update PE_ref/<normalized_author>_reference.bib, PE_ref/<normalized_author>_reference.md, and PE_ref/<normalized_author>_reference.html from verified sources. Rebuild PE_ref/references-index.json and report records that need verification. Do not invent missing metadata.
```

## Review a Draft Before Submission

```text
Use skills/ieee-paper-latex-writing/SKILL.md and references/latex-submission-checklist.md.

Review this IEEE manuscript draft for publication readiness:
<path or paste draft>

Lead with must-fix issues, then quality upgrades, then minor style issues.
```

## Respond to Reviewers

```text
Use skills/ieee-paper-latex-writing/references/reviewer-response.md.

Reviewer comments:
<paste comments>

Manuscript changes available:
<paste changes or say unknown>

Create a response matrix and draft polite, evidence-linked responses. Mark any response that needs a real manuscript edit.
```
