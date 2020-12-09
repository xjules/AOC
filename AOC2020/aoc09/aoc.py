import numpy as np
from collections import deque
from copy import deepcopy
from utils import read_lines_int

values = read_lines_int("AOC2020/aoc09/input.txt")

preamble_numbers = deque()


class Preamble:
    def __init__(self, sz):
        self._sum = {}
        self._numbers = deque()
        self._sz = sz
        self._id = 0

    def add(self, number):
        for num in self._numbers:
            _sum = num + number
            if _sum not in self._sum:
                self._sum[_sum] = []
            self._sum[_sum].append((num, number))

        if self._id >= self._sz:
            num_to_pop = self._numbers.popleft()
            self.popnum(num_to_pop)

        self._numbers.append(number)
        self._id += 1

    def popnum(self, num):
        dd = deepcopy(self._sum)
        for key in self._sum:
            for vals in self._sum[key]:
                if num in vals:
                    dd[key].remove(vals)
            if not bool(dd[key]):
                del dd[key]
        self._sum = dd

    def is_sum(self, num):
        if self._id >= self._sz:
            # print(f"checking {num}")
            # print(f"dict = {self._sum}")
            if num in self._sum:
                return self._sum[num]
            return None
        return 1


# part I
preamble = Preamble(sz=25)
for number in values:
    if not bool(preamble.is_sum(number)):
        val = number
        print(number)
        break
    preamble.add(number)

# part II
start_x = 0
end_x = 1
sum = 0
values = np.array(values)
while True:
    while np.sum(values[start_x:end_x]) < val:
        end_x += 1
    if np.sum(values[start_x:end_x]) == val:
        print(np.min(values[start_x:end_x]) + np.max(values[start_x:end_x]))
        break
    else:
        start_x += 1
