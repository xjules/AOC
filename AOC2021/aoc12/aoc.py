import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc12/test_input_2.txt")


def is_big_cave(node):
    return node[0].isupper()


def is_small_cave(node):
    return node[0].islower()


class Graph:
    def __init__(self):
        self._edges = {}
        self._visited = {}
        self._paths = []

    def add_edge(self, node1, node2):
        if node1 not in self._edges:
            self._edges[node1] = []
        if node2 not in self._edges:
            self._edges[node2] = []
        self._edges[node1].append(node2)
        self._edges[node2].append(node1)

    def visit(self, node, c_path, visited):
        # print(c_path + [node], visited)
        if node == "end":
            self._paths.append(c_path + [node])
        elif is_small_cave(node) and node in visited:
            return False
        else:
            _visited = deepcopy(visited)
            _visited[node] = _visited.get(node, 0) + 1
            for node_b in self._edges[node]:
                self.visit(node_b, c_path + [node], _visited)
        return True

    def visit2(self, node, c_path, visited):
        # print(c_path + [node], visited)
        if node == "end":
            self._paths.append(c_path + [node])
        elif node == "start" and node in visited:
            return False
        elif is_small_cave(node) and node in visited and visited[node] > 1:
            return False
        else:
            _visited = deepcopy(visited)
            _visited[node] = _visited.get(node, 0) + 1
            for node_b in self._edges[node]:
                self.visit(node_b, c_path + [node], _visited)
        return True


def part_I(arr):
    G = Graph()
    for line in arr:
        nodes = line.split("-")
        G.add_edge(nodes[0], nodes[1])
    print(G._edges)
    G.visit("start", [], {})
    print(len(G._paths))


def part_II(arr):
    G = Graph()
    for line in arr:
        nodes = line.split("-")
        G.add_edge(nodes[0], nodes[1])
    print(G._edges)
    G.visit2("start", [], {})
    print(G._paths)


# part_I(lines_raw)
part_II(lines_raw)
