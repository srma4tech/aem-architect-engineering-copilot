---
name: aem-migration
description: Plan and de-risk migration from AEM 6.5 to AEM as a Cloud Service, including scope, sequencing, content, code, integrations, validation, cutover, and rollback. Use for migration roadmaps and execution planning.
license: MIT
---

# AEM Migration

1. Establish source topology/version, target scope, content/data volumes, integrations, release constraints, compliance needs, downtime tolerance, and team ownership.
2. Build an evidence-based inventory and readiness backlog. Cover code/APIs, repository/package structure, indexes, workflows and async processing, assets, MSM, external systems, secrets, Dispatcher/CDN, CI/CD, and operations.
3. Sequence work by dependency and risk. Separate platform remediation, content transfer, integration changes, and operational preparation; define entry/exit criteria for each stage.
4. Plan representative rehearsals: content integrity and permissions, functional behavior, query/performance baseline, cache behavior, security, integration failure modes, and rollback/recovery.
5. Define cutover mechanics, data freeze/synchronization where applicable, traffic/DNS or routing changes, acceptance signals, decision owner, rollback trigger, and post-cutover verification. Do not assume a universal migration tool or cutover pattern.
6. Link platform-specific steps to current Adobe documentation. Label unknowns and avoid presenting estimates or compatibility conclusions without inventory evidence.

Return a phased plan with dependencies, risks, evidence gaps, validation, and rollback. Scale detail to the requested horizon.
