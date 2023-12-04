from pathlib import Path
from typing import List, Set


class Card:
    def __init__(self, id_: int, left_nums: Set[int], right_nums: Set[int]):
        self.id = id_
        self.left_nums = left_nums
        self.right_nums = right_nums

    @classmethod
    def from_str(cls, line: str):
        card_num, nums = line.split(": ")
        card_num = int(card_num.split(" ")[-1])
        left, right = nums.split(" | ")
        left = {int(n) for n in left.split(" ") if n != ""}
        right = {int(n) for n in right.split(" ") if n != ""}
        return Card(card_num, left, right)
    
    def match(self) -> int:
        counter = 0
        for num in self.left_nums:
            if num in self.right_nums:
                counter += 1
        return counter


def process_one_line(line: str) -> int:
    nums = line.split(": ")[1]
    left, right = nums.split(" | ")
    left = {int(n) for n in left.split(" ") if n != ""}
    right = {int(n) for n in right.split(" ") if n != ""}
    counter = 0
    for num in left:
        if num in right:
            counter += 1
    if counter > 0:
        return 2 ** (counter - 1)
    else:
        return 0


def run(lines: List[str]) -> int:
    cards = {}
    for line in lines:
        line = line.strip()
        card = Card.from_str(line)
        cards[card.id] = card.match()
    
    to_check_list = list(cards.keys())
    counter = len(to_check_list)
    while len(to_check_list) > 0:
        card_id = to_check_list.pop()
        new_cards = cards[card_id]
        for c in range(new_cards):
            to_check_list.append(card_id + 1 + c)
            counter += 1
    return counter


def test() -> int:
    lines =  [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
    return run(lines)
    
    
if __name__ == '__main__':
    with Path("aoc-4.txt").open() as f:
        lines = f.readlines()
    
    assert test() == 30, test()
    print(run(lines))
