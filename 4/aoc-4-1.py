from pathlib import Path
from typing import List


def process_one_line(line: str) -> int:
    nums = line.split(": ")[1]
    left, right = nums.split(" | ")
    left = {int(n) for n in left.split(" ") if n != ""}
    right = {int(n) for n in right.split(" ") if n != ""}
    counter = 0
    for l in left:
        if l in right:
            counter += 1
    if counter > 0:
        return 2 ** (counter - 1)
    else:
        return 0


def run(lines: List[str]) -> int:
    counter = 0
    for line in lines:
        line = line.strip()
        counter += process_one_line(line)
    return counter


def test() -> int:
    lines =  [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
    return run(lines)
    
    
if __name__ == '__main__':
    with Path("aoc-4.txt").open() as f:
        lines = f.readlines()
    
    assert test() == 13
    print(run(lines))
