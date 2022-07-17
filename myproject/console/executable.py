import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

ErrorCode = Literal[0, 1]


def main() -> ErrorCode:
    try:
        return run(sys.argv)
    except Exception as e:  # pylint: disable=broad-except
        sys.stderr.write(f'{e}\n')
        return 1


def run(arguments: List[str]) -> ErrorCode:
    sys.stdout.write(f'mock command line interface: {arguments}\n')
    return 0
