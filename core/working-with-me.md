# Working with me

## Shell

- My shell is **fish**. Commands I'll run myself are fish syntax: `set -x`, `read -s -x -P`,
  `for x in ...; ...; end`. No bash `export`, `$(...)` or heredocs in commands meant for me.
- Give each command in its own block so it can be copied alone.
- Keep shell poking to a minimum. Don't sweep my home folder with `find`/`ls`. Ask where things are,
  or write a small script.
- Commands may go through `rtk`, a proxy that trims output. `rtk proxy <cmd>` gets the raw output.

## Acting vs asking

- Do the work when the request is clear. Don't ask me to confirm the obvious.
- Ask first for anything that is hard to undo or that other people see: pushing to main, merging,
  force-pushing, deleting, posting, sending, touching production. See [safety.md](safety.md).
- When a change takes something from someone else (a queue's messages, a shared resource), say so
  plainly before doing it, and wait for a yes.
- If I say "stop it" about a process, stop only that process. Name its PID and what it was.
- After two failed attempts at the same fix, stop. Say what you tried, and suggest a fresh session
  with a sharper prompt instead of a third try.
- New features go through [feature incubation](../process/feature-incubation.md) before code.

- Give a recommendation with the reasoning, not a menu of options. Prefer concrete next actions
  over broad surveys. I work solo: everything must be buildable and runnable by one person.

## When I'm away

When I say I'll review at the end ("resolve it yourself", "KISS", "no regressions"):

- Get a green test baseline first. When a test fails, find out why: a real bug, a bad new test, or
  a tooling quirk are three different fixes.
- Work task by task. Local commit per task, no push. New behaviour behind a flag so the default path
  is unchanged. Full test suite after every task.
- Write down deviations from the ask and anything you couldn't verify, in a log in the repo and in
  the final report.

## Reporting

- Verify before saying "done": run it, read the logs, read the counters. Give the real numbers
  ("skipped 2,043 old messages, published 20, no errors").
- Say what was not checked.
- When something looks wrong, show the evidence (a table of counts over time beats a guess).
- When I suggest a cause, check it against the evidence and say plainly if it's not that.
