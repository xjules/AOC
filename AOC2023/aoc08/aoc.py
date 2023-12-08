from collections import defaultdict

# lines = [l.strip().split() for l in open("AOC2023/aoc07/test_input.txt").readlines()]
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

print(cmds)
print(nodes)


d = {}
for l in nodes:
    d[l[0]] = (l[1], l[2])

current_node = "AAA"
steps = 0
cmd_id = 0
while current_node != "ZZZ":
    if current_node == "ZZZ":
        break

    if cmd_id >= len(cmds[0]):
        cmd_id = 0
    cmd = cmds[0][cmd_id]
    if cmd == "L":
        current_node = d[current_node][0]
        steps += 1
    else:
        current_node = d[current_node][1]
        steps += 1
    cmd_id += 1

print(f"{steps=}")
