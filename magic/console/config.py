import string
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import TYPE_CHECKING

from magic.utils.errors import (
    BadProjectRootError,
    EmptyError,
    NoProjectRootError,
    NotAllowedError,
    NotLowAsciiError,
)

if TYPE_CHECKING:
    from typing import List


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
            raise EmptyError(thing="package name")
        if any(c not in string.ascii_lowercase for c in self.name):
            raise NotLowAsciiError(thing="package name", value=self.name)
        if self.name in {"magic", "tests", "tools", "dist", "build"}:
            raise NotAllowedError(thing="package name", value=self.name)

    def _validate_root(self) -> None:
        # do a few sanity checks...
        if not self.genvi_root.is_dir():
            raise NoProjectRootError
        if not Path(self.genvi_root, "Makefile").is_file():
            raise BadProjectRootError


def parse_config(arguments: "List[str]") -> Config:
    parser = ArgumentParser()
    parser.add_argument("--name", help="package name")
    parser.add_argument("--author", help="package author name")
    parser.add_argument("--email", help="package author email")
    config = parser.parse_args(
        args=arguments,
        namespace=Config(genvi_root=resolve_genvi_root()),
    )

    if not config.name:
        config.name = safe_input("Package name: ")
    if not config.author:
        config.author = safe_input("Author name: ")
    if not config.email:
        config.email = safe_input("Author email: ")

    if not config.author:
        config.author = "Arthur Author"
    if not config.email:
        config.email = "author@example.com"

    config.validate()
    return config


def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        return ""


def resolve_genvi_root() -> Path:
    return Path(__file__).parent.parent.parent
