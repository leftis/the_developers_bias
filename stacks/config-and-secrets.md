---
paths:
  - "**/*.env"
  - "**/*.env.example"
  - "**/docker-compose*.yml"
  - "**/Makefile"
---

# Config, env files and Docker Compose

## One settings file, read literally

- Keep one `name.env` file that every tool reads: the service, helper apps, `make run`, compose.
- Read it **literally**, the way `docker run --env-file` does: `KEY=value` per line, no quote removal,
  no `$` expansion, `#` comments and blank lines skipped. Passwords with `$`, `"` or `'` then work
  everywhere.
- Don't load it with `set -a; . ./file` or `export $(grep ... | xargs)`: both mangle quotes and
  expand `$`. In a Makefile, use a read loop:

  ```make
  run:
  	@while IFS= read -r line; do \
  		case "$$line" in ''|'#'*) ;; *) export "$$line" ;; esac; \
  	 done < app.env; ./target/release/app
  ```

- In Compose, use `env_file` with `format: raw` for the same literal reading.
- Settings come in through env vars with clap-style `env =` defaults, and every one is listed in a
  table (name, default, meaning).

## Compose traps

- Any `environment:` entry **overrides** `env_file`, even when the shell variable it reads is
  unset (it becomes empty). To let people type a secret in instead of storing it, put that
  `environment:` entry in a separate override file (`docker-compose.secret.yml`) that's added only
  when needed:

  ```bash
  docker compose -f docker-compose.yml -f docker-compose.secret.yml up -d
  ```

- Edits to the env file take effect only when containers are **recreated**
  (`up -d --force-recreate`). `restart` keeps the old settings.
- Put optional extras (Prometheus, Grafana) behind a `profiles:` entry so the default start stays
  small.
- Bind admin UIs to `127.0.0.1`, not all interfaces.

## Typing a secret in instead of storing it

```fish
read -s -x -P "Secret URL: " SERVICE_URL
```

```bash
read -rs -p "Secret URL: " SERVICE_URL && export SERVICE_URL
```

It's then in no file and not in shell history.
