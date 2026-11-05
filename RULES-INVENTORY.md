# Rules inventory

Every rule found in my repos and saved agent memories on 2026-11-03, sorted by category. Rules
that came up in more than one project are the core of the framework.

## 1. Communication and writing

- Plain, short, active English; no jargon or corporate speak
- Be specific: name the function, file, endpoint, value, number; no "cleaned up", "hardened"
- State limits: what you didn't change or couldn't verify
- Recommend one option with reasons instead of a menu
- Label claims `[fact]` / `[assumption]` / `[to verify]`
- User-facing text in the product's languages, through i18n keys; never hardcode UI strings
- My shell is fish; give fish commands

## 2. Safety: production, client systems, data, secrets

- Default is **read only** on live systems; ask before every write, list what will change
- Some resources are untouchable, even read-only (irreplaceable data, no backup)
- Never test against production; use the provider's sandbox
- Sandbox integration tests run only in CI, gated on secrets, self-skip locally, big warning banner
- Don't create resources (queues, etc.) on someone else's production
- A push to `main` may auto-deploy to production: never push there directly
- Never print, log or hardcode secrets; encrypt credentials at rest
- Never log PII or tokens at INFO+
- Don't delete infra stacks unless told; one was deleted by accident
- Pin region and profile explicitly on every cloud command
- Bulk operations: dry run first, one approval per group
- Never change encryption schemes, ID/serial formulas, or public APIs without a deprecation path

## 3. Changes, git, PRs and review

- Commit as me only; no AI co-author trailer, no "Generated with" line
- Branch, never push to main; owner merges
- Atomic commits, one logical change; message `component: change`
- Don't fix unrelated lint in the same change
- **Disclose every refactor** beyond the minimal fix; prefer asking first
- PR body has **Regression risks** and **How to test** (incl. what wasn't verified)
- **Triage** before planning: score blast radius, risk, complexity, size (0–2) → Direct / Planned / Spec
- Big work: design dialogue (one question at a time) → approved spec → tasks ≤ 400 lines / 10 files
- Every agent PR gets a **fresh-context review** (scope, correctness, slop checklist) before the owner
- A failed or empty reviewer is reported **not run**, never "no findings" (source: google/elephant-goldfish-model `agents/synthesizer.md`, 2026-11-04)
- A Ready plan leaves **no design choice** to the builder (source: google/elephant-goldfish-model, implementation-readiness standard, 2026-11-04)
- Re-triage when a change grows mid-flight
- Version bump + CHANGELOG + user-facing docs/FAQ in the same commit
- Agents write their own changelog entries, specific, newest date first
- Backlog items go to GitHub issues, not chat
- Tokens are repo-limited; never ask for org access or browser OAuth

## 4. Engineering standards

- Backend Rust; frontend React + strict TypeScript; WASM only from Rust
- Analysis in Python (Rust if needed), DuckDB storage, presentable charts
- TDD: failing test first
- Never edit an existing test just to pass; log the reason for any test change
- No `unwrap` in production paths; typed errors in libs
- Golden tests for generated output and for ports of another implementation
- Never commit commented-out code; no TODO without an issue
- Don't remove `#[allow]` / lint disables without knowing why
- Provider/integration-specific logic lives in its own module behind a trait
- Migrations: timestamped, idempotent, header comment, never drop columns without deprecation
- Delete code the live path doesn't use

## 5. Verification

- Verify against the real running thing before saying done
- UI: check mobile (375) and tablet (768–1024), not just desktop
- CSS: confirm with `getComputedStyle`, not by reading the file
- Pre-flight: check current state, live URLs, IDs before acting; stale values are the #1 failure
- Post-deploy checks named in the PR
- Check "no existing test changed" against `git diff`, don't assume

## 6. Working mode and autonomy

- When I'm away: task by task, local commits, no push, feature flag, full suite after each
- Don't touch my running dev containers; clean up rows you created
- Don't sweep my filesystem with shell; ask where things are
- Ask before anything other people see or that is hard to undo
- Design changes: run the design-taste skills first, ask which ones, get a go before building
- Be practical: size asks and changes to what is actually used, not the maximum; clients see our
  work (from a Shopify client project, 2026-11-05)

## 7. Session memory and project knowledge

- `.ai/` folder: AGENTS, DECISIONS (ADRs), TODO, SESSION_LOG, KNOWN_ISSUES, RUNBOOK
- Check decisions before architecture choices; log new ones
- Append-only decision log per item; killing an idea is a valid outcome
- Keep project facts (IDs, regions, URLs) in the agent file, and mark stale ones
- Before a session closes or archives, persist open items and unanswered questions to the
  project's task list (added 2026-11-04 at my request)

## 8. Platform playbooks (project-type specific)

| Platform | Rules |
|---|---|
| Shopify themes | Don't edit core theme files; `custom-` prefix; schema-first, no hardcoding; `render` not `include`; i18n; never edit `templates/*.json` / `settings_data.json`; no stray files in theme dirs; branch → theme mapping |
| Shopify store data | Read only; smart collections with rules on tags/metafields, never titles; SEO-first ASCII handles |
| AWS CDK | Fixed region; `cdk synth` + grep for stale values; CORS exact origin with credentials; rebuild frontend after env change |
| Messaging | Exchanges copy, queues split; viewers use temp queues |
| Supabase | Migrations rules, scope by tenant, RLS |

## 9. Tooling and tokens

- Commands go through `rtk` to trim output
- Don't `cat` files > 200 lines; quiet test runs; `git diff --stat`

## Conflicts, settled 2026-11-03

| Topic | Was | Decided |
|---|---|---|
| CSS `!important` | never vs accepted escape hatch | only against vendor CSS you can't edit, with a comment naming the selector it beats |
| When to commit | always commit each unit vs only when asked | commit each finished task locally without asking; push and PR only when asked |
| Deploy approval | `--require-approval never` vs confirm first | every production deploy needs a yes for that deploy |
| Facts in agent files | IDs kept in agent files, some stale | facts go in the project file, checked against live, stale ones marked `STALE` |
