# Security Notes

AttackReplay Studio is defensive and analysis-focused.

## Safe Use

- Use only logs from systems you own or have permission to assess.
- Do not commit real customer logs, private IP inventories, tokens, session IDs, or sensitive incident data.
- Treat generated reports as sensitive because they can describe attack paths and visibility gaps.

## Current Boundary

The MVP uses safe local sample logs and deterministic GeoIP fixtures. It does not query external services.

## Before Production

- Add redaction for usernames, paths, query strings, and private addresses.
- Add upload limits and retention controls.
- Add authentication and authorization.
- Add audit logging for replay exports.
