from AdventOfCode2023.day_02 import (
    Game,
    find_color_max,
    game_dict,
    parse_input,
    possible_games,
    sum_power_max_colors
)

PART_I_EX_INPUT = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

def test_find_color_max():
    line = "Game 1: 3 blue, 4 red; 1 red, 6 blue"
    assert find_color_max("blue", line) == 6
    assert find_color_max("green", line) == 0


def test_game_dict():
    line = "Game 1: 3 blue, 4 red; 1 red, 6 blue"
    assert game_dict(line) == {'blue': 6, 'green': 0, 'red': 4}


def test_parse_input():
    assert parse_input(PART_I_EX_INPUT) == [
        Game(id=1, blue=6, green=2, red=4),
        Game(id=2, blue=4, green=3, red=1),
        Game(id=3, blue=6, green=13, red=20),
        Game(id=4, blue=15, green=3, red=14),
        Game(id=5, blue=2, green=3, red=6),
    ]

def test_possible_games():
    assert possible_games(PART_I_EX_INPUT) == 8

def test_sum_power_max_colors():
    assert sum_power_max_colors(PART_I_EX_INPUT) == 2286