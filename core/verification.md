# Verification

"Done" means checked on the real thing, not "the code looks right". Every task needs a check that
passes or fails (a test, a command, a script). Show the command you ran and its output as evidence.

## Before acting

- Check the current state first: read the files, query the live system, confirm URLs and IDs.
  Stale values (old URLs, old client IDs, wrong region) are the most common cause of failure.
- Pin region, profile and account explicitly on every cloud command. Never trust the default.
- Grep the build output (`cdk synth`, bundles) for stale hardcoded values before deploying.

## After changing

- Run lint and the tests for every component touched. Quiet output (`-q`), but read failures.
- Run it: start the service, hit the endpoint, read the log lines and the counters.
- UI: check **375 px (phone), 768–1024 px (tablet) and desktop**. Confirm CSS landed with
  `getComputedStyle`; a lost specificity fight looks identical to a working edit until checked.
- Claims like "no existing test changed" get checked against `git diff <base>`.
- After deploy: hit the live URL, check CORS headers, auth callbacks and the version shown.

## Reporting

- Give numbers: how many read, skipped, published, failed.
- List what you could not verify (needs real admin, production-only path, hardware) so I test it.
- Clean up what you created to test (rows, queues, files). Don't touch my running dev containers.
