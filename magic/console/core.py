import shutil
import sys
from pathlib import Path
from typing import List

from magic.console.config import parse_config
from magic.utils.files import (
    generate_readme,
    rename_package,
    strip_lines_between_markers,
)

ErrorCode = int


def main() -> ErrorCode:
    try:
        return run(sys.argv)
    except Exception as e:  # pylint: disable=broad-except
        sys.stderr.write(f'{e}\n')
        return 1


def run(arguments: List[str]) -> ErrorCode:
    config = parse_config(arguments[1:])

    rename_package(config)
    strip_lines_between_markers(
        target=Path(config.genvi_root, 'Makefile'),
        start='# -->',
        end='# <--',
    )
    strip_lines_between_markers(
        target=Path(config.genvi_root, '.github/workflows/ci.yml'),
        start='  # -->',
        end='  # <--',
    )

    readme = Path(config.genvi_root, 'README.md')
    readme.unlink()
    with readme.open(encoding='utf-8', mode='w') as file:
        file.write(generate_readme(config))

    # bibbidi-bobbidi-poof!
    shutil.rmtree(Path(config.genvi_root, 'magic'))
    shutil.rmtree(Path(config.genvi_root, 'images'))
    Path(config.genvi_root, 'ABOUT.md').unlink()

    write_out(
        [
            '',
            f'Project "{config.name}" has been created!',
            '',
            'Suggestions what to do next:',
            f'  * run `cd {config.genvi_root}`',
            '  * run `rm -rf .git/` to remove any relation to "genvi"',
            '  * run `git init` to create a new local repository',
            '  * run `git add --all` to stage all content',
            '  * run `git commit --message="Initial commit"` to save all changes',
            '  * continue development by reading the new "README.md"',
            '',
        ],
    )

    return 0


def write_out(messages: List[str]) -> None:
    for message in messages:
        sys.stdout.write(f'{message}\n')
