# Change size and review

Why: big multi-component PRs cost too much to review and hide regressions.

## 1. Triage before planning

Score the work 0–2 on each line and post the card before writing code.

| | 0 | 1 | 2 |
|---|---|---|---|
| **Blast radius** | one component | 2 components or a shared module | 3+ components, or auth, billing, money, encryption, migrations on existing tables |
| **Risk** | reversible, internal | user-visible change, needs a flag | money, legal/tax data, irreversible effects |
| **Complexity** | copies an existing pattern | new pattern or unchecked external API | new architecture or integration, open questions |
| **Size** (non-test lines) | ≤ 400 and ≤ 10 files | 401–800 or 11–15 files | > 800 or > 15 files |

| Track | When | Then |
|---|---|---|
| **Direct** | total ≤ 2, no 2s | one PR, continue after posting the card |
| **Planned** | total 3–4, no 2s | short plan file (goal, files, acceptance, tests); wait for my OK |
| **Spec** | total ≥ 5 or any 2 | design dialogue → approved spec → tasks; no code until I approve |

Re-score and tell me if a change grows past its track mid-way.

## 2. From triage to code

Every feature then goes through [feature-incubation.md](feature-incubation.md): shaping, spec and
breakdown until I mark it Ready. One task = one branch = one PR, ≤ 400 changed non-test lines and
≤ 10 files, test first, with a pass/fail check and a way to *see* it working.

## 3. Minimal changes

- Do the fix asked for. **List every extra** (rename, restructure, reformat, "align with prod",
  tidy nearby code) with why and whether the fix needed it. Better: ask before doing it.
- Don't fix unrelated lint in the same change.
- Never edit an existing test just to make it pass. If one must change, write down why.

## 4. Review before me

1. **Self-check** by the author: lint, tests, slop checklist over its own diff.
2. **Fresh-context review** (a new session or subagent that didn't write it): scope vs the ask,
   correctness, slop. One comment: **Must fix / Should fix / Nits**. Review only changed lines.
3. Author fixes every Must, answers every Should.
4. I review and I merge. Agents never merge their own work unasked.

**Slop checklist:** dead code; commented-out code; TODO without an issue; comments that narrate
instead of explaining why; duplicated logic where a helper exists; abstractions with one user;
defensive checks for impossible states; fallbacks that hide bugs; magic values; vague names;
changes outside the task's files; new `unwrap`/`any`/lint-disables without a reason; tests that
only check a mock was called.
