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
    │   ├── figure-plan.md
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
- `styles/`: author-owned support files. Official classes, styles, fonts, logos, and required template assets stay at the original relative locations beside `main.tex`, so class-internal file lookups work on Overleaf without environment variables. Do not edit them.
- `notes/`: planning and audit artifacts. These are not part of the final submission unless the user requests them.
- `build/`: local compile output when the toolchain supports an output directory. Do not cite files from `build/`.

## Template Handling

Choose `venues/<id>/profile.json` and follow `core/workflows/manuscript-generation.md`.
The profile identifies the real template and entry file. Do not substitute a generic
conference preamble for a journal. `notes/venue-profile.json` records the selection.

The abstract fragment contains text only; the real entry retains its abstract
environment in the venue-required position. Official support files are preserved
at their original relative paths. Original sample .tex files are not copied into
the active workspace, so sample citations cannot contaminate manuscript audits.

## Overleaf Compatibility

- Keep paths relative to `main.tex`.
- Avoid local absolute paths.
- Store all generated images and author-provided paper figures in `figures/`.
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
