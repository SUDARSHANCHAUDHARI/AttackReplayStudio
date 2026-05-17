"""Build deterministic incident summaries."""

from __future__ import annotations

def summarize_incident(timeline: list[dict], attack_paths: list[dict]) -> str:
    if not timeline:
        return 'No events were available for replay.'
    top = attack_paths[0] if attack_paths else {'ip': 'unknown', 'event_count': 0}
    success = any(item.get('event_type') == 'login_success' for item in timeline)
    result = f"AttackReplay reconstructed {len(timeline)} event(s). Most active IP: {top['ip']} with {top['event_count']} event(s)."
    if success:
        result += ' At least one successful login occurred after suspicious activity and should be investigated.'
    return result
