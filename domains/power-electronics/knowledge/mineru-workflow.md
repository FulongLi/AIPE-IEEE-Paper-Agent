# MinerU Workflow

MinerU is a document parsing engine that converts PDFs and other document formats into Markdown and JSON for downstream retrieval, extraction, and processing. It is useful for extracting reading-order text, formulas, tables, figures, and OCR content from complex technical PDFs.

## Install MinerU

Follow the official MinerU documentation for the current installation method. After installation, confirm that the CLI is available:

```bash
mineru --help
```

## Parse the Local PDF

Use this only if you have the rights to process and reuse the extracted content. Full converted Markdown should remain local and uncommitted unless redistribution is explicitly permitted.

```bash
mkdir -p domains/power-electronics/knowledge/raw-mineru-output
mineru -p books/Robert_Erikson_fundamentals-of-power-electronics-3n_2020.pdf -o domains/power-electronics/knowledge/raw-mineru-output -b pipeline
```

Notes:

- `-b pipeline` selects the CPU-capable pipeline backend.
- MinerU can also use GPU/MPS acceleration when configured.
- Keep raw outputs local unless redistribution is allowed.

## Chapterized Private Cache

If you want fast local lookup without repeatedly opening the PDF, create a private cache:

```text
domains/power-electronics/knowledge/private-fulltext-cache/
```

This directory is ignored by Git. It can contain local-only MinerU Markdown, page JSON, images, and chapter splits for personal retrieval. Do not commit it to this repository unless the source license permits redistribution of the converted text.

Recommended local layout:

```text
private-fulltext-cache/
├── mineru-raw/
├── chapters/
│   ├── ch01.md
│   ├── ch02.md
│   └── ...
└── index/
    ├── local-toc.md
    └── local-search-notes.md
```

## Curate Into the Knowledge Base

After parsing, do not copy full textbook text into committed Markdown. Instead, curate small, original notes:

1. Identify a topic, such as buck converter steady-state conversion ratio.
2. Write a short original explanation in your own words.
3. Record useful terminology and equation labels.
4. Add a pointer to the local source section or page for your own navigation.
5. Avoid long quotations and copied paragraphs.

Suggested curated-note shape:

```markdown
## Topic Name

Core idea: ...

Useful terms: ...

Typical IEEE phrasing: ...

Related equations or models: ...

Local source pointer: chapter/section/page, if known.
```

Committed notes should live under `chapter-notes/`. Private full text should stay under `private-fulltext-cache/`.

## Quality Check

For each curated note, ask:

- Is this useful for writing a paper?
- Is it original and non-substitutive?
- Does it avoid copying textbook prose?
- Does it preserve technical accuracy?
- Is the source pointer enough for local verification?
