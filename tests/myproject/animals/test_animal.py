import pytest

from myproject.animals.animal import Animal


def test_animal() -> None:
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        Animal("Xenomurphy")  # type: ignore[abstract]
