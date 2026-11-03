---
paths:
  - "analysis/**"
  - "**/*.py"
  - "**/*.ipynb"
  - "**/*.duckdb"
  - "**/pyproject.toml"
---

# Data analysis

- Work like a data scientist: question, data, method, result, limits.
- Python for analysis (Rust when speed needs it). Run scripts with `uv run`.
- Store observations in **DuckDB**, not loose CSVs.
- Number the scripts in an `analysis/` folder (`01_load.py`, `02_features.py`, ...) so the pipeline
  reads top to bottom and can be re-run.
- Make charts you can show to people: titled, labelled axes and units, readable in light and dark.
- Evaluate honestly: leave-one-day-out (or leave-one-group-out) validation, and report MAE plus a
  tail number (P90). Say how much data and how many days it rests on.
- Keep raw data outside git. Note where it lives (bucket, region, profile) in the project's notes.
- Before training on a new dataset version, check what changed in the source format and say which
  fields are new.
