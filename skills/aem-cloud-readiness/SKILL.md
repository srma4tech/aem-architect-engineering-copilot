---
name: aem-cloud-readiness
description: Assess code, content, operations, and architecture for AEM as a Cloud Service compatibility. Use for cloud readiness reviews, modernization backlogs, or evaluating AEM 6.5 assumptions.
license: MIT
---

# AEM Cloud Readiness

1. Establish the current AEM 6.5 service pack, installed capabilities, customizations, integrations, content volume, and target Cloud Service scope. Mark unknowns explicitly.
2. Assess code/API compatibility, repository content/package design, Oak indexes and queries, OSGi configuration, workflows/jobs/schedulers, local filesystem assumptions, network egress/integrations/secrets, asset processing, Dispatcher/CDN, pipelines, and observability.
3. Classify each item as evidence-backed compatible, requires change, blocked pending evidence, or out of scope. Include impact, owner-facing evidence needed, and recommended disposition.
4. Focus on cloud operating constraints such as immutable deployment, scaling, replaceable instances, managed services, and supported extension points; verify current Adobe requirements instead of relying on remembered restrictions.
5. Prioritize by migration risk and dependency. Define validation and rollback signals for high-impact changes.

Use `aem-migration` when asked for sequencing, cutover, or program planning. Readiness is an assessment, not a guarantee of successful migration.
