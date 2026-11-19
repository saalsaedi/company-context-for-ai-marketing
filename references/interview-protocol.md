# Adaptive interview protocol

## Opening
Review attached sources and prior progress before speaking. Infer mode from the user's request. Follow [beginner-guided-mode.md](beginner-guided-mode.md) for the short first reply, help handling, early draft, maturity adaptation and progress. Use [first-reply.json](../templates/first-reply.json) for starting copy, adapted to what the user has already supplied. Do not request an intake form or repeat a known project description. On resume, give only a brief help reminder and continue from the saved next step.

## Question selection
1. Build an internal list of missing facts and decisions.
2. Exclude answered questions using state.questions and existing sources.
3. Rank: intended-use blocker → contradictory material claim → strategic decision → high-value unknown → optional detail.
4. Ask one focused question by default. Only batch if the user explicitly prefers it. Use everyday language and a brief purpose or fictional example when helpful; accept unknown/not decided/defer. Do not bundle multiple information requests into one sentence.
5. Normalize the answer into atomic records with source IDs. Preserve the original scope; do not invent dates, quantities, or customer validation.
6. Update the question's status to answered, deferred, or open. A rephrasing is not a new question if it asks the same thing.

A user saying "no revenue yet" answers the question; it is not an invitation to ask for MRR again. A new period, changed scope, or contradiction may justify a follow-up and should be explained.

## Language
Use explicit user preference first, otherwise the most recent substantive message. Detect language from natural language, not pasted code or a file's language. A short "OK" need not reset Arabic preference. Save conversation_language and document_language independently using BCP-47-style tags such as ar or en; unknown regional variants do not need guessing.

Switch on request immediately. Translate labels and prose, keep canonical keys, IDs, trademarks, currencies, and source locators stable. Ask about ambiguous dates such as 03/04 only if relevant.

## Synthesis and review
Use templates/stage-summary.md. Separate "documented", "proposed decisions", and "open questions". Normalize rough answers without asking approval for every paraphrase. After a coherent set of topics, request one review of a short summary with explicit scope; one review may cover several named stages. A broad "looks good" approves only that displayed scope; it does not approve hidden changes or fabricate missing evidence. Where review is already explicit, record it and proceed. Do not append a new discovery question to a review request.

Review can approve honest uncertainty. An approved hypothesis remains a hypothesis. The founder can choose a strategy, but cannot make an unsupported market claim empirically verified.

## Interview boundaries
Do not demand personal records or credentials. Ask for aggregated operational facts where sufficient. When the company lacks evidence, propose a test or record unknown instead of asking the same question repeatedly.

At pause or session end, stop business questions. Provide a brief checkpoint: what is known, what was deferred, the next step, and saved artifacts/version if any. Keep internal IDs in the resume packet, not the conversational headline. If persistence is unavailable, give a copyable packet and say the user must save it; never claim a file was saved.

