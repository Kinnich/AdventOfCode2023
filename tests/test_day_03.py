from AdventOfCode2023.day_03 import (
    Part,
    Symbol,
    get_part_positions,
    get_symbol_positions,
    find_adjacent,
    sum_parts,
)

EX_INPUT = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

def test_get_part_positions():
    lines = [
        '467..114..',
        '...*......',
    ]
    expected = [
        Part(row=0, span=range(0, 3), val=467),
        Part(row=0, span=range(5, 8), val=114),
    ]
    assert get_part_positions(lines) == expected

def test_get_symbol_positions():
    lines = [
        '......755.',
        '...$.*....',
    ]
    expected = [
        Symbol(row=1, col=3, val='$'),
        Symbol(row=1, col=5, val='*'),
    ]
    assert get_symbol_positions(lines) == expected


def test_find_adjacent():
    # '467..114..',
    # '..1*200...',
    # '..5.9.....',
    # '..35......',
    parts = [
        Part(row=0, span=range(0, 3), val=467),
        Part(row=0, span=range(5, 8), val=114),
        Part(row=1, span=range(2, 3), val=1),
        Part(row=1, span=range(4, 7), val=200),
        Part(row=2, span=range(2, 3), val=5),
        Part(row=2, span=range(4, 5), val=9),
        Part(row=3, span=range(2, 4), val=35),
    ]
    symbol = Symbol(row=1, col=3, val='*')
    assert find_adjacent(parts, symbol) == [
        Part(row=0, span=range(0, 3), val=467),
        Part(row=1, span=range(2, 3), val=1),
        Part(row=1, span=range(4, 7), val=200),
        Part(row=2, span=range(2, 3), val=5),
        Part(row=2, span=range(4, 5), val=9),
    ]

def test_sum_parts():
    assert sum_parts(EX_INPUT) == 4361