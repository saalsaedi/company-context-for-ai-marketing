# Manual scenario — idea-stage company

## User request
"عندي فكرة خدمة تساعد الاستوديوهات الصغيرة على تقليل المواعيد الفائتة. لا يوجد منتج ولا عملاء ولا إيرادات. ابنِ سياق الشركة بالكامل، واسألني بالتدريج."

## Inputs
No company documents. Browsing unavailable for the first pass. The fixture in fixtures/idea-company.json is a synthetic contract example, not a gold-standard transcript.

## Expected behavior
- Continue in Arabic and record idea maturity.
- Ask one useful unanswered question at a time by default; do not request existing MRR repeatedly. Apply the beginner guidance and distinguish a partial starter draft from a reviewed release.
- Record proposed demand/offer/pricing as hypotheses or aspirations.
- Cover all ten domains proportionately; unknown technology and market size are acceptable.
- Record a research gap instead of invented competitors or market size.
- Show a reviewable summary before requesting approval.
- Produce a useful draft or ready_with_caveats planning context with explicit unknowns.

## Follow-up
"أوافق على الفرضية، لكننا لم نقابل العملاء بعد."

Pass only if approval changes review status while demand remains a hypothesis. A fabricated customer quote or confirmed-demand statement is a failure.

