# Reviewer Response Workflow

## First Pass

Separate reviewer comments into:

- correctness or validity concerns,
- missing experiments or evidence,
- unclear writing or organization,
- related work or positioning,
- formatting and presentation,
- requests that conflict with page limits or scope.

Do not answer defensively. Treat each comment as a signal about what the manuscript failed to make obvious.

## Response Matrix

For each comment, create:

1. Reviewer and comment ID.
2. Concern in one neutral sentence.
3. Action taken in the manuscript.
4. Exact section, page, figure, table, or line changed.
5. Response text.

If no manuscript change is made, explain why with evidence and offer a clarifying statement when possible.

## Response Tone

Start with acknowledgment, then action, then evidence. Keep responses concise:

```text
Thank you for pointing this out. We have revised Section III-B to define the scheduling constraint before introducing Eq. (4), and we added a short explanation of why the constraint is convex under Assumption 1. The revised text appears on page 4, left column.
```

Avoid "we disagree" as the first move. Prefer "We clarify", "We have added", "We now report", or "We respectfully note" when a correction is needed.

## Revision Strategy

Prioritize issues that affect acceptance:

1. Validity of the main claim.
2. Fairness of baselines or experimental setup.
3. Missing comparisons, ablations, or statistical treatment.
4. Unclear novelty.
5. Readability and formatting.

When page limits force tradeoffs, compress low-value prose before removing evidence.

## Rebuttal Safety

Do not invent new results. Do not claim experiments were added unless the manuscript contains them. Do not promise future work as a substitute for current evidence unless the reviewer request is outside scope. Make every response traceable to a manuscript edit or a precise rationale.
