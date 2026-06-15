# Installing AIPE IEEE Paper Agent

This repository supports three installation paths:

1. Codex skill from GitHub.
2. Codex plugin marketplace package.
3. Claude-compatible skill ZIP.

## For Codex Users

### Simple GitHub Skill Install

Ask Codex:

```text
Install the skill from this GitHub repository:
<owner>/<repo>, path: skills/ieee-paper-latex-writing
```

Restart Codex after installation.

This installs the source skill. It is best when the user will also open this full repository, or when the workflow guidance is enough.

Copy-ready prompt:

```text
Please install the Codex skill from GitHub repo <owner>/<repo> at path skills/ieee-paper-latex-writing. After installing, remind me to restart Codex.
```

### Full Codex Skill Package

Use the release artifact:

```text
ieee-paper-latex-writing-codex-skill-v<version>.zip
```

Unzip the folder into:

```text
~/.codex/skills/
```

On Windows this is usually:

```text
C:\Users\<you>\.codex\skills\
```

Restart Codex after installation.

This package includes the skill plus repository assets such as workflows, templates, power electronics references, and scripts.

### Codex Plugin Marketplace Package

Use the release artifact:

```text
aipe-ieee-paper-agent-codex-plugin-marketplace-v<version>.zip
```

Unzip it to a stable local folder. Then add the local marketplace:

```bash
codex plugin marketplace add <path-to-unzipped-codex-plugin-marketplace>
codex plugin add aipe-ieee-paper-agent@aipe-local
```

Start a new Codex thread after installing or updating the plugin.

## For Claude Users

Use the release artifact:

```text
aipe-ieee-paper-agent-claude-skill-v<version>.zip
```

Upload or install the ZIP as a Claude skill, depending on the Claude product surface you are using. The package root contains `SKILL.md`, `references/`, `scripts/`, and `assets/`.

Copy-ready prompt after upload:

```text
Use the AIPE IEEE Paper Agent skill. Turn this paper plan into an IEEE manuscript workspace, verify citations from the bundled reference index, and mark missing experiments instead of inventing results.
```

## Maintainer Release Workflow

1. Update the source materials:
   - `skills/ieee-paper-latex-writing/`
   - `workflows/`
   - `templates/`
   - `knowledge-base/`
   - `PE_IEEE_reference/*.bib`
   - `scripts/`

2. Update `VERSION` using semantic versioning:

```text
0.1.0
```

3. Rebuild the reference index and release packages:

```bash
python scripts/package-release.py
```

The packaging script automatically runs:

```bash
python scripts/build-reference-index.py
```

4. Upload the generated ZIP files from `dist/` to the GitHub release.

5. Tell users to install from the newest release artifact or ask Codex to install from the GitHub skill path.

## Versioning Notes

- Use patch versions for reference additions, prompt updates, and minor workflow fixes.
- Use minor versions for new scripts, new workflows, or changed manuscript structure.
- Use major versions only when old prompts or generated manuscript layouts may no longer behave the same way.
