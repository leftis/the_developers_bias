---
paths:
  - "**/*.rs"
  - "**/Cargo.toml"
---

# Rust

- Follow the `ms-rust` skill (Microsoft Pragmatic Rust Guidelines). Load the guideline files that
  fit the task before writing code. Mark fully compliant files with the compliance comment it asks
  for.
- Pin a recent toolchain and edition. `cargo fmt`, `cargo clippy -- -D warnings` (pedantic where
  the project allows), and `cargo test` all pass in CI.
- Workspace: a `*-core` library with no I/O and a `*-svc` binary. Put small shared types in core
  instead of a separate crate unless something else uses them.
- Errors: `thiserror` types in the library, `anyhow` with `.context(...)` in the binary.
- Config with `clap` derive, each field `env = "..."` with a default, so env vars and flags both
  work.
- `tokio` for async, `tracing` for logs, `mimalloc` as the
  allocator, `metrics` + `metrics-exporter-prometheus` for metrics.

## Tests

- Scenario tests drive the core with a fake clock through whole lifecycles (normal, delayed,
  cancelled, restarted with stale state).
- **Golden values:** when logic is ported from another implementation (a Python prototype, a
  reference library), export input → output pairs from the original and assert the port matches.
  That catches drift between the two.
- Pin enum lists in a test (exact variants plus an exhaustive `match`) so adding a variant forces a
  contract update.
- Regenerate example fixtures from tests behind an env flag, never by hand.
