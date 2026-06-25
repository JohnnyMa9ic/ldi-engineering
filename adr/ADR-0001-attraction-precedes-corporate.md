---
id: ADR-0001
type: architectural-decision-record
title: "The Attraction Precedes the Corporate Layer"
status: active
severity: null
created: 2026-06-25
updated: 2026-06-25
author: john
references: []
referenced_by:
  - ES-0001
  - DS-0001
tags:
  - information-architecture
  - brand-strategy
  - routing
  - ldi-identity
summary: "The public entry point for lithium-dreams.com is the roadside attraction, not the consulting services section. This records why."
---

# ADR-0001 — The Attraction Precedes the Corporate Layer

## Context

Lithium Dreams Industries has two distinct faces:

1. **The Attraction** — A strange, hand-built roadside experience. Arcade cabinets, a fortune machine, a mystery museum, Ghost's Workshop. Industrial folklore. The creative laboratory and lore universe.

2. **The Corporate Layer** — A consulting and operational systems design practice. Client intake, case files, technical advisory. Professional and direct.

Both are real. Both are LDI. The question was which face greets the visitor first.

## Options Considered

**Option A: Corporate-first.** `/` routes to the consulting homepage. The attraction lives at `/attraction` or `/lab`. Maximizes immediate business legibility.

**Option B: Attraction-first.** `/` routes to the roadside attraction experience. The corporate layer lives at `/work`. Curiosity is the entry drug.

**Option C: Toggle on arrival.** Landing page asks "Are you here for the attraction or the work?" Two explicit paths from the start.

## Decision

**Option B — Attraction-first.**

`/` is The Last Roadside Attraction. `/work` is the consulting layer. The nav badge on the attraction layout links to `/work`. The work layout links back with `← The Attraction`.

## Reasoning

The attraction is not a creative hobby that funds the consulting work. The consulting work is one expression of the same creative intelligence that built the attraction. They are the same thing. Presenting the consulting layer first would misrepresent what LDI actually is.

Visitors who arrive for consulting and encounter the attraction first will either understand immediately or ask about it — both outcomes are better than a visitor who sees only the consulting surface and never discovers that it sits inside something stranger and more interesting.

The attraction also functions as a filter. Clients who are confused or put off by it are not the clients LDI is optimizing for.

## Consequences

- The attraction must be genuinely good — it is the first impression for everyone, including prospective clients
- Navigation between the two surfaces must be frictionless and clearly signposted
- The two visual grammars (attraction and corporate) must be distinct but must share a recognizable material foundation — see ES-0001
- SEO for consulting services will depend on `/work` being well-structured, since `/` is not a conventional consulting homepage
- The `LDI` badge in the attraction nav links to `/work` — this is the primary crossing point

## Status Note

Decided at site founding. No known challenges to this decision as of 2026-06-25.
