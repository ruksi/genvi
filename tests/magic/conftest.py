from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from magic.utils.consts import DEFAULT_AUTHOR, DEFAULT_PACKAGE_NAME

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture()
def tmp_genvi_path(tmp_path: Path) -> Path:
    # Create a mini version of what `genvi` directory looks like.

    (tmp_path / "Makefile").write_text(
        f"mock:\n	echo {DEFAULT_PACKAGE_NAME}",
    )

    (tmp_path / "LICENSE").write_text(
        f"(c) {DEFAULT_AUTHOR} and others",
    )
    (tmp_path / "README.md").write_text(
        f"{DEFAULT_PACKAGE_NAME} README",
    )
    (tmp_path / "ABOUT.md").write_text(
        f"{DEFAULT_PACKAGE_NAME} ABOUT",
    )
    (tmp_path / "MANIFEST.in").write_text(
        (
            "global-exclude tests/* */tests/* *_test.py\n"
            f"include {DEFAULT_PACKAGE_NAME}/py.typed"
        ),
    )
    (tmp_path / "pyproject.toml").write_text(
        "[tool.isort]\n profile = 'black'\n",
    )

    code_dir = tmp_path / DEFAULT_PACKAGE_NAME
    code_dir.mkdir()
    (code_dir / "__init__.py").write_text(
        f"# {DEFAULT_PACKAGE_NAME}",
    )

    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()
    (tests_dir / "test_tests.py").write_text(
        f"# {DEFAULT_PACKAGE_NAME} tests",
    )

    tests_magic_dir = tests_dir / "magic"
    tests_magic_dir.mkdir()
    (tests_magic_dir / "test_magic.py").write_text(
        "# magic tests",
    )

    workflows_dir = tmp_path / ".github/workflows"
    workflows_dir.mkdir(parents=True)
    (workflows_dir / "ci.yml").write_text(
        f"# {DEFAULT_PACKAGE_NAME} automation",
    )

    (tmp_path / "magic").mkdir()

    return tmp_path
