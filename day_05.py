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
    maps = sorted(maps, key=lambda x: x[1])
    for i in range(len(maps)):
        if seed >= maps[i][1]: 
            if i == len(maps) - 1: # last map
                # check the map
                dest, source, r = maps[i]
                if seed in range(source, source + r):
                    return (seed - source) + dest
                # not in mapping, return the seed
                return seed
            
            if seed < maps[i+1][1]: # greater than this, not as big as next
                # check it
                dest, source, r = maps[i]
                if seed in range(source, source + r):
                    return (seed - source) + dest
                return seed
            # keep looking for the right spot
            continue
            
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

# PART II expands the seed list
def expand_seed_list(seeds):
    # seed list is actually pairs of numbers and their ranges
    # so SEEDS = [79, 14, 55, 13]
    # is seeds numbered 79 through 79+14 and 55 through 55+13
    # all the seed need to be mapped to locations to find the closest 
    seed_list = []
    assert len(seed_list) % 2 == 0
    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_range = seeds[i + 1]
        seed_end = seed_start + seed_range
        seed_list.extend([x for x in range(seed_start, seed_end)])

    return seed_list

if __name__ == "__main__":
    with open('puzzle_input/day_05.txt', 'r') as f:
        lines = f.readlines()
    
    seeds, almanac = parse_almanac(lines)
 
    print(get_closest_location(seeds, almanac)) # 388071289

#     expanded_seeds = expand_seed_list(seeds)
#     get_closest_location(expanded_seeds, almanac)
#     print("PART II result", get_closest_location(expanded_seeds, almanac))
