import utils
import numpy as np
from copy import deepcopy
import networkx as nx


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc16/input.txt")
line = lines_raw[0]


hex_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet:
    version_sum = 0

    def __init__(self, word):
        self._word = word
        self._value = 0
        self._sub_packets = []
        self._type_op = -1
        self._loc = 0

    def parse(self):
        self._version = int(self._word[:3], 2)
        self._id = int(self._word[3:6], 2)
        Packet.version_sum += self._version
        # print(f"WORD={self._word} PACKET=ID {self._id} VERSION {self._version}")
        print("SUM: ", Packet.version_sum)
        if self._id == 4:
            return self.parse_lit_value(6)
        return self.parse_op(6)

    def eval(self):
        if self._id == 0:
            return np.sum([p.eval() for p in self._sub_packets])
        elif self._id == 1:
            return np.product([p.eval() for p in self._sub_packets])
        elif self._id == 2:
            return np.min([p.eval() for p in self._sub_packets])
        elif self._id == 3:
            return np.max([p.eval() for p in self._sub_packets])
        elif self._id == 4:
            return self._value
        elif self._id == 5:
            return int(self._sub_packets[0].eval() > self._sub_packets[1].eval())
        elif self._id == 6:
            return int(self._sub_packets[0].eval() < self._sub_packets[1].eval())
        elif self._id == 7:
            return int(self._sub_packets[0].eval() == self._sub_packets[1].eval())

    def parse_lit_value(self, loc):
        num = ""
        while True:
            num += self._word[loc + 1 : loc + 5]
            if self._word[loc] == "0":
                loc += 5
                break
            loc += 5
        self._value = int(num, 2)
        # print(f"ID {self._id} VALUE {self._value}")
        return loc

    def parse_op(self, loc):
        if self._word[loc] == "0":
            self._type_op = 0
            num = int(self._word[loc + 1 : loc + 15 + 1], 2)
            # print("DEBUG bits in subpackets ", num)
            loc += 16
            new_loc = loc
            while loc < new_loc + num:
                packet = Packet(self._word[loc:])
                self._sub_packets.append(packet)
                loc += packet.parse()
            return loc
        elif self._word[loc] == "1":
            self._type_op = 1
            num = int(self._word[loc + 1 : loc + 11 + 1], 2)
            # print("DEBUG num of subpackets ", num)
            loc += 12
            for i in range(num):
                packet = Packet(self._word[loc:])
                self._sub_packets.append(packet)
                loc += packet.parse()
            return loc


def part_I(arr):
    s = ""
    for c in arr:
        s += hex_table[c]
    p = Packet(s)
    p.parse()


def part_II(arr):
    s = ""
    for c in arr:
        s += hex_table[c]
    p = Packet(s)
    p.parse()
    print(p.eval())


# part_I(line)
part_II(line)
