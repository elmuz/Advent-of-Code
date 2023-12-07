from pathlib import Path
from typing import Dict, List, Tuple


input_fpath = Path("aoc-2-1.txt")

def parse_one_line(line: str) -> Tuple[int, Dict[str, int]]:
    left_part, right_part = line.strip().split(": ")
    game_id = int(left_part.split(" ")[1])
    hands = right_part.split("; ")
    game_dict = {"red": 0, "green": 0, "blue": 0}
    for hand in hands:
        for quantity in hand.split(", "):
            qt, color = quantity.split(" ")
            game_dict[color] = max(int(qt), game_dict[color])
    return game_id, game_dict


with input_fpath.open() as f:
    games = f.readlines()

def process_lines(lines: List[str]) ->  int:
    total = 0
    for line in lines:
        game_id, game = parse_one_line(line)
        powerset = game['red'] * game['green'] * game['blue']
        total += powerset
    return total

test_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
assert process_lines(test_lines) == 2286, process_lines(test_lines)

print(process_lines(games))
