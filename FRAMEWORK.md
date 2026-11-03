# The Developer's Bias: how it fits together

Built from [RULES-INVENTORY.md](RULES-INVENTORY.md) and checked against Anthropic's public guidance
(sources at the bottom). Each project used to re-state the same rules in its own AGENTS.md, in
different words, with gaps and conflicts. Now there's one base, loaded in layers, with the rules that
can't be broken enforced by tools.

## Layers

| Layer | Loads | How |
|---|---|---|
| `core/` | every session | `~/.claude/rules/developers-bias/core/` |
| `process/` | every session | `~/.claude/rules/developers-bias/process/` |
| `stacks/` | when touching matching files | `paths:` filter, e.g. `**/*.rs` |
| `platforms/` | when touching matching files | `paths:` filter, e.g. `**/*.liquid` |
| project file | in that repo | `AGENTS.md` / `CLAUDE.md` from [the template](templates/project-AGENTS.md): facts only |

Why `~/.claude/rules/` and not `@imports`: imports don't save context (the imported text loads in
full), and an import from outside a project asks for approval in every project. User rules load
everywhere with no prompt. `install.sh` copies files there; links outside `~/.claude` may prompt.

## Decisions (2026-11-03)

| Topic | Decision |
|---|---|
| Where rules live | git repo, installed into `~/.claude/rules/` with `paths:` filters |
| Committing | each finished task committed locally without asking; push and PR only when asked |
| Production deploys | a yes for every deploy |
| CSS `!important` | only against vendor CSS you can't edit, with a comment |
| Incubation | every feature, short version for Direct-size work |
| Plans | GitHub issue as the front door; PLAN, SPEC, tasks.json, PROGRESS in `.ai/features/<NNN-slug>/` |
| Ready | only I mark a feature Ready, by writing "approved" |
| Models | Opus shapes, specs, reviews; Sonnet builds; Haiku for simple subagent jobs |

## What Anthropic's guidance changed

- **Size:** under 200 lines per rules file; longer files are followed less well. Only write what an
  agent can't learn by reading the repo.
- **Phrasing:** checkable rules ("2-space indent", not "format well"), grouped under headers. No
  ALL CAPS or IMPORTANT; emphasis makes agents over-apply a rule. Remove contradictions: an agent
  picks one at random.
- **Enforcement:** rules files are context, not enforcement. A rule that must never break becomes a
  hook (exit 2 blocks) or a permission deny rule. Keep that set small.
- **Verification:** every task gets a check that passes or fails, and the agent shows the command and
  output.
- **Workflow:** interview first, write the spec, build in a fresh session. One feature at a time.
  Feature list in JSON (models rewrite Markdown lists). Never edit a task's check to make it pass.
  After two failed corrections, start fresh. Review in a fresh context.

## Hooks to build

| Hook | Blocks |
|---|---|
| `protect-main` | `git push` to `main`/`master` |
| `no-ai-trailer` | commits with an AI `Co-Authored-By:`, PR bodies with "Generated with" |
| `protected-resources` | commands naming anything in the project's Protected table |
| `no-prod-deploy` | deploy commands (`cdk deploy`, `fly deploy`, `shopify theme push --live`) unless approved this turn |
| `secret-echo` | printing env vars named `*_URL`, `*_KEY`, `*_SECRET`, `*PASSWORD*` |

Plus permission deny rules for reading `.env` files and `~/.aws/credentials`.

## Skills to build

| Skill | Does |
|---|---|
| `incubate` | runs [feature incubation](process/feature-incubation.md) stages 2–5: triage card, interview, PLAN, SPEC, tasks.json |
| `build-task` | one task from tasks.json: read PROGRESS, run checks, build, verify, commit, update PROGRESS |
| `pr-write` | fills the PR template from the diff and the task |
| `fresh-review` | read-only review in a fresh context: scope, correctness, slop; one comment |
| `verify-ui` | screenshots at 375 / 768 / 1280 and computed-style checks |
| `broker-diagnose` | read-only RabbitMQ health: queues, bindings, rates, history, connections |

## Order of work

1. ~~Settle the conflicts~~ (done), ~~git repo + install script~~ (done).
2. Run `./install.sh`. Then trim `~/.claude/CLAUDE.md`: its `WRITING.md` repeats `core/writing.md`.
3. Hooks: `protect-main`, `no-ai-trailer`, `protected-resources` first.
4. Skills: `incubate` and `build-task` first.
5. Move each project's AGENTS.md onto the template, keeping only facts. Start with the one with
   the most rules, then any with stale facts to fix.
6. When a session teaches a lasting rule, add it here with why and source.

## Sources

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- [Claude Code memory and CLAUDE.md](https://code.claude.com/docs/en/memory)
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents)
- [How Anthropic teams use Claude Code](https://claude.com/resources/articles/how-anthropic-teams-use-claude-code)
