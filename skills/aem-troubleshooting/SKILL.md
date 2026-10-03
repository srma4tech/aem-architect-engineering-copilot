---
name: aem-troubleshooting
description: Diagnose AEM production incidents and unexpected behavior using evidence, falsifiable hypotheses, safe mitigations, and recovery plans. Use for outages, errors, regressions, or operational investigations.
license: MIT
---

# AEM Troubleshooting

1. Define impact, scope, start time, affected tier/instances, recent changes, and whether the issue is ongoing. Separate user-reported facts from observed evidence.
2. Build a short timeline and request the highest-value missing evidence. Use logs, access/status patterns, metrics, traces, thread/heap/GC data, query plans, cache headers, queue/workflow state, OSGi config, and deployment differences as relevant.
3. Keep symptom, mechanism, and root cause distinct. Offer at most a few plausible hypotheses, each paired with supporting evidence, a falsification check, and a low-risk next step.
4. Recommend reversible containment before invasive changes. State blast radius, success signal, rollback, and data-loss risk for material mitigations.
5. Confirm root cause only when evidence supports it. Then give permanent correction, recovery/replay steps, prevention, and monitoring/alerting changes.
6. Account for author/publish topology, Dispatcher/CDN, Oak, async processing, and AEM 6.5 versus Cloud Service only as they relate to evidence. Verify platform-specific operational claims.

Prefer concise diagnostic sequences over generic checklists. Never prescribe a production repository/index/config change without an appropriate validation and rollback path.
