# IEEE LaTeX and Submission Checklist

## Template Selection

Start from the official venue template. Do not rewrite IEEE class files or change margins, fonts, line spacing, column widths, bibliography style, or caption styling unless the venue instructions explicitly require it.

Common patterns:

- Conference: `\documentclass[conference]{IEEEtran}`
- Transactions/journal: `\documentclass[lettersize,journal]{IEEEtran}`
- IEEE Access: `\documentclass{ieeeaccess}`

In this repository, useful starting points live under `venues/`, including conference, Transactions, IEEE Access, TAI, OJCSYS, and OJPEL templates.

## Front Matter

Check the title, author blocks, affiliations, ORCID/email requirements, funding notes, copyright footers, running headers, corresponding author, and anonymization rules.

Avoid symbols, footnotes, and special formatting in titles unless the current template explicitly permits them. Keep the abstract self-contained. Define acronyms on first use in the abstract and body as required by the template.

## Sections

Use the section structure expected by the venue and paper type. Typical research papers include:

- Abstract
- Keywords
- Introduction
- Related Work or Background
- Method/System/Model
- Experiments/Evaluation
- Discussion or Limitations when needed
- Conclusion
- Acknowledgment when allowed
- References

Do not manually number headings. Let LaTeX and the IEEE class handle numbering.

## Figures

Use vector graphics for plots when possible. Ensure text remains legible at final column width. Avoid screenshots of plots unless unavoidable.

Figure rules:

- Put `\caption` after `\includegraphics`.
- Put `\label` after or inside `\caption`.
- Use `figure*` sparingly for two-column floats.
- Refer to figures before or near placement.
- Keep filenames stable and portable; avoid spaces when creating new files.

## Tables

IEEE table captions usually appear above the table. Put `\label` after or inside `\caption`. Include units in headers, align decimals when practical, and make the metric direction clear.

Use tables for exact comparisons and figures for trends. Do not make tables unreadably small to force page limits.

## Equations

Define symbols before or immediately after use. Punctuate equations as part of the sentence. Use `\eqref{...}` for equation references. Avoid `eqnarray`; prefer `align`, `multline`, or `IEEEeqnarray` when suitable.

Do not hard-code equation numbers. Do not use display equations in abstracts unless the venue explicitly allows them.

## Citations and Bibliography

Use `\cite{...}` and BibTeX entries with complete metadata. Multiple citations can be grouped in one command. Ensure every cited work appears in the bibliography and every bibliography item is cited, unless the venue allows uncited references.

Prefer primary sources over survey-only citations for core technical claims. Cite datasets, software, standards, and benchmark definitions when they materially support the work.

## LaTeX Hygiene

Before submission:

- Compile from a clean state.
- Fix undefined references and citations.
- Inspect overfull and underfull boxes that affect readability.
- Confirm figures are included at the expected resolution.
- Check page limits and file size limits.
- Remove template filler text and unused sample images.
- Remove draft packages, comments with sensitive content, and local absolute paths.
- Verify generated PDF metadata if required by the venue.

## Common IEEE Style Details

Use SI units consistently. Put a zero before decimal points. Avoid vague intensifiers such as "very", "clearly", and "obviously". Use "Fig." for figure references in many IEEE styles, but follow the current template. Use "et al." with a period after "al." and no period after "et".
