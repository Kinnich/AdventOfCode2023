"""
Day 6: Toy boat races
https://adventofcode.com/2023/day/6
Time:      7  15   30
Distance:  9  40  200
The input document describes three races:
The time the race lasts and the record distance traveled

Your boat starts at a speed of 0 and for each ms you spend
pressing the button, the speed will increase by 1 mm/ms.
So if you hold the button for 2 ms it will have 5 ms left
to travel at a pace of 2 mm/ms for a total distance of 10 mm.

Calculate how many ways you can beat the record for each race
and then return the result as these numbers multiplied together.
In the above example the answer is 288 (4 * 8 * 9)
"""
import re


def calculate_win_options(time, record):
    wins = 0
    for t in range(1, time):
        distance = (time - t) * t
        if distance > record:
            wins += 1
    return wins

def win_margin(times: list, records: list):
    win_options = 1
    for time, record in zip(times, records):
        win_options *= calculate_win_options(time, record)
    return win_options


if __name__ == '__main__':
    with open('puzzle_input/day_06.txt', 'r') as f:
        lines = f.readlines()
    
    times = [int(x) for x in re.findall('[0-9]+',lines[0])]
    records = [int(x) for x in re.findall('[0-9]+',lines[1])]
    print(times, records)
    print(win_margin(times, records))