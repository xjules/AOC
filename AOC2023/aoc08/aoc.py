import math
from collections import defaultdict

lines = [
    l.strip()
    .replace("(", "")
    .replace(")", "")
    .replace(",", "")
    .replace("=", "")
    .split()
    for l in open("AOC2023/aoc08/input.txt").readlines()
]


cmds = lines[0]

nodes = lines[2:]


d = {}
for l in nodes:
    d[l[0]] = (l[1], l[2])

# part I
# current_node = "AAA"
# steps = 0
# cmd_id = 0
# while current_node != "ZZZ":
#     if current_node == "ZZZ":
#         break

#     if cmd_id >= len(cmds[0]):
#         cmd_id = 0
#     cmd = cmds[0][cmd_id]
#     if cmd == "L":
#         current_node = d[current_node][0]
#         steps += 1
#     else:
#         current_node = d[current_node][1]
#         steps += 1
#     cmd_id += 1

# print(f"{steps=}")

s_nodes = [s for s in d if "A" in s]
print(s_nodes)


def count_steps(c_node):
    n = c_node
    steps = []
    c_steps = 0
    cmd_id = 0
    while True:
        if cmd_id >= len(cmds[0]):
            cmd_id = 0
        if "Z" in n:
            steps.append((n, c_steps))
            c_steps = 0
        if cmds[0][cmd_id] == "L":
            n = d[n][0]
            c_steps += 1
        else:
            n = d[n][1]
            c_steps += 1
        cmd_id += 1
        if len(steps) > 5:
            return steps


total_steps = []
for node in s_nodes:
    steps = count_steps(node)
    total_steps.append(steps[0][1])
    print(f"{node=}")
    print(steps)
    print("******************")


print(math.lcm(*total_steps))
