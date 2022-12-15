import re

import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc15/input.txt")

ll = []


class Beacon:
    beacons = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Beacon.beacons.append(self)

    def is_beacon(x, y):
        for b in Beacon.beacons:
            if b.x == x and b.y == y:
                return True
        return False


class Sensor:
    def __init__(self, x, y, beacon, idx):
        self.x = x
        self.y = y
        self.id = idx
        self.beacon = beacon
        self.min_span = self.get_span()

    def get_span(self):
        return abs(self.beacon.x - self.x) + abs(self.beacon.y - self.y) + 1

    def is_free(self, x, y):
        return (abs(x - self.x) + abs(y - self.y)) < self.min_span

    def not_free(self, row, g):
        for i in range(self.min_span):
            if not Beacon.is_beacon(self.x - i, row) and self.is_free(self.x - i, row):
                g[int(self.x - i)] = 1
            if not Beacon.is_beacon(self.x + i, row) and self.is_free(self.x + i, row):
                g[int(self.x + i)] = 1

    def search_border(self, sensors):
        def test_sensors(xx, yy):
            if xx < 0 or yy < 0:
                return False
            if xx > 4000000 or yy > 4000000:
                return False
            for s in sensors:
                if s == self:
                    continue
                if s.is_free(xx, yy):
                    return False
            return True

        for dx in range(self.min_span):
            y = self.y + self.min_span - dx
            x = self.x + dx
            if test_sensors(x, y):
                print(f"FOUND={x=} {y=}")
                return True

            y = self.y + self.min_span - dx
            x = self.x - dx
            if test_sensors(x, y):
                print(f"FOUND={x=} {y=}")
                return True

            y = self.y - self.min_span + dx
            x = self.x + dx
            if test_sensors(x, y):
                print(f"FOUND={x=} {y=}")
                return True

            y = self.y - self.min_span + dx
            x = self.x - dx
            if test_sensors(x, y):
                print(f"FOUND={x=} {y=}")
                return True


sensors = []
for v in values:
    xxx = re.findall("-?\d+", v)
    coor = [int(val) for val in xxx]
    b = Beacon(coor[2], coor[3])
    s = Sensor(coor[0], coor[1], b, len(sensors))
    sensors.append(s)


# g = {}
# for s in sensors:
#     s.not_free(2000000, g)
# print(len(g))

for s in sensors:
    s.search_border(sensors)
