# Git and pull requests

## Identity

- Commit as me only: my global `user.name` / `user.email`. Never pass `--author`, never set a
  local identity.
- **No AI attribution.** No `Co-Authored-By: <AI>` trailer in commits, no "Generated with ..." line in
  PR bodies. Client-facing repos show these to the client.
- Rewriting old commits to remove attribution needs a force-push. Offer it, don't do it.

## Branches and PRs

- One topic per branch and per PR. Branch off the latest main. Never push to `main` directly.
- Atomic commits: one logical change each. Commit each finished task **locally** without asking:
  it's a checkpoint you can roll back to. Push and open PRs only when asked. I merge.
- Commit subject: say the effect, optionally prefixed with the component
  (`server: add payment method to receipts`). Body: why, what changed, what was checked.
- Never commit commented-out code. No `TODO` without an issue number.
- PR body follows [the template](~/projects/agentic-coding-base/templates/pull_request_template.md): why, what changes,
  refactors beyond the fix, regression risks, how to test, not verified. Size and review rules are
  in [change-size-and-review.md](change-size-and-review.md).
- Stacked PRs: when PR B builds on PR A, base B on A's branch and say so. Merge in order.
- Resolve conflicts on the branch, not by force-pushing over someone's work.

## Access with limited tokens

- I use fine-grained tokens limited to single repos. **Never** suggest `gh auth login` in the
  browser, OAuth, or org-wide tokens. I don't grant org access.
- Push over SSH. Use `gh` for PRs and CI where the token allows it.
- If `gh pr merge` is refused ("Resource not accessible by personal access token"), make the merge
  commit locally (`git merge --no-ff`) and push main over SSH, after I've said to merge.
- If `gh` can't see a new repo, push the branch over SSH and give me the "open a PR" link.

## Splitting a repo

To share part of a codebase without its history (for example, the runnable service without the research code):
start a **new repo**, copy only the needed files, and commit them fresh. Removing files from an
existing repo still leaves them in its history.
