import logging
from typing import TYPE_CHECKING

import pytest
from click.testing import CliRunner

from myproject.console.core import cli

if TYPE_CHECKING:
    from typing import List

    from _pytest.capture import CaptureFixture
    from _pytest.logging import LogCaptureFixture
    from pytest_mock import MockFixture


@pytest.mark.parametrize(
    ("args", "log_level"),
    [
        ([], "INFO"),
        (["-v"], "DEBUG"),
        (["-q"], "WARNING"),
        (["-qq"], "ERROR"),
    ],
)
def test_main_log_levels(
    capsys: "CaptureFixture[str]",
    caplog: "LogCaptureFixture",
    args: "List[str]",
    log_level: str,
) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, args)

    assert result.exit_code == 0
    assert result.output == "hello!\n"

    info_records = [r for r in caplog.records if r.levelno == logging.INFO]
    assert len(info_records) == 1
    assert info_records[0].getMessage() == f"log level = {log_level}"

    # didn't write __straight__ to stdout/stderr
    std = capsys.readouterr()
    assert not std.out
    assert not std.err


def test_main_logging_setup_fails(mocker: "MockFixture") -> None:
    error_message = "boom things went wrong"
    error_source = "myproject.console.core.setup_console_logging"
    mocker.patch(error_source).side_effect = Exception(error_message)

    runner = CliRunner()
    result = runner.invoke(cli, [])

    assert result.exit_code == 1
    assert error_message in str(result.exception)
