import regex
import numpy as np
from utils import read_lines_str

values = read_lines_str("AOC2020/aoc06/input.txt", ch=None)

answer = None
group_sz = 0
ll = []
for line in values:
    line = line.strip()
    if bool(line):
        if answer is None:
            answer = {}
        for ch in line:
            if ch in answer:
                answer[ch] += 1
            else:
                answer[ch] = 1
        group_sz += 1
    else:
        answer["group_sz"] = group_sz
        ll.append(answer.copy())
        answer = None
        group_sz = 0

if bool(answer):
    answer["group_sz"] = group_sz
    ll.append(answer.copy())

# part I
sum_q = 0
for a in ll:
    sum_q += len(a)
print(sum_q)

# part II
sum_q = 0
for a in ll:
    sz = a["group_sz"]
    for key in a:
        if key == "group_sz":
            continue
        if a[key] == sz:
            sum_q += 1
print(sum_q)
