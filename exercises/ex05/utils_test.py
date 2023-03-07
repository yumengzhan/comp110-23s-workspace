"""EX05 - utils_test."""
__author__ = "730619940"

from exercises.ex05.utils import only_evens, sub, concat


def test_() -> None:
    """Test only_evens."""
    assert only_evens([1, 2, 3]) == [2]   


def test_three() -> None:
    """Test only_evens."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_none() -> None:
    """Test only_evens."""
    assert only_evens([]) == []


def test_emp() -> None:
    """Test concat."""
    assert concat([], []) == []


def test_one_elemet() -> None:
    """Test concat."""
    assert concat([1, 2], [1, 2]) == [1, 2, 1, 2]   


def test_three_elements() -> None:
    """Test concat."""
    assert concat([4, 4, 4], [1, 2, 3]) == [4, 4, 4, 1, 2, 3]


def test_empty() -> None:
    """Test sub."""
    assert sub([], 1, 2) == []


def test_elements() -> None:
    """Test sub."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]   


def test_negative() -> None:
    """Test sub."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_lastindex() -> None:
    """Test sub."""
    assert sub([10, 20, 30, 40], 1, 5) == [20, 30, 40]
