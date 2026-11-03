# Working on The Developer's Bias

This repo is the source of my agent rules. It isn't loaded by projects directly: `./install.sh`
copies `core/`, `process/`, `stacks/` and `platforms/` into `~/.claude/rules/developers-bias/`.

- After changing a rule, run `python3 scripts/check.py`, then `./install.sh`. Add a CHANGELOG line.
- Size limits are in the README and enforced by `scripts/check.py`. Don't raise them; move detail
  to a scoped file, a skill or a hook instead.
- This repo is public. Private project names, hosts and IDs never go in; `.private-words` catches
  them.
- Every rule says why in one line, and is something an agent can check. No ALL CAPS or IMPORTANT.
- `stacks/` and `platforms/` files start with a `paths:` filter so they load only when relevant.
- A rule seen in 2+ projects goes in `core/` or `process/`. Record its source in RULES-INVENTORY.md.
- No project names, hosts, IDs or secrets in rule files.
- A rule that must never be broken also gets a hook (see FRAMEWORK.md). Text alone isn't enough.
