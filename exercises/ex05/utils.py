"""EX05 - utils."""
__author__ = "730619940"


def only_evens(numbers: list[int]) -> list[int]:
    """Find even numbers in a list."""
    newlist: list[int] = list()
    for idx in numbers:
        if idx % 2 == 0:
            newlist.append(idx)
    return newlist


def concat(l1: list[int], l2: list[int]) -> list[int]:
    """Combine two lists."""
    return l1 + l2       


def sub(list0: list[int], num1: int, num2: int) -> list[int]:
    """Find the corresponding elements in a list."""
    newlist: list[int] = []
    if len(list0) == 0:
        return []
    if num1 < 0:
        num1 = 0
    if num2 > len(list0):
        num2 = len(list0)
    if num1 >= len(list0) or num2 <= 0:
        return []
    while num1 < num2:
        newlist.append(list0[num1])
        num1 += 1
    return newlist
