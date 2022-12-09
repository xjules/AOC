import math

import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc09/input.txt")

pos = (0, 0)


class Head:
    def __init__(self, x, y, idx, tail=None):
        self._x = x
        self._y = y
        self._idx = idx

        self._tail = tail
        self.history = {}
        self.update_pos((0, 0))

    def set_dir_steps(self, d, steps):
        self.move_steps(d, steps)

    def move_steps(self, d, steps):
        d_dict = {
            "D": (0, -1),
            "U": (0, 1),
            "L": (-1, 0),
            "R": (1, 0),
        }
        for i in range(steps):
            self.update_pos(d_dict[d])
            if self._tail:
                self._tail.follow(self)

    def increase_count(self):
        idx = (self._x, self._y)
        self.history[idx] = self.history.get(idx, 0) + 1

    def print_history(self):
        print(f"{self._idx=}=({self._x}, {self._y})")
        if self._tail:
            self._tail.print_history()

    def update_pos(self, dxy):
        self._x += dxy[0]
        self._y += dxy[1]
        self.increase_count()

    def follow(self, other):
        dx = other._x - self._x
        dy = other._y - self._y
        if abs(dx) == 1 and abs(dy) == 1:
            pass
        elif abs(dx) == 0 and abs(dy) > 1:
            self.update_pos((0, np.sign(dy)))
        elif abs(dy) == 0 and abs(dx) > 1:
            self.update_pos((np.sign(dx), 0))
        elif abs(dy) > 1 and abs(dx) >= 1:
            self.update_pos((np.sign(dx), np.sign(dy)))
        elif abs(dx) > 1 and abs(dy) >= 1:
            self.update_pos((np.sign(dx), np.sign(dy)))
        if self._tail:
            self._tail.follow(self)


tail = Head(0, 0, 1)
head = Head(0, 0, 0, tail)
for line in values:
    d, steps = line.split()
    head.set_dir_steps(d, int(steps))

print(f"PART1 = {len(tail.history)}")


tail = Head(0, 0, 9)
head = tail
for i in range(8):
    head = Head(0, 0, 8 - i, head)
head = Head(0, 0, "H", head)

a = np.zeros((30, 30))

for idx, line in enumerate(values):
    d, steps = line.split()
    head.set_dir_steps(d, int(steps))
print(f"PART2 = {len(tail.history)}")
