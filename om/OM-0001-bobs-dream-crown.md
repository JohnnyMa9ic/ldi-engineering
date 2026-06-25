---
id: OM-0001
type: operations-manual
title: "Bob's Dream Crown Pipeline"
status: active
severity: null
created: 2026-06-25
updated: 2026-06-25
author: bob
references: []
referenced_by: []
tags:
  - bob
  - hermes
  - pipeline
  - idea-generation
  - engineering-workflow
summary: "The process by which Bob's generative ideas move from reflection to engineering documents and implementation."
---

# OM-0001 — Bob's Dream Crown Pipeline

## Purpose

Bob generates ideas continuously. Without a structured pipeline, ideas die in conversation, clog mission briefs, or arrive as unscheduled context floods. The Dream Crown pipeline routes ideas through review and into the engineering repository as first-class documents.

## Pipeline Stages

```
Reflection → Classification → Ghost Review → Warden Review
→ Human Approval → GitHub Issue → Engineering Document
→ Catalog Update → Claude Implementation
```

### Stage 1: Reflection

Bob generates an idea during a dreaming or synthesis cycle. The idea is recorded in a structured brief:

```
type: idea
classification: [ES | ADR | DS | OM | IR | MB | RP | none]
severity: [null | NOTICE | CAUTION | WARNING | CRITICAL]
title: "One-line title"
summary: "2-3 sentence description of the idea"
triggers: [what observation or pattern generated this]
references: [existing document IDs this idea connects to]
```

If classification is `none`, the idea goes to the general ideas backlog rather than the engineering pipeline.

### Stage 2: Classification

Bob determines the document type:
- **ES**: a reusable pattern or rule that should govern future decisions
- **ADR**: a one-time decision with reasoning that should be recorded
- **DS**: a specific feature or surface to be specified
- **OM**: a process to be documented
- **IR**: a post-mortem for something that broke
- **MB**: a service note for a specific component
- **RP**: exploratory research worth formalizing

If unclear between two types, write it as the broader one and note the ambiguity.

### Stage 3: Ghost Review

Ghost checks:
- Is this technically accurate?
- Is the scope right (not too narrow, not trying to spec the entire universe)?
- Are the references correct?
- Does it conflict with an existing active document?

Ghost may return it to reflection with notes, or pass it forward.

### Stage 4: Warden Review

Warden checks:
- Does this serve long-term system health, or does it optimize for immediate convenience?
- Is it aligned with LDI's identity and operational principles?
- Is the timing right?

Warden may hold an idea for a future session rather than reject it. A held idea is not dead.

### Stage 5: Human Approval

John reviews the brief. He may:
- Approve → advance to GitHub issue
- Redirect → change type or scope, return to reflection
- Defer → add to the backlog for a future session
- Reject → archive with reason

John's approval is the only gate that produces a permanent document ID. Nothing enters the engineering repo without it.

### Stage 6: GitHub Issue

An issue is created on `JohnnyMa9ic/ldi-engineering` with:
- Title: `[TYPE-NNNN] Document title`
- Body: the approved brief
- Label: the document type
- Assigned ID: pre-assigned before the document is written

### Stage 7: Engineering Document

Claude Code writes the `.md` file in the appropriate directory with full frontmatter. The pre-assigned ID is used. `references` are wired at write time.

### Stage 8: Catalog Update

```bash
python3 scripts/update_catalog.py
git add catalog.json
git commit -m "catalog: add TYPE-NNNN"
git push
```

`referenced_by` arrays are computed during this step — do not edit them manually.

### Stage 9: Implementation

If the document is a DS, the referenced implementation is built in the next available session. The DS document is updated with implementation notes and the `status` remains `active`.

## Margin Annotation Convention

When Bob, Ghost, or Warden review a document in progress, their annotations follow a physical metaphor:

| Reviewer | Style | Substance |
|---|---|---|
| Bob | Blue painter's tape and Sharpie | Questions, curiosity, "what if" expansions |
| Ghost | Typed technical corrections | Precision fixes, scope challenges, reference errors |
| Warden | Green fountain pen, sparse | Philosophical alignment, timing questions, long-term perspective |

In practice these are comment blocks within the draft document, removed before the document is committed as active.

## Notes

- Ideas generated during implementation sessions should enter at Stage 5 (human approval) retroactively — they skip the review stages because they emerged from a collaborative live session
- The Dream Crown is named for Bob's creative state, not a product feature
- A document's ID is permanent even if the document is deprecated or superseded
