---
name: aem-security
description: Assess AEM code, configuration, architecture, and operational exposure for security risk. Use for threat modeling, access-control changes, security reviews, or suspected vulnerabilities.
license: MIT
---

# AEM Security

1. Define assets, trust boundaries, attacker-controlled inputs, identities, exposure path, and AEM tier. Use the code/configuration and deployment facts provided.
2. Check authentication and authorization, effective ACLs, service-user mappings and least privilege, resolver scope, servlet/filter exposure, Dispatcher/CDN rules, and private-response caching.
3. Inspect relevant application risks: input validation, output encoding, XSS, CSRF, SSRF, path traversal, unsafe parsing/deserialization, injection, information leakage, secrets, and dependency trust.
4. For each material finding, state evidence, preconditions at a high level, impact, severity, recommended fix, and a validation method. Separate confirmed vulnerability from potential risk.
5. Consider AEM 6.5 versus Cloud Service configuration/deployment constraints when relevant; verify version-sensitive Adobe guidance.
6. Recommend defense in depth and safe rollout. Avoid exposing exploit payloads or requesting real secrets; use placeholders and approved secret stores.

Do not infer security from the presence of a Dispatcher rule or service user alone. Assess effective behavior and permissions.
