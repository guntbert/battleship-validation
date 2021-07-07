import kata
import pytest

# This battlefield is not a valid one, I use it to test the detecting functions
battleField =   [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
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

def test_detect_ones():
    assert kata.detect_ones(battleField) == 4


def test_detect_horizontal_twos():
    assert kata.detect_hor_twos(battleField) == 1


def test_detect_vertical_twos():
    assert kata.detect_vert_twos(battleField) == 2


def test_detect_horizontal_threes():
    assert kata.detect_hor_threes(battleField) == 1

def test_detect_vertical_threes():
    assert kata.detect_vert_threes(battleField) == 1

@pytest.mark.parametrize("size, expected_count", [
    (2,1),
    (3,1),
    (4,1)
])
def test_count_horizontal_ships(size, expected_count):
    assert kata.count_hor_ships(battleField, size) == expected_count


# def test_detect_horizontal_fours():
#     assert kata.detect_hor_fours(battleField) == 1

# def test_detect_vertical_fours():
#     assert kata.detect_vert_fours(battleField) == 1

