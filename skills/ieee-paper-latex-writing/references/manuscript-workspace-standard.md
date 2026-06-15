# Manuscript Workspace Standard

Use this structure for each generated IEEE paper workspace unless the target venue template requires a different layout.

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

## Directory Rules

- `main.tex`: entry point for compilation. Keep author metadata, document class, packages, section inputs, bibliography command, and template-required front/back matter here.
- `sections/`: manuscript body. Use separate files when the paper is long or when multiple agents/authors will edit sections independently.
- `figures/`: all paper figures. Use stable ASCII filenames with no spaces. Prefer vector formats for plots when the venue accepts them.
- `tables/`: optional table fragments or generated table sources. Small tables may stay directly in section files.
- `refs/`: BibTeX files and citation audit notes. Do not mix reference files with figures or template files.
- `styles/`: copied official template support files such as `.cls`, `.bst`, `.sty`, fonts, logos, and required template images. Do not edit these unless the venue requires it.
- `notes/`: planning and audit artifacts. These are not part of the final submission unless the user requests them.
- `build/`: local compile output when the toolchain supports an output directory. Do not cite files from `build/`.

## Template Handling

Start from the closest official template under the repository's `IEEE paper Template/` folder when available:

- IEEE conference: `IEEE-conference-template-062824`
- IEEE Transactions or journal: `IEEE-Transactions-LaTeX2e-templates-and-instructions`
- IEEE Access: `ACCESS_latex_template_20240429`
- IEEE TAI, OJCSYS, or OJPEL: use the matching venue folder

Copy the template into the manuscript workspace or copy required support files into `styles/`. Preserve official class files, bibliography styles, fonts, margins, and column widths.

## Overleaf Compatibility

- Keep paths relative to `main.tex`.
- Avoid local absolute paths.
- Avoid spaces, non-ASCII characters, and punctuation-heavy filenames for new assets.
- Keep the bibliography file in `refs/references.bib` unless the template strongly expects another name.
- Include all `.cls`, `.bst`, `.sty`, font, logo, and figure files needed for a clean Overleaf compile.
- Remove sample template text and unused sample figures before final submission.

## Naming

Use a short lowercase `paper-slug`, for example:

```text
manuscripts/wide-input-dcdc-control/
```

Do not place new manuscript drafts inside the original template directories.

