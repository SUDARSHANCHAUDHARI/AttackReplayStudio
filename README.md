# AttackReplay Studio

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Visual incident replay dashboard that turns safe sample logs into an attack timeline, path view, and incident summary.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/AttackReplayStudio
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/AttackReplayStudio`

## MVP Snapshot

This repository includes a working MVP with safe sample logs, deterministic replay logic, timeline output, attack path risk scoring, summary JSON, triage checklist, tests, and Docker demo support.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- log timeline
- IP activity map
- login attempts
- request path view
- incident replay
- AI summary
- IP risk scoring
- MITRE-style tactic labels
- triage checklist

## Suggested Stack

FastAPI, React, GeoIP data, Docker.

## Status

Working CLI MVP.


## Install

```bash
pip install .
```

This registers the `attack-replay-studio` command. Or run directly:

```bash
python3 main.py --help
```

## Quick Start

Replay the included safe sample logs:

```bash
python3 -m apps.api.app.cli \
  data/samples/auth.log \
  data/samples/nginx-access.log \
  --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Generated outputs:

- `data/reports/events.json`
- `data/reports/timeline.json`
- `data/reports/attack_paths.json`
- `data/reports/geoip.json`
- `data/reports/summary.json`
- `data/reports/report.md`
- `data/reports/triage.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Ingests Linux auth logs and nginx access logs.
- Builds a chronological incident timeline.
- Groups events into attack paths by source IP.
- Adds deterministic GeoIP-style enrichment for demo IPs.
- Generates JSON events, JSON timeline, JSON attack paths, JSON IP map, and a Markdown incident report.
- Adds IP path risk scoring, tactic labels, summary JSON, priority queue, and triage checklist.

## Roadmap

- Add timestamp normalization across log formats
- Add richer attack-stage classification
- Add visual replay dashboard
- Add importers for firewall and EDR logs
- Add case export bundle
