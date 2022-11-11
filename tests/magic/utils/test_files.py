from pathlib import Path

import pytest

from magic.console.config import Config
from magic.utils.files import (
    generate_readme,
    rename_package,
    strip_lines_between_markers,
)
from tests.magic.fake_directory import fake_directory


@pytest.mark.parametrize(
    ('author', 'email'),
    [('', ''), ('Barry Bananas', 'barry@example.com')],
)
def test_renaming_package(author: str, email: str) -> None:
    with fake_directory() as directory:
        config = Config(
            name='monkey',
            author=author,
            email=email,
            genvi_root=Path(directory),
        )
        rename_package(config)


def test_generating_readme() -> None:
    with fake_directory() as directory:
        config = Config(name='monkey', author='', email='', genvi_root=Path(directory))
        readme_contents = generate_readme(config)
    assert '# `monkey`' in readme_contents
    assert '$name' not in readme_contents


def test_stripping_files() -> None:
    with fake_directory() as directory:
        test_file = Path(directory, 'my_file')
        with test_file.open(encoding='utf-8', mode='w') as file:
            file.writelines(
                [
                    '# HEADING\n',
                    '\n',
                    '# --> Here we have something to snip snip\n',
                    '# <-- end of snip snip\n',
                    '# AFTER\n',
                ],
            )
        strip_lines_between_markers(
            target=test_file,
            start='# -->',
            end='# <--',
        )
        with test_file.open(encoding='utf-8') as file:
            assert file.readlines() == ['# HEADING\n', '\n', '# AFTER\n']
