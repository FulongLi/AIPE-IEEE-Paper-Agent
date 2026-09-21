# Reference Verification Workflow

Use this workflow whenever the agent drafts related work, inserts citations, builds BibTeX, or audits a manuscript.

## Source and Metadata Policy

Follow `core/policies/citation-policy.md` for source priority, metadata requirements,
traceability, and reference-index semantics. A domain collection is optional.

## Structural Check

Run `python scripts/check-citations.py <workspace> --write-audit`. It reports
resolved citation keys, missing BibTeX entries, duplicate keys, and uncited entries.
Comments are ignored. Review cited works against original source records and the
claims they support; key resolution alone is not reference verification.

The regenerated report is `notes/citation-audit.md`. Keep manual metadata, DOI/URL,
and claim-support findings in `notes/citation-verification.md`, which the checker
never overwrites. Trace optional library records back to their original source file.

## Audit Checklist

For each manuscript:

- List all citation keys used in `.tex`.
- List all BibTeX keys available in `refs/*.bib`.
- Report missing BibTeX entries.
- Report uncited BibTeX entries.
- Flag entries with missing title, author, year, venue, DOI, or URL when that metadata should exist.
- Flag strong technical claims that lack evidence or citation support.
