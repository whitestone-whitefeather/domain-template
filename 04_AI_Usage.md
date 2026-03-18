# 04 AI Usage

## Document Metadata

- Project: `[Project Name]`
- Version: `v0.1`
- Status: `Draft | In Review | Approved`
- Owner: `[Team or Person]`
- Last Updated: `[YYYY-MM-DD]`

---

## 1. Purpose

Define where and how AI is used, including guardrails, prompt strategy, validation, and traceability.

---

## 2. AI Use Cases

| Use Case | Input Data | Model/Provider | Output | Human Review Required |
| --- | --- | --- | --- | --- |
| `[use case]` | `[input]` | `[model/provider]` | `[output]` | `[Yes/No]` |

---

## 3. Prompt Design

### 3.1 System Prompt Template

```text
[Define role, constraints, tone, output format, and refusal boundaries]
```

### 3.2 User Prompt Template

```text
[Describe context, task, required structure, and grounding data]
```

### 3.3 Prompt Versioning

- Prompt ID: `[prompt-id]`
- Version: `[vX.Y]`
- Change rationale: `[reason]`

---

## 4. Safety and Governance

- Disallowed content controls: `[policy summary]`
- PII handling policy: `[policy]`
- Hallucination mitigation strategy:
  - `[grounding approach]`
  - `[verification step]`
- Human-in-the-loop checkpoints: `[where required]`

---

## 5. Evaluation and Quality

- Acceptance criteria:
  - `[criterion 1]`
  - `[criterion 2]`
- Evaluation dataset: `[location]`
- Quality metrics: `[factuality, completeness, consistency, etc.]`
- Drift monitoring cadence: `[cadence]`

---

## 6. Operational Controls

- Retry policy: `[policy]`
- Timeout policy: `[policy]`
- Cost controls: `[token/budget controls]`
- Fallback behavior: `[fallback model or deterministic path]`

---

## 7. Traceability

- Store prompt and model metadata: `[where]`
- Store output and validation artifacts: `[where]`
- Link outputs to run ID: `[how]`

---

## 8. Change Log

| Date | Change | Author |
| --- | --- | --- |
| `[YYYY-MM-DD]` | `[what changed]` | `[name]` |
