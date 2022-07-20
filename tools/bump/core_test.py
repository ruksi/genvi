import tempfile
from pathlib import Path

import pytest

from tools.bump.core import SemanticPart, bump


@pytest.mark.parametrize('quote', ["'", '"'])
def test_bumping_version(quote: str) -> None:
    with tempfile.NamedTemporaryFile() as temporary_file:
        ptf = Path(temporary_file.name)
        with ptf.open(encoding='utf-8', mode='w') as file:
            file.write(f'__version__ = {quote}1.2.3{quote}\n# untouched\n')
        bump(ptf, SemanticPart.PATCH)
        with ptf.open(encoding='utf-8') as file:
            assert file.read() == "__version__ = '1.2.4'\n# untouched\n"
        bump(ptf, SemanticPart.MINOR)
        with ptf.open(encoding='utf-8') as file:
            assert file.read() == "__version__ = '1.3.0'\n# untouched\n"
        bump(ptf, SemanticPart.MAJOR)
        with ptf.open(encoding='utf-8') as file:
            assert file.read() == "__version__ = '2.0.0'\n# untouched\n"
