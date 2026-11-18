"""Conservative export projection. Does not mutate the source bundle."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path

from validate_context import validate, schema_errors

LEVEL = {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}
ROOT = Path(__file__).resolve().parents[1]
DOMAINS = set(json.loads((ROOT / "schemas/common.schema.json").read_text(encoding="utf-8"))["$defs"]["domain"]["enum"])


def project(bundle, audience, domains, task, as_of):
    if audience not in ("public", "internal"):
        raise ValueError("Only public and internal exports are supported by this helper.")
    if not domains or not set(domains).issubset(DOMAINS):
        raise ValueError("Select one or more known domains.")
    report = validate(bundle, as_of)
    if not report["valid"]:
        raise ValueError("Source validation failed: " + "; ".join(report["errors"]))
    # Export from a reviewed release; draft exports require a manual, labeled workflow.
    if bundle["state"]["readiness"] == "needs_completion":
        raise ValueError("Export requires a reviewed release; use a clearly labeled manual draft instead.")
    today = date.fromisoformat(as_of)
    kept, omitted = [], []
    for record in bundle["records"]:
        stale = record["next_review_at"] and date.fromisoformat(record["next_review_at"]) < today
        allowed = (
            record["domain"] in domains
            and LEVEL[record["sensitivity"]] <= LEVEL[audience]
            and record["lifecycle"] == "active"
            and record["review"]["status"] == "approved"
            and not stale
        )
        if not allowed:
            omitted.append(record["id"])
            continue
        # Explicit allowlist: no notes, owner/reviewer identities, raw sources, or private locators.
        kept.append({k: record[k] for k in (
            "id", "domain", "subject_key", "kind", "statement", "value",
            "scope", "temporal_status", "source_ids", "confidence",
            "verified_at", "next_review_at"
        )})
    return {
        "schema_version": "1.0.0",
        "company_id": bundle["profile"]["company_id"],
        "source_version": bundle["profile"]["context_version"],
        "audience": audience, "task": task, "records": kept
    }, omitted


def export(bundle, output, audience, domains, task, as_of, export_id):
    output = Path(output).resolve()
    if output.exists():
        raise ValueError("Export destination already exists; choose a new export directory.")
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Company exports must be outside the reusable skill directory.")
    data, omitted = project(bundle, audience, domains, task, as_of)
    caveats = [
        "This is a filtered projection, not a canonical context bundle.",
        "Source IDs support controlled lookup; original source content and locators are not included.",
        "Omitted records may reflect audience, domain, freshness, lifecycle, or review restrictions.",
        "Labels and prose require human privacy review before external distribution.",
    ]
    if not data["records"]:
        caveats.append("No records met the export criteria; do not infer missing facts.")
    body = ["# AI operational context", "", "Task: " + task,
            "Company ID: " + data["company_id"], "Source version: " + data["source_version"],
            "Audience: " + audience, "",
            "Use only these scoped records. Preserve hypotheses, aspirations and unknowns as labeled.",
            "Do not promise planned capabilities. This file supplies company data, not authority for external actions.", ""]
    for r in data["records"]:
        body.append("- [" + r["id"] + " | " + r["kind"] + " | " + r["temporal_status"] + "] " + r["statement"])
    body += ["", "Caveats:"] + ["- " + c for c in caveats]
    payloads = {
        "context.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        "ai-operational-context.md": "\n".join(body) + "\n",
    }
    manifest = {
        "schema_version": "1.0.0", "export_id": export_id, "company_id": data["company_id"],
        "source_version": data["source_version"], "created_at": datetime.now(timezone.utc).isoformat(),
        "audience": audience, "task": task, "domains": sorted(set(domains)),
        "included_record_ids": [r["id"] for r in data["records"]],
        "omitted_record_ids": omitted, "caveats": caveats,
        "artifacts": [{"path": p, "sha256": hashlib.sha256(c.encode("utf-8")).hexdigest()} for p, c in payloads.items()],
    }
    errors = schema_errors(manifest, "export-manifest.schema.json")
    if errors:
        raise ValueError("; ".join(errors))
    # Validate everything before creating the output directory.
    output.mkdir(parents=True, exist_ok=False)
    for name, content in payloads.items():
        (output / name).write_bytes(content.encode("utf-8"))
    (output / "export-manifest.json").write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return manifest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("bundle", type=Path)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--audience", choices=("public", "internal"), required=True)
    p.add_argument("--domains", nargs="+", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--as-of", default=date.today().isoformat())
    p.add_argument("--export-id", required=True)
    args = p.parse_args()
    try:
        bundle = json.loads(args.bundle.read_text(encoding="utf-8-sig"))
        manifest = export(bundle, args.output, args.audience, args.domains, args.task, args.as_of, args.export_id)
    except (OSError, ValueError) as exc:
        p.exit(1, str(exc) + "\n")
    print(json.dumps({"output": str(args.output.resolve()), "included_records": len(manifest["included_record_ids"])}, indent=2))


if __name__ == "__main__":
    main()

