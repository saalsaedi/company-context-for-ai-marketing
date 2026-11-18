# Stage 02 — Business model and finance context

Domain: business_model  
Dependencies: 01 foundation; usable offer draft.

## Inputs
Pricing, contracts, revenue definitions, billing model, cost summaries, forecast assumptions when supplied.

## Review
Identify buyer versus user, value exchange, revenue streams, sales motion, cost drivers, margin definitions and current pricing.

## Investigate
Resolve currency, tax inclusion, billing period, contract scope and measurement period. Request aggregates rather than unnecessary customer-level financial data.

Candidate questions (select only unanswered, useful questions):
- Who pays, for what, and on what schedule?
- Which prices are live today and which are experiments?
- What costs or constraints most affect your ability to deliver?

## Synthesize
Represent current model, planned experiments and targets separately. Define metrics and calculations; record pricing ownership and revision dates.

## Validate
Revenue is not cash collected; bookings are not MRR. Missing revenue is unknown or not yet applicable, never assumed zero unless stated. Do not invent unit economics.

## Approve
Show pricing and business-model decisions with tradeoffs; mark proposals pending until the owner accepts them.

## Maturity adaptation
Idea: revenue-model hypotheses and willingness-to-pay tests. MVP: pilot pricing and known costs. Launched: actual billing/collections definitions. Operating: period-bound performance, margin and concentration risks.

## Outputs
Business-model records; pricing/metric definitions; finance caveats; assumptions to test.

Save records under domain=business_model; preserve record IDs in all rendered views. Use [stage summary](../templates/stage-summary.md) and update the canonical progress state after meaningful changes.

## Exit gate
The model is understandable for the company's maturity; price/metric units are explicit; no unsupported financial performance claims.

If blocked, log a gap type, affected claim/task, owner and next action. Continue independent draft work when possible. Review approval never changes evidence kind. See [stage engine](../references/adaptive-stage-engine.md) for transitions and [validation protocol](../references/validation-protocol.md) for release criteria.

