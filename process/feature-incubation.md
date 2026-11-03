# Feature incubation

Why: agents build well from a clear plan and badly from a vague ask. Every feature is worked into a
plan until it's ready for agents, and only then built.

## Stages

| Stage | Who | Output | Leaves when |
|---|---|---|---|
| 1. Request | me | GitHub issue: the ask in my words | issue exists |
| 2. Triage | Opus | scorecard on the issue (see [change-size-and-review.md](change-size-and-review.md)) | track picked: Direct / Planned / Spec |
| 3. Shaping | Opus + me | `PLAN.md`: problem, outcome, out of scope, constraints | no open questions about *what* |
| 4. Spec | Opus + me | `SPEC.md`: boundaries, data, APIs, flags, rollout and rollback, tests | no open questions about *how* |
| 5. Breakdown | Opus | `tasks.json` + `PROGRESS.md` | every task meets the Ready check |
| 6. **Ready** | **me only** | I write "approved" | — |
| 7. Build | Sonnet, one task per fresh session | one branch, one PR per task | task's check passes |
| 8. Review | Opus, fresh context | one PR comment: Must / Should / Nits | Musts fixed |
| 9. Done | me | merged, issue closed | — |

Direct-track work (triage total ≤ 2) still goes through it, but stages 3–5 shrink to one short
`PLAN.md` with the tasks inline.

Files live in the repo under `.ai/features/<NNN-slug>/`, linked from the issue. Start from
[templates/feature/](~/projects/agentic-coding-base/templates/feature/).

## Shaping and spec: how the interview runs

- One question at a time, each with a recommended answer and the reason.
- Ground options in the repo: name the file, function or pattern each one reuses or changes.
- Check `.ai/DECISIONS.md` first. A choice between real options becomes an ADR.
- No implementation code. A throwaway spike only with my OK, deleted after.
- Label anything unproven `[assumption]` or `[to verify]`; Ready can't have any `[to verify]` left.

## The Ready check

A feature is ready when **every** line is true. Agents may say "I think it's ready"; only I mark it.

- [ ] Outcome and out-of-scope written; no open questions.
- [ ] Every task is ≤ 400 changed non-test lines and ≤ 10 files, and names those files.
- [ ] Every task has a **check that passes or fails** (a test, a command, a script) and a demo step.
- [ ] Tasks are ordered, with dependencies listed. Each can merge on its own without breaking main.
- [ ] Regression risks listed, with rollback per task. Flags named if behaviour changes.
- [ ] Nothing left marked `[to verify]`.
- [ ] Anything touching protected resources or production says how it's tested without them.

## Building from the plan

- Start each session by reading `PROGRESS.md`, `tasks.json` and `git log`, then run the project's
  checks to catch anything already broken.
- Take the first unfinished task. One task per session. Don't start the next one in the same session.
- Only flip that task's `status` in `tasks.json`. Never edit or delete a task's check to make it pass.
- Done means the check passes and the demo step works, seen with your own eyes (browser, curl, logs).
- Commit locally when the task is done; push and open the PR only when asked.
- Update `PROGRESS.md`: what was done, what was learned, what the next session should know.
- If the plan turns out wrong, stop. Update `SPEC.md` first (with a dated note), then the tasks, and
  tell me.
- After two failed attempts at the same fix, stop and start a fresh session with a better prompt.

## Models

| Work | Model |
|---|---|
| Triage, shaping, spec, breakdown, review | Opus |
| Building a task | Sonnet |
| Simple subagent jobs (search, summarize, list) | Haiku |
