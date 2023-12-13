from pathlib import Path
from typing import List


def run(map: List[str]) -> int:
    found = False
    for r, row in enumerate(map):
        for c, s in enumerate(row):
            if s == "S":
                found = True
                break
        if found:
            break
    assert found
    
    direction = None
    while True:
        # Check North
        if r > 0 and map[r - 1][c] in ["|", "7", "F"]:
            direction = "N"
            r -= 1
            break
        if c < len(map[0]) - 1 and map[r][c + 1] in ["-", "J", "7"]:
            direction = "E"
            c += 1
            break
        if r < len(map) - 1 and map[r + 1][c] in ["|", "J", "L"]:
            direction = "S"
            r += 1
            break
        if c > 0 and map[r][c - 1] in ["-", "L", "F"]:
            direction = "W"
            c -= 1
            break
    assert direction is not None
    
    counter = 1
    found = False
    while found is False:
        if map[r][c] == "|":
            if direction == "S":
                r += 1
            elif direction == "N":
                r -= 1
        elif map[r][c] == "7":
            if direction == "E":
                r += 1
                direction = "S"
            elif direction == "N":
                c -= 1
                direction = "W"
        elif map[r][c] == "J":
            if direction == "E":
                r -= 1
                direction = "N"
            elif direction == "S":
                c -= 1
                direction = "W"
        elif map[r][c] == "F":
            if direction == "N":
                c += 1
                direction = "E"
            elif direction == "W":
                r += 1
                direction = "S"
        elif map[r][c] == "L":
            if direction == "W":
                r -= 1
                direction = "N"
            elif direction == "S":
                c += 1
                direction = "E"
        elif map[r][c] == "-":
            if direction == "W":
                c -= 1
            elif direction == "E":
                c += 1
        counter += 1
        if map[r][c] == "S":
            found = True
    
    return counter // 2
    
    


if __name__ == '__main__':
    assert run(
        [
            "..F7.",
            ".FJ|.",
            "SJ.L7",
            "|F--J",
            "LJ...",
        ]
    ) == 8
    with Path("aoc-10.txt").open() as f:
        map = f.readlines()
    print(run(map))