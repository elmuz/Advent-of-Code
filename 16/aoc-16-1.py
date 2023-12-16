from pathlib import Path
from typing import List


def run(lines: List[str]) -> int:
    tiles = set()
    lut = set()
    to_do = [(0, 0, "E")]
    while len(to_do) > 0:
        r, c, d = to_do.pop()
        if r < 0 or c < 0 or r == len(lines) or c == len(lines[0].strip()) or (r, c, d) in lut:
            continue
        tiles.add((r, c))
        lut.add((r, c, d))
        if lines[r][c] == ".":
            if d == "E":
                to_do.append((r, c + 1, d))
            elif d == "N":
                to_do.append((r - 1, c, d))
            elif d == "S":
                to_do.append((r + 1, c, d))
            elif d == "W":
                to_do.append((r, c - 1, d))
        elif lines[r][c] == "|":
            if d == "E":
                to_do.append((r - 1, c, "N"))
                to_do.append((r + 1, c, "S"))
            elif d == "N":
                to_do.append((r - 1, c, d))
            elif d == "S":
                to_do.append((r + 1, c, d))
            elif d == "W":
                to_do.append((r - 1, c, "N"))
                to_do.append((r + 1, c, "S"))
        elif lines[r][c] == "-":
            if d == "E":
                to_do.append((r, c + 1, d))
            elif d == "N":
                to_do.append((r, c - 1, "W"))
                to_do.append((r, c + 1, "E"))
            elif d == "S":
                to_do.append((r, c - 1, "W"))
                to_do.append((r, c + 1, "E"))
            elif d == "W":
                to_do.append((r, c - 1, d))
        elif lines[r][c] == "/":
            if d == "E":
                to_do.append((r - 1, c, "N"))
            elif d == "N":
                to_do.append((r, c + 1, "E"))
            elif d == "S":
                to_do.append((r, c - 1, "W"))
            elif d == "W":
                to_do.append((r + 1, c, "S"))
        elif lines[r][c] == "\\":
            if d == "E":
                to_do.append((r + 1, c, "S"))
            elif d == "N":
                to_do.append((r, c - 1, "W"))
            elif d == "S":
                to_do.append((r, c + 1, "E"))
            elif d == "W":
                to_do.append((r - 1, c, "N"))
    return len(tiles)


if __name__ == '__main__':
    test = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""
    assert run(
        test.split("\n")
    ) == 46
    
    print(run(Path("aoc-16.txt").read_text().strip().split("\n")))
