import logging
import os
from typing import TYPE_CHECKING

import click

from myproject.console.reporting import setup_console_logging

if TYPE_CHECKING:
    from typing import Optional

log = logging.getLogger(__name__)


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "--verbose",
    "-v",
    "log_level",
    flag_value=logging.getLevelName(logging.DEBUG),
    help="Turn on verbose mode, also showing debug information.",
)
@click.option(
    "--quiet",
    "-q",
    "log_level",
    flag_value=logging.getLevelName(logging.WARNING),
    help="Turn on quiet mode, only showing warnings and up.",
)
@click.option(
    "--quiet-quirks",
    "-qq",
    "log_level",
    flag_value=logging.getLevelName(logging.ERROR),
    help="Turn on quiet quirks mode, only showing errors and up.",
)
def cli(
    log_level: "Optional[str]",
) -> None:
    """
    Show debug information.

    This docstring will show up in the command line help.
    """
    if not log_level:
        default_log_level = logging.getLevelName(logging.INFO)
        log_level = os.environ.get("LOGLEVEL", default_log_level).upper()

    setup_console_logging(log_level)
    log.info("log level = %s", log_level)
    click.echo("hello!")
