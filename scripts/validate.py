"""Validate skill packaging and local documentation; does not evaluate design quality."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError as exc:
    raise SystemExit("Install development dependencies: python -m pip install -r requirements-dev.txt") from exc


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    def read(path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            return ""

    for required in ("README.md", "README.pt-PT.md", "LICENSE", "CONTRIBUTING.md"):
        if not (root / required).is_file():
            errors.append(f"Missing repository file: {required}")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills/*/SKILL.md found")

    for path in skills:
        content = read(path)
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", content, re.DOTALL)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing YAML frontmatter")
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{path.relative_to(root)}: invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.relative_to(root)}: frontmatter must be a mapping")
            continue
        name = data.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"{path.relative_to(root)}: invalid skill name")
        elif name != path.parent.name:
            errors.append(f"{path.relative_to(root)}: skill name must match its directory")
        description = data.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{path.relative_to(root)}: description must contain 1-1024 characters")
        if data.get("license") != "MIT":
            errors.append(f"{path.relative_to(root)}: expected MIT licence")
        metadata = data.get("metadata", {})
        if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
            errors.append(f"{path.relative_to(root)}: metadata keys and values must be strings")
        licence = path.parent / "LICENSE"
        if not licence.is_file() or read(licence) != read(root / "LICENSE"):
            errors.append(f"{path.relative_to(root)}: bundled licence must match repository licence")
        config = path.parent / "agents" / "openai.yaml"
        if config.is_file():
            try:
                settings = yaml.safe_load(read(config))
                interface = settings["interface"]
                short = interface["short_description"]
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append(f"{config.relative_to(root)}: short description must contain 25-64 characters")
                if not isinstance(interface.get("default_prompt"), str) or f"${name}" not in interface["default_prompt"]:
                    errors.append(f"{config.relative_to(root)}: default prompt must mention the skill")
                if settings.get("policy", {}).get("allow_implicit_invocation") is not True:
                    errors.append(f"{config.relative_to(root)}: automatic selection should be enabled")
            except (yaml.YAMLError, KeyError, TypeError, AttributeError) as exc:
                errors.append(f"{config.relative_to(root)}: invalid interface metadata: {exc}")

    # This repository uses ordinary inline Markdown links without nested parentheses.
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", read(path)):
            target = target.strip().strip("<>")
            if re.match(r"^[A-Za-z]:[\\/]", target):
                errors.append(f"{path.relative_to(root)}: non-portable link {target}")
                continue
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (path.parent / unquote(parts.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link leaves repository: {target}")
            elif not destination.exists():
                errors.append(f"{path.relative_to(root)}: broken local link: {target}")

    try:
        cases = json.loads(read(root / "evals" / "cases.json"))
        if not isinstance(cases, list) or not cases:
            raise ValueError("expected a non-empty list")
        seen: set[str] = set()
        for case in cases:
            if not isinstance(case, dict):
                raise ValueError("each case must be an object")
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id or case_id in seen:
                raise ValueError("case IDs must be non-empty and unique")
            seen.add(case_id)
            if type(case.get("activate")) is not bool:
                raise ValueError(f"{case_id}: activate must be a boolean")
            for key in ("prompt", "setup"):
                if not isinstance(case.get(key), str) or not case[key].strip():
                    raise ValueError(f"{case_id}: {key} must be non-empty text")
            criteria = case.get("criteria")
            if not isinstance(criteria, list) or not criteria or any(not isinstance(item, str) or not item.strip() for item in criteria):
                raise ValueError(f"{case_id}: criteria must be a non-empty list of text")
        if {case["activate"] for case in cases} != {True, False}:
            raise ValueError("include both activation and non-activation cases")
    except (ValueError, TypeError) as exc:
        errors.append(f"evals/cases.json: {exc}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: skill packaging, metadata, local links, and evaluation-case structure")
    print("Visual quality and agent behaviour are not evaluated by this command.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
