import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc04/input.txt")


def get_interval(str_int):
    a, b = str_int.split("-")
    a, b = int(a), int(b)
    return a, b


def in_interval(int_a, int_b):
    if int_a[0] >= int_b[0] and int_a[1] <= int_b[1]:
        return True
    return False


def is_overlap(int_a, int_b):
    if int_a[0] >= int_b[0] and (int_a[1] <= int_b[1] or int_a[0] <= int_b[1]):
        return True
    return False


intervals = []

for val in values:
    val = val.strip()
    int_a, int_b = val.split(",")
    int_a = get_interval(int_a)
    int_b = get_interval(int_b)
    intervals.append((int_a, int_b))

count_itx = 0
for int_a, int_b in intervals:
    if in_interval(int_a, int_b) or in_interval(int_b, int_a):
        count_itx += 1

print(f"PART-I SUM intx = {count_itx}")


count_itx = 0
for int_a, int_b in intervals:
    if is_overlap(int_a, int_b) or is_overlap(int_b, int_a):
        count_itx += 1

print(f"PART-II SUM intx = {count_itx}")
