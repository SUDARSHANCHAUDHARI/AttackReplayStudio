"""CLI for AttackReplay Studio MVP."""

from __future__ import annotations

import argparse, json
from pathlib import Path

from apps.api.app.services.ai_incident_summary import summarize_incident
from apps.api.app.services.attack_path_mapper import map_attack_paths
from apps.api.app.services.geoip_lookup import enrich_ips
from apps.api.app.services.log_ingestor import ingest_files
from apps.api.app.services.timeline_builder import build_timeline

def build_report(summary: str, timeline: list[dict], paths: list[dict], geo: dict) -> str:
    lines = ['# AttackReplay Studio Report', '', summary, '', '## Timeline', '']
    for item in timeline:
        lines.append(f"- {item['step']}. `{item['severity']}` {item['timestamp']} {item['ip']} {item['label']}")
    lines.extend(['', '## Attack Paths', ''])
    for path in paths:
        lines.append(f"- `{path['ip']}` {path['event_count']} event(s): {' -> '.join(path['stages'])}")
    lines.extend(['', '## IP Map', ''])
    for ip, details in geo.items():
        lines.append(f"- `{ip}`: {details['city']}, {details['country']}")
    return '\n'.join(lines) + '\n'

def main() -> None:
    parser = argparse.ArgumentParser(description='AttackReplay Studio log replay')
    parser.add_argument('logs', nargs='+', type=Path)
    parser.add_argument('--out-dir', type=Path, default=Path('data/reports'))
    args = parser.parse_args()
    events = ingest_files(args.logs)
    timeline = build_timeline(events)
    paths = map_attack_paths(events)
    geo = enrich_ips(events)
    summary = summarize_incident(timeline, paths)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in {'events': events, 'timeline': timeline, 'attack_paths': paths, 'geoip': geo}.items():
        (args.out_dir / f'{name}.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    (args.out_dir / 'report.md').write_text(build_report(summary, timeline, paths, geo), encoding='utf-8')
    print(f'Replayed {len(timeline)} event(s)')

if __name__ == '__main__':
    main()
