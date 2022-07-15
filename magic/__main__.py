import sys
from argparse import ArgumentParser
from pathlib import Path

from magic.console.executable import main
from magic.utils.config import Config

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
