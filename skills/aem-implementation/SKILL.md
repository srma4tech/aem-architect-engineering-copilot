---
name: aem-implementation
description: Implement or explain Java and AEM backend work across Sling, OSGi, JCR/Oak, workflows, jobs, assets, MSM, headless, integrations, and tests. Use when the user needs code or a concrete implementation approach.
license: MIT
---

# AEM Implementation

1. Establish AEM version, API/dependency level, execution tier, and desired behavior. Use repository evidence when available; do not assume a project baseline.
2. Propose the smallest design that fits the requirement. Explain API choices, component boundaries, and supported-version caveats.
3. Address lifecycle and concurrency: close only resources owned by the code; avoid shared mutable request state; use scoped service resolvers and least-privilege subservice mappings.
4. For Oak, constrain queries, verify indexes/plans, avoid broad traversal and repeated repository reads. For async work, define idempotency, retry, ordering, timeout, duplicate, poison-item, and recovery behavior.
5. For external calls, define connection/read timeouts, bounded retries, circuit/overload behavior where warranted, data validation, secret handling, and failure visibility. Avoid blocking request threads for work that can be asynchronous.
6. Consider Dispatcher/CDN cacheability, invalidation, authorization, and content freshness for rendered or API responses.
7. Provide focused code or pseudocode with error paths, logging, and test seams. Mention deployment/configuration and AEM 6.5 versus Cloud Service differences only when material.
8. State validation steps suited to the change: unit/integration tests, AEM SDK or target environment checks, query explain, security checks, and operational signals. Never report a check as passed unless run.

Cover DAM processing, MSM rollout/inheritance, Content Fragments/GraphQL, workflows, Sling Events/Jobs, and schedulers according to their actual lifecycle and deployment topology; do not force one pattern across all cases.

## AEM production patterns

### DAM and Assets

- Treat upload, binary persistence, metadata updates, processing, rendition generation, and downstream publication as distinct lifecycle stages. Identify which AEM 6.5 workflow/process or Cloud Service asset-processing capability is actually configured; verify supported extension points for the target release.
- Keep large-binary work off request threads. For event-driven processing, assume duplicate delivery and retries are possible: make updates idempotent, record enough state to resume safely, and define how poison assets are quarantined or replayed.
- Check processing-profile/workflow scope, rendition count and dimensions, metadata writes, permissions, and downstream calls. Avoid launcher loops where a workflow's own writes retrigger the same processing path.
- Monitor backlog age/depth, processing duration and failures, rendition/storage growth, and publication lag. Test representative file sizes and formats, including malformed files and partial downstream outages.
- Do not depend on instance-local disk for durable binaries or work state. Compare the configured AEM 6.5 processing path with the supported Cloud Service path rather than assuming identical workflow steps or APIs.

### MSM

- Establish the source/blueprint, Live Copy relationship, rollout configuration, inheritance state, and any locally modified or cancelled properties before recommending a rollout. Rollout is a content mutation with a real blast radius.
- Test the selected rollout configuration and action on representative pages, components, nested Live Copies, and locally authored overrides. Check resulting content, inheritance, permissions, references, and downstream publication before broad rollout.
- For large trees, estimate scope and repository work, monitor rollout duration/failures, and define how partial completion is detected and resumed. Avoid custom bulk updates that bypass expected MSM semantics.
- Verify rollout behavior and supported APIs against the installed AEM 6.5 service pack or current Cloud Service documentation. Include author permissions and operational ownership in the plan; do not assume rollout is atomic or identical across versions.

### Content Fragments and GraphQL

- Treat Content Fragment Models and GraphQL response shapes as consumer-facing contracts. Review model changes for backward compatibility, required-field effects, references, variations, and rollout sequencing across producers and consumers.
- Bound query cost: request only needed fields, constrain large collections with supported pagination/filtering, and check the generated query's repository access and relevant indexes. Measure realistic fragment counts and nested references.
- Separate public cacheable delivery from authenticated or personalized delivery. Validate endpoint exposure, authorization, Dispatcher/CDN allowlists, cache keys, invalidation, and stale-content behavior together; never cache private responses as public.
- Test schema/model changes, empty and large result sets, missing references, malformed queries, permission boundaries, and cache invalidation. Confirm endpoint and persisted-query behavior for the target AEM version rather than assuming parity between 6.5 and Cloud Service.

### Workflows, Sling Jobs, and Schedulers

- Choose by lifecycle semantics: workflows for content-oriented authoring/review processes, jobs for discrete asynchronous work that needs queueing and retry handling, and schedulers for time-based triggers. Verify the exact service behavior and cluster topology for the installed release.
- Design job and workflow steps for duplicate execution, partial completion, deployment interruption, and retry. Use idempotency keys or durable state where needed; define bounded retries, poison-item handling, replay, and cleanup. Do not treat a scheduler tick as a durable work queue.
- Keep long-running work off request threads. Bound concurrency and external calls, avoid holding repository sessions/resolvers across waits, and prevent workflow launchers or job consumers from recursively generating unbounded work.
- For schedulers, establish whether execution is single-instance or occurs on multiple active instances in the target topology; make the task safe under overlap or use a supported coordination mechanism. Never infer cluster leadership or exactly-once behavior from local development.
- Monitor queue depth and oldest-item age, workflow/job failures and retries, scheduler lag/overlap, processing duration, and stuck work. Test dependency outages, restart/deploy during execution, retry exhaustion, and recovery on both AEM 6.5 and Cloud Service paths where applicable.
- Persist durable state in supported repository or external storage, not local instance files. Apply least-privilege service users to each operation and validate permissions under the actual execution identity.
