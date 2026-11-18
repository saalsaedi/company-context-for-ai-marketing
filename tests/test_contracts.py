"""Contract and boundary tests; synthetic data only, no live-platform claims."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_context import validate, schema_validator, schema_errors
from export_context import project, export
from build_package import build, collect, check_links

AS_OF = "2026-11-14"


class ContextContracts(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "tests/fixtures/idea-company.json").read_text(encoding="utf-8"))

    def invalid(self, fragment=None):
        result = validate(self.data, AS_OF)
        self.assertFalse(result["valid"], result)
        if fragment:
            self.assertTrue(any(fragment in e for e in result["errors"]), result)
        return result

    def test_all_schema_definitions_are_valid(self):
        for path in (ROOT / "schemas").glob("*.json"):
            validator = schema_validator(path.name)
            validator.check_schema(validator.schema)

    def test_idea_company_accepts_honest_unknowns(self):
        self.assertTrue(validate(self.data, AS_OF)["valid"])

    def test_fact_without_evidence_is_rejected(self):
        self.data["records"][7]["source_ids"] = []
        self.invalid()

    def test_fact_requires_verified_date(self):
        self.data["records"][7]["verified_at"] = None
        self.invalid()

    def test_founder_attestation_cannot_verify_market_claim(self):
        self.data["records"][7]["scope"]["basis"] = "external"
        self.invalid("external fact")

    def test_unapproved_founder_decision_is_rejected(self):
        self.data["records"][0]["review"]["status"] = "pending"
        self.invalid()

    def test_approved_hypothesis_stays_hypothesis_and_input_unchanged(self):
        before = copy.deepcopy(self.data)
        self.assertTrue(validate(self.data, AS_OF)["valid"])
        self.assertEqual(self.data, before)
        self.assertEqual(self.data["records"][1]["kind"], "hypothesis")

    def test_unknown_cannot_be_silently_coerced_to_zero(self):
        self.data["records"][3]["value"] = 0
        self.invalid()

    def test_planned_feature_cannot_be_confirmed_fact(self):
        r = self.data["records"][2]
        r.update(kind="confirmed_fact", verification_method="founder_attested", verified_at=AS_OF)
        self.invalid()

    def test_invalid_calendar_date_is_rejected(self):
        self.data["records"][7]["verified_at"] = "2026-02-30"
        self.invalid()

    def test_future_verification_is_rejected(self):
        self.data["records"][7]["verified_at"] = "2026-11-15"
        self.invalid("future")

    def test_missing_source_reference_is_rejected(self):
        self.data["records"][0]["source_ids"] = ["S-missing"]
        self.invalid("missing source")

    def test_cross_company_contamination_is_rejected(self):
        self.data["records"][0]["company_id"] = "C-another"
        self.invalid("company_id mismatch")

    def test_duplicate_record_id_is_rejected(self):
        self.data["records"].append(copy.deepcopy(self.data["records"][0]))
        self.invalid("duplicate IDs")

    def test_duplicate_stage_cannot_hide_missing_stage(self):
        self.data["state"]["stages"][1] = copy.deepcopy(self.data["state"]["stages"][0])
        self.invalid("stages")

    def test_unsupported_schema_version_is_rejected(self):
        self.data["schema_version"] = "2.0.0"
        self.invalid()

    def test_missing_domain_blocks_release(self):
        self.data["records"].pop(8)
        self.invalid("missing domain")

    def test_critical_gap_blocks_release_even_if_deferred(self):
        self.data["state"]["gaps"][0].update(type="critical", status="deferred")
        self.invalid("blocking gap")

    def test_release_requires_approval(self):
        self.data["state"]["release_review"]["status"] = "pending"
        self.invalid("explicit review")

    def test_ready_cannot_hide_research_caveats(self):
        self.data["state"]["readiness"] = "ready"
        self.invalid("warnings")

    def test_stale_base_is_rejected(self):
        self.data["state"].update(mode="update", base_version="0.9.0")
        result = validate(self.data, AS_OF, expected_base="1.0.0")
        self.assertFalse(result["valid"])
        self.assertTrue(any("stale" in e for e in result["errors"]))

    def test_update_requires_new_version(self):
        self.data["state"].update(mode="update", base_version="1.0.0")
        self.invalid("must differ")

    def test_supersession_preserves_old_record(self):
        old = self.data["records"][1]
        old["lifecycle"] = "superseded"
        new = copy.deepcopy(old)
        new.update(id="R-011", lifecycle="active", supersedes=[old["id"]], value="Annual hypothesis")
        self.data["records"].append(new)
        self.assertTrue(validate(self.data, AS_OF)["valid"])
        self.assertEqual(old["value"], "Monthly subscription hypothesis")

    def test_supersession_cannot_leave_replaced_record_active(self):
        new = copy.deepcopy(self.data["records"][1])
        new.update(id="R-011", supersedes=["R-002"])
        self.data["records"].append(new)
        self.invalid("lifecycle=superseded")

    def test_supersession_cycle_is_rejected(self):
        first = self.data["records"][1]
        first.update(lifecycle="superseded", supersedes=["R-011"])
        second = copy.deepcopy(first)
        second.update(id="R-011", supersedes=["R-002"])
        self.data["records"].append(second)
        self.invalid("cycle")

    def test_same_subject_scope_conflict_is_rejected(self):
        new = copy.deepcopy(self.data["records"][7])
        new.update(id="R-011", value="Three full-time employees")
        self.data["records"].append(new)
        self.invalid("conflicting active value")

    def test_different_periods_are_not_automatically_conflicts(self):
        first = self.data["records"][7]
        first["scope"]["period"] = "2026-10"
        second = copy.deepcopy(first)
        second.update(id="R-011", value="Three people")
        second["scope"]["period"] = "2026-11"
        self.data["records"].append(second)
        self.assertTrue(validate(self.data, AS_OF)["valid"])

    def test_answered_question_needs_provenance(self):
        self.data["state"]["questions"][0]["answer_source_ids"] = []
        self.invalid("answered question")

    def test_public_export_filters_internal_and_private_metadata(self):
        self.data["sources"][0]["locator"] = "private://SOURCE_CANARY"
        self.data["records"][0]["notes"] = "PRIVATE_NOTE_CANARY"
        self.data["records"][7]["statement"] = "INTERNAL_CLAIM_CANARY"
        before = copy.deepcopy(self.data)
        data, omitted = project(self.data, "public", list(self.data["profile"]["domains"]), "Public summary", AS_OF)
        serialized = json.dumps(data)
        for canary in ("SOURCE_CANARY", "PRIVATE_NOTE_CANARY", "INTERNAL_CLAIM_CANARY", "Fictional founder"):
            self.assertNotIn(canary, serialized)
        self.assertIn("R-008", omitted)
        self.assertEqual(self.data, before)

    def test_confidential_export_is_not_enabled_by_ceiling_flag(self):
        with self.assertRaises(ValueError):
            project(self.data, "confidential", ["foundation"], "Share", AS_OF)

    def test_export_excludes_stale_claim(self):
        self.data["records"][0]["next_review_at"] = "2026-11-13"
        data, omitted = project(self.data, "public", ["foundation"], "Summary", AS_OF)
        self.assertEqual(data["records"], [])
        self.assertIn("R-001", omitted)

    def test_export_enforces_domain_scope(self):
        data, _ = project(self.data, "public", ["products_services"], "Product overview", AS_OF)
        self.assertEqual([r["id"] for r in data["records"]], ["R-003"])
        self.assertEqual(data["records"][0]["kind"], "aspiration")

    def test_export_rejects_draft_source(self):
        self.data["state"]["readiness"] = "needs_completion"
        with self.assertRaises(ValueError):
            project(self.data, "public", ["foundation"], "Summary", AS_OF)

    def test_export_manifest_hashes_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "export"
            manifest = export(self.data, out, "public", ["foundation"], "Public summary", AS_OF, "E-demo")
            self.assertFalse(schema_errors(manifest, "export-manifest.schema.json"))
            for a in manifest["artifacts"]:
                self.assertEqual(a["sha256"], hashlib.sha256((out / a["path"]).read_bytes()).hexdigest())
            with self.assertRaises(ValueError):
                export(self.data, out, "public", ["foundation"], "Public summary", AS_OF, "E-demo")

    def test_utf8_roundtrip_preserves_arabic(self):
        text = json.dumps(self.data, ensure_ascii=False)
        self.assertIn("نماء التجريبية", text)
        self.assertEqual(json.loads(text), self.data)

    def test_references_are_resolvable(self):
        check_links(collect())

    def test_build_is_deterministic_and_has_single_skill_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = build(Path(tmp) / "one")
            second = build(Path(tmp) / "two")
            self.assertEqual(first["sha256"], second["sha256"])
            archive = Path(tmp) / "one" / first["archive"]
            with zipfile.ZipFile(archive) as zf:
                names = zf.namelist()
                self.assertIn("ai-company-context-architect/SKILL.md", names)
                self.assertTrue(all(n.startswith("ai-company-context-architect/") for n in names))
                self.assertFalse(any("__pycache__" in n or "company-context/" in n for n in names))
            instructions = (Path(tmp) / "one/chatgpt/project-instructions.txt").read_text(encoding="utf-8")
            self.assertIn("hypothesis", instructions)
            workflow = (Path(tmp) / "one/chatgpt/workflow-reference.txt").read_text(encoding="utf-8")
            self.assertIn("FILE: stages/05-customer-intelligence.md", workflow)

    def test_export_rejects_invalid_id_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "export"
            with self.assertRaises(ValueError):
                export(self.data, out, "public", ["foundation"], "Summary", AS_OF, "../invalid")
            self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()

