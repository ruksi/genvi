from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from magic.console.config import Config
from magic.utils.files import (
    generate_readme,
    rename_package,
    strip_lines_between_markers,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize(
    ("author", "email"),
    [("", ""), ("Barry Bananas", "barry@example.com")],
)
def test_renaming_package(tmp_genvi_path: Path, author: str, email: str) -> None:
    config = Config(
        name="monkey",
        author=author,
        email=email,
        genvi_root=tmp_genvi_path,
    )
    rename_package(config)


def test_generating_readme(tmp_genvi_path: Path) -> None:
    config = Config(
        name="monkey",
        author="",
        email="",
        genvi_root=tmp_genvi_path,
    )
    readme_contents = generate_readme(config)
    assert "# `monkey`" in readme_contents
    assert "$$name" not in readme_contents


def test_stripping_files(tmp_path: Path) -> None:
    test_file = tmp_path / "my_file"
    test_file.write_text(
        "# HEADING\n"
        "\n"
        "# --> Here we have something to snip snip\n"
        "# <-- end of snip snip\n"
        "# AFTER\n",
    )
    strip_lines_between_markers(
        target=test_file,
        start="# -->",
        end="# <--",
    )
    assert test_file.read_text() == "# HEADING\n\n# AFTER\n"
