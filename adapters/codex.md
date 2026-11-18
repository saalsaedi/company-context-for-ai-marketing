# Codex adapter

Local installation guidance checked against the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) on 2026-11-18.

## Install

Extract the release skill ZIP and place the entire ai-company-context-architect folder in the personal .agents/skills directory under the user's home directory. On Windows this is %USERPROFILE%\.agents\skills; on macOS/Linux it is ~/.agents/skills.

For a project-only installation, place the folder in .agents/skills inside that project. Keep SKILL.md directly inside the skill folder, with all supporting files intact. Avoid duplicate installations at multiple scopes unnecessarily.

Codex detects changes automatically; start a new chat and restart Codex if the skill does not appear. In CLI/IDE, invoke by $ai-company-context-architect or use the skills selector. In the desktop app, select the skill or ask for it by name.

## Runtime contract

The core workflow remains SKILL.md. Read the current stage and relevant references on demand. Store real company artifacts in a separate workspace, not inside the reusable skill.

Inspect actual file, research, execution, and persistence capabilities. Helpers are optional and require the dependency in requirements.txt. Do not claim automated validation without running it.

Use the same Build/Audit/Update/Export rules, evidence classifications, language adaptation, review gates, and scoped exports. This adapter does not expand permissions or authorize external publishing.

## Resume and validation

Load saved context.json before continuing. Check company ID and version; reuse answered questions and unchanged approvals. Return named files or a resume packet if the environment cannot save them.

Run behavioral cases in tests/TEST-PLAN.md on the chosen Codex surface before claiming tested live compatibility. Local package tests are separate from that acceptance step.

