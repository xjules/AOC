from os import times
from utils import read_lines_str
from copy import deepcopy
import numpy as np

values = read_lines_str("AOC2020/aoc13/input.txt", ch=None)
values = [v.strip() for v in values]

timestart = int(values[0])
buses = []
for busid in values[1].split(","):
    if busid == "x":
        continue
    buses.append(int(busid))

# part I.
def get_first_busid(bus_list):
    depart_time = []
    for bus in bus_list:
        ntime = int(timestart / bus)
        left = timestart % bus
        if left > 0:
            depart_time.append(bus * (ntime + 1) - timestart)
        else:
            depart_time.append(bus * (ntime) - timestart)

    idbus = np.argmin(np.array(depart_time))
    return bus_list[idbus] * depart_time[idbus]


# print(get_first_busid(buses))
# values = [[], "17,x,13,19"]  # 3417
# values = [[], "67,7,59,61"]  # 754018
# values = [[], "67,7,x,59,61"]  # 1261476
# values = [[], "67,x,7,59,61"]  # 779210
# values = [[], "1789,37,47,1889"]  # 1202161486
#  part II.
buses = []
t_delta = []
for t, busid in enumerate(values[1].split(",")):
    if busid == "x":
        continue
    buses.append(int(busid))
    t_delta.append(t)


print(buses, t_delta)


def get_common_timestamp(bus_list, delta):
    a = np.array(bus_list)
    b = np.array(delta)
    bus_id = 1
    step = a[0]
    timestamp = step
    while True:
        c = np.mod(timestamp + b, a)
        if c[bus_id] == 0:
            _ts = timestamp + step
            while (_ts + b[bus_id]) % a[bus_id] != 0:
                _ts += step
            step = _ts - timestamp
            bus_id += 1
        if np.all(c == 0):
            return timestamp
        timestamp += step


print(get_common_timestamp(buses, t_delta))
