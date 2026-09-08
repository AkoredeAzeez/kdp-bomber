# UCGF 1.0 — Universal Cookbook Generation Framework (integration manifest)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Niche:** `uapf-niche-cookbook` (OV-COOK) — LOCKED existing niche, not modified in architecture.
**Framework id (lock token):** `UCGF 1.0`  ·  **Folder:** `frameworks/UCGF-1.0/`

## Authoritative source (do not duplicate)
The authoritative, human-authored framework for this niche is, and remains:
1. `../../SKILL.md` — the cookbook niche skill (expert panel, book architecture, recipe-page
   structure, interior design, image contract, content rules, QA gates, KDP positioning).
2. `../../../uapf-global-rules/SKILL.md` and `AGENTS.md` global hard rules.

This folder does **not** re-author or copy those rules. It is the *machine-executable projection*
of them: the structured constants, gate-checkable validation, ordered phases, and deterministic
Python operations, extracted verbatim-in-meaning from the SKILL.md so the production agent can
execute them identically. Where this folder and `SKILL.md` ever disagree, **`SKILL.md` wins** and
this projection is corrected.

## The five parts (operator protocol)
| Part | File | Consumed by |
|---|---|---|
| reasoning / instruction rules | `rules.md` (index into SKILL.md) | Claude + the production agent |
| structured configuration | `config.json` | both, deterministic |
| validation requirements | `validation.json` | quality gates |
| deterministic Python operations | `genie_cookbook.py` | both, executed |
| production phases | `phases.md` | both |

## Persistence & lock
At Phase 0 the router stamps the canonical line into `book_lock.md` with `framework=UCGF 1.0`
(`framework_locked=true`). The resume controller reads that token, points the production agent at this folder +
the niche SKILL.md, and forbids reclassification. One source of truth feeds both agents.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
