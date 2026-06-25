---
id: DS-0001
type: design-specification
title: "/work Hero Section"
status: active
severity: null
created: 2026-06-25
updated: 2026-06-25
author: ghost
references:
  - ES-0001
  - ADR-0001
referenced_by: []
tags:
  - frontend
  - corporate-grammar
  - hero
  - work-section
summary: "Full-bleed background image hero for the /work landing page. Copy floats left over a left-to-right gradient. Brass accents throughout."
---

# DS-0001 — /work Hero Section

## Visual Intent

The hero communicates: this organization is operational, grounded, and built by people who make physical things as well as digital ones. The workshop photograph (LDI field notebooks, compass, scissors, bonsai, stacked manuals, dashboard monitor, dark library behind it) establishes credibility before a word is read.

## Layout

**Desktop:** Full-bleed section. Background image spans the full container width. Copy floats on the left, readable against a left-to-right gradient overlay. The right side of the image is exposed — the desk, instruments, and library visible.

**Mobile:** Copy stacks full-width. Background image still present, repositioned to `70% 30%` to show the desk area rather than the ceiling. A vertical gradient (dark at bottom, lighter at top) ensures copy legibility.

## Implementation (as of 2026-06-25)

File: `src/pages/work/index.astro`

The `.hero` section breaks out of the `.work-content` container via negative margins:

```css
.hero {
  position: relative;
  margin: calc(-1 * var(--space-xl)) calc(-1 * var(--space-xl)) 0;
  padding: var(--space-xl) var(--space-xl) var(--space-xl);
  min-height: 500px;
  display: flex;
  align-items: center;
  background-image: url('/work-hero.png');
  background-size: cover;
  background-position: right 30%;
}
```

Gradient overlay applied via `::before`:

```css
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to right,
    rgba(10,10,12,0.97) 0%,
    rgba(10,10,12,0.88) 30%,
    rgba(10,10,12,0.55) 58%,
    rgba(10,10,12,0.15) 82%,
    transparent 100%
  );
  pointer-events: none;
}
```

Copy container:

```css
.hero-copy {
  position: relative;
  z-index: 1;
  max-width: 520px;
}
```

## Content Structure

```
[EYEBROW — brass, mono, 0.65rem, 0.25em tracking, uppercase]
Operating Systems Design Company

[H1 — Oswald, clamp(2rem → 3.25rem), paper]
Operational systems for modern organizations.

[BODY — 1rem, paper 65% opacity]
We design and build practical systems that remove friction...

[SECONDARY — 0.875rem, paper 38% opacity]
AI is one of our tools. Not our product.

[CTA GROUP]
  [PRIMARY BUTTON — brass background, ldi-black text]
  Start a Mission Brief

  [GHOST BUTTON — rain-slate border]
  Case Files

[FOOTNOTE — mono, 0.7rem, paper 22% opacity]
Automation begins only after understanding.
```

## Hero Image

File: `public/work-hero.png`

Subject: Dark workshop interior. Blueprint papers on a worn wood desk. Two LDI field notebooks (gold-stamped covers). Compass, scissors. Stacked manuals (Operational Systems, Pattern Library, Human + Machine, Infrastructure Design). Bonsai. Monitor showing a dashboard (Mission Control, harbor health metrics, manifest activity). Dark library shelving behind, warm ambient light.

The image is the clean source photograph. If replacing: use a photograph of a physical workspace, no baked-in text, no screen mockup, dark ambient tones, warm practical elements.

## Accent Colors (Corporate Grammar)

All accents in the `/work` section use `--brass: #B5893E`. Ghost-blue is reserved for the attraction grammar and must not appear in `/work/` pages. See ES-0001.

## See Also

- [ES-0001](../es/ES-0001-material-language.md) — Token definitions including `--brass`
- [ADR-0001](../adr/ADR-0001-attraction-precedes-corporate.md) — Why `/work` uses a different visual grammar than `/`
