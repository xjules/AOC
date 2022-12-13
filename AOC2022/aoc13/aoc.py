import functools
import json

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc13/input.txt")


def parse_line(a):
    return json.loads(a)


def cmp_values(a, b):
    idx = 0
    while True:
        if idx < len(a) and idx < len(b):
            a_val = a[idx]
            b_val = b[idx]
            if isinstance(a_val, int) and isinstance(b_val, int):
                if a_val > b_val:
                    return -1
                elif a_val < b_val:
                    return 1
            elif isinstance(a_val, list) and isinstance(b_val, list):
                ret = cmp_values(a_val, b_val)
                if ret != 0:
                    return ret
            elif isinstance(a_val, int) and isinstance(b_val, list):
                ret = cmp_values([a_val], b_val)
                if ret != 0:
                    return ret
            elif isinstance(a_val, list) and isinstance(b_val, int):
                ret = cmp_values(a_val, [b_val])
                if ret != 0:
                    return ret
        elif len(a) < len(b):
            return 1
        elif len(a) > len(b):
            return -1
        else:
            return 0
        idx += 1
    return 0


def cmp2(a, b):
    return -1 * cmp_values(a, b)


idx = 0
l = []
pair_id = 1
lines = []
while True:
    if idx >= len(values):
        break
    l1 = parse_line(values[idx])
    l2 = parse_line(values[idx + 1])

    lines.append(l1)
    lines.append(l2)

    ret = cmp_values(l1, l2)
    if ret == 1:
        l.append(pair_id)
    idx += 3
    pair_id += 1

print(f"SUM id pairs={sum(l)}")
lines.append([[2]])
lines.append([[6]])

sorted_lines = sorted(lines, key=functools.cmp_to_key(cmp2))

idx1 = sorted_lines.index([[2]]) + 1
idx2 = sorted_lines.index([[6]]) + 1
print(idx1 * idx2)
