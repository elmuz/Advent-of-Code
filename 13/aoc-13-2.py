from pathlib import Path
from typing import List


def process_one_mirror(mirror: List[str]) -> int:
    # Vertical mirror
    for m_i in range(1, len(mirror[0])):
        smudge = 0
        for j in range(1, min(m_i, len(mirror[0]) - m_i) + 1):
            for row in range(len(mirror)):
                if mirror[row][m_i - j] != mirror[row][m_i - 1 + j]:
                    smudge += 1
                    if smudge > 1:
                        break
            if smudge > 1:
                break
        if smudge == 1:
            return m_i
    
    # Horizontal mirror:
    for m_i in range(1, len(mirror)):
        smudge = 0
        for j in range(1, min(m_i, len(mirror) - m_i) + 1):
            for col in range(len(mirror[0])):
                if mirror[m_i - j][col] != mirror[m_i - 1 + j][col]:
                    smudge += 1
                    if smudge > 1:
                        break
            if smudge > 1:
                break
        if smudge == 1:
            return m_i * 100
    
    # It should never get here
    raise


def run(input_file: Path) -> int:
    lines = input_file.read_text().splitlines()
    line_idx = 0
    mirror = []
    counter = 0
    while line_idx < len(lines):
        while line_idx < len(lines) and lines[line_idx] != "":
            mirror.append(lines[line_idx])
            line_idx += 1
        counter += process_one_mirror(mirror)
        mirror = []
        line_idx += 1
    return counter


if __name__ == '__main__':
    assert run(Path("aoc-13-test.txt")) == 400
    print(run(Path("aoc-13.txt")))