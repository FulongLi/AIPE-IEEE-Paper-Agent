# Idea-to-Paper Workflow

Use this workflow when a user has a rough research idea and wants to turn it into a scientific paper.

## Inputs

Ask for or infer the following:

- Research domain and target audience
- Core idea or proposed method
- Problem setting
- Expected novelty
- Available experiments, simulations, data, theory, or prototype
- Target venue type: IEEE conference, IEEE Transactions/journal, IEEE Access/open journal, or unknown
- Page limit if known

If information is missing, proceed with clearly labeled assumptions and a "missing evidence" list.

## Step 1: Clarify the Research Spine

Produce five concise statements:

1. Problem: what technical problem matters?
2. Gap: what current methods fail to solve or explain?
3. Idea: what is the user's core mechanism, method, model, or system?
4. Evidence: what proof, experiment, simulation, or prototype can support it?
5. Impact: why should the venue audience care?

Use this pattern:

```text
This paper addresses <problem> in <application/domain>. Existing approaches struggle with <gap>. We propose <idea>, which enables <benefit>. The claim can be tested through <evidence>. This matters because <impact>.
```

## Step 2: Convert the Idea Into Research Questions

Create 3-5 research questions. Each question should map to one result section, figure, table, theorem, or experiment.

Good research questions are testable:

- How does the proposed method compare with baseline methods under <condition>?
- Which design parameter most strongly affects <metric>?
- Does the proposed controller remain stable under <disturbance>?
- What tradeoff exists among <efficiency>, <power density>, and <control complexity>?

## Step 3: Draft Contribution Claims

Write 2-4 contributions. Each contribution must be concrete and verifiable.

Use this format:

```text
1. We develop <method/model/system> that <technical capability>, addressing <gap>.
2. We derive/analyze <model/theorem/design rule> that explains <mechanism>.
3. We validate <claim> using <simulation/experiment/prototype/dataset> across <conditions>.
```

Do not claim novelty without specifying the technical difference.

## Step 4: Build the Paper Outline

Use a default IEEE research-paper structure:

1. Abstract
2. Introduction
3. Related Work / Background
4. System Model / Method / Converter Design
5. Analysis / Control / Theoretical Development
6. Experimental or Simulation Setup
7. Results and Discussion
8. Limitations
9. Conclusion

For each section, provide:

- purpose,
- key messages,
- required evidence,
- likely figures/tables/equations.

## Step 5: Build the Figure and Table Plan

Create a figure/table plan before drafting prose.

Typical figures:

- System architecture or converter topology
- Operating waveforms or switching states
- Control block diagram
- Small-signal model or equivalent circuit
- Experimental prototype or test setup
- Efficiency curve, transient response, Bode plot, or ablation plot

Typical tables:

- Specification table
- Parameter table
- Baseline comparison
- Loss breakdown
- Component stress comparison
- Experimental condition summary

## Step 6: Identify Missing Evidence

List what must be produced before the paper can make strong claims:

- Baselines
- Metrics
- Datasets or operating points
- Hardware prototype details
- Simulation model details
- Ablations
- Statistical treatment
- Failure cases or limitations
- Citations and standards

Classify each item as:

- blocking,
- important,
- optional.

## Step 7: Choose the LaTeX Template

Recommend a starting template:

- IEEE conference: `venues/ieee-conference/template/`
- IEEE Transactions/journal: `venues/ieee-transactions/template/`
- IEEE Access: `venues/ieee-access/template/`
- Specialized open journals: inspect the matching template folder.

Do not modify the source template. Copy it into a manuscript workspace first.

## Output Format

Return:

```markdown
# Paper Plan

## Working Title

## Research Spine

## Research Questions

## Contributions

## Paper Outline

## Figure and Table Plan

## Evidence Needed

## Recommended Template

## Next Actions
```
