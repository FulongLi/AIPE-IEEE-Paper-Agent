#!/usr/bin/env python3
"""Create a standard IEEE manuscript workspace."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


SECTION_FILES = [
    "00-abstract.tex",
    "01-introduction.tex",
    "02-related-work.tex",
    "03-method.tex",
    "04-experiments.tex",
    "05-results-discussion.tex",
    "06-conclusion.tex",
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise ValueError("manuscript slug cannot be empty")
    return slug


def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")


def create_workspace(root: Path, slug: str, title: str, template: Path | None) -> Path:
    workspace = root / "manuscripts" / slug
    workspace.mkdir(parents=True, exist_ok=False)

    for dirname in ["sections", "figures", "tables", "refs", "styles", "notes", "build"]:
        (workspace / dirname).mkdir()

    for section in SECTION_FILES:
        write_if_missing(
            workspace / "sections" / section,
            "% TODO: Draft this section from verified plan evidence.\n",
        )

    write_if_missing(workspace / "refs" / "references.bib", "% Add verified BibTeX entries here.\n")
    write_if_missing(
        workspace / "notes" / "paper-plan.md",
        "# Paper Plan\n\nTODO: Paste or summarize the approved paper plan.\n",
    )
    write_if_missing(
        workspace / "notes" / "evidence-checklist.md",
        "# Evidence Checklist\n\n- [ ] TODO: List missing experiments, figures, baselines, and claims.\n",
    )
    write_if_missing(
        workspace / "notes" / "figure-plan.md",
        "# Figure Plan\n\n| Figure | Section | Purpose | Type | Prompt/File | Revision Notes |\n| --- | --- | --- | --- | --- | --- |\n| Fig. 1 | Introduction | TODO | block diagram | figures/fig-system-overview.png | TODO |\n",
    )
    write_if_missing(
        workspace / "notes" / "citation-audit.md",
        "# Citation Audit\n\nTODO: Run scripts/check-citations.py after citations are added.\n",
    )
    write_if_missing(
        workspace / "notes" / "latex-todo.md",
        "# LaTeX TODO\n\n- [ ] Confirm target venue template and page limit.\n",
    )

    main_tex = rf"""\documentclass[conference]{{IEEEtran}}

\usepackage{{cite}}
\usepackage{{amsmath,amssymb,amsfonts}}
\usepackage{{graphicx}}

\title{{{title}}}

\author{{%
\IEEEauthorblockN{{Author Name}}
\IEEEauthorblockA{{Affiliation\\
Email}}
}}

\begin{{document}}
\maketitle

\input{{sections/00-abstract}}
\begin{{IEEEkeywords}}
TODO, IEEE paper, keywords
\end{{IEEEkeywords}}

\input{{sections/01-introduction}}
\input{{sections/02-related-work}}
\input{{sections/03-method}}
\input{{sections/04-experiments}}
\input{{sections/05-results-discussion}}
\input{{sections/06-conclusion}}

\bibliographystyle{{IEEEtran}}
\bibliography{{refs/references}}

\end{{document}}
"""
    write_if_missing(workspace / "main.tex", main_tex)

    if template:
        template_target = workspace / "styles" / "template-source"
        shutil.copytree(template, template_target)

    return workspace


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="short manuscript slug, for example wide-input-dcdc-control")
    parser.add_argument("--root", default=".", help="repository root or output root")
    parser.add_argument("--title", default="TODO: Working Title", help="LaTeX manuscript title")
    parser.add_argument("--template", help="optional template directory to copy into styles/template-source")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = slugify(args.slug)
    template = Path(args.template).resolve() if args.template else None

    if template and not template.is_dir():
        raise SystemExit(f"template directory not found: {template}")

    workspace = create_workspace(root, slug, args.title, template)
    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
