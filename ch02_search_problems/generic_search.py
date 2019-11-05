from __future__ import annotations
import typing
from heapq import heappush, heappop

T = typing.TypeVar("T")

def linear_search(iterable: typing.Iterable, key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


C = typing.TypeVar("C", bound="Comparable")


class Comparable(typing.Protocol):

    def __eq__(self, other: typing.Any) -> bool:
        pass

    def __lt__(self: C, other: C) -> bool:
        pass

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: typing.Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    pass