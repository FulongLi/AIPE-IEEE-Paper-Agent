# AI Figure Generation Workflow

Use this workflow after the paper direction, section outline, and figure/table plan are agreed.

## Purpose

Generate paper figures with an image-generation model such as Image 2 or the available image-generation tool, then store all final figure assets in the manuscript `figures/` folder for LaTeX and Overleaf use.

## Figure Planning First

Before generating images, create or update:

```text
notes/figure-plan.md
```

For each planned figure, record:

- figure number,
- target section,
- purpose in the argument,
- figure type,
- required technical content,
- evidence or assumptions,
- generation prompt,
- output filename,
- revision notes.

Do not generate decorative figures. Every figure must support the paper's argument, method, experiment, or explanation.

## Recommended Figure Types

For power electronics and IEEE papers, useful AI-generated figures include:

- converter topology overview,
- system architecture block diagram,
- control-loop block diagram,
- signal-flow diagram,
- operating-mode illustration,
- experimental setup schematic,
- workflow or algorithm diagram,
- conceptual comparison between baseline and proposed method.

Use measured plots, efficiency curves, Bode plots, waveforms, thermal maps, and quantitative result figures only when real data is supplied by the author or generated from verified simulation/measurement data. Do not invent numerical plots.

## Generation Rules

- Generate figures after the paper plan is stable.
- Use the paper's technical vocabulary, symbols, and section goals in the prompt.
- Prefer clean IEEE-style diagrams: white or transparent background, simple labels, high contrast, minimal decoration.
- Avoid photorealistic hardware images unless the author asks and the figure is clearly illustrative.
- Avoid fake measured axes, fake waveforms, fake numerical values, fake experimental labels, and fake device part numbers.
- Keep generated labels short. If exact labels matter, prefer adding text later in LaTeX, SVG, or a vector editor.
- Save generated images into `figures/` with portable filenames such as `fig-system-architecture.png`.
- Record the prompt and revision notes in `notes/figure-plan.md`.

## LaTeX Integration

Reference figures from `main.tex` or section files using relative paths:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig-system-architecture.png}
  \caption{System-level architecture of the proposed method.}
  \label{fig:system-architecture}
\end{figure}
```

Place `\label` after or inside `\caption`. Refer to the figure in text before or near its placement.

## Overleaf Package Rule

The final manuscript package must include:

- `main.tex`,
- `sections/`,
- `figures/`,
- `refs/`,
- `styles/`,
- any template-required files.

All generated figures must be inside `figures/`. Do not use local absolute image paths.

