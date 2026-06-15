# Reference Collection Maintenance

Use this reference when adding, updating, or auditing repository-level reference collections under `PE_ref/`.

## Purpose

The repository can maintain author- or topic-based BibTeX collections from IEEE Xplore, DOI records, publisher pages, and user-provided sources. These collections support discovery and citation audit; they are not automatic citation recommendations.

## Author-Based Collection Workflow

1. Define the author.
   - Canonical name.
   - Name variants and initials.
   - Known affiliations and coauthors.
   - Scope: IEEE-only, power-electronics-only, or full bibliography.

2. Search trusted sources.
   - Prefer IEEE Xplore author profiles and publication search.
   - Use DOI/publisher records to verify metadata.
   - Use ORCID, lab pages, and Google Scholar only as discovery aids unless metadata is independently verified.

3. Avoid homonym errors.
   - Confirm affiliation, coauthors, venue, topic, and time period.
   - Exclude uncertain publications or mark them for verification.

4. Export BibTeX.
   - Prefer IEEE Xplore BibTeX export when available.
   - Preserve DOI, title, authors, venue, year, volume, number, pages, and keywords.
   - Keep exported IEEE article-number keys unless creating a manual curated topic list.

5. Save three files when maintaining a full collection.
   - `PE_ref/<normalized_author>_reference.bib`
   - `PE_ref/<normalized_author>_reference.md`
   - `PE_ref/<normalized_author>_reference.html`

6. Rebuild the index.

```bash
python scripts/build-reference-index.py
```

7. Review the generated `PE_ref/references-index.json`.
   - `record_count`
   - `duplicate_key_count`
   - `verification_status_counts`
   - records marked `needs-verification`

## Markdown Summary Contents

For each `<author>_reference.md`, include:

- collection scope,
- source method,
- record count,
- major topic clusters,
- verification notes,
- known limitations.

## Citation Use Rule

When drafting a paper, first find candidate references through `PE_ref/references-index.json`, then copy only relevant, verified BibTeX entries into the manuscript-local `refs/references.bib`.

