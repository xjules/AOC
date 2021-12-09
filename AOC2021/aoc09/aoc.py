import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc09/input.txt")
cols = len(lines_raw[0])
hf = [int(a) for l in lines_raw for a in l]
hf = np.array(hf).reshape(-1, cols)


class HeightField:
    def __init__(self, hf):
        self._hf = hf
        self._labels = np.zeros_like(self._hf)
        self._xdim, self._ydim = hf.shape

    def check_lowest(self, i, j, val):
        min_i = max(0, i - 1)
        min_j = max(0, j - 1)
        max_i = min(self._xdim - 1, i + 1)
        max_j = min(self._ydim - 1, j + 1)

        for x in range(min_i, max_i + 1):
            for y in range(min_j, max_j + 1):
                if x != i or y != j:
                    if val >= self._hf[x, y]:
                        return False
        return True

    def find_lowest(self):
        return [
            (x, y, val + 1)
            for (x, y), val in np.ndenumerate(self._hf)
            if self.check_lowest(x, y, val)
        ]

    def grow(self, x, y, label):
        if x < 0 or y < 0 or x >= self._xdim or y >= self._ydim:
            return
        if self._hf[x, y] == 9 or self._labels[x, y] != 0:
            return
        self._labels[x, y] = label
        self.grow(x - 1, y, label)
        self.grow(x + 1, y, label)
        self.grow(x, y - 1, label)
        self.grow(x, y + 1, label)

    def label(self):
        basins = self.find_lowest()
        sizes = []
        for id, basin in enumerate(basins):
            self.grow(basin[0], basin[1], id + 1)
            sizes.append(len(self._labels[self._labels == id + 1]))

        print(np.prod(np.sort(np.array(sizes))[-3:]))


def part_I(arr):
    hf = HeightField(arr)
    print(sum((v[2] for v in hf.find_lowest())))


def part_II(arr):
    hf = HeightField(arr)
    hf.label()


part_I(hf)
part_II(hf)
