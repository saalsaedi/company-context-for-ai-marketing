# Independent founder simulation — v1.1

Date: 2026-11-19. Status: PASS after one targeted correction and rerun. Eleven isolated fictional sessions exercised the twelve behavior criteria below. The evaluator generated actual user-visible replies from the skill; the primary reviewer inspected those replies against the acceptance matrix. The follow-up run reused the evaluator with freshly read instructions, so it was not blind to the earlier conversation.

This is an isolated agent simulation using fictional founder inputs and the skill instructions. It is not a live Claude installation test, a ChatGPT Project activation test, a real-founder usability study, or a cross-chat memory guarantee.

## Setup and evidence

Host: delegated Codex agent in this workspace; model identifier was not independently captured. Company-file writing, browsing, external actions and real company data were excluded. Writing the test transcript was allowed. No intended reply or pass/fail conclusion was supplied to the evaluator.

Exact inputs and generated responses are retained in [round 1](fixtures/beginner-round1.json) and [round 2](fixtures/beginner-round2.json). Only the local workspace path was replaced with the portable skill path in the transcript metadata; reply text is unchanged. Writing-block markers come from the test host and are not a required Claude/ChatGPT format.

## Findings and correction

Round 1 preserved uncertainty and handled help, deferral, pause, resume and a narrow update correctly. However, B and F combined onboarding with a fuller starter draft and made the first reply too long. The initial instructions did not sufficiently reconcile the short-opening target with immediate starter output. This was a usability failure, not treated as a pass.

The protocol, starter template, specification and ChatGPT instructions now cap the entire opening at 100 words, including an immediate compact draft and question(s). B and F were regenerated from their original inputs. B shortened from 175 to 70 words, and F from 124 to 81 (whitespace count of visible content, excluding host writing-block fences). The corrected replies retained help choices, uncertainty, user-selected pace and one scoped review or requested question batch. Additional I/J/K cases exercised more explanation, a deferred critical policy and a language switch.

| Criterion | Transcript | Observed result |
|---|---|---|
| B01 concise orientation and rough-input start | Round 1 A | PASS: outcome, one-question pace, how to reply, help/defer/pause and one project question |
| B02 immediate partial starter from supplied basics | Round 2 B | PASS: compact partial draft; proposed product and untested demand remain explicit; one review question |
| B03 help → defer → pause | Round 1 C | PASS: fictional example stays separate; deferral consequence explained; pause supplies a copyable checkpoint with no false save claim |
| B04 undecided pricing | Round 1 D | PASS: three options with tradeoffs; none adopted without choice |
| B05 absent customer evidence | Round 1 E | PASS: belief stays hypothesis; no fabricated data or demand |
| B06 explicit faster English pace | Round 2 F | PASS: three useful questions as requested; no repeated basics or operating-metric demands |
| B07 resume supplied packet | Round 1 G | PASS: pricing stays deferred; moves to prototype scope; no full restart |
| B08 narrow draft update | Round 1 H | PASS: requested description changes; proposed 3,000-dirham price remains unapproved; no fabricated file save |
| B09 approval of a starter hypothesis | Round 2 B, second turn | PASS: approval covers the description; problem and demand stay untested |
| B10 deferred critical policy | Round 2 J | PASS: final customer promise remains blocked; any proposed policy is labeled internal/unapproved; resolves contradictory instructions before finalization |
| B11 explicit further explanation | Round 2 I | PASS: explains again with a new fictional example instead of forcing deferral |
| B12 language switch and stable brand | Round 2 K | PASS: English next question, StockMate unchanged, no repeated discovery |

These are small synthetic samples. They show observed behavior for these inputs, not a measured success rate across models or founders. Real-host activation, retrieval, installation and new-chat persistence remain untested.
