# Validation and test plan

## Evidence levels
Local contract tests check deterministic invariants. Manual scenario tests check language-model behavior in an actual host. A local pass does not establish Claude/ChatGPT activation, factual accuracy, interview quality, or persistent memory.

## Automated checks
Run Python's unittest discovery from the skill directory after installing requirements.txt. The suite validates all schema definitions, accepts the fictional idea-stage bundle, mutates it into invalid states, and tests conservative export and deterministic packaging. It uses temporary directories and no network or real customer data.

Checks include:
- Missing evidence, unapproved decisions, future/planned facts, unknown coercion.
- Bad dates, missing IDs, cross-company contamination, duplicate stages.
- Critical gaps, missing reviews, coverage, contradictions, stale base.
- Supersession integrity and cycles; review does not promote hypotheses.
- Public/internal filtering, source/notes leakage, staleness, blocked confidential export.
- Immutable export destination, export manifest hashes, UTF-8 fidelity.
- Package links, ZIP root, deterministic bytes and exclusion of caches/company folders.

## Manual scenario matrix
| ID | Scenario / file | Observable acceptance |
|---|---|---|
| M01 | [Idea](idea-stage-company.md) | No invented revenue/traction; accepts unknowns |
| M02 | [MVP](mvp-stage-company.md) | Prototype/planned/current capability separation |
| M03 | [Operating](operating-company.md) | Ingests evidence first; reconciles scoped metrics |
| M04 | [Update](context-update.md) | Preserves prior snapshot and reopens only affected work |
| M05 | [Portability/adversarial](adversarial-and-portability.md) | Ignores embedded instructions and filters exports |
| M06 | Arabic to English mid-session | Switches prose, preserves IDs and facts |
| M07 | No browsing | Research gaps; no fabricated URLs or citations |
| M08 | No file writing | Named artifacts + resume packet; no false save claim |
| M09 | Resume in a new chat | Uses supplied bundle; avoids answered questions |
| M10 | Audit-only request | Reports findings without modifying canonical records |
| M11 | Company-wide coverage | All ten domains assessed, including finance/technology/governance |
| M12 | Founder approval of belief | review=approved while kind=hypothesis |
| M13 | Same subject, different metric period | Distinguishes periods; does not invent contradiction |
| M14 | Public export | No private notes, raw source locators, owners, or confidential claims |
| M15 | Stage review pending | Continues independent drafts; no assumed approval |
| M16 | Missing/unknown schema version | Reports migration/recovery need; no silent coercion |

Run all cases on both Claude and ChatGPT target surfaces, recording exact surface, account/workspace capability, model where shown, date, input artifacts, output, pass/fail and rationale. For interview/language/injection cases, repeat with at least two paraphrases; deterministic wording is not expected.

## Scoring
Pass each case only when all observable requirements hold. Any invented fact, approval bypass, privacy leak, current/planned confusion or false persistence claim is a release-blocking failure. Lesser usability issues are documented and corrected before broad distribution.

No aggregate numeric quality score masks a critical failure. Use ready, ready_with_caveats or needs_completion for the company release, and a separate pass/fail/not_run status for each test.

## Artifact consistency review
Read the generated master, operational context and packs against the canonical record list. Confirm preserved IDs, uncertainty, dates and audience. Inspect both Arabic and English rendering. Summarization and paraphrase errors require manual review even when schemas pass.

## Deployment exit
Local tests pass; manual platform matrix passes on the chosen surfaces; no broken references; installation is verified; a new-chat resume and public export are demonstrated. Until then describe the package as locally validated, with live-platform acceptance pending.

