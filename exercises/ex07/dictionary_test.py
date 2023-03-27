"""EX07 - dictionary functions."""
__author__ = "730619940"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_three() -> None:
    """Test invert."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}   


def test_one() -> None:
    """Test invert."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_none() -> None:
    """Test invert."""
    assert invert({"kris": "jordan", "michael": "jorda"}) == {"jordan": "kris", "jorda": "michael"}


def test_one_color() -> None:
    """Test favorite_color."""
    assert favorite_color({"Marc": "yellow"}) == 'yellow'


def test_three_color() -> None:
    """Test favorite_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_four_color() -> None:
    """Test favorite_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "A": "yellow"}) == 'yellow'


def test_two_colors() -> None:
    """Test count."""
    assert count(["yellow", "blue"]) == {'yellow': 1, 'blue': 1}


def test_three_colors() -> None:
    """Test count."""
    assert count(["yellow", "blue", "yellow"]) == {'yellow': 2, 'blue': 1}
 

def test_empty_list() -> None:
    """Test count."""
    assert count([]) == {}
