---
paths:
  - "observability/**"
  - "**/prometheus*.yml"
  - "**/alerts*.yml"
  - "**/grafana/**"
  - "**/metrics.*"
  - "**/observe.*"
---

# Observability

## Metrics that answer real questions

Expose `/metrics` (Prometheus) from the service itself. Count what a person would ask about:

- Input: messages read / unreadable / skipped as old, and the time of the last one.
- Decisions: items handled per outcome (handled, not covered, missing data), with unknown keys
  labelled (for example a value the service has no rule for).
- Output: messages published per type and event.
- Quality: how early the output arrives before it's needed, and how late its inputs arrive.
- Health: broker connected (0/1), disconnects, items in memory, version info of loaded data or models, reload results.

## Traps

- **Start every counter and histogram at 0** at startup. A series that is *born* with a non-zero
  value makes `increase()` and `rate()` miss the first event after a restart.
- For counters with labels you can't know in advance, catch new series with
  `x unless x offset 1h`, or in a dashboard `x - (x offset 24h or x * 0)`.
- Use percentiles over a window long enough to have data (`[30m]`), not `[5m]`, for low-traffic
  services.
- Test before trusting: replay events and check every alert fires and every panel returns data. Make
  sure the zeros were scraped *before* replaying.

## Alerts

- Down, disconnected, input silent during business hours, unreadable input, unknown keys, items
  with missing data, output too late, reload failing.
- Keep alert rules in the repo with `promtool test rules` tests, and run `promtool check config` in CI.
- Also set alarms on the broker or host side (queue growing, consumers = 0). They still fire when
  your own monitoring is down.

## Dashboards

Provision Grafana from the repo (datasource + dashboard JSON) with anonymous viewer access on
localhost, so `docker compose --profile observability up` shows everything with no clicks.
