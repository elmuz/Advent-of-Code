from typing import List, Tuple


def process_one_race(time: int , distance: int) -> int:
    counter = 0
    for t in range(time):
        distance_t = t * (time - t)
        if distance_t > distance:
            counter += 1
    return counter


def run(races: List[Tuple[int, int]]):
    total = 1
    for time, distance in races:
        total *= process_one_race(time, distance)
    return total


if __name__ == '__main__':
    assert run([
        (7, 9), (15, 40), (30, 200),
    ]) == 288
    print(run([
        (53, 275), (71, 1181), (78, 1215), (80, 1524)
    ]))
