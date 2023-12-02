# 12 red cubes, 13 green cubes, and 14 blue cubes
from pathlib import Path
from typing import Dict, List, Tuple


input_fpath = Path("aoc-2-1.txt")

def parse_one_line(line: str) -> Tuple[int, List[Dict[str, int]]]:
    left_part, right_part = line.strip().split(": ")
    game_id = int(left_part.split(" ")[1])
    hands = right_part.split("; ")
    hands_list = []
    for hand in hands:
        hand_dict = {"red": 0, "green": 0, "blue": 0}
        for quantity in hand.split(", "):
            qt, color = quantity.split(" ")
            hand_dict[color] = int(qt)
        hands_list.append(hand_dict)
    return game_id, hands_list


with input_fpath.open() as f:
    games = f.readlines()

def process_lines(lines: List[str]) ->  int:
    total = 0
    for line in lines:
        game_id, hands_list = parse_one_line(line)
        possible = True
        for hand in hands_list:
            if hand["red"] > 12 or hand["green"] > 13 or hand["blue"] > 14:
                possible = False
                break
        if possible:
            print(f"game {game_id} is possible")
            total += game_id
    return total

test_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
assert process_lines(test_lines) == 8

print(process_lines(games))
