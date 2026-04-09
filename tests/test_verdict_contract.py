import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class VerdictContractTest(unittest.TestCase):
    def test_public_verdict_json_loads(self):
        payload = json.loads((ROOT / "public" / "verdict.json").read_text(encoding="utf-8"))
        self.assertEqual(
            sorted(payload.keys()),
            [
                "contradictions",
                "execution_ref",
                "generated_at",
                "law_ref",
                "proof_ref",
                "reason_codes",
                "state_ref",
                "verdict",
                "verifier_version",
            ],
        )

    def test_fixture_verdict_uses_pinned_law(self):
        payload = json.loads((ROOT / "fixtures" / "verdict" / "minimal-verdict.json").read_text(encoding="utf-8"))
        self.assertTrue(payload["law_ref"].startswith("SYNTAGMARIUM@"))
        self.assertIn(payload["verdict"], {"PASS", "FAIL", "INDETERMINATE", "CONTRADICTED"})

if __name__ == "__main__":
    unittest.main()
