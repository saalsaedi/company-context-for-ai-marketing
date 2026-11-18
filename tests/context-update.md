# Manual scenario — update and resume

## Starting artifact
Use the fictional idea-company.json fixture, version 1.0.0. Treat the prior snapshot as read-only.

## User request
"We selected a prototype stack and changed our focus to boutique fitness studios. Update only the affected context. Keep the earlier version."

## Expected behavior
- Inspect the base version and gather the concrete stack evidence and approved focus change.
- Create new records and supersede only replaced assertions.
- Reopen foundation/customer/technology and any downstream affected summaries; preserve unrelated approvals.
- Regenerate affected projections, increment context version, create a new snapshot/change log.
- Do not erase earlier records or imply the prototype is a live product.

## Concurrency variation
A second saved revision 1.0.1 appears before committing the candidate based on 1.0.0. Pass only if the host compares the actual latest version and reconciles changes before saving. --expected-base alone cannot discover another file.

## Resume variation
Start a new chat with only the updated canonical bundle and the skill. Ask "Continue." The host should report the current stage/next gap and avoid re-asking the answered maturity question.

## Recovery variation
Remove the progress state or provide an unknown schema_version. The host must disclose recovery/migration need, reconstruct only what evidence supports, and not invent lost approval.

