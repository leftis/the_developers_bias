#!/usr/bin/env python3
"""Checks the rules before they're installed or pushed.

- every rules file stays under the line limit (Anthropic: under 200 lines per file);
- the always-loaded set (core/ + process/) stays within the token budget;
- stacks/ and platforms/ files start with a `paths:` filter, so they load only when relevant;
- relative links resolve;
- no ALL CAPS emphasis (it makes agents over-apply a rule);
- none of the words in `.private-words` (git-ignored, one per line) appear anywhere.

Run: python3 scripts/check.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_LINES = 150
ALWAYS = ["core", "process"]
SCOPED = ["stacks", "platforms"]
ALWAYS_BUDGET_CHARS = 24_000  # about 6,000 tokens at ~4 characters per token
SHOUTING = re.compile(r"\b(IMPORTANT|MUST|NEVER|ALWAYS|CRITICAL)\b")

problems = []


def rules(dirs):
    return sorted(p for d in dirs for p in (ROOT / d).glob("*.md"))


for path in rules(ALWAYS + SCOPED):
    text = path.read_text()
    name = path.relative_to(ROOT)
    lines = text.count("\n")
    if lines > MAX_LINES:
        problems.append(f"{name}: {lines} lines, limit {MAX_LINES}; split it")
    if path.parent.name in SCOPED and not text.startswith("---\npaths:\n"):
        problems.append(f"{name}: no `paths:` filter, so it would load in every session")
    if path.parent.name in ALWAYS and text.startswith("---\npaths:"):
        problems.append(f"{name}: core and process rules must load always, remove `paths:`")
    for match in SHOUTING.finditer(text):
        problems.append(f"{name}: ALL CAPS '{match.group()}'; say it plainly and give the why")

always_chars = sum(len(p.read_text()) for p in rules(ALWAYS))
if always_chars > ALWAYS_BUDGET_CHARS:
    problems.append(
        f"core/ + process/ is {always_chars} characters (~{always_chars // 4} tokens), "
        f"budget {ALWAYS_BUDGET_CHARS}; move detail to a scoped file or a skill"
    )

link = re.compile(r"\]\(([^)#:]+?)(#[^)]*)?\)")
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for target, _ in link.findall(path.read_text()):
        if target.startswith("~"):
            target = target.replace("~/projects/agentic-coding-base", str(ROOT), 1)
            resolved = pathlib.Path(target)
        else:
            resolved = path.parent / target
        if not resolved.exists():
            problems.append(f"{path.relative_to(ROOT)}: broken link {target}")

private = ROOT / ".private-words"
if private.exists():
    words = [w.strip() for w in private.read_text().splitlines() if w.strip() and not w.startswith("#")]
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path != private:
            text = path.read_text(errors="ignore").lower()
            for word in words:
                if word.lower() in text:
                    problems.append(f"{path.relative_to(ROOT)}: private word '{word}'")

print(f"always loaded: {always_chars} characters, about {always_chars // 4} tokens")
for problem in problems:
    print("FAIL", problem)
print("ok" if not problems else f"{len(problems)} problem(s)")
sys.exit(1 if problems else 0)
