import logging
import sys
from typing import List

from myproject.console.reporting import setup_console_logging

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
    setup_console_logging()
    try:
        return run(sys.argv)
    except Exception as e:  # pylint: disable=broad-except
        log.exception(e)
        return 1


def run(arguments: List[str]) -> ErrorCode:
    log.info('mock command line interface: %s', arguments)
    return 0
