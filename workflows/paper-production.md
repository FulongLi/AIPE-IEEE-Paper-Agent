# Paper Production Workflow

Use this workflow after the idea has a clear paper plan. If the user only has a rough idea, use `workflows/idea-to-paper.md` first.

## Stage 0: Confirm the Plan

Before creating manuscript files, confirm that the plan includes:

- problem, gap, idea, evidence, and impact,
- 2-4 contribution claims,
- section plan,
- figure/table plan,
- target venue or template family,
- missing evidence list.

If any item is missing, proceed with labeled assumptions and track missing items in `notes/evidence-checklist.md`.

## Stage 1: Create the Manuscript Workspace

Use `workflows/manuscript-workspace-standard.md`.

1. Select the closest IEEE template.
2. Copy the template directory into a manuscript workspace or copy required support files into `styles/`.
3. Rename or create `main.tex` if desired.
4. Keep official `.cls`, `.bst`, `.sty`, font, and image assets unchanged unless the venue requires otherwise.

Standard workspace layout:

```text
manuscripts/
└── paper-slug/
    ├── main.tex
    ├── sections/
    ├── figures/
    ├── tables/
    ├── refs/
    ├── styles/
    ├── notes/
    └── build/
```

## Stage 2: Draft the Skeleton

Create the paper skeleton before full prose:

- title,
- abstract placeholder,
- keywords,
- section headings,
- contribution bullets,
- figure/table placeholders,
- citation placeholders,
- experiment checklist,
- evidence checklist,
- citation audit.

## Stage 3: Draft in Evidence Order

Recommended order:

1. Method or system section.
2. Experiment setup.
3. Results.
4. Introduction.
5. Related Work.
6. Abstract.
7. Conclusion.

This order keeps the Introduction and Abstract honest because they are written after the evidence is visible.

## Stage 4: Reference Verification Pass

Use `workflows/reference-verification.md`.

Check:

- every `\cite{...}` resolves to a BibTeX entry,
- references come from user-provided sources, `refs/`, `PE_ref/`, or verified external records,
- no invented citations or BibTeX entries are present,
- strong claims have either evidence or citation support,
- unresolved sources are tracked in `notes/citation-audit.md`.

## Stage 5: IEEE Style Pass

Check:

- claims are specific and evidence-linked,
- acronyms are defined,
- figures are referenced and readable,
- tables include units and metric direction,
- equations define all symbols,
- citations support related work and technical claims,
- limitations are stated without weakening the contribution unnecessarily.

## Stage 6: LaTeX Submission Pass

Use:

```text
skills/ieee-paper-latex-writing/references/latex-submission-checklist.md
```

Check:

- clean compile,
- no undefined references or citations,
- no serious overfull boxes,
- correct page limit,
- correct author metadata,
- correct bibliography style,
- no template filler text,
- no local absolute file paths.

## Stage 7: Publication-Readiness Review

Review the manuscript as if acting as a strict IEEE reviewer:

- Is the novelty explicit?
- Is the baseline fair?
- Are claims supported by evidence?
- Are experimental conditions clear?
- Are figures and tables necessary and interpretable?
- Are limitations handled honestly?
- Would a reviewer know why the work matters?

