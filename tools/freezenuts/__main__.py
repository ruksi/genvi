import sys
from pathlib import Path

from tools.freezenuts.core import get_oldest_requirements

if __name__ == '__main__':
    INPUT_FILE = ''
    try:
        INPUT_FILE = sys.argv[1]
    except IndexError:
        sys.stderr.write('missing input file e.g. requirements.in\n')
        sys.exit(1)
    for dependency in get_oldest_requirements(Path(INPUT_FILE)):
        sys.stdout.write(f'{dependency}\n')
