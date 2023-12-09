from pathlib import Path
from typing import List


def compute_differences(row: List[int]) -> List[int]:
    output = []
    for a, b in zip(row[:-1], row[1:]):
        output.append(b - a)
    return output

def extrapolate_one_line(line: str) -> int:
    row = [int(n) for n in line.split(" ")]
    rows = [row]
    while sum(row) != 0:
        row = compute_differences(row)
        rows.append(row)
    i = 0
    for row in rows[::-1]:
        i = row[0] - i
    return i


def run(lines: List[str]) -> int:
    extrapolations = [extrapolate_one_line(line.strip()) for line in lines]
    return sum(extrapolations)


if __name__ == '__main__':
    assert run(["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]) == 2
    with Path("aoc-9.txt").open() as f:
        lines = f.readlines()
    print(run(lines))
