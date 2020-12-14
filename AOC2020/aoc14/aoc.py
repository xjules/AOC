from utils import read_lines_str
from copy import deepcopy
import regex as re
from itertools import product

values = read_lines_str("AOC2020/aoc14/input.txt", ch=None)
values = [v.strip() for v in values]


mem_re = "mem\[([0-9]+)\] = ([0-9]+)"

current_mask = None
mem_dict = {}


def write_values(mask, address, value):
    global mem_dict
    bin_str = bin(int(value))[2:]
    bin_str = "0" * (36 - len(bin_str)) + bin_str
    res_l = []
    for maskb, valb in zip(mask, bin_str):
        if maskb == "X":
            res_l.append(valb)
        else:
            res_l.append(maskb)
    mem_dict[address] = "".join(res_l)


for v in values:
    if "mask" in v:
        current_mask = v.split()[-1]
    elif "mem" in v:
        addr, value = re.search(mem_re, v).groups()
        write_values(current_mask, addr, value)

# part I
print(sum(int(mem_dict[addr], 2) for addr in mem_dict))

mem_dict = {}
# part II
def write_values_2(mask, address, value):
    global mem_dict
    bin_addr = bin(int(address))[2:]
    bin_addr = "0" * (36 - len(bin_addr)) + bin_addr
    res_l = []
    for maskb, addb in zip(mask, bin_addr):
        if maskb in ["X", "1"]:
            res_l.append(maskb)
        else:
            res_l.append(addb)
    addr = "".join(res_l)

    num_x = addr.count("X")
    for comb in product(["0", "1"], repeat=num_x):
        idx = 0
        real = []
        for bit in addr:
            if bit != "X":
                real.append(bit)
            else:
                real.append(comb[idx])
                idx += 1
        real = "".join(real[::-1])
        mem_dict[real] = int(value)


for v in values:
    if "mask" in v:
        current_mask = v.split()[-1]
    elif "mem" in v:
        addr, value = re.search(mem_re, v).groups()
        write_values_2(current_mask, addr, value)

print(sum(mem_dict[addr] for addr in mem_dict))