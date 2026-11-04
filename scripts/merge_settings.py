#!/usr/bin/env python3
"""Merges settings/settings.json into a Claude settings file, keeping every other key.

Only the top-level keys in settings/settings.json are set; the rest of the target is untouched.
Run: python3 scripts/merge_settings.py <target> [--dry-run]
"""

import json
import pathlib
import sys

SOURCE = pathlib.Path(__file__).resolve().parent.parent / "settings" / "settings.json"


def main():
    target = pathlib.Path(sys.argv[1]).expanduser()
    dry = "--dry-run" in sys.argv[2:]
    ours = json.loads(SOURCE.read_text())
    current = json.loads(target.read_text()) if target.exists() else {}
    changed = [k for k, v in ours.items() if current.get(k) != v]
    for key in changed:
        print(f"settings: {key} {json.dumps(current.get(key))} -> {json.dumps(ours[key])}")
    if changed and not dry:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({**current, **ours}, indent=2) + "\n")
    if not changed:
        print("settings: already up to date")


if __name__ == "__main__":
    main()
