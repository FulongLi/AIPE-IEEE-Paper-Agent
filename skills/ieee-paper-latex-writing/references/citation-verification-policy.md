# Citation Verification Policy

Use this policy whenever generating, editing, or auditing references for an IEEE manuscript.

## Core Rule

Every reference must be traceable. Do not invent papers, venues, authors, years, DOIs, IEEE Xplore links, or BibTeX keys.

## Trusted Sources

Prefer references in this order:

1. User-provided BibTeX or DOI/URL.
2. Manuscript-local `refs/references.bib`.
3. Repository reference index `PE_ref/references-index.json`, when the full repository is available.
4. Repository reference files such as `PE_ref/*.bib`.
5. Official publisher pages, IEEE Xplore, DOI records, arXiv, or university/project pages when browsing is available.
6. Clearly marked placeholders when verification is not possible.

## BibTeX Requirements

For each cited work, keep as much metadata as available:

- stable citation key,
- title,
- authors,
- venue or journal,
- year,
- DOI or URL when available,
- publisher or organization for standards and datasets.

Use `@article`, `@inproceedings`, `@book`, `@standard`, `@misc`, or another appropriate BibTeX type. Do not downgrade all entries to `@misc` merely because metadata is incomplete.

## Manuscript Rules

- Every `\cite{key}` in `.tex` must resolve to a BibTeX entry.
- Every strong technical claim must be supported by evidence, a citation, or a clearly marked author-provided result.
- Prefer primary technical papers for method claims.
- Use surveys for taxonomy and context, not as the only support for a specific prior method.
- When using `PE_ref/references-index.json`, trace selected records back to `source_file` before copying BibTeX into the manuscript.
- Mark uncertain citations with `% TODO: verify citation` or add them to `notes/citation-audit.md`.

## Reference Index Maintenance

When the full repository is available, rebuild the reference index after adding, removing, or editing repository BibTeX files:

```bash
python scripts/build-reference-index.py
```

Use the JSON index for search and audit. Keep manuscript-ready BibTeX entries in `refs/references.bib`.

## Audit Output

When auditing citations, create or update `notes/citation-audit.md` with:

```text
## Citation Audit

### Resolved Citations

- <key>: found in <file>; metadata complete/incomplete.

### Missing BibTeX Entries

- <key>: cited in <file>; no matching BibTeX entry found.

### Uncited BibTeX Entries

- <key>: present in <bib file>; not cited in manuscript.

### Verification Needed

- <claim or key>: needs DOI, IEEE Xplore page, user confirmation, or replacement.
```

If a citation cannot be verified, keep the manuscript honest by using a placeholder instead of fabricating a reference.
