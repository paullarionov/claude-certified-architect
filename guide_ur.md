# Claude Certified Architect — Foundations Certification

## مطالعہ گائیڈ (سرکاری امتحانی گائیڈ کی بنیاد پر)

---

## تعارف

**Claude Certified Architect — Foundations** سرٹیفیکیشن اس بات کی تصدیق کرتی ہے کہ ایک ماہر حقیقی دنیا کے Claude-based حل نافذ کرتے وقت درست trade-off فیصلے کر سکتا ہے۔ یہ امتحان Claude Code، Claude Agent SDK، Claude API، اور Model Context Protocol (MCP) کے بنیادی علم کا جائزہ لیتا ہے — یعنی وہ بنیادی ٹیکنالوجیز جن سے Claude کے ساتھ پروڈکشن ایپلیکیشنز بنائی جاتی ہیں۔

امتحانی سوالات حقیقت پسندانہ صنعتی منظرناموں پر مبنی ہوتے ہیں: کسٹمر سپورٹ کے لیے agentic systems بنانا، multi-agent research pipelines ڈیزائن کرنا، Claude Code کو CI/CD میں ضم کرنا، developer productivity tools بنانا، اور غیر ساختہ دستاویزات سے structured data نکالنا۔

---

## ہدف امیدوار

مثالی امیدوار ایک **solution architect** ہے جو Claude کے ساتھ پروڈکشن ایپلیکیشنز ڈیزائن اور ship کرتا ہے۔ آپ کے پاس کم از کم 6 ماہ کا عملی تجربہ ہونا چاہیے:

- **Claude Agent SDK** — multi-agent orchestration، subagents کو delegate کرنا، tool integration، lifecycle hooks
- **Claude Code** — CLAUDE.md، MCP servers، Agent Skills، planning mode
- **Model Context Protocol (MCP)** — backend integration کے لیے tools اور resources
- **Prompt engineering** — JSON schemas، few-shot examples، data extraction templates
- **Context windows** — لمبی دستاویزات کے ساتھ کام، multi-agent context passing
- **CI/CD pipelines** — automated code review، test generation
- **Escalation and reliability** — error handling، human-in-the-loop

---

## امتحانی فارمیٹ

| پیرامیٹر | قدر |
|---|---|
| سوال کی قسم | Multiple choice (4 میں سے 1 درست) |
| اسکورنگ | 100–1000 scale، passing score **720** |
| Guessing penalty | نہیں (ہر سوال کا جواب دیں!) |
| Scenarios | 6 میں سے 4 (randomly selected) |

---

## امتحانی مواد: 5 ڈومینز

| ڈومین | وزن |
|---|---|
| 1. Agent architecture and orchestration | **27%** |
| 2. Tool design and MCP integration | **18%** |
| 3. Claude Code configuration and workflows | **20%** |
| 4. Prompt engineering and structured output | **20%** |
| 5. Context management and reliability | **15%** |

---

## امتحانی منظرنامے

### Scenario 1: Customer Support Agent
آپ ایک agent بناتے ہیں جو Claude Agent SDK استعمال کرتے ہوئے returns، billing disputes، اور account issues سنبھالتا ہے۔ یہ agent MCP tools (`get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`) استعمال کرتا ہے۔ ہدف 80%+ first-contact resolution ہے، مناسب escalation کے ساتھ۔

### Scenario 2: Claude Code کے ساتھ Code Generation
آپ Claude Code کو development تیز کرنے کے لیے استعمال کرتے ہیں: code generation، refactoring، debugging، documentation۔ آپ کو اسے custom slash commands اور CLAUDE.md configuration کے ساتھ integrate کرنا ہے، اور یہ سمجھنا ہے کہ planning mode کب استعمال کرنا ہے۔

### Scenario 3: Multi-Agent Research System
ایک coordinator agent specialized subagents کو tasks سونپتا ہے: web research، document analysis، synthesis، اور report generation۔ سسٹم کو citations کے ساتھ مکمل reports تیار کرنے چاہئیں۔

### Scenario 4: Developer Productivity Tools
یہ agent engineers کو unfamiliar codebases explore کرنے، boilerplate code بنانے، اور routine tasks automate کرنے میں مدد دیتا ہے۔ Built-in tools (Read، Write، Bash، Grep، Glob) اور MCP servers استعمال کیے جاتے ہیں۔

### Scenario 5: Claude Code for Continuous Integration
Claude Code کو CI/CD pipeline میں ضم کریں تاکہ automated code reviews، test generation، اور pull request feedback حاصل ہو۔ Prompts ایسے ڈیزائن ہونے چاہئیں کہ false positives کم سے کم ہوں۔

### Scenario 6: Structured Data Extraction
سسٹم غیر ساختہ دستاویزات سے معلومات نکالتا ہے، output کو JSON schemas کے ذریعے validate کرتا ہے، اور high accuracy برقرار رکھتا ہے۔ اسے edge cases کو درست طور پر سنبھالنا چاہیے۔

---

# سرکاری دستاویزات

| وسیلہ | URL |
|---|---|
| **Claude API — Messages** | https://platform.claude.com/docs/en/api/messages |
| **Claude API — Tool Use** | https://platform.claude.com/docs/en/build-with-claude/tool-use |
| **Claude API — Message Batches** | https://platform.claude.com/docs/en/build-with-claude/message-batches |
| **Claude Agent SDK — Overview** | https://platform.claude.com/docs/en/agent-sdk/overview |
| **Claude Agent SDK — Hooks** | https://platform.claude.com/docs/en/agent-sdk/hooks |
| **Claude Agent SDK — Subagents** | https://platform.claude.com/docs/en/agent-sdk/subagents |
| **Claude Agent SDK — Sessions** | https://platform.claude.com/docs/en/agent-sdk/sessions |
| **Model Context Protocol (MCP)** | https://modelcontextprotocol.io/ |
| **MCP — Tools** | https://modelcontextprotocol.io/docs/concepts/tools |
| **MCP — Resources** | https://modelcontextprotocol.io/docs/concepts/resources |
| **MCP — Servers** | https://modelcontextprotocol.io/docs/concepts/servers |
| **Claude Code — Documentation** | https://code.claude.com/docs/en/overview |
| **Claude Code — CLAUDE.md and Memory** | https://code.claude.com/docs/en/memory |
| **Claude Code — Skills (incl. slash commands)** | https://code.claude.com/docs/en/skills |
| **Claude Code — Hooks** | https://code.claude.com/docs/en/hooks |
| **Claude Code — Sub-agents** | https://code.claude.com/docs/en/sub-agents |
| **Claude Code — MCP Integration** | https://code.claude.com/docs/en/mcp |
| **Claude Code — GitHub Actions CI/CD** | https://code.claude.com/docs/en/github-actions |
| **Claude Code — GitLab CI/CD** | https://code.claude.com/docs/en/gitlab-ci-cd |
| **Claude Code — Headless (non-interactive mode)** | https://code.claude.com/docs/en/headless |
| **Prompt Engineering Guide** | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview |
| **Extended Thinking** | https://platform.claude.com/docs/en/build-with-claude/extended-thinking |
| **Anthropic Cookbook (code examples)** | https://github.com/anthropics/anthropic-cookbook |

---

# حصہ I: نظریاتی بنیادیں

یہ حصہ وہ تمام نظریہ احاطہ کرتا ہے جس کی آپ کو امتحان میں کامیابی کے لیے ضرورت ہے۔ مواد کو ٹیکنالوجیز اور concepts کے مطابق ترتیب دیا گیا ہے، نہ کہ امتحانی domains کے مطابق — اس سے آپ ہر موضوع کی زیادہ گہری سمجھ پیدا کر سکتے ہیں۔

---

# باب 1: Claude API — Model Interaction کی بنیادیں

> دستاویزات: [Messages API](https://platform.claude.com/docs/en/api/messages) | [Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

## 1.1 API Request Structure

Claude API ایک request–response model کی پیروی کرتا ہے۔ Claude Messages API کی ہر request میں یہ شامل ہوتا ہے:

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "system": "You are a helpful assistant.",
  "messages": [
    {"role": "user", "content": "Hi!"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "How are you?"}
  ],
  "tools": [...],
  "tool_choice": {"type": "auto"}
}
```

**اہم فیلڈز:**
- `model` — model selection (`claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`)
- `max_tokens` — response میں زیادہ سے زیادہ tokens کی تعداد
- `system` — system prompt (model کے رویے کی تعریف کرتا ہے)
- `messages` — conversation history (**تسلسل برقرار رکھنے کے لیے آپ کو مکمل history بھیجنی ہوتی ہے**)
- `tools` — دستیاب tools کی definitions
- `tool_choice` — tool selection strategy

## 1.2 Message Roles

`messages` array تین roles استعمال کرتا ہے:
- `user` — user messages
- `assistant` — model responses (history بھیجتے وقت شامل کیے جاتے ہیں)
- `tool` — tool call results (role واضح طور پر set نہیں کیا جاتا؛ یہ `tool_result` content block کی صورت میں ظاہر ہوتا ہے)

**انتہائی اہم:** ہر API request میں آپ کو **مکمل conversation history** بھیجنی چاہیے۔ Model requests کے درمیان state محفوظ نہیں رکھتا — ہر call آزاد ہوتا ہے۔

## 1.3 Response میں `stop_reason` Field

Claude API response میں `stop_reason` شامل ہوتا ہے، جو بتاتا ہے کہ model نے generation کیوں روکی:

| Value | Description | Action |
|---|---|---|
| `"end_turn"` | Model نے response مکمل کر لیا | نتیجہ user کو دکھائیں |
| `"tool_use"` | Model tool call کرنا چاہتا ہے | Tool execute کریں اور result واپس دیں |
| `"max_tokens"` | Token limit ختم ہو گئی | Response truncated ہے; ممکن ہے limit بڑھانی پڑے |
| `"stop_sequence"` | Stop sequence مل گئی | اپنی application logic کے مطابق handle کریں |

Agentic systems میں `"tool_use"` اور `"end_turn"` سب سے اہم ہیں — یہی agent loop کو کنٹرول کرتے ہیں۔

## 1.4 System Prompt

System prompt ایک خاص instruction ہے جو context اور behavioral rules متعین کرتا ہے۔ یہ:
- `messages` array کا حصہ نہیں ہوتا؛ یہ الگ `system` field میں دیا جاتا ہے
- user messages پر فوقیت رکھتا ہے
- ایک بار load ہوتا ہے اور پوری conversation میں لاگو رہتا ہے
- role، constraints، اور output format کی تعریف کے لیے استعمال ہوتا ہے

**امتحان کے لیے اہم:** system prompt کی wording غیر ارادی tool associations پیدا کر سکتی ہے۔ مثال کے طور پر، “ہمیشہ customer کی تصدیق کریں” جیسی ہدایت model کو `get_customer` کو ضرورت سے زیادہ استعمال کرنے پر مجبور کر سکتی ہے، حتیٰ کہ جب یہ ضروری نہ ہو۔

## 1.5 Context Window

Context window text (tokens) کی کل مقدار ہے جسے model ایک وقت میں process کر سکتا ہے۔ اس میں شامل ہے:
- System prompt
- مکمل message history
- Tool definitions
- Tool results

**اہم context-window مسائل:**

1. **Lost-in-the-middle effect:** models لمبے input کے آغاز اور اختتام پر موجود معلومات کو زیادہ اعتماد سے process کرتے ہیں، مگر درمیان کی تفصیلات miss کر سکتے ہیں۔ حل: اہم معلومات شروع یا آخر کے قریب رکھیں۔

2. **Tool results کا جمع ہونا:** ہر tool call context میں output شامل کرتا ہے۔ اگر tool 40+ fields واپس کرے مگر صرف 5 اہم ہوں، تو context کا بڑا حصہ ضائع ہو جاتا ہے۔

3. **Progressive summarization:** history compress کرتے وقت numeric values، percentages، اور dates اکثر گم ہو کر غیر واضح ہو جاتے ہیں (“تقریباً”، “کچھ”، “چند”)۔

---

# باب 2: Tools اور `tool_use`

> دستاویزات: [Tool Use](https://platform.claude.com/docs/en/build-with-claude/tool-use)

## 2.1 `tool_use` کیا ہے

`tool_use` ایک mechanism ہے جو Claude کو external functions call کرنے کی اجازت دیتا ہے۔ Model براہِ راست code نہیں چلاتا — وہ structured tool call request بناتا ہے؛ آپ کا code اسے execute کرتا ہے اور result واپس کرتا ہے۔

## 2.2 Tool Definition

ہر tool ایک JSON schema کے ذریعے define کیا جاتا ہے:

```json
{
  "name": "get_customer",
  "description": "Finds a customer by email or ID. Returns the customer profile, including name, email, order history, and account status. Use this tool BEFORE lookup_order to verify the customer's identity. Accepts an email (format: user@domain.com) or a numeric customer_id.",
  "input_schema": {
    "type": "object",
    "properties": {
      "email": {"type": "string", "description": "Customer email"},
      "customer_id": {"type": "integer", "description": "Numeric customer ID"}
    },
    "required": []
  }
}
```

**Tool description کے انتہائی اہم پہلو:**

1. **Description tool selection کا بنیادی mechanism ہے۔** LLM tools کو ان کی descriptions کی بنیاد پر منتخب کرتا ہے۔ Minimal descriptions (“Customer information retrieve کرتا ہے”) اُن مواقع پر غلطیوں کا باعث بنتی ہیں جب tools ایک دوسرے سے overlap کرتے ہوں۔

2. **Description میں شامل کریں:**
   - Tool کیا کرتا ہے اور کیا واپس کرتا ہے
   - Input formats اور example values
   - Edge cases اور constraints
   - یہ tool similar alternatives کے مقابلے میں کب استعمال ہو

3. **ایک جیسے یا overlapping descriptions سے بچیں۔** اگر `analyze_content` اور `analyze_document` کی descriptions تقریباً ایک جیسی ہوں، تو model انہیں خلط ملط کر دے گا۔

4. **Built-in tools بمقابلہ MCP tools:** agents similar functionality والے built-in tools (Read، Grep) کو MCP tools پر ترجیح دے سکتے ہیں۔ اس سے بچنے کے لیے MCP tool descriptions مضبوط بنائیں — concrete advantages، unique data، یا وہ context نمایاں کریں جو built-in tools فراہم نہیں کر سکتے۔

## 2.3 `tool_choice` Parameter

`tool_choice` یہ کنٹرول کرتا ہے کہ model tools کیسے منتخب کرتا ہے:

| Value | Behavior | کب استعمال کریں |
|---|---|---|
| `{ "type": "auto" }` | Model خود طے کرتا ہے کہ tool call کرنا ہے یا text میں جواب دینا ہے | زیادہ تر حالات میں default |
| `{ "type": "any" }` | Model کو لازماً کوئی tool call کرنا ہوگی | جب آپ کو guaranteed structured output چاہیے |
| `{ "type": "tool", "name": "extract_metadata" }` | Model کو لازماً ایک مخصوص tool call کرنی ہوگی | جب آپ کو forced first step / execution order چاہیے |

**اہم منظرنامے:**
- `tool_choice: "any"` + multiple extraction tools → model بہترین tool منتخب کرتا ہے، مگر پھر بھی structured output ملتا ہے
- Forced selection → جب آپ کو کسی خاص پہلی action کی ضمانت چاہیے (مثلاً enrichment سے پہلے `extract_metadata`)

## 2.4 Structured Output کے لیے JSON Schemas

JSON schemas کے ساتھ `tool_use` استعمال کرنا Claude سے structured output حاصل کرنے کا **سب سے قابلِ اعتماد** طریقہ ہے۔ یہ:
- Syntax کے اعتبار سے درست JSON کی ضمانت دیتا ہے (braces غائب نہیں ہوتے، trailing commas نہیں ہوتے)
- مطلوبہ structure نافذ کرتا ہے (required fields موجود ہوتے ہیں)
- Semantic correctness کی ضمانت نہیں دیتا (values پھر بھی غلط ہو سکتی ہیں)

**Schema design — بنیادی اصول:**

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "enum": ["bug", "feature", "docs", "unclear", "other"]
    },
    "category_detail": {
      "type": ["string", "null"],
      "description": "Details if category = 'other' or 'unclear'"
    },
    "severity": {
      "type": "string",
      "enum": ["critical", "high", "medium", "low"]
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "optional_field": {
      "type": ["string", "null"],
      "description": "Null if the information was not found in the source"
    }
  },
  "required": ["category", "severity"]
}
```

