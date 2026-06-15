# AI Figure Generation Workflow

Use this reference after the user has agreed on the paper direction, section outline, and figure/table plan.

## Core Rule

Generate figures with Image 2 or the available image-generation tool only after the paper plan is stable. Store all final figure assets in the manuscript `figures/` folder so the LaTeX package can be opened directly in Overleaf.

## Required Planning Artifact

Create or update:

```text
notes/figure-plan.md
```

For each figure, track:

- figure number,
- target section,
- purpose,
- figure type,
- technical content,
- assumptions or required evidence,
- generation prompt,
- output filename,
- revision notes.

## What AI May Generate

Appropriate generated figures:

- system architecture block diagrams,
- converter topology overviews,
- control-loop diagrams,
- method/workflow diagrams,
- operating-mode illustrations,
- experimental setup schematics,
- conceptual baseline-versus-proposed illustrations.

Do not invent quantitative result plots, measured waveforms, efficiency curves, Bode plots, thermal maps, or numerical comparisons. Generate those only from author-supplied data or verified simulation output.

## Visual Style

- Prefer clean IEEE-style diagrams.
- Use white or transparent backgrounds.
- Use high contrast and simple labels.
- Keep labels short and technically conservative.
- Avoid decorative visual noise.
- Avoid fake hardware details, fake part numbers, fake axes, and fake measurements.

## File Handling

- Save generated figures under `figures/`.
- Use ASCII filenames with no spaces, for example `fig-control-loop.png`.
- Use relative paths in LaTeX.
- Keep prompt/revision history in `notes/figure-plan.md`.
- If the user wants editable diagrams, note that the generated raster can be recreated or refined later, but exact text-heavy diagrams may be better finished in LaTeX/TikZ, SVG, PowerPoint, Figma, or another vector editor.

