from utils import read_lines_str
from copy import deepcopy


class Ship:
    rotate = {
        "L": -1,
        "R": 1,
    }
    move_cmd = {"W": 2, "E": 0, "N": 3, "S": 1}

    def __init__(self):
        self.heading = 0
        self.steps = {0: 0, 1: 0, 2: 0, 3: 0}
        self.waypoint = {0: 10, 1: 0, 2: 0, 3: 1}
        # self.y_steps = 0

    def add_steps(self, cmd, value):
        if cmd in Ship.rotate:
            self.heading += Ship.rotate[cmd] * value / 90
            self.heading %= 4
        elif cmd in Ship.move_cmd:
            self.steps[Ship.move_cmd[cmd]] += value
        elif cmd == "F":
            self.steps[self.heading] += value


values = read_lines_str("AOC2020/aoc12/input.txt", ch=None)
values = [v.strip() for v in values]
# part I
ship = Ship()
for v in values:
    cmd, value = v[0], int(v[1:])
    ship.add_steps(cmd, value)
ew_pos = ship.steps[0] - ship.steps[2]
ns_pos = ship.steps[3] - ship.steps[1]
print(abs(ew_pos) + abs(ns_pos))

# part II
class Ship2:
    move_cmd = {"W": (0, -1), "E": (0, 1), "N": (1, 1), "S": (1, -1)}

    def __init__(self):
        # (0, 1) - east
        # (0, -1) - west
        # (1, 1) - north
        # (1, -1) - south
        self.pos = [0, 0]
        self.waypoint = {0: 10, 1: 1}

    def add_steps(self, cmd, value):
        if cmd == "L":
            _new_waypoint = deepcopy(self.waypoint)
            for i in range(int(value / 90)):
                _new_waypoint[0] = -self.waypoint[1]
                _new_waypoint[1] = self.waypoint[0]
                self.waypoint = deepcopy(_new_waypoint)
        elif cmd == "R":
            _new_waypoint = deepcopy(self.waypoint)
            for i in range(int(value / 90)):
                _new_waypoint[0] = self.waypoint[1]
                _new_waypoint[1] = -self.waypoint[0]
                self.waypoint = deepcopy(_new_waypoint)
        elif cmd in Ship2.move_cmd:
            axis, dir = Ship2.move_cmd[cmd]
            self.waypoint[axis] += dir * value
        elif cmd == "F":
            self.pos[0] += self.waypoint[0] * value
            self.pos[1] += self.waypoint[1] * value


ship = Ship2()
for v in values:
    cmd, value = v[0], int(v[1:])
    ship.add_steps(cmd, value)

print(abs(ship.pos[0]) + ship.pos[1])