**Schema design rules:**
1. **Required بمقابلہ optional:** صرف اُن fields کو required بنائیں جن کی معلومات ہمیشہ دستیاب ہو۔ Required fields model کو data غائب ہونے پر values گھڑنے پر مجبور کر سکتی ہیں۔
2. **Nullable fields:** ایسی معلومات کے لیے `"type": ["string", "null"]` استعمال کریں جو ممکنہ طور پر موجود نہ ہوں۔ Model `null` واپس کر سکتا ہے بجائے اس کے کہ وہ خود ساختہ value بنائے۔
3. **Enums with `"other"`:** اپنی predefined categories سے باہر کی معلومات ضائع ہونے سے بچانے کے لیے `"other"` + ایک detail string شامل کریں۔
4. **Enum `"unclear"`:** اُن صورتوں کے لیے جب model category کے بارے میں پُراعتماد نہ ہو — ایماندار `"unclear"` غلط category سے بہتر ہے۔

## 2.5 Syntax بمقابلہ Semantic Errors

| Error type | Example | Mitigation |
|---|---|---|
| **Syntax** | Invalid JSON، غلط field type | JSON schema کے ساتھ `tool_use` (ختم کر دیتا ہے) |
| **Semantic** | Totals match نہیں کرتے، value غلط field میں، hallucination | Validation checks، feedback کے ساتھ retry، self-correction |

---

# باب 3: Claude Agent SDK — Agentic Systems بنانا

> دستاویزات: [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) | [Hooks](https://platform.claude.com/docs/en/agent-sdk/hooks) | [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) | [Sessions](https://platform.claude.com/docs/en/agent-sdk/sessions)

## 3.1 Agentic Loop کیا ہے

Agentic loop خودکار task execution کا بنیادی pattern ہے۔ Model صرف جواب نہیں دیتا — وہ actions کی ایک sequence انجام دیتا ہے:

```
1. Claude کو tools کے ساتھ request بھیجیں
2. Response وصول کریں
3. stop_reason چیک کریں:
   - "tool_use" -> tool execute کریں، result history میں append کریں، step 1 پر واپس جائیں
   - "end_turn" -> task مکمل، result user کو دکھائیں
4. مکمل ہونے تک repeat کریں
```

**یہ model-driven approach ہے:** Claude اپنے context اور پچھلے tool results کی بنیاد پر اگلا tool خود منتخب کرتا ہے۔ یہ hard-coded decision trees سے مختلف ہے جہاں action sequence پہلے سے fixed ہوتی ہے۔

**Anti-patterns (ان سے بچیں):**
- Completion detect کرنے کے لیے assistant text parse کرنا (“Task completed”)
- Primary stop condition کے طور پر arbitrary iteration limit استعمال کرنا (مثلاً `max_iterations=5`)
- یہ چیک کرنا کہ assistant نے textual content دیا ہے یا نہیں، اسے completion signal سمجھنا

**درست طریقہ:** completion کا واحد قابلِ اعتماد signal `stop_reason == "end_turn"` ہے۔

## 3.2 `AgentDefinition` Configuration

`AgentDefinition` Claude Agent SDK میں agent configuration object ہے:

```python
agent = AgentDefinition(
    name="customer_support",
    description="Handles customer requests for returns and order issues",
    system_prompt="You are a customer support agent...",
    allowed_tools=["get_customer", "lookup_order", "process_refund", "escalate_to_human"],
    # Coordinator کے لیے:
    # allowed_tools=["Task", "get_customer", ...]
)
```

**اہم parameters:**
- `name` / `description` — agent کی شناخت اور وضاحت
- `system_prompt` — ہدایات والا system prompt
- `allowed_tools` — اجازت یافتہ tools کی فہرست (least privilege اصول)

## 3.3 Hub-and-Spoke: Coordinator اور Subagents

Multi-agent architecture عموماً hub-and-spoke topology میں بنائی جاتی ہے:

```
         Coordinator
        /     |      \
   Subagent1  Subagent2  Subagent3
    (search)   (analysis)   (synthesis)
```

**Coordinator کی ذمہ داریاں:**
- Task کو subtasks میں تقسیم کرنا
- یہ طے کرنا کہ کون سے subagents درکار ہیں (dynamic selection)
- کام subagents کو سونپنا
- نتائج جمع اور validate کرنا
- Errors اور retries handle کرنا
- نتائج user تک پہنچانا

**اہم اصول: subagents کا context الگ ہوتا ہے۔**
- Subagents خود بخود coordinator کی conversation history inherit نہیں کرتے
- تمام ضروری context subagent prompt میں **واضح طور پر** دینا ہوتا ہے
- Subagents calls کے درمیان memory share نہیں کرتے
- تمام communication coordinator کے ذریعے گزرتی ہے (observability اور error control کے لیے)

## 3.4 Subagents بنانے کے لیے `Task` Tool

Subagents `Task` tool کے ذریعے spawn کیے جاتے ہیں:

```python
# Coordinator کے allowedTools میں "Task" ہونا چاہیے
coordinator_agent = AgentDefinition(
    allowed_tools=["Task", "get_customer"]
)
```

**Explicit context passing لازمی ہے:**

```
# Bad: subagent کے پاس context نہیں ہے
Task: "Analyze the document"

# Good: مکمل context prompt میں
Task: "Analyze the following document.
Document: [full document text]
Prior search results: [web search results]
Output format requirements: [schema]"
```

**Parallel spawning:** coordinator ایک response میں متعدد `Task`s call کر سکتا ہے — subagents parallel چلتے ہیں:

```
# Coordinator کے ایک response میں یہ شامل ہے:
Task 1: "Search for articles about X"
Task 2: "Analyze document Y"
Task 3: "Search for articles about Z"
# تینوں ایک ساتھ چلتے ہیں
```

## 3.5 Agent SDK میں Hooks

Hooks agent lifecycle کے مخصوص points پر interception اور transformation کی اجازت دیتے ہیں۔

**PostToolUse** tool result کو model تک پہنچانے سے پہلے intercept کرتا ہے:

```python
# مثال: مختلف MCP tools سے تاریخ کے formats normalize کریں
@hook("PostToolUse")
def normalize_dates(tool_result):
    # Unix timestamp -> ISO 8601
    # "Mar 5, 2025" -> "2025-03-05"
    return normalized_result
```

**Outgoing-call interception hook** policy کی خلاف ورزی کرنے والے actions کو block کرتا ہے:

```python
# مثال: $500 سے اوپر refunds block کریں
@hook("PreToolUse")
def enforce_refund_limit(tool_call):
    if tool_call.name == "process_refund" and tool_call.args.amount > 500:
        return redirect_to_escalation(tool_call)
```

**Hooks اور prompt instructions میں فرق**

| Attribute | Hooks | Prompt instructions |
|---|---|---|
| Guarantee | **Deterministic** (100%) | **Probabilistic** (>90%, 100% نہیں) |
| کب استعمال کریں | Critical business rules، financial operations، compliance | General preferences، recommendations، formatting |
| مثال | Refunds > $500 block کریں | “Try to solve before escalating” |

**قاعدہ:** جب failure کے مالی، قانونی، یا حفاظتی نتائج ہوں — prompts نہیں، hooks استعمال کریں۔

# باب 4: Model Context Protocol (MCP)

> دستاویزات: [MCP](https://modelcontextprotocol.io/) | [Tools](https://modelcontextprotocol.io/docs/concepts/tools) | [Resources](https://modelcontextprotocol.io/docs/concepts/resources) | [Servers](https://modelcontextprotocol.io/docs/concepts/servers)

## 4.1 MCP کیا ہے

Model Context Protocol (MCP) ایک open protocol ہے جو external systems کو Claude سے جوڑتا ہے۔ MCP تین بنیادی resource types define کرتا ہے:

1. **Tools** — functions جنہیں agent actions انجام دینے کے لیے call کر سکتا ہے (CRUD operations، API calls، command execution)
2. **Resources** — context کے لیے data جسے agent پڑھ سکتا ہے (documentation، database schemas، content catalogs)
3. **Prompts** — عام tasks کے لیے predefined prompt templates

## 4.2 MCP Servers

MCP server ایک process ہے جو MCP protocol implement کرتا ہے اور tools/resources فراہم کرتا ہے۔ جب آپ MCP server سے connect کرتے ہیں:
- تمام tools خود بخود discover ہو جاتے ہیں
- تمام connected servers کے tools ایک ساتھ دستیاب ہوتے ہیں
- Tool descriptions طے کرتی ہیں کہ model انہیں کیسے استعمال کرے گا

## 4.3 MCP Servers کو Configure کرنا

**Project configuration (`.mcp.json`)** — team usage کے لیے:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "jira": {
      "command": "npx",
      "args": ["-y", "mcp-server-jira"],
      "env": {
        "JIRA_TOKEN": "${JIRA_TOKEN}"
      }
    }
  }
}
```

**اہم نکات:**
- `.mcp.json` project root میں محفوظ ہوتا ہے اور version control میں ہوتا ہے
- Environment variables (`${GITHUB_TOKEN}`) secrets کے لیے استعمال ہوتے ہیں — tokens خود commit نہیں کیے جاتے
- یہ project کے تمام contributors کے لیے دستیاب ہوتا ہے

**User configuration (`~/.claude.json`)** — personal/experimental servers کے لیے:
- User کے home directory میں محفوظ ہوتا ہے
- Version control کے ذریعے share نہیں ہوتا
- Personal experiments اور testing کے لیے موزوں

**Servers کا انتخاب:**
- Standard integrations (Jira، GitHub، Slack) کے لیے پہلے سے موجود community MCP servers کو ترجیح دیں
- اپنی custom servers صرف unique، team-specific workflows کے لیے بنائیں

## 4.4 MCP میں `isError` Flag

جب MCP tool میں error آتا ہے تو response میں `isError: true` استعمال ہوتا ہے۔ یہ agent کو بتاتا ہے کہ call fail ہوئی ہے۔

**Structured error (اچھا):**

```json
{
  "isError": true,
  "content": {
    "errorCategory": "transient",
    "isRetryable": true,
    "message": "The service is temporarily unavailable. Timeout while calling the orders API.",
    "attempted_query": "order_id=12345",
    "partial_results": null
  }
}
```

**Generic error (anti-pattern):**

```json
{
  "isError": true,
  "content": "Operation failed"
}
```

Generic error agent کو فیصلہ سازی کے لیے کوئی معلومات نہیں دیتا — کیا retry کریں، query بدلیں، یا escalate کریں؟

## 4.5 MCP Resources

Resources ایسا data ہیں جو agent context حاصل کرنے کے لیے actions کیے بغیر طلب کر سکتا ہے:

- Content catalogs (مثلاً تمام project tasks کی فہرست، hierarchical navigation)
- Database schemas (data structure سمجھنے کے لیے)
- Documentation (API references، internal guides)
- Issue/task summaries

**Resource کا فائدہ:** agent کو یہ سمجھنے کے لیے exploratory tool calls کی ضرورت نہیں پڑتی کہ data موجود کیا ہے۔ Resource فوری “map” فراہم کرتا ہے۔

---

# باب 5: Claude Code — Configuration اور Workflows

> دستاویزات: [Claude Code](https://code.claude.com/docs/en/overview) | [Memory / CLAUDE.md](https://code.claude.com/docs/en/memory) | [Skills](https://code.claude.com/docs/en/skills) | [MCP](https://code.claude.com/docs/en/mcp) | [Hooks](https://code.claude.com/docs/en/hooks) | [Sub-agents](https://code.claude.com/docs/en/sub-agents) | [GitHub Actions](https://code.claude.com/docs/en/github-actions) | [Headless](https://code.claude.com/docs/en/headless)

## 5.1 CLAUDE.md Hierarchy

CLAUDE.md وہ instruction file(s) ہیں جو Claude Code استعمال کرتا ہے۔ اس کی تین سطحی hierarchy ہے:

```
1. User-level: ~/.claude/CLAUDE.md
   - صرف اسی user پر لاگو
   - VCS کے ذریعے share نہیں ہوتا
   - ذاتی preferences اور working style

2. Project-level: .claude/CLAUDE.md یا root CLAUDE.md
   - تمام project contributors پر لاگو
   - VCS کے ذریعے manage ہوتا ہے
   - Coding standards، testing standards، architectural decisions

3. Directory-level: subdirectories میں CLAUDE.md
   - جب اسی directory کی files کے ساتھ کام ہو تو لاگو ہوتا ہے
   - codebase کے اُس حصے کے مخصوص conventions
```

**عام غلطی:** ایک نئے team member کو project instructions نہیں ملتیں کیونکہ وہ `.claude/CLAUDE.md` (project-level) کے بجائے `~/.claude/CLAUDE.md` (user-level) میں رکھی گئی تھیں۔

## 5.2 `@path` Syntax (File Imports)

CLAUDE.md بیرونی files کو `@path` کے ذریعے refer کر سکتا ہے، جس سے configuration modular ہو جاتی ہے:

```markdown
# Project CLAUDE.md

Coding standards @./standards/coding-style.md میں بیان کیے گئے ہیں
Test requirements @./standards/testing-requirements.md میں ہیں
Project overview @README.md میں اور dependencies @package.json میں ہیں
```

**`@path` کے قواعد:**
- `@` کے فوراً بعد file path آئے (کوئی space نہیں)
- Relative اور absolute دونوں paths supported ہیں
- Relative paths اُس file کے مطابق resolve ہوتے ہیں جس میں import ہے
- Maximum import nesting depth 5 ہے

اس سے duplication کم ہوتی ہے اور ہر package میں صرف متعلقہ standards شامل ہوتے ہیں۔

## 5.3 `.claude/rules/` Directory

`.claude/rules/` monolithic CLAUDE.md کا متبادل ہے، جو rules کو topic کے حساب سے organize کرنے کے لیے استعمال ہوتا ہے:

```
.claude/rules/
  testing.md          -- testing conventions
  api-conventions.md  -- API conventions
  deployment.md       -- deployment rules
  react-patterns.md   -- React patterns
```

**YAML frontmatter کے ساتھ `paths` conditional loading:**

```yaml
---
paths: ["src/api/**/*"]
---

API files کے لیے async/await کے ساتھ explicit error handling استعمال کریں۔
ہر endpoint standard response wrapper واپس کرے۔
```

```yaml
---
paths: ["**/*.test.tsx", "**/*.test.ts"]
---

