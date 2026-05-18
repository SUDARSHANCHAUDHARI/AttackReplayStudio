"""CLI for AttackReplay Studio MVP."""

from __future__ import annotations

import argparse, json
from pathlib import Path

from apps.api.app.services.ai_incident_summary import summarize_incident
from apps.api.app.services.attack_path_mapper import map_attack_paths
from apps.api.app.services.geoip_lookup import enrich_ips
from apps.api.app.services.log_ingestor import ingest_files
from apps.api.app.services.timeline_builder import build_timeline

def summarize_replay(timeline: list[dict], paths: list[dict]) -> dict:
    severity_counts: dict[str, int] = {}
    tactic_counts: dict[str, int] = {}
    for item in timeline:
        severity_counts[item['severity']] = severity_counts.get(item['severity'], 0) + 1
        tactic_counts[item['tactic']] = tactic_counts.get(item['tactic'], 0) + 1
    highest = max((path['risk_score'] for path in paths), default=0)
    return {
        'events': len(timeline),
        'source_ips': len(paths),
        'highest_ip_risk': highest,
        'risk_level': 'high' if highest >= 70 else 'medium' if highest >= 35 else 'low',
        'severity_counts': severity_counts,
        'tactic_counts': tactic_counts,
        'top_ip': paths[0] if paths else None,
    }

def build_report(summary: str, timeline: list[dict], paths: list[dict], geo: dict) -> str:
    replay_summary = summarize_replay(timeline, paths)
    lines = [
        '# AttackReplay Studio Report',
        '',
        summary,
        '',
        f"- Events: {replay_summary['events']}",
        f"- Source IPs: {replay_summary['source_ips']}",
        f"- Replay risk level: {replay_summary['risk_level']}",
        f"- Highest IP risk: {replay_summary['highest_ip_risk']}/100",
        '',
        '## Priority Queue',
        '',
    ]
    for path in paths:
        lines.append(f"- `{path['ip']}` {path['risk_level']} risk ({path['risk_score']}/100): {' -> '.join(path['stages'])}")
    lines.extend(['', '## Timeline', ''])
    for item in timeline:
        lines.append(f"- {item['step']}. `{item['severity']}` {item['timestamp']} {item['ip']} {item['label']} ({item['tactic']})")
    lines.extend(['', '## Attack Paths', ''])
    for path in paths:
        lines.append(f"- `{path['ip']}` {path['event_count']} event(s), {path['risk_level']} risk: {' -> '.join(path['stages'])}")
    lines.extend(['', '## IP Map', ''])
    for ip, details in geo.items():
        lines.append(f"- `{ip}`: {details['city']}, {details['country']}")
    return '\n'.join(lines) + '\n'

def build_triage_report(timeline: list[dict], paths: list[dict]) -> str:
    lines = ['# AttackReplay Studio Triage', '', '## Analyst Checklist', '']
    if not paths:
        lines.append('No attack paths require triage.')
    for path in paths:
        if path['risk_level'] in {'high', 'medium'}:
            lines.append(f"- [ ] Review `{path['ip']}` path: {' -> '.join(path['stages'])}")
            if path['suspicious_paths']:
                lines.append(f"  - Suspicious paths: {', '.join(path['suspicious_paths'])}")
    lines.extend(['', '## High Severity Events', ''])
    high = [item for item in timeline if item['severity'] == 'high']
    if not high:
        lines.append('No high severity events were detected.')
    for item in high:
        lines.append(f"- `{item['timestamp']}` `{item['ip']}` {item['label']}")
    return '\n'.join(lines).rstrip() + '\n'

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
    replay_summary = summarize_replay(timeline, paths)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in {'events': events, 'timeline': timeline, 'attack_paths': paths, 'geoip': geo, 'summary': replay_summary}.items():
        (args.out_dir / f'{name}.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    (args.out_dir / 'report.md').write_text(build_report(summary, timeline, paths, geo), encoding='utf-8')
    (args.out_dir / 'triage.md').write_text(build_triage_report(timeline, paths), encoding='utf-8')
    print(f'Replayed {len(timeline)} event(s)')

if __name__ == '__main__':
    main()
