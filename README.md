# Company context for AI marketing

Build a reusable, evidence-linked company reference for AI marketing and company-wide work.

**English / العربية · Claude · Codex · ChatGPT · v1.1.0**

This portable skill combines adaptive founder interviews, document review, and targeted research. It helps idea-stage startups, MVPs, and operating companies capture what is known, what has been decided, and what still needs testing.

The underlying workflow and installed identifier remain **AI Company Context Architect** / **ai-company-context-architect**. The scope includes the whole company, so marketing assistants can work from accurate product, customer, brand, business, operations, data, and governance context.

## Download

- [Latest release and installation files](https://github.com/saalsaedi/company-context-for-ai-marketing/releases/latest)
- [Claude / Codex skill ZIP](https://github.com/saalsaedi/company-context-for-ai-marketing/raw/refs/heads/main/downloads/ai-company-context-architect-1.1.0.zip)
- [ChatGPT setup ZIP](https://github.com/saalsaedi/company-context-for-ai-marketing/raw/refs/heads/main/downloads/chatgpt-setup-1.1.0.zip)

Use the packaged skill ZIP for installation. It contains the correctly named skill folder and supporting files.

## What it does

- **Build:** create context from available evidence and focused questions.
- **Audit:** identify gaps, contradictions, unsupported claims, and stale information.
- **Update:** revise context while preserving history and unchanged approvals.
- **Export:** create task- and audience-specific context for AI assistants.

Includes 12 stage protocols, 8 JSON Schemas, 10 Markdown output templates and bilingual opening copy, shared interview/research/validation guidance, and optional local helpers.

Six kinds stay distinct: confirmed facts, founder decisions, research evidence, hypotheses, aspirations, and unknowns. Approving a hypothesis does not make it a fact.

## Install on Claude

1. Download the skill ZIP from the release.
2. Enable **Code execution and file creation** / **Create and edit files** in settings.
3. Open **Customize → Skills → + → Create skill → Upload a skill**.
4. Upload the ZIP without extracting it and enable the skill.
5. Start a chat and ask to use **AI Company Context Architect**.

See the [Claude adapter](adapters/claude.md) and [official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Availability depends on the workspace's enabled capabilities.

## Install on Codex

1. Extract the skill ZIP.
2. Copy the entire ai-company-context-architect folder to your personal skill directory:
   - Windows: %USERPROFILE%\.agents\skills\
   - macOS/Linux: ~/.agents/skills/
3. Ensure SKILL.md is directly inside that folder, alongside its supporting folders.
4. Start a new chat. If it is not discovered, restart Codex.
5. Ask to use the skill by name; in Codex CLI/IDE, mention $ai-company-context-architect.

For project-local use, put the folder in .agents/skills/ inside the project. See the [Codex adapter](adapters/codex.md) and [official guide](https://learn.chatgpt.com/docs/build-skills).

## Use in a ChatGPT Project

1. Download and extract the ChatGPT setup ZIP.
2. Create a project for your company.
3. Paste project-instructions.txt into the project's instruction field.
4. Attach workflow-reference.txt and templates-and-schemas.txt as project sources.
5. Add company documents separately and start a chat inside the project.

The files are also in the [chatgpt folder](https://github.com/saalsaedi/company-context-for-ai-marketing/tree/main/chatgpt). See the [ChatGPT adapter](adapters/chatgpt.md).

## Start with one sentence

~~~text
Use AI Company Context Architect. Help me build my company reference, one question at a time.
~~~

Add a rough idea if you have one. No company name, documents, business vocabulary or completed questionnaire is required. The skill explains how to reply, uses your own words, offers help and shows a short first draft early. That draft clearly marks unknowns and still needs the remaining company coverage and review.

You can say **explain**, **give an example**, **I don't know**, **defer**, or **pause**. If you want a faster pace, ask for several questions together. On resume, provide the latest saved context and progress packet.

## البدء بالعربية

السكيل ترتّب معلومات شركتك في مرجع تستخدمه مع الذكاء الاصطناعي. تقدر تبدأ حتى لو مشروعك مجرد فكرة، وما عندك اسم أو مستندات.

ابدأ بهذه الرسالة:

~~~text
استخدم سكيل AI Company Context Architect وساعدني أبني مرجع شركتي، سؤال واحد كل مرة.
~~~

تكون البداية بهذا الأسلوب، ويتغير السؤال إذا سبق وشرحت مشروعك:

> بنجهّز مرجع واضح لشركتك خطوة بخطوة. بسألك سؤالًا واحدًا كل مرة؛ جاوب بكلامك، حتى لو بجملة أو فكرة غير مكتملة. تقدر تقول: «اشرح لي»، «عطني مثال»، «ما أعرف»، «نؤجل»، أو «نوقف ونكمل لاحقًا». بنوضح الافتراضات، وأعرض لك ملخصًا تراجعه.
>
> **احكِ لي عن مشروعك بجملة أو جملتين: وش تحاول تسوي؟**

الرد بجملة أو نقاط يكفي. إذا ما فهمت السؤال، اطلب شرحًا أو مثالًا. وإذا ما قررت أو ما عندك بيانات، قل ذلك؛ السكيل تساعدك بالخيارات وتوضح الافتراضات. تقدر تؤجل أي موضوع أو توقف وتكمل من ملخص التقدم. ستظهر مسودة أولية مبكرًا، ثم تُستكمل تفاصيل الشركة ومراجعتها.

## Upgrade from v1.0

Keep your company context and progress files in a separate workspace. Download v1.1.0, then replace the older skill in Claude using its Skills settings, or replace the installed ai-company-context-architect folder in Codex. Start a new chat. In ChatGPT, replace the project instructions and both reference files with the new versions; remove the older copies to avoid conflicting instructions. Supply your saved company context to continue.

The installed skill name and company schema remain unchanged. Old company bundles remain supported. [Release notes](CHANGELOG.md) describe the seven improvements; the old v1.0.0 release stays available.

## Outputs and resumption

The skill produces a Company Context Master, concise AI operational context, domain packs, evidence/assumption registers, progress state, and a change log.

Keep real company data in a separate workspace. Save the latest context.json and progress summary, then supply them when resuming in another chat or platform. No automatic cross-platform sync is assumed.

All included company fixtures are fictional. The reusable package contains no real company context.

## Documentation

- [Implementation specification and architecture](IMPLEMENTATION-SPEC.md)
- [Portable skill instructions](SKILL.md)
- [Stage engine](references/adaptive-stage-engine.md)
- [Validation protocol](references/validation-protocol.md)
- [Privacy and export rules](references/privacy-and-governance.md)
- [Test plan](tests/TEST-PLAN.md)
- [Observed validation results](tests/VALIDATION-REPORT.md)

## Optional local verification

Python 3.10+ is needed only for helpers.

~~~text
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_context.py tests/fixtures/idea-company.json --as-of 2026-11-14
python scripts/build_package.py --output-dir ../dist
~~~

The build writes both installation ZIPs, consolidated ChatGPT reference files, and versioned SHA-256 checksums outside the source directory, using release.json. No credentials or API calls are required.

**Validation status:** see the [observed validation report](tests/VALIDATION-REPORT.md) for executed checks and limitations. Live Claude/ChatGPT installation acceptance remains pending. Schema checks do not certify the factual truth of company statements.