Tests میں describe/it blocks استعمال ہونے چاہئیں۔
Data factories استعمال کریں، hardcoding نہیں۔
Database mock نہ کریں — test database استعمال کریں۔
```

**یہ کیسے کام کرتا ہے:**
- Rule صرف اس وقت load ہوتا ہے جب Claude Code ایسا file edit کرے جو `paths` pattern سے match کرتا ہو
- اس سے context اور tokens بچتے ہیں — غیر متعلقہ rules load نہیں ہوتے
- Glob patterns آپ کو file type کے لحاظ سے conventions apply کرنے دیتے ہیں، چاہے files codebase میں کہیں بھی ہوں (tests کے لیے بہت مفید)

**`paths` والے `.claude/rules/` بمقابلہ directory-level CLAUDE.md کب استعمال کریں:**
- `.claude/rules/` with `paths` — جب conventions کئی directories میں بکھری files (tests، migrations) پر لاگو ہوں
- Directory-level CLAUDE.md — جب conventions کسی خاص directory سے وابستہ ہوں اور کہیں اور ضروری نہ ہوں

## 5.4 Custom Slash Commands اور Skills

> **نوٹ:** موجودہ Claude Code version میں custom commands (`.claude/commands/`) کو skills (`.claude/skills/`) کے ساتھ unify کر دیا گیا ہے۔ دونوں formats `/name` commands بناتے ہیں۔ امتحانی گائیڈ `.claude/commands/` کا ذکر کرتی ہے — وہ format اب بھی supported ہے۔

Slash commands reusable prompt templates ہیں جو `/name` کے ذریعے invoke ہوتے ہیں:

**`.claude/commands/` format (legacy، supported):**

```
.claude/commands/
  review.md        -- /review -- standard code review
  test-gen.md      -- /test-gen -- test generation
```

**`.claude/skills/` format (current):**

```
.claude/skills/
  review/SKILL.md  -- /review -- frontmatter configuration کے ساتھ
  test-gen/SKILL.md
```

**Project commands** (`.claude/commands/` یا `.claude/skills/`):
- VCS میں محفوظ ہوتے ہیں اور repo clone کرنے والے سب کے لیے دستیاب ہوتے ہیں
- ٹیم میں consistent workflows یقینی بناتے ہیں

**User commands** (`~/.claude/commands/` یا `~/.claude/skills/`):
- ذاتی commands جو VCS کے ذریعے share نہیں ہوتے
- انفرادی workflows کے لیے

## 5.5 Skills — `.claude/skills/`

Skills advanced commands ہیں جو SKILL.md frontmatter کے ذریعے configure ہوتے ہیں:

```yaml
---
context: fork
allowed-tools: ["Read", "Grep", "Glob"]
argument-hint: "Path to the directory to analyze"
---

دی گئی directory میں code structure کا تجزیہ کریں۔
Dependencies اور architectural patterns پر ایک report تیار کریں۔
```

**Frontmatter parameters:**

| Parameter | Description |
|---|---|
| `context: fork` | Skill کو isolated subagent میں چلاتا ہے۔ Verbose output main session کو pollute نہیں کرتا |
| `allowed-tools` | یہ محدود کرتا ہے کہ کون سے tools دستیاب ہوں گے (security — مثلاً skill files delete نہیں کر سکے گی اگر اجازت نہ ہو) |
| `argument-hint` | جب skill parameters کے بغیر invoke ہو تو argument مانگنے کا اشارہ |

**Skill بمقابلہ CLAUDE.md کب استعمال کریں:**
- **Skill** — مخصوص task کے لیے on-demand invocation (review، analysis، generation)
- **CLAUDE.md** — ہمیشہ لوڈ ہونے والے general standards اور conventions

**Personal skills (`~/.claude/skills/`):**
- اپنی personal variants مختلف ناموں سے بنائیں تاکہ teammates متاثر نہ ہوں

## 5.6 Planning Mode بمقابلہ Direct Execution

**Planning mode:**
- Model صرف investigate اور plan کرتا ہے؛ changes نہیں کرتا
- Codebase explore کرنے کے لیے Read، Grep، Glob استعمال کرتا ہے
- ایک implementation plan تیار کرتا ہے جسے user approve کرتا ہے
- بغیر side effects کے safe exploration

**Planning mode کب استعمال کریں:**
- بڑے changes (درجنوں files)
- Multiple plausible approaches (microservices: boundaries کیسے define ہوں؟)
- Architectural decisions (کون سا framework؟ کیا structure؟)
- Unfamiliar codebase (change کرنے سے پہلے سمجھنا ضروری ہے)
- Library migrations جو 45+ files کو متاثر کریں

**Direct execution کب استعمال کریں:**
- Single-file fixes واضح stack trace کے ساتھ
- ایک validation check شامل کرنا
- اچھی طرح سمجھے گئے، غیر مبہم changes

**Combined approach:**
1. Investigation اور design کے لیے planning mode
2. User plan approve کرے
3. Approved plan implement کرنے کے لیے direct execution

**Explore subagent** — codebase explore کرنے کے لیے specialized subagent:
- Verbose output کو main context سے isolate کرتا ہے
- صرف summary واپس کرتا ہے
- Multi-phase tasks میں context-window exhaustion روکتا ہے

## 5.7 `/compact` Command

`/compact` context compress کرنے کے لیے built-in command ہے:
- Pچھلی history کو summarize کر کے context window میں جگہ خالی کرتا ہے
- Long investigation sessions میں استعمال ہوتا ہے جب verbose tool output سے context بھر جائے
- Risk: exact numeric values، dates، اور specific details summarization میں گم ہو سکتے ہیں

## 5.8 `/memory` Command

`/memory` sessions کے درمیان memory manage کرنے کے لیے built-in command ہے:
- `CLAUDE.md` file editing کے لیے کھولتا ہے، تاکہ notes، preferences، اور context محفوظ کیے جا سکیں
- Information sessions کے پار برقرار رہتی ہے اور startup پر خود بخود load ہوتی ہے
- Project conventions، user preferences، frequently used commands، اور current work context محفوظ کرنے کے لیے مفید
- ہر session میں وہی instructions دوبارہ سمجھانے کا متبادل

## 5.9 Claude Code CLI for CI/CD

**`-p` (یا `--print`) flag:**

```bash
claude -p "Analyze this pull request for security issues"
```

- Non-interactive mode: prompt process کرتا ہے، stdout پر print کرتا ہے، اور exit ہو جاتا ہے
- User input کا انتظار نہیں کرتا
- CI/CD pipelines میں Claude چلانے کا واحد درست طریقہ

**CI کے لیے structured output:**

```bash
claude -p "Review this PR" --output-format json --json-schema '{"type":"object",...}'
```

- `--output-format json` — output کو JSON میں دیتا ہے
- `--json-schema` — output کو schema کے مطابق validate کرتا ہے
- Result کو automatically inline PR comments پوسٹ کرنے کے لیے parse کیا جا سکتا ہے

**Session context isolation:**
وہی Claude session جس نے code generate کیا ہو، اکثر review میں کم مؤثر ہوتی ہے (model اپنی reasoning context ساتھ رکھتا ہے اور اپنے فیصلوں کو challenge کرنے کا امکان کم ہوتا ہے)۔ Review کے لیے independent instance استعمال کریں۔

**Duplicate comments سے بچاؤ:**
نئے commits کے بعد دوبارہ review کرتے وقت، پچھلے review results context میں شامل کریں اور Claude کو صرف نئے یا unresolved issues report کرنے کی ہدایت دیں۔

## 5.10 `fork_session` اور Session Management

**`--resume <session-name>`** named session کو resume کرتا ہے:

```bash
claude --resume investigation-auth-bug
```

- saved context کے ساتھ پچھلی conversation جاری رکھتا ہے
- Long investigations جو متعدد sessions پر پھیلی ہوں ان کے لیے مفید
- Risk: اگر پچھلی session کے بعد files بدل چکی ہوں تو tool results stale ہو سکتے ہیں

**`fork_session`** shared context سے independent branch بناتا ہے:

```
Codebase investigation
         |
    fork_session
    /           \
Approach A:      Approach B:
Redux            Context API
```

- دونوں forks branch point تک context inherit کرتے ہیں
- اس کے بعد وہ آزادانہ طور پر diverge کرتے ہیں
- Approaches compare کرنے یا strategies test کرنے کے لیے مفید

**Resume کے بجائے نئی session کب شروع کریں:**
- Tool results stale ہوں (files بدل چکی ہوں)
- کافی وقت گزر چکا ہو اور context degrade ہو گیا ہو
- پرانے tool data کے ساتھ resume کرنے کے بجائے یہ بہتر ہے کہ "ہم نے جو پایا اس کا مختصر خلاصہ یہ ہے: ..." سے restart کیا جائے

---

# باب 6: Prompt Engineering — Advanced Techniques

> دستاویزات: [Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

## 6.1 Few-shot Prompting

Few-shot prompting وہ طریقہ ہے جس میں expected behavior دکھانے کے لیے prompt میں 2–4 input/output examples شامل کیے جاتے ہیں۔

**Few-shot text descriptions سے زیادہ مؤثر کیوں ہے:**
- مبہم instruction جیسے “زیادہ precise ہوں” کو کئی طریقوں سے سمجھا جا سکتا ہے
- Example غیر مبہم طور پر expected format اور decision logic دکھاتا ہے
- Model pattern کو نئے cases پر generalize کرتا ہے (صرف examples دہراتا نہیں)

**Few-shot examples کی اقسام اور استعمال:**

1. **Ambiguous scenarios کے لیے examples:**

```
Request: "My order is broken"
Action: Call get_customer -> lookup_order -> check status.
Rationale: “broken” damaged item بھی ہو سکتا ہے؛ آپ کو order details درکار ہیں۔

Request: "Get me a manager"
Action: فوراً escalate_to_human call کریں.
Rationale: Customer واضح طور پر human مانگ رہا ہے۔ خود حل کرنے کی کوشش نہ کریں۔
```

2. **Output formatting کے لیے examples:**

```
Finding example:
{
  "location": "src/auth/login.ts:42",
  "issue": "SQL injection in the username parameter",
  "severity": "critical",
  "suggested_fix": "Use a parameterized query"
}
```

3. **Acceptable بمقابلہ problematic code الگ کرنے کے لیے examples:**

```javascript
// Acceptable (flag نہ کریں):
const items = data.filter(x => x.active);

// Problem (flag کریں):
const items = data.filter(x => x.active == true); // Use strict equality ===
```

4. **Different document formats سے extraction کے examples:**

```
Document with inline citations:
"As shown in the study (Smith, 2023), the rate is 42%."
-> {"value": "42%", "source": "Smith, 2023", "type": "inline_citation"}

Document with bibliography references:
"The rate is 42%. [1]"
-> {"value": "42%", "source": "reference_1", "type": "bibliography"}
```

5. **Informal measurements کے لیے examples:**

```
Text: "about two handfuls of rice"
-> {"amount": "~100g", "original_text": "two handfuls", "precision": "approximate"}

Text: "a pinch of salt"
-> {"amount": "~1g", "original_text": "a pinch", "precision": "approximate"}
```

Few-shot خاص طور پر informal اور non-standard measurement units نکالنے میں مؤثر ہے جو purely rule-based instructions کے لیے بہت متنوع ہوتی ہیں۔

**Prompts میں format normalization rules:**
جب structured output کے لیے strict JSON schemas استعمال کریں، prompt میں normalization rules شامل کریں:

```
Normalization:
- Dates: ہمیشہ ISO 8601 (YYYY-MM-DD); "yesterday" -> absolute date compute کریں
- Currency: numeric amount + currency code; "five bucks" -> {"amount": 5, "currency": "USD"}
- Percentages: decimal fraction; "half" -> 0.5
```

اس سے semantic errors کم ہوتے ہیں جہاں JSON syntactically درست ہو مگر values inconsistent ہوں۔

## 6.2 Explicit Criteria بمقابلہ Vague Instructions

**Bad (vague):**

```
Code comments کی accuracy چیک کریں۔
Conservative رہیں — صرف high-confidence findings report کریں۔
```

**Good (explicit criteria):**

```
Comment کو problematic صرف اُس صورت میں flag کریں جب:
1. Comment کا بیان actual code behavior سے CONTRADICT کرتا ہو
2. Comment کسی غیر موجود function یا variable کا حوالہ دے
3. TODO/FIXME comment کسی ایسے bug کی طرف اشارہ کرے جو code میں پہلے ہی fix ہو چکا ہو

Flag نہ کریں:
- ایسے comments جو صرف style کے لحاظ سے پرانے ہوں
- معمولی wording inaccuracies
- Missing comments (یہ الگ category ہے)
```

**Severity criteria examples کے ساتھ define کریں:**

```
CRITICAL: User کے لیے runtime failure
  Example: Payment process کرتے وقت NullPointerException

HIGH: Security vulnerability
  Example: SQL injection، XSS، missing authorization checks

MEDIUM: Logic bug بغیر فوری impact کے
  Example: Wrong sorting، off-by-one error

LOW: Code quality
  Example: Duplication، چھوٹے data کے لیے suboptimal algorithm
```

## 6.3 Prompt Chaining

Prompt chaining ایک complex task کو focused steps کی sequence میں توڑتا ہے:

```
Step 1: auth.ts analyze کریں (صرف local issues)
       -> Output: auth.ts میں issues کی list

Step 2: database.ts analyze کریں (صرف local issues)
       -> Output: database.ts میں issues کی list

Step 3: Integration pass (cross-file dependencies)
       -> Output: module boundaries پر issues
```

**یہ کیوں اہم ہے:**
- **Attention dilution** سے بچاتا ہے—جب model ایک ساتھ بہت سی files دیکھتا ہے تو کچھ files کے bugs miss کر سکتا ہے اور باقی پر shallow commentary دے سکتا ہے
- ہر file کے لیے consistent analysis quality یقینی بناتا ہے
- Cross-file interactions کے لیے الگ analysis کی اجازت دیتا ہے

**Prompt chaining بمقابلہ dynamic decomposition کب استعمال کریں:**
- **Prompt chaining** — predictable، repeatable tasks (code review، file migrations)
- **Dynamic decomposition** — open-ended investigations جہاں subtasks execution کے دوران واضح ہوتے ہیں

## 6.4 “Interview” Pattern

Solution implement کرنے سے پہلے Claude clarifying questions پوچھتا ہے:

```
Claude: "API کے لیے caching implement کرنے سے پہلے چند سوالات:
1. آپ TTL یا event-based میں سے کون سی cache invalidation strategy پسند کرتے ہیں؟
2. اگر cache unavailable ہو تو کیا stale data قابلِ قبول ہے؟
3. Caching per-user ہونی چاہیے یا global؟
4. Cache کرنے کے لیے expected data volume کیا ہے؟"
```

**یہ کب مفید ہے:**
- Unfamiliar domain (fintech، healthcare، legal systems)
- غیر واضح implications والے tasks (cache strategies، failure modes)
- متعدد viable approaches جہاں بہترین انتخاب context پر منحصر ہو

## 6.5 Validation اور Retry-with-Feedback

جب extracted data validation fail کرے:

```
Step 1: Document سے data extract کریں
Step 2: Validate کریں (Pydantic، JSON Schema، business rules)
Step 3: اگر error ہو — context کے ساتھ retry کریں:
  - Original document
  - Previous (incorrect) extraction
  - Specific error: "Field 'total' = 150, but sum(line_items) = 145. Re-check values."
