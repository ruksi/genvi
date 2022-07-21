import string
from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import List

from magic.utils.errors import InternalError, ValidationError


@dataclass
class Config:
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
        if self.name in {'images', 'magic', 'tests'}:
            raise ValidationError('package name is invalid')

    def _validate_root(self) -> None:
        if not self.genvi_root.is_dir():
            raise InternalError('package root must be an existing directory')
        if not Path(self.genvi_root, 'Makefile').is_file():  # sanity check
            raise InternalError('package root does not look like `genvi` root')


def parse_config(arguments: List[str]) -> Config:
    parser = ArgumentParser()
    parser.add_argument('--name', help='package name')
    parser.add_argument('--author', help='package author name')
    parser.add_argument('--email', help='package author email')
    parguments = parser.parse_args(args=arguments)

    if not parguments.name:
        parguments.name = input('Package name: ')
    if not parguments.author:
        parguments.author = input('Author name: ')
    if not parguments.email:
        parguments.email = input('Author email: ')

    if not parguments.author:
        parguments.author = 'Arthur Author'
    if not parguments.email:
        parguments.email = 'author@example.com'

    config = Config(
        name=parguments.name,
        author=parguments.author,
        email=parguments.email,
        genvi_root=resolve_genvi_root(),
    )
    config.validate()
    return config


def resolve_genvi_root() -> Path:
    return Path(__file__).parent.parent.parent
