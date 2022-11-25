from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture
from pytest_mock import MockFixture

from magic.console.core import main

VALID_ARGV = [
    '/mock/executable',
    '--name',
    'monkey',
    '--author',
    'John Doe',
    '--email',
    'john@example.com',
]


@pytest.fixture(autouse=True)
def _patch_resolve_genvi_root(
    mocker: MockFixture,
    tmp_genvi_path: Path,
) -> None:
    # also effectively initializes the `tmp_genvi_path` for all tests in this module
    target = 'magic.console.config.resolve_genvi_root'
    mocker.patch(target).return_value = tmp_genvi_path


def test_main(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
) -> None:
    mocker.patch('sys.argv', VALID_ARGV)
    assert main() == 0
    std = capsys.readouterr()
    assert 'Project "monkey" has been created!' in std.out
    assert std.err == ''


def test_main_no_arguments(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
) -> None:
    mocker.patch('builtins.input').return_value = ''
    mocker.patch('sys.argv', ['/mock/executable'])
    assert main() == 1
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == 'package name cannot be empty\n'


def test_main_not_interactive(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
) -> None:
    mocker.patch('builtins.input').side_effect = EOFError
    mocker.patch('sys.argv', ['/mock/executable'])
    assert main() == 1
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == 'package name cannot be empty\n'


def test_main_internal_error(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
    tmp_genvi_path: Path,
) -> None:
    (tmp_genvi_path / 'Makefile').unlink()
    mocker.patch('sys.argv', VALID_ARGV)
    assert main() == 1
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == 'package root does not look like `genvi` root\n'
