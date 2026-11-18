# Company context for AI marketing

Build a reusable, evidence-linked company reference for AI marketing and company-wide work.

**English / العربية · Claude · Codex · ChatGPT · v1.0.0**

This portable skill combines adaptive founder interviews, document review, and targeted research. It helps idea-stage startups, MVPs, and operating companies capture what is known, what has been decided, and what still needs testing.

The underlying workflow and installed identifier remain **AI Company Context Architect** / **ai-company-context-architect**. The scope includes the whole company, so marketing assistants can work from accurate product, customer, brand, business, operations, data, and governance context.

## Download

- [Latest release and installation files](https://github.com/saalsaedi/company-context-for-ai-marketing/releases/latest)
- [Claude / Codex skill ZIP](https://github.com/saalsaedi/company-context-for-ai-marketing/releases/latest/download/ai-company-context-architect-1.0.0.zip)
- [ChatGPT setup ZIP](https://github.com/saalsaedi/company-context-for-ai-marketing/releases/latest/download/chatgpt-setup-1.0.0.zip)

Use the attached skill ZIP for installation. It contains the correctly named skill folder and supporting files.

## What it does

- **Build:** create context from available evidence and focused questions.
- **Audit:** identify gaps, contradictions, unsupported claims, and stale information.
- **Update:** revise context while preserving history and unchanged approvals.
- **Export:** create task- and audience-specific context for AI assistants.

Includes 12 stage protocols, 8 JSON Schemas, 9 output templates, shared interview/research/validation guidance, and optional local helpers.

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

## First message

~~~text
Use AI Company Context Architect in Build mode to create the core context for my company.
Company: [name]
What we do: [short description]
Stage: [idea / MVP / launched / operating]
Available material: [attached documents / no documents yet]
Main AI use: [marketing, product, support, or another task]

Read the skill instructions and available material first. Speak in my preferred language. Ask 1–3 useful questions at a time and reuse information I already supplied. Keep facts, decisions, hypotheses, goals, and unknowns distinct. Show each stage summary for review. Save the context and a resume packet when supported.
~~~

## البدء بالعربية

السكيل تساعدك في بناء مرجع موثوق للشركة تستخدمه مع الذكاء الاصطناعي، وتشمل التسويق وبقية مجالات الشركة. لغة المحاورة والمخرجات تتكيف مع المستخدم.

- **Claude:** حمّل حزمة السكيل من الإصدار، وارفع ملف ZIP في Customize → Skills ثم فعّله.
- **Codex:** فك الحزمة وانسخ مجلد السكيل كاملًا إلى .agents/skills في مجلد المستخدم.
- **ChatGPT:** حمّل حزمة الإعداد، والصق التعليمات في مشروع، وأرفق ملفّي التشغيل والقوالب.

ابدأ بهذه الرسالة:

~~~text
استخدم مهارة AI Company Context Architect لبناء سياق شركتي بالكامل.
اسم الشركة: [الاسم]
فكرتها: [الوصف]
مرحلتها: [فكرة / منتج أولي / أُطلقت / شركة تعمل]
تحدث معي بالعربية. اقرأ التعليمات والمستندات أولًا، ثم اسألني من سؤال إلى ثلاثة أسئلة في كل مرة. فرّق بين الحقائق والفرضيات والقرارات والأهداف، واعرض ملخص كل مرحلة للمراجعة.
~~~

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

The build writes a native skill ZIP and consolidated ChatGPT reference files outside the source directory. No credentials or API calls are required.

**Validation status:** 38 local contract tests passed. Live Claude/Codex/ChatGPT activation and model-behavior acceptance tests have not been run. Schema checks do not certify the factual truth of company statements.

