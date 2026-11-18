# Stage 11 — Validation and publishing

Domain: orchestration  
Dependencies: All domains assessed for applicability; reviewable candidate exists.

## Inputs
Canonical bundle, stage summaries, all projected outputs, intended-use and audience definition.

## Review
Check coverage, sources, contradictions, review status, maturity fit, sensitive data and stale claims across all outputs.

## Investigate
Resolve only release blockers; defer noncritical gaps with owners and caveats. Run local validation if supported; otherwise record manual checks.

Candidate questions (select only unanswered, useful questions):
- Does this release accurately describe the company and its open questions?
- Are the stated limitations acceptable for the intended AI task?
- Which owner should review the next material change?

## Synthesize
Render master, operational context, selected domain packs, registers, progress and change log from one version.

## Validate
Check IDs, dates, references, current/planned distinctions, approvals, artifact consistency, and use-specific truthfulness. Read generated prose for unsupported paraphrases.

## Approve
Present the concrete release summary and caveats. Record the owner's review of this version; preserve already explicit approval.

## Maturity adaptation
Apply the same truth standards to every maturity; completeness requirements remain proportional to actual company operations.

## Outputs
Versioned context bundle; rendered deliverables; release manifest; readiness result; next-review actions.

Use [stage summary](../templates/stage-summary.md) and update the canonical progress state after meaningful changes.

## Exit gate
ready or ready_with_caveats only after required reviews and checks; otherwise deliver a labeled draft with needs_completion. Public sharing is separate from local release.

If blocked, log a gap type, affected claim/task, owner and next action. Continue independent draft work when possible. Review approval never changes evidence kind. See [stage engine](../references/adaptive-stage-engine.md) for transitions and [validation protocol](../references/validation-protocol.md) for release criteria.

