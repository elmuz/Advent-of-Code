from collections import defaultdict
from enum import Enum
from functools import total_ordering
from pathlib import Path
from typing import List


class Type(Enum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


@total_ordering
class Card:
    def __init__(self, s: str):
        self.char = s
        self.value = Card.value_from_char(s)
    
    @staticmethod
    def value_from_char(s: str) -> int:
        if s == "A":
            return 14
        elif s == "K":
            return 13
        elif s == "Q":
            return 12
        elif s == "J":
            return 1
        elif s == "T":
            return 10
        else:
            return int(s)
    
    def __lt__(self, other: "Card") -> bool:
        return self.value < other.value
    
    def __eq__(self, other: "Card") -> bool:
        return self.value == other.value


@total_ordering
class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = [Card(c) for c in cards]
        self.bid = bid
        self.type = Hand.get_type_from_hand(self.cards)
    
    @staticmethod
    def get_type_from_hand(cards: List[Card]) -> Type:
        map = defaultdict(lambda: 0)
        for card in cards:
            map[card.char] += 1
        
        if "J" in map:
            if len(map) > 1:
                num_jokers = map.pop("J")
                best_v = 0
                best = None
                for k, v in map.items():
                    if v > best_v:
                        best_v = v
                        best = k
                map[best] += num_jokers
        
        if len(map) == 1:
            return Type.FiveOfAKind
        if len(map) == 2:
            for v in map.values():
                if v == 1 or v == 4:
                    return Type.FourOfAKind
                return Type.FullHouse
        if len(map) == 3:
            for v in map.values():
                if v == 1:
                    continue
                if v == 3:
                    return Type.ThreeOfAKind
                else:
                    return Type.TwoPairs
        if len(map) == 4:
            return Type.OnePair
        return Type.HighCard
    
    def __eq__(self, other) -> bool:
        if self.type.value != other.type.value:
            return False
        for c_i, c_j in zip(self.cards, other.cards):
            if c_i != c_j:
                return False
        return True
    
    def __lt__(self, other) -> bool:
        if self.type.value < other.type.value:
            return True
        elif self.type.value > other.type.value:
            return False
        for c_i, c_j in zip(self.cards, other.cards):
            if c_i < c_j:
                return True
            if c_i > c_j:
                return False
        return False


def run(lines: List[str]) -> int:
    hands = []
    for line in lines:
        hand, bid_str = line.strip().split(" ")
        hands.append(Hand(hand, int(bid_str)))
    hands = sorted(hands)
    bids = [idx * hand.bid for (idx, hand) in enumerate(hands, start=1)]
    return sum(bids)


if __name__ == '__main__':
    assert run(
        [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]
    ) == 5905
    with Path("aoc-7.txt").open() as f:
        lines = f.readlines()
    print(run(lines))