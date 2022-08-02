from typing import List

from tools.perkele.utils import pop_until


def test_noop() -> None:
    items = ['', 'one', 'two', '', 'three']
    pop_until(items, lambda item: bool(item != ''))
    assert items == ['', 'one', 'two', '', 'three']


def test_initially_empty() -> None:
    items: List[str] = []
    pop_until(items, lambda item: bool(item != ''))
    assert not items


def test_popped_empty() -> None:
    items: List[str] = ['', '', '']
    pop_until(items, lambda item: bool(item != ''))
    assert not items
