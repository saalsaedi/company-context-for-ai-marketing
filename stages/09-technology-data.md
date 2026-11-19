# Stage 09 — Technology, data and AI

Domain: technology_data  
Dependencies: 03 product; 08 operations.

## Inputs
System inventory, approved architecture notes, analytics definitions, data policies, existing AI use cases.

## Review
Identify systems of record, integrations, data flows, access ownership, constraints and existing AI tasks.

## Investigate
Clarify available versus planned integrations, meaningful data quality problems and source-of-truth conflicts. Never request secrets to describe an integration.

Candidate questions (choose one useful unanswered question; these are alternatives, not a questionnaire):
- Which systems hold the information the company trusts?
- Which integrations work today?
- Which company information may the AI assistant use for this task?

## Synthesize
Create system/data context, metric ownership, AI use boundaries, capability dependencies and appropriate source locators.

## Validate
Do not claim an integration works from its logo on a slide. Do not include credentials, raw customer data or unjustified security assurances.

## Approve
Owner reviews data/AI usage boundaries and planned technology changes; current-system claims retain their evidence.

## Maturity adaptation
Idea: minimum requirements and choices pending. MVP: current stack and manual workarounds. Operating: ownership, quality, integration limits and approved AI uses.

## Outputs
System/data inventory; AI operating constraints; technical dependencies and data gaps.

Save records under domain=technology_data; preserve record IDs in all rendered views. Use [stage summary](../templates/stage-summary.md) and update the canonical progress state after meaningful changes.

## Exit gate
Current tools and allowed data use are clear; credentials and unnecessary personal data are absent.

If blocked, log a gap type, affected claim/task, owner and next action. Continue independent draft work when possible. Review approval never changes evidence kind. See [stage engine](../references/adaptive-stage-engine.md) for transitions and [validation protocol](../references/validation-protocol.md) for release criteria.

