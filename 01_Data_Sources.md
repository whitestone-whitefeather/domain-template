# 01 Data Sources

## Document Metadata

- Project: `[Project Name]`
- Version: `v0.1`
- Status: `Draft | In Review | Approved`
- Owner: `[Team or Person]`
- Last Updated: `[YYYY-MM-DD]`

---

## 1. Purpose

Document all source datasets, how they are accessed, and how they are governed.

---

## 2. Source Inventory

| Source Name | Type (Spatial/Tabular/API) | Owner | Access Method | Refresh Cadence | Criticality |
| --- | --- | --- | --- | --- | --- |
| `[name]` | `[type]` | `[owner]` | `[REST/CSV/DB/etc.]` | `[daily/weekly/monthly]` | `[High/Medium/Low]` |

---

## 3. Source Details Template

### 3.1 `[Source Name]`

- Description: `[what this source contains]`
- Business Purpose: `[why needed]`
- Location/URL: `[link/path]`
- Format: `[CSV, GeoJSON, Shapefile, API JSON, etc.]`
- Expected Schema: `[key fields and types]`
- Join Keys: `[field names used for joins]`
- Data Quality Rules:
  - `[rule 1]`
  - `[rule 2]`
- Known Limitations:
  - `[limitation 1]`
  - `[limitation 2]`

Repeat subsection 3.1 for each source.

---

## 4. Access and Authentication

- Auth type: `[public, service principal, managed identity, etc.]`
- Secret handling approach: `[how secrets are managed]`
- Least-privilege controls: `[roles/policies]`

---

## 5. Data Governance and Compliance

- Classification: `[public/internal/confidential]`
- Retention policy: `[policy]`
- Licensing/usage restrictions: `[details]`
- Compliance considerations: `[if any]`

---

## 6. Validation Checklist

- [ ] Source endpoint reachable
- [ ] Schema matches expected version
- [ ] Null/duplicate thresholds acceptable
- [ ] Refresh timestamps within SLA
- [ ] Licensing/compliance validated

---

## 7. Change Log

| Date | Change | Author |
| --- | --- | --- |
| `[YYYY-MM-DD]` | `[what changed]` | `[name]` |
