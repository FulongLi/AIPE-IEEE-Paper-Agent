#!/usr/bin/env python3
"""Generate self-contained Codex/Claude packages from canonical repository assets."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

from venue_profiles import filesystem_path, list_venues, load_profile

ROOT = filesystem_path(Path(__file__).resolve().parents[1])
DIST = ROOT / "dist"
IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc",
                               "raw-mineru-output", "workspace", "private-fulltext-cache")
RUNTIME_SCRIPTS = ("create-manuscript.py", "venue_profiles.py", "check-latex.py",
                   "build-reference-index.py", "check-citations.py")


def clean_generated(path: Path, dist: Path) -> None:
    # Only remove a named package directory below the chosen output root.
    target, boundary = path.resolve(), dist.resolve()
    target.relative_to(boundary)
    if target == boundary or target == ROOT.resolve():
        raise ValueError("refusing to remove the output/repository root")
    if target.exists():
        shutil.rmtree(target)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def zip_dir(source: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source.parent))


def render_instruction(text: str) -> str:
    """Rewrite repository-root instruction paths to portable skill-root paths."""
    text = text.replace("core/SKILL.md", "SKILL.md").replace("AGENTS.md", "SKILL.md")
    text = text.replace("core/workflows/", "references/workflows/")
    text = text.replace("core/policies/", "references/policies/")
    return re.sub(r"(?<![\w/-])(venues/|domains/|artifacts/|PE_IEEE_reference/)", r"assets/\1", text)


def build_skill(target: Path, dist: Path, venues: list[str], include_domain: bool) -> None:
    clean_generated(target, dist)
    target.mkdir(parents=True)
    provenance = []
    sources = [(ROOT / "core" / "SKILL.md", target / "SKILL.md")]
    for kind in ("workflows", "policies"):
        sources.extend((path, target / "references" / kind / path.name)
                       for path in sorted((ROOT / "core" / kind).glob("*.md")))
    for source, destination in sources:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render_instruction(source.read_text(encoding="utf-8")), encoding="utf-8")
        provenance.append({
            "source": source.relative_to(ROOT).as_posix(),
            "target": destination.relative_to(target).as_posix(),
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "generated_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        })
    shutil.copytree(ROOT / "core" / "agents", target / "agents")
    assets = target / "assets"
    shutil.copytree(ROOT / "artifacts", assets / "artifacts", ignore=IGNORE)
    copy_file(ROOT / "venues" / "README.md", assets / "venues" / "README.md")
    for venue in venues:
        shutil.copytree(ROOT / "venues" / venue, assets / "venues" / venue, ignore=IGNORE)
    if include_domain:
        shutil.copytree(ROOT / "domains" / "power-electronics",
                        assets / "domains" / "power-electronics", ignore=IGNORE)
        shutil.copytree(ROOT / "PE_IEEE_reference", assets / "PE_IEEE_reference", ignore=IGNORE)
    # Domain/planning docs are canonical assets too; rewrite their instruction paths.
    for directory in (assets / "artifacts", assets / "domains", assets / "venues"):
        for path in directory.rglob("*.md"):
            path.write_text(render_instruction(path.read_text(encoding="utf-8")), encoding="utf-8")
    for script in RUNTIME_SCRIPTS:
        copy_file(ROOT / "scripts" / script, target / "scripts" / script)
    copy_file(ROOT / "VERSION", target / "VERSION")
    (target / "generated-sources.json").write_text(json.dumps({
        "notice": "Generated package. Edit canonical repository sources, then rebuild.",
        "venues": venues, "domains": ["power-electronics"] if include_domain else [],
        "instructions": provenance,
    }, indent=2) + "\n", encoding="utf-8")
    (target / "PACKAGE.md").write_text(
        "# Generated IEEE Paper Agent Skill\n\n"
        "Start with SKILL.md. All instruction paths are relative to this directory.\n"
        "Use the absolute path of scripts/create-manuscript.py when running elsewhere;\n"
        "--root chooses output while bundled assets are found relative to the script.\n\n"
        f"Included venues: {', '.join(venues)}.\n"
        f"Power-electronics domain/reference collection included: {include_domain}.\n"
        "References to an omitted domain or venue apply only if that asset is installed.\n"
        "Instruction copies are generated; provenance is recorded in generated-sources.json.\n",
        encoding="utf-8")


def plugin_manifest(config: dict, version: str) -> dict:
    return {
        "name": config["plugin_name"], "version": version,
        "description": config["description"],
        "author": {"name": config["developer_name"]},
        "license": config.get("license", "MIT"),
        "keywords": config.get("keywords", []),
        "skills": "./skills/",
        "interface": {
            "displayName": config["display_name"],
            "shortDescription": config["description"],
            "longDescription": "IEEE paper production with canonical workflows, real venue templates, optional domain knowledge, and citation validation.",
            "developerName": config["developer_name"],
            "category": config.get("category", "Productivity"),
            "capabilities": ["Write", "Research", "Review"],
            "defaultPrompt": list(config.get("default_prompts", []))[:3],
        },
    }


def build_release(dist: Path, venues: list[str] | None = None, include_domain: bool = True) -> list[Path]:
    config = json.loads((ROOT / "release-config.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    venues = sorted(set(venues if venues is not None else list_venues(ROOT)))
    for venue in venues:
        load_profile(venue, ROOT)
    if not venues:
        raise ValueError("at least one venue is required")
    dist = filesystem_path(dist)
    dist.mkdir(parents=True, exist_ok=True)
    if include_domain:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-reference-index.py")],
                       cwd=ROOT, check=True)
    skill_name, plugin_name = config["skill_name"], config["plugin_name"]
    # Config values become directory names, never arbitrary paths.
    for name in (skill_name, plugin_name, version):
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", name):
            raise ValueError(f"invalid release name/version: {name}")
    codex = dist / "codex-skill" / skill_name
    build_skill(codex, dist, venues, include_domain)
    marketplace = dist / "codex-plugin-marketplace"
    clean_generated(marketplace, dist)
    plugin = marketplace / "plugins" / plugin_name
    # Assets and tools live inside the actual skill, including in plugin packages.
    shutil.copytree(codex, plugin / "skills" / skill_name)
    manifest = plugin / ".codex-plugin" / "plugin.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text(json.dumps(plugin_manifest(config, version), indent=2) + "\n", encoding="utf-8")
    (marketplace / "marketplace.json").write_text(json.dumps({
        "name": "aipe-local", "interface": {"displayName": "AIPE Local"},
        "plugins": [{
            "name": plugin_name,
            "source": {"source": "local", "path": f"./plugins/{plugin_name}"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": config.get("category", "Productivity"),
        }],
    }, indent=2) + "\n", encoding="utf-8")
    claude = dist / "claude-skill" / plugin_name
    clean_generated(claude, dist)
    shutil.copytree(codex, claude)
    archives = [
        dist / f"{skill_name}-codex-skill-v{version}.zip",
        dist / f"{plugin_name}-codex-plugin-marketplace-v{version}.zip",
        dist / f"{plugin_name}-claude-skill-v{version}.zip",
    ]
    for source, archive in zip((codex, marketplace, claude), archives):
        zip_dir(source, archive)
    (dist / "RELEASE.md").write_text(
        f"# AIPE IEEE Paper Agent {version}\n\nGenerated from canonical core sources.\n\n"
        + "\n".join(f"- {path.name}" for path in archives)
        + f"\n\nVenues: {', '.join(venues)}.\nPower-electronics domain: {include_domain}.\n"
        "Generated instruction provenance is included in each skill.\n"
        "Regenerate with python scripts/package-release.py.\n", encoding="utf-8")
    return archives


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=DIST, help="release output directory")
    parser.add_argument("--venue", action="append", help="include only this venue; repeatable")
    parser.add_argument("--without-domain", action="store_true", help="omit power-electronics assets and reference library")
    parser.add_argument("--no-clean", action="store_true", help="accepted for compatibility; only named generated package trees are replaced")
    args = parser.parse_args()
    try:
        for path in build_release(args.dist, args.venue, not args.without_domain):
            print(path)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
