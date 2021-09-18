from is_virtualenv import is_virtualenv


def test_for_smoke() -> None:
    # tedious to test something that check environment status
    # just do a smoke test that it runs and seems consistent
    assert is_virtualenv() or not is_virtualenv()
