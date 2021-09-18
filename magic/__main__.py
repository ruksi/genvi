import shutil
import sys
from argparse import ArgumentParser
from pathlib import Path

from magic.utils.config import Config
from magic.utils.errors import ValidationError
from magic.utils.files import (
    generate_readme,
    rename_package,
    strip_lines_between_markers,
)

ErrorCode = int


def main(config: Config) -> ErrorCode:
    try:
        config.validate()
    except ValidationError as exception:
        print('error:', exception)  # noqa: T201
        return 1

    rename_package(config)
    strip_lines_between_markers(
        target=Path(config.genvi_root, 'Makefile'),
        start='# -->',
        end='# <--',
    )
    strip_lines_between_markers(
        target=Path(config.genvi_root, '.github/workflows/ci.yml'),
        start='# -->',
        end='# <--',
    )

    readme = Path(config.genvi_root, 'README.md')
    readme.unlink()
    with readme.open(encoding='utf-8', mode='w') as file:
        file.write(generate_readme(config))

    # bibbidi-bobbidi-poof!
    shutil.rmtree(Path(config.genvi_root, 'magic'))
    shutil.rmtree(Path(config.genvi_root, 'images'))
    Path(config.genvi_root, 'ABOUT.md').unlink()
    return 0


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--name', help='package name')
    parser.add_argument('--author', help='package author name')
    parser.add_argument('--email', help='package author email')
    arguments = parser.parse_args()
    if not arguments.name:
        arguments.name = input('Package name: ')
    if not arguments.author:
        arguments.author = input('Author name: ')
    if not arguments.email:
        arguments.email = input('Author email: ')
    if not arguments.author:
        arguments.author = 'Arthur Author'
    if not arguments.email:
        arguments.email = 'author@example.com'
    sys.exit(
        main(
            Config(
                name=arguments.name,
                author=arguments.author,
                email=arguments.email,
                genvi_root=Path(__file__).parent.parent,
            ),
        ),
    )
