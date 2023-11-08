from __future__ import annotations

import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from packaging.requirements import Requirement
from packaging.version import Version
from typing_extensions import Protocol

from tools.freezenuts.core import (
    get_oldest_matching_requirement,
    get_oldest_requirements,
    package_versions,
)

if TYPE_CHECKING:
    from pytest_mock import MockFixture

REQUIREMENTS_CONTENT = """
# comments
melchior
# are
caspar[toml]>=2.0.0
balthazar>=1.24,<1.28  # not
# included
"""


class CheckOutputMock(Protocol):
    def __call__(self, output: str | None) -> None:
        ...


@pytest.fixture(name="check_output_mock")
def check_output_mocker(mocker: MockFixture) -> CheckOutputMock:
    def setup_check_output_mocker(output: str | None = None) -> None:
        if output is not None:
            mocker.patch("subprocess.check_output").return_value = output.encode()

    return setup_check_output_mocker


def test_file_parsing(check_output_mock: CheckOutputMock) -> None:
    check_output_mock(
        output=(
            "zion (0.3.0)\n"
            "Available versions: 2.0.0, 1.24.0, 0.3.0, 0.2.1, 0.1.3, 0.0.1\n"
        ),
    )
    with tempfile.NamedTemporaryFile() as temporary_file:
        ptf = Path(temporary_file.name)
        with ptf.open(encoding="utf-8", mode="w") as file:
            file.write(REQUIREMENTS_CONTENT)
        requirements = [str(r) for r in get_oldest_requirements(ptf)]
        expected = [
            str(Requirement(r))
            for r in [
                "balthazar==1.24.0",
                "caspar[toml]==2.0.0",
                "melchior==0.0.1",
            ]
        ]
        assert requirements == expected


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ("abraham~=2.27.1", "abraham==2.27.1"),
        ("andrew", "andrew==0.2.0"),
        ("bartholomew>=3.0", "bartholomew==3.0.0"),
        ("caleb~=1.0,!=1.0.0", "caleb==1.1.0"),
        ("james>=2.27.0,<2.28", "james==2.27.0"),
        ("john>2", "john==2.27.0"),
        ("judas==2.27.1", "judas==2.27.1"),
        ("lazarus~=1.0", "lazarus==1.0.0"),
        ("matthew<3", "matthew==0.2.0"),
        ("philip>1.9.9,<2.28", "philip==2.0.0"),
        ("simon>0,<5.7", "simon==0.2.0"),
        ("thaddeus<=2, >=1.1.0", "thaddeus==1.1.0"),
        ("thomas<3,>=2", "thomas==2.0.0"),
    ],
)
def test_requirement_deep_freezing(
    line: str,
    expected: str,
    check_output_mock: CheckOutputMock,
) -> None:
    check_output_mock(
        output=(
            "zion (0.1.0)\n"
            "Available versions: 3.0.1, 3.0.0, 2.28.0, 2.27.1, 2.27.0, "
            "2.0.0, 1.2.0, 1.1.0, 1.0.0, 0.2.0"
        ),
    )
    requirement = get_oldest_matching_requirement(Requirement(line))
    assert str(requirement) == str(Requirement(expected))


@pytest.mark.parametrize(
    ("output", "expected"),
    [
        (
            "zion (0.1.0)\nAvailable versions: 0.1.0\n",
            ["0.1.0"],
        ),
        (
            "zion (0.3.0)\nAvailable versions: 0.3.0, 0.2.1, 0.1.3, 0.0.1\n",
            [
                "0.0.1",
                "0.1.3",
                "0.2.1",
                "0.3.0",
            ],
        ),
        (
            (
                "zion (0.1.0)\n"
                "Available versions: 2.28.0, 2.27.1, 2.27.0\n"
                "  INSTALLED: 2.27.1\n"
            ),
            [
                "2.27.0",
                "2.27.1",
                "2.28.0",
            ],
        ),
    ],
)
def test_querying_package_versions(
    output: str,
    expected: list[str],
    check_output_mock: CheckOutputMock,
) -> None:
    check_output_mock(output)
    assert package_versions("zion") == [Version(e) for e in expected]


def test_stupid_specification(check_output_mock: CheckOutputMock) -> None:
    check_output_mock("zion (0.1.0)\nAvailable versions: 3.0.0, 2.0.0, 1.0.0")
    with pytest.raises(RuntimeError, match="No valid candidate found for mox<=1,>2"):
        get_oldest_matching_requirement(Requirement("mox<=1,>2"))


def test_impossible_specification(check_output_mock: CheckOutputMock) -> None:
    check_output_mock("zion (0.1.0)\nAvailable versions: 3.0.0, 2.0.0, 1.0.0")
    with pytest.raises(RuntimeError, match="No valid candidate found for mox>3"):
        get_oldest_matching_requirement(Requirement("mox>3"))
