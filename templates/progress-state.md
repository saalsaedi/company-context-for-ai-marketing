# Resume state — {{company_name}}

Canonical bundle: {{bundle_location_or_named_text_block}}  
Company ID: {{company_id}} | Context version: {{context_version}} | Base: {{base_version}}  
Mode: {{mode}} | Current stage: {{current_stage}} | Updated: {{updated_at}}

## Stage progress
| Stage | Status | Review scope / reason |
|---|---|---|
{{stage_rows}}

## Already answered
{{question_ids_topics_and_answer_source_ids}}

## Pending questions and gaps
{{pending_ids_owners_and_next_actions}}

## Next action
{{exact_next_action_without_repeating_completed_interview}}

## Conversation handoff
{{guided_or_compact_preference_visible_journey_group_starter_draft_location_and_last_help_attempt}}

Record answered/deferred topics in the canonical question log and gaps. Include the next useful step and relevant help/pace reminder in state.next_action; do not introduce new JSON fields. On resume, give a short reminder and continue rather than restarting onboarding.

## Resume instructions
Load the canonical bundle and validate company/version before proceeding. Reuse answered topics and preserve approvals for unchanged content. If files were not saved, provide this packet and the canonical bundle to the next chat.

## Capabilities
{{observed_capabilities_and_persistence_limits}}

Render rule: record operational state, not hidden reasoning. This readable view must agree with state in context.json.

