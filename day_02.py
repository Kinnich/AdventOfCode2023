"""A bag loaded with cubes of different colors, in each game
some cubes are removed from the bag and the numbers/colors recorded,
then cubes are returned to bag

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

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
import re
from dataclasses import dataclass

@dataclass
class Game:
    id: str
    blue: int
    green: int
    red: int
    
    @classmethod
    def from_dict(cls, game_dict, game_id):
        return Game(
            id=game_id,
            blue=game_dict.get('blue'),
            green=game_dict.get('green'),
            red=game_dict.get('red'),
        )


def find_color_max(color: str, line: int) -> int:
    num_cubes = re.findall(f'[0-9]+\s{color}', line)
    if not num_cubes:
        return 0
    return max(int(cubes.split()[0]) for cubes in num_cubes)


def game_dict(line: str) -> dict:
    colors = ['blue', 'green', 'red']
    return {color: find_color_max(color, line) for color in colors}


def parse_input(lines: list) -> list[Game]:
    return [
        Game.from_dict(game_dict(line), i) for i, line in enumerate(lines, 1)
    ]


def possible_games(lines):
    games = parse_input(lines)
    possible = []
    for game in games:
        if game.blue <= 14 and game.green <= 13 and game.red <= 12:
            possible.append(game.id)
    return sum(possible)


"""Part II
Find the minimum number of each color cubes
Format the final answer as the SUM of the product of the min number of each color
in each game.
The power of the minimum set of cubes in game 1 is 48. 
In games 2-5 it was 12, 1560, 630, and 36, respectively. 
Adding up these five powers produces the sum 2286.
"""

def sum_power_min_colors(lines):
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
    part_II_result = sum_power_min_colors(lines)
    print('part II result', part_II_result)
    # Correct answer = 2085