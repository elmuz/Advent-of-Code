from math import lcm
from pathlib import Path
from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None
    
    def is_last(self) -> bool:
        return self.name[2] == "Z"


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
    
    current_nodes = [graph[n[0]] for n in node_list if n[0][2] == "A"]
    z_steps = []
    for node in current_nodes:
        # Compute the periodicity
        counter = 0
        z_steps_n = []
        instruction_id = 0
        num_instr = len(instructions)
        steps = {}
        while (node, instruction_id) not in steps:
            steps[(node, instruction_id)] = counter
            instruction = instructions[instruction_id]
            instruction_id = (instruction_id + 1) % num_instr
            if instruction == "L":
                node = node.left
            else:
                node = node.right
            counter += 1
            if node.is_last():
                z_steps_n.append(counter)
        print(f"PRE-LOOP: 0-{steps[(node, instruction_id)]-1}, LOOP: {steps[(node, instruction_id)]}-{counter - 1}, Z: {z_steps_n}")
        z_steps += z_steps_n
    
    # This is buggy. LCM is the solution, but there's nothing in the problem statement that tells LCM can be the solution.
    counter = lcm(*z_steps)
    print("LCM:", counter)
    return counter


if __name__ == '__main__':
    assert run(
        nodes=
        [
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)',
        ],
        instructions="LR",
    ) == 6
    
    with Path("aoc-8.txt").open() as f:
        lines = f.readlines()
    instructions = lines[0].strip()
    nodes = lines[2:]
    run(nodes, instructions)
