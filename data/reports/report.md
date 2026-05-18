# AttackReplay Studio Report

AttackReplay reconstructed 5 event(s). Most active IP: 198.51.100.22 with 3 event(s). At least one successful login occurred after suspicious activity and should be investigated.

- Events: 5
- Source IPs: 3
- Replay risk level: medium
- Highest IP risk: 50/100

## Priority Queue

- `198.51.100.22` medium risk (50/100): login_failed -> login_failed -> http_request
- `203.0.113.10` medium risk (40/100): login_success
- `192.0.2.45` low risk (15/100): http_request

## Timeline

- 1. `medium` May 17 10:00:01 198.51.100.22 login_failed user=admin (Credential Access)
- 2. `medium` May 17 10:00:04 198.51.100.22 login_failed user=root (Credential Access)
- 3. `high` May 17 10:05:17 203.0.113.10 login_success user=kiosk (Credential Access)
- 4. `medium` 17/May/2026:10:06:01 +0000 198.51.100.22 http_request /.env (Reconnaissance)
- 5. `medium` 17/May/2026:10:07:11 +0000 192.0.2.45 http_request /search?q=union%20select (Reconnaissance)

## Attack Paths

- `198.51.100.22` 3 event(s), medium risk: login_failed -> login_failed -> http_request
- `203.0.113.10` 1 event(s), medium risk: login_success
- `192.0.2.45` 1 event(s), low risk: http_request

## IP Map

- `192.0.2.45`: Payload Bay, ExampleLab
- `198.51.100.22`: Scanner City, ExampleNet
- `203.0.113.10`: Admin Town, ExampleOrg
