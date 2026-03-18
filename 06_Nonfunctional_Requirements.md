# 06 Nonfunctional Requirements

## Document Metadata

- Project: `[Project Name]`
- Version: `v0.1`
- Status: `Draft | In Review | Approved`
- Owner: `[Team or Person]`
- Last Updated: `[YYYY-MM-DD]`

---

## 1. Purpose

Capture nonfunctional requirements (NFRs) such as reliability, performance, security, maintainability, and auditability.

---

## 2. Reliability

| Requirement | Target | Measurement Method | Owner |
| --- | --- | --- | --- |
| Pipeline success rate | `[e.g., >= 99%]` | `[how measured]` | `[owner]` |
| Recovery time objective | `[e.g., <= 4 hours]` | `[how measured]` | `[owner]` |

---

## 3. Performance

| Requirement | Target | Measurement Method | Owner |
| --- | --- | --- | --- |
| End-to-end runtime | `[target]` | `[how measured]` | `[owner]` |
| Throughput | `[target]` | `[how measured]` | `[owner]` |

---

## 4. Security and Privacy

- Authentication and authorization: `[approach]`
- Secret management: `[approach]`
- Encryption at rest/in transit: `[approach]`
- Data classification handling: `[approach]`
- Audit logging requirements: `[approach]`

---

## 5. Maintainability

- Code quality standards: `[linting, tests, review gates]`
- Documentation standards: `[required docs]`
- Dependency management: `[policy]`
- Backward compatibility policy: `[policy]`

---

## 6. Observability

- Required logs: `[list]`
- Required metrics: `[list]`
- Alerting thresholds: `[list]`
- On-call or incident process: `[process]`

---

## 7. Scalability

- Expected growth assumptions: `[data volume/users/frequency]`
- Scaling strategy: `[vertical/horizontal/partitioning]`
- Capacity limits and thresholds: `[limits]`

---

## 8. Compliance and Auditability

- Applicable standards/policies: `[list]`
- Traceability requirements: `[run IDs, artifact links, lineage]`
- Audit evidence retention: `[duration and location]`

---

## 9. Testing Strategy for NFRs

- Reliability tests: `[plan]`
- Load/performance tests: `[plan]`
- Security tests: `[plan]`
- Disaster recovery tests: `[plan]`

---

## 10. Acceptance Criteria

- [ ] All NFR targets are defined and measurable
- [ ] Monitoring and alerting are implemented
- [ ] Security controls are documented and verified
- [ ] Recovery procedures are tested
- [ ] Audit requirements are satisfied

---

## 11. Change Log

| Date | Change | Author |
| --- | --- | --- |
| `[YYYY-MM-DD]` | `[what changed]` | `[name]` |
