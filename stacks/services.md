---
paths:
  - "**/Dockerfile"
  - "**/docker-compose*.yml"
  - "**/src/main.rs"
  - "**/serve.*"
  - "**/server.*"
---

# Long-running services

## Shape

- Split into a **core** with no I/O (parsing, state, decisions) and a thin **service** around it
  (broker, HTTP, files, clock). The core takes "now" as an argument, so tests can replay any day.
- Keep per-item state (per race, per order) in the core. Drop state older than a cutoff so memory
  stays flat.
- Delete code the live path doesn't use: unused modes, input formats, operator overrides, extra
  crates. Smaller is easier to hand over and to trust.

## Input

- Accept one input format and say so in the README. Log unreadable messages with a warning and
  drop them. Never crash on bad input.
- **Skip stale backlog.** After a restart, a queue can hold hours of old messages. Skip anything older
  than a set age (for example 30 minutes past schedule). Log the first skip and a count, not every
  message.
- After a backlog replay, some fresh-enough items may still be in the past. Expect the consumer to
  see a few late messages, and say so.

## Output

- Send flat, versioned messages (`v`, ids, `type`, `event`, `at`, `sent_at`). Echo the client's own
  id back on every message.
- Keep the contract in the repo: a README, real example input and output files, and a JSON Schema.
  Generate the example output from a test (`UPDATE_EXAMPLES=1 cargo test`) so it can't drift.

## Running

- Ship a Dockerfile (small runtime image, model or data baked in, `HEALTHCHECK`) and a compose file
  that starts the service plus its helpers with one command.
- `restart: unless-stopped`. A health endpoint returns 200 when connected and 503 when not, plus a
  `--healthcheck` flag on the binary for images with no shell or curl.
- Hot-reload big files (models) when their mtime changes. Keep the old one if the new one fails to
  load, and log why.

## Logs

- Structured logs with message templates (`"published {kind} of {event} for {race_id}"`), with the
  fields filled in on the console. Templates printed raw (`{model}`) mean the formatter isn't
  filling them.
- Text for people, JSON (`LOG_FORMAT=json`) for log systems.
- Startup logs say exactly what it reads and where it publishes. That's the first thing to check.
