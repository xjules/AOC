from io import open_code
import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc11/input.txt")
lines_raw = [[int(a) for a in line] for line in lines_raw]
lines_raw = np.array(lines_raw)
print(lines_raw.shape)


class Cave:
    def __init__(self, arr):
        self._arr = arr
        self._xdim, self._ydim = arr.shape
        self._flash_count = 0
        self._flash_local = 0

    def do_step(self):
        self._arr += 1
        self.flash()
        idx = np.where(self._arr > 9)
        self._arr[idx] = 0

    def flash(self):
        idx = np.where(self._arr == 10)
        if len(idx[0]) > 0:
            stack = list(zip(idx[0], idx[1]))
            # print(stack)
            self._flash_local = 0
            while len(stack) > 0:
                i, j = stack.pop()
                self._flash_count += 1
                self._flash_local += 1
                min_i = max(0, i - 1)
                min_j = max(0, j - 1)
                max_i = min(self._xdim, i + 2)
                max_j = min(self._ydim, j + 2)
                for x in range(min_i, max_i):
                    for y in range(min_j, max_j):
                        if x != i or y != j:
                            self._arr[x, y] += 1
                            if self._arr[x, y] == 10:
                                stack.append((x, y))
            return True
        return False


def part_I(arr):
    cave = Cave(arr)
    for step in range(100):
        cave.do_step()

    print(cave._flash_count)


def part_II(arr):
    cave = Cave(arr)
    for step in range(1000):
        cave.do_step()
        if cave._flash_local == 100:
            print("STEP: ", step + 1, cave._flash_local)
            print("**********************")
            break


part_I(lines_raw)
part_II(lines_raw)
