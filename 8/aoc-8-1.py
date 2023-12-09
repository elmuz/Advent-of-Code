from pathlib import Path
from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None
    

def run(nodes: List[str], instructions: str) -> int:
    node_list = []
    graph = {}
    for node in nodes:
        node_id, edges = node.strip().split(" = ")
        node_list.append((node_id, edges[1:4], edges[6:9]))
        graph[node_id] = Node(node_id)
    for node in node_list:
        graph[node[0]].left = graph[node[1]]
        graph[node[0]].right = graph[node[2]]

    counter = 0
    instruction_id = 0
    num_instr = len(instructions)
    node = graph["AAA"]
    while node.name != "ZZZ":
        instruction = instructions[instruction_id]
        instruction_id = (instruction_id + 1) % num_instr
        if instruction == "L":
            node = node.left
        else:
            node = node.right
        counter += 1
    return counter


if __name__ == '__main__':
    assert run(
        nodes=
        [
            'AAA = (BBB, BBB)',
            'BBB = (AAA, ZZZ)',
            'ZZZ = (ZZZ, ZZZ)',
        ],
        instructions="LLR",
    ) == 6
    
    with Path("aoc-8.txt").open() as f:
        lines = f.readlines()
    instructions = lines[0].strip()
    nodes = lines[2:]
    print(run(nodes, instructions))
