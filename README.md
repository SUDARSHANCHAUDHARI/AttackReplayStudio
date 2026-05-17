# AttackReplay Studio

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Visual incident replay dashboard that turns safe sample logs into an attack timeline, path view, and incident summary.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/AttackReplayStudio
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/AttackReplayStudio`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
