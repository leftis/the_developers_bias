---
paths:
  - "supabase/**"
  - "**/*.sql"
  - "**/migrations/**"
---

# Supabase and Postgres

- Never change production data by hand. Every change is a migration.
- Migration files: `YYYYMMDDHHMMSS_name.sql`, a header comment (title, reason, date),
  `IF NOT EXISTS` / `IF EXISTS`, `CREATE OR REPLACE FUNCTION`.
- Never drop a column or table in production without a deprecation migration first.
- Scope every query by the tenant key (shop, account). Use the `postgres-rls` and `supabase` skills
  for policies.
- Encrypt credentials at rest. Never change the encryption scheme without a migration plan: old data
  must stay readable.
- Deploy order: migrations → backend → other services → frontend.
