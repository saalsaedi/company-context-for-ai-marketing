# Local validation report

Package: AI Company Context Architect 1.0.0  
Date: 2026-11-14

Publication check: 2026-11-18. Re-ran all 38 contract tests and the skill frontmatter validator after adding the public title, bilingual installation guide, and Codex adapter; all passed. Live-platform acceptance remains not run.

## Observed local results

| Check | Result |
|---|---|
| Python unittest contract suite | PASS: 38 tests |
| JSON Schema Draft 2020-12 definitions | PASS: all 8 schemas checked |
| Fictional idea-stage bundle | PASS: no errors; one expected research-gap warning |
| Skill frontmatter/name validation | PASS: bundled skill validator returned valid; description shortened to fit Claude's documented 200-character limit |
| Local Markdown reference resolution | PASS |
| Public/internal export and metadata filtering | PASS on synthetic fixtures/canaries |
| Export manifests, hashes and overwrite prevention | PASS |
| Deterministic ZIP and single skill-folder root | PASS |
| Arabic UTF-8 roundtrip | PASS |

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
- The 16 behavioral scenario categories on either target model: not run.
- Real-company source truth, founder authority, interview quality and cross-chat persistence: not established by local tests.
- Automated checks detect contract violations and some exact-scope conflicts; they do not prove factual correctness, detect every paraphrased contradiction, or enforce access control.
- The exporter filters by labels and omits private metadata. Human review remains necessary for sensitive text incorrectly labeled public.

Delivery status: final specification and reference package complete; locally validated. Live-platform acceptance remains pending and is explicitly separated from the local results.

