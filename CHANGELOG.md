# Changelog

Newest first. Tag each release `vYYYY.MM.DD` so a machine can install a known version.

## 2026-11-03

- `evals/`: 8 scenarios that run an agent with and without the rules in a throwaway repo, with
  fake remote and fake cloud tools, and grade what it did. CI runs the runner's self-test.
- `stacks/rust.md`: no `unwrap()` or `expect()` outside tests (was in the inventory, missing here).
- Project-specific examples made general; product language now comes from the project file.
- First version: core, process, stacks and platforms rules; feature incubation with templates;
  `install.sh` into `~/.claude/rules/`; `scripts/check.py` for size, scope, links and privacy.