```

**Retry کب مؤثر ہوگا:**
- Format errors (date غلط format میں)
- Structural errors (field غلط جگہ)
- Arithmetic inconsistencies (model دوبارہ check کر سکتا ہے)

**Retry کب مدد نہیں کرے گا:**
- Information source document میں موجود ہی نہیں
- Required context external ہے (data کسی اور document میں ہے جو فراہم نہیں کیا گیا)

**Pydantic بطور validation tool:**
Pydantic Python library ہے جو schema-based data validation کے لیے استعمال ہوتی ہے۔ امتحان کے لیے اہم نکات یہ ہیں:
- **Structural validation:** types، requiredness، enum constraints JSON کے بعد code میں چیک کیے جاتے ہیں
- **Semantic validation:** custom validators business logic enforce کرتے ہیں (sum of items equals total؛ start_date < end_date)
- **Validate–retry loops:** Pydantic validation failure پر error message بنا کر Claude کو error context کے ساتھ دوبارہ prompt کریں
- **JSON Schema generation:** Pydantic models `tool_use` کے لیے JSON Schema generate کر سکتے ہیں، جو ایک single source of truth فراہم کرتا ہے

## 6.6 Self-correction

Internal contradictions detect کرنے کا pattern:

```json
{
  "stated_total": "$150.00",
  "calculated_total": "$145.00",
  "conflict_detected": true,
  "line_items": [
    {"name": "Widget A", "price": 75.00},
    {"name": "Widget B", "price": 70.00}
  ]
}
```

Model stated value اور computed value دونوں نکالتا ہے — اگر وہ مختلف ہوں تو `conflict_detected` آپ کو discrepancy handle کرنے دیتا ہے۔

---

# باب 7: Message Batches API

> دستاویزات: [Message Batches](https://platform.claude.com/docs/en/build-with-claude/message-batches)

## 7.1 Overview

Message Batches API آپ کو asynchronous processing کے لیے requests کے batches submit کرنے دیتا ہے:

| Attribute | Value |
|---|---|
| Savings | synchronous calls کے مقابلے میں **50%** |
| Processing window | زیادہ سے زیادہ **24 hours** (latency SLA guarantee نہیں) |
| Multi-turn tool calling | **Supported نہیں** (ایک request = ایک response) |
| Correlation | request اور response کو جوڑنے کے لیے `custom_id` field |

## 7.2 Batch API بمقابلہ Synchronous API کب استعمال کریں

| Task | API | Why |
|---|---|---|
| Pre-merge PR check | **Synchronous** | Developer انتظار کر رہا ہے؛ 24 hours قابلِ قبول نہیں |
| Overnight tech-debt report | **Batch** | Result صبح تک چاہیے؛ 50% savings |
| Weekly security audit | **Batch** | فوری نہیں؛ 50% savings |
| Interactive code review | **Synchronous** | فوری response درکار ہے |
| 10,000 documents process کرنا | **Batch** | Bulk processing؛ savings اہم ہیں |

## 7.3 `custom_id` کا استعمال

```json
{
  "custom_id": "doc-invoice-2024-001",
  "params": {
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Extract data from: ..."}]
  }
}
```

`custom_id` آپ کو یہ کرنے دیتا ہے:
- Result کو original document سے link کرنا
- Failure کی صورت میں صرف failed documents دوبارہ submit کرنا
- Successful documents کو دوبارہ process کرنے سے بچنا

## 7.4 Batch میں Failures کو Handle کرنا

1. 100 documents کا batch submit کریں
2. 95 succeed کریں؛ 5 fail ہوں (context limit exceeded)
3. Failures کو `custom_id` سے identify کریں
4. Strategy بدلیں (مثلاً long documents کو chunks میں تقسیم کریں)
5. صرف اُن 5 failed documents کو دوبارہ submit کریں

## 7.5 SLA Planning

اگر آپ کو 30 hours میں result چاہیے اور Batch API کو 24 hours تک لگ سکتے ہیں:
- Submission window: 30 - 24 = **6 hours**
- Batches کو deadline سے کم از کم 24 hours پہلے submit کرنا ہوگا
- Frequent submissions کے لیے 4-hour windows میں تقسیم کریں

---

# باب 8: Task Decomposition Strategies

## 8.1 Fixed Pipelines (Prompt Chaining)

ہر step پہلے سے defined ہوتا ہے:

```
Document -> Metadata extraction -> Data extraction -> Validation -> Enrichment -> Final output
```

**کب استعمال کریں:**
- Task structure predictable ہو (reviews ہمیشہ ایک ہی template follow کریں)
- تمام steps پہلے سے معلوم ہوں
- آپ کو stability اور reproducibility چاہیے

## 8.2 Dynamic Adaptive Decomposition

Subtasks intermediate results کی بنیاد پر generate ہوتے ہیں:

```
1. "Legacy codebase کے لیے tests add کریں"
2. -> پہلے structure map کریں (Glob, Grep)
3. -> ملا: 3 modules بغیر tests کے، 2 partial coverage کے ساتھ
4. -> Prioritize: payments module سے شروع کریں (high risk)
5. -> کام کے دوران: external API پر dependency دریافت ہوئی
6. -> Adapt: tests لکھنے سے پہلے external API کے لیے mock add کریں
```

**کب استعمال کریں:**
- Open-ended investigative tasks
- جب مکمل scope شروع میں معلوم نہ ہو
- جب ہر step پچھلے step کے results پر منحصر ہو

## 8.3 Multi-pass Code Review

10+ files والی pull requests کے لیے:

```
Pass 1 (per-file): auth.ts analyze کریں -> local issues کی list
Pass 1 (per-file): database.ts analyze کریں -> local issues کی list
Pass 1 (per-file): routes.ts analyze کریں -> local issues کی list
...
Pass 2 (integration): files کے درمیان relationships analyze کریں
  -> Cross-file issues: inconsistent types, circular dependencies
```

**14 files پر ایک ہی pass کیوں خراب ہے:**
- Attention dilution: کچھ files کی deep analysis، کچھ کی shallow
- Inconsistent comments: ایک file میں pattern flag، دوسری میں approve
- Missed bugs: cognitive overload کی وجہ سے واضح errors چھوٹ جاتے ہیں

---

# باب 9: Escalation اور Human-in-the-Loop

## 9.1 کب Human کی طرف Escalate کریں

**Escalation triggers (واضح rules):**

| Situation | Action |
|---|---|
| Customer واضح طور پر کہے “get me a manager” | فوراً escalate کریں؛ حل کرنے کی کوشش نہ کریں |
| Policy request کو cover نہ کرتی ہو | Escalate کریں (مثلاً competitor price matching جب policy خاموش ہو) |
| Agent پیش رفت نہ کر سکے | مناسب تعداد میں attempts کے بعد escalate کریں |
| Threshold سے اوپر financial operation | Escalate کریں (ترجیحاً hook کے ذریعے enforce، prompt کے ذریعے نہیں) |
| Customer تلاش کرتے وقت multiple matches | مزید identifiers مانگیں؛ اندازہ نہ لگائیں |

**جو reliable trigger نہیں ہے:**

| Unreliable method | Why it fails |
|---|---|
| Sentiment analysis | Customer کا mood case complexity سے correlate نہیں کرتا |
| Model self-rated confidence (1–10) | Model confidently غلط ہو سکتا ہے؛ calibration کمزور ہے |
| Automatic classifier | Overengineering؛ ممکن ہے training data موجود نہ ہو |

## 9.2 Escalation Patterns

**Immediate escalation:**

```
Customer: "I want to speak to a manager"
Agent: [فوراً escalate_to_human call کرتا ہے]
NOT: "I can help with your issue, let me..."
```

**Resolve کرنے کی کوشش کے بعد escalation:**

```
Customer: "My refrigerator broke two days after purchase"
Agent: [order چیک کرتا ہے، warranty replacement offer کرتا ہے]
اگر customer مطمئن نہ ہو -> escalate
```

**Nuanced escalation (acknowledge → resolve → reiteration پر escalate):**

```
Customer: "This is outrageous, I'm very unhappy with the quality!"
Agent: [frustration acknowledge] "میں آپ کی frustration سمجھتا ہوں."
       [resolution offer] "میں replacement یا refund پیش کر سکتا ہوں."
Customer: "No, I want to talk to someone!"
Agent: [customer دوبارہ insist کرے -> immediate escalation]
```

بنیادی اصول: پہلے emotion acknowledge کریں، پھر concrete solution دیں، اور صرف اسی وقت escalate کریں جب customer human کی خواہش دہرائے۔ dissatisfaction کے پہلے اظہار پر escalate نہ کریں (یہ manager مانگنے کے برابر نہیں ہے)۔

**Policy gap کے لیے escalation:**

```
Customer: "Competitor X has this item 30% cheaper—give me a discount"
Policy: صرف اپنی site پر price adjustments cover کرتی ہے
Agent: [escalate — policy competitor price matching کو cover نہیں کرتی]
```

## 9.3 Structured Handoff Protocols

Escalation پر agent کو structured summary human کو دینی چاہیے:

```json
{
  "customer_id": "CUST-12345",
  "customer_name": "Ivan Petrov",
  "issue_summary": "Refund request for a damaged item",
  "order_id": "ORD-67890",
  "root_cause": "Item arrived damaged; photos attached",
  "actions_taken": [
    "Verified customer via get_customer",
    "Confirmed order via lookup_order",
    "Offered a standard replacement — customer insists on a refund"
  ],
  "refund_amount": "$89.99",
  "recommended_action": "Approve a full refund",
  "escalation_reason": "Customer requested to speak with a manager"
}
```

Human operator کو full conversation transcript تک رسائی نہیں ہوتی — وہ صرف یہ summary دیکھتا ہے۔ اس لیے یہ مکمل اور self-contained ہونی چاہیے۔

## 9.4 Confidence Calibration اور Human Oversight

Data extraction systems کے لیے:

1. **Field-level confidence scores:** model ہر extracted field کے لیے confidence score نکالتا ہے
2. **Calibration:** labeled validation sets استعمال کر کے thresholds tune کریں
3. **Routing:**
   - High confidence + stable accuracy -> automated processing
   - Low confidence یا ambiguous sources -> human review

**Stratified random sampling:**
- High-confidence extractions کے لیے بھی باقاعدگی سے sample audit کریں
- Aggregate 97% accuracy کسی مخصوص document type کے لیے 40% errors چھپا سکتی ہے
- Accuracy کو صرف overall نہیں، document type اور field کے حساب سے analyze کریں

---

# باب 10: Multi-agent Systems میں Error Handling

## 10.1 Error Categories

| Category | Examples | Retryable | Agent action |
|---|---|---|---|
| **Transient** | Timeout، 503، network failure | Yes | Exponential backoff کے ساتھ retry |
| **Validation** | Invalid input format، missing required field | No (input fix کریں) | Request modify کریں اور retry کریں |
| **Business** | Policy violation، threshold exceeded | No | User کو سمجھائیں؛ alternative پیش کریں |
| **Permission** | Access denied | No | Escalate کریں |

## 10.2 Error-handling Anti-patterns

| Anti-pattern | Problem | Correct approach |
|---|---|---|
| Generic status “search unavailable” | Coordinator decide نہیں کر سکتا کہ recover کیسے کرنا ہے | Error type، query، partial results، alternatives واپس کریں |
| Silent suppression (empty result = success) | Coordinator سمجھتا ہے match نہیں ملا، حالانکہ failure ہوا تھا | “no results” اور “search failure” میں فرق کریں |
| ایک failure پر پورا workflow abort کرنا | تمام partial results ضائع ہو جاتے ہیں | Partial results کے ساتھ جاری رکھیں؛ gaps annotate کریں |
| Subagent میں infinite retries | Latency اور resources کا ضیاع | Local recovery (1–2 retries)، پھر coordinator تک propagate |

## 10.3 Structured Subagent Error

```json
{
  "status": "partial_failure",
  "failure_type": "timeout",
  "attempted_query": "AI impact on music industry 2024",
  "partial_results": [
    {"title": "AI Music Generation Report", "url": "...", "relevance": 0.8}
  ],
  "alternative_approaches": [
    "Try a narrower query: 'AI music composition tools'",
    "Use an alternative data source"
  ],
  "coverage_impact": "Not covered: AI impact on music production"
}
```

یہ coordinator کو فیصلہ کرنے کے لیے ضروری معلومات دیتا ہے:
- Modified query کے ساتھ retry کریں؟
- Partial results استعمال کریں؟
- کسی اور subagent کو delegate کریں؟
- اس section کے بغیر جاری رکھیں اور gap annotate کریں؟

## 10.4 Final Synthesis میں Coverage Annotations

```markdown
## Report: AI Impact on Creative Industries

### Visual Art (FULL COVERAGE)
[research results]

### Music (PARTIAL COVERAGE — search agent timeout)
[partial results]
⚠️ Note: اس section کی coverage search agent timeout کی وجہ سے محدود ہے.

### Literature (FULL COVERAGE)
[research results]
```

---

# باب 11: Production Systems میں Context Management

## 11.1 Facts کو Separate Block میں Extract کریں

Conversation history پر انحصار کرنے کے بجائے (جو summarization کے دوران degrade ہو جاتی ہے)، key facts کو structured block میں extract کریں:

```
=== CASE FACTS (جب بھی نیا fact آئے update کیا جائے) ===
Customer ID: CUST-12345
Order ID: ORD-67890
Order Date: 2025-01-15
Order Amount: $89.99
Issue: Damaged item on delivery
Customer Request: Full refund
Status: Pending manager approval
===
```

یہ block ہر prompt میں شامل کریں، چاہے history کتنی ہی summarized کیوں نہ ہو۔

## 11.2 Tool Results کو Trimming کرنا

اگر `lookup_order` 40+ fields واپس کرتا ہے مگر current task کے لیے صرف 5 درکار ہیں:

```python
# PostToolUse hook: صرف relevant fields رکھیں
@hook("PostToolUse", tool="lookup_order")
def trim_order_fields(result):
    return {
        "order_id": result["order_id"],
        "status": result["status"],
        "total": result["total"],
        "items": result["items"],
        "return_eligible": result["return_eligible"]
    }
```

اس سے context بچتا ہے اور noise کم ہوتی ہے۔

## 11.3 Position-aware Input

Lost-in-the-middle effect کو ذہن میں رکھتے ہوئے critical information رکھیں:

```
[KEY FINDINGS — اوپر]
3 critical vulnerabilities ملیں...

[DETAILED RESULTS — درمیان]
=== File auth.ts ===
...
=== File database.ts ===
...

[ACTION ITEMS — آخر میں]
Priority: merge سے پہلے auth.ts vulnerabilities fix کریں.
```

## 11.4 Scratchpad Files

Long investigations میں agent key findings scratchpad file میں لکھ سکتا ہے:

```
# investigation-scratchpad.md
## Key findings
- PaymentProcessor in src/payments/processor.ts inherits from BaseProcessor
- refund() تین places سے call ہوتی ہے: OrderController، AdminPanel، CronJob
- External PaymentGateway API limit: 100 req/min
- Migration #47 نے refund_reason (NOT NULL) add کیا — 2024-12-01
```

جب context degrade ہو جائے (یا نئی session میں)، agent discovery دوبارہ چلانے کے بجائے scratchpad consult کر سکتا ہے۔

## 11.5 Context بچانے کے لیے Subagents کو Delegate کرنا

```
Main agent: "payments module کی dependencies investigate کریں"
  -> Subagent (Explore): 15 files read کرتا ہے، imports trace کرتا ہے
  -> Returns: "Payments depends on AuthService, OrderModel, and the external PaymentGateway API"

Main agent: context میں 15 files کے بجائے ایک line رکھتا ہے
```

**Separate context layer:**
Multi-agent systems میں ہر subagent محدود context budget میں کام کرتا ہے — اسے صرف اپنے task کے لیے ضروری information ملتی ہے۔ Coordinator ایک separate context layer کے طور پر کام کرتا ہے: وہ subagent outputs aggregate کرتا ہے، global state store کرتا ہے، اور context allocate کرتا ہے۔ اس سے “context leakage” نہیں ہوتا، جہاں ایک agent window کو ایسی information سے بھر دیتا ہے جو دوسروں کے لیے غیر متعلق ہو۔

**Subagents کے لیے constrained context budgets:**
- Minimal context بھیجیں: specific task + ضروری data
- Subagent کو raw data dumps کے بجائے structured results واپس کرنے کی ہدایت دیں
- `allowedTools` سے subagent کے toolset کو limit کریں — کم tools کا مطلب کم distractions اور کم context cost

## 11.6 Structured State Persistence (crash recovery کے لیے)

ہر agent اپنی state ایک معلوم location پر export کرتا ہے:

```json
// agent-state/web-search-agent.json
{
  "status": "completed",
  "queries_executed": ["AI music 2024", "AI music composition"],
  "results_count": 12,
  "key_findings": [...],
  "coverage": ["music composition", "music production"],
  "gaps": ["music distribution", "music licensing"]
}
```

Coordinator resume پر ایک manifest load کرتا ہے:

```json
// agent-state/manifest.json
{
  "web-search": "completed",
  "doc-analysis": "in_progress",
  "synthesis": "not_started"
}
```

---

# باب 12: Provenance کو محفوظ رکھنا

## 12.1 Attribution Loss Problem

جب متعدد sources سے results summarize کیے جاتے ہیں، تو “claim → source” link گم ہو سکتا ہے:

```
Bad: "The AI music market is estimated at $3.2B." (No source, no year.)

