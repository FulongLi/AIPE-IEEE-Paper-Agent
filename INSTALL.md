# Installing AIPE IEEE Paper Agent

Use the full repository or a generated self-contained package. `core/` is the
canonical instruction source, with sibling venue/domain/artifact/script assets;
copying `core/SKILL.md` alone is not a complete installation.

## Repository Mode

Open this repository in Codex or Claude and start with `AGENTS.md` and
`core/SKILL.md`. Python tools require Python 3.10+ with no external dependencies.
PDF builds require a separate LaTeX installation, or upload a generated workspace
to Overleaf and select `main.tex`.

## Build or Download a Release

Use release artifacts, or build them from the repository root:

```bash
python scripts/package-release.py
```

All six supported venue profiles/templates and the optional power-electronics
pack/reference library are included by default. To omit the domain and limit venues:

```bash
python scripts/package-release.py --without-domain --venue ieee-access --venue ieee-ojpel --dist dist/generic
```

The packager generates portable `references/` from `core/workflows/` and
`core/policies/`, renders `core/SKILL.md` with portable paths, and copies relevant
assets plus runtime scripts. `generated-sources.json` identifies canonical sources.
Never maintain or edit generated instruction copies independently.

## Codex Skill

Extract `ieee-paper-latex-writing-codex-skill-v<version>.zip` into
`~/.codex/skills/` (Windows: `C:\Users\<you>\.codex\skills\`). The result should be
`~/.codex/skills/ieee-paper-latex-writing/SKILL.md`. Restart Codex after installation.
The previous source-only GitHub skill path is no longer maintained; use this full
package or repository mode so venue profiles and scripts are available.

## Codex Plugin Marketplace

Extract `aipe-ieee-paper-agent-codex-plugin-marketplace-v<version>.zip` into a stable
local folder and add its marketplace using the existing plugin installation flow:

```bash
codex plugin marketplace add <path-to-unzipped-codex-plugin-marketplace>
codex plugin add aipe-ieee-paper-agent@aipe-local
```

Start a new Codex task after installation/update. The plugin's skill contains its
own `references/`, `scripts/`, and `assets/`, so resource lookup stays local to the skill.

## Claude Skill

Use `aipe-ieee-paper-agent-claude-skill-v<version>.zip` through the skill installation
surface supported by your Claude product. The archive contains one skill folder
with `SKILL.md`, `references/`, `scripts/`, and `assets/`.

```text
Use the IEEE paper-production skill. Turn this plan into a manuscript for
ieee-transactions. Verify reference sources and mark missing evidence as TODOs.
```

## Running Installed Tools

From another working directory, invoke the script using its installed absolute
path. For example, substitute your skill directory below:

```bash
python <skill-dir>/scripts/create-manuscript.py my-paper --venue ieee-access --root <output-dir>
python <skill-dir>/scripts/check-citations.py <output-dir>/manuscripts/my-paper --write-audit
python <skill-dir>/scripts/check-latex.py <output-dir>/manuscripts/my-paper
```

The output root does not need a checkout or any assets. `--domain power-electronics`
is available only when that pack is included. The index builder defaults to the
bundled library; generic packages can instead pass `--ref-dir` for user references.

## Maintainers

Edit `core/`, `venues/` profiles, `domains/`, `artifacts/`, and `scripts/` as needed;
preserve official template/support files. Keep the existing `PE_IEEE_reference/`
collection and rebuild its index after BibTeX changes. Curated domain notes may be
packaged; raw extraction/private caches and source books are excluded.

Before release run:

```bash
python -m unittest discover -s tests -v
python scripts/build-reference-index.py
python scripts/package-release.py
```

Tests initialize every venue, check actual template differences and relative
paths, exercise citation/index behavior, verify official template checksums, and
extract/run all three release formats from an unrelated working directory.
Compile and visually inspect completed manuscripts separately; static validation
does not claim PDF compilation or publication readiness.

Update `VERSION` for releases and upload the three ZIPs in `dist/` as appropriate.
Use patch versions for small content fixes, minor versions for new workflows/tools,
and major versions for incompatible established workflows.
