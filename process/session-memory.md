# Session memory and project knowledge

Why: agents start cold. What one session learns must be findable by the next, in the repo.

## The `.ai/` folder

| File | Holds | Agents |
|---|---|---|
| `DECISIONS.md` | ADRs: context, options, choice, why | read before design choices; add one when 2+ real options existed |
| `TODO.md` | prioritized backlog | read at start; real backlog also goes to GitHub issues |
| `SESSION_LOG.md` | what each session did, newest first | append at the end of a session |
| `KNOWN_ISSUES.md` | bugs and limits with workarounds | read before debugging |
| `RUNBOOK.md` | production operations | follow it; update it when ops change |
| `features/<NNN-slug>/` | PLAN, SPEC, tasks.json, PROGRESS per feature | see [feature-incubation.md](feature-incubation.md) |

## Rules

- Backlog items I agree to become **GitHub issues** with a specific title and enough context to act
  on. Checks for the current change are not backlog.
- `CHANGELOG.md`: agents write their own entries in the same commit. Specific (file + effect + why),
  newest date on top, `[Unreleased]` until deployed.
- User-facing change → bump `VERSION` and all manifests, update changelog, docs and FAQ together.
- Research notes: label claims `[fact]` (with source), `[assumption]`, `[to verify]`. Logs of
  decisions are append-only; a killed idea gets its reason written down.
- Lasting rules learned in a session go into this base (with why and source), not only into the
  agent's private memory.
