"""Map attack paths by source IP."""

from __future__ import annotations

from collections import defaultdict

def map_attack_paths(events: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for event in events:
        if event.get('ip'):
            grouped[str(event['ip'])].append(event)
    paths = []
    for ip, ip_events in grouped.items():
        stages = [event['event_type'] for event in ip_events]
        paths.append({'ip': ip, 'event_count': len(ip_events), 'stages': stages, 'paths': [event.get('path') for event in ip_events if event.get('path')]})
    return sorted(paths, key=lambda item: item['event_count'], reverse=True)