Good:
{
  "claim": "The AI music market is estimated at $3.2B.",
  "source_url": "https://example.com/report",
  "source_name": "Global AI Music Report 2024",
  "publication_date": "2024-06-15",
  "confidence": 0.9
}
```

## 12.2 Conflicting Data کو Handle کرنا

جب دو sources مختلف values دیں:

```json
{
  "claim": "Share of AI-generated music on streaming platforms",
  "values": [
    {
      "value": "12%",
      "source": "Spotify Annual Report 2024",
      "date": "2024-03",
      "methodology": "Automated classification"
    },
    {
      "value": "8%",
      "source": "Music Industry Association Survey",
      "date": "2024-07",
      "methodology": "Survey of 500 labels"
    }
  ],
  "conflict_detected": true,
  "possible_explanation": "Methodology اور time period کا فرق"
}
```

کسی ایک value کو اندھا دھند منتخب نہ کریں۔ دونوں کو attribution کے ساتھ محفوظ رکھیں اور coordinator کو فیصلہ کرنے دیں۔

## 12.3 Correct Interpretation کے لیے Dates شامل کریں

Dates کے بغیر temporal differences کو contradiction سمجھ لیا جا سکتا ہے:

```
Bad: "Source A says 10%, source B says 15%. Contradiction."
Good: "Source A (2023) says 10%, source B (2024) says 15%. Likely ایک سال میں +5% growth."
```

## 12.4 Content Type کے مطابق Render کریں

ہر چیز کو ایک ہی format میں نہ ٹھونسیں:
- Financial data -> tables
- News اور analysis -> prose
- Technical findings -> structured lists
- Time series -> chronological ordering

---

# باب 13: Claude Code کے Built-in Tools

## 13.1 Tool Selection Reference

| Task | Tool | Example |
|---|---|---|
| نام/pattern سے files تلاش کرنا | **Glob** | `**/*.test.tsx`, `src/components/**/*.ts` |
| File contents کے اندر search کرنا | **Grep** | Function name، error message، import |
| File مکمل پڑھنا | **Read** | Analysis کے لیے file load کرنا |
| نیا file بنانا | **Write** | Scratch سے file create کرنا |
| موجودہ file میں precise edit | **Edit** | Unique text match کے ذریعے specific snippet replace کرنا |
| Shell command چلانا | **Bash** | git، npm، tests، build |

## 13.2 Incremental Investigation Strategy

ایک ساتھ تمام files نہ پڑھیں۔ سمجھ بوجھ کو رفتہ رفتہ بنائیں:

```
1. Grep: entry points تلاش کریں (function definition، export)
2. Read: ملنے والی files پڑھیں
3. Grep: usages تلاش کریں (import، calls)
4. Read: consumer files پڑھیں
5. جب تک مکمل picture نہ مل جائے repeat کریں
```

## 13.3 Fallback: Edit کے بجائے Read + Write

جب Edit non-unique text match کی وجہ سے fail ہو جائے:
1. Read — مکمل file content لوڈ کریں
2. Content کو programmatically modify کریں
3. Write — updated version لکھ دیں

---

# حصہ II: امتحانی ڈومین نوٹس

---

# ڈومین 1: Agent Architecture اور Orchestration (27%)

## 1.1 Autonomous Task Execution کے لیے Agentic Loops Design کرنا

### Key knowledge:
- Agent loop lifecycle: Claude request بھیجیں، `stop_reason` (`"tool_use"` بمقابلہ `"end_turn"`) چیک کریں، tools execute کریں، اگلی iteration کے لیے results واپس کریں
- Tool results conversation history میں append ہوتے ہیں تاکہ model اگلا action طے کر سکے
- Model-driven decision making (Claude اگلا tool چنتا ہے) بمقابلہ hard-coded decision trees

### Key skills:
- Flow control: جب `stop_reason = "tool_use"` ہو تو loop جاری رکھیں اور `"end_turn"` پر رک جائیں
- Iterations کے درمیان tool results کو context میں append کرنا
- Anti-patterns سے بچنا: completion کے لیے assistant text parse کرنا، primary stopping mechanism کے طور پر arbitrary iteration limits استعمال کرنا

## 1.2 Multi-agent Systems (Coordinator–Subagent) Orchestrate کرنا

### Key knowledge:
- Hub-and-spoke architecture: coordinator تمام inter-agent communication، error handling، اور routing کا مالک ہوتا ہے
- Subagents isolated context میں کام کرتے ہیں — وہ خود بخود coordinator کی history inherit نہیں کرتے
- Coordinator responsibilities: task decomposition، delegation، result aggregation، dynamic selection of subagents
- Coordinator کی overly narrow decomposition کا خطرہ

### Key skills:
- Research coverage کو subagents کے درمیان تقسیم کریں تاکہ duplication کم ہو
- Iterative refinement loops implement کریں (coordinator synthesis evaluate کرے اور tasks re-route کرے)
- Observability کے لیے تمام communication coordinator کے ذریعے route کریں

## 1.3 Subagent Calls، Context Passing، اور Spawning Configure کرنا

### Key knowledge:
- `Task` tool subagents spawn کرتا ہے؛ coordinator کے `allowedTools` میں `"Task"` شامل ہونا چاہیے
- Subagent context prompt میں explicitly شامل ہونا چاہیے؛ subagents parent context inherit نہیں کرتے
- `AgentDefinition` configuration: descriptions، system prompts، tool constraints
- Alternatives explore کرنے کے لیے `fork_session` کے ذریعے session management

### Key skills:
- Previous agents کے full outputs subagent prompt میں شامل کریں
- Context pass کرتے وقت data اور metadata کو separate کرنے کے لیے structured formats استعمال کریں
- ایک coordinator turn میں متعدد `Task` calls کے ذریعے parallel subagents spawn کریں
- Coordinator prompts goals اور quality criteria کے طور پر لکھیں، step-by-step instructions کے طور پر نہیں

## 1.4 Enforcement اور Handoff Patterns کے ساتھ Multi-step Workflows Implement کرنا

### Key knowledge:
- Workflow ordering کے لیے **programmatic enforcement** (hooks، preconditions) اور **prompt guidance** کے درمیان فرق
- جب deterministic guarantees درکار ہوں (مثلاً مالی operations سے پہلے identity verification)، prompts کافی نہیں ہوتے
- Escalation کے دوران structured handoff protocols (customer ID، reason، recommended action)

### Key skills:
- ایسے programmatic preconditions جو downstream calls کو block کریں جب تک پہلے steps مکمل نہ ہوں (مثلاً `get_customer` کے verified ID واپس کرنے تک `process_refund` block کریں)
- Multi-aspect customer requests کو الگ items میں تقسیم کریں
- Human کو escalate کرتے وقت structured summaries produce کریں

## 1.5 Tool Calls Intercept کرنے اور Data Normalize کرنے کے لیے Agent SDK Hooks

### Key knowledge:
- Hook patterns (مثلاً `PostToolUse`) tool results کو model کے consume کرنے سے پہلے intercept کرتے ہیں
- Hooks outgoing calls intercept کر کے compliance rules enforce کرتے ہیں (مثلاً threshold سے اوپر refunds block کرنا)
- Hooks **deterministic guarantees** دیتے ہیں، جبکہ prompt instructions **probabilistic compliance** دیتی ہیں

### Key skills:
- `PostToolUse` hooks سے data formats normalize کریں (Unix timestamps، ISO 8601، numeric status codes)
- Policy-violating actions block کرنے کے لیے interception hooks استعمال کریں اور escalation کی طرف redirect کریں
- جب business rules کو guaranteed compliance چاہیے ہو تو prompts کے بجائے hooks منتخب کریں

## 1.6 Complex Workflows کے لیے Task Decomposition Strategies

### Key knowledge:
- **Fixed pipelines** (prompt chaining) بمقابلہ intermediate results کی بنیاد پر **dynamic adaptive decomposition**
- Prompt chaining: sequential steps (ہر file کو الگ analyze کریں، پھر integration pass)
- Adaptive investigation plans جو discovered information کی بنیاد پر subtasks generate کرتے ہیں

### Key skills:
- Predictable multi-aspect reviews کے لیے prompt chaining استعمال کریں؛ open-ended investigations کے لیے dynamic decomposition
- Large code reviews کو per-file analysis + separate cross-file integration pass میں تقسیم کریں
- Open-ended tasks کو degrade کریں: پہلے structure map کریں، پھر prioritized plan بنائیں

## 1.7 Session State، Resuming، اور Forking

### Key knowledge:
- Named sessions continue کرنے کے لیے `--resume <session-name>`
- Shared context سے independent investigation branches بنانے کے لیے `fork_session`
- Resume کرتے وقت agent کو file changes بتانے کی اہمیت
- Structured summary کے ساتھ نئی session، stale results کے ساتھ resuming سے زیادہ reliable ہو سکتی ہے

### Key skills:
- Named investigation sessions continue کرنے کے لیے `--resume` استعمال کریں
- Approaches parallel compare کرنے کے لیے `fork_session` استعمال کریں
- Resuming (context ابھی current ہے) اور نئی session شروع کرنے (results stale ہیں) کے درمیان انتخاب کریں

---

## 5.10 `fork_session` اور Session Management

**`--resume <session-name>`** named session کو resume کرتا ہے:

```bash
claude --resume investigation-auth-bug
```

- saved context کے ساتھ پچھلی conversation جاری رکھتا ہے
- Long investigations جو متعدد sessions پر پھیلی ہوں ان کے لیے مفید
- Risk: اگر پچھلی session کے بعد files بدل چکی ہوں تو tool results stale ہو سکتے ہیں

**`fork_session`** shared context سے independent branch بناتا ہے:

```
Codebase investigation
         |
    fork_session
    /           \
