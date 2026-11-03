# Safety: production, client systems, data, secrets

## Read only, by default

Why: live systems have real users, real money or legal weight, and often no undo.

- On production or a client's system, **look, don't touch**. Reading stats, queue depths, bindings,
  records and logs is fine. Creating, changing or deleting anything needs my yes **for that one
  action**: show a plain summary and every record it touches (IDs, names) first.
- Bulk changes: dry run first, one approval per group. Never batch speculatively.
- Don't create resources (queues, topics, buckets, users) on someone else's production to "just
  test". Test against a local copy (a Docker container of the same broker or database).
- Peeking at messages with "get and requeue" still changes the queue. Treat it as a write.
- Before reading a shared resource directly (a queue, a table to drain), say who else might read it
  and what they'd lose.

## Protected resources

- Each project lists its protected resources (see [the template](~/projects/agentic-coding-base/templates/project-AGENTS.md)).
  Don't touch them **in any way**, not even a read-only listing. Typical case: storage holding
  irreplaceable originals with no backup.
- A broad OK ("you can deploy it") does not lift a protected-resource rule.
- Never delete an infrastructure stack unless told to.

## Production paths

- **Never test against production APIs** (payments, government or other regulated services). Use the sandbox flag. Passing the sandbox
  doesn't prove production will accept it.
- Sandbox integration tests run **only in CI**, gated on secrets, skip (not fail) when secrets are
  missing, and carry a big warning banner at the top of the file.
- **Every production deploy needs my yes for that deploy.** An earlier yes doesn't carry over.
  Flags like `--require-approval never` are fine only after that yes.
- Where `main` auto-deploys (theme stores, CD), never push to `main`. Use a branch or `staging`.
- Never change an encryption scheme, an ID or serial formula, or a public API without a migration
  or deprecation path. Stored data and existing callers depend on them.

## Secrets

- Never print a secret: not in logs, replies, or partially. Read it into a variable inside the
  command that uses it.
- To compare a running container's settings with a file, compare inside the command and print only
  "same" or "different" per key.
- If I paste a password in chat, tell me once to rotate it.
- Secrets live in git-ignored files (`*.env`) or env vars. Commit only `*.env.example` with
  placeholders. Encrypt credentials at rest.
- Never log tokens, credentials or customer personal data at INFO or above.
- Never put secrets in URLs, query strings or args that land in shell history.

## Processes

- Stop only processes you can name and that we started. Show the PID and command first.
- An old helper still running (a bridge, a watcher) is a common cause of strange input. Check for
  leftovers before blaming the new code.
