import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc03/input.txt")


def char2index(a):
    if a.islower():
        return ord(a) - 96
    return ord(a.lower()) - 96 + 26


sum_pts = 0
for val in values:
    val = val.strip()
    n = int(len(val) / 2)
    comp_a, comp_b = set(val[:n]), set(val[n:])
    int_comp = comp_a.intersection(comp_b)
    for a in int_comp:
        sum_pts += char2index(a)

print(f"SUM 2 sets = {sum_pts}")

sum_pts = 0
sets = []
for val in values:
    val = val.strip()
    sets.append(set(val))
    if len(sets) == 3:
        int_comp = sets[0].intersection(sets[1]).intersection(sets[2])
        for a in int_comp:
            sum_pts += char2index(a)
        sets = []

print(f"SUM 3 sets = {sum_pts}")
