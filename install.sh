#!/usr/bin/env bash
# Installs The Developer's Bias into ~/.claude/rules/developers-bias/, and merges
# settings/settings.json into ~/.claude/settings.json (other keys are kept).
#
# Claude Code loads ~/.claude/rules/ in every project with no approval prompt. core/ and process/
# load in every session; stacks/ and platforms/ carry `paths:` filters, so they load only when an
# agent reads or edits matching files.
#
# Files are copied, not linked: links pointing outside ~/.claude may need approval per project.
# Re-run after every change to this repo. --dry-run shows what would change.
set -euo pipefail

src="$(cd "$(dirname "$0")" && pwd)"
dest="${CLAUDE_RULES_DIR:-$HOME/.claude/rules}/developers-bias"
dry=""
if [[ "${1:-}" == "--dry-run" ]]; then dry="--dry-run"; fi

python3 "$src/scripts/check.py" > /dev/null || { python3 "$src/scripts/check.py"; exit 1; }

mkdir -p "$dest"
for dir in core process stacks platforms; do
  rsync -a --delete --itemize-changes $dry "$src/$dir/" "$dest/$dir/"
done

# Claude Code's own prompt tells it to add a Co-Authored-By trailer; that beats the rule text
# (evals/commit-no-ai-trailer failed with the rules on). The attribution setting turns it off.
python3 "$src/scripts/merge_settings.py" "${CLAUDE_SETTINGS_FILE:-$HOME/.claude/settings.json}" $dry

if [[ -z "$dry" ]]; then
  echo "Installed to $dest"
  echo "Always loaded: $(cat "$dest"/core/*.md "$dest"/process/*.md | wc -l | tr -d ' ') lines"
fi
