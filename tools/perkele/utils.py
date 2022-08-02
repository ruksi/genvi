from typing import Callable, List, TypeVar

T = TypeVar('T')


def pop_until(items: List[T], condition: Callable[[T], bool]) -> None:
    while items and not condition(items[-1]):
        items.pop()
