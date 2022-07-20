import sys
from pathlib import Path

from tools.bump.core import SemanticPart, bump

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        sys.stderr.write(f'Invalid number of arguments: {args}\n')
        sys.stderr.write('Are you sure you specified major, minor or patch?\n')
        sys.exit(1)
    target = args[0]
    by = args[1]
    try:
        bump(Path(target), SemanticPart(by))
    except Exception as e:  # pylint: disable=broad-except
        sys.stderr.write(f'error: {e}\n')
        sys.exit(2)
