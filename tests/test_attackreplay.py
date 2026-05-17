"""Tests for AttackReplay Studio MVP."""

from __future__ import annotations

import json, subprocess, sys, tempfile, unittest
from pathlib import Path

from apps.api.app.services.attack_path_mapper import map_attack_paths
from apps.api.app.services.log_ingestor import ingest_files
from apps.api.app.services.timeline_builder import build_timeline

ROOT = Path(__file__).resolve().parents[1]
LOGS = [ROOT / 'data/samples/auth.log', ROOT / 'data/samples/nginx-access.log']

class AttackReplayTests(unittest.TestCase):
    def test_builds_timeline_and_paths(self) -> None:
        events = ingest_files(LOGS)
        timeline = build_timeline(events)
        paths = map_attack_paths(events)
        self.assertEqual(len(events), 5)
        self.assertEqual(len(timeline), 5)
        self.assertEqual(paths[0]['ip'], '198.51.100.22')

    def test_cli_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, '-m', 'apps.api.app.cli', *map(str, LOGS), '--out-dir', tmp], cwd=ROOT, check=True, capture_output=True, text=True)
            timeline = json.loads(Path(tmp, 'timeline.json').read_text(encoding='utf-8'))
            report = Path(tmp, 'report.md').read_text(encoding='utf-8')
            self.assertIn('Replayed 5 event', result.stdout)
            self.assertEqual(len(timeline), 5)
            self.assertIn('AttackReplay Studio Report', report)

if __name__ == '__main__':
    unittest.main()
