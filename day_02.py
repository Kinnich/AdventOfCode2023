"""
Day 2
https://adventofcode.com/2023/day/2
A bag is loaded with cubes of different colors, in each game
some cubes are removed from the bag and the numbers/colors recorded,
then cubes are returned to bag.

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

---PART I ---
Which games would have been possible if the bag contained only
12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag 
had been loaded with that configuration. However, game 3 would have been 
impossible because at one point the Elf showed you 20 red cubes at once; 
similarly, game 4 would also have been impossible because the Elf showed 
you 15 blue cubes at once. 

If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. 
What is the sum of the IDs of those games?
"""
from __future__ import annotations
import re
from dataclasses import dataclass

@dataclass
class Game:
    """Small dataclass to the basic info for each game"""
    # Unique ID for each game
    id: str
    # Max number of blue cubes used in each game
    blue: int
    # Max number of green cubes
    green: int
    # Max number of red cubes
    red: int
    
    @classmethod
    def from_dict(cls, game_dict, game_id) -> Game:
        """Create a Game object from a dict and the given id"""
        return Game(
            id=game_id,
            blue=game_dict.get('blue'),
            green=game_dict.get('green'),
            red=game_dict.get('red'),
        )


def find_color_max(color: str, line: int) -> int:
    """Parse a line of input to find the max number for a given cube color"""
    num_cubes_list = re.findall(f'[0-9]+\s{color}', line)
    if not num_cubes_list:
        return 0
    return max(int(cubes.split()[0]) for cubes in num_cubes_list)


def game_dict(line: str) -> dict:
    """Make a dictionary with cube colors as keys and the max number
    of the colors used in a game as the values"""
    colors = ['blue', 'green', 'red']
    return {color: find_color_max(color, line) for color in colors}


def parse_input(lines: list) -> list[Game]:
    """Parse the list of strings representing the game info and return
    a list of Game objects holding the max number of cubes for each color and
    the id of the game, ordered sequentially, starting at 1"""
    return [
        Game.from_dict(game_dict(line), i) for i, line in enumerate(lines, 1)
    ]


def possible_games(lines):
    """Determine which games in the list are possible if there are only
    14 blue, 13 green, and 12 red cubes. Return the result as the sum of
    the game ID's"""
    games = parse_input(lines)
    possible = []
    for game in games:
        if game.blue <= 14 and game.green <= 13 and game.red <= 12:
            possible.append(game.id)
    return sum(possible)


"""
---Part II---
Find the maximum number of each color cubes used in each game.
Format the final answer as the SUM of the product of the max number of each color
in each game.

Using the above example from part I, the power of the set of cubes in game 1 is 48.
4 red, 6 blue, 2 green ->  4 * 8 * 2 = 48
In games 2-5 it was 12, 1560, 630, and 36, respectively. 
Adding up these five powers produces the sum 2286.

Find this outcome for the given input.
"""

def sum_power_max_colors(lines: list[str]) -> int:
    """To find the answer to part II return the sum of the max number of
    each cube color used in each game"""
    games = parse_input(lines)
    return sum(game.blue * game.red * game.green for game in games)

if __name__ =="__main__":
    input = 'puzzle_input/day_02.txt'
    with open(input, 'r') as f:
        lines = f.readlines()
    
    # Part I
    part_I_result = possible_games(lines)
    print('part I result', part_I_result)
    # Correct answer = 2085

    # Part II
    part_II_result = sum_power_max_colors(lines)
    print('part II result', part_II_result)
    # Correct answer = 79315