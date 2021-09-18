from pathlib import Path

import pytest

from magic.tests.fake_directory import fake_directory
from magic.utils.config import Config
from magic.utils.errors import InternalError, ValidationError


def test_config_validation() -> None:
    with fake_directory() as directory:
        Config(name='test', author='', email='', genvi_root=Path(directory)).validate()


@pytest.mark.parametrize('name', ['', 'bad name', 'images', 'magic', 'tests'])
def test_config_invalid_package_name(name: str) -> None:
    with fake_directory() as directory:
        with pytest.raises(ValidationError):
            Config(
                name=name,
                author='',
                email='',
                genvi_root=Path(directory),
            ).validate()


@pytest.mark.parametrize('write_makefile', [True, False])
def test_config_not_directory(write_makefile: bool) -> None:
    with fake_directory(write_makefile=write_makefile) as directory:
        with pytest.raises(InternalError):
            Config(
                name='test',
                author='',
                email='',
                genvi_root=Path(directory, 'Makefile'),
            ).validate()


def test_config_setup_smells_fishy() -> None:
    with fake_directory(write_makefile=False) as directory:
        with pytest.raises(InternalError):
            Config(
                name='test',
                author='',
                email='',
                genvi_root=Path(directory),
            ).validate()
