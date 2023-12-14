from collections import defaultdict
from pathlib import Path
from typing import List


def run(map: List[str]) -> int:
    # IDEA
    # You are inside the loop when you cross the boundary an odd number of times.
    # Then, we can traverse the map row by row and keep track of how many times we cross the loop.
    # Finally, we return the number of tiles we have counted while "inside" the loop.
    #
    # 1) Track down the loop and take not of the coordinates into a lookup table.
    # 2) Create a sorted data structure, here `lut_r`. Every row contains the sorted columns that are
    #    traversed by the loop.
    # 3) Replace "S" with the proper symbol according to the routing.
    # 4) Notice that "L" followed by "7" or "F" followed by "J" do not flip the in/out condition.
    
    found = False
    for r, row in enumerate(map):
        for c, s in enumerate(row):
            if s == "S":
                found = True
                break
        if found:
            break
    assert found

    while True:
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
    start_direction = direction

    loop_coords = set()
    lut_r = defaultdict(list)
    lut_r[r].append((c, map[r][c]))
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
        if map[r][c] == "S":
            found = True
            end_direction = direction
        else:
            loop_coords.add((r, c))
            lut_r[r].append((c, map[r][c]))

    # Replace "S" with the appropriate symbol
    s_symbol = None
    if (
        start_direction == "N"
        and end_direction == "N"
        or start_direction == "S"
        and end_direction == "S"
    ):
        s_symbol = "|"
    elif (
        start_direction == "W"
        and end_direction == "W"
        or start_direction == "E"
        and end_direction == "E"
    ):
        s_symbol = "-"
    elif (
        end_direction == "N"
        and start_direction == "E"
        or end_direction == "W"
        and start_direction == "S"
    ):
        s_symbol = "F"
    elif (
        end_direction == "N"
        and start_direction == "W"
        or end_direction == "E"
        and start_direction == "S"
    ):
        s_symbol = "7"
    elif (
        end_direction == "S"
        and start_direction == "W"
        or end_direction == "E"
        and start_direction == "N"
    ):
        s_symbol = "J"
    elif (
        end_direction == "S"
        and start_direction == "E"
        or end_direction == "W"
        and start_direction == "N"
    ):
        s_symbol = "L"
    assert s_symbol is not None
    loop_coords.add((r, c))
    lut_r[r].append((c, s_symbol))

    for col_list in lut_r.values():
        col_list.sort()

    counter = 0
    for r, col_list in lut_r.items():
        inner = False
        boundary_start = None
        last_s = None
        for c, s in col_list:
            if s in ["|", "7", "J", "F", "L"]:
                if last_s == "L" and s == "7":
                    continue
                elif last_s == "F" and s == "J":
                    continue
                last_s = s
                inner = not inner
                if inner:
                    boundary_start = c
                if not inner:
                    boundary_end = c
                    for c_inner in range(boundary_start + 1, boundary_end):
                        if (r, c_inner) not in loop_coords:
                            counter += 1

    return counter


if __name__ == "__main__":
    assert (
        run(
            [
                ".F----7F7F7F7F-7....",
                ".|F--7||||||||FJ....",
                ".||.FJ||||||||L7....",
                "FJL7L7LJLJ||LJ.L-7..",
                "L--J.L7...LJS7F-7L7.",
                "....F-J..F7FJ|L7L7L7",
                "....L7.F7||L7|.L7L7|",
                ".....|FJLJ|FJ|F7|.LJ",
                "....FJL-7.||.||||...",
                "....L---J.LJ.LJLJ...",
            ]
        )
        == 8
    )
    assert (
        run(
            [
                "FF7FSF7F7F7F7F7F---7",
                "L|LJ||||||||||||F--J",
                "FL-7LJLJ||||||LJL-77",
                "F--JF--7||LJLJ7F7FJ-",
                "L---JF-JLJ.||-FJLJJ7",
                "|F|F-JF---7F7-L7L|7|",
                "|FFJF7L7F-JF7|JL---7",
                "7-L-JL7||F7|L7F-7F7|",
                "L.L7LFJ|||||FJL7||LJ",
                "L7JLJL-JLJLJL--JLJ.L",
            ]
        )
        == 10
    )
    with Path("aoc-10.txt").open() as f:
        map = f.readlines()
    print(run(map))
