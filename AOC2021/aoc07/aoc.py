import utils
import numpy as np


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc07/input.txt")

crabs = [int(a) for a in lines_raw[0].split(",")]


def part_I(arr):
    print(int(np.abs((np.median(arr) - np.array(arr))).sum()))


def part_II(arr):
    mean = int(np.mean(arr))
    diff_arr = np.abs(mean - np.array(arr)).astype(np.int32)
    dst = lambda x: np.sum(np.arange(x) + 1)
    print(sum(dst(x) for x in diff_arr))


part_I(crabs)
part_II(crabs)
