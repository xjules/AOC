from utils import read_lines_int
import numpy as np

values = read_lines_int("AOC2021/aoc01/input.txt")


def part_I():
    a = np.diff(np.array(values))
    print(len(a[(a > 0)]))


def part_II():
    a = np.array(values)
    b = a[0:-2] + a[1:-1] + a[2:]
    b = np.diff(b)
    print(len(b[(b > 0)]))


part_I()
part_II()
