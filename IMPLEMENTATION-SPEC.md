# Final implementation specification

Product: AI Company Context Architect  
Release: 1.1.0  
Specification date: 2026-11-19  
Scope: portable hybrid skill, entire company, adaptive conversation language.

## 1. Accepted design and boundaries

The approved conversation selected the hybrid advisor: interview for private intent and decisions, read available evidence first, research external questions, synthesize structured context, and request review of concrete outputs. The design supports idea, MVP, launched, and operating companies.

Four modes are required in v1: Build, Audit, Update, Export. Twelve stages remain the navigation backbone. All ten substantive domains receive an applicability decision; a small company need not invent departments, metrics, or policies it does not yet have.

This release includes instructions, operational protocols, eight JSON Schemas, Markdown templates, three host adapters, fictional fixtures, and local validation/export/build helpers. It is an executable reference package, not a hosted application or autonomous integration service. Live-platform acceptance is a separate release check.

No CRM connection, database, account creation, employee messaging, scheduled job, or cross-platform synchronization is required. "Publish" below means create a reviewed local/context artifact. External sharing is a distinct action governed by the user's request and available permissions.

## 2. Architecture

~~~text
User + supplied documents + optional scoped public research
                         |
             Host adapter / capability report
                         |
              Mode router + stage engine
                         |
    Interview / Research / Evidence / Synthesis engines
                         |
       Canonical context bundle + progress checkpoint
                         |
           Validation + founder review gates
                         |
   Master / Operational context / Domain packs / Registers
                         |
          Versioned snapshots + selective exports
~~~

| Component | Inputs | Responsibility | Output / failure behavior |
|---|---|---|---|
| Host adapter | User request, available tools | Map core workflow to host capabilities | Explicit capability map; degrade honestly |
| Mode router | Intent, existing bundle | Choose one of four modes | Build by default only when no context exists |
| Interview engine | Evidence, gaps, maturity | Select highest-value unanswered questions | One question by default, help handling, question log, normalized responses |
| Research engine | External gaps, permitted scope | Retrieve and compare relevant sources | Source register; inaccessible sources stay unresolved |
| Evidence engine | Statements, extracts, observations | Assign kind, provenance, dates, confidence | Atomic records; no invented citations |
| Stage engine | Progress, dependencies, gaps | Route, checkpoint, reopen affected stages | Stage summary + review request where needed |
| Synthesis engine | Canonical records | Build readable views without changing epistemic status | ID-linked master and packs |
| Validation engine | Bundle + intended use | Structural, semantic, freshness, coverage, human review | ready / ready_with_caveats / needs_completion |
| Publishing engine | Reviewed candidate | Freeze version and render consistent outputs | Manifest, snapshot, outputs |
| Maintenance engine | Base version + change | Diff, impact analysis, supersession | New revision; old snapshot retained |

The orchestrator is the host language model following SKILL.md. These components are logical responsibilities, not claims that eight separate services or agents exist.

## 3. File architecture

~~~text
ai-company-context-architect/
  SKILL.md
  README.md
  IMPLEMENTATION-SPEC.md
  requirements.txt
  release.json
  CHANGELOG.md
  references/
    beginner-guided-mode.md
    interview-protocol.md
    adaptive-stage-engine.md
    research-methodology.md
    evidence-classification.md
    validation-protocol.md
    privacy-and-governance.md
    update-protocol.md
  stages/
    00-discovery.md
    01-company-foundation.md
    02-business-model.md
    03-products-services.md
    04-market-intelligence.md
    05-customer-intelligence.md
    06-brand-communication.md
    07-marketing-growth.md
    08-operations-team.md
    09-technology-data.md
    10-governance-risks.md
    11-validation-publishing.md
  templates/
    first-reply.json
    starter-context.md
    discovery-brief.md
    stage-summary.md
    company-context-master.md
    ai-operational-context.md
    domain-context-pack.md
    evidence-register.md
    assumptions-register.md
    progress-state.md
    change-log.md
  schemas/
    common.schema.json
    company-profile.schema.json
    context-record.schema.json
    evidence-source.schema.json
    progress-state.schema.json
    context-bundle.schema.json
    export-manifest.schema.json
    release-manifest.schema.json
  adapters/
    claude.md
    codex.md
    chatgpt.md
    chatgpt-project-instructions.txt
  scripts/
    validate_context.py
    export_context.py
    build_package.py
  tests/
    TEST-PLAN.md
    VALIDATION-REPORT.md
    idea-stage-company.md
    mvp-stage-company.md
    operating-company.md
    context-update.md
    adversarial-and-portability.md
    test_contracts.py
    test_distribution.py
    beginner-scenarios.md
    beginner-evaluation.md
    fixtures/idea-company.json
