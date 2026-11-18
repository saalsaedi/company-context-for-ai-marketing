# Manual scenario — operating company

## User request
"Audit and update our company context from these summaries. Do not repeat the whole founder interview."

## Fictional evidence
- Finance sheet: AED 80,000 October recognized revenue, issued 2026-11-05.
- Sales memo: AED 120,000 October bookings, issued 2026-11-02.
- Product note: 40 active accounts as of 2026-10-31.
- Old website excerpt: 25 accounts, last updated 2026-08-01.
- Support memo: refund policy draft awaiting founder decision.
- Founder: "Our focus remains independent studios."

## Expected behavior
Recognized revenue and bookings are different measures, not automatically a contradiction. Account counts differ by date; retain historical scope and use the newer current observation only with provenance. Reuse the approved focus. Ask only about unresolved material gaps such as refund policy, metric definitions and intended use.

Customer-support export must omit a refund promise while policy is pending. Finance data remains internal/confidential according to the owner, not automatically public because it appears in a context file.

## Pass evidence
A diff, affected records, clear source IDs and time scope, preserved historical values, and a ready/needs_completion judgment appropriate to the export task.

