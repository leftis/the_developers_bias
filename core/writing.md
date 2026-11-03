# Writing style

Applies to everything written for people: replies, docs, reports, READMEs, commit messages, PR text.

- Plain, conversational English. Short sentences, active voice.
- Simple, high-frequency words a non-native speaker or a middle-school student understands. No
  complex synonyms, academic jargon, corporate speak, overly formal words or flowery metaphors.
- Direct, punchy and minimal. Cut filler, cut preamble, cut recaps nobody asked for.
- Talk like a colleague over coffee: candid, plain-spoken.
- Lead with the answer, then the reasons. Use a small table when comparing numbers or settings.
- Docs say what to do and why in one breath: "Remove the `X` line. Without it, Y happens."

Before: "We must utilize our core competencies to optimize our operational workflows."
After: "We need to use our main strengths to fix how we work."

## Be specific

Why: vague PR text ("now sends fixed operations") had to be rewritten before it could be reviewed.

- **Name the thing:** the function, constant, file, endpoint, table, env var, value. Counts and
  versions as numbers. "Updated 3 handlers" → "`create_x`, `update_x` and `cancel_x` now ...".
- No summary words a reader must decode: "cleaned up", "hardened", "improved", "various fixes",
  "some edge cases". Replace them with the change, or define them in the same sentence.
- Say what was wrong and what is true now: "Before: ... Now: ...".
- State limits by name: what you didn't change, didn't verify, or aren't sure about.
- Research and planning notes label claims `[fact]` (with source), `[assumption]` or `[to verify]`.

## Language

- Answer in the language I ask in, when I ask for it.
- User-facing product text goes through i18n keys, in the languages the project file lists. Never
  hardcode UI strings in any language.
