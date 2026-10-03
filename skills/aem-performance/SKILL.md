---
name: aem-performance
description: Investigate AEM latency, throughput, capacity, and scalability using measurements across requests, caches, Oak, JVM, queues, and dependencies. Use for performance regressions or capacity planning.
license: MIT
---

# AEM Performance

1. Define the workload, tier, baseline, target, affected percentile, concurrency, and time window. Separate user perception from measured latency.
2. Trace the path relevant to the request: client/CDN/Dispatcher, AEM rendering or endpoint, Sling/OSGi, Oak, async queues, network, and dependencies.
3. Form a bottleneck hypothesis and identify a measurement that can confirm or falsify it before proposing optimization.
4. Inspect relevant signals: percentiles and throughput, cache hit/miss and headers, CPU, heap/allocation/GC, thread pools and blocked work, Oak query plans/indexes/traversal, serialization, dependency latency/timeouts, queue depth and age.
5. Change one material factor at a time where practical. Explain expected effect, trade-off, safety limit, and how to remeasure under representative load.
6. Distinguish correlation from causation. Do not recommend indexes, cache rules, thread-pool increases, or broad caching without query/traffic evidence and invalidation/security analysis.

For Cloud Service, verify current Adobe measurement and scaling guidance. Avoid assuming local production access or persistent local state.
