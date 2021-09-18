import sys
from typing import Optional, TextIO

ErrorCode = int


def main(text_io: Optional[TextIO] = None) -> ErrorCode:
    if not text_io:
        text_io = sys.stdout
    print(f'mock command line interface: {sys.argv}', file=text_io)  # noqa: T201
    return 0


if __name__ == '__main__':
    sys.exit(main())
