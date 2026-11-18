# Update, audit, and recovery protocol

## Entry
Load the canonical bundle and establish company_id, schema_version, context_version and requested change. If only a rendered master exists, reconstruct a draft with uncertainty and provenance to that document; do not pretend a missing structured history exists.

Audit defaults to read-only findings. Update prepares a candidate revision. Export does not mutate canonical records.

## Change algorithm
1. Capture the expected base version; compare it with the latest stored version immediately before saving.
2. Identify affected subject keys, domains, dependencies, and outputs.
3. Add new evidence sources and new records. Retain original IDs. Mark replaced records superseded and point the new record's supersedes to them.
4. Do not remove historical facts simply because a current decision changed. Retracted claims retain a retraction reason.
5. Review material decisions and uncertainties. Preserve approval for unchanged records; pending changes must not borrow old approval.
6. Reopen affected stage reviews, regenerate projections, and validate.
7. Increment context_version (patch for corrections, minor for material additions/changes, major for deliberate baseline restructuring). Schema version changes only when contracts change.
8. Save a new snapshot, manifest, and change log. Never overwrite prior releases.

## Stale base
If another revision appeared, stop the save, compare both changes, and merge only nonconflicting content. Present strategic conflicts to the owner. The validator's --expected-base option checks the declared base; the host still must inspect actual stored latest state before writing.

## Rollback
Restore by creating a new revision referencing the chosen older snapshot and the reason. Preserve both history and the intervening versions; do not delete them to make rollback look like it never happened.

## Resume
Load context.json, validate, identify the current stage and next action, and reuse question statuses. If state and records conflict, prefer reconstructable evidence while flagging the discrepancy. Do not guess lost approvals.

No files: return the full context/resume blocks for the user to save. A subsequent chat must receive these artifacts; model memory alone is insufficient.

## Triggers
Product launch, pricing change, audience shift, new customer evidence, metric period close, team/process changes, and expired review dates can trigger an update. Store next_review_at as data. Do not create a background schedule unless separately requested.

