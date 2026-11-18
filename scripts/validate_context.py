"""Offline JSON Schema and semantic checks; never certifies factual truth."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry, Resource
except ImportError:
    raise SystemExit("Install the optional local dependency: python -m pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"


def schema_validator(name):
    schemas = [json.loads(p.read_text(encoding="utf-8")) for p in SCHEMA_DIR.glob("*.json")]
    registry = Registry().with_resources((s["$id"], Resource.from_contents(s)) for s in schemas)
    selected = next(s for s in schemas if s["$id"].endswith("/" + name))
    return Draft202012Validator(selected, registry=registry, format_checker=FormatChecker())


def schema_errors(value, name):
    return [
        "schema /" + "/".join(map(str, e.absolute_path)) + ": " + e.message
        for e in sorted(schema_validator(name).iter_errors(value), key=lambda e: str(list(e.absolute_path)))
    ]


def validate(bundle, as_of=None, expected_base=None):
    today = date.fromisoformat(as_of) if isinstance(as_of, str) else (as_of or date.today())
    errors = schema_errors(bundle, "context-bundle.schema.json")
    warnings = []
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}
    profile, state = bundle["profile"], bundle["state"]
    cid = profile["company_id"]
    records, sources = bundle["records"], bundle["sources"]

    def unique(items, label):
        ids = [x["id"] for x in items]
        if len(ids) != len(set(ids)):
            errors.append(label + ": duplicate IDs")
        return {x["id"]: x for x in items}

    by_record = unique(records, "records")
    by_source = unique(sources, "sources")
    unique(state["gaps"], "gaps")
    unique(state["questions"], "questions")
    stages = unique(state["stages"], "stages")
    if set(stages) != {f"{i:02}" for i in range(12)}:
        errors.append("stages: require exactly stages 00 through 11")
    if expected_base is not None and state["base_version"] != expected_base:
        errors.append("base_version: stale or unexpected base; inspect latest stored revision")
    if state["mode"] == "update" and state["base_version"] is None:
        errors.append("update: base_version is required")
    if state["mode"] == "update" and state["base_version"] == profile["context_version"]:
        errors.append("update: candidate version must differ from base_version")

    def stamp(text):
        return datetime.fromisoformat(text.replace("Z", "+00:00"))

    def check_review(review, label):
        if review["at"] and stamp(review["at"]).date() > today:
            errors.append(label + ": review date is in the future")

    if stamp(profile["created_at"]) > stamp(profile["updated_at"]):
        errors.append("profile: created_at is after updated_at")
    for s in sources:
        if s["company_id"] != cid:
            errors.append(s["id"] + ": source company_id mismatch")
        if stamp(s["accessed_at"]).date() > today:
            errors.append(s["id"] + ": accessed_at is in the future")
        if s["published_at"] and date.fromisoformat(s["published_at"]) > stamp(s["accessed_at"]).date():
            warnings.append(s["id"] + ": publication date is after access; review source dating")
    for r in records:
        rid = r["id"]
        if r["company_id"] != cid:
            errors.append(rid + ": record company_id mismatch")
        for sid in r["source_ids"]:
            if sid not in by_source:
                errors.append(rid + ": missing source " + sid)
        for other in r["supersedes"] + r["related_record_ids"]:
            if other not in by_record:
                errors.append(rid + ": missing record reference " + other)
            if other == rid:
                errors.append(rid + ": self reference")
        if stamp(r["created_at"]) > stamp(r["updated_at"]):
            errors.append(rid + ": created_at is after updated_at")
        if stamp(r["updated_at"]).date() > today:
            errors.append(rid + ": updated_at is in the future")
        if r["verified_at"] and date.fromisoformat(r["verified_at"]) > today:
            errors.append(rid + ": verified_at is in the future")
        if r["verified_at"] and r["next_review_at"] and r["next_review_at"] < r["verified_at"]:
            errors.append(rid + ": next_review_at precedes verification")
        if r["lifecycle"] == "active" and r["next_review_at"] and date.fromisoformat(r["next_review_at"]) < today:
            warnings.append(rid + ": review overdue")
        scope = r["scope"]
        if scope["effective_from"] and scope["effective_to"] and scope["effective_from"] > scope["effective_to"]:
            errors.append(rid + ": effective date range is reversed")
        check_review(r["review"], rid)
        linked = [by_source[sid] for sid in r["source_ids"] if sid in by_source]
        if r["kind"] == "confirmed_fact":
            if r["verification_method"] == "founder_attested":
                if scope["basis"] != "internal":
                    errors.append(rid + ": founder attestation cannot establish an external fact")
                if not any(s["type"] == "user_statement" for s in linked):
                    errors.append(rid + ": founder attestation requires a user statement source")
            elif not any(s["type"] != "user_statement" for s in linked):
                errors.append(rid + ": verification requires documentary or observed evidence")
            if scope["basis"] == "external" and not any(s["evidence_class"].startswith("external_") for s in linked):
                errors.append(rid + ": external fact requires external evidence")
        if r["kind"] == "research_evidence" and not any(s["evidence_class"].startswith("external_") for s in linked):
            errors.append(rid + ": research evidence requires an external source")
        for old_id in r["supersedes"]:
            old = by_record.get(old_id)
            if old:
                if old["lifecycle"] != "superseded":
                    errors.append(rid + ": superseded target must have lifecycle=superseded")
                if old["subject_key"] != r["subject_key"] or old["domain"] != r["domain"]:
                    errors.append(rid + ": supersession must preserve subject and domain")
        if r["lifecycle"] == "retracted" and not r["notes"].strip():
            errors.append(rid + ": retraction needs an explanation")

    visited, visiting = set(), set()

    def walk(rid):
        if rid in visiting:
            errors.append("supersession: cycle detected at " + rid)
            return
        if rid in visited:
            return
        visiting.add(rid)
        for old in by_record[rid]["supersedes"]:
            if old in by_record:
                walk(old)
        visiting.remove(rid)
        visited.add(rid)

    for rid in by_record:
        walk(rid)
    active = [r for r in records if r["lifecycle"] == "active"]
    covered = {r["domain"] for r in active}
    for domain, entry in profile["domains"].items():
        if entry["applicability"] == "applicable" and domain not in covered:
            warnings.append(domain + ": no active record; use an explicit unknown if appropriate")
        if entry["applicability"] != "applicable":
            warnings.append(domain + ": applicability=" + entry["applicability"])
    for gap in state["gaps"]:
        for rid in gap["record_ids"]:
            if rid not in by_record:
                errors.append(gap["id"] + ": gap references missing record " + rid)
        if gap["status"] == "resolved" and (not gap["resolution"] or not gap["resolved_at"]):
            errors.append(gap["id"] + ": resolved gap requires resolution and resolved_at")
        if gap["status"] != "resolved":
            warnings.append(gap["id"] + ": unresolved " + gap["type"] + " gap")
    for question in state["questions"]:
        for sid in question["answer_source_ids"]:
            if sid not in by_source:
                errors.append(question["id"] + ": missing answer source " + sid)
        if question["status"] == "answered" and not question["answer_source_ids"]:
            errors.append(question["id"] + ": answered question needs provenance")
    for stage in stages.values():
        check_review(stage["review"], "stage " + stage["id"])
    check_review(state["release_review"], "release")

    # Obvious exact-key collisions are flagged; semantic contradiction review remains manual.
    keys = {}
    for r in active:
        if r["kind"] not in ("confirmed_fact", "founder_decision"):
            continue
        key = (r["domain"], r["subject_key"], json.dumps(r["scope"], sort_keys=True), r["kind"])
        if key in keys and keys[key]["value"] != r["value"]:
            errors.append(r["id"] + ": conflicting active value for same subject/scope as " + keys[key]["id"])
        keys[key] = r

    if state["readiness"] != "needs_completion":
        if state["release_review"]["status"] != "approved":
            errors.append("release: ready status requires explicit review")
        if state["automated_validation"] == "failed":
            errors.append("release: failed automated validation cannot be ready")
        for s in state["stages"]:
            if s["status"] not in ("approved", "not_applicable", "deferred"):
                errors.append("release: incomplete stage " + s["id"])
            if s["status"] == "deferred":
                warnings.append("stage " + s["id"] + ": deferred")
        if stages.get("00", {}).get("status") != "approved" or stages.get("11", {}).get("status") != "approved":
            errors.append("release: discovery and publishing stages must be approved")
        for gap in state["gaps"]:
            if gap["status"] != "resolved" and gap["type"] in ("critical", "strategic_decision"):
                errors.append("release: blocking gap " + gap["id"])
        for domain, entry in profile["domains"].items():
            if entry["applicability"] == "applicable" and domain not in covered:
                errors.append("release: missing domain " + domain)
        for r in active:
            if r["review"]["status"] != "approved":
                errors.append("release: active record not reviewed " + r["id"])
        if state["readiness"] == "ready" and warnings:
            errors.append("release: warnings require resolution or ready_with_caveats")
    return {"valid": not errors, "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--as-of", help="YYYY-MM-DD; defaults to local date")
    parser.add_argument("--expected-base", help="Expected saved base context version")
    args = parser.parse_args()
    try:
        bundle = json.loads(args.bundle.read_text(encoding="utf-8-sig"))
        report = validate(bundle, args.as_of, args.expected_base)
    except (OSError, ValueError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)], "warnings": []}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())

