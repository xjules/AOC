from utils import read_lines_str
import numpy as np

comands = read_lines_str("AOC2021/aoc02/input.txt")


class Submarine:
    def __init__(self):
        self.H = 0
        self.D = 0
        self.aim = 0

    def do_steps(self, cmd):
        c, x = cmd.split()
        steps_depth = {"down": 1, "up": -1}
        steps_pos = {"forward": 1}
        if c in steps_depth:
            self.D += steps_depth[c] * int(x)
        elif c in steps_pos:
            self.H += steps_pos[c] * int(x)

    def do_steps_complex(self, cmd):
        c, x = cmd.split()
        steps_depth = {"down": 1, "up": -1}
        steps_pos = {"forward": 1}
        if c in steps_depth:
            self.aim += steps_depth[c] * int(x)
        elif c in steps_pos:
            self.H += steps_pos[c] * int(x)
            self.D += self.aim * int(x)


def part_I(cmds):
    sub = Submarine()
    for cmd in cmds:
        sub.do_steps(cmd)
    print(sub.H * sub.D)


def part_II(cmds):
    sub = Submarine()
    for cmd in cmds:
        sub.do_steps_complex(cmd)
    print(sub.H * sub.D)


part_II(comands)
