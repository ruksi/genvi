import logging
import os
from argparse import ArgumentParser, Namespace
from typing import List


class Settings(Namespace):
    log_level: str


def parse_settings(arguments: List[str]) -> Settings:
    parser = ArgumentParser(prog='myproject')

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-v',
        '--verbose',
        dest='log_level',
        action='store_const',
        const=logging.getLevelName(logging.DEBUG),
        help='turn on verbose mode, also showing debug information',
        default=os.environ.get('LOGLEVEL', logging.getLevelName(logging.INFO)).upper(),
    )
    group.add_argument(
        '-q',
        '--quiet',
        dest='log_level',
        action='store_const',
        help='turn on quiet mode, only showing warnings and up',
        const=logging.getLevelName(logging.WARNING),
    )
    group.add_argument(
        '-qq',
        '--quiet-quirks',
        dest='log_level',
        action='store_const',
        help='turn on quiet quirks mode, only showing errors and up',
        const=logging.getLevelName(logging.ERROR),
    )

    settings: Settings = parser.parse_args(
        args=arguments,
        namespace=Settings(),
    )
    return settings
