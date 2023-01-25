from myproject.animals.common_viper import CommonViper


def test_viper() -> None:
    noodle = CommonViper("Danger Noodle")
    stringy = CommonViper("Stringy Cheese")
    assert noodle != stringy
    assert noodle.vocalize() == stringy.vocalize()
