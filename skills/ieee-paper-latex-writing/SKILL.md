---
name: ieee-paper-latex-writing
description: Write, revise, generate, audit, and prepare IEEE-style research manuscripts in LaTeX. Use when the user asks to turn a research idea or paper plan into an IEEE manuscript, create an Overleaf-ready LaTeX workspace, draft IEEE conference/Transactions/Access/Open Journal papers, use IEEE templates, write abstracts, introductions, related work, methods, experiments, figures, tables, equations, BibTeX/citations, verify references, prepare reviewer responses, or run publication-readiness checks for scientific papers, especially power electronics papers.
---

# IEEE Paper LaTeX Writing

## Overview

Turn a research idea, paper plan, or existing draft into a credible IEEE manuscript and keep the LaTeX source submission-safe. Optimize for a clear scientific story, defensible claims, verified references, reproducible evidence, and IEEE-compliant typography.

This skill can operate in two modes:

- **Repository mode:** use the full paper-agent repository, including top-level workflows, IEEE templates, `knowledge-base/`, and `PE_ref/`.
- **Packaged skill mode:** use this skill folder and its bundled `references/` as the minimum portable workflow when the full repository is not available.

## Workflow

1. Decide the task stage.
   - If the user only has a raw idea, first produce a plan: problem, gap, thesis, contributions, outline, evidence plan, figure/table plan, template direction, and next actions.
   - If the user already has a plan or section plan, load `references/article-generation-workflow.md` before creating manuscript files.
   - If the user wants a LaTeX workspace or Overleaf package, load `references/manuscript-workspace-standard.md`.
   - If the task involves generating paper figures, diagrams, or framework illustrations, load `references/figure-generation-workflow.md`.
   - If the task involves citations, BibTeX, related work, or literature retrieval, load `references/citation-verification-policy.md`.
   - If the task involves adding or updating repository reference collections from IEEE Xplore, DOI records, or author profiles, load `references/reference-collection-maintenance.md`.

2. Identify the target venue and template before editing.
   - Use `IEEEtran` conference mode for conference proceedings.
   - Use `IEEEtran` journal/lettersize mode for Transactions and journals.
   - Use the venue-specific class for IEEE Access and open journals when provided.
   - In this repo, inspect the matching folder under `IEEE paper Template/` before changing class options or author metadata.

3. Extract the paper's spine before drafting.
   - One-sentence thesis: "We solve X for Y by Z, improving A under B."
   - Gap: what prior work cannot do, not merely what it has not tried.
   - Contributions: 2-4 concrete claims that can be verified by sections, figures, or experiments.
   - Evidence: each contribution needs a method detail, experiment, ablation, theorem, dataset, or qualitative analysis.
   - Boundary: state assumptions and limitations precisely enough to prevent overclaiming.

4. Draft from argument to prose.
   - Start with title, contribution bullets, figure/table plan, and section outline.
   - When generating a full manuscript, create the workspace first and keep draft TODOs in `notes/`.
   - After the paper framework is agreed, generate or plan figures using the AI figure workflow and store final assets in `figures/`.
   - Write the Introduction as a funnel: problem importance, technical barrier, gap in existing work, core idea, evidence and contributions.
   - Write Methods for reproducibility, not narrative charm.
   - Write Experiments around research questions, baselines, metrics, ablations, and failure cases.
   - Write Related Work as a taxonomy that positions the paper, not as a citation dump.

5. Edit for IEEE style and reviewer trust.
   - Prefer active, specific claims: "Our method reduces latency by 18.4%" over "The results are promising."
   - Tie every strong claim to a number, figure, table, theorem, or citation.
   - Use cautious language for generalization: "in our benchmark", "under the tested workloads", "for this class of systems".
   - Define acronyms on first use in the abstract and again in the main text if needed by the venue template.

6. Make LaTeX changes conservatively.
   - Preserve the official class file, margins, fonts, column widths, and bibliography style unless the venue instructions explicitly require a change.
   - Use semantic cross-references: `\label`, `\ref`, `\eqref`, `\cite`.
   - Put figure/table `\label` commands after or inside the corresponding `\caption`.
   - Avoid hard-coded equation numbers, manual spacing hacks, and `eqnarray`.
   - Keep figures, tables, algorithms, and equations close to first reference when possible, but let floats float.

7. Validate references before treating related work as complete.
   - Prefer user-provided BibTeX, manuscript-local `refs/`, repository `PE_ref/`, IEEE Xplore/DOI records, or other official sources.
   - Do not invent references, DOIs, authors, years, or BibTeX entries.
   - Mark uncertain sources in `notes/citation-audit.md`.

8. Validate before calling the manuscript ready.
   - Compile from a clean state and inspect warnings, missing references, overfull boxes, undefined citations, and font substitutions.
   - Check page limits, abstract word limits, keyword format, author metadata, funding notes, copyright lines, and anonymization rules.
   - Confirm every figure is readable in two-column PDF scale and every table has units, baselines, and statistical context where relevant.

## Task Patterns

For a raw idea, produce in this order: thesis, contribution list, outline, figure/table plan, evidence plan, recommended template, and next actions.

For a planned paper, load `references/article-generation-workflow.md` and produce in this order: normalized plan, workspace structure, LaTeX skeleton, section drafts where evidence exists, citation audit, and author TODOs.

For figure generation, load `references/figure-generation-workflow.md`, create `notes/figure-plan.md`, generate only argument-supporting diagrams, save assets under `figures/`, and integrate them with relative LaTeX paths.

For rewriting, preserve the user's technical meaning but improve the argument structure, specificity, and IEEE tone. Do not invent results, baselines, datasets, or citations. Mark missing evidence explicitly.

For LaTeX debugging, first identify the class/template and compiler path, then inspect only the relevant source, log, bibliography, and figure declarations. Prefer small source edits over template rewrites.

For publication audit, review both manuscript quality and LaTeX readiness. Lead with blocking issues, then high-impact improvements, then minor style fixes.

For reviewer responses, build a response matrix: reviewer concern, manuscript action, exact location changed, and concise response text. Keep responses respectful, evidence-based, and traceable to edits.

## References

Load these only when the task needs more detail:

- `references/writing-playbook.md`: section-by-section writing heuristics for strong IEEE research papers.
- `references/latex-submission-checklist.md`: IEEE LaTeX, figures, equations, citations, and pre-submission checks.
- `references/reviewer-response.md`: revision and rebuttal workflow for peer review.
- `references/article-generation-workflow.md`: plan-to-manuscript generation workflow.
- `references/manuscript-workspace-standard.md`: required manuscript workspace layout and Overleaf-compatible file organization.
- `references/figure-generation-workflow.md`: AI figure generation, storage, and LaTeX integration workflow.
- `references/citation-verification-policy.md`: citation and BibTeX verification rules.
- `references/reference-collection-maintenance.md`: author/topic reference collection maintenance workflow for `PE_ref/`.

## Output Standards

When writing manuscript text, return polished paper-ready prose unless the user asks for notes. When auditing, separate "must fix before submission" from "quality upgrades". When editing LaTeX files, keep diffs narrow and explain any venue-sensitive assumptions.
