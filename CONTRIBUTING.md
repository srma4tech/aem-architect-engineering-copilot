# Contributing

Contributions should make the plugin more accurate, portable, and useful to working AEM engineers without increasing instruction duplication.

## Before proposing a change

- Read the main skill and the focused skill relevant to the change.
- Check whether the information already exists elsewhere; keep shared principles in the main skill.
- Use authoritative Adobe sources for version-sensitive AEM claims. Phrase uncertain behavior as a question or verification step.
- Do not include credentials, personal tokens, customer information, or environment-specific configuration.

## Skill guidance

- Use one skill per coherent workflow and write its invocation conditions in the frontmatter description.
- Keep instructions concrete: evidence to inspect, decisions to make, risks to consider, and useful output shape.
- Avoid generic advice, rigid templates that overfit every request, duplicate quality gates, and unsupported “best practice” claims.
- Mention AEM 6.5 versus Cloud Service only where it affects the workflow.
- Update README skill inventory and CHANGELOG for user-visible additions or behavior changes.

## Validation

Run `python scripts/validate_plugin.py` from the repository root. Review the full diff and confirm that changed links and skill references resolve. For schema changes, compare against the canonical [Agent Plugins v1.0.0 specification](https://agent-plugins.org/specification) and schema. The local validator is not a full client-conformance suite.

## Pull requests

Describe the problem, the intended user benefit, affected skills/files, source basis for factual changes, and validation performed. Do not state that validation passed unless it was run successfully.
