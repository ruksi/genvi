import logging
from typing import List

import pytest
from _pytest.capture import CaptureFixture
from _pytest.logging import LogCaptureFixture
from pytest_mock import MockFixture

from myproject.console.core import main

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

    info_records = [r for r in caplog.records if r.levelno == logging.INFO]
    assert len(info_records) == 1
    assert 'mock command line interface:' in info_records[0].msg


@pytest.mark.parametrize(
    'error_source',
    [
        'myproject.console.core.run',
        'myproject.console.core.log.info',
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

    error_records = [r for r in caplog.records if r.levelno == logging.ERROR]
    assert len(error_records) == 1
    assert error_records[0].msg == 'runtime exception:'
    assert msg in str(error_records[0].exc_text)


@pytest.mark.parametrize(
    'error_sources',
    [
        # logging setup fails
        ['myproject.console.core.setup_console_logging'],
        # all logging fails after setup
        [
            'myproject.console.core.log.debug',
            'myproject.console.core.log.info',
            'myproject.console.core.log.warning',
            'myproject.console.core.log.error',
            'myproject.console.core.log.exception',
            'myproject.console.core.log.critical',
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
