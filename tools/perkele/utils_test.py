from typing import List

from tools.perkele.utils import pop_until


def test_noop() -> None:
    items = ['', 'one', 'two', '', 'three']
    popped = pop_until(items, lambda item: bool(item != ''))
    assert items == ['', 'one', 'two', '', 'three']
    assert not popped


def test_initially_empty() -> None:
    items: List[str] = []
    popped = pop_until(items, lambda item: bool(item != ''))
    assert not items
    assert not popped


def test_popped_empty() -> None:
    items: List[str] = ['', '', '']
    popped = pop_until(items, lambda item: bool(item != ''))
    assert not items
    assert popped == ['', '', '']
