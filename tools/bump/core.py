import re
from enum import Enum
from pathlib import Path
from typing import Tuple

# Tools for managing project semantic version numbering.
# `bumpversion` is unmaintained and the alternatives don't look
# very reassuring so use a simple custom script.


class SemanticPart(Enum):
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


def bump(version_file: Path, bump_by: SemanticPart) -> None:
    with version_file.open(encoding="utf-8") as file:
        content = file.read()
    content = bump_line(content, bump_by)
    with version_file.open(encoding="utf-8", mode="w") as file:
        file.write(content)


def bump_line(line: str, bump_by: SemanticPart) -> str:
    semver_str = re.findall(r"(.+)", line)[0]
    major, minor, patch = (int(s) for s in semver_str.split("."))
    major, minor, patch = bump_version(major, minor, patch, bump_by)
    return f"{major}.{minor}.{patch}\n"


def bump_version(
    major: int,
    minor: int,
    patch: int,
    bump_by: SemanticPart,
) -> Tuple[int, int, int]:
    if bump_by == SemanticPart.PATCH:
        patch += 1
    if bump_by == SemanticPart.MINOR:
        patch = 0
        minor += 1
    if bump_by == SemanticPart.MAJOR:
        patch = 0
        minor = 0
        major += 1
    return major, minor, patch
