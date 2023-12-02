from AdventOfCode2023.day_01 import (
    get_line_cal_vals,
    sum_cal_vals,
    get_spelled_num,
    get_line_digits_and_string_nums,
)


PART_I_EX_INPUT = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

def test_get_line_cal_vals():
    line = "pqr3stu8vwx"
    assert get_line_cal_vals(line) == 38


def test_sum_cal_vals():
    assert sum_cal_vals(PART_I_EX_INPUT) == 142


PART_II_EX_INPUT = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

def test_get_spelled_num():
    line = "23eightw"
    assert get_spelled_num(line) == 8

def test_get_line_digits_and_string_nums():
    line = "1eightwothree45"
    assert get_line_digits_and_string_nums(line) == [1,8,2,3,4,5]


# In this example, the calibration values are 
# 29, 83, 13, 24, 42, 14, and 76. 
# Adding these together produces 281.
def test_cal_vals_including_spelled_digits():
    updated_total = sum_cal_vals((get_line_digits_and_string_nums(line) for line in PART_II_EX_INPUT))
    assert updated_total == 281
