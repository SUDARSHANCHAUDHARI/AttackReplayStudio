# AttackReplay Studio Report

AttackReplay reconstructed 5 event(s). Most active IP: 198.51.100.22 with 3 event(s). At least one successful login occurred after suspicious activity and should be investigated.

## Timeline

- 1. `medium` May 17 10:00:01 198.51.100.22 login_failed user=admin
- 2. `medium` May 17 10:00:04 198.51.100.22 login_failed user=root
- 3. `high` May 17 10:05:17 203.0.113.10 login_success user=kiosk
- 4. `low` 17/May/2026:10:06:01 +0000 198.51.100.22 http_request /.env
- 5. `low` 17/May/2026:10:07:11 +0000 192.0.2.45 http_request /search?q=union%20select

## Attack Paths

- `198.51.100.22` 3 event(s): login_failed -> login_failed -> http_request
- `203.0.113.10` 1 event(s): login_success
- `192.0.2.45` 1 event(s): http_request

## IP Map

- `192.0.2.45`: Payload Bay, ExampleLab
- `198.51.100.22`: Scanner City, ExampleNet
- `203.0.113.10`: Admin Town, ExampleOrg
