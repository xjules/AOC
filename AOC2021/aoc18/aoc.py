import utils
import numpy as np
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc18/test_input.txt")


class SnailFish:
    def __init__(self, line):
        self.line = line
        self.depth = 0
        self.fish = {i: [] for i in range(10)}

    def add_fish(self):
        self.depth += 1
        self.fish[self.depth].append([])

    def add_num(self, num):
        self.fish[self.depth][-1].append(num)

    def parse_fish(self):
        num_str = ""
        for c in self.line:
            if c == "[":
                self.add_fish()
            elif c == "]":
                if num_str != "":
                    self.add_num(int(num_str))
                    num_str = ""
                self.depth -= 1
            elif c == ",":
                if num_str != "":
                    self.add_num(int(num_str))
                    num_str = ""
            else:
                num_str += c
        print(self.fish)


def part_I(arr):
    for line in arr:
        sf = SnailFish(line)
        sf.parse_fish()


def part_II(arr):
    pass


part_I(lines_raw)
# part_II(line)
