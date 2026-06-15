#!/usr/bin/env python3
"""Build a JSON index from repository BibTeX reference files."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


FIELD_RE = re.compile(r"(\w+)\s*=\s*([{\"])")
AUTHOR_SPLIT_RE = re.compile(r"\s+and\s+", re.IGNORECASE)


def strip_wrapping(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if len(value) >= 2 and ((value[0] == "{" and value[-1] == "}") or (value[0] == '"' and value[-1] == '"')):
        value = value[1:-1]
    return re.sub(r"\s+", " ", value).strip()


def find_matching_brace(text: str, start: int) -> int:
    depth = 0
    in_quote = False
    escape = False
    for index in range(start, len(text)):
        char = text[index]
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_quote = not in_quote
            continue
        if in_quote:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return -1


def iter_entries(text: str) -> Iterable[dict[str, str]]:
    index = 0
    while True:
        match = re.search(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text[index:], re.MULTILINE)
        if not match:
            break
        entry_type = match.group(1)
        key = match.group(2)
        absolute_start = index + match.start()
        body_start = index + match.end()
        brace_start = text.find("{", absolute_start)
        body_end = find_matching_brace(text, brace_start)
        if body_end == -1:
            break
        body = text[body_start:body_end]
        fields = parse_fields(body)
        fields["entry_type"] = entry_type.lower()
        fields["key"] = key
        yield fields
        index = body_end + 1


def parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    position = 0
    while True:
        match = FIELD_RE.search(body, position)
        if not match:
            break
        name = match.group(1).lower()
        delimiter = match.group(2)
        value_start = match.end() - 1
        if delimiter == "{":
            value_end = find_matching_brace(body, value_start)
            if value_end == -1:
                break
            raw_value = body[value_start : value_end + 1]
            position = value_end + 1
        else:
            value_end = value_start + 1
            while value_end < len(body):
                if body[value_end] == '"' and body[value_end - 1] != "\\":
                    break
                value_end += 1
            raw_value = body[value_start : value_end + 1]
            position = value_end + 1
        fields[name] = strip_wrapping(raw_value)
    return fields


def infer_topic(path: Path) -> str:
    name = path.stem
    replacements = {
        "_reference": "",
        "AIPE_added_refs": "ai paper agents",
        "kolar_guillod_converter_optimization": "converter optimization",
    }
    topic = replacements.get(name, name.replace("_reference", ""))
    return topic.replace("_", " ").replace("-", " ").strip()


def split_authors(author_field: str) -> list[str]:
    if not author_field:
        return []
    return [author.strip() for author in AUTHOR_SPLIT_RE.split(author_field) if author.strip()]


def venue_for(entry: dict[str, str]) -> str:
    for field in ["journal", "booktitle", "publisher", "institution", "organization", "school"]:
        if entry.get(field):
            return entry[field]
    return ""


def verification_status(entry: dict[str, str]) -> str:
    if entry.get("doi"):
        return "doi-present"
    if entry.get("url"):
        return "url-present"
    if "arxiv" in (entry.get("journal", "") + " " + entry.get("eprint", "")).lower():
        return "arxiv-mentioned"
    return "needs-verification"


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve())).replace("\\", "/")
    except ValueError:
        return str(path)


def build_index(ref_dir: Path) -> dict[str, object]:
    records: list[dict[str, object]] = []
    seen_keys: dict[str, list[str]] = {}
    for bib_path in sorted(ref_dir.glob("*.bib")):
        text = bib_path.read_text(encoding="utf-8", errors="ignore")
        for entry in iter_entries(text):
            key = entry["key"]
            source_file = bib_path.name
            seen_keys.setdefault(key, []).append(source_file)
            records.append(
                {
                    "key": key,
                    "entry_type": entry.get("entry_type", ""),
                    "title": entry.get("title", ""),
                    "authors": split_authors(entry.get("author", "")),
                    "year": entry.get("year", ""),
                    "venue": venue_for(entry),
                    "doi": entry.get("doi", ""),
                    "url": entry.get("url", ""),
                    "keywords": entry.get("keywords", ""),
                    "topic": infer_topic(bib_path),
                    "source_file": source_file,
                    "verification_status": verification_status(entry),
                }
            )

    duplicate_keys = {key: files for key, files in seen_keys.items() if len(files) > 1}
    status_counts: dict[str, int] = {}
    for record in records:
        status = str(record["verification_status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_directory": display_path(ref_dir),
        "record_count": len(records),
        "duplicate_key_count": len(duplicate_keys),
        "verification_status_counts": dict(sorted(status_counts.items())),
        "duplicate_keys": duplicate_keys,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref-dir", default="PE_IEEE_reference", help="directory containing .bib files")
    parser.add_argument("--output", default="PE_IEEE_reference/references-index.json", help="output JSON path")
    args = parser.parse_args()

    ref_dir = Path(args.ref_dir).resolve()
    output = Path(args.output).resolve()
    if not ref_dir.is_dir():
        raise SystemExit(f"reference directory not found: {ref_dir}")

    index = build_index(ref_dir)
    output.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    print(f"records: {index['record_count']}")
    print(f"duplicate keys: {index['duplicate_key_count']}")
    print(f"verification status: {index['verification_status_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
