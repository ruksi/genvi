import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from magic.utils.consts import DEFAULT_AUTHOR, DEFAULT_PACKAGE_NAME


@contextmanager
def fake_directory(*, write_makefile: bool = True) -> Generator[str, None, None]:
    def write_to_file(file_path: Path, file_contents: str) -> None:
        with file_path.open(mode='w') as file:
            file.write(file_contents)

    with tempfile.TemporaryDirectory() as directory:
        if write_makefile:
            write_to_file(
                Path(directory, 'Makefile'),
                f'mock:\n	echo {DEFAULT_PACKAGE_NAME}',
            )

        write_to_file(
            Path(directory, 'LICENSE'),
            f'(c) {DEFAULT_AUTHOR} and others',
        )
        write_to_file(
            Path(directory, 'README.md'),
            f'{DEFAULT_PACKAGE_NAME} README',
        )
        write_to_file(
            Path(directory, 'ABOUT.md'),
            f'{DEFAULT_PACKAGE_NAME} ABOUT',
        )
        write_to_file(
            Path(directory, 'MANIFEST.in'),
            'global-exclude tests/* */tests/* *_test.py\n'
            f'include {DEFAULT_PACKAGE_NAME}/py.typed',
        )
        write_to_file(
            Path(directory, 'pyproject.toml'),
            "[tool.isort]\n profile = 'black'\n",
        )
        write_to_file(
            Path(directory, 'setup.cfg'),
            f'[metadata]\nname = {DEFAULT_PACKAGE_NAME}\n',
        )

        code_dir = Path(directory, DEFAULT_PACKAGE_NAME)
        code_dir.mkdir()
        write_to_file(
            Path(code_dir, '__init__.py'),
            f'# {DEFAULT_PACKAGE_NAME}',
        )

        tests_dir = Path(directory, 'tests')
        tests_dir.mkdir()
        write_to_file(
            Path(tests_dir, 'test_tests.py'),
            f'# {DEFAULT_PACKAGE_NAME} tests',
        )

        workflows_dir = Path(directory, '.github/workflows')
        workflows_dir.mkdir(parents=True)
        write_to_file(
            Path(workflows_dir, 'ci.yml'),
            f'# {DEFAULT_PACKAGE_NAME} automation',
        )

        magic_dir = Path(directory, 'magic')
        magic_dir.mkdir(parents=True)

        magic_dir = Path(directory, 'images')
        magic_dir.mkdir(parents=True)

        yield directory
