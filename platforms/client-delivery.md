---
paths:
  - "README.md"
  - "docs/**"
  - "contract/**"
---

# Handing a service to a client

## Ship the smallest thing that proves the idea

- Share the runnable part first (for example inference with a compiled model file), and keep the
  rest (training, research) back until the idea is proven.
- Use a separate repo with clean history. See [git-and-prs.md](../process/git-and-prs.md).
- Make it "almost ready to run": one settings file, one command to start.

## README must answer

1. **Who it's for and what it doesn't cover.** Put limits up front (for example "GB races only,
   not for AU: AU input has a different shape").
2. **How to run it:** copy the example settings, fill in one URL, `docker compose up -d --build`, and
   what the first log lines should look like.
3. **Input:** the one accepted format, with a real example file.
4. **Output:** every field, every message type, an example sequence, and a JSON Schema.
5. **Monitoring and troubleshooting:** a table of error message → cause → fix, built from
   real problems.
6. **Updating:** how to swap in a new model or version.

## Give them a way to see it work

- A small viewer (web page) that watches the output through its own temporary queue and shows each
  item live with a countdown. It must take nothing from the real consumer.
- Optional monitoring stack behind a compose profile. See [observability.md](../stacks/observability.md).

## When their side changes

Their systems will change without notice (a feed moving from an exchange to a queue, a renamed
key). When input stops:

1. Prove it with numbers from the broker (see [messaging.md](../stacks/messaging.md)).
2. Write them a short, factual note on what changed and what you need.
3. Change config, not code, when you can. Update the example settings and docs in a PR so the
   repo matches what's running.
