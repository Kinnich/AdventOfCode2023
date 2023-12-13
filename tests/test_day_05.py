import pytest

from AdventOfCode2023.day_05 import (
    map_to_destination,
    get_location,
    get_closest_location,
    parse_almanac,
    expand_seed_list,
)

@pytest.mark.parametrize(
    'seed, exp_result',
    [
        (0, 2),
        (50, 52),
        (14, 14),
        (55, 57),
        (99, 51),
        (97, 99)
    ]
)
def test_map_to_destination(seed, exp_result):
    maps = [
        (50, 98, 2),
        (52, 50, 48),
        (2, 0, 1),
    ]
    result = map_to_destination(seed, maps)
    assert result == exp_result

SEEDS = [79, 14, 55, 13]

ALMANAC = [
    [ # seed-to-soil map
        (50, 98, 2),
        (52, 50, 48),
    ],
    [ # soil-to-fertilizer map
        (0, 15, 37),
        (37, 52, 2),
        (39, 0, 15),
    ],
    [ # fertilizer-to-water map:
        (49, 53, 8),
        (0, 11, 42),
        (42, 0, 7),
        (57, 7, 4),
    ],
    [ # water-to-light map:
        (88, 18, 7),
        (18, 25, 70),
    ],
    [ # light-to-temperature map:
        (45, 77, 23),
        (81, 45, 19),
        (68, 64, 13),
    ],
    [ # temperature-to-humidity map:
        (0, 69, 1),
        (1, 0, 69),
    ],
    [ # humidity-to-location map:
        (60, 56, 37),
        (56, 93, 4),
    ],
]

def test_get_location():
    seed = 79
    assert get_location(seed, ALMANAC) == 82

def test_get_closest_location():
    assert get_closest_location(SEEDS, ALMANAC) == 35


def test_parse_almanac():
    with open('tests/day_05_TEST.txt', 'r') as f:
        lines = f.readlines()
    
    seeds, almanac = parse_almanac(lines)
    assert seeds == SEEDS
    assert len(almanac) == 7
    assert [len(x) for x in almanac] == [2, 3, 4, 2, 3, 2, 2]


def test_expand_seed_list():
    assert len(expand_seed_list(SEEDS)) == 27

def test_part_two():
    expanded_seeds = expand_seed_list(SEEDS)
    assert get_closest_location(expanded_seeds, ALMANAC) == 46