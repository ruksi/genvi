import sys
import tempfile
from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture
from pytest_mock import MockFixture

from magic.console.executable import main, resolve_genvi_root
from magic.tests.fake_directory import fake_directory

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

VALID_ARGV = [
    '/mock/executable',
    '--name',
    'monkey',
    '--author',
    'John Doe',
    '--email',
    'john@example.com',
]


class PatchGenviRoot(Protocol):
    def __call__(self, directory: str) -> None:
        ...


@pytest.fixture(name='patch_genvi_root')
def genvi_root_patcher(mocker: MockFixture) -> PatchGenviRoot:
    def patch_genvi_root(directory: str) -> None:
        target = 'magic.console.executable.resolve_genvi_root'
        mocker.patch(target).return_value = Path(directory)

    return patch_genvi_root


def test_main(
    mocker: MockFixture,
    patch_genvi_root: PatchGenviRoot,
    capsys: CaptureFixture[str],
) -> None:
    with fake_directory() as directory:
        patch_genvi_root(directory)
        mocker.patch('sys.argv', VALID_ARGV)
        assert main() == 0
        standard = capsys.readouterr()
        assert '' == standard.out
        assert '' == standard.err


def test_main_no_arguments(
    mocker: MockFixture,
    patch_genvi_root: PatchGenviRoot,
    capsys: CaptureFixture[str],
) -> None:
    mocker.patch('builtins.input').return_value = ''
    with fake_directory() as directory:
        patch_genvi_root(directory)
        mocker.patch('sys.argv', ['/mock/executable'])
        assert main() == 1
        standard = capsys.readouterr()
        assert '' == standard.out
        assert 'package name cannot be empty\n' == standard.err


def test_main_internal_error(
    mocker: MockFixture,
    patch_genvi_root: PatchGenviRoot,
    capsys: CaptureFixture[str],
) -> None:
    with tempfile.TemporaryDirectory() as directory:
        patch_genvi_root(directory)
        mocker.patch('sys.argv', VALID_ARGV)
        assert main() == 1
        standard = capsys.readouterr()
        assert '' == standard.out
        assert 'package root does not look like `genvi` root\n' == standard.err


def test_resolve_genvi_root() -> None:
    assert resolve_genvi_root()
