# LDI Engineering Repository

Lithium Dreams Industries — living knowledge graph for engineering decisions, design specifications, operational standards, and incident history.

## What this is

Not a static document collection. A traversable graph. Every document carries a stable ID and a `references` list pointing to other document IDs. AI agents and engineers navigate it the way a circuit follows traces — by reference, not by search.

## Document Types

| Prefix | Type | Purpose |
|---|---|---|
| ES | Engineering Standard | Reusable patterns and material rules (tokens, naming, conventions) |
| ADR | Architectural Decision Record | Why a structural choice was made, at the time it was made |
| DS | Design Specification | What a specific feature or surface should look like and how it behaves |
| OM | Operations Manual | How a recurring process runs (pipeline steps, agent behavior) |
| IR | Incident Report | What broke, why, and what changed as a result |
| MB | Maintenance Bulletin | Service notes for a specific system, component, or prop |
| RP | Research Paper | Exploratory findings, benchmarks, option surveys |

## Severity Scale (IR and MB only)

`NOTICE` → `CAUTION` → `WARNING` → `CRITICAL` → `CATHEDRAL_EVENT`

Cathedral Event: system-level failure that forces architectural reconsideration. Named for the event that created the Cathedral of Glitch.

## ID Format

`TYPE-NNNN` where NNNN is a zero-padded four-digit integer, assigned sequentially within each type. IDs are permanent and never reused. A deprecated document retains its ID and gains a `superseded_by` pointer.

## Frontmatter Schema

Every document begins with YAML frontmatter:

```yaml
---
id: ES-0001
type: engineering-standard
title: "Material Language — CSS Design Tokens"
status: active          # draft | active | deprecated | superseded
severity: null          # IR/MB only: NOTICE | CAUTION | WARNING | CRITICAL | CATHEDRAL_EVENT
created: 2026-06-25
updated: 2026-06-25
author: ghost           # ghost | bob | warden | john | claude
references:             # IDs of documents this document cites
  - ADR-0001
referenced_by: []       # populated by update_catalog.py — do not edit manually
tags:
  - css
  - design-tokens
summary: "Defines all CSS custom properties used across the LDI site, mapped to their semantic roles."
---
```

## Catalog

`catalog.json` is the machine-readable index. Run `python3 scripts/update_catalog.py` to rebuild it from current frontmatter. AI agents should read the catalog first, then follow reference IDs to specific documents.

## Bob's Dream Crown Pipeline

Ideas enter the engineering repository through the Dream Crown process:

1. **Reflection** — Bob generates an idea or observation during a dreaming cycle
2. **Classification** — Bob tags it with type (ES / ADR / DS / OM / IR / MB / RP) and severity
3. **Ghost review** — Ghost validates technical accuracy and scope
4. **Warden review** — Warden checks alignment with long-term system health
5. **Human approval** — John approves or redirects
6. **GitHub issue** — Approved idea becomes a GitHub issue with ID pre-assigned
7. **Engineering document** — Claude Code writes the document into the appropriate type directory
8. **Catalog update** — `update_catalog.py` runs, cross-references are wired

Documents written outside this pipeline (e.g. during active implementation sessions) should be added retroactively with the same frontmatter structure.

## For AI Agents

To understand the current state of any LDI system:
1. Read `catalog.json` — get the full document list and reference graph
2. Filter by `type` and `status: active`
3. Follow `references` arrays to traverse related decisions
4. Read the full `.md` files only for documents relevant to the current task

Do not rely on keyword search alone. The reference graph is the navigation layer.
