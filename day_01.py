"""
https://adventofcode.com/2023/day/1

DAY 1 Part I:
The given document consist of lines of text.
Find the desired value by combining the first digit 
and the last digit (in that order) to form a single two-digit number.

For example:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the values of these
four lines are 12, 38, 15, and 77. 
Adding these together produces 142.

Consider your entire document. What is the sum of all of the values?
"""

def get_line_cal_vals(line: str) -> int:
    digits = []
    for l in line:
        try:
            digits.append(int(l))
        except ValueError:
            continue
    return digits[0] * 10 + digits[-1]


def sum_cal_vals(lines: list[str]) -> int:
    return sum(get_line_cal_vals(line) for line in lines)

"""Part II
Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. 
For example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.
"""

DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def get_spelled_num(chunk: str) -> int:
    """Given a chunk of a line, determine if there is a spelled out digit and return it
    as an integer"""
    digits = [n for n in DIGITS.keys()]
    for d in digits:
        if d in chunk:
            return DIGITS.get(d, None)


def get_line_digits_and_string_nums(line: str) -> list[int]:
    """Parse a line, char by char. First check if the char is an integer, if so, add to
    a list of numbers. If not, check if the characters (starting from the last identified
    number) contained a spelled out int and add to the running list of numbers. Return a list
    all numbers in the order encountered when reading the line
    """
    nums = []

    # Keep track of the beginning of the chunk of characters in which to check for a spelled out digit
    start_of_chunk = 0

    for i, l in enumerate(line):
        try:
            # Cast the char to an int and add to our list
            nums.append(int(l))
            start_of_chunk = i + 1
        
        except ValueError: # If char is a letter and not a digit
            chunk = line[start_of_chunk: i + 1]
            if (num := get_spelled_num(chunk)) is not None:
                nums.append(num)
                # In case spelled out digits overlap, i.e. 'oneight', move pointer
                # to include the last char of the most recently found digit
                start_of_chunk = i - 1
            continue      
    return nums


if __name__ == '__main__':
    with open('puzzle_input/day_01.txt', 'r') as f:
        lines = f.readlines()
        
        # Part I - Get the sum of the calibrated values 
        part_I_result = sum_cal_vals(lines)
        print('part I result', part_I_result) 
        # Correct answer = 55834

        # Part II - Parse spelled out digits as numbers (don't forget to handle overlapping digits)
        # and then get the sum of values like in Part I
        part_II_result = sum_cal_vals((get_line_digits_and_string_nums(line) for line in lines))
        print('part II result', part_II_result) 
        # Correct answer = 53221
