import re
import sys
from enum import Enum
from pathlib import Path
from typing import Tuple

# Tools for managing project semantic version numbering.
# `bumpversion` is unmaintained and the alternatives don't look
# very reassuring so use a simple custom script.


class SemanticPart(Enum):
    MAJOR = 'major'
    MINOR = 'minor'
    PATCH = 'patch'


def bump(version_file: Path, bump_by: SemanticPart) -> None:
    with version_file.open(encoding='utf-8') as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        if line.startswith('__version__ ='):
            lines[index] = bump_line(line, bump_by)
    with version_file.open(encoding='utf-8', mode='w') as file:
        file.writelines(lines)


def bump_line(line: str, bump_by: SemanticPart) -> str:
    semver_str = re.findall(r'["\'](.+)["\']', line)[0]
    major, minor, patch = (int(s) for s in semver_str.split('.'))
    major, minor, patch = bump_version(major, minor, patch, bump_by)
    return f"__version__ = '{major}.{minor}.{patch}'\n"


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


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        sys.stderr.write(f'Invalid number of arguments: {args}\n')
        sys.stderr.write('Are you sure you specified major, minor or patch?\n')
        sys.exit(1)
    target = args[0]
    by = args[1]
    try:
        bump(Path(target), SemanticPart(by))
    except Exception as e:  # pylint: disable=broad-except
        sys.stderr.write(f'error: {e}\n')
        sys.exit(2)
