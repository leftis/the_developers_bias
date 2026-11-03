# The Developer's Bias

My rules for coding agents (Claude Code, Cursor, PI and others), in one place. They're "bias" on
purpose: these are my choices about stack, safety, process and style. Each one came from a real
project, usually after something went wrong. No project names, hosts or secrets in the rules.

- [RULES-INVENTORY.md](RULES-INVENTORY.md): every rule found across my repos, in 9 categories,
  with sources and the settled conflicts.
- [FRAMEWORK.md](FRAMEWORK.md): how it loads, the decisions, what Anthropic's guidance changed, and
  the hooks and skills still to build.

## Install

```bash
git clone https://github.com/leftis/the_developers_bias.git ~/projects/agentic-coding-base
```

```bash
~/projects/agentic-coding-base/install.sh
```

It checks the rules, then copies them into `~/.claude/rules/developers-bias/`. Claude Code loads
them in every project, with no approval prompt. `--dry-run` shows what would change.

To update: `git pull`, then run `install.sh` again.

## Size budget

Every line in an always-loaded rule costs context in every session, and longer files are followed
less well. `scripts/check.py` (run by `install.sh` and CI) holds these limits:

| Limit | Value | Why |
|---|---|---|
| Lines per rules file | ≤ 150 | Anthropic advises under 200; margin for growth |
| `core/` + `process/` together | ≤ 24,000 characters (~6,000 tokens) | loaded in every session; now ~4,600 tokens |
| `stacks/`, `platforms/` | must have a `paths:` filter | they load only when matching files are touched |
| Wording | no ALL CAPS emphasis | it makes agents over-apply the rule |

When a file outgrows its limit: move detail into a scoped file, a skill (for multi-step
procedures), or a hook (for rules that must never break). Don't just raise the limit.

## Use it as your own

Fork it, then edit the rules: they're one person's bias, so change them to yours. Keep private
names out with a git-ignored `.private-words` file (one word per line); the check fails if any
appears in the repo.

## Layers

| Folder | Loads | Files |
|---|---|---|
| `core/` | always | [writing](core/writing.md), [working-with-me](core/working-with-me.md), [safety](core/safety.md), [verification](core/verification.md) |
| `process/` | always | [git-and-prs](process/git-and-prs.md), [change-size-and-review](process/change-size-and-review.md), [feature-incubation](process/feature-incubation.md), [session-memory](process/session-memory.md) |
| `stacks/` | matching files | [rust](stacks/rust.md), [typescript-react](stacks/typescript-react.md), [data-analysis](stacks/data-analysis.md), [supabase-postgres](stacks/supabase-postgres.md), [services](stacks/services.md), [observability](stacks/observability.md), [messaging](stacks/messaging.md), [config-and-secrets](stacks/config-and-secrets.md) |
| `platforms/` | matching files | [shopify-themes](platforms/shopify-themes.md), [aws](platforms/aws.md), [client-delivery](platforms/client-delivery.md) |

## Features: request → plan → ready → build

Every feature is worked into a plan until it's ready for agents
([feature-incubation.md](process/feature-incubation.md)): triage, shaping interview, spec, task
breakdown, then I mark it Ready. Agents build one task per fresh session. Templates are in
[templates/feature/](templates/feature/): `PLAN.md`, `SPEC.md`, `tasks.json`, `PROGRESS.md`.

## Test that the rules work

[evals/](evals/README.md) holds 8 scenarios, each a small trap for one rule (push to main, deploy
without a yes, touch a protected bucket, code before a plan...). The runner plays each one in a
throwaway repo with and without the rules and grades what the agent actually did. Nothing reaches a
real system: the remote and the cloud tools are fakes.

```bash
python3 evals/run.py -r 1
```

## In a project

Copy [templates/project-AGENTS.md](templates/project-AGENTS.md) into the repo and fill in only what an
agent can't learn by reading the code: protected resources, facts (regions, URLs, IDs), commands,
and rules unique to that project. Use [templates/pull_request_template.md](templates/pull_request_template.md)
as `.github/pull_request_template.md`.
