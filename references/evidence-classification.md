# Evidence classification and provenance

| Kind | Meaning | Minimum basis | Example |
|---|---|---|---|
| confirmed_fact | Verified, scoped present/past assertion | Supporting source, verified_at, method | "Pilot had 12 accounts as of 2026-10-31" |
| founder_decision | Explicitly chosen direction or rule | Founder/delegated owner approval and source | "Focus on UAE independent gyms" |
| research_evidence | What an external source reports | Public source, dated retrieval, scoped attribution | "Competitor lists AED 99 on its price page" |
| hypothesis | Testable belief not established | Rationale; optional evidence | "Owners may value WhatsApp reminders" |
| aspiration | Desired future state or target | Owner and horizon where known | "Aim for 1,000 customers next year" |
| unknown | Material information not available | value=null, gap/next step | "Willingness to pay has not been tested" |

Kind is epistemic status. review.status is owner acceptance of wording/decision. lifecycle is active/superseded/retracted. temporal_status is current/historical/planned/unknown. Keep all four axes distinct.

## Atomic records
Use one independently reviewable statement per record. Record subject_key (for example pricing.base_monthly), domain, value, scope, owner, sources, verified_at, next_review_at, confidence with rationale, sensitivity, and review.

Split "the app exists and customers love it" into at least two claims. Product existence does not establish customer sentiment.

## Verification methods
- direct_observation: observed artifact or operation, with a dated locator.
- corroborated: evidence supports the claim; explain its scope.
- founder_attested: owner confirms an internal matter; disclose self-reported basis.
- not_verified: required for unknowns and normal for early hypotheses.

confirmed_fact cannot use not_verified. Founder attestation cannot establish an external market fact. A confirmed fact with temporal_status=planned is invalid; future plans belong to founder decisions or aspirations.

## Confidence
Use high, medium, low, unassessed, with a sentence explaining why. This is a qualitative assessment of evidence fit, recency, and consistency, not a calibrated probability. Unknown uses unassessed. Review must not automatically raise confidence.

## Freshness
Set review dates according to volatility and purpose, not universal truth: prices/features may need early review; historical incorporation facts usually change less often. Unknown review dates are allowed with a reason in notes. Overdue does not mean false; exclude or refresh overdue claims when the use requires current truth.

## Contradictions
Match subject_key plus scope/time before calling two records contradictory. Retain conflicting active versions with a critical or noncritical gap until resolved. A documented decision can change a policy; it cannot rewrite history.

## Example
"We believe small studios prefer annual billing."
kind=hypothesis; review=approved after founder review; confidence=low; sources point to the founder statement; no verified fact is created.

After dated customer interviews, add research/customer evidence with sample limits. If the hypothesis is supported, add a scoped confirmed_fact with new provenance and supersede only the assertion actually replaced.

