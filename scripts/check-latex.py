#!/usr/bin/env python3
"""Static venue/layout audit. Compilation and PDF inspection remain separate steps."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from venue_profiles import asset_root, document_class, load_profile, relative_path, strip_comments

SUPPORT_SUFFIXES = {".cls", ".bst", ".sty", ".pfb", ".tfm", ".fd", ".map", ".png", ".jpg", ".eps"}


def audit(workspace: Path) -> list[str]:
    errors = []
    try:
        snapshot = json.loads((workspace / "notes" / "venue-profile.json").read_text(encoding="utf-8"))
        profile = load_profile(snapshot["id"])
        if snapshot != profile:
            errors.append("saved venue profile differs from the canonical profile")
        main = strip_comments((workspace / "main.tex").read_text(encoding="utf-8"))
        expected = profile["document_class"]
        if document_class(main) != (expected["name"], expected["options"]):
            errors.append("document class/options do not match the selected venue")
        for command in profile["checks"]["required_commands"]:
            if command not in main:
                errors.append(f"missing venue command: {command}")
        for directory in ("sections", "figures", "tables", "refs", "styles", "notes", "build"):
            if not (workspace / directory).is_dir():
                errors.append(f"missing workspace directory: {directory}")
        for environment in ("abstract", profile["normalization"]["keywords_environment"]):
            if r"\begin{" + environment + "}" not in main:
                errors.append(f"missing {environment}")
        if r"\bibliographystyle{" + profile["bibliography"]["style"] + "}" not in main:
            errors.append("bibliography style does not match venue")
        for tex in workspace.rglob("*.tex"):
            if "build" in tex.relative_to(workspace).parts:
                continue
            text = strip_comments(tex.read_text(encoding="utf-8"))
            pattern = r"\\(input|include|includegraphics|bibliography)(?:\[[^\]]*\])?\{([^}]+)\}"
            for match in re.finditer(pattern, text):
                command, values = match.groups()
                for value in values.split(","):
                    try:
                        target = relative_path(workspace, value.strip())
                        extensions = {"input": [".tex"], "include": [".tex"], "bibliography": [".bib"],
                                      "includegraphics": [".pdf", ".png", ".jpg", ".eps"]}[command]
                        if not target.is_file() and not any(Path(str(target) + ext).is_file() for ext in extensions):
                            errors.append(f"missing {command} file: {value}")
                    except ValueError:
                        errors.append(f"non-portable path: {value}")
        template = relative_path(asset_root(), profile["template"]["path"])
        for source in template.rglob("*"):
            if source.is_file() and source.suffix.lower() in SUPPORT_SUFFIXES:
                target = workspace / source.relative_to(template)
                # Unused demonstration images may be removed before submission.
                # Fonts/classes/styles and profile-declared logos remain required.
                required = (source.suffix.lower() not in {".png", ".jpg", ".eps"}
                            or source.relative_to(template).as_posix() in profile["checks"]["required_assets"])
                if not required and not target.exists():
                    continue
                if not target.is_file() or target.read_bytes() != source.read_bytes():
                    errors.append(f"missing or modified template asset: {source.name}")
    except (OSError, KeyError, ValueError) as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace")
    args = parser.parse_args()
    errors = audit(Path(args.workspace).resolve())
    for error in errors:
        print(f"ERROR: {error}")
    print(f"static venue audit: {'FAIL' if errors else 'PASS'}; PDF compilation and content readiness not assessed")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
