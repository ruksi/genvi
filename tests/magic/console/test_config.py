from pathlib import Path

import pytest

from magic.console.config import Config, resolve_genvi_root
from magic.utils.errors import InternalError, ValidationError


def test_config_validation(tmp_genvi_path: Path) -> None:
    Config(name="test", author="", email="", genvi_root=tmp_genvi_path).validate()


@pytest.mark.parametrize("name", ["", "bad name", "magic", "tests"])
def test_config_invalid_package_name(name: str, tmp_genvi_path: Path) -> None:
    with pytest.raises(ValidationError):
        Config(name=name, author="", email="", genvi_root=tmp_genvi_path).validate()


def test_config_doesnt_exist(tmp_genvi_path: Path) -> None:
    root = Path(tmp_genvi_path, "i-do-not-exist")
    with pytest.raises(InternalError):
        Config(name="test", author="", email="", genvi_root=root).validate()


def test_config_not_directory(tmp_genvi_path: Path) -> None:
    root = Path(tmp_genvi_path, "Makefile")
    with pytest.raises(InternalError):
        Config(name="test", author="", email="", genvi_root=root).validate()


def test_config_setup_smells_fishy(tmp_path: Path) -> None:
    with pytest.raises(InternalError):
        Config(name="test", author="", email="", genvi_root=tmp_path).validate()


def test_resolve_genvi_root() -> None:
    assert resolve_genvi_root().name == "genvi"
