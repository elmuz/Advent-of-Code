from pathlib import Path
from typing import Optional

class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.is_word = False
        
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

            
digit_map = {
    "0": 0,
    "zero": 0,
    "1": 1,
    "one": 1,
    "2": 2,
    "two": 2,
    "3": 3,
    "three": 3,
    "4": 4,
    "four": 4,
    "5": 5,
    "five": 5,
    "6": 6,
    "six": 6,
    "7": 7,
    "seven": 7,
    "8": 8,
    "eight": 8,
    "9": 9,
    "nine": 9,    
}

def get_code_from_line(line: str) -> int:
    nums = []
    i = 0
    while i < len(line):
        node = trie.root
        for j in range(i, len(line)):
            if line[j] in node.children:
                if node.children[line[j]].is_word:
                    num = digit_map[node.children[line[j]].text]
                    nums.append(num)
                    break
                node = node.children[line[j]]
            else:
                break
        i += 1
    return nums[0] * 10 + nums[-1]

fpath = Path("AoC-1.txt")
trie = PrefixTree()
for k in digit_map:
    trie.insert(k)
    
total = 0
with fpath.open() as f:
    lines = f.readlines()

for l in lines:
    total += get_code_from_line(l)


assert get_code_from_line("two1nine") == 29 
assert get_code_from_line("eightwothree") == 83 
assert get_code_from_line("abcone2threexyz") == 13
assert get_code_from_line("7pqrstsixteen") == 76



print(total)