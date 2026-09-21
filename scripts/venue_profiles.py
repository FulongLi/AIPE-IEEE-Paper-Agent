"""Dependency-free venue profiles and portable asset lookup."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path, PureWindowsPath


def filesystem_path(path: Path) -> Path:
    """Support bundled assets beyond Windows' legacy 260-character path limit."""
    path = path.resolve()
    value = str(path)
    if os.name == "nt" and not value.startswith("\\\\?\\"):
        value = "\\\\?\\UNC\\" + value[2:] if value.startswith("\\\\") else "\\\\?\\" + value
    return Path(value)


def asset_root() -> Path:
    root = filesystem_path(Path(__file__).resolve().parents[1])
    return root / "assets" if (root / "assets" / "venues").is_dir() else root


def relative_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"expected a relative POSIX path: {value!r}")
    path = Path(value)
    if path.is_absolute() or PureWindowsPath(value).drive or ".." in path.parts:
        raise ValueError(f"path must stay inside its asset directory: {value}")
    target = (root / path).resolve()
    target.relative_to(root.resolve())
    return target


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def document_class(text: str) -> tuple[str, list[str]]:
    matches = re.findall(r"\\documentclass(?:\[([^\]]*)\])?\{([^}]+)\}", strip_comments(text))
    if len(matches) != 1:
        raise ValueError("expected exactly one document class")
    options, name = matches[0]
    return name, [part.strip() for part in options.split(",") if part.strip()]


def load_profile(venue: str, assets: Path | None = None) -> dict:
    assets = assets or asset_root()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", venue):
        raise ValueError(f"invalid venue id: {venue}")
    path = assets / "venues" / venue / "profile.json"
    if not path.is_file():
        raise ValueError(f"unknown venue: {venue}; use --list-venues")
    profile = json.loads(path.read_text(encoding="utf-8"))
    try:
        if profile["schema_version"] != 1 or profile["id"] != venue:
            raise ValueError("profile version or id mismatch")
        if profile["family"] not in {"journal", "conference"}:
            raise ValueError("invalid venue family")
        template = relative_path(assets, profile["template"]["path"])
        entry = relative_path(template, profile["template"]["entry"])
        text = entry.read_text(encoding=profile["template"].get("encoding", "utf-8"))
        expected = profile["document_class"]
        if document_class(text) != (expected["name"], expected["options"]):
            raise ValueError(f"profile class disagrees with {entry.name}")
        if not (template / (expected["name"] + ".cls")).is_file():
            raise ValueError("template is missing its document class")
        if profile["family"] == "journal" and "conference" in expected["options"]:
            raise ValueError("journal cannot use conference mode")
        if profile["layout"]["columns"] not in {1, 2}:
            raise ValueError("columns must be 1 or 2")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", profile["bibliography"]["style"]):
            raise ValueError("invalid bibliography style")
        active = strip_comments(text)
        normalization = profile["normalization"]
        if active.count(normalization["body_start"]) != 1:
            raise ValueError("body marker must occur exactly once")
        environments = ["abstract", normalization["keywords_environment"]]
        environments += normalization["placeholder_environments"]
        for environment in environments:
            for boundary in ("begin", "end"):
                if active.count("\\" + boundary + "{" + environment + "}") != 1:
                    raise ValueError(f"expected one {environment} {boundary}")
        for command in profile["checks"]["required_commands"] + normalization["end_commands"]:
            if command not in active:
                raise ValueError(f"missing required template command: {command}")
        for filename in profile["checks"]["required_assets"]:
            if not relative_path(template, filename).is_file():
                raise ValueError(f"missing required template asset: {filename}")
        for field in ("abstract", "keywords"):
            if type(profile["requirements"][field]) is not bool:
                raise ValueError(f"requirements.{field} must be boolean")
        for field in ("preserve_class", "preserve_margins", "preserve_fonts"):
            if profile["checks"][field] is not True:
                raise ValueError(f"checks.{field} must be true")
    except (KeyError, TypeError, OSError) as exc:
        raise ValueError(f"invalid profile {path}: {exc}") from exc
    return profile


def list_venues(assets: Path | None = None) -> list[str]:
    assets = assets or asset_root()
    return sorted(path.parent.name for path in (assets / "venues").glob("*/profile.json"))
