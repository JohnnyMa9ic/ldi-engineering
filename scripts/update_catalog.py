#!/usr/bin/env python3
"""
Rebuild catalog.json by scanning all document directories for frontmatter.

Usage: python3 scripts/update_catalog.py
Run from the repo root.
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent

TYPE_DIRS = {
    "es": "engineering-standard",
    "adr": "architectural-decision-record",
    "ds": "design-specification",
    "om": "operations-manual",
    "ir": "incident-report",
    "mb": "maintenance-bulletin",
    "rp": "research-paper",
}


def parse_frontmatter(path: Path) -> dict | None:
    """Parse YAML frontmatter from a markdown file.

    Returns the frontmatter as a dict, or None if no frontmatter found.
    """
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None

    raw = match.group(1)
    result: dict = {}

    for line in raw.splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("-"):
            continue
        key, _, val = line.partition(":")
        v = val.strip()
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1]
        result[key.strip()] = v

    # Collect list fields (references, referenced_by, tags)
    for list_field in ("references", "referenced_by", "tags"):
        items = []
        in_block = False
        for line in raw.splitlines():
            if line.strip() == f"{list_field}:":
                in_block = True
                continue
            if in_block:
                stripped = line.strip()
                if stripped.startswith("- "):
                    items.append(stripped[2:].strip())
                elif stripped and not stripped.startswith("-"):
                    break
        result[list_field] = items

    # Normalize null/empty
    for k, v in result.items():
        if v in ("null", "~", ""):
            result[k] = None

    return result


def build_catalog() -> dict:
    """Scan all document directories and build the catalog structure."""
    documents = []

    for dir_prefix, doc_type in TYPE_DIRS.items():
        doc_dir = REPO_ROOT / dir_prefix
        if not doc_dir.exists():
            continue

        for md_file in sorted(doc_dir.glob("*.md")):
            fm = parse_frontmatter(md_file)
            if not fm:
                print(f"  SKIP (no frontmatter): {md_file.name}")
                continue

            doc_id = fm.get("id")
            if not doc_id:
                print(f"  SKIP (no id): {md_file.name}")
                continue

            documents.append(
                {
                    "id": doc_id,
                    "type": doc_type,
                    "title": fm.get("title", ""),
                    "status": fm.get("status", "draft"),
                    "severity": fm.get("severity"),
                    "created": fm.get("created", ""),
                    "updated": fm.get("updated", ""),
                    "author": fm.get("author", ""),
                    "path": f"{dir_prefix}/{md_file.name}",
                    "references": fm.get("references", []),
                    "referenced_by": fm.get("referenced_by", []),
                    "tags": fm.get("tags", []),
                    "summary": fm.get("summary", ""),
                }
            )
            print(f"  OK: {doc_id} — {fm.get('title', '')}")

    # Build reference graph
    reference_graph = {}
    all_ids = {d["id"] for d in documents}

    for doc in documents:
        doc_id = doc["id"]
        refs = [r for r in doc.get("references", []) if r in all_ids]
        reference_graph[doc_id] = {"references": refs, "referenced_by": []}

    for doc_id, entry in reference_graph.items():
        for ref_id in entry["references"]:
            if ref_id in reference_graph:
                reference_graph[ref_id]["referenced_by"].append(doc_id)

    # Rewrite referenced_by in documents to match computed graph
    for doc in documents:
        doc["referenced_by"] = reference_graph.get(doc["id"], {}).get("referenced_by", [])

    # Counts
    status_counts: dict[str, int] = {"active": 0, "draft": 0, "deprecated": 0, "superseded": 0}
    type_counts: dict[str, int] = {v: 0 for v in TYPE_DIRS.values()}

    for doc in documents:
        s = doc.get("status", "draft")
        if s in status_counts:
            status_counts[s] += 1
        t = doc.get("type", "")
        if t in type_counts:
            type_counts[t] += 1

    return {
        "version": "1.0",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "total": len(documents),
            "by_type": type_counts,
            "by_status": status_counts,
        },
        "documents": documents,
        "reference_graph": reference_graph,
    }


def main() -> None:
    """Rebuild catalog.json from frontmatter in all document directories."""
    print("Scanning document directories...")
    catalog = build_catalog()

    out_path = REPO_ROOT / "catalog.json"
    out_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")

    total = catalog["counts"]["total"]
    print(f"\nOutput written to: {out_path}")
    print(f"Total documents indexed: {total}")


if __name__ == "__main__":
    main()
