---
name: aem-code-review
description: Review AEM or Java code, diffs, and pull requests for correctness and production risk. Use for requested code review; prioritize actionable findings over broad commentary.
license: MIT
---

# AEM Code Review

1. Identify the patch scope, intended behavior, AEM baseline, and available tests/configuration. Review only evidence in the supplied diff and context; label assumptions.
2. Report findings first, ordered by severity and impact. For each include file/line when available, failure scenario, consequence, and concrete fix. Avoid speculative findings and style-only noise.
3. Check correctness and edge cases; API/version compatibility; resolver/session ownership; DS lifecycle and thread safety; Oak query/index cost; async idempotency/retries; external-call timeouts; security/ACLs/input/output handling; cache/Dispatcher behavior; cloud compatibility; logs/metrics and test coverage.
4. Distinguish blockers from follow-up improvements. If there are no material findings, say so and note any limits in review coverage.
5. Preserve behavior in suggested refactors unless a behavior change is explicit. Do not claim tests, builds, or scanners ran unless they did.

Pay particular attention to leaked ResourceResolvers, unbounded traversal, unindexed queries, unsafe path-bound servlets, request-thread network waits, cluster-duplicated schedulers, overprivileged service users, secrets, private-response caching, and local-disk persistence assumptions in Cloud Service.
