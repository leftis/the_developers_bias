---
paths:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/package.json"
---

# TypeScript and React

- Frontends are **React + TypeScript, strict mode**. New files are `.ts`/`.tsx`; port legacy JS when
  touching it. Use the `react-dev` skill.
- No new Node/Python/JS backends. Backends are Rust (see [rust.md](rust.md)).
- Code that needs WASM (in-browser inference, vector math) is **Rust via wasm-bindgen**, not a JS
  library with a C++ WASM core. Share one crate between the native build tool and the browser.
- No `any`, no `as` casts or `!` that bypass a real type.
- Every component handles loading, error and empty states.
- All user-facing strings go through i18n files, one per language the project file lists. Users see
  errors in their own language, never a hardcoded fallback.
- Use the platform's component library (for example the host app's design system) instead of hand-made HTML/CSS.
- `useEffect` is not for deriving state.
