import tempfile
from pathlib import Path

import pytest

from tools.bump.core import SemanticPart, bump


@pytest.mark.parametrize("suffix", ["", " ", "\n"])
def test_bumping_version(suffix: str) -> None:
    with tempfile.NamedTemporaryFile() as temporary_file:
        ptf = Path(temporary_file.name)
        with ptf.open(encoding="utf-8", mode="w") as file:
            file.write(f"1.2.3{suffix}")
        bump(ptf, SemanticPart.PATCH)
        with ptf.open(encoding="utf-8") as file:
            assert file.read() == "1.2.4\n"
        bump(ptf, SemanticPart.MINOR)
        with ptf.open(encoding="utf-8") as file:
            assert file.read() == "1.3.0\n"
        bump(ptf, SemanticPart.MAJOR)
        with ptf.open(encoding="utf-8") as file:
            assert file.read() == "2.0.0\n"
