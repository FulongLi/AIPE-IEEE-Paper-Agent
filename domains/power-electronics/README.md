# Optional Power-Electronics Domain Pack

Load this pack for power-electronics writing; the generic IEEE engine and venue
initialization work without it. It adds terminology and curated notes, not results.

- `domains/power-electronics/knowledge/concept-map.md`: topic map.
- `domains/power-electronics/knowledge/chapter-notes/`: existing chapter notes,
  formula index, and retrieval guide.
- `domains/power-electronics/terminology/domain-vocabulary.md`: technical terms.
- `domains/power-electronics/terminology/paper-language-bank.md`: writing patterns.
- `domains/power-electronics/knowledge/source-manifest.md`: source inventory.
- `domains/power-electronics/knowledge/mineru-workflow.md`: authorized local parsing;
  raw extraction and private full-text caches stay local and out of releases.
- `domains/power-electronics/literature/reference-collection-maintenance.md`:
  author/topic collection maintenance.

The original BibTeX, Markdown, HTML, and index remain in `PE_IEEE_reference/` to
preserve reference-tool compatibility. `PE_IEEE_reference/references-index.json`
links candidate records to original `source_file` values. Copy only relevant,
verified entries to manuscript-local `refs/references.bib`.

`doi-present` and `url-present` indicate available metadata, not successful network
verification. Duplicate keys remain visible; do not silently delete records.
