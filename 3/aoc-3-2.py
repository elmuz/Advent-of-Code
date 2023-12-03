from pathlib import Path
from typing import Dict, List, Set, Tuple


class Number:
    def __init__(self, row: int):
        self._row = row
        self._col_start = None
        self._str = ""
    
    def append(self, col: int, char: str):
        if self._col_start is None:
            self._col_start = col
            self._col_end = col
        else:
            self._col_end += 1
        self._str += char
    
    def reset(self):
        self._col_start = None
        self._str = ""
    
    def is_number(self) -> bool:
        return len(self._str) > 0
    
    def is_part_number(self, symbol_map: Set[Tuple[int, int]]) -> bool:
        if self._str == "":
            return False
        for col in range(self._col_start, self._col_end + 1):
            if col == self._col_start:  # left-most char
                if (self._row - 1, col - 1) in symbol_map:
                    return True
                if (self._row, col - 1) in symbol_map:
                    return True
                if (self._row + 1, col - 1) in symbol_map:
                    return True
            if col == self._col_end:  # right-most char
                if (self._row - 1, col + 1) in symbol_map:
                    return True
                if (self._row, col + 1) in symbol_map:
                    return True
                if (self._row + 1, col + 1) in symbol_map:
                    return True
            if (self._row - 1, col) in symbol_map:
                return True
            if (self._row + 1, col) in symbol_map:
                return True
        return False
    
    def to_int(self) -> int:
        return int(self._str)


def _create_symbol_map(schema: List[str]) -> Set[Tuple[int, int]]:
    symbol_map = set()
    for row, line in enumerate(schema):
        line = line.strip()
        for col, char in enumerate(line):
            if char not in {".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                symbol_map.add((row, col))
    return symbol_map


def add_number_to_map(number_map: Dict[Tuple[int, int], Tuple[Tuple[int, int], Tuple[int, int], str]],
    number: Number) -> None:
    for col in range(number._col_start, number._col_end + 1):
        number_map[(number._row, col)] = ((number._row, number._col_start), (number._row, number._col_end), number._str)


def run(schema: List[str]) -> int:
    symbol_map = _create_symbol_map(schema)
    number_map = {}
    
    for row, line in enumerate(schema):
        line = line.strip()
        col = 0
        num = Number(row)
        while col < len(line):
            if (row, col) in symbol_map or line[col] == ".":
                if num.is_part_number(symbol_map):
                    add_number_to_map(number_map, num)
                num.reset()
            else:
                num.append(col, line[col])
            col += 1
        if num.is_number():
            if num.is_part_number(symbol_map):
                add_number_to_map(number_map, num)
    counter = 0
    for row, line in enumerate(schema):
        line = line.strip()
        for col, char in enumerate(line):
            if char != "*":
                continue
            neighbors = set()
            if (row - 1, col - 1) in number_map:
                neighbors.add(number_map[(row - 1, col - 1)])
            if (row - 1, col) in number_map:
                neighbors.add(number_map[(row - 1, col)])
            if (row - 1, col + 1) in number_map:
                neighbors.add(number_map[(row - 1, col + 1)])
            if (row, col + 1) in number_map:
                neighbors.add(number_map[(row, col + 1)])
            if (row + 1, col + 1) in number_map:
                neighbors.add(number_map[(row + 1, col + 1)])
            if (row + 1, col) in number_map:
                neighbors.add(number_map[(row + 1, col)])
            if (row + 1, col - 1) in number_map:
                neighbors.add(number_map[(row + 1, col - 1)])
            if (row, col - 1) in number_map:
                neighbors.add(number_map[(row, col - 1)])
            if len(neighbors) == 2:
                tot = 1
                for n in neighbors:
                    tot *= int(n[2])
                counter += tot
    return counter


def main(schema_path: Path):
    with schema_path.open() as f:
        schema = f.readlines()
    counter = run(schema)
    print(f"Total: {counter}")


def test():
    test_lines = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert run(test_lines) == 467835, run(test_lines)


if __name__ == '__main__':
    test()
    main(Path("aoc-3.txt"))