Approach A:      Approach B:
Redux            Context API
```

- دونوں forks branch point تک context inherit کرتے ہیں
- اس کے بعد وہ آزادانہ طور پر diverge کرتے ہیں
- Approaches compare کرنے یا strategies test کرنے کے لیے مفید

**Resume کے بجائے نئی session کب شروع کریں:**
- Tool results stale ہوں (files بدل چکی ہوں)
- کافی وقت گزر چکا ہو اور context degrade ہو گیا ہو
- پرانے tool data کے ساتھ resume کرنے کے بجائے یہ بہتر ہے کہ "ہم نے جو پایا اس کا مختصر خلاصہ یہ ہے: ..." سے restart کیا جائے

---

# ڈومین 2: Tool Design اور MCP Integration (18%)

## 2.1 Clear Descriptions کے ساتھ Tool Interfaces Design کرنا

### Key knowledge:
- Tool descriptions وہ **بنیادی mechanism** ہیں جن سے LLM tools select کرتا ہے؛ minimal descriptions unreliable selection دیتی ہیں
- Input formats، example queries، edge cases، اور applicability boundaries شامل کرنے کی اہمیت
- Ambiguous یا overlapping descriptions misrouting کا سبب بنتی ہیں
- System prompt wording tools کے ساتھ غیر ارادی associations بنا سکتی ہے

### Key skills:
- ایسی descriptions لکھیں جو ہر tool کو similar alternatives سے واضح طور پر distinguish کریں
- Functional overlap ختم کرنے کے لیے tools rename کریں (مثلاً `analyze_content` -> `extract_web_results`)
- General-purpose tools کو specialized tools میں تقسیم کریں جن کے input/output contracts واضح ہوں

## 2.2 MCP Tools کے لیے Structured Error Responses Implement کرنا

### Key knowledge:
- MCP tool responses میں `isError` flag
- **Transient errors** (timeouts)، **validation errors** (bad input)، **business errors** (policy violations)، اور **access/permission errors** کے درمیان فرق
- Generic errors ("Operation failed") صحیح recovery decisions روک دیتے ہیں
- Retryable اور non-retryable errors میں فرق

### Key skills:
- `errorCategory` (transient/validation/permission)، `isRetryable`، اور human-readable message جیسی structured metadata واپس کریں
- Business-rule violations کے لیے واضح user-facing explanations کے ساتھ `retryable: false` استعمال کریں
- Transient failures کے لیے subagents میں local recovery کریں؛ صرف وہ errors propagate کریں جو وہ خود حل نہ کر سکیں
- Access failures (retry decision) اور valid empty results (no matches) میں فرق کریں

## 2.3 Agents میں Tools Allocation اور `tool_choice` Configure کرنا

### Key knowledge:
- بہت زیادہ tools (مثلاً 18 کے بجائے 4–5) tool selection reliability کم کرتی ہے
- Specialization سے باہر tools رکھنے والے agents انہیں غلط استعمال کرتے ہیں
- Scoped tool access: صرف role-relevant tools + محدود cross-role utilities
- `tool_choice`: `"auto"`, `"any"`, اور forced tool selection (`{"type": "tool", "name": "..."}`)

### Key skills:
- ہر subagent کا toolset صرف relevant tools تک محدود رکھیں
- General tools کو constrained alternatives سے بدلیں (مثلاً `fetch_url` -> `load_document`)
- `tool_choice: "any"` استعمال کریں تاکہ text answer کے بجائے tool call یقینی ہو
- Specific tool force کریں تاکہ execution order assured ہو

## 2.4 MCP Servers کو Claude Code اور Agent Workflows میں Integrate کرنا

### Key knowledge:
- MCP server scope: ٹیموں کے لیے project (`.mcp.json`) بمقابلہ experiments کے لیے user (`~/.claude.json`)
- Secrets management کے لیے `.mcp.json` میں environment variable substitution (مثلاً `${GITHUB_TOKEN}`)
- تمام connected MCP servers کے tools connection پر discover ہو جاتے ہیں اور ایک ساتھ available ہوتے ہیں
- MCP resources بطور “content catalogs” (task summaries، database schemas) exploratory tool calls کم کرتے ہیں

### Key skills:
- Shared MCP servers کو project `.mcp.json` میں env-var-based tokens کے ساتھ configure کریں
- Personal/experimental servers کو `~/.claude.json` میں رکھیں
- Standard integrations کے لیے community MCP servers کو custom servers پر ترجیح دیں

## 2.5 Built-in Tools (Read, Write, Edit, Bash, Grep, Glob) منتخب اور Apply کرنا

### Key knowledge:
- **Grep**: file contents کے اندر search (function names، error messages، imports)
- **Glob**: name/extension patterns سے files تلاش کرنا
- **Read/Write**: full-file operations؛ **Edit**: unique text matches کے ذریعے precise changes
- اگر Edit non-unique matches کی وجہ سے fail ہو تو Read + Write پر واپس جائیں

### Key skills:
- Content search کے لیے Grep اور pattern-based discovery کے لیے Glob استعمال کریں
- سمجھ بوجھ رفتہ رفتہ بنائیں: entry points کے لیے Grep، پھر flows trace کرنے کے لیے Read
- Wrapper modules کے ذریعے function usage trace کریں

---

# ڈومین 3: Claude Code Configuration اور Workflows (20%)

## 3.1 Hierarchy، Scope، اور Modular Organization کے ساتھ CLAUDE.md Configure کرنا

### Key knowledge:
- CLAUDE.md hierarchy: user (`~/.claude/CLAUDE.md`)، project (`.claude/CLAUDE.md` یا root `CLAUDE.md`)، اور directory-level (subdirectories میں CLAUDE.md)
- User-level settings صرف ایک user پر لاگو ہوتے ہیں اور VCS کے ذریعے share نہیں ہوتے
- External files refer کرنے کے لیے `@path` syntax (مثلاً `@./standards/coding-style.md`) تاکہ CLAUDE.md modular بنے
- Monolithic CLAUDE.md کے بجائے topic-focused rule files کے لیے `.claude/rules/` directory

### Key skills:
- Hierarchy issues diagnose کریں (نئے team member کو instructions اس لیے نہیں ملتیں کیونکہ وہ user-level میں تھیں، project-level میں نہیں)
- ہر package کے CLAUDE.md میں standards selectively include کرنے کے لیے `@path` (مثلاً `@./standards/testing.md`) استعمال کریں
- بڑے CLAUDE.md کو متعدد `.claude/rules/` files (testing.md، api-conventions.md، deployment.md) میں تقسیم کریں

## 3.2 Custom Slash Commands اور Skills بنانا اور Configure کرنا

### Key knowledge:
- `.claude/commands/` میں **Project commands** (VCS کے ذریعے shared) بمقابلہ `~/.claude/commands/` میں **user commands**
- `.claude/skills/` میں SKILL.md frontmatter: `context: fork`، `allowed-tools`، `argument-hint`
- `context: fork` skill کو isolated subagent context میں چلاتا ہے تاکہ main session pollute نہ ہو
- Personal skill variants `~/.claude/skills/` میں مختلف ناموں سے رہ سکتے ہیں

### Key skills:
- Project slash commands `.claude/commands/` میں رکھیں تاکہ پوری team انہیں حاصل کرے
- Verbose output والے skills isolate کرنے کے لیے `context: fork` استعمال کریں
- Skill کے استعمال کردہ tools محدود کرنے کے لیے `allowed-tools` استعمال کریں
- Required parameters مانگنے کے لیے `argument-hint` استعمال کریں

## 3.3 Conditional Convention Loading کے لیے Path-specific Rules استعمال کرنا

### Key knowledge:
- `.claude/rules/` files میں YAML frontmatter `paths` شامل ہو سکتا ہے تاکہ glob patterns کے مطابق rules activate ہوں
- Path-scoped rules صرف matching files edit کرتے وقت load ہوتے ہیں، context اور tokens بچتے ہیں
- Glob-based path rules directory-level CLAUDE.md سے بہتر ہو سکتے ہیں جب conventions کئی directories میں apply ہوں (مثلاً tests)

### Key skills:
- `paths: ["terraform/**/*"]` کے ساتھ `.claude/rules/` files بنائیں تاکہ صرف matching files پر load ہوں
- Glob patterns (`**/*.test.tsx`) استعمال کریں تاکہ location سے قطع نظر file type کے لحاظ سے conventions apply ہوں
- جب conventions codebase بھر میں پھیلی ہوں تو directory-level CLAUDE.md کے بجائے path-specific rules کو ترجیح دیں

## 3.4 Planning Mode بمقابلہ Direct Execution کب استعمال کریں

### Key knowledge:
- **Planning mode**: complex tasks، بڑے changes، multiple viable approaches، اور architectural decisions کے لیے
- **Direct execution**: سادہ، اچھی طرح سمجھے گئے changes (مثلاً single validation شامل کرنا)
- Planning mode changes سے پہلے codebase کی safe exploration ممکن بناتا ہے
- Explore subagent verbose discovery output isolate کرتا ہے

### Key skills:
- Architectural consequences والے tasks (microservices، 45+ files والی migrations) کے لیے planning mode استعمال کریں
- واضح stack trace اور single file والے fixes کے لیے direct execution استعمال کریں
- Multi-phase tasks میں context-window exhaustion روکنے کے لیے Explore subagent استعمال کریں
- Approaches کو combine کریں: discovery کے لیے plan، implementation کے لیے execute

## 3.5 Progressive Improvement کے لیے Iterative Refinement

### Key knowledge:
- Concrete input/output examples expectations communicate کرنے کا سب سے مؤثر طریقہ ہیں
- **Test-driven iteration**: پہلے tests لکھیں، پھر failures کی بنیاد پر iterate کریں
- “Interview” pattern: Claude clarifying questions پوچھتا ہے تاکہ non-obvious design considerations سامنے آئیں
- تمام issues ایک message میں کب دیں (interdependent) اور sequentially کب (independent)

### Key skills:
- Transformation requirements واضح کرنے کے لیے 2–3 concrete input/output examples فراہم کریں
- Implementation سے پہلے expected behavior، edge cases، اور performance requirements کے ساتھ test sets بنائیں
- Design aspects (cache invalidation، failure modes) سامنے لانے کے لیے interview pattern استعمال کریں
- Edge cases کے لیے sample inputs اور expected outputs کے ساتھ concrete test cases دیں

## 3.6 Claude Code کو CI/CD Pipelines میں Integrate کرنا

### Key knowledge:
- Automated pipelines میں non-interactive mode کے لیے `-p` (یا `--print`) flag
- CI میں structured output کے لیے `--output-format json` اور `--json-schema`
- CLAUDE.md project context (testing standards، review criteria) فراہم کرتا ہے
- **Session context isolation**: code generate کرنے والی same session اسے review کرنے میں کم مؤثر ہوتی ہے

### Key skills:
- Interactive input پر hang ہونے سے بچنے کے لیے CI میں Claude Code کو `-p` کے ساتھ چلائیں
- Structured results (مثلاً inline PR comments) کے لیے `--output-format json` + `--json-schema` استعمال کریں
- نئے commits کے بعد دوبارہ run کرتے وقت پچھلے review results شامل کریں (صرف new/unfixed issues report کریں)
- Test generation quality بہتر کرنے کے لیے CLAUDE.md میں testing standards اور available fixtures document کریں
- نئے tests generate کرتے وقت existing test files کو context میں شامل کریں تاکہ duplication نہ ہو اور style consistent رہے

---

# ڈومین 4: Prompt Engineering اور Structured Output (20%)

## 4.1 Accuracy بہتر کرنے کے لیے Explicit Criteria کے ساتھ Prompts Design کرنا

### Key knowledge:
- Explicit criteria vague instructions سے زیادہ مؤثر ہوتے ہیں (مثلاً “flag comments only when they contradict code” بمقابلہ “check comment accuracy”)
- “be more conservative” جیسی generic guidance concrete categorical criteria سے کم مؤثر ہے
- False positives developer trust پر اثر انداز ہوتے ہیں: کچھ categories میں high false-positive rates درست categories پر بھی trust کم کر دیتی ہیں

### Key skills:
- Review criteria define کریں: کیا report کرنا ہے (bugs، security) اور کیا ignore کرنا ہے (minor style)
- High false-positive rates والی categories عارضی طور پر disable کریں
- ہر level کے لیے code examples کے ساتھ explicit severity criteria define کریں

## 4.2 Output Consistency بہتر کرنے کے لیے Few-shot Prompting استعمال کرنا

### Key knowledge:
- Few-shot examples consistently formatted، actionable output پیدا کرنے کا سب سے مؤثر method ہیں
- Few-shot مبہم cases (tool selection، test coverage gaps) کو دکھا سکتا ہے
- Few-shot model کو نئے patterns پر generalize کرنے میں مدد دیتا ہے، صرف defaults دہرانے میں نہیں
- Few-shot extraction tasks میں hallucinations کم کر سکتا ہے

### Key skills:
- Ambiguous scenarios کے لیے rationale کے ساتھ 2–4 targeted examples دیں
- Output format (location، issue، severity، suggested fix) دکھانے والے examples شامل کریں
- ایسے examples دیں جو acceptable code patterns اور real issues میں فرق دکھائیں
- مختلف structures والے documents سے درست extraction کے examples دیں

## 4.3 `tool_use` اور JSON Schemas کے ساتھ Structured Output Enforce کرنا

### Key knowledge:
- `tool_use` with JSON Schemas schema-conformant output کی ضمانت دینے اور JSON syntax errors ختم کرنے کا سب سے reliable طریقہ ہے
- `tool_choice: "auto"` میں model text واپس کر سکتا ہے؛ `"any"` میں اسے لازماً tool call کرنی ہوتی ہے؛ forced selection specific tool منتخب کرتی ہے
- Strict JSON Schemas syntax errors ختم کرتی ہیں مگر semantic errors نہیں روکتیں (totals نہیں ملتے؛ values غلط fields میں)
- Schema design: required vs optional fields؛ enums کے ساتھ “other” + detail string extensibility کے لیے

### Key skills:
- JSON Schemas کے ساتھ extraction tools define کریں اور `tool_use` results سے data parse کریں
- متعدد schemas ہوں تو structured output یقینی بنانے کے لیے `tool_choice: "any"` استعمال کریں
- Specific tool call force کریں: `tool_choice: {"type": "tool", "name": "extract_metadata"}`
- Source میں information نہ ہونے کی صورت میں values fabricate ہونے سے بچانے کے لیے fields optional/nullable رکھیں
- Extensible categorization کے لیے `"unclear"` اور `"other"` جیسے enum values + detail fields استعمال کریں

## 4.4 Extraction Quality کے لیے Validation، Retries، اور Feedback Loops Implement کرنا

### Key knowledge:
- Retry-with-error-feedback: correction guide کرنے کے لیے retry prompt میں concrete validation errors شامل کریں
- اگر information source میں موجود ہی نہ ہو تو retries بے فائدہ ہوتے ہیں
- Feedback loop design: finding کو trigger کرنے والا pattern (`detected_pattern`) track کریں
- Semantic errors (totals reconcile نہیں ہوتے) بمقابلہ syntax errors (جو `tool_use` سے address ہوتے ہیں)

### Key skills:
- Original document، incorrect extraction، اور specific validation errors کے ساتھ follow-up prompts دیں
- جب retry بے فائدہ ہو (required info صرف external document میں ہو) تو اس کی شناخت کریں
- False positives analyze کرنے کے لیے findings میں `detected_pattern` fields شامل کریں
- Discrepancies detect کرنے کے لیے `calculated_total` اور `stated_total` دونوں extract کر کے self-correction design کریں

## 4.5 Efficient Batch Processing Strategies Design کرنا

### Key knowledge:
- Message Batches API: 50% savings، 24-hour تک processing window، latency SLA guarantee نہیں
- Batch processing non-blocking tasks (overnight reports، audits) کے لیے مناسب ہے اور blocking tasks (pre-merge checks) کے لیے نہیں
- Batch API ایک single request میں multi-turn tool calling support نہیں کرتا
- `custom_id` fields batch کے اندر request/response correlate کرتی ہیں

### Key skills:
- Blocking checks کے لیے synchronous API اور overnight/weekly workloads کے لیے Batch API استعمال کریں
- SLA needs کے مطابق batch submission cadence plan کریں (مثلاً 30-hour guarantee کے لیے 24-hour processing کے ساتھ 4-hour windows)
- Failed documents (identified by `custom_id`) صرف انہی کو دوبارہ submit کر کے failures handle کریں
- Large-scale processing سے پہلے sample کے ساتھ prompts iterate کریں

## 4.6 Multi-instance اور Multi-pass Review Architectures Design کرنا

### Key knowledge:
- Self-review limitations: model اپنی reasoning context ساتھ رکھتا ہے اور اپنے فیصلوں کو challenge کرنے کا امکان کم ہوتا ہے
- Independent review instances (generation context کے بغیر) subtle issues تلاش کرنے میں بہتر ہوتی ہیں
- Multi-pass review: per-file local analysis + cross-file integration pass attention dilution سے بچاتا ہے

### Key skills:
- Changes review کرنے کے لیے generation context کے بغیر second independent Claude instance استعمال کریں
- Multi-file reviews کو per-file passes + integration passes میں تقسیم کریں تاکہ cross-file dataflow analysis ہو سکے
- Self-rated confidence کے ساتھ verification passes استعمال کر کے reviews کو calibrated طریقے سے route کریں

---

# ڈومین 5: Context Management اور Reliability (15%)

## 5.1 Critical Information محفوظ رکھنے کے لیے Conversation Context Manage کرنا

### Key knowledge:
- Progressive summarization کے خطرات: numeric values، percentages، اور dates vague summaries میں بدل جاتے ہیں
- Lost-in-the-middle effect: models long inputs کے شروع اور آخر کو زیادہ reliable طریقے سے process کرتے ہیں، لیکن درمیان کے findings miss کر سکتے ہیں
- Tool outputs relevance کے مقابلے میں context میں disproportionally جمع ہو سکتے ہیں (40+ fields جب 5 درکار ہوں)
- Subsequent API requests میں full conversation history بھیجنے کی اہمیت

### Key skills:
- Transactional facts کو summarized history سے باہر ایک persistent “case facts” block میں نکالیں
- Verbose tool outputs کو relevant fields تک trim کریں
- Key findings کو aggregated data کے شروع میں explicit section headings کے ساتھ رکھیں
- Subagents سے structured outputs میں metadata (dates، sources) شامل کروائیں

## 5.2 Effective Escalation Patterns Design کرنا اور Ambiguity Resolve کرنا

### Key knowledge:
- Suitable escalation triggers: human کی explicit request، policy gaps/exceptions، پیش رفت نہ ہو پانا
- Immediate escalation (explicit request) بمقابلہ attempt-to-resolve (agent scope کے اندر)
- Sentiment analysis اور model confidence self-ratings case complexity کے unreliable proxies ہیں
- Multiple customer matches کے لیے heuristic guessing کے بجائے additional identifiers مانگنے چاہئیں

### Key skills:
- System prompt میں explicit escalation criteria few-shot examples کے ساتھ دیں
- Human کی explicit request کو بغیر اضافی investigation کے فوراً execute کریں
- جب policy کسی specific request کے لیے ambiguous یا silent ہو تو escalate کریں
- Tool results میں multiple matches ہوں تو additional identifiers مانگیں

## 5.3 Multi-agent Systems میں Error Propagation Strategies Implement کرنا

### Key knowledge:
- Structured error context (failure type، query، partial results، alternatives) coordinator کو smarter recovery دیتا ہے
- Access failures (timeouts retry decision چاہتے ہیں) اور valid empty results (no matches) میں فرق کریں
- Generic error statuses (“search unavailable”) coordinator سے valuable context چھپا دیتے ہیں
- Silent suppression یا ایک failure پر پورا workflow abort کرنا دونوں anti-patterns ہیں

### Key skills:
- Structured error context واپس کریں: failure type، کیا attempt کیا گیا، partial results، possible alternatives
- Access failures کو valid empty results سے الگ کریں
- Transient failures کے لیے subagents میں local recovery کریں؛ صرف non-recoverable errors partial results کے ساتھ propagate کریں
- Synthesis میں coverage annotate کریں: کیا اچھی طرح supported ہے اور کہاں gaps باقی ہیں

## 5.4 Large Codebases Investigate کرتے وقت Context Efficiently Manage کرنا

### Key knowledge:
- Long sessions میں context degradation: model unstable answers دینے لگتا ہے اور مخصوص classes کے بجائے “typical patterns” کا حوالہ دیتا ہے
- Scratchpad files key findings کو context boundaries کے پار محفوظ رکھتے ہیں
- Subagents کو delegate کرنے سے verbose discovery output isolate ہو جاتی ہے
- Structured state persistence crash recovery ممکن بناتی ہے

### Key skills:
- Specific questions کے لیے subagents spawn کریں جبکہ high-level coordination main agent میں رکھیں
- Key findings محفوظ رکھنے اور بعد میں refer کرنے کے لیے scratchpad files استعمال کریں
- اگلے phase کے subagents spawn کرنے سے پہلے key findings summarize کریں
- Long investigations کے دوران context usage کم کرنے کے لیے `/compact` استعمال کریں

## 5.5 Human Oversight اور Confidence Calibration کے ساتھ Workflows Design کرنا

### Key knowledge:
- Aggregate metrics (مثلاً 97% overall accuracy) specific document types یا fields پر کمزوری چھپا سکتے ہیں
- Stratified random sampling high-confidence extractions میں error rates measure کرتا ہے
- Field-level confidence calibration labeled validation sets کے ذریعے
- Automation سے پہلے document type اور field segment کے حساب سے accuracy validate کریں

### Key skills:
- New error patterns detect کرنے کے لیے stratified random sampling implement کریں
- Stable performance validate کرنے کے لیے document type اور field کے حساب سے accuracy analyze کریں
- Field-level confidence scores output کریں اور labeled data کے ذریعے review thresholds calibrate کریں
- Low-confidence یا ambiguous-source extractions human review کی طرف route کریں

## 5.6 Multi-source Synthesis میں Provenance Preserve کرنا اور Uncertainty Handle کرنا

### Key knowledge:
- Summarization کے دوران attribution کھو جاتی ہے اگر “claim → source” mappings محفوظ نہ رہیں
- Aggregation کے دوران structured mappings برقرار رہنی چاہئیں
- Conflicting statistics کو arbitrarily ایک value منتخب کرنے کے بجائے attribution کے ساتھ conflict annotate کر کے handle کریں
- Temporal differences کو contradiction سمجھنے سے بچنے کے لیے publication/collection dates شامل کریں

### Key skills:
- Subagents سے “claim → source” mappings (URL، document name، quotes) output کروائیں
- Reports کو stable findings اور disputed ones میں الگ structure کریں
- Conflicting values کو annotations کے ساتھ محفوظ رکھیں اور reconciliation کے لیے coordinator کو دیں
- Correct temporal interpretation کے لیے publication dates شامل کریں
- Content type کے مطابق render کریں: financial data tables میں، news prose میں، technical findings structured lists میں

---
# Claude Certified Architect — Foundations Certification

## مطالعہ گائیڈ (سرکاری امتحانی گائیڈ کی بنیاد پر)

---

## تعارف

**Claude Certified Architect — Foundations** سرٹیفیکیشن اس بات کی تصدیق کرتی ہے کہ ایک ماہر Claude-based حل بناتے وقت درست trade-off فیصلے کر سکتا ہے۔ یہ امتحان Claude Code، Claude Agent SDK، Claude API، اور Model Context Protocol (MCP) کے بنیادی علم کو جانچتا ہے — یعنی وہ بنیادی ٹیکنالوجیز جن سے Claude کے ساتھ پروڈکشن ایپلیکیشنز تیار کی جاتی ہیں۔

امتحان کے سوالات حقیقی دنیا کے منظرناموں پر مبنی ہوتے ہیں: کسٹمر سپورٹ کے لیے agentic systems بنانا، multi-agent research pipelines ڈیزائن کرنا، Claude Code کو CI/CD میں شامل کرنا، developer productivity tools بنانا، اور غیر ساختہ دستاویزات سے structured data نکالنا۔

---

## ہدف امیدوار

مثالی امیدوار ایک **solution architect** ہے جو Claude کے ساتھ پروڈکشن ایپلیکیشنز ڈیزائن اور ship کرتا ہے۔ آپ کے پاس کم از کم 6 ماہ کا عملی تجربہ ہونا چاہیے:

- **Claude Agent SDK** — multi-agent orchestration، subagents کو delegate کرنا، tool integration، lifecycle hooks
- **Claude Code** — CLAUDE.md، MCP servers، Agent Skills، planning mode
- **Model Context Protocol (MCP)** — backend integration کے لیے tools اور resources
- **Prompt engineering** — JSON schemas، few-shot examples، data extraction templates
- **Context windows** — لمبی دستاویزات، multi-agent context passing
- **CI/CD pipelines** — automated code review، test generation
- **Escalation and reliability** — error handling، human-in-the-loop

---

## امتحانی فارمیٹ

| پیرامیٹر | قدر |
|---|---|
| سوال کی قسم | Multiple choice (4 میں سے 1 درست) |
| اسکورنگ | 100–1000 scale، passing score **720** |
| Guessing penalty | نہیں (ہر سوال کا جواب دیں!) |
| Scenarios | 6 میں سے 4 (randomly selected) |

---

## امتحانی مواد: 5 ڈومینز

| ڈومین | وزن |
|---|---|
| 1. Agent architecture and orchestration | **27%** |
| 2. Tool design and MCP integration | **18%** |
| 3. Claude Code configuration and workflows | **20%** |
| 4. Prompt engineering and structured output | **20%** |
| 5. Context management and reliability | **15%** |

---

## امتحانی منظرنامے

### Scenario 1: Customer Support Agent
آپ ایک agent بناتے ہیں جو Claude Agent SDK استعمال کرتے ہوئے returns، billing disputes، اور account issues سنبھالتا ہے۔ یہ agent MCP tools (`get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`) استعمال کرتا ہے۔ ہدف 80%+ first-contact resolution ہے، مناسب escalation کے ساتھ۔

### Scenario 2: Claude Code کے ساتھ Code Generation
آپ Claude Code کو development تیز کرنے کے لیے استعمال کرتے ہیں: code generation، refactoring، debugging، documentation۔ آپ کو اسے custom slash commands اور CLAUDE.md configuration کے ساتھ integrate کرنا ہے، اور planning mode کے استعمال کو سمجھنا ہے۔

### Scenario 3: Multi-Agent Research System
ایک coordinator agent specialized subagents کو tasks سونپتا ہے: web research، document analysis، synthesis، اور report generation۔ سسٹم کو citations کے ساتھ مکمل رپورٹس تیار کرنی چاہئیں۔

### Scenario 4: Developer Productivity Tools
یہ agent engineers کو unfamiliar codebases explore کرنے، boilerplate code بنانے، اور routine tasks automate کرنے میں مدد دیتا ہے۔ Built-in tools (Read، Write، Bash، Grep، Glob) اور MCP servers استعمال ہوتے ہیں۔

### Scenario 5: Claude Code for Continuous Integration
Claude Code کو CI/CD pipeline میں ضم کریں تاکہ automated code reviews، test generation، اور pull request feedback حاصل ہو۔ Prompts ایسے بننے چاہئیں کہ false positives کم سے کم ہوں۔

### Scenario 6: Structured Data Extraction
سسٹم غیر ساختہ دستاویزات سے معلومات نکالتا ہے، output کو JSON schemas کے ذریعے validate کرتا ہے، اور high accuracy برقرار رکھتا ہے۔ اسے edge cases درست طور پر سنبھالنے چاہئیں۔

---

# حصہ I: نظریاتی بنیادیں

یہ حصہ وہ بنیادی نظریہ بیان کرتا ہے جس کی آپ کو امتحان میں کامیابی کے لیے ضرورت ہے۔ مواد کو technologies اور concepts کے مطابق ترتیب دیا گیا ہے، نہ کہ امتحانی domains کے مطابق — اس سے ہر topic کی گہری سمجھ بنتی ہے۔

---

# باب 1: Claude API — Model Interaction کی بنیادیں

> دستاویزات: [Messages API](https://platform.claude.com/docs/en/api/messages) | [Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

## 1.1 API Request Structure

Claude API ایک request–response model پر کام کرتا ہے۔ Claude Messages API request میں عموماً یہ شامل ہوتا ہے:

```json
{
	"model": "claude-sonnet-4-6",
	"max_tokens": 1024,
	"system": "You are a helpful assistant.",
	"messages": [
		{"role": "user", "content": "Hi!"},
		{"role": "assistant", "content": "Hello!"},
		{"role": "user", "content": "How are you?"}
	],
	"tools": [...],
	"tool_choice": {"type": "auto"}
}
```

**اہم فیلڈز:**
- `model` — model selection (`claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`)
- `max_tokens` — response میں زیادہ سے زیادہ tokens
- `system` — system prompt (model کے رویے کی تعریف)
- `messages` — conversation history (**full history بھیجنا ضروری ہے**)
- `tools` — available tools کی definitions
- `tool_choice` — tool selection strategy

## 1.2 Message Roles

`messages` array میں تین roles ہوتے ہیں:
- `user` — user messages
- `assistant` — model responses (history بھیجتے وقت شامل ہوتے ہیں)
- `tool` — tool call results (عملاً `tool_result` content block)

**اہم بات:** ہر API request میں مکمل conversation history بھیجیں۔ Model requests کے درمیان state محفوظ نہیں رکھتا؛ ہر call آزاد ہوتی ہے۔

## 1.3 `stop_reason`

Claude API response میں `stop_reason` ہوتا ہے جو بتاتا ہے کہ model نے کیوں رُکا:

| Value | Description | Action |
|---|---|---|
| `"end_turn"` | Model نے جواب مکمل کر لیا | user کو نتیجہ دکھائیں |
| `"tool_use"` | Model tool call چاہتا ہے | tool چلائیں اور result واپس دیں |
| `"max_tokens"` | Token limit ختم ہو گئی | response truncated ہے؛ limit بڑھا سکتے ہیں |
| `"stop_sequence"` | Stop sequence مل گئی | application logic کے مطابق handle کریں |

Agentic systems میں `"tool_use"` اور `"end_turn"` سب سے اہم signals ہیں — یہی loop control کرتے ہیں۔

## 1.4 System Prompt

System prompt ایک خاص instruction ہے جو context اور behavioral rules متعین کرتا ہے۔ یہ:
- `messages` array کا حصہ نہیں ہوتا؛ الگ `system` field میں دیا جاتا ہے
- user messages پر فوقیت رکھتا ہے
- ایک بار load ہو کر پوری گفتگو میں لاگو رہتا ہے
- role، constraints، اور output format کی وضاحت کے لیے استعمال ہوتا ہے

**امتحان کے لیے اہم:** system prompt کی wording tool selection کو غیر ارادی طور پر متاثر کر سکتی ہے۔ مثال کے طور پر “ہمیشہ customer کی تصدیق کریں” جیسی ہدایت model کو `get_customer` ضرورت سے زیادہ استعمال کرنے پر لے جا سکتی ہے۔

## 1.5 Context Window

Context window وہ کل متن (tokens) ہے جسے model ایک وقت میں process کر سکتا ہے۔ اس میں شامل ہے:
- System prompt
- مکمل message history
- Tool definitions
- Tool results

**اہم مسائل:**

1. **Lost-in-the-middle effect:** لمبے input کے آغاز اور اختتام کی معلومات زیادہ مؤثر ہوتی ہیں، درمیان کی details miss ہو سکتی ہیں۔ حل: اہم معلومات شروع یا آخر میں رکھیں۔

2. **Tool results کا جمع ہونا:** ہر tool call context میں output شامل کرتی ہے۔ اگر tool 40+ fields واپس کرے مگر صرف 5 اہم ہوں تو context ضائع ہوتا ہے۔

3. **Progressive summarization:** history compress کرنے پر numeric values، percentages، اور dates اکثر vague ہو جاتی ہیں۔

---

# باب 2: Tools اور `tool_use`

> دستاویزات: [Tool Use](https://platform.claude.com/docs/en/build-with-claude/tool-use)

## 2.1 `tool_use` کیا ہے

`tool_use` وہ mechanism ہے جس کے ذریعے Claude external functions call کر سکتا ہے۔ Model براہِ راست code نہیں چلاتا — وہ structured tool call بناتا ہے؛ آپ کا code اسے execute کر کے result واپس کرتا ہے۔

## 2.2 Tool Definition

ہر tool JSON schema کے ذریعے define ہوتا ہے:

```json
{
	"name": "get_customer",
	"description": "Finds a customer by email or ID. Returns the customer profile, including name, email, order history, and account status. Use this tool BEFORE lookup_order to verify the customer's identity. Accepts an email (format: user@domain.com) or a numeric customer_id.",
	"input_schema": {
		"type": "object",
		"properties": {
			"email": {"type": "string", "description": "Customer email"},
			"customer_id": {"type": "integer", "description": "Numeric customer ID"}
		},
		"required": []
	}
}
```

**Tool description کے اہم نکات:**

1. Description ہی tool selection کا بنیادی mechanism ہے۔ Minimal descriptions غلط selection کا سبب بنتی ہیں۔
2. Description میں یہ شامل کریں: tool کیا کرتا ہے، کیا واپس کرتا ہے، input format کیا ہے، edge cases کیا ہیں، اور یہ کب استعمال ہو۔
3. Overlapping descriptions سے بچیں۔
4. Built-in tools اور MCP tools میں overlap ہو تو MCP tool کو بہتر اور واضح بنائیں۔

## 2.3 `tool_choice`

| Value | Behavior | کب استعمال کریں |
|---|---|---|
| `{ "type": "auto" }` | Model خود طے کرتا ہے | عام default |
| `{ "type": "any" }` | Model کو لازماً tool call کرنی ہوگی | جب structured output چاہیے |
| `{ "type": "tool", "name": "extract_metadata" }` | خاص tool لازماً call ہوگی | forced first step / order کے لیے |

## 2.4 JSON Schemas for Structured Output

JSON schemas کے ساتھ `tool_use` استعمال کرنا Claude سے structured output لینے کا سب سے reliable طریقہ ہے۔ یہ syntax errors کم کرتا ہے اور required structure نافذ کرتا ہے، مگر semantic correctness کی ضمانت نہیں دیتا۔

**Design اصول:**
1. صرف وہ fields required رکھیں جو ہمیشہ ملنے چاہئیں۔
2. ممکنہ missing data کے لیے nullable fields استعمال کریں۔
3. `"other"` اور `"unclear"` جیسے enum values شامل کریں تاکہ information ضائع نہ ہو۔

## 2.5 Syntax اور Semantic Errors

| Error type | Example | Mitigation |
|---|---|---|
| **Syntax** | Invalid JSON، غلط field type | JSON schema کے ساتھ `tool_use` |
| **Semantic** | Totals match نہیں کرتے، value غلط field میں | Validation checks، feedback retry |

---

# باب 3: Claude Agent SDK — Agentic Systems بنانا

> دستاویزات: [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) | [Hooks](https://platform.claude.com/docs/en/agent-sdk/hooks) | [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) | [Sessions](https://platform.claude.com/docs/en/agent-sdk/sessions)

## 3.1 Agentic Loop

Agentic loop میں Claude صرف جواب نہیں دیتا، بلکہ actions کی sequence چلاتا ہے:

1. Claude کو tools کے ساتھ request بھیجیں
2. Response لیں
3. `stop_reason` چیک کریں:
	 - `"tool_use"` → tool چلائیں، result history میں ڈالیں، پھر دوبارہ request
	 - `"end_turn"` → task مکمل، نتیجہ user کو دیں
4. مکمل ہونے تک دہرائیں

**درست signal:** completion کے لیے `stop_reason == "end_turn"` دیکھیں۔ Text parsing یا arbitrary iteration limit قابلِ اعتماد نہیں۔

## 3.2 `AgentDefinition`

```python
agent = AgentDefinition(
		name="customer_support",
		description="Handles customer requests for returns and order issues",
		system_prompt="You are a customer support agent...",
		allowed_tools=["get_customer", "lookup_order", "process_refund", "escalate_to_human"],
)
```

اہم چیزیں: `name`، `description`، `system_prompt`، اور `allowed_tools`۔ Least privilege اصول اپنائیں۔

## 3.3 Coordinator اور Subagents

Multi-agent systems اکثر hub-and-spoke topology استعمال کرتی ہیں:

```
				 Coordinator
				/     |      \
	 Subagent1  Subagent2  Subagent3
```

Coordinator task کو توڑتا ہے، subagents منتخب کرتا ہے، کام سونپتا ہے، نتائج جوڑتا ہے، errors handle کرتا ہے، اور user تک final جواب پہنچاتا ہے۔

**اہم اصول:** subagents کا context الگ ہوتا ہے؛ وہ parent history خود بخود inherit نہیں کرتے۔

## 3.4 `Task` Tool

Subagents `Task` tool کے ذریعے spawn ہوتے ہیں۔ Coordinator کے `allowed_tools` میں `"Task"` ہونا چاہیے۔

**صحیح context passing:**
- `Task: "Analyze the document"` کافی نہیں
- `Task: "Analyze this document. Full text: ... Output schema: ..."` درست ہے

Coordinator ایک response میں multiple `Task`s بھیج سکتا ہے، لہٰذا parallel subagents ممکن ہیں۔

## 3.5 Hooks

Hooks lifecycle کے مخصوص points پر work کرتے ہیں۔

**PostToolUse** tool result کو model تک پہنچانے سے پہلے normalize کر سکتا ہے:

```python
@hook("PostToolUse")
def normalize_dates(tool_result):
		return normalized_result
```

**PreToolUse** policy violation block کر سکتا ہے:

```python
@hook("PreToolUse")
def enforce_refund_limit(tool_call):
		if tool_call.name == "process_refund" and tool_call.args.amount > 500:
				return redirect_to_escalation(tool_call)
```

**یاد رکھیں:** hooks deterministic ہوتے ہیں؛ prompt instructions probabilistic ہوتی ہیں۔ Critical business rules کے لیے hooks بہتر ہیں۔

---

# باب 4: Model Context Protocol (MCP)

> دستاویزات: [MCP](https://modelcontextprotocol.io/) | [Tools](https://modelcontextprotocol.io/docs/concepts/tools) | [Resources](https://modelcontextprotocol.io/docs/concepts/resources) | [Servers](https://modelcontextprotocol.io/docs/concepts/servers)

## 4.1 MCP کیا ہے

MCP ایک open protocol ہے جو external systems کو Claude سے جوڑتا ہے۔ اس کے تین بنیادی resource types ہیں:

1. **Tools** — actions کے لیے functions
2. **Resources** — context data (documentation، schemas، catalogs)
3. **Prompts** — predefined task templates

## 4.2 MCP Servers

MCP server ایک process ہے جو tools/resources expose کرتا ہے۔ Connect ہونے پر tools discover ہو جاتے ہیں اور descriptions کے مطابق استعمال ہوتے ہیں۔

## 4.3 Configuration

**Project config (`.mcp.json`)** ٹیم کے لیے:

```json
{
	"mcpServers": {
		"github": {
			"command": "npx",
			"args": ["-y", "@modelcontextprotocol/server-github"],
			"env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}
		}
	}
}
```

Project config version control میں ہوتی ہے؛ secrets environment variables سے آتی ہیں۔ User config (`~/.claude.json`) personal/experimental servers کے لیے ہوتی ہے۔

## 4.4 `isError`

MCP tool errors میں `isError: true` استعمال کریں۔ Generic errors کے بجائے structured error واپس کریں:

```json
{
	"isError": true,
	"content": {
		"errorCategory": "transient",
		"isRetryable": true,
		"message": "The service is temporarily unavailable."
	}
}
```

## 4.5 Resources

Resources وہ data ہیں جو agent بغیر action کیے پڑھ سکتا ہے: schemas، docs، content catalogs، summaries۔ یہ exploratory tool calls کم کرتے ہیں۔

---

# باب 5: Claude Code — Configuration اور Workflows

> دستاویزات: [Claude Code](https://code.claude.com/docs/en/overview) | [Memory / CLAUDE.md](https://code.claude.com/docs/en/memory) | [Skills](https://code.claude.com/docs/en/skills) | [MCP](https://code.claude.com/docs/en/mcp) | [Hooks](https://code.claude.com/docs/en/hooks) | [Sub-agents](https://code.claude.com/docs/en/sub-agents) | [GitHub Actions](https://code.claude.com/docs/en/github-actions) | [Headless](https://code.claude.com/docs/en/headless)

## 5.1 CLAUDE.md Hierarchy

CLAUDE.md تین سطحوں پر ہو سکتا ہے:
- **User-level:** `~/.claude/CLAUDE.md` — صرف اسی user پر لاگو
- **Project-level:** `.claude/CLAUDE.md` یا root `CLAUDE.md` — پوری team کے لیے
- **Directory-level:** subdirectories میں CLAUDE.md — مخصوص folder conventions

## 5.2 `@path` Syntax

CLAUDE.md میں `@path` سے external files refer کیے جا سکتے ہیں تاکہ config modular ہو:

```markdown
Coding standards @./standards/coding-style.md میں ہیں
Test rules @./standards/testing-requirements.md میں ہیں
```

## 5.3 `.claude/rules/`

`.claude/rules/` rules کو topic کے لحاظ سے organize کرتا ہے اور `paths` کے ذریعے conditional loading دیتا ہے:

```yaml
---
paths: ["src/api/**/*"]
---

