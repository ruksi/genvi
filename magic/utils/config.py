import string
from dataclasses import dataclass
from pathlib import Path

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
