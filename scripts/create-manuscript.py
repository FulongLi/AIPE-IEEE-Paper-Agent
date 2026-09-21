#!/usr/bin/env python3
"""Initialize a manuscript from the actual template of an IEEE venue."""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

from venue_profiles import asset_root, list_venues, load_profile, relative_path, strip_comments

SECTIONS = [
    ("00-abstract", None),
    ("01-introduction", "Introduction"),
    ("02-related-work", "Related Work"),
    ("03-method", "Method"),
    ("04-experiments", "Experimental Setup"),
    ("05-results-discussion", "Results and Discussion"),
    ("06-conclusion", "Conclusion"),
]
SECTION_FILES = [name + ".tex" for name, _ in SECTIONS]
DIRECTORIES = ("sections", "figures", "tables", "refs", "styles", "notes", "build")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise ValueError("manuscript slug cannot be empty")
    return slug


def latex_escape(value: str) -> str:
    escapes = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
               "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
               "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(escapes.get(char, char) for char in value)


def replace_arguments(text: str, command: str, replacement: str, count: int = 1) -> str:
    """Replace balanced arguments, preserving the command and optional argument."""
    pattern = re.compile(r"\\" + re.escape(command) + r"\b\s*(?:\[[^\]]*\]\s*)?\{")
    position = 0
    while True:
        match = pattern.search(text, position)
        if not match:
            return text
        opening = match.end() - 1
        for number in range(count):
            if text[opening] != "{":
                raise ValueError(f"missing argument to {command}")
            depth, end = 1, opening + 1
            while end < len(text) and depth:
                if text[end] == "\\":
                    end += 2
                    continue
                if text[end] == "{":
                    depth += 1
                if text[end] == "}":
                    depth -= 1
                end += 1
            if depth:
                raise ValueError(f"unbalanced argument to {command}")
            text = text[:opening + 1] + replacement + text[end - 1:]
            position = opening + len(replacement) + 2
            if number < count - 1:
                opening = position
                while opening < len(text) and text[opening].isspace():
                    opening += 1


def replace_environment(text: str, environment: str, content: str) -> str:
    pattern = re.compile(r"(\\begin\{" + re.escape(environment) + r"\}).*?(\\end\{" + re.escape(environment) + r"\})", re.S)
    text, count = pattern.subn(lambda m: m[1] + "\n" + content + "\n" + m[2], text)
    if count != 1:
        raise ValueError(f"expected one {environment} environment")
    return text


def normalize_entry(source: str, profile: dict, title: str) -> str:
    # The template supplies the entire preamble and front-matter ordering.
    active = strip_comments(source)
    front, _ = active.split(profile["normalization"]["body_start"], 1)
    title_text = latex_escape(title)
    if profile["family"] == "conference" and r"\thanks{" in front.split(r"\author{", 1)[0]:
        title_text += r"\thanks{TODO: Funding information}"
    front = replace_arguments(front, "title", title_text)
    for command in ("thanks", "address", "affil", "corresp", "tfootnote", "authornote",
                    "history", "doi", "doiinfo", "receiveddate", "reviseddate", "accepteddate",
                    "publisheddate", "currentdate", "editor", "sptitle", "IEEEpubid"):
        front = replace_arguments(front, command, "TODO: " + command)
    front = replace_arguments(front, "markboth", "TODO: running header", count=2)
    for command, value in (("jvol", "00"), ("jnum", "00"), ("paper", "0000000"), ("pubyear", "0000")):
        front = replace_arguments(front, command, value)
    front = replace_arguments(front, "IEEEauthorblockN", "TODO: Author")
    front = replace_arguments(front, "IEEEauthorblockA", r"TODO: Affiliation\\ TODO: Email")
    front = replace_arguments(front, "IEEEmembership", "TODO: Membership")
    # Preserve author macros, reference marks and the affiliation structure.
    for sample in ("IEEE Publication Technology", "First A. Author", "Second B. Author",
                   "Third C. Author", "F. A. AUTHOR", "B. AUTHOR", r"C.~AUTHOR"):
        front = front.replace(sample, "TODO: Author")
    front = re.sub(r"FIRST A\. AUTHOR|SECOND B\.\s*AUTHOR|THIRD C\. AUTHOR", "TODO: Author", front)
    front = front.replace("FELLOW, IEEE", "TODO: Membership").replace("MEMBER, IEEE", "TODO: Membership")
    front = front.replace("(Student Member, IEEE)", "(TODO: Membership)").replace("(Member, IEEE)", "(TODO: Membership)")
    front = replace_environment(front, "abstract", r"\input{sections/00-abstract}")
    front = replace_environment(front, profile["normalization"]["keywords_environment"], "TODO: Keywords")
    for environment in profile["normalization"]["placeholder_environments"]:
        front = replace_environment(front, environment, "TODO: Write from verified evidence.")
    inputs = "\n".join(r"\input{sections/" + name + "}" for name, _ in SECTIONS[1:])
    bibliography = (r"\bibliographystyle{" + profile["bibliography"]["style"] + "}\n"
                    r"\bibliography{refs/references}" + "\n")
    ending = "\n".join(profile["normalization"]["end_commands"] + [r"\end{document}"])
    return ("% Initialized from the selected venue template. Replace all TODO metadata.\n"
            + front.rstrip() + "\n\n" + inputs + "\n\n" + bibliography + "\n" + ending + "\n")