API files کے لیے async/await اور explicit error handling استعمال کریں۔
```

## 5.4 Commands اور Skills

`.claude/commands/` project commands کے لیے ہے، جبکہ `~/.claude/commands/` personal commands کے لیے۔ `.claude/skills/` میں frontmatter کے ساتھ skills ملتی ہیں۔

## 5.5 Skills اور `context: fork`

`context: fork` skill کو isolated context میں چلاتا ہے۔ `allowed-tools` سے tool access محدود کریں، اور `argument-hint` سے required input مانگیں۔

## 5.6 Planning Mode

Planning mode بڑی architectural تبدیلیوں، multiple approaches، اور unfamiliar codebases کے لیے بہترین ہے۔ Direct execution چھوٹے اور واضح changes کے لیے بہتر ہے۔

## 5.7 `/compact` اور `/memory`

`/compact` context compress کرتا ہے، اور `/memory` notes اور preferences سنبھالنے میں مدد دیتا ہے۔

## 5.8 Claude Code CLI for CI/CD

`-p` / `--print` non-interactive mode کے لیے استعمال ہوتا ہے:

```bash
claude -p "Analyze this pull request for security issues"
```

Structured output کے لیے `--output-format json` اور `--json-schema` استعمال کریں۔

---

# باب 6: Prompt Engineering — Advanced Techniques

> دستاویزات: [Prompt Engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

## 6.1 Few-shot Prompting

Few-shot prompting میں 2–4 examples دے کر expected behavior دکھایا جاتا ہے۔ یہ vague instructions سے زیادہ مؤثر ہے کیونکہ example ambiguity کم کرتا ہے۔

## 6.2 Explicit Criteria

Vague instructions کے بجائے clear criteria دیں: کیا flag کرنا ہے، کیا ignore کرنا ہے، اور severity کیسے decide کرنی ہے۔

## 6.3 Prompt Chaining

Complex task کو focused steps میں توڑیں: local analysis، پھر integration pass۔ یہ attention dilution کم کرتا ہے۔

## 6.4 Interview Pattern

Claude سے clarifying questions پوچھوانا design ambiguity سامنے لاتا ہے، خاص طور پر جب domain unfamiliar ہو۔

## 6.5 Validation and Retry

Extraction fail ہو تو original document، incorrect output، اور specific validation error کے ساتھ retry کریں۔

## 6.6 Self-correction

Model stated value اور calculated value دونوں نکالے؛ conflict ہو تو discrepancy handle کریں۔

---

# باب 7: Message Batches API

> دستاویزات: [Message Batches](https://platform.claude.com/docs/en/build-with-claude/message-batches)

## 7.1 Overview

Message Batches API asynchronous processing کے لیے ہے: 50% savings، up to 24 hours window، اور multi-turn tool calling supported نہیں۔ `custom_id` سے requests اور responses link ہوتے ہیں۔

## 7.2 کب استعمال کریں

Pre-merge checks اور interactive tasks کے لیے synchronous API، جبکہ overnight reports اور bulk jobs کے لیے Batch API استعمال کریں۔

## 7.3 `custom_id`

`custom_id` result کو original document سے جوڑنے، failures identify کرنے، اور صرف failed items دوبارہ submit کرنے میں مدد دیتا ہے۔

---

# باب 8: Task Decomposition Strategies

## 8.1 Fixed Pipelines

Predictable tasks کے لیے fixed pipeline استعمال کریں، جیسے Document → Extraction → Validation → Final output۔

## 8.2 Dynamic Decomposition

Open-ended tasks میں subtasks intermediate results کی بنیاد پر بنتے ہیں۔

## 8.3 Multi-pass Code Review

Large PRs کے لیے per-file analysis کے بعد cross-file integration pass کریں تاکہ attention dilution کم ہو۔

---

# باب 9: Escalation اور Human-in-the-Loop

## 9.1 کب Escalate کریں

Explicit user request، policy gaps، progress نہ ہونا، threshold سے اوپر financial action، یا ambiguous matching کی صورت میں escalate کریں۔ Sentiment analysis اور self-rated confidence unreliable ہیں۔

## 9.2 Escalation Patterns

پہلے مسئلہ resolve کرنے کی کوشش کریں، پھر اگر policy gap یا explicit insistence ہو تو human کو hand off کریں۔

## 9.3 Structured Handoff

Escalation پر customer ID، issue summary، actions taken، اور recommended action شامل کریں تاکہ human operator کو مکمل context ملے۔

## 9.4 Confidence Calibration

Field-level confidence scores، calibration on labeled data، اور stratified sampling استعمال کریں۔

---

# باب 10: Multi-agent Systems میں Error Handling

## 10.1 Error Categories

Transient errors retryable ہیں، validation errors input fix مانگتی ہیں، business errors policy-driven ہوتی ہیں، اور permission errors generally escalate کی جاتی ہیں۔

## 10.2 Anti-patterns

Generic “search unavailable” response، silent suppression، یا پورا workflow abort کرنا نقصان دہ ہے۔ Structured errors واپس کریں۔

## 10.3 Structured Subagent Error

Structured error میں failure type، attempted query، partial results، alternative approaches، اور coverage impact شامل کریں۔

## 10.4 Final Synthesis میں Coverage

Report میں واضح کریں کہ کون سی sections fully covered ہیں، کون سی partially covered ہیں، اور کہاں gaps باقی ہیں۔

---

# باب 11: Production Systems میں Context Management

## 11.1 Facts Separate Block میں

Transactional facts کو persistent case facts block میں رکھیں تاکہ summarization کے باوجود critical data ضائع نہ ہو۔

## 11.2 Tool Results Trimming

PostToolUse hook سے صرف relevant fields رکھیں۔

## 11.3 Position-aware Input

Important findings شروع میں اور action items آخر میں رکھیں تاکہ lost-in-the-middle effect کم ہو۔

## 11.4 Scratchpad Files

Verbose findings scratchpad میں لکھیں تاکہ long investigations میں context محفوظ رہے۔

## 11.5 Subagents کو Delegate کرنا

Exploration subagents میں دیں اور main context میں صرف summary رکھیں۔

## 11.6 Structured State Persistence

ہر agent اپنی state manifest یا JSON file میں export کرے تاکہ crash recovery ممکن ہو۔

---

# باب 12: Provenance کو محفوظ رکھنا

## 12.1 Attribution Loss

Claim کے ساتھ source URL، publication date، اور confidence رکھیں۔

## 12.2 Conflicting Data

اگر sources مختلف values دیں تو دونوں کو attribution کے ساتھ محفوظ رکھیں اور conflict flag کریں۔

## 12.3 Dates

Temporal differences کو contradiction سمجھنے سے پہلے publication dates دیکھیں۔

## 12.4 Content Type کے مطابق Render

Financial data tables میں، news prose میں، technical findings structured lists میں، اور time series chronological order میں دکھائیں۔

---

# باب 13: Claude Code کے Built-in Tools

## 13.1 Tool Selection Reference

| Task | Tool | Example |
|---|---|---|
| pattern سے file تلاش کرنا | **Glob** | `**/*.test.tsx` |
| file contents میں search | **Grep** | function name, error message |
| file پڑھنا | **Read** | analysis کے لیے |
| نیا file بنانا | **Write** | scratch سے |
| precise edit | **Edit** | unique text match |
| shell command | **Bash** | git، npm، tests |

## 13.2 Incremental Investigation

ایک ساتھ سب files نہ پڑھیں؛ پہلے entry points، پھر usages، پھر consumer files دیکھیں۔

## 13.3 Read + Write Fallback

اگر Edit fail ہو تو Read کریں، تبدیلی programmatically کریں، پھر Write کریں۔

---

# حصہ II: امتحانی ڈومین نوٹس

---

## ڈومین 1: Agent Architecture اور Orchestration (27%)

Agentic loops، coordinator–subagent architecture، `Task` کے ذریعے spawning، hooks، escalation، اور multi-step workflows پر فوکس کریں۔

## ڈومین 2: Tool Design اور MCP Integration (18%)

Tool descriptions، `tool_choice`, JSON schema output، structured errors، MCP servers، resources، اور built-in tools کے فرق کو سمجھیں۔

## ڈومین 3: Claude Code Configuration اور Workflows (20%)

CLAUDE.md hierarchy، `.claude/rules/`, commands، skills، planning mode، `context: fork`, اور CI/CD integration اہم ہیں۔

## ڈومین 4: Prompt Engineering اور Structured Output (20%)

Few-shot prompting، explicit criteria، prompt chaining، validation/retry loops، JSON schema enforcement، اور batch-friendly prompting پر توجہ دیں۔

## ڈومین 5: Context Management اور Reliability (15%)

Summarization risks، lost-in-the-middle، trimming tool output، confidence calibration، escalation، اور provenance preservation یاد رکھیں۔

---

# عملی مشقیں

## Exercise 1: Multi-tool Agent with Escalation Logic

Goal: tool integration، structured errors، اور escalation کے ساتھ agent loop بنائیں۔

## Exercise 2: Configuring Claude Code for Team Development

Goal: CLAUDE.md، custom commands، path-specific rules، اور MCP servers configure کریں۔

## Exercise 3: Structured Data Extraction Pipeline

Goal: JSON schema، validation/retry loops، اور Message Batches API کے ساتھ extraction pipeline بنائیں۔

## Exercise 4: Designing and Debugging a Multi-agent Research Pipeline

Goal: subagent orchestration، explicit context passing، error propagation، اور source tracking implement کریں۔

---

# Appendix: Technologies and Concepts

| Technology | Key aspects |
|---|---|
| **Claude Agent SDK** | agent loops, `stop_reason`, hooks, `Task`, `allowedTools` |
| **MCP** | servers, tools, resources, `isError`, `.mcp.json` |
| **Claude Code** | CLAUDE.md, `.claude/rules/`, `.claude/commands/`, `.claude/skills/`, planning mode |
| **Claude Code CLI** | `-p`, `--output-format json`, `--json-schema` |
| **Claude API** | `tool_use`, `tool_choice`, `stop_reason`, `max_tokens` |
| **Message Batches API** | 50% savings, 24-hour window, `custom_id` |
| **JSON Schema** | required/optional, nullable, enum values |
| **Few-shot prompting** | ambiguous scenarios کے لیے examples |
| **Prompt chaining** | sequential decomposition |
| **Context window** | token budget, lost-in-the-middle |
| **Confidence calibration** | field-level scoring, stratified sampling |

---

# Out-of-Scope Topics

یہ موضوعات امتحان میں شامل نہیں ہیں:

- Claude models کی fine-tuning
- Authentication، billing، یا account management
- مخصوص programming languages کی تفصیلی implementation
- MCP servers کی hosting/infrastructure
- Claude کی internal architecture یا model weights
- Constitutional AI، RLHF، یا safety training
- Embeddings یا vector databases کی implementation details
- Computer use / browser automation
- Vision / image analysis
- Streaming API یا SSE
- Rate limiting اور detailed API cost calculations
- OAuth اور API key rotation details
- Cloud-provider-specific configs
- Performance benchmarks
- Prompt caching implementation details
- Token counting algorithms

---

# Preparation Recommendations

1. Claude Agent SDK کے ساتھ ایک agent بنائیں
2. Claude Code کو real project پر configure کریں
3. MCP tools design اور test کریں
4. Data extraction pipeline بنائیں
5. Prompt engineering practice کریں
6. Context management patterns سیکھیں
7. Escalation اور human-in-the-loop workflows سمجھیں
8. Practice exam حل کریں