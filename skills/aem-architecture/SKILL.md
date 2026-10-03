---
name: aem-architecture
description: Design or evaluate AEM solutions, platform boundaries, system integrations, and architecture decision records. Use for new systems, major design choices, and Lead or Architect-level trade-offs.
license: MIT
---

# AEM Architecture

1. Clarify the business outcome, actors, content/data flows, scale, latency, availability, security, lifecycle, and constraints. Mark missing inputs as assumptions; ask only when the answer changes the design.
2. Draw the relevant boundaries: author/publish, CDN/Dispatcher, Sling/OSGi, Oak/JCR, async workers, and external systems. Do not include irrelevant layers.
3. Select AEM primitives by semantics and operational behavior. Compare, when relevant: resource-type vs path servlet, Resource API vs JCR API, event vs job vs scheduler vs workflow, synchronous vs queued integration, and cache layers.
4. Evaluate correctness, security/least privilege, throughput and repository cost, failure/retry behavior, deployment and rollback, operability, maintainability, AEM 6.5/Cloud Service fit, and cost.
5. State the recommendation, assumptions, rejected alternatives, trade-offs, and evidence that would change the decision. Avoid context-free “best practice” claims.
6. For significant decisions, produce a concise ADR with context, requirements, options, decision, rationale, consequences, risks, operations, rollback, and validation criteria.

For AEM 6.5 and Cloud Service differences, use `aem-cloud-readiness`; use `aem-migration` for program planning. Verify current platform-specific claims against Adobe documentation when available.
