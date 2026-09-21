# Publication-Readiness Review

Use `core/policies/scientific-integrity.md`, `core/policies/citation-policy.md`,
and `core/policies/latex-policy.md` as the authoritative review criteria.

1. Inspect the research spine and evidence matrix. Check explicit novelty, fair
   baselines, reproducible conditions, supported contributions, and limitations.
2. Run `scripts/check-citations.py <workspace> --write-audit`, then inspect source
   metadata and claim relevance using `core/workflows/citation-verification.md`.
3. Run `scripts/check-latex.py <workspace>` to check venue class, essential front
   matter, relative file references, and unchanged official support assets.
4. Compile `main.tex` from a clean workspace with the venue's toolchain. Inspect
   errors, missing references, font substitutions, overfull boxes, and the PDF.
5. Confirm current submission limits, author/anonymity metadata, bibliography,
   figure readability at column width, units, caption placement, and absence of
   TODOs and sample text. Remove unused demonstration assets before submission.

Report blocking issues first, then important improvements, then optional polish.
Distinguish executed checks from checks that still require tools or author input.
Static validation does not establish a successful PDF build or scientific quality.
