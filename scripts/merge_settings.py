#!/usr/bin/env python3
"""Merges settings/settings.json into a Claude settings file, keeping every other key.

Each top-level key in settings/settings.json replaces the target's key as a whole (nested keys
aren't merged); the rest of the target is untouched. A target that isn't a JSON object stops
with a message and is left as it is.
Run: python3 scripts/merge_settings.py <target> [--dry-run]
"""

import json
import pathlib
import sys

SOURCE = pathlib.Path(__file__).resolve().parent.parent / "settings" / "settings.json"


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: merge_settings.py <settings.json> [--dry-run]")
    target = pathlib.Path(sys.argv[1]).expanduser()
    dry = "--dry-run" in sys.argv[2:]
    ours = json.loads(SOURCE.read_text())
    try:
        current = json.loads(target.read_text()) if target.exists() else {}
    except json.JSONDecodeError as err:
        sys.exit(f"settings: {target} is not valid JSON ({err}); fix it, then re-run")
    if not isinstance(current, dict):
        sys.exit(f"settings: {target} is not a JSON object; fix it, then re-run")
    changed = [k for k, v in ours.items() if current.get(k) != v]
    verb = "would set" if dry else "set"
    for key in changed:
        print(f"settings: {verb} {key} {json.dumps(current.get(key))} -> {json.dumps(ours[key])}")
    if changed and not dry:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({**current, **ours}, indent=2, ensure_ascii=False) + "\n")
    if not changed:
        print("settings: already up to date")


if __name__ == "__main__":
    main()
