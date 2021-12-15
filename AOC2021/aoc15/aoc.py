import utils
import numpy as np
from copy import deepcopy
import networkx as nx


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc15/input.txt")
lines_raw = [[int(a) for a in line] for line in lines_raw]
lines_raw = np.array(lines_raw)


class Cave:
    def __init__(self, arr):
        self._cave = arr
        self._sums = []
        self._xdim, self._ydim = arr.shape
        self._g = nx.Graph()

    def _arr(self, i, j):
        x = int(i / self._xdim)
        y = int(j / self._ydim)
        i = i % self._xdim
        j = j % self._ydim
        val = self._cave[(i, j)]
        return (val + (y * 5 + x)) % 9

    def build_bigger_cave(self, arr):
        _xdim, _ydim = arr.shape
        big_cave = np.zeros((_xdim * 5, _ydim * 5))
        for k in range(5):
            for l in range(5):
                col = _xdim * k
                row = _ydim * l
                for i in range(_xdim):
                    for j in range(_ydim):
                        point = col + i, row + j
                        val = self._cave[(i, j)] + k + l
                        if val >= 10:
                            val = val - 10 + 1
                        big_cave[point] = val
        self.short_path(big_cave)

    def short_path(self, arr):
        end_point = arr.shape[0] - 1, arr.shape[1] - 1
        G = nx.Graph()
        for i in range(end_point[0]):
            for j in range(end_point[1]):
                G.add_edge((i, j), (i + 1, j), weight=arr[(i + 1, j)] + arr[(i, j)])
                G.add_edge((i, j), (i, j + 1), weight=arr[(i, j + 1)] + arr[(i, j)])
        G.add_edge(
            (end_point[0] - 1, end_point[1]),
            end_point,
            weight=arr[end_point] + arr[(end_point[0] - 1, end_point[1])],
        )
        G.add_edge(
            (end_point[0], end_point[1] - 1),
            end_point,
            weight=arr[end_point] + arr[(end_point[0], end_point[1] - 1)],
        )

        path = nx.dijkstra_path(G, source=(0, 0), target=end_point)

        print(sum(arr[p] for p in path[1:]))


def part_I(arr):

    cave = Cave(arr)
    cave.short_path(arr)


def part_II(arr):
    cave = Cave(arr)
    cave.build_bigger_cave(arr)


part_I(lines_raw)
part_II(lines_raw)
