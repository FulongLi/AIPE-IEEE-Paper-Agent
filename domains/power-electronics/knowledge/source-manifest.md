# Source Manifest

## Local Sources

| Source | Path | Intended Use | Commit Raw Extraction? |
| --- | --- | --- | --- |
| Robert Erickson power electronics textbook PDF | `books/Robert_Erikson_fundamentals-of-power-electronics-3n_2020.pdf` | Local reference, concept indexing, terminology inspiration, chapter-level navigation when authorized | No |

## Rights Boundary

The local PDF is a full textbook-scale source. Treat it as copyrighted unless you have clear evidence that redistribution and derivative Markdown conversion are permitted.

Allowed project artifacts should be non-substitutive:

- Brief conceptual summaries
- Original explanations written from general knowledge
- Topic indexes
- Terminology and phrase banks
- Search metadata and local-only processing instructions

Do not commit full parsed Markdown or extracted images/tables from the textbook into the repository.

## Local-Only Processing Outputs

MinerU outputs should go under:

```text
domains/power-electronics/knowledge/raw-mineru-output/
```

That directory is ignored by Git. Use it as a local workspace for authorized parsing, review, and note extraction.
