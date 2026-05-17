# AttackReplay Studio

**Goal:** Visual incident replay dashboard.

**MVP:** Upload logs, generate attack timeline.

## Core Features

- log timeline
- IP activity map
- login attempts
- request path view
- incident replay
- AI summary

## Suggested Stack

FastAPI, React, GeoIP data, Docker.

## Status

Working CLI MVP.

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

## MVP Capabilities

- Ingests Linux auth logs and nginx access logs.
- Builds a chronological incident timeline.
- Groups events into attack paths by source IP.
- Adds deterministic GeoIP-style enrichment for demo IPs.
- Generates JSON events, JSON timeline, JSON attack paths, JSON IP map, and a Markdown incident report.

## Repository Status

This repository contains the production-ready foundation for the AttackReplay Studio MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
