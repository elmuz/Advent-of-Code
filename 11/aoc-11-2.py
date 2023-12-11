from pathlib import Path
from typing import List


class Galaxy:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
    
    def distance(self, other: "Galaxy") -> int:
        return abs(self.row - other.row) + abs(self.col - other.col)


def run(lines: List[str], expansion_factor: int) -> int:
    expand_rows_set = set(range(len(lines)))
    expand_cols_set = set(range(len(lines[0])))
    galaxies = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "#":
                if row in expand_rows_set:
                    expand_rows_set.remove(row)
                if col in expand_cols_set:
                    expand_cols_set.remove(col)
                galaxies.append(Galaxy(row, col))
    galaxies.sort(key=lambda galaxy: galaxy.row)
    expand_rows = sorted(list(expand_rows_set))
    expand_cols = sorted(list(expand_cols_set))
    
    g_idx = 0
    expand_id = 0
    while g_idx < len(galaxies):
        while expand_id < len(expand_rows) and galaxies[g_idx].row > expand_rows[expand_id]:
            expand_id += 1
        galaxies[g_idx].row += expand_id * expansion_factor - expand_id
        g_idx += 1
    
    galaxies.sort(key=lambda galaxy: galaxy.col)
    g_idx = 0
    expand_id = 0
    while g_idx < len(galaxies):
        while expand_id < len(expand_cols) and galaxies[g_idx].col > expand_cols[expand_id]:
            expand_id += 1
        galaxies[g_idx].col += expand_id * expansion_factor - expand_id
        g_idx += 1
    
    counter = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            counter += galaxies[i].distance(galaxies[j])
    return counter


if __name__ == '__main__':
    assert run(
        [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#.....",
        ], expansion_factor=10
    ) == 1030
    print(run(Path("aoc-11.txt").read_text().split("\n"), expansion_factor=1000000))
