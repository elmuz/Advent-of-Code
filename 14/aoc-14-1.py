from pathlib import Path
from typing import List


def run(map: List[str]) -> int:
    counter = 0
    for c in range(len(map[0])):
        stack = 0
        for r in range(len(map) - 1, -1, -1):
            if map[r][c] == ".":
                continue
            elif map[r][c] == "#":
                for i in range(len(map) - r - stack, len(map) - r):
                    counter += i
                stack = 0
            elif map[r][c] == "O":
                stack += 1
        for i in range(len(map) - stack + 1, len(map) + 1):
            counter += i
    return counter


if __name__ == '__main__':
    assert run(
        [
            "O....#....",
            "O.OO#....#",
            ".....##...",
            "OO.#O....O",
            ".O.....O#.",
            "O.#..O.#.#",
            "..O..#O..O",
            ".......O..",
            "#....###..",
            "#OO..#....",
        ]
    ) == 136
    
    print(run(Path("aoc-14.txt").read_text().strip().split("\n")))
