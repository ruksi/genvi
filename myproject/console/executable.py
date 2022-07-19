import logging
import sys

from myproject.console.reporting import setup_console_logging
from myproject.console.settings import Settings, parse_settings

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

ErrorCode = Literal[0, 1]

log = logging.getLogger(__name__)


def main() -> ErrorCode:
    try:
        return main_with_logging()
    except Exception as e:  # pylint: disable=broad-except
        # an exception escaped logging system
        # so write straight to stderr
        sys.stderr.write(f'{e}\n')
        return 1


def main_with_logging() -> ErrorCode:
    settings = parse_settings(sys.argv[1:])
    setup_console_logging(settings.log_level)
    try:
        return run(settings)
    except Exception as e:  # pylint: disable=broad-except
        log.exception(e)
        return 1


def run(settings: Settings) -> ErrorCode:
    log.info('mock command line interface: %s', settings)
    return 0
