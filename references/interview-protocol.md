# Adaptive interview protocol

## Opening
Review attached sources and prior progress before speaking. Infer mode from the user's request. If identity, maturity, and purpose are already present, reflect them briefly and start the first unresolved point. Otherwise ask only what blocks routing.

Example Arabic: "سأبدأ بالمعلومات المتاحة، ثم أسأل عن الفجوات فقط. هل المشروع فكرة، أم منتج أولي، أم أُطلق بالفعل؟"
Example English: "I found the product brief and pricing sheet. I can reuse those. Who is the primary customer you want this context to serve?"

## Question selection
1. Build an internal list of missing facts and decisions.
2. Exclude answered questions using state.questions and existing sources.
3. Rank: intended-use blocker → contradictory material claim → strategic decision → high-value unknown → optional detail.
4. Ask 1–3 related questions. Use a recommendation when useful; include unknown/not decided as a legitimate answer.
5. Normalize the answer into atomic records with source IDs. Preserve the original scope; do not invent dates, quantities, or customer validation.
6. Update the question's status to answered, deferred, or open. A rephrasing is not a new question if it asks the same thing.

A user saying "no revenue yet" answers the question; it is not an invitation to ask for MRR again. A new period, changed scope, or contradiction may justify a follow-up and should be explained.

## Language
Use explicit user preference first, otherwise the most recent substantive message. Detect language from natural language, not pasted code or a file's language. A short "OK" need not reset Arabic preference. Save conversation_language and document_language independently using BCP-47-style tags such as ar or en; unknown regional variants do not need guessing.

Switch on request immediately. Translate labels and prose, keep canonical keys, IDs, trademarks, currencies, and source locators stable. Ask about ambiguous dates such as 03/04 only if relevant.

## Synthesis and review
Use templates/stage-summary.md. Separate "documented", "proposed decisions", and "open questions". Ask review only after a concrete summary exists. A broad "looks good" approves only the clearly displayed scope; it does not approve hidden changes or fabricate missing evidence. Where review is already explicit, record it and proceed.

Review can approve honest uncertainty. An approved hypothesis remains a hypothesis. The founder can choose a strategy, but cannot make an unsupported market claim empirically verified.

## Interview boundaries
Do not demand personal records or credentials. Ask for aggregated operational facts where sufficient. When the company lacks evidence, propose a test or record unknown instead of asking the same question repeatedly.

At pause or session end, provide current stage, saved version, unanswered IDs, next question, and which artifacts the user must bring back if persistence is unavailable.

