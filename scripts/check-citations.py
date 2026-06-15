#!/usr/bin/env python3
"""Check LaTeX citation keys against BibTeX entries."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CITE_RE = re.compile(r"\\cite(?:[a-zA-Z*]*)?(?:\[[^\]]*\]){0,2}\{([^}]+)\}")
BIB_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def collect_citations(root: Path) -> dict[str, set[str]]:
    citations: dict[str, set[str]] = {}
    for tex in root.rglob("*.tex"):
        if "build" in tex.parts:
            continue
        text = read_text(tex)
        for match in CITE_RE.finditer(text):
            for key in match.group(1).split(","):
                clean = key.strip()
                if clean:
                    citations.setdefault(clean, set()).add(str(tex.relative_to(root)))
    return citations


def collect_bib_keys(root: Path) -> dict[str, set[str]]:
    keys: dict[str, set[str]] = {}
    for bib in root.rglob("*.bib"):
        if "build" in bib.parts:
            continue
        text = read_text(bib)
        for match in BIB_RE.finditer(text):
            key = match.group(1).strip()
            if key:
                keys.setdefault(key, set()).add(str(bib.relative_to(root)))
    return keys


def write_audit(root: Path, citations: dict[str, set[str]], bib_keys: dict[str, set[str]]) -> None:
    notes = root / "notes"
    notes.mkdir(exist_ok=True)
    missing = sorted(set(citations) - set(bib_keys))
    uncited = sorted(set(bib_keys) - set(citations))
    resolved = sorted(set(citations) & set(bib_keys))

    lines = ["# Citation Audit", ""]
    lines.extend(["## Resolved Citations", ""])
    lines.extend(
        f"- `{key}`: cited in {', '.join(sorted(citations[key]))}; found in {', '.join(sorted(bib_keys[key]))}."
        for key in resolved
    )
    if not resolved:
        lines.append("- None.")

    lines.extend(["", "## Missing BibTeX Entries", ""])
    lines.extend(f"- `{key}`: cited in {', '.join(sorted(citations[key]))}." for key in missing)
    if not missing:
        lines.append("- None.")

    lines.extend(["", "## Uncited BibTeX Entries", ""])
    lines.extend(f"- `{key}`: present in {', '.join(sorted(bib_keys[key]))}." for key in uncited)
    if not uncited:
        lines.append("- None.")

    (notes / "citation-audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", help="manuscript workspace path")
    parser.add_argument("--write-audit", action="store_true", help="write notes/citation-audit.md")
    args = parser.parse_args()

    root = Path(args.workspace).resolve()
    if not root.is_dir():
        raise SystemExit(f"workspace not found: {root}")

    citations = collect_citations(root)
    bib_keys = collect_bib_keys(root)
    missing = sorted(set(citations) - set(bib_keys))
    uncited = sorted(set(bib_keys) - set(citations))

    print(f"citations: {len(citations)}")
    print(f"bib entries: {len(bib_keys)}")
    print(f"missing bib entries: {len(missing)}")
    for key in missing:
        print(f"  missing: {key}")
    print(f"uncited bib entries: {len(uncited)}")
    for key in uncited:
        print(f"  uncited: {key}")

    if args.write_audit:
        write_audit(root, citations, bib_keys)

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

