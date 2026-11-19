# Local validation report

Package: AI Company Context Architect 1.1.0  
Date: 2026-11-19

Release check: 2026-11-19. All 45 local tests passed (38 existing contract tests plus 7 distribution checks), the skill frontmatter validator passed, and the existing fictional company bundle still validated. Live-platform installation acceptance remains not run. Independent founder simulation is reported separately in [beginner-evaluation.md](beginner-evaluation.md).

## Observed local results

| Check | Result |
|---|---|
| Python unittest contract/distribution suite | PASS: 45 tests |
| JSON Schema Draft 2020-12 definitions | PASS: all 8 schemas checked |
| Fictional idea-stage bundle | PASS: no errors; one expected research-gap warning |
| Skill frontmatter/name validation | PASS: bundled skill validator returned valid; description shortened to fit Claude's documented 200-character limit |
| Local Markdown reference resolution | PASS |
| Public/internal export and metadata filtering | PASS on synthetic fixtures/canaries |
| Export manifests, hashes and overwrite prevention | PASS |
| Deterministic ZIP and single skill-folder root | PASS |
| Arabic UTF-8 roundtrip | PASS |
| Shared guided rules and opening in both distributions | PASS: source content preserved in native ZIP and ChatGPT references |
| Both versioned ZIPs and SHA-256 checksums | PASS: deterministic bytes and correct hashes |
| Previous downloads / company-schema compatibility | PASS: old archives untouched; schema stays 1.0.0 |
| Independent founder simulations | PASS after a short-opening correction: 11 fictional sessions covering 12 behavior criteria; see evaluation and exact transcripts |

The sample's unresolved market research is intentional. It is labeled ready_with_caveats for its limited planning use; no market-size claim is invented.

Environment: Python 3.12.10; jsonschema 4.26.0; Windows. The optional frontmatter check used PyYAML 6.0.3. Dependencies were installed into a local build directory, which is excluded from the package. Runtime helpers require only the dependency declared in requirements.txt.

Commands run from the project workspace (with the local dependency directory on Python's module path):

~~~text
python -m unittest discover -s ai-company-context-architect/tests -p "test_*.py" -v
python ai-company-context-architect/scripts/validate_context.py ai-company-context-architect/tests/fixtures/idea-company.json --as-of 2026-11-14
python <bundled-skill-creator>/scripts/quick_validate.py ai-company-context-architect
~~~

## Not run / limitations

- Live Claude upload/activation and ChatGPT project installation: not run.
- The original 16 platform scenario categories on Claude/ChatGPT: not run. Isolated v1.1 founder simulations are a separate evidence level, documented in the linked evaluation.
- Real-company source truth, founder authority, interview quality and cross-chat persistence: not established by local tests.
- Automated checks detect contract violations and some exact-scope conflicts; they do not prove factual correctness, detect every paraphrased contradiction, or enforce access control.
- The exporter filters by labels and omits private metadata. Human review remains necessary for sensitive text incorrectly labeled public.

Delivery status: final specification and reference package complete; locally validated. Live-platform acceptance remains pending and is explicitly separated from the local results.

