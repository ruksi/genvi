"""
Tools for resolving the oldest valid dependency versions.

Usage:

.. code:: bash

    python -m tools.freezenuts requirements.in > requirements.out

"""

import subprocess
import sys
from typing import TYPE_CHECKING

from packaging.requirements import Requirement
from packaging.version import Version

if TYPE_CHECKING:
    from pathlib import Path
    from typing import List


def package_versions(project_name: str) -> "List[Version]":
    """Get package version history from PyPI using `pip`."""
    # possibly switch to `distlib`, raw requests or something else later
    # https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
    # should we consider using `--platform` or `--python-version`?
    cmd = [sys.executable, "-m", "pip", "index", "versions", project_name]
    output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode()  # noqa: S603
    lines = output.split("\n")
    versions_line, *_ = filter(
        lambda line: line.startswith("Available versions: "),
        lines,
    )
    _, _, *version_texts = versions_line.split(" ")
    version_texts = [vt.rstrip(",") for vt in version_texts]
    return sorted(Version(vt) for vt in version_texts)  # oldest -> newest


def get_oldest_matching_requirement(requirement: Requirement) -> Requirement:
    # not perfect but should work well enough
    extras = ""
    if requirement.extras:
        extras_str = ",".join(requirement.extras)
        extras = f"[{extras_str}]"

    candidates = all_candidates = package_versions(requirement.name)
    if not requirement.specifier:
        return Requirement(f"{requirement.name}{extras}=={candidates[0]}")

    candidates = [c for c in candidates if c in requirement.specifier]
    if not candidates:
        raise PackageNotFoundError(requirement, all_candidates)

    return Requirement(f"{requirement.name}{extras}=={candidates[0]}")


def get_oldest_requirements(requirements_file: "Path") -> "List[Requirement]":
    with requirements_file.open(encoding="utf-8") as file:
        lines = file.readlines()
    lines = [line.partition("#")[0].rstrip(" \n") for line in lines]
    requirements_in = [Requirement(line) for line in lines if line]
    requirements_out = [get_oldest_matching_requirement(req) for req in requirements_in]
    return sorted(requirements_out, key=lambda r: r.name)


class PackageNotFoundError(RuntimeError):
    def __init__(self, requirement: Requirement, candidates: "List[Version]") -> None:
        as_strings = ", ".join([str(c) for c in candidates])
        super().__init__(f"No valid candidate found for {requirement} in: {as_strings}")
