import math

import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc10/test_input.txt")


class SingleCommand:
    def __init__(self, cmd):
        self.value = None
        self.cmd = "noop"
        self.cycles = 1
        if cmd.startswith("addx"):
            ss = cmd.split()
            self.cmd, self.value = ss[0], int(ss[1])
            self.cycles = 2

    def execute(self, X):
        if self.cmd == "addx":
            return self.value + X
        return X


class MainProgram:
    def __init__(self):
        self.X = 1
        self.cmds = {}
        self.cycle = 0

    def add_cmd(self, cmd):
        c = SingleCommand(cmd)
        self.cycle += c.cycles
        self.cmds[self.cycle] = c

    def signal_strength(self, cycle):
        return cycle * self.X
        # return self.X

    def execute(self, cycle):
        if cycle in self.cmds:
            self.X = self.cmds[cycle].execute(self.X)


p = MainProgram()
for v in values:
    p.add_cmd(v)
p.cycle = 0

keys = set([20, 60, 100, 140, 180, 220])
l = []
raster = np.zeros((6, 40))
for i in range(221):
    if i in keys:
        l.append(p.signal_strength(cycle=i))
        print(f"{p.X=} {i=}")
    p.execute(cycle=i)
print(l)
print(sum(l))
