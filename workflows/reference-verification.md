# Reference Verification Workflow

Use this workflow whenever the agent drafts related work, inserts citations, builds BibTeX, or audits a manuscript.

## Policy

Every citation must be traceable. The agent must not invent authors, titles, venues, years, DOIs, IEEE Xplore URLs, or BibTeX keys.

## Preferred Source Order

1. User-provided BibTeX, DOI, URL, or uploaded reference list.
2. The manuscript workspace `refs/references.bib`.
3. Repository reference index `PE_IEEE_reference/references-index.json`.
4. Repository references under `PE_IEEE_reference/*.bib`.
5. Official publisher records such as IEEE Xplore, DOI pages, arXiv, or standards bodies when browsing is available.
6. Explicit placeholders when verification is not possible.

## Drafting Rules

- Use citation placeholders instead of fake citations.
- Prefer primary literature for method comparisons.
- Use surveys for broad taxonomy and positioning.
- Use `PE_IEEE_reference/references-index.json` to find candidate references, then trace each selected record back to its `source_file`.
- Mark incomplete or uncertain references in `notes/citation-audit.md`.
- Ensure every `\cite{...}` key exists in a BibTeX file before final review.

## Maintaining the Index

After changing repository reference files, regenerate the JSON index:

```bash
python scripts/build-reference-index.py
```

The index is a retrieval and audit aid. It does not replace the original `.bib` files, and `verification_status` only reflects available metadata such as DOI, URL, or arXiv markers.

## Audit Checklist

For each manuscript:

- List all citation keys used in `.tex`.
- List all BibTeX keys available in `refs/*.bib`.
- Report missing BibTeX entries.
- Report uncited BibTeX entries.
- Flag entries with missing title, author, year, venue, DOI, or URL when that metadata should exist.
- Flag strong technical claims that lack evidence or citation support.