~~~

Stage files contain domain-specific inputs, checks, candidate questions, maturity adaptations, outputs, and exit gates. References contain shared rules once. Templates are render contracts, not prefilled company facts. Schemas enforce machine structure. Scripts handle repetitive checks and packaging; the conversation does not require script execution.

## 4. Runtime company workspace

~~~text
company-context/<company-id>/
  working/
    context.json
    company-context-master.md
    ai-operational-context.md
    domain-packs/<domain>.md
    evidence-register.md
    assumptions-register.md
    progress-state.md
    change-log.md
  releases/<context-version>/
    context.json
    release-manifest.json
    [rendered documents for this release]
  exports/<export-id>/
    context.json
    ai-operational-context.md
    export-manifest.json
~~~

context.json is the canonical bundle containing profile, sources, records, and state. Human-readable files are projections, not independent authorities. Progress JSON is nested in the bundle to avoid synchronization races; the Markdown progress file is a readable view.

Separate paths by company ID. Compare company ID and base context version before merging. If storage is unavailable, return equivalent named text blocks and a resume packet; the user must save and provide them in the next session.

Snapshots are immutable by workflow. A filename does not provide filesystem immutability, authorization, encryption, or a backup guarantee. Hashes detect accidental content drift only.

## 5. Stage protocol and state machine

Each stage applies the same micro-cycle:

1. Review existing sources, record IDs, previous decisions, unresolved gaps, and stage applicability.
2. Investigate only missing evidence: inspect documents, ask a focused question, or perform targeted research.
3. Synthesize atomic records and a stage summary. Separate facts, decisions, hypotheses, aspirations, unknowns, and research evidence.
4. Validate source coverage, internal consistency, scope, freshness, and appropriate maturity requirements.
5. Approve: show the proposed statements/decisions and caveats to the owner. Preserve explicit prior approval for unchanged records. Record reviewer, timestamp, and reviewed scope.

Stage status values: not_started, in_progress, awaiting_review, approved, deferred, not_applicable. Deferred and not_applicable need reasons. An approved stage may reopen after affected records change. An unknown statement may be approved as an honest description of uncertainty.

Stage 00 establishes scope and routing. Stages 01–10 build domain context, with dependencies and independent work as described in the engine. Stage 11 validates and freezes the release. Numeric ordering is a default path, not an instruction to repeat already answered interviews.

Gaps are critical, non_critical, research, or strategic_decision. Criticality depends on intended use. A support export cannot state an unresolved refund policy; an idea-stage master can explicitly say revenue does not exist. Only the blocked dependency waits; independent draft work continues.

## 6. Maturity adaptation

| Maturity | Primary emphasis | Acceptable unknowns | Unacceptable invention |
|---|---|---|---|
| idea | Problem, founder intent, proposed offer, alternatives | Revenue, conversion, retention, org structure | Fake traction or proven demand |
| mvp | Current functionality, pilot evidence, learning goals | Stable unit economics or scalable operations | Treating prototype features as generally available |
| launched | Actual onboarding, user behavior, delivery and support | Long-term retention or mature governance | Generalizing a tiny sample to a whole market |
| operating | Revenue definitions, segments, processes, ownership, constraints | Explicit gaps with owners | Presenting stale metrics as current performance |

Do not use maturity as a proxy for incorporation, funding, headcount, or profitability.

## 7. Data contracts

All schemas use JSON Schema Draft 2020-12, UTF-8, strict known properties, stable English field keys, and localized human strings. Version 1.0.0 describes schema compatibility; context_version describes a company's content release.

