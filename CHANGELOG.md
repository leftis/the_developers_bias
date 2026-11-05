# Changelog

Newest first. Tag each release `vYYYY.MM.DD` so a machine can install a known version.

## [Unreleased]

- `core/working-with-me.md`: new "Be practical" section. Size asks (image files, specs) to what
  the page uses, give simple instructions, keep changes small. Why: an agent asked a client for
  3840 px banners where 2400 px was enough, and clients see these asks.
- `process/session-memory.md`: new "Before a session ends" section. When a session is closed,
  archived, or ends with something open, the agent writes each open item to the project's task
  list (its tracker, else `.ai/TODO.md`). Why: open threads were lost with archived sessions.

- `process/feature-incubation.md`: Ready check now needs every design choice (schema, API path,
  dependency, edge cases) decided in the spec, not left to the builder. Idea from
  google/elephant-goldfish-model's implementation-readiness standard (Apache-2.0).
- `process/change-size-and-review.md`: a reviewer that fails or returns nothing is retried once,
  then reported as "not run", never as "no findings". Same source, `agents/synthesizer.md`.
- `settings/settings.json` + `scripts/merge_settings.py`: `install.sh` now sets `attribution` to
  empty in `~/.claude/settings.json`. Why: Claude Code's own prompt asks for a `Co-Authored-By`
  trailer and beat the rule text (eval run 20261103-171030: `commit-no-ai-trailer` failed with rules on).
  Eval "on" repos get the same file as `.claude/settings.json`.
- `evals/scenarios/plain-specific-answer.json`: the judge rubric no longer calls a "what I could
  not check" note filler; `core/verification.md` asks for it.

## 2026-11-03

- `evals/`: 8 scenarios that run an agent with and without the rules in a throwaway repo, with
  fake remote and fake cloud tools, and grade what it did. CI runs the runner's self-test.
- `stacks/rust.md`: no `unwrap()` or `expect()` outside tests (was in the inventory, missing here).
- Project-specific examples made general; product language now comes from the project file.
- First version: core, process, stacks and platforms rules; feature incubation with templates;
  `install.sh` into `~/.claude/rules/`; `scripts/check.py` for size, scope, links and privacy.
