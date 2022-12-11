import math
import queue
import re

import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc11/test_input.txt")


class Item:
    def __init__(self, level):
        self.level = level

    def div_3(self):
        self.level = int(self.level / 3)

    def mod_by(self, val):
        return self.level % val == 0


class Monkey:
    def __init__(self, idx):
        self.idx = idx
        self.items = queue.Queue()


monkeys = {}

current_idx = 0
for v in values:
    if v.startswith("Monkey"):
        _, idx = v.split()
        current_idx = int(idx)
        monkeys[current_idx] = Monkey(current_idx)
    elif "Starting items" in v:
        levels = re.findall("\d+", v)
        for level in levels:
            monkeys[current_idx].items.put(Item(int(level)))