- Profile: identity, maturity, language settings, requested use, domain applicability, classification defaults.
- Source: internal/public origin, locator, date, authority, sensitivity, and limitations.
- Record: one material claim, domain, kind, subject key, scope, temporal status, evidence IDs, owner, confidence and rationale, review, revision linkage.
- State: mode, current stage, stage reviews, gaps, questions already asked, next action, release status, capabilities, base version.
- Bundle: profile + sources + records + state; canonical input for validation.
- Export manifest: source version, audience, domains, included/omitted record IDs, caveats, and hashes.
- Release manifest: exact artifact paths and SHA-256 digests, readiness, review details, validator outcome.

IDs are unique within a company bundle. Prefixes are conventional (C-, R-, S-, G-, Q-), not source authority. A correction creates a new record ID with supersedes pointing to the old record; the old record becomes superseded. Source IDs remain stable. Existing snapshots retain their exact historical content.

The validator checks schemas, ID references, company identity, supersession, approval invariants, fact provenance, temporal consistency, and operational release gates. It does not prove the truth of a source, independently authenticate a reviewer, or detect all semantic contradictions.

### Fact and decision policy

A confirmed fact requires attributable supporting evidence, a verification date, and a described verification method. Founder-attested facts are limited to internal company matters, with that basis visible. Public market claims require evidence beyond founder assertion.

A founder decision requires explicit approval, a reviewer, and an approval time. A target such as "reach 1,000 customers" is an aspiration. Approval of a hypothesis changes review status only. Research evidence describes what a source reports; it does not imply the conclusion universally holds.

### Null and unknown

Unknowns use kind=unknown, value=null, and a meaningful statement explaining the missing information. Null means not known, never zero, false, or not applicable. Record whether a domain is not applicable and why in profile.domains.

Metrics need unit, period, denominator/population, geography, and observation date in structured scope fields or explicit text. A metric must not be compared across incompatible definitions.

## 8. Interview and research behavior

Ask the most consequential unanswered question first. Ask one meaningful question at a time by default; batch only at the user's explicit preference. Do not ask an entire domain catalog. Extract already supplied answers and quote/paraphrase them for review instead of re-asking. Keep the question log for cross-session deduplication.

Source selection follows question type:
- Private intent and strategic choice: founder or delegated owner.
- Current product and operations: approved company material and direct observation.
- Market conditions: dated authoritative sources and independent corroboration when material.
- Customer needs: direct customer evidence; external reviews provide adjacent signals with sampling limits.
- Legal or regulated claims: jurisdiction-specific authoritative evidence and unresolved review needs.

Default research budget is a small scoped pass (up to five useful sources per external question). Stop when the specific gap is adequately resolved, evidence remains unavailable, or scope/time requested by the user is reached. This is a working convention, not a reason to omit necessary verification.

### Guided experience in v1.1

The default first reply explains the outcome, pace, acceptable rough answers, help/defer/pause phrases, and review in roughly 45–90 words. Then it asks one unanswered question. The entire opening stays within 100 words, including a compact starter draft when enough context already exists and any explicitly requested question batch. Fuller starter details can follow. It does not expose internal stages or require a form. The shared contract is references/beginner-guided-mode.md and the starting copy is templates/first-reply.json; the ChatGPT adapter embeds the essential behavior so it does not depend on perfect retrieval.

Distinguish unclear meaning, undecided strategy and missing evidence. Help once, then offer deferral unless more explanation is requested. Accept short or unpolished answers. Assistant-generated suggestions stay proposals. Pause stops questions and creates a truthful checkpoint or copyable resume packet.

Once the basic idea, problem, customer, solution and maturity are known or explicitly unknown, show a short starter-context draft, usually within about five useful answers. This is a partial projection, not a release or a question quota. It cannot mark unvisited stages approved, satisfy missing coverage, or enter the reviewed-release exporter. The schema stays 1.0.0. Use existing questions, gaps, next_action and the readable progress file; do not add new canonical properties.

Present Understand project → Clarify details → Review reference while retaining the 12 internal stages. Group review of named, displayed topics without repeated paraphrase approval. Adapt depth to maturity; an idea does not need invented operating metrics. Save the last help attempt, deferred topics and next step for resumption.

## 9. Language contract

Determine conversation language from an explicit preference, otherwise the latest substantive user message. Document language initially follows conversation language but can be set independently. Mixed Arabic/English input does not require translating company names, product names, acronyms, IDs, or schema keys.

Use natural business language, preserve original evidence excerpts with optional translations, and mark translated quotations. Keep ASCII IDs and numeric data stable. Display monetary currency and dates explicitly. Store dates in ISO 8601, including timezone offsets on timestamps. Locale is not evidence of jurisdiction.

