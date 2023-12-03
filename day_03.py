"""
Day 3
https://adventofcode.com/2023/day/3

"Parts" are represented by numbers adjacent to a symbol.
Sum every number adjacent (and diagonal) to a symbol (not including period (.)):

Example input:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

Two numbers are not part numbers because they are not adjacent to a symbol:
114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and their sum is 4361.
"""
# need the position of the numbers and the position of the symbols
import re
from dataclasses import dataclass


@dataclass
class Part:
    row: int
    span: range
    val: int

@dataclass
class Symbol:
    row: int
    col: int
    val: str

def get_part_positions(lines):
    parts = []
    for row, line in enumerate(lines):
        # Use regex to match numbers with any amount of digits
        for match in re.finditer('[0-9]+', line):
            span = range(match.span()[0], match.span()[1]) # make a range from the match's span attribute
            parts.append(Part(row=row, span=span, val=int(match.group()))) 
    
    return parts


def get_symbol_positions(lines):
    symbols = []
    for row, line in enumerate(lines):
        # Use regex to match everything EXCEPT word characters, digits, and periods (.)
        for match in re.finditer('[^\.\w\d]', line): 
            col = match.span()[0]
            symbols.append(Symbol(row=row, col=col, val=match.group()))
    
    return symbols


def find_adjacent(parts: list[Part], symbol: Symbol) -> list[Part]:
    adj = []
    symbol_rows = range(symbol.row -1, symbol.row + 2) # check rows above and below
    symbol_cols = range(symbol.col -1, symbol.col + 2) # check columns on either side
    for part in parts:
        if part.row in symbol_rows:
            if set(symbol_cols).intersection(part.span):
                adj.append(part)
    return adj


def sum_parts(lines: list[str]) -> int:
    parts = get_part_positions(lines)
    symbols = get_symbol_positions(lines)
    
    adjacent_parts = []
    for symbol in symbols:
        adjacent_parts.extend(find_adjacent(parts, symbol))
    
    return sum(ap.val for ap in adjacent_parts)

"""
 ---Part II ---
 A gear is any '*' symbol that is adjacent to exactly two part numbers. 
 Its gear ratio is the result of multiplying those two numbers together.

Find the gear ratio of every gear and add them all up.
"""
def sum_gear_ratios(lines: list[str]) -> int:
    
    parts = get_part_positions(lines)
    symbols = get_symbol_positions(lines)

    gears = []
    for symbol in symbols:
        if symbol.val == '*':
            adj_parts = find_adjacent(parts, symbol)
            if len(adj_parts) == 2:
                gear_ratio = adj_parts[0].val * adj_parts[1].val
                gears.append(gear_ratio)
    
    return sum(g for g in gears)


if __name__ == "__main__":
    with open('puzzle_input/day_3.txt','r') as f:
        lines = [line.rstrip() for line in f.readlines()] # don't forget to get rid of new line!
        
        print("Part I result", sum_parts(lines)) 
        # Correct answer = 559667

        print("Part II result", sum_gear_ratios(lines))
        # Correct answer = 86841457