def create_workspace(root: Path, slug: str, title: str, venue: str = "ieee-conference",
                     domain: str | None = None, assets: Path | None = None) -> Path:
    assets = assets or asset_root()
    profile = load_profile(venue, assets)
    template = relative_path(assets, profile["template"]["path"])
    entry = relative_path(template, profile["template"]["entry"])
    main = normalize_entry(entry.read_text(encoding=profile["template"].get("encoding", "utf-8")), profile, title)
    domain_readme = None
    if domain:
        domain_readme = relative_path(assets, f"domains/{domain}/README.md")
        if not domain_readme.is_file():
            raise ValueError(f"domain pack not available: {domain}")
    workspace = root.resolve() / "manuscripts" / slugify(slug)
    # Validate configuration and source before creating any output.
    workspace.mkdir(parents=True, exist_ok=False)
    for dirname in DIRECTORIES:
        (workspace / dirname).mkdir()
    # Preserve support-file locations: Access maps and OJPEL logos must resolve
    # without absolute paths, TEXINPUTS, or changes to official files.
    for path in template.rglob("*"):
        if not path.is_file() or path.suffix.lower() == ".tex" or path.name.endswith((".synctex.gz", ".DS_Store")):
            continue
        target = workspace / path.relative_to(template)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    for name, heading in SECTIONS:
        text = (r"\section{" + heading + "}\n") if heading else ""
        text += "% TODO: Draft from verified evidence; track gaps in notes/evidence-checklist.md.\n"
        text += "TODO: Author evidence required.\n"
        (workspace / "sections" / (name + ".tex")).write_text(text, encoding="utf-8")
    for path in (assets / "artifacts").glob("*.md"):
        shutil.copy2(path, workspace / "notes" / path.name)
    (workspace / "refs" / "references.bib").write_text("% Add only verified, relevant BibTeX entries.\n", encoding="utf-8")
    (workspace / "notes" / "evidence-checklist.md").write_text(
        "# Evidence Checklist\n\nClassify gaps as blocking, important, or optional.\n\n"
        "- [ ] blocking: connect each research question and contribution to real evidence in evidence-matrix.md.\n", encoding="utf-8")
    (workspace / "notes" / "latex-todo.md").write_text(
        "# LaTeX TODO\n\n- [ ] Replace TODO authors, affiliations, funding, dates, DOI, and running headers with verified metadata.\n"
        "- [ ] Confirm current venue limits and anonymity requirements.\n"
        "- [ ] Add biographies/acknowledgments if required; consult the original venue template.\n"
        "- [ ] Add verified references, compile main.tex, and inspect the PDF.\n"
        "- [ ] Remove unused sample assets before submission.\n", encoding="utf-8")
    (workspace / "styles" / "README.md").write_text(
        "Official class, style, font and logo files retain their original paths at the workspace root.\n"
        "This folder is available for author-owned support files.\n", encoding="utf-8")
    if domain_readme:
        (workspace / "notes" / "domain.md").write_text(
            f"# Optional Domain: {domain}\n\nLoad domains/{domain}/README.md from the agent asset root.\n"
            "No domain text or reference entries are inserted automatically.\n", encoding="utf-8")
    (workspace / "notes" / "venue-profile.json").write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    (workspace / "main.tex").write_text(main, encoding="utf-8")
    return workspace


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", nargs="?", help="short manuscript slug")
    parser.add_argument("--root", default=".", help="output root; assets are located relative to the script")
    parser.add_argument("--title", default="TODO: Working Title", help="plain-text manuscript title")
    parser.add_argument("--venue", default="ieee-conference", help="venue id; default: ieee-conference")
    parser.add_argument("--domain", help="optional domain pack, for example power-electronics")
    parser.add_argument("--list-venues", action="store_true")
    parser.add_argument("--template", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.template:
        parser.error("--template was replaced by --venue; use --list-venues to choose a real venue template")
    if args.list_venues:
        print("\n".join(list_venues()))
        return 0
    if not args.slug:
        parser.error("a manuscript slug is required")
    try:
        print(create_workspace(Path(args.root), args.slug, args.title, args.venue, args.domain))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
