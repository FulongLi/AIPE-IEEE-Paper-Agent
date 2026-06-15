# Manuscript Workspace Standard

Use this standard whenever the repository generates a new IEEE paper workspace.

```text
manuscripts/
└── paper-slug/
    ├── main.tex
    ├── sections/
    │   ├── 00-abstract.tex
    │   ├── 01-introduction.tex
    │   ├── 02-related-work.tex
    │   ├── 03-method.tex
    │   ├── 04-experiments.tex
    │   ├── 05-results-discussion.tex
    │   └── 06-conclusion.tex
    ├── figures/
    ├── tables/
    ├── refs/
    │   └── references.bib
    ├── styles/
    ├── notes/
    │   ├── paper-plan.md
    │   ├── evidence-checklist.md
    │   ├── citation-audit.md
    │   └── latex-todo.md
    └── build/
```

## Folder Roles

- `main.tex`: compilation entry point and template front matter.
- `sections/`: article body files, split by section.
- `figures/`: all paper figures with portable filenames.
- `tables/`: optional table fragments or generated table sources.
- `refs/`: BibTeX files and citation audit material.
- `styles/`: copied official class/style/font/bibliography files needed by the selected IEEE template.
- `notes/`: planning, evidence, citation, and LaTeX TODO files.
- `build/`: local compilation output when supported.

## Rules

- Do not edit the original source templates under `IEEE paper Template/`.
- Copy the closest official template into a manuscript workspace or copy required support files into `styles/`.
- Use relative paths so the workspace can be uploaded to Overleaf.
- Do not use local absolute paths in LaTeX files.
- Do not create unsupported experimental claims. Put missing results in `notes/evidence-checklist.md`.
- Do not fabricate citations. Put uncertain sources in `notes/citation-audit.md`.

