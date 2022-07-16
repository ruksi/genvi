import sys
from typing import Optional, TextIO

ErrorCode = int


def main(text_io: Optional[TextIO] = None) -> ErrorCode:
    if not text_io:
        text_io = sys.stdout
    text_io.write(f'mock command line interface: {sys.argv}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
