from myproject.animals.human import Human


def test_human() -> None:
    bob = Human('Bob')
    alice = Human('Alice')
    assert bob != alice
    assert bob.vocalize() == alice.vocalize()
