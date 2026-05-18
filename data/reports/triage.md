# AttackReplay Studio Triage

## Analyst Checklist

- [ ] Review `198.51.100.22` path: login_failed -> login_failed -> http_request
  - Suspicious paths: /.env
- [ ] Review `203.0.113.10` path: login_success

## High Severity Events

- `May 17 10:05:17` `203.0.113.10` login_success user=kiosk
