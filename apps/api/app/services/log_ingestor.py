"""Ingest auth and nginx logs for replay."""

from __future__ import annotations

import re
from pathlib import Path

AUTH_FAILED = re.compile(r"(?P<ts>\w+\s+\d+\s+[\d:]+).*Failed password for(?: invalid user)? (?P<user>\S+) from (?P<ip>[\d.]+)")
AUTH_OK = re.compile(r"(?P<ts>\w+\s+\d+\s+[\d:]+).*Accepted password for (?P<user>\S+) from (?P<ip>[\d.]+)")
NGINX = re.compile(r'(?P<ip>[\d.]+) \S+ \S+ \[(?P<ts>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) (?P<proto>[^"]+)" (?P<status>\d+) (?P<size>\S+) "(?P<ref>[^"]*)" "(?P<ua>[^"]*)"')

def ingest_file(path: Path) -> list[dict]:
    text = path.read_text(encoding='utf-8', errors='replace')
    events: list[dict] = []
    for line in text.splitlines():
        if m := AUTH_FAILED.search(line):
            events.append({'source': 'auth', 'event_type': 'login_failed', 'timestamp': m.group('ts'), 'ip': m.group('ip'), 'user': m.group('user'), 'raw': line})
        elif m := AUTH_OK.search(line):
            events.append({'source': 'auth', 'event_type': 'login_success', 'timestamp': m.group('ts'), 'ip': m.group('ip'), 'user': m.group('user'), 'raw': line})
        elif m := NGINX.match(line):
            events.append({'source': 'nginx', 'event_type': 'http_request', 'timestamp': m.group('ts'), 'ip': m.group('ip'), 'method': m.group('method'), 'path': m.group('path'), 'status': int(m.group('status')), 'user_agent': m.group('ua'), 'raw': line})
    return events

def ingest_files(paths: list[Path]) -> list[dict]:
    events: list[dict] = []
    for path in paths:
        events.extend(ingest_file(path))
    return events
