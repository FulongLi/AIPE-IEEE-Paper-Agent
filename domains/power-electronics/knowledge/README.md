# Power Electronics Foundations Knowledge Base

This knowledge base supports IEEE-style paper writing in power electronics. It is designed to provide domain vocabulary, concept maps, writing patterns, and retrieval-friendly notes without reproducing a full copyrighted textbook.

## Purpose

- Provide technically precise language for papers on power converters, switching devices, magnetics, control, modeling, and converter design.
- Keep reusable domain knowledge close to the IEEE paper templates and writing skill.
- Support future article generation with field-specific terminology rather than generic engineering prose.
- Maintain a clean separation between local PDF parsing artifacts and curated, non-substitutive knowledge notes.

## Source Material

The local `books/` folder contains:

```text
books/Robert_Erikson_fundamentals-of-power-electronics-3n_2020.pdf
```

This appears to be a full textbook-scale PDF. Do not commit full-book Markdown, copied chapters, or page-by-page transformations unless you have explicit rights to redistribute that derived text.

## What Belongs Here

Good knowledge-base content:

- Concept maps and topic taxonomies
- Short non-verbatim summaries
- Terminology lists
- Formula topic indexes without copying long textbook explanations
- Paper-writing phrase banks
- Curated chapter notes that help retrieval without replacing the source book
- Citation placeholders and source-aware notes
- Research-question prompts and experiment vocabulary

Avoid committing:

- Full Markdown conversion of the textbook
- Long verbatim passages
- Complete chapter summaries that replace the book
- Extracted figures, tables, or images from the PDF unless redistribution is allowed

## Files

- `source-manifest.md`: Local source inventory and usage boundary.
- `mineru-workflow.md`: How to run MinerU locally when authorized.
- `chapter-notes/`: Commit-safe chapter note templates and curated topic pages.
- `concept-map.md`: High-level power electronics topic map.
- `domains/power-electronics/terminology/domain-vocabulary.md`: Professional vocabulary for IEEE writing.
- `domains/power-electronics/terminology/paper-language-bank.md`: Reusable sentence patterns for academic writing.

## Recommended Use With Codex

Example prompt:

```text
Use the IEEE writing skill and the knowledge base at domains/power-electronics/knowledge to draft a related-work section on DC-DC converter control.
```

Another example:

```text
Use domains/power-electronics/terminology/domain-vocabulary.md to make this paragraph sound more like an IEEE power electronics paper.
```
