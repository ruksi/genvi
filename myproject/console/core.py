import logging
import sys

from typing_extensions import Literal

from myproject.console.reporting import setup_console_logging
from myproject.console.settings import Settings, parse_settings

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
    except Exception:  # pylint: disable=broad-except
        log.exception('runtime exception:')
        return 1


def run(settings: Settings) -> ErrorCode:
    log.info('mock command line interface: %s', settings)
    return 0
