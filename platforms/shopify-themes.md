---
paths:
  - "**/*.liquid"
  - "sections/**"
  - "snippets/**"
  - "blocks/**"
  - "locales/**"
  - "config/settings_schema.json"
  - "shopify.*.toml"
---

# Shopify themes and store data

## Theme code

- **Don't edit the base theme's own files.** New work goes in `custom-*` sections/snippets, so theme
  upgrades stay clean.
- Never edit `templates/*.json` or `config/settings_data.json`: the Shopify admin owns them.
- **Schema first, no hardcoding:** colors, fonts, sizes, text, images, handles and metafield keys
  come from section/block settings or CSS variables. Defaults must render a complete component.
- `{% render %}` with parameters, never `{% include %}`. Snippets don't read `section.settings`.
- Every string through `{{ 'key' | t }}` in every language the store sells in (`locales/*.json`).
- Images: explicit `width`/`height`, `loading="lazy"`, no layout shift. Scripts `defer`/`async`.
  Respect `prefers-reduced-motion`. `aria-label` on icon buttons. Tap targets ≥ 48 px.
- Vendor CSS you can't edit: match its specificity first; `!important` only when you can't, with a
  comment naming the selector it beats. Check with `getComputedStyle`.
- Never leave backups or scratch files (`*.bak`) inside theme folders: `shopify theme dev` tries to
  upload them and breaks the preview. Use a `.backups/` folder at the root.
- Validate with theme-check / `validate_theme` before committing.

## Branches deploy

Git branches are wired to themes: `main` → live theme, `staging` → staging theme. **A push to `main`
goes live with no review.** Work on a branch or `staging`; ask before anything reaches `main`.

## Design changes

Taste calls (hierarchy, color, type, spacing, new controls) aren't made on the agent's own judgment:
ask the design skills whether the change is justified, ask me which skills to use for proposals,
show me the proposals, and build only after I say go. Check phone and tablet widths every time.

## Store data (Admin API)

- **Read only by default.** Before any write: plain summary, every record affected (IDs, handles),
  then wait for a written yes. Dry run bulk operations first.
- Products and navigation menus are read-only without explicit approval.
- Collections: smart collections with rules on tags, metafields, vendor or price, **never on
  titles**. Check the rule's field is filled on products before creating it.
- Handles: lowercase ASCII English, `audience-type-qualifier`, under 50 characters, self-describing.
  Titles in the customer's language with SEO title and description filled.
