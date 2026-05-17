"""Deterministic GeoIP-style enrichment for sample/demo IPs."""

from __future__ import annotations

GEO = {
    '198.51.100.22': {'country': 'ExampleNet', 'city': 'Scanner City'},
    '203.0.113.10': {'country': 'ExampleOrg', 'city': 'Admin Town'},
    '192.0.2.45': {'country': 'ExampleLab', 'city': 'Payload Bay'},
}

def enrich_ips(events: list[dict]) -> dict[str, dict]:
    ips = sorted({str(e.get('ip')) for e in events if e.get('ip')})
    return {ip: GEO.get(ip, {'country': 'Unknown', 'city': 'Unknown'}) for ip in ips}
