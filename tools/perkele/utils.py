from typing import Callable, List, TypeVar

T = TypeVar('T')


def pop_until(items: List[T], condition: Callable[[T], bool]) -> List[T]:
    popped: List[T] = []
    while items and not condition(items[-1]):
        popped.append(items.pop())
    return popped
