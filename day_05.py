"""
https://adventofcode.com/2023/day/5

"seeds: 79 14 55 13",

"seed-to-soil map:",
"50 98 2",
"52 50 48",

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
"""
import re

def map_to_destination(seed:int, maps:list[tuple]):
    # TODO: sort maps by source, then start search at closest to seed num
    for m in maps:
        dest, source, r = m
        if seed in range(source, source + r):
            return (seed - source) + dest
    return seed


def get_location(seed: int, almanac: list[list[tuple]]):
    current_val = seed
    for a in almanac:
        current_val = map_to_destination(current_val, a)
    return current_val


def get_closest_location(seeds: list[int], almanac: list[list[tuple]]):
        return min(get_location(seed, almanac) for seed in seeds)


def parse_almanac(lines: list[str]):
    # Seeds list is first line in text
    seeds = [int(seed) for seed in re.findall('[0-9]+', lines[0])]
    
    almanac = []
    mapping = []
    
    # Keep track of line nums so we know to save the last mapping
    # when we get to end of file
    line_cnt = 0
    end = len(lines[1:])
    
    for line in lines[1:]:
        line_cnt += 1
        partial_map =  re.findall('[0-9]+', line)
        if partial_map:
            mapping.append(tuple([int(p) for p in partial_map]))
        
        # Identify new mapping as starting after a new line
        if line == '\n' or line_cnt == end:
            # Save the previously parsed map if there is one
            if mapping:
                almanac.append(mapping)
                mapping = []
            continue
    return seeds, almanac

if __name__ == "__main__":
    with open('puzzle_input/day_05.txt', 'r') as f:
        lines = f.readlines()
    
    seeds, almanac = parse_almanac(lines)
 
    print(get_closest_location(seeds, almanac))

#     print(almanac)
#     print(len(almanac))
#     print([len(a) for a in almanac])