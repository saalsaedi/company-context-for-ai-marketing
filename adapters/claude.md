# Claude adapter

Checked against official documentation on 2026-11-14.

## Native activation
Where custom skills are available, upload the distribution ZIP containing the ai-company-context-architect folder and SKILL.md. Enable it in Customize > Skills. Account/workspace capabilities and code execution settings determine availability. Follow the current UI if labels change. [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [Use skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Invoke with a normal request such as "Use AI Company Context Architect to build context for my MVP." Verify actual activation with a small test before using live company data.

Claude Code can use a filesystem skill folder under .claude/skills/ for the project, or its user skill directory. Skills are managed separately across Claude surfaces; there is no assumed automatic synchronization. [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Runtime mapping
| Core need | Adapter behavior |
|---|---|
| Instructions | Load SKILL.md, current stage and relevant reference |
| Documents | Use available file tools; report unreadable files |
| Research | Use exposed research tools when present; network access is not assumed |
| Validation | Run Python helper only if execution/dependency is available |
| Checkpoint | Save artifacts where supported; return downloadable files or text otherwise |
| Resume | Load prior context.json supplied in the next session |
| External sharing | Follow explicit task scope; local release does not imply publication |

Do not place live company context into the reusable skill ZIP. Keep it in a separate project/company workspace.

## Fallback
If native installation is unavailable, provide SKILL.md as instructions and the relevant references/stages as attachments, or paste their needed contents. State that this is a conversation-driven workflow, not a verified native installation. Use the same evidence and review rules.

## Acceptance
Run tests/idea-stage-company.md and tests/adversarial-and-portability.md in the actual surface. Then restart a chat with a saved bundle and verify resume. Native upload and live-model behavior have not been tested as part of this local package.

