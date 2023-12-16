from pathlib import Path
from typing import List


def run(lines: List[str]) -> int:
    def run_with_start(r, c, d) -> int:
        tiles = set()
        lut = set()
        
        to_do = [(r, c, d)]
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
        
    best = 0
    for c in range(len(lines[0])):
        best = max(best, run_with_start(0, c, "S"))
        best = max(best, run_with_start(len(lines) - 1, c, "N"))
    for r in range(len(lines)):
        best = max(best, run_with_start(r, 0, "E"))
        best = max(best, run_with_start(0, len(lines[0]), "W"))
    return best


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
    ) == 51
    
    print(run(Path("aoc-16.txt").read_text().strip().split("\n")))
