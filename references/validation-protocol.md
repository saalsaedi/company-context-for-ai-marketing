# Validation and release protocol

## Pass 1: structure
Validate the bundle against all local schemas with scripts/validate_context.py. Use an explicit --as-of date for reproducible freshness results. Reject unknown schema versions, malformed dates, extra fields, unresolved IDs, wrong company identity, and invalid supersession chains.

## Pass 2: semantics
Check fact sources and verification, explicit decision approval, unknown null values, planned-versus-current separation, source dates, and scope. Compare statements about the same subject across domains. A schema-valid claim can still be wrong.

## Pass 3: coverage and maturity
Every domain must be applicable/deferred/not_applicable with explanation where needed. Every applicable domain needs a substantive record or an honest unknown. Early-stage absence is documented, not filled with invented numbers. Audit identity, offer, intended customer, business model, delivery, technology/data, ownership, and material risks proportionately.

## Pass 4: intended-use and audience
Inspect the target task. Exclude or block unresolved facts that would cause the agent to make an unsupported promise. Confirm every included record fits the requested audience and data scope. Read the full text for accidental private data; sensitivity labels alone do not redact prose.

## Pass 5: human review
Present a stage/release summary, material caveats, changes, and proposed strategic decisions. Record who reviewed which scope and when. Explicit earlier approval applies to unchanged content. Do not re-ask merely because a file is being rendered.

## Readiness
ready: structural/semantic checks clear, all required stages reviewed or justified non-applicable, no open material blockers.
ready_with_caveats: only noncritical gaps or bounded uncertainty remain and the intended use is safe with explicit limitations.
needs_completion: errors, critical gaps, pending strategic decisions, unreviewed release, or unresolved material contradictions.

No numeric "quality percentage" is used. The automated validator returns errors and warnings, not a truth certification. The host sets readiness after reviewing those findings.

## Freeze
1. Finish the candidate bundle and review.
2. Assign a content version; compare the expected base version.
3. Render master, operational context, packs and registers from the same bundle.
4. Validate the bundle and inspect the rendered files for agreement.
5. Create a new release directory and manifest with relative artifact paths and SHA-256 hashes. Fail if that version already exists; never silently overwrite a snapshot.
6. Report readiness, checks run/not run, caveats, and next review owners.

Manifest hashes exclude the manifest itself. Artifact digests attest to bytes, not factual truth. Check path containment before writing any artifact. Automated execution requires the optional Python dependency; manual validation remains available and must be labeled accurately.

## Manual fallback
Check required fields, types, IDs, provenance, dates, stage reviews, gaps, audience, and output consistency using the same rubric. Record automated_validation=not_run. Never claim scripts passed if code execution or dependencies were unavailable.

