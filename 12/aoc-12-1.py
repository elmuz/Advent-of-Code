from pathlib import Path
from typing import List


def process_one_line(line: str) -> int:
    springs, groups = line.split(" ")
    groups = [int(g) for g in groups.split(",")]
    
    def dfs(springs_idx: int, group_idx: int, counter: int) -> int:
        if group_idx == len(groups):
            # Verify if it is a valid configuration (i.e. no more "#").
            if springs_idx < len(springs) and "#" in springs[springs_idx:]:
                return counter
            else:
                return counter + 1
        
        if springs_idx >= len(springs):
            return counter
        
        # Skip all the "."
        while springs_idx < len(springs) and springs[springs_idx] == ".":
            springs_idx += 1
       
        if springs_idx >= len(springs):
            return counter
        
        if springs[springs_idx] == "?":
            counter_i = dfs(springs_idx + 1, group_idx, counter)
        else:
            counter_i = 0
        # Scenario failing spring. Try to set N failed spring
        for i in range(groups[group_idx]):
            if springs_idx + i == len(springs) or springs[springs_idx + i] not in ["?", "#"]:
                # Invalid configuration
                return counter_i
        if springs_idx + groups[group_idx] < len(springs) and springs[springs_idx + groups[group_idx]] == "#":
            # Invalid: "#" must be contiguous
            return counter_i
        
        counter_j = dfs(springs_idx + groups[group_idx] + 1, group_idx + 1, counter)
    
        return counter_i + counter_j
    
    output = dfs(springs_idx=0, group_idx=0, counter=0)
    return output
                

def run(lines: List[str]) -> int:
    return sum([process_one_line(line) for line in lines])


if __name__ == '__main__':
    assert run(
        [
            "???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1",
        ]
    ) == 21
    lines = Path("aoc-12.txt").read_text().splitlines()
    print(run(lines))