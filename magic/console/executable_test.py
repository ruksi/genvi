import tempfile
from pathlib import Path

import pytest

from magic.console.executable import main
from magic.tests.fake_directory import fake_directory
from magic.utils.config import Config
from magic.utils.errors import InternalError


def test_main_with_valid_config() -> None:
    with fake_directory() as directory:
        config = Config(
            name='monkey',
            author='John Doe',
            email='john@example.com',
            genvi_root=Path(directory),
        )
        assert main(config=config) == 0


def test_main_with_invalid_config() -> None:
    with fake_directory() as directory:
        config = Config(
            name='',
            author='John Doe',
            email='john@example.com',
            genvi_root=Path(directory),
        )
        assert main(config=config) != 0


def test_main_internal_error() -> None:
    with tempfile.TemporaryDirectory() as directory:
        config = Config(
            name='monkey',
            author='John Doe',
            email='john@example.com',
            genvi_root=Path(directory),
        )
        with pytest.raises(InternalError, match='does not look like'):
            main(config=config)
