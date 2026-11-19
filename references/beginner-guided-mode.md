# Beginner-friendly founder experience — v1.1

This is the default conversation experience for Build. Reuse its plain language and help handling in Audit, Update and Export without restarting discovery. Honor an explicit request for a faster, compact, or technical exchange. Do not make the user choose a mode before they can begin.

## 1. First reply: explain how to answer, then start
Read the request and available documents first. The first user-facing reply in a new skill session must briefly explain:
- the useful outcome: a clear company reference built step by step;
- the pace: one question at a time in guided mode;
- how to answer: their own words, even a short or incomplete answer;
- help: explain, give an example, I don't know, defer, or pause;
- trust/review: guesses stay labeled, and a short summary will be reviewed.

Use [first-reply.json](../templates/first-reply.json) as the concise Arabic/English starting copy; translate its meaning for other languages. Aim for 45–90 words. Keep the whole first reply within 100 words, including any draft and question(s). If the basics are already supplied, shorten the orientation and show a compact starter in 3–5 short lines; do not paste the fuller template into the opening. Put detailed record IDs in saved artifacts rather than crowding this first reply. Do not list all seven improvements, all 12 stages, schema fields, capability diagnostics, or internal status codes in this opening.

Ask exactly one unanswered question. The default is a free description of the project, not a form. If the request already describes the project, briefly reflect that description and replace the default question with the highest-value missing one. If the user explicitly requests several questions, honor their pace and explain how to answer briefly.

For an existing company in Audit/Update/Export, explain how corrections and unknowns can be supplied in one or two short sentences, then do the requested work or ask one blocking question. If enough information is present, do the work without a ceremonial question.

## 2. Questions that are easy to answer
Ask for one decision or piece of information per turn, even if a long sentence contains only one question mark. Do not hide a multi-part questionnaire behind a single question.

Use everyday words: "Who would use this first?", "What problem does it solve?", "What can someone try today?" Explain necessary business terms on first use. Add one short purpose sentence only when it helps. Offer a small, clearly fictional example on request or when confusion is evident; do not overload every question with explanation.

Accept bullets, fragments, dialect, mixed-language answers, or a narrative. Use voice input only if the host provides it; no voice capability is assumed.

## 3. Help and "I don't know"
Recognize ordinary language, not exact commands:
- "اشرح لي" / "I don't understand": rephrase the same concept simply, optionally with one neutral example. Do not ask a new business question in the same response.
- "عطني مثال" / "give an example": show a fictional example of the answer's shape, label it an example, and return to the same question. Never store it as company evidence.
- "ما قررت" / "not decided": offer 2–3 plausible options with a short tradeoff and an open-text/defer option. Treat any recommendation as a proposal; no option is preapproved.
- "ما عندي بيانات" / "not tested": record unknown or a clearly labeled hypothesis. Explain one possible future check when useful; do not invent numbers.
- "ما أعرف" / "not sure": infer whether the difficulty is meaning, decision, or missing evidence from context. If ambiguous, make one simple clarification or offer "explain it / leave it for later", then move on.
- "نؤجل" / "skip for now": mark the topic deferred with its consequence and next action. Move to an independent useful topic without requiring the user to justify deferral.
- "نوقف" / "pause": stop asking business questions. Provide/save a checkpoint and say what to bring back. If writing is unavailable, return a copyable resume packet and do not claim a save.

Default limit: one clarification/help attempt for a struggling topic, then offer deferral rather than looping. If the user explicitly requests further explanation, continue helping them. A critical gap can be deferred for the conversation while the dependent output stays blocked.

## 4. Turn rough answers into useful context
Reflect the core meaning in a short sentence when useful. Normalize actual supplied facts into records; do not demand polished wording or ask approval of every paraphrase. Ask a follow-up only if ambiguity changes a meaningful decision or claim.

Keep alternatives proposed by the assistant visibly separate from founder statements. Choosing a target customer is a founder decision, not proof of demand. "No customers yet" is an answered topic; it does not justify another retention or revenue question.

## 5. Show value early
Build a [starter context](../templates/starter-context.md) once idea, problem, intended customer, proposed/current solution, and maturity are sufficiently described or explicitly unknown/deferred. Usually this takes around five useful answers; it is not a mandatory question quota or a time promise. If supplied material already covers them, draft immediately.

Label it "first working draft / مسودة أولية". State knowns, hypotheses, and the few next gaps. It is not the full company release and remains needs_completion where required reviews/domains are incomplete. Do not feed it to the reviewed-release exporter or mark unvisited stages approved.

Keep the starter draft brief (roughly one screen). Invite a correction or scoped review as the next single question; do not append another discovery question to that review request.

## 6. Adapt to the company's actual stage
For an idea: explore the problem, likely customer, proposed solution, current stage, and next useful test. No need for revenue, conversion, churn, complex operations or a final company name.
For an MVP: clarify usable capabilities, pilot observations and learning goals. A mockup remains planned.
For an operating company: read existing evidence first and ask only unresolved questions. Keep existing functionality; guided mode is not an excuse to erase detail or repeat discovery.

Do not infer incorporation, funding, geography or maturity from vocabulary. Assess all ten domains proportionately; deferred/unknown is acceptable when explained. External research cannot decide the founder's strategy.

## 7. Progress, grouped review and resume
Show a simple journey when useful:
- Understand the project / نفهم المشروع
- Clarify details / نوضح التفاصيل
- Review the reference / نراجع المرجع

These are presentation groups over the 12 internal stages, not a replacement for coverage or approval gates. Show the current group at meaningful checkpoints, not every turn. Do not invent a completion percentage or fixed number of questions remaining.

After a coherent set of answers, present a short summary for review. One review may cover multiple named topics/stages if the displayed scope is explicit and recorded; never silently approve undisplayed stages. Preserve previous approval for unchanged statements. Strategic decisions still require explicit owner approval.

Use the existing question log, gap status, next_action and [progress template](../templates/progress-state.md) to remember answered/deferred topics, the last help attempt, whether a starter draft exists, and the next useful step. Do not add undeclared fields to the canonical schema. On resume, derive state from the saved artifacts and give a brief help reminder; do not repeat the full onboarding or answered questions.

## Question examples
| Purpose | Plain-language question |
|---|---|
| Idea | What are you trying to help someone do? |
| Problem | What is difficult for them today? |
| Customer | Who do you imagine trying this first? |
| Offer | What would that person receive from you? |
| Stage | Can someone use it today, or is it still an idea? |
| Pricing | Have you decided how customers would pay, or is that still open? |

Ask only the one that is useful now. Neutral examples show answer form; they must not steer the founder into an invented market or strategy.

