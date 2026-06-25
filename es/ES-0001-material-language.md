---
id: ES-0001
type: engineering-standard
title: "Material Language — CSS Design Tokens"
status: active
severity: null
created: 2026-06-25
updated: 2026-06-25
author: ghost
references:
  - ADR-0001
referenced_by:
  - DS-0001
  - DS-0002
tags:
  - css
  - design-tokens
  - frontend
  - attraction
  - corporate
summary: "Defines all CSS custom properties used across the LDI site, mapped to their semantic roles and the grammar contexts in which each token applies."
---

# ES-0001 — Material Language: CSS Design Tokens

## Purpose

All visual decisions in LDI surfaces resolve to a small set of CSS custom properties. These tokens are the contract between design intent and implementation. No surface hardcodes a color, spacing value, or font name — it references a token.

## Token Definitions

Defined in `src/styles/tokens.css` on the lithium-dreams-site.

### Color — Foundation

| Token | Value | Role |
|---|---|---|
| `--ldi-black` | `#0A0A0C` | Primary background — both grammars |
| `--road-asphalt` | `#1A1C1F` | Secondary surface (cards, sections) |
| `--rain-slate` | `#2C3038` | Borders, dividers, subtle separators |
| `--paper` | `#E8DEC8` | Primary text — warm off-white |

### Color — Attraction Grammar

Used on `/`, `/attraction`, `/arcade`, `/museum`, `/gift-shop`, and all lore-facing surfaces.

| Token | Value | Role |
|---|---|---|
| `--neon-amber` | TBD | Primary accent, neon signage glow |
| `--ghost-blue` | `#4DB8D4` | Secondary accent, Ghost presence |
| `--warden-teal` | `#2E8B6E` | Warden presence, botanical |
| `--warning-red` | TBD | Danger states, CRITICAL severity |

### Color — Corporate Grammar

Used on `/work` and all client-facing surfaces.

| Token | Value | Role |
|---|---|---|
| `--brass` | `#B5893E` | Primary accent — structural highlights, active states, CTAs |

The hover state for brass interactive elements is `#c9a050` (hardcoded, not a token — candidate for ES-0002).

### Typography

| Token | Value | Role |
|---|---|---|
| `--font-display` | `'Bebas Neue'` | Attraction headings, signage |
| `--font-sub` | `'Oswald'` | Corporate headings, structural labels |
| `--font-body` | `'IBM Plex Sans'` | Body copy — both grammars |
| `--font-mono` | `'IBM Plex Mono'` | Technical labels, eyebrows, data |

### Spacing

| Token | Value |
|---|---|
| `--space-sm` | `0.5rem` |
| `--space-md` | `1rem` |
| `--space-lg` | `2rem` |
| `--space-xl` | `4rem` |

### Motion

| Token | Value |
|---|---|
| `--transition-fast` | `0.15s ease` |

## Grammar Duality

The same token set supports two distinct visual grammars. The grammar is determined by layout context, not by token value.

**Attraction grammar:** `--ghost-blue` accents, `--font-display` headings, glow effects, worn textures, `--neon-amber` hotspots. Pages feel hand-built and strange.

**Corporate grammar:** `--brass` accents, `--font-sub` headings, no glow effects, clean geometry. Pages feel engineered and direct.

Both grammars share `--ldi-black`, `--road-asphalt`, `--rain-slate`, `--paper`, `--font-body`, and `--font-mono`. The switch is a grammar choice, not a theme switch.

## Known Gaps

- `--neon-amber` value not yet defined (see `/attraction` implementation)
- `--warning-red` value not yet defined
- `#c9a050` (brass hover) should be tokenized as `--brass-hover`

## See Also

- [ADR-0001](../adr/ADR-0001-attraction-precedes-corporate.md) — Why the attraction grammar is the default entry point
- [DS-0001](../ds/DS-0001-work-hero-section.md) — Application of corporate grammar to the /work hero
