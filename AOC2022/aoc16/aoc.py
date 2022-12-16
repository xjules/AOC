import re
from copy import deepcopy

import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc16/test_input.txt")


class Valve:

    valves = {}

    def __init__(self, name, flow, valves):
        self.name = name
        self.flow = flow
        self.valves = [v.strip() for v in valves]
        Valve.valves[self.name] = self

    def print_valve(self):
        print(f"{self.name=} {self.flow=} {self.valves=}")


class Realization:

    realizations = {}

    def __init__(self, node, timer, press, open_set):
        self.steps = []
        self.open = deepcopy(open_set)
        self.node = node
        self.timer = timer
        self.press = press

    def new_real(self, node):
        return Realization(node, self.timer, self.press, self.open)

    def get_press(self):
        self.press += Valve.valves[self.node].flow * self.timer
        return self.press

    def do_node(self):
        print(f"DOING {self.node=} {self.timer=}")
        if self.timer == 0:
            return self.get_press()
        if Valve.valves[self.node].flow > 0 and self.node not in self.open:
            self.open_valve()
        ll = []
        for node in Valve.valves[self.node].valves:
            real = self.new_real(node)
            real.move_to(node)
            ll.append(real.do_node())
        self.press = max(ll) + self.press
        print(f"PRESS {self.press=}")
        return self.press

    def move_to(self, node):
        self.steps.append((node, "m"))
        self.node = node
        self.timer -= 1
        return self.timer

    def open_valve(self):
        self.steps.append((self.node, "o"))
        self.timer -= 1
        self.open.add(self.node)
        self.get_press()
        return self.timer

    def eval(self, timer):
        press = 0
        for s in self.steps:
            if s[2] == "o":
                timer -= 1
                press += timer * Valve.valves[s[0]]
        return press

    def add_realization(self):
        Realization.realizations[tuple(self.steps)] = self


first_valve = None

for v in values:
    data = v.split(";")
    _flow = re.findall("-?\d+", data[0])
    _name = data[0].split()[1]
    _valves = re.findall("(?<=valves).*", v)
    if len(_valves) == 0:
        _valves = re.findall("(?<=valve).*", v)
    _valves = _valves[0].strip().split(",")
    if first_valve is None:
        first_valve = _name
    v = Valve(_name, int(_flow[0]), _valves)


for key in Valve.valves:
    Valve.valves[key].print_valve()

node = first_valve

timer = 30

real = Realization(node, 30, 0, set())
print(real.do_node())