## 10. Outputs and selection

The master covers every applicable domain and states omissions. The operational context should normally fit a brief working prompt (about 600–1,000 words as a tunable target), with source version, task, factual boundaries, current decisions, unknowns, and links/IDs for detail. This is a design target, not a platform token limit.

Domain packs are generated only when useful for the requested role. A marketing pack can include customer and brand context, but must not silently import restricted finance or HR data. Evidence and assumptions registers include IDs and ownership; the change log records why a revision happened and which outputs changed.

A renderer must preserve meaning, review state, IDs, dates, and caveats. It must not create a new claim by "polishing" uncertainty out of prose.

## 11. Validation and approval

Readiness is categorical:
- ready: no blocking structural/semantic/use-specific gaps; required reviews complete; all applicable domains represented.
- ready_with_caveats: noncritical research gaps, bounded uncertainty, or stale noncritical material are visible and safe for the stated use.
- needs_completion: invalid structure, unsupported fact, unresolved material contradiction, missing approval, or blocked critical dependency.

Automated success is necessary for machine-validated releases but is not sufficient for substantive readiness. Manual review covers truth, contradiction meaning, relevance, privacy leakage, and usability. If code execution is unavailable, manual release may proceed with checks recorded and automated_validation=not_run; never label it machine-validated.

Founder review gates are content-specific. No extra approval is needed to prepare drafts or routine files. A proposed strategic change must be presented before it is recorded as a decision. Approval to create local outputs does not imply approval to publish publicly.

## 12. Updates, resumption, and concurrency

Load the saved context and source version. Ask only unresolved questions after reconstructing the current stage. A missing or corrupt checkpoint triggers recovery from the last valid bundle, with uncertainty about lost work disclosed.

Updates are append-and-supersede with a new content version, change reason, affected domains, and regenerated views. Preserve approved unchanged records. Reopen stage review for material changes. A stale base version causes a merge review before saving. Unknown future schema versions are not silently coerced.

No background update or memory persistence is promised. Review dates are reminders in data; scheduled execution requires a separate user request and platform capability.

## 13. Platform contracts

The same SKILL.md and protocols define behavior. Host adapters only describe activation, reference loading, tools, and persistence. They may not relax evidence/review rules.

Claude uses a native skill ZIP where supported. ChatGPT's baseline is project instructions plus consolidated reference files; ordinary chat can use pasted instructions and a resume packet. Optional existing GPT configuration is documented only where available. Neither adapter assumes permanent file edits or automatic synchronization.

Platform setup facts were checked on 2026-11-14 against the sources linked in the adapter documents. These capabilities can change, so inspect the actual workspace. No live account deployment was performed for this package.

## 14. Acceptance and implementation status

Must pass locally: schema self-validation; accepted/rejected fixture checks; broken reference detection; unknown handling; fact/decision provenance gates; stale base rejection; supersession integrity; restrictive public export; deterministic packaging; UTF-8 preservation.

Must pass on each target surface before claiming live compatibility: activation, stage routing, adaptive interview, evidence handling, language switch, resume after a new chat, role-specific export, missing-tool fallback, and injection-resistant document ingestion.

Delivered code covers validation, conservative export, and packaging. Natural-language orchestration and Markdown rendering are performed by the host under the protocols. Real-company runs, platform activation, and factual source review remain human/model acceptance activities.

## 15. Traceability

| Accepted requirement | Implementation |
|---|---|
| Hybrid advisor | Interview/research references and per-stage protocols |
| Whole company | Stages 01–10 and required domain applicability |
| Claude + ChatGPT | Core instructions, adapters, generated distribution |
| Adaptive language | SKILL.md, interview rules, bilingual test cases |
| Founder review | Stage review + per-record review contracts |
| Evidence distinction | Six-kind enum and semantic validator |
| Persistent outputs | Canonical bundle, snapshot layout, resume protocol |
| Build / Audit / Update / Export | Router and mode-specific gates |
| Appropriate early-stage outputs | Maturity profiles and idea fixture |
| Quality and maintenance | Validation protocol, update rules, tests |

The detailed tests and actual local results live in tests/TEST-PLAN.md and tests/VALIDATION-REPORT.md.

