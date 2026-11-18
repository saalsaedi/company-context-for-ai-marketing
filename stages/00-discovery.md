# Stage 00 — Discovery and routing

Domain: orchestration  
Dependencies: None.

## Inputs
User request, attached documents, existing context/state if available.

## Review
Identify the company and check whether this is a new build or an existing revision. Inventory sources without assuming all can be read.

## Investigate
Establish maturity, intended use, audience, company owner and available tools. Determine conversation/document language from the user; ask only if ambiguous.

Candidate questions (select only unanswered, useful questions):
- What does the company do, and how far along is it?
- What should an AI assistant be able to do with this context?
- Which existing documents or decisions should we treat as the starting point?

## Synthesize
Create profile, source inventory, capability map, domain applicability, and a first gap list. Use a working company label if no final name exists.

## Validate
No mix-up between companies; no invented incorporation, geography or revenue. Each tool capability is available, unavailable, or unknown based on observation.

## Approve
Confirm the displayed scope and routing when not already explicit. Discovery can finish with a provisional company name.

## Maturity adaptation
Idea: accept a working name and proposed offer. MVP: distinguish pilot from public release. Launched: establish actual customer scope. Operating: inventory owners and dated systems of record.

## Outputs
Discovery brief; profile; all 12 stage entries; next action; documented scope.

Use [stage summary](../templates/stage-summary.md) and update the canonical progress state after meaningful changes.

## Exit gate
Company identity is sufficiently distinct, mode/maturity/use are known or explicitly provisional, and source/tool limitations are recorded.

If blocked, log a gap type, affected claim/task, owner and next action. Continue independent draft work when possible. Review approval never changes evidence kind. See [stage engine](../references/adaptive-stage-engine.md) for transitions and [validation protocol](../references/validation-protocol.md) for release criteria.

