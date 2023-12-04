"""
Day 4
https://adventofcode.com/2023/day/4

Determine how many numbers in the second half of each card
are in the first half. For each card, one match is worth
1 point, each additional match doubles the points for that card
For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

The final result is the sum of the points for all cards.
In this example, the cards are worth 13 points

--can I assume there are no duplicated numbers in 
each half of a card?
"""

import re
from collections import defaultdict

def get_matching_nums(win_list: list, my_list: list) -> int:
    win_set = set(win_list)
    my_set = set(my_list)

    # Checking that each list has a unique set of nums
    assert len(win_set) == len(win_list)
    assert len(my_set) == len(my_list)

    return len(win_set.intersection(my_set))

def calculate_points(matches: int) ->int:
    if matches:
        return 2 ** (matches - 1)
    return 0


def sum_points(cards) -> int:
    points = 0
    for card in cards:
        win_list = card[0]
        my_list = card[1]
        points += calculate_points(get_matching_nums(win_list, my_list))
    return points


def process_cards(cards: list[list[list[int]]]) -> int:
    card_dict = {c: 1 for c in range(len(cards))}
    for i in range(len(cards)):
        win_list = cards[i][0]
        my_list = cards[i][1]
        matches = get_matching_nums(win_list, my_list)
        if not matches:
            continue
        else:
            for j in range(1, matches + 1):
                card_dict[i+j] = card_dict.get(i+j, 1) + card_dict[i]
    
    return sum(v for v in card_dict.values())


def parse_input(lines: list[str]) -> list[list[list[int]]]:
    """Takes list of strings resulting from readlines() and
    returns a list of cards. Each card is a list of two lists, the
    first representing the winning nums, the second representing my nums
    """
    lines = [line.split(':') for line in lines]
    lines = [line[1] for line in lines] # Drop the card number
    lines = [line.split('|') for line in lines]
        
    card_list = []
    for line in lines:
        card = [cast_to_ints(re.findall('[0-9]+',l)) for l in line]
        card_list.append(card)
    
    return card_list


def cast_to_ints(digits: list[str]) -> list[int]:
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    return digits


if __name__ == "__main__":

    with open("puzzle_input/day_04.txt", "r") as f:
        lines = f.readlines()
    
    cards = parse_input(lines)

    print("Part I result", sum_points(cards))
    # Correct answer -> 23678

    print("Part II result", process_cards(cards))
    # Correct answer -> 15455663
