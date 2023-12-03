from pathlib import Path
from typing import Optional

digit_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

def isint(char: str) -> Optional[int]:
    return digit_map.get(char)

def get_code_from_line(line: str) -> int:
    idx = 0
    idx_2 = len(line) - 1
    left = None
    right = None
    while idx < len(line):
        num = isint(line[idx])
        if num is not None:
            left = num
            break
        idx += 1
    while idx_2 > idx:
        num = isint(line[idx_2])
        if num is not None:
            right = num
            break
        idx_2 -= 1
    if right is None:
        right = left
    return left * 10 + right

fpath = Path("AoC-1.txt")
total = 0
with fpath.open() as f:
    lines = f.readlines()

for l in lines:
    total += get_code_from_line(l)
    
print(total)