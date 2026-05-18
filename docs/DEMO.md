# Demo

## Local CLI

```bash
python3 -m apps.api.app.cli \
  data/samples/auth.log \
  data/samples/nginx-access.log \
  --out-dir data/reports
```

Expected terminal output:

```text
Replayed 5 event(s)
```

## Review Outputs

```bash
cat data/reports/report.md
cat data/reports/triage.md
cat data/reports/summary.json
```

## Docker CLI

```bash
docker compose run --rm api
```
