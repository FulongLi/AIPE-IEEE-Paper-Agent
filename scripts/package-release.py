#!/usr/bin/env python3
"""Package Codex and Claude release artifacts for the IEEE Paper Agent."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_config() -> dict[str, object]:
    return json.loads((ROOT / "release-config.json").read_text(encoding="utf-8"))


def copy_tree(src: Path, dst: Path, ignore: shutil.IgnorePattern | None = None) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=ignore)


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def zip_dir(src_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(src_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(src_dir.parent))


def rebuild_reference_index() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build-reference-index.py")],
        cwd=ROOT,
        check=True,
    )


def copy_common_assets(target: Path) -> None:
    assets = target / "assets"
    copy_tree(ROOT / "PE_ref", assets / "PE_ref")
    copy_tree(ROOT / "templates", assets / "templates")
    copy_tree(ROOT / "workflows", assets / "workflows")
    copy_tree(ROOT / "knowledge-base", assets / "knowledge-base")
    copy_tree(ROOT / "IEEE paper Template", assets / "IEEE paper Template")
    copy_file(ROOT / "README.md", assets / "README.md")
    copy_file(ROOT / "AGENTS.md", assets / "AGENTS.md")
    copy_file(ROOT / "INSTALL.md", assets / "INSTALL.md")


def copy_release_scripts(target: Path) -> None:
    scripts = target / "scripts"
    scripts.mkdir(parents=True, exist_ok=True)
    for name in ["build-reference-index.py", "check-citations.py", "create-manuscript.py"]:
        copy_file(ROOT / "scripts" / name, scripts / name)


def build_codex_skill(config: dict[str, object], version: str) -> Path:
    skill_name = str(config["skill_name"])
    package_root = DIST / "codex-skill" / skill_name
    copy_tree(ROOT / "skills" / skill_name, package_root)
    copy_common_assets(package_root)
    copy_release_scripts(package_root)
    copy_file(ROOT / "VERSION", package_root / "VERSION")
    zip_dir(package_root, DIST / f"{skill_name}-codex-skill-v{version}.zip")
    return package_root


def plugin_manifest(config: dict[str, object], version: str) -> dict[str, object]:
    prompts = list(config.get("default_prompts", []))[:3]
    return {
        "name": config["plugin_name"],
        "version": version,
        "description": config["description"],
        "author": {"name": config["developer_name"]},
        "license": config.get("license", "MIT"),
        "keywords": config.get("keywords", []),
        "skills": "./skills/",
        "interface": {
            "displayName": config["display_name"],
            "shortDescription": config["description"],
            "longDescription": (
                "A reusable IEEE paper production assistant with LaTeX manuscript "
                "workspace setup, power electronics knowledge assets, reference indexing, "
                "citation verification, and publication-readiness workflows."
            ),
            "developerName": config["developer_name"],
            "category": config.get("category", "Productivity"),
            "capabilities": ["Write", "Research", "Review"],
            "defaultPrompt": prompts,
        },
    }


def build_codex_plugin_marketplace(config: dict[str, object], version: str) -> Path:
    plugin_name = str(config["plugin_name"])
    skill_name = str(config["skill_name"])
    marketplace_root = DIST / "codex-plugin-marketplace"
    plugin_root = marketplace_root / "plugins" / plugin_name
    if marketplace_root.exists():
        shutil.rmtree(marketplace_root)

    copy_tree(ROOT / "skills" / skill_name, plugin_root / "skills" / skill_name)
    copy_common_assets(plugin_root)
    copy_release_scripts(plugin_root)
    copy_file(ROOT / "VERSION", plugin_root / "VERSION")

    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(plugin_manifest(config, version), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    marketplace = {
        "name": "aipe-local",
        "interface": {"displayName": "AIPE Local"},
        "plugins": [
            {
                "name": plugin_name,
                "source": {"source": "local", "path": f"./plugins/{plugin_name}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": config.get("category", "Productivity"),
            }
        ],
    }
    (marketplace_root / "marketplace.json").write_text(
        json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    zip_dir(marketplace_root, DIST / f"{plugin_name}-codex-plugin-marketplace-v{version}.zip")
    return marketplace_root


def build_claude_skill(config: dict[str, object], version: str) -> Path:
    plugin_name = str(config["plugin_name"])
    skill_name = str(config["skill_name"])
    package_root = DIST / "claude-skill" / plugin_name
    if package_root.exists():
        shutil.rmtree(package_root)
    package_root.mkdir(parents=True)

    copy_file(ROOT / "skills" / skill_name / "SKILL.md", package_root / "SKILL.md")
    copy_tree(ROOT / "skills" / skill_name / "references", package_root / "references")
    if (ROOT / "skills" / skill_name / "agents").exists():
        copy_tree(ROOT / "skills" / skill_name / "agents", package_root / "agents")
    copy_common_assets(package_root)
    copy_release_scripts(package_root)
    copy_file(ROOT / "VERSION", package_root / "VERSION")

    zip_dir(package_root, DIST / f"{plugin_name}-claude-skill-v{version}.zip")
    return package_root


def write_release_notes(config: dict[str, object], version: str) -> None:
    notes = f"""# AIPE IEEE Paper Agent Release {version}

Generated artifacts:

- `{config["skill_name"]}-codex-skill-v{version}.zip`: self-contained Codex skill package.
- `{config["plugin_name"]}-codex-plugin-marketplace-v{version}.zip`: local Codex plugin marketplace package.
- `{config["plugin_name"]}-claude-skill-v{version}.zip`: Claude-compatible skill package.

Regenerate with:

```bash
python scripts/package-release.py
```

The script rebuilds `PE_ref/references-index.json` before packaging.
"""
    (DIST / "RELEASE.md").write_text(notes, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-clean", action="store_true", help="do not delete dist before packaging")
    args = parser.parse_args()

    config = load_config()
    version = read_text(ROOT / "VERSION")

    if not args.no_clean and DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    rebuild_reference_index()
    codex_skill = build_codex_skill(config, version)
    codex_plugin = build_codex_plugin_marketplace(config, version)
    claude_skill = build_claude_skill(config, version)
    write_release_notes(config, version)

    print(f"version: {version}")
    print(f"codex skill: {codex_skill}")
    print(f"codex plugin marketplace: {codex_plugin}")
    print(f"claude skill: {claude_skill}")
    print(f"release notes: {DIST / 'RELEASE.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
