"""Build attack timelines."""

from __future__ import annotations

SEVERITY = {'login_success': 'high', 'login_failed': 'medium', 'http_request': 'low'}

def build_timeline(events: list[dict]) -> list[dict]:
    timeline = []
    for idx, event in enumerate(events, start=1):
        label = event.get('event_type', 'event')
        if event.get('path'):
            label += f" {event['path']}"
        if event.get('user'):
            label += f" user={event['user']}"
        timeline.append({'step': idx, 'timestamp': event.get('timestamp'), 'ip': event.get('ip'), 'event_type': event.get('event_type'), 'severity': SEVERITY.get(event.get('event_type'), 'low'), 'label': label, 'event': event})
    return timeline
