# Mode router and adaptive stage engine

## Mode contracts
| Mode | Entry | Work | Exit |
|---|---|---|---|
| Build | No trusted bundle, or rebuild explicitly requested | Discovery, applicable domains, validation | Reviewed context or labeled draft with gaps |
| Audit | Existing context | Read-only review, findings and proposed corrections | Audit result; no silent canonical edits |
| Update | Existing bundle + change | Compare base, impact, append/supersede, validate | New candidate revision and change log |
| Export | Existing bundle + task/audience | Select allowed records and preserve caveats | Scoped export; canonical bundle unchanged |

If a user asks to audit and fix, that authorizes ordinary fixes in an Update candidate; strategic choices still need their owner. If mode is unclear, infer from available artifacts and ask only if it changes consequential behavior.

## Stage index and dependencies
| Stage | File | Typical dependency |
|---|---|---|
| 00 | [Discovery](../stages/00-discovery.md) | None |
| 01 | [Foundation](../stages/01-company-foundation.md) | 00 |
| 02 | [Business model](../stages/02-business-model.md) | 01 |
| 03 | [Products/services](../stages/03-products-services.md) | 01 |
| 04 | [Market intelligence](../stages/04-market-intelligence.md) | 01 + proposed offer |
| 05 | [Customer intelligence](../stages/05-customer-intelligence.md) | 03 + customer scope |
| 06 | [Brand/communication](../stages/06-brand-communication.md) | 01 + 05 |
| 07 | [Marketing/growth](../stages/07-marketing-growth.md) | 02 + 05 + 06 |
| 08 | [Operations/team](../stages/08-operations-team.md) | 02 + 03 |
| 09 | [Technology/data](../stages/09-technology-data.md) | 03 + 08 |
| 10 | [Governance/risks](../stages/10-governance-risks.md) | 00 + available domain context |
| 11 | [Validation/publishing](../stages/11-validation-publishing.md) | Applicability recorded for every domain |

Dependencies require a usable draft or explicitly bounded unknown, not perfect information. Review → Investigate → Synthesize → Validate → Approve is the cycle inside every stage.

## Routing rules
Read before asking. In idea mode, prioritize 01, 03, 05, and founder hypotheses; do not fabricate operating data. In an operating company, ingest evidence first and concentrate questions on discrepancies and ownership.

A critical gap blocks only a dependent output. Record the blocked claim/task and an owner. A research gap can remain a caveat if the claim is excluded or labeled unverified. A strategic_decision gap remains pending until the founder decides; the model may offer options.

All stages have a state entry, including deferred/not_applicable with a reason. Do not mark a stage approved until its displayed summary has been reviewed. Stage 11 requires review of the release candidate and its caveats.

## Transitions
not_started → in_progress → awaiting_review → approved
in_progress → deferred (reason required)
not_started/in_progress → not_applicable (reason required)
approved/deferred/not_applicable → in_progress (new evidence or scope, explain why)

Transitions are enforced by the orchestrator and audited in state, not by a hidden daemon. Stage review applies to the stated context version. Material changes reopen affected stages; purely typographic edits can retain substantive review with an audit note.

## Checkpoint
After a meaningful change, save context.json and a readable progress view. Store mode, stage, review scope, questions, gaps, next action, base version, and observed capabilities. Never store private hidden reasoning.

On resume, validate the bundle, company ID, schema version and base revision. Reconstruct from records; avoid re-running completed interviews. If a capability changes, update the capability report and continue with an honest fallback.

