# Architecture

AttackReplay Studio is a defensive incident replay MVP for turning safe logs into an attack narrative.

## Flow

1. `log_ingestor.py` parses auth and nginx sample logs.
2. `timeline_builder.py` creates ordered replay events with severity and tactic metadata.
3. `attack_path_mapper.py` groups events by source IP and scores attack paths.
4. `geoip_lookup.py` adds deterministic demo GeoIP metadata.
5. `ai_incident_summary.py` creates a plain-English summary.
6. `cli.py` writes JSON, Markdown report, and triage outputs.

## Outputs

- raw parsed events
- timeline JSON
- attack path JSON
- GeoIP-style map JSON
- replay summary JSON
- Markdown report
- Markdown triage checklist

The MVP uses local safe sample logs only.
