# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic log replay, attack path mapping, summary output, triage output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add timestamp normalization and parser error handling.
- Add tests for malformed logs and empty input.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling uploaded incident logs.
- Run dependency and secret scans before release.
- Add retention and redaction controls for real incident data.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports include replay risk, attack path scoring, and analyst triage guidance.
