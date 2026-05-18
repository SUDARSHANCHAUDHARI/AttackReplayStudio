"""Map attack paths by source IP."""

from __future__ import annotations

from collections import defaultdict

POINTS = {'high': 40, 'medium': 20, 'low': 5}

def map_attack_paths(events: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for event in events:
        if event.get('ip'):
            grouped[str(event['ip'])].append(event)
    paths = []
    for ip, ip_events in grouped.items():
        stages = [event['event_type'] for event in ip_events]
        score = 0
        if stages.count('login_failed') >= 2:
            score += 35
        if 'login_success' in stages:
            score += 40
        suspicious_paths = [event.get('path') for event in ip_events if event.get('path') in {'/.env', '/admin'} or 'union' in str(event.get('path', '')).lower()]
        score += 15 * len(suspicious_paths)
        paths.append({
            'ip': ip,
            'event_count': len(ip_events),
            'stages': stages,
            'paths': [event.get('path') for event in ip_events if event.get('path')],
            'suspicious_paths': suspicious_paths,
            'risk_score': min(100, score),
            'risk_level': 'high' if score >= 70 else 'medium' if score >= 35 else 'low',
        })
    return sorted(paths, key=lambda item: (item['risk_score'], item['event_count']), reverse=True)
