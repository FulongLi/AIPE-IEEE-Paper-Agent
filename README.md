# IEEE Paper Agent

A LaTeX template and writing-skill repository for drafting, organizing, and reviewing IEEE-style research papers.

This repository helps authors quickly find the right IEEE LaTeX template and use a structured writing workflow to turn research ideas into publication-ready manuscripts.

## What This Repository Does

- Collects common IEEE LaTeX templates, including conference, Transactions/journal, IEEE Access, TAI, OJCSYS, and OJPEL formats.
- Provides a reusable Codex Skill, `ieee-paper-latex-writing`, for IEEE paper writing, LaTeX editing, pre-submission checks, and reviewer-response preparation.
- Organizes practical research-writing knowledge into executable workflows: paper storyline, Introduction, Related Work, Method, Experiments, Figures/Tables, and LaTeX submission checks.

## Repository Structure

```text
IEEE-Paper-Agent/
├── IEEE paper Template/
│   ├── IEEE-conference-template-062824/
│   ├── Conference-LaTeX-template_10-17-19/
│   ├── IEEE-Transactions-LaTeX2e-templates-and-instructions/
│   ├── ACCESS_latex_template_20240429/
│   ├── TAI_LaTex_Template/
│   ├── OJCSYS_template_Latex/
│   ├── IEEE-ojpel-latex-template/
│   └── Transactions_win_or_mac_LaTeX2e_style_file/
└── skills/
    └── ieee-paper-latex-writing/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## How to Use the LaTeX Templates

1. Choose a template based on the target venue:
   - IEEE conference: start with `IEEE paper Template/IEEE-conference-template-062824/`
   - IEEE Transactions / journal: start with `IEEE paper Template/IEEE-Transactions-LaTeX2e-templates-and-instructions/`
   - IEEE Access: use `IEEE paper Template/ACCESS_latex_template_20240429/`
   - TAI / OJCSYS / OJPEL: use the corresponding template directory

2. Copy the selected template directory and use the copy as your paper workspace.

3. Edit the `.tex` file, figures, and BibTeX files inside your copied workspace. Do not modify official `.cls` files unless the target venue explicitly requires it.

4. Compile the paper with your local LaTeX environment, for example:

```bash
latexmk -pdf main.tex
```

If the template uses a different `.tex` filename, replace `main.tex` with the correct file name.

## How to Use the Writing Skill

The skill is located at:

```text
skills/ieee-paper-latex-writing/
```

It is useful for:

- Generating an IEEE paper outline from a research idea
- Rewriting abstracts, introductions, related work, methods, and experiment sections
- Checking whether the paper contributions are clear and defensible
- Reviewing whether a LaTeX manuscript follows IEEE submission practices
- Checking figures, tables, equations, citations, and references
- Organizing reviewer comments and preparing rebuttal / response letters

Example Codex prompt:

```text
Use the skill at skills/ieee-paper-latex-writing to review my IEEE paper draft.
```

Another example:

```text
Use ieee-paper-latex-writing to help me rewrite the abstract and introduction for an IEEE Transactions paper.
```

## Core Skill Materials

- `SKILL.md`: Main workflow that explains when to use the skill and how to approach IEEE writing and LaTeX review.
- `references/writing-playbook.md`: Writing guidance for IEEE research papers, including titles, abstracts, Introduction, Related Work, Methods, Experiments, figures, tables, and tone.
- `references/latex-submission-checklist.md`: IEEE LaTeX pre-submission checklist.
- `references/reviewer-response.md`: Reviewer-response and revision workflow.

## Recommended Workflow

1. Choose the target IEEE venue and template.
2. Use the skill to clarify the paper spine:
   - What is the research problem?
   - What gap exists in current methods?
   - What is the core method or idea?
   - What are the main contributions?
   - What experiments, theory, or evidence support those contributions?
3. Draft the outline, then write the abstract and introduction.
4. Fill in the method, experiment, related work, and conclusion sections.
5. Compile the PDF and use the LaTeX checklist to review formatting, citations, figures, equations, and page limits.
6. Run a publication-readiness review before submission.

## Who This Is For

- Students and researchers writing IEEE conference papers
- Authors preparing IEEE Transactions or journal submissions
- Research teams that want to standardize LaTeX templates, writing workflows, and submission checks
- Anyone using an AI agent to support research writing, rewriting, and reviewer-response preparation

## Notes

- This repository provides templates and writing workflows; it does not replace the latest author guidelines from the target conference or journal.
- Before submission, always check the target venue website for page limits, anonymization rules, copyright requirements, bibliography style, and supplementary-material rules.
- Do not change official IEEE class files, margins, fonts, or line spacing just to reduce page count.
- The writing skill does not generate real experimental results, citations, or data. All scientific claims must be supported by your experiments, theory, or credible literature.
