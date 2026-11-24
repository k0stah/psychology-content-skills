#!/usr/bin/env python3
"""Validate this collection's structure and publishable files using the stdlib.

This checks the deliberately small frontmatter subset used here; it is not a
general YAML parser, a secret scanner, or a behavioral evaluation of an agent.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def public_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, capture_output=True, check=False,
    )
    if result.returncode:
        errors.append("Run validation in a Git checkout of this collection.")
        return []
    return sorted({ROOT / p.decode("utf-8") for p in result.stdout.split(b"\0") if p})


def check_skills() -> int:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    require(bool(skills), "No skills found.")
    for path in skills:
        name = path.parent.name
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        require(match is not None, f"{name}: missing frontmatter.")
        if not match:
            continue
        fields = dict(re.findall(r"^([a-z_-]+):\s*([^\n]*)", match[1], re.M))
        require(set(fields) == {"name", "description"}, f"{name}: use name and description only.")
        declared_name = fields.get("name", "").strip().strip('\"\'')
        require(declared_name == name, f"{name}: frontmatter name does not match directory.")
        require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)) and len(name) < 64,
                f"{name}: invalid skill name.")
        description = fields.get("description", "").strip().strip('\"\'')
        require(len(description) >= 30, f"{name}: description is missing or too vague.")
        require(len(text.splitlines()) < 500, f"{name}: split long instructions into references.")
        require("[TODO" not in text, f"{name}: unfinished initializer placeholder.")
        require("private/psychology-content/context.md" in text,
                f"{name}: shared private context path is missing.")
        metadata = path.parent / "agents" / "openai.yaml"
        require(metadata.is_file(), f"{name}: missing UI metadata.")
        if metadata.is_file():
            content = metadata.read_text(encoding="utf-8")
            require(f"${name}" in content, f"{name}: default prompt must invoke the skill.")
            short = re.search(r'^\s*short_description:\s*"(.*)"\s*$', content, re.M)
            require(short is not None and 25 <= len(short[1]) <= 64,
                    f"{name}: short UI description must be 25–64 characters.")
    return len(skills)


def check_sources() -> int:
    path = ROOT / "sources" / "upstream.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"Cannot load upstream source ledger: {exc}")
        return 0
    require(manifest.get("schema_version") == 1, "Unsupported source ledger schema.")
    sources = manifest.get("sources", [])
    require(bool(sources), "Source ledger is empty.")
    for source in sources:
        label = source.get("id", "unnamed source")
        require(bool(re.fullmatch(r"[a-f0-9]{40}", source.get("revision", "") or "")),
                f"{label}: exact reviewed commit is required.")
        require(source.get("mode") in {"adapted", "reference-only"}, f"{label}: invalid reuse mode.")
        for target in source.get("targets", []):
            require((ROOT / target).is_file(), f"{label}: missing target {target}.")
        if source.get("mode") == "adapted":
            license_path = ROOT / source.get("license_file", "MISSING")
            require(license_path.is_file(), f"{label}: adapted source needs a preserved license.")
            if license_path.is_file():
                data = license_path.read_bytes()
                digest = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
                recorded = next((x["blob_sha"] for x in source.get("reviewed_files", [])
                                 if x.get("path") == "LICENSE"), None)
                require(digest == recorded, f"{label}: preserved notice differs from recorded Git blob.")
    return len(sources)


def check_installation_manifest() -> None:
    try:
        manifest = json.loads((ROOT / "install-manifest.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"Cannot load installation manifest: {exc}")
        return
    require(manifest.get("schema_version") == 1, "Unsupported installation manifest schema.")
    require(manifest.get("installation_unit") == "individual-skill",
            "Install each skill as a separate package.")
    skills = manifest.get("skills", [])
    names = [entry.get("name") for entry in skills]
    actual_names = sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))
    require(sorted(str(name) for name in names) == actual_names,
            "Installation manifest must list every skill exactly once.")
    require(bool(names) and names[-1] == "psychology-blog", "Install the coordinator last.")
    for entry in skills:
        name = entry.get("name")
        if name not in actual_names:
            continue
        expected_path = f"skills/{name}"
        require(entry.get("path") == expected_path, f"{name}: wrong source skill path.")
        folder = ROOT / expected_path
        actual_files = sorted(str(path.relative_to(folder)) for path in folder.rglob("*") if path.is_file())
        require(sorted(entry.get("required_files", [])) == actual_files,
                f"{name}: installation manifest omits or adds bundled resources.")
    attribution = manifest.get("attribution", {})
    expected = {"LICENSE", "NOTICE.md", "sources/upstream.json", "docs/sources.md"}
    expected.update(str(path.relative_to(ROOT)) for path in (ROOT / "LICENSES").glob("*") if path.is_file())
    listed = attribution.get("files", [])
    require(len(listed) == len(expected) and set(listed) == expected,
            "Installation must preserve the project license and complete attribution package.")
    require(all((ROOT / path).is_file() for path in expected), "An attribution resource is missing.")
    require(attribution.get("destination") == "provenance", "Unexpected attribution destination.")
    require(attribution.get("source_record") == "provenance/install-source.json",
            "Installation source record path is inconsistent.")


def check_public_boundary(files: list[Path]) -> None:
    for path in files:
        rel = path.relative_to(ROOT)
        require("private" not in rel.parts, f"Private file is included in Git: {rel}.")
        require(not (path.name == ".env" or path.name.startswith(".env.") and path.name != ".env.example"),
                f"Environment file is included in Git: {rel}.")
        require(not path.is_symlink(), f"Publish regular files only; inspect symlink {rel}.")
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "private/psychology-content/context.md"],
        cwd=ROOT, capture_output=True, check=False,
    )
    require(result.returncode == 0, "Default private context path is not ignored by Git.")


def check_links(files: list[Path]) -> None:
    for path in files:
        if path.suffix != ".md" or not path.is_file():
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for match in re.finditer(r"\[[^\]\n]+\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            target = match[1]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            require((path.parent / local).exists(),
                    f"{path.relative_to(ROOT)}: broken local link {target}.")


def main() -> int:
    files = public_files()
    count = check_skills()
    sources = check_sources()
    check_installation_manifest()
    check_public_boundary(files)
    check_links(files)
    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1
    print(f"PASS: {count} skills, {sources} source records, {len(files)} public files.")
    print("Metadata, installation manifest, local links, preserved license hashes and private-path exclusion passed.")
    print("Behavior, clinical correctness and live integrations are outside this check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
