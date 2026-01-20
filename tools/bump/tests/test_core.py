from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from tools.bump.core import SemanticPart, bump


@pytest.mark.parametrize("suffix", ["", " ", "\n"])
def test_bumping_version(suffix: str) -> None:
    with tempfile.NamedTemporaryFile() as temporary_file:
        ptf = Path(temporary_file.name)
        ptf.write_text(f"1.2.3{suffix}", encoding="utf-8")

        bump(ptf, SemanticPart.PATCH)
        assert ptf.read_text(encoding="utf-8") == "1.2.4\n"

        bump(ptf, SemanticPart.MINOR)
        assert ptf.read_text(encoding="utf-8") == "1.3.0\n"

        bump(ptf, SemanticPart.MAJOR)
        assert ptf.read_text(encoding="utf-8") == "2.0.0\n"
