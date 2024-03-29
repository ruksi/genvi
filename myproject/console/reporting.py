from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from typing import Mapping


class ColorFormatter(logging.Formatter):  # pragma: no cover
    _grey = "\x1b[38;20m"
    _yellow = "\x1b[33;20m"
    _red = "\x1b[31;20m"
    _bold_red = "\x1b[31;1m"
    _reset = "\x1b[0m"
    _msg_format = "%(message)s"
    _formats: ClassVar[Mapping[int, str]] = {
        logging.CRITICAL: _bold_red + _msg_format + _reset,
        logging.ERROR: _red + _msg_format + _reset,
        logging.WARNING: _yellow + _msg_format + _reset,
        logging.INFO: _grey + _msg_format + _reset,
        logging.DEBUG: _grey + _msg_format + _reset,
        logging.NOTSET: _grey + _msg_format + _reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_format = self._formats.get(record.levelno)
        formatter = logging.Formatter(log_format)
        result = formatter.format(record)
        if record.exc_text:
            # remove newlines from exception stack traces
            # as it's a good `syslog` practice that each event
            # takes exactly one row
            return result.replace("\n", " ")
        return result


def setup_console_logging(log_level: str) -> None:  # pragma: no cover
    out_handler = logging.StreamHandler(sys.stdout)
    out_handler.addFilter(lambda record: record.levelno <= logging.INFO)
    out_handler.setFormatter(ColorFormatter())

    err_handler = logging.StreamHandler(sys.stderr)
    err_handler.addFilter(lambda record: record.levelno > logging.INFO)
    err_handler.setFormatter(ColorFormatter())

    logging.basicConfig(
        level=log_level,
        handlers=[out_handler, err_handler],
    )
