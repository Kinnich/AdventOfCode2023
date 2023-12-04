import pytest
from AdventOfCode2023.day_04 import (
    get_matching_nums,
    calculate_points,
    sum_points,
    process_cards,
    parse_input,
)

EX_LINES = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n',
]

EX_INPUT = [
    [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]],
    [[13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]],
    [[1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]],
    [[41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]],
    [[87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]],
    [[31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]],
]

def test_get_matching_nums():
    win_list = [41, 48, 83, 86, 17]
    my_list = [83, 86, 6, 31, 17, 9, 48, 53]
    assert get_matching_nums(win_list, my_list) == 4

@pytest.mark.parametrize(
    "matches, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (5, 16),
    ]
)
def test_calculate_points(matches, expected):
    assert calculate_points(matches) == expected

def test_sum_points():
    assert sum_points(EX_INPUT) == 13

def test_parse_input():
    assert parse_input(EX_LINES) == EX_INPUT

def test_process_cards():
    assert process_cards(EX_INPUT) == 30