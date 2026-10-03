#!/usr/bin/env python3
"""Focused structural checks for this Agent Plugin repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAME_PATTERN = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: invalid or unreadable JSON ({exc})")
        return None


def validate_manifest() -> None:
    path = ROOT / "plugin.json"
    data = load_json(path)
    if not isinstance(data, dict):
        fail("plugin.json: top level must be an object")
        return
    allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
    for key in data.keys() - allowed:
        fail(f"plugin.json: unsupported top-level field {key!r}")
    if data.get("$schema") != PLUGIN_SCHEMA:
        fail("plugin.json: $schema must be the canonical Agent Plugins v1.0.0 schema URL")
    name = data.get("name")
    if not isinstance(name, str) or not 1 <= len(name) <= 64 or not NAME_PATTERN.fullmatch(name):
        fail("plugin.json: name must be 1-64 lowercase letters/digits/dots/hyphens, with alphanumeric ends and no repeated separators")
    for key in ("version", "description", "license", "homepage", "repository"):
        if key in data and not isinstance(data[key], str):
            fail(f"plugin.json: {key} must be a string")
    if "author" in data:
        author = data["author"]
        if not isinstance(author, dict) or author.keys() - {"name", "email", "url"} or any(not isinstance(v, str) for v in author.values()):
            fail("plugin.json: author must contain only optional string fields name, email, and url")
    if "keywords" in data and (not isinstance(data["keywords"], list) or any(not isinstance(v, str) for v in data["keywords"])):
        fail("plugin.json: keywords must be an array of strings")
    if "extensions" in data and (not isinstance(data["extensions"], dict) or any(not isinstance(v, dict) for v in data["extensions"].values())):
        fail("plugin.json: extensions must map namespace names to objects")


def parse_frontmatter(path: Path) -> tuple[dict, str] | None:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: unreadable UTF-8 Markdown ({exc})")
        return None
    if not content.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter opening delimiter")
        return None
    closing = content.find("\n---\n", 4)
    if closing < 0:
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter closing delimiter")
        return None
    try:
        fields = yaml.safe_load(content[4:closing])
    except yaml.YAMLError as exc:
        fail(f"{path.relative_to(ROOT)}: invalid YAML frontmatter ({exc})")
        return None
    if not isinstance(fields, dict):
        fail(f"{path.relative_to(ROOT)}: YAML frontmatter must be a mapping")
        return None
    return fields, content[closing + 5:]


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    if not skills_root.is_dir():
        fail("skills/: required directory is missing")
        return
    folders = [p for p in skills_root.iterdir() if p.is_dir()]
    if not folders:
        fail("skills/: no immediate skill directories found")
    names = {folder.name for folder in folders}
    for folder in folders:
        path = folder / "SKILL.md"
        if not path.is_file():
            fail(f"{folder.relative_to(ROOT)}: missing SKILL.md")
            continue
        parsed = parse_frontmatter(path)
        if parsed is None:
            continue
        fields, body = parsed
        allowed_fields = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        for key in fields.keys() - allowed_fields:
            fail(f"{path.relative_to(ROOT)}: unsupported Agent Skills frontmatter field {key!r}")

        for required in ("name", "description"):
            if required not in fields:
                fail(f"{path.relative_to(ROOT)}: missing required frontmatter field {required!r}")

        name = fields.get("name")
        if (not isinstance(name, str) or not 1 <= len(name) <= 64
                or not SKILL_NAME_PATTERN.fullmatch(name) or name != folder.name):
            fail(f"{path.relative_to(ROOT)}: name must be 1-64 lowercase letters, digits, or single hyphens and match its directory")
        description = fields.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            fail(f"{path.relative_to(ROOT)}: description must be a non-empty string of at most 1024 characters")

        if "license" in fields and (not isinstance(fields["license"], str) or not fields["license"].strip()):
            fail(f"{path.relative_to(ROOT)}: license must be a non-empty string")
        if "compatibility" in fields:
            compatibility = fields["compatibility"]
            if not isinstance(compatibility, str) or not 1 <= len(compatibility.strip()) <= 500:
                fail(f"{path.relative_to(ROOT)}: compatibility must be a non-empty string of at most 500 characters")
        if "metadata" in fields:
            metadata = fields["metadata"]
            if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
                fail(f"{path.relative_to(ROOT)}: metadata must be a mapping of strings to strings")
        if "allowed-tools" in fields and not isinstance(fields["allowed-tools"], str):
            fail(f"{path.relative_to(ROOT)}: allowed-tools must be a space-separated string")
        if "\ufffd" in body or any(marker in body for marker in ("â†", "ðŸ", "â€”", "â€“")):
            fail(f"{path.relative_to(ROOT)}: appears to contain mojibake or replacement characters")
        for reference in re.findall(r"`(aem-[a-z0-9-]+)`", body):
            if reference not in names:
                fail(f"{path.relative_to(ROOT)}: references missing skill {reference!r}")
        check_markdown_links(path, body)


LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_markdown_links(source: Path, content: str) -> None:
    for target in LINK_PATTERN.findall(content):
        target = target.split("#", 1)[0].strip()
        if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I) or target.startswith("mailto:"):
            continue
        resolved = (source.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(f"{source.relative_to(ROOT)}: local link escapes repository: {target}")
            continue
        if not resolved.exists():
            fail(f"{source.relative_to(ROOT)}: broken local link: {target}")


def main() -> int:
    validate_manifest()
    validate_skills()
    for markdown in (ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "CHANGELOG.md"):
        if markdown.is_file():
            try:
                check_markdown_links(markdown, markdown.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError) as exc:
                fail(f"{markdown.name}: unreadable UTF-8 Markdown ({exc})")
    if errors:
        print("Plugin validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    skill_count = sum(1 for p in (ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    print(f"Plugin structure valid: manifest and {skill_count} skills passed local checks.")
    print("Scope: focused local checks only; this is not full JSON Schema, Markdown, or client-conformance validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
