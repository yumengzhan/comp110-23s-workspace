"""EX04 - utils."""
__author__ = "730619940"


def all(numbers: list[int], num1: int) -> bool:
    """Testing if all the integers in the list are the same."""
    length: int = len(numbers)
    i: int = 0
    if len(numbers) == 0:
        return False
    while i <= length - 1:
        if numbers[i] != num1:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Find the maximum integer in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    length: int = len(input)
    i: int = 1
    maxnum: int = input[0]
    while i <= length - 1:
        if input[i] > maxnum:
            maxnum = input[i]
        i += 1 
    return maxnum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Testing if two lists are the same."""
    if len(list1) != len(list2):
        return False
    idx1: int = 0
    while idx1 < len(list2):
        if list1[idx1] != list2[idx1]:
            return False
        idx1 += 1
    return True