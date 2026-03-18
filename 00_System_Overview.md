# 00 System Overview

## Document Metadata

- Project: `[Project Name]`
- Version: `v0.1`
- Status: `Draft | In Review | Approved`
- Owner: `[Team or Person]`
- Last Updated: `[YYYY-MM-DD]`

---

## 1. Purpose

Describe the system at a high level, including what this data product is intended to do.

### Prompt Questions

- What business or mission problem does this system solve?
- Who are the primary users/consumers of the outputs?
- What decisions will this system support?

---

## 2. Scope

### In Scope

- `[Capability 1]`
- `[Capability 2]`
- `[Capability 3]`

### Out of Scope

- `[Explicit non-goal 1]`
- `[Explicit non-goal 2]`

---

## 3. System Goals

1. `[Goal 1]`
2. `[Goal 2]`
3. `[Goal 3]`

Define success criteria for each goal.

---

## 4. Architecture Summary

Provide a short description of each layer.

1. Ingestion Layer: `[summary]`
2. Transformation Layer: `[summary]`
3. Processing Layer: `[summary]`
4. Output Layer: `[summary]`

---

## 5. Data Flow Summary

```text
External Sources
      ->
Raw Ingestion
      ->
Standardized Schemas
      ->
Processing / AI Logic
      ->
Validated Outputs
```

---

## 6. Key Dependencies

- Data platforms: `[e.g., Fabric, OneLake, Blob Storage]`
- Runtime: `[e.g., Python, Spark]`
- External APIs: `[list]`
- Security services: `[e.g., Key Vault]`

---

## 7. Risks and Constraints

- Risk: `[risk]` | Mitigation: `[mitigation]`
- Constraint: `[constraint]` | Impact: `[impact]`

---

## 8. Related Documents

- `docs/01_Data_Sources.md`
- `docs/02_Pipeline_Stages.md`
- `docs/03_Capability_Assessment.md`
- `docs/04_AI_Usage.md`
- `docs/05_Report_Outputs.md`
- `docs/06_Nonfunctional_Requirements.md`
