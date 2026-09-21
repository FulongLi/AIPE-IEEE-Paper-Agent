# Reference Collection Maintenance Workflow

Use this workflow when adding or updating repository-level reference collections under `PE_IEEE_reference/`, especially author-based collections from IEEE Xplore.

## Goal

Maintain reusable, traceable BibTeX collections for influential researchers, topics, and paper-agent background references. These collections are candidates for later manuscript citation, not automatic recommendations.

## Source Priority

Prefer sources in this order:

1. IEEE Xplore author profile or publication search results.
2. DOI records and publisher pages.
3. Author lab pages, university repositories, ORCID, or Google Scholar only as secondary discovery aids.
4. User-provided BibTeX or verified publication lists.

Do not invent missing metadata. If a publication cannot be verified, omit it or mark it as needing verification.

## Author Collection Procedure

1. Define the collection target.
   - Canonical author name, for example `Johann W. Kolar`.
   - Known name variants, initials, and affiliations.
   - Scope: IEEE-only, power-electronics-only, or full author bibliography.

2. Search IEEE Xplore.
   - Use author profile pages when available.
   - Otherwise search the author name and filter by relevant IEEE venues, years, and topic keywords.
   - Watch for homonyms. Confirm affiliation, coauthors, venue, and topic before adding records.

3. Export or capture BibTeX.
   - Prefer IEEE Xplore citation export when available.
   - Keep DOI, title, authors, venue, year, pages, volume/number, and keywords.
   - Preserve IEEE article-number keys when exported, unless creating a curated semantic-key topic set.

4. Save the collection under `PE_IEEE_reference/`.
   - BibTeX: `PE_IEEE_reference/<normalized_author>_reference.bib`
   - Markdown summary: `PE_IEEE_reference/<normalized_author>_reference.md`
   - HTML browse page: `PE_IEEE_reference/<normalized_author>_reference.html`

5. Write the Markdown summary.
   - State source and scope.
   - List collection count.
   - Highlight major topic clusters.
   - Mention known limitations, missing DOI records, or likely homonym risks.

6. Write the HTML browse page when useful.
   - Include title, venue, year, DOI link, and BibTeX key.
   - Keep it as a lightweight browse aid, not a replacement for publisher records.

7. Rebuild the JSON index.

```bash
python scripts/build-reference-index.py
```

8. Inspect the index output.
   - Check `record_count`.
   - Check `duplicate_key_count`.
   - Check `verification_status_counts`.
   - Review entries with `needs-verification`.

## Topic Collection Procedure

For a topic-specific collection, such as converter optimization:

- Use semantic citation keys when the list is manually curated.
- Include only papers that directly support the topic.
- Add a header comment in the `.bib` file describing scope and source assumptions.
- Rebuild `PE_IEEE_reference/references-index.json`.

## Quality Rules

- Keep references traceable to DOI, IEEE Xplore, publisher, or user-provided source.
- Do not use the repository reference library to pad related work.
- Do not cite a paper only because it belongs to a famous author.
- Prefer the most relevant primary paper for each claim.
- Keep duplicate keys visible in the JSON index rather than silently deleting them.

