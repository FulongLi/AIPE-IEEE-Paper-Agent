# IEEE Research Writing Playbook

## Manuscript Spine

Before drafting, force the paper into five sentences:

1. Problem: what concrete scientific or engineering problem matters?
2. Gap: what exactly current methods, theory, datasets, or systems fail to handle?
3. Idea: what is the central mechanism or insight?
4. Evidence: what proves the idea works?
5. Impact: what changes for the reader if the claim is true?

If any sentence is vague, improve the research story before polishing prose.

## Title

Make the title searchable and claim-bearing. Prefer "Method/Mechanism for Problem under Condition" over a clever slogan. Avoid unexplained acronyms, math-heavy notation, broad superlatives, and phrases such as "A Novel Approach" unless the novelty is explicit.

## Abstract

Use a compact five-move abstract:

1. Context and problem.
2. Specific gap or limitation.
3. Proposed method or core idea.
4. Main quantitative or theoretical results.
5. Implication and scope.

Keep it self-contained. Avoid citations, footnotes, undefined acronyms, displayed equations, and claims not supported in the body. For IEEE Access, respect the common 150-250 word, one-paragraph expectation unless the current template says otherwise.

## Introduction

Build the Introduction as an argument, not a tour:

1. Establish importance in the first paragraph with a concrete setting.
2. Name the technical barrier that makes the problem hard.
3. Explain why prior work is insufficient using categories, not a list of papers.
4. State the core idea in plain technical language.
5. Summarize evidence and contributions with measurable outcomes.

Contribution bullets should be verifiable. A weak contribution says "we propose a framework"; a strong one says what the framework enables, how it differs, and where the proof or evaluation appears.

## Related Work

Organize by concepts, assumptions, or method families. For each cluster, say:

- what the cluster is good at,
- what assumption or limitation matters for this paper,
- how the proposed work differs.

Avoid dismissive language. Use "complementary", "orthogonal", "requires", "assumes", and "does not address" only when technically accurate.

## Methods

Make the method reproducible and inspectable:

- Define inputs, outputs, symbols, and assumptions before equations.
- Separate design intuition from formal procedure.
- Explain each module's role in the overall claim.
- For algorithms, state complexity, convergence condition, or operational constraints when relevant.
- For systems papers, describe implementation details that affect performance or reproducibility.

## Experiments

Experiments should answer research questions, not merely show plots.

Use this structure:

1. Research questions or hypotheses.
2. Datasets, workloads, hardware, or simulation setup.
3. Baselines and why they are fair.
4. Metrics and statistical treatment.
5. Main results.
6. Ablations and sensitivity analysis.
7. Failure cases or limits.

A table without a question is decoration. A figure without an interpretation is unfinished evidence.

## Figures and Tables

Every major figure should be understandable at IEEE two-column scale.

Captions should state what is plotted, the experimental condition, and the takeaway. Tables should include units, dataset names, metric direction, and baseline grouping. Prefer fewer, denser figures that support the argument over many isolated charts.

## Claims and Tone

Use active voice and quantified claims. Replace "significantly improves performance" with the measured improvement and context. Avoid universal claims unless proven across the relevant domain. Good hedges protect credibility: "on the evaluated benchmarks", "for the tested operating range", "under the stated assumptions".

## Final Quality Test

A publishable paper should answer these questions without the reader guessing:

- What is new?
- Why was it hard?
- Why is the solution technically sound?
- What evidence supports each claim?
- What are the limits?
- Why should this venue's audience care?
