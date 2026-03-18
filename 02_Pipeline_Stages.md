# 02 Pipeline Stages

## Document Metadata

- Project: `[Project Name]`
- Version: `v0.1`
- Status: `Draft | In Review | Approved`
- Owner: `[Team or Person]`
- Last Updated: `[YYYY-MM-DD]`

---

## 1. Purpose

Describe each stage of the pipeline end-to-end, including inputs, transformations, and outputs.

---

## 2. Pipeline Overview

| Stage | Objective | Input(s) | Output(s) | Trigger | Retry Strategy |
| --- | --- | --- | --- | --- | --- |
| `Bronze` | `[objective]` | `[inputs]` | `[outputs]` | `[schedule/event]` | `[strategy]` |
| `Silver` | `[objective]` | `[inputs]` | `[outputs]` | `[schedule/event]` | `[strategy]` |
| `Gold` | `[objective]` | `[inputs]` | `[outputs]` | `[schedule/event]` | `[strategy]` |

---

## 3. Stage Template

### 3.1 `[Stage Name]`

- Objective: `[what this stage does]`
- Input Datasets: `[list]`
- Core Transformations:
  - `[transformation 1]`
  - `[transformation 2]`
- Business Rules:
  - `[rule 1]`
  - `[rule 2]`
- Output Datasets: `[list]`
- Output Schema: `[link or inline table]`
- Data Quality Checks: `[list checks]`
- Failure Conditions: `[what can fail]`
- Recovery/Backfill Procedure: `[steps]`

Repeat subsection 3.1 for each stage.

---

## 4. Orchestration and Scheduling

- Orchestrator: `[Fabric Pipeline, Airflow, etc.]`
- Schedule: `[cron or cadence]`
- Dependencies: `[upstream/downstream]`
- SLA/SLO targets: `[time and reliability targets]`

---

## 5. Observability

- Logs: `[where to find logs]`
- Metrics: `[latency, row counts, errors]`
- Alerts: `[thresholds and channels]`
- Runbook link: `[path/link]`

---

## 6. Deployment and Environments

- Dev: `[details]`
- Test: `[details]`
- Prod: `[details]`
- Promotion process: `[how code moves environments]`

---

## 7. Change Log

| Date | Change | Author |
| --- | --- | --- |
| `[YYYY-MM-DD]` | `[what changed]` | `[name]` |
