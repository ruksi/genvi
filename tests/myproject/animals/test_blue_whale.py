from myproject.animals.blue_whale import BlueWhale


def test_blue_whale() -> None:
    squirty = BlueWhale('Squirty')
    splashy = BlueWhale('Splashy')
    assert squirty != splashy
    assert squirty.vocalize() == splashy.vocalize()
