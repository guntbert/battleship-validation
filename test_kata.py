import pytest

import kata

# This battlefield is not a valid one, I use it to test the detecting functions
battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]


# test.assert_equals(validate_battlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");

def test_count_ones():
    assert kata.count_ones(battleField) == 4


@pytest.mark.parametrize("size, expected_count", [
    (2, 1),
    (3, 1),
    (4, 1)
])
def test_count_horizontal_ships(size, expected_count):
    assert kata.count_hor_ships(battleField, size) == expected_count


@pytest.mark.parametrize("size, expected_count", [
    (2, 2),
    (3, 1),
    (4, 1)
])


def test_count_vertical_ships(size, expected_count):
    assert kata.count_vert_ships(battleField, size) == expected_count

