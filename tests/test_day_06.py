from AdventOfCode2023.day_06 import (
    calculate_win_options,
    win_margin
)

TIME = [7, 15, 30]
DISTANCE = [9, 40, 200]

def test_calculate_win_options():
    assert calculate_win_options(7, 9) == 4

def test_win_margin():
    assert win_margin(TIME, DISTANCE) == 288
