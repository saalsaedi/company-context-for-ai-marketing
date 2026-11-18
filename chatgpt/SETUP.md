# ChatGPT adapter

Checked against official documentation on 2026-11-14. Default deployment is a Project with instructions and reference files.

## Project setup
The build creates a dist/chatgpt folder. Paste project-instructions.txt into the project's instruction field. Attach workflow-reference.txt and templates-and-schemas.txt as project sources. Attach real company material separately, with one company per project where practical.

Projects support project instructions and files; instructions apply within that project. Availability and file limits depend on the actual account/workspace. [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

Start with: "Use AI Company Context Architect. Read the attached workflow and templates. Build our company context from these files; ask only for missing information."

The two consolidated text files preserve original path markers. To load stages/05-customer-intelligence.md, locate its FILE marker in workflow-reference.txt. This supports hosts that do not expose an attached folder as a filesystem. If a file cannot be read, ask for the needed excerpt; do not claim it was loaded.

## Behavior contract
The pasted project instructions contain essential workflow and evidence rules. Reference files supply details; uploading documents alone is not the activation contract. Check actual tools: file read/write, browsing, code, and durable storage.

If code is available, attach/extract the source ZIP in the execution environment before using helpers, and verify the dependency exists. A generated download does not prove the source/project files were updated. Save and reattach the latest canonical context.json when needed.

## Other surfaces
For ordinary chat, paste project-instructions.txt and attach the two references. Return a resume packet if persistence is absent.

For an existing custom GPT where configuration remains available, map behavioral rules to Instructions and reference material to Knowledge, then test in Preview. This is an optional route: OpenAI's current documentation describes a transition away from custom GPTs, so it is not the package's default dependency. [Creating/editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts), [GPTs in ChatGPT](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt).

For other skill/plugin-capable ChatGPT environments, inspect supported installation capabilities before adapting the same core. This package does not assume a universal ChatGPT ZIP installer.

## Acceptance
Run the manual scenarios in tests/TEST-PLAN.md. Verify the assistant reads the requested FILE marker, preserves uncertainty, switches Arabic/English without resetting, exports only the allowed scope, and resumes from a supplied bundle in a new chat.

No live ChatGPT project installation or model acceptance test was performed for this local package.

