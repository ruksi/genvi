import string
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import List

from magic.utils.errors import InternalError, ValidationError


class Config(Namespace):
    name: str
    author: str
    email: str
    genvi_root: Path

    def validate(self) -> None:
        self._validate_name()
        self._validate_root()

    def _validate_name(self) -> None:
        if not self.name:
            raise ValidationError('package name cannot be empty')
        if any(c not in string.ascii_lowercase for c in self.name):
            raise ValidationError(
                'package name must consist of lowercase ASCII'
                f' ({string.ascii_lowercase})',
            )
        if self.name in {'images', 'magic', 'tests', 'tools', 'dist', 'build'}:
            raise ValidationError('package name is invalid')

    def _validate_root(self) -> None:
        # do a few sanity checks...
        if not self.genvi_root.is_dir():
            raise InternalError('package root must be an existing directory')
        if not Path(self.genvi_root, 'Makefile').is_file():
            raise InternalError('package root does not look like `genvi` root')


def parse_config(arguments: List[str]) -> Config:
    parser = ArgumentParser()
    parser.add_argument('--name', help='package name')
    parser.add_argument('--author', help='package author name')
    parser.add_argument('--email', help='package author email')
    config = parser.parse_args(
        args=arguments,
        namespace=Config(genvi_root=resolve_genvi_root()),
    )

    if not config.name:
        config.name = input('Package name: ')
    if not config.author:
        config.author = input('Author name: ')
    if not config.email:
        config.email = input('Author email: ')

    if not config.author:
        config.author = 'Arthur Author'
    if not config.email:
        config.email = 'author@example.com'

    config.validate()
    return config


def resolve_genvi_root() -> Path:
    return Path(__file__).parent.parent.parent
