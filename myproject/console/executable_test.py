import logging
from typing import List

import pytest
from _pytest.capture import CaptureFixture
from _pytest.logging import LogCaptureFixture
from pytest_mock import MockFixture

from myproject.console.executable import main

VALID_ARGV = ['/mock/myproject.py']


def test_main_success(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
    caplog: LogCaptureFixture,
) -> None:
    mocker.patch('sys.argv', VALID_ARGV)
    assert main() == 0

    # didn't write __straight__ to stdout/stderr
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == ''

    infos = [r.msg for r in caplog.records if r.levelno == logging.INFO]
    assert len(infos) == 1
    assert 'mock command line interface:' in infos[0]


@pytest.mark.parametrize(
    'error_source',
    [
        'myproject.console.executable.run',
        'myproject.console.executable.log.info',
    ],
)
def test_main_failure(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
    caplog: LogCaptureFixture,
    error_source: str,
) -> None:
    mocker.patch('sys.argv', VALID_ARGV)
    msg = 'boom things went wrong'
    mocker.patch(error_source).side_effect = Exception(msg)
    assert main() == 1

    # didn't write __straight__ to stdout/stderr
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == ''

    errors = [r.msg for r in caplog.records if r.levelno == logging.ERROR]
    assert len(errors) == 1
    assert isinstance(errors[0], Exception)
    assert str(errors[0]) == msg


@pytest.mark.parametrize(
    'error_sources',
    [
        # logging setup fails
        ['myproject.console.executable.setup_console_logging'],
        # all logging fails after setup
        [
            'myproject.console.executable.log.debug',
            'myproject.console.executable.log.info',
            'myproject.console.executable.log.warning',
            'myproject.console.executable.log.error',
            'myproject.console.executable.log.exception',
            'myproject.console.executable.log.critical',
        ],
    ],
)
def test_main_log_system_failure(
    mocker: MockFixture,
    capsys: CaptureFixture[str],
    error_sources: List[str],
) -> None:
    mocker.patch('sys.argv', VALID_ARGV)
    error_message = 'boom things went wrong'
    for target in error_sources:
        mocker.patch(target).side_effect = Exception(error_message)
    assert main() == 1

    # writes straight to stderr as logging didn't work
    std = capsys.readouterr()
    assert std.out == ''
    assert std.err == f'{error_message}\n'
