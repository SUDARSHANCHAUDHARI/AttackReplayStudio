# AttackReplay Studio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Visual incident replay dashboard that turns safe sample logs into an attack timeline, attack path view, GeoIP map, and incident summary.

---

## Overview

AttackReplay Studio is a defensive analysis tool for security teams to replay logs as a structured incident. It ingests Linux auth logs and nginx access logs, builds a chronological timeline, groups events into attack paths per source IP, scores risk, applies MITRE-style tactic labels, and emits both JSON and Markdown reports for triage.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Log ingestion for Linux auth logs and nginx access logs
- Chronological incident timeline
- Attack path grouping per source IP
- Deterministic GeoIP-style enrichment for demo IPs
- IP path risk scoring with priority queue
- MITRE-style tactic labels per event
- Markdown incident report and triage checklist
- JSON outputs for events, timeline, attack paths, and summary

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/AttackReplayStudio.git
cd AttackReplayStudio
pip install .
```

This registers the `attack-replay-studio` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Replay the included safe sample logs:

```bash
python3 main.py \
  data/samples/auth.log \
  data/samples/nginx-access.log \
  --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `events.json` — parsed event list
- `timeline.json` — chronological incident timeline
- `attack_paths.json` — per-IP attack paths with risk score
- `geoip.json` — IP enrichment map
- `summary.json` — counts and highest risk IP
- `report.md` — full Markdown incident report
- `triage.md` — analyst triage checklist

## Project Structure

```
AttackReplayStudio/
├── apps/
│   ├── api/       FastAPI app scaffold (planned)
│   └── web/       React/Next.js app scaffold (planned)
├── data/
│   ├── samples/   Safe sample logs for replay
│   └── reports/   Example generated output
├── docker/        Dockerfile + compose support
├── docs/          Architecture, security, and demo notes
├── scripts/       Setup, seed, and run helpers
├── tests/         Unit and integration tests
├── main.py        CLI entrypoint
├── pyproject.toml Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, and lab environments you own or have explicit written permission to assess. The included sample data is synthetic and safe for public demo use.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Timestamp normalization across log formats
- Richer attack-stage classification
- Visual replay dashboard (FastAPI + React)
- Importers for firewall and EDR logs
- Case export bundle

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/AttackReplayStudio/issues).
