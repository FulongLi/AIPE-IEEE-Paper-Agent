# Plan-to-Article Workflow

Use this reference after the user already has a paper plan, section plan, or research brief and wants the skill to produce a manuscript scaffold or draft.

## Operating Principle

Draft the paper from verified structure and available evidence. Do not fabricate experiments, datasets, numerical results, citations, hardware specifications, or comparative claims. If evidence is missing, write a precise placeholder and add the item to the evidence checklist.

## Required Inputs

Collect or infer:

- working title,
- target venue or template family,
- research problem and gap,
- method or core idea,
- planned section outline,
- available theory, simulation, hardware, data, or prototype evidence,
- candidate references or reference database location,
- expected figures and tables,
- author-supplied constraints such as page limit, anonymity, and Overleaf use.

If any item is missing, continue with labeled assumptions and create `notes/evidence-checklist.md`.

## Generation Stages

1. Normalize the paper plan.
   - Convert vague ideas into research questions.
   - Map each research question to one section, figure, table, equation, or experiment.
   - Mark unsupported claims as missing evidence.

2. Create or update the manuscript workspace.
   - Follow `manuscript-workspace-standard.md`.
   - Copy an IEEE template into the manuscript workspace.
   - Keep official `.cls`, `.bst`, `.sty`, font, and logo files unchanged.

3. Build the LaTeX skeleton.
   - Create `main.tex` or adapt the template main file.
   - Use `sections/` for manuscript body files when the template permits `\input`.
   - Add placeholders for abstract, keywords, introduction, method, evidence, results, limitations, and conclusion.
   - Add figure and table placeholders only when the paper plan requires them.

4. Draft in evidence order.
   - Draft method, model, or system sections before the Introduction.
   - Draft experiment/setup/results only from available author-supplied evidence.
   - Draft Introduction and Abstract after the evidence map is clear.
   - Use power electronics vocabulary and language-bank material when the topic is in power electronics.

5. Add citations conservatively.
   - Use verified BibTeX entries from the manuscript `refs/` folder, the repository `PE_IEEE_reference/` folder, or user-provided trusted sources.
   - Use `citation-needed` comments instead of invented references.
   - Follow `citation-verification-policy.md`.

6. Produce review notes.
   - Update `notes/evidence-checklist.md`.
   - Update `notes/citation-audit.md`.
   - Update `notes/latex-todo.md` when compile or template tasks remain.

## Expected Output

For a draft request, produce:

- manuscript workspace structure,
- LaTeX skeleton or edited `.tex` files,
- section-level draft text where evidence exists,
- explicit placeholders where author input is required,
- citation audit,
- next author actions.

For a planning-only request, do not create manuscript files unless the user asks. Return a plan with missing evidence and recommended template.

