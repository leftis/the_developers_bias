# <Project name>

<One paragraph: what it is, who uses it, stage (prototype / production with live users).>

The Developer's Bias rules load from `~/.claude/rules/developers-bias/` (run `install.sh` in the
base repo). This file holds only what an agent can't learn by reading the repo: protected resources,
facts, commands, and rules unique to this project. Anything true for 2+ projects belongs in the base.

## Protected (never touch without a yes for that one action)

| Resource | Why |
|---|---|
| <bucket / DB / vhost / branch> | <e.g. originals, no backup; main auto-deploys to the live store> |

## Facts

Verify against the live system before relying on any of these. Mark a value `STALE` instead of
deleting it, so nobody brings it back.

| What | Value | Checked |
|---|---|---|
| Product languages (i18n) | | |
| Region / profile | | |
| Live URLs | | |
| IDs (pools, clients, themes) | | |

## Components

| Component | Tech | Run | Test | Deploy |
|---|---|---|---|---|

## Project rules

- <rule> — why: <one line>
