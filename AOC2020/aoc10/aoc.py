import numpy as np
import math
from collections import Counter
from copy import deepcopy

from numpy.lib.function_base import diff
from utils import read_lines_int

values = read_lines_int("AOC2020/aoc10/input.txt")

values = np.array(values + [0] + [max(values) + 3])


# part I
def count_1_3_diff(vals):
    vals = np.sort(vals)
    difference = np.diff(vals)
    count = Counter(difference)
    return count[1] * count[3]


print(count_1_3_diff(values))
# part II
combs = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6: 24, 7: 44, 8: 81, 9: 149}


def count_arrangements2(vals):
    vals = np.sort(vals)
    diff0 = np.diff(vals)

    num_one = 0
    combs = []
    for a in diff0:
        if a == 1:
            num_one += 1
        elif num_one >= 1:
            combs.append(combs[num_one])
            num_one = 0
    return np.product(combs)


def count_arrangements(vals):
    vals = np.sort(vals)
    diff0 = list(np.diff(vals))
    list_conf = [(list(diff0), 0)]
    conf_count = 1
    conf_dict = {}
    while bool(list_conf):
        dl, id = list_conf.pop()
        for i in range(id, len(dl) - 1):
            _diff = deepcopy(dl)
            _sum_diff = _diff[i] + _diff[i + 1]
            if _sum_diff <= 3:
                _diff.pop(i)
                _diff[i] = _sum_diff
                conf_count += 1
                list_conf.append((_diff, i))
    return conf_count


print(count_arrangements2(values))