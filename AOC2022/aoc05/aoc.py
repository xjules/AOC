import numpy as np
import re
from utils import read_lines_str

values = read_lines_str("AOC2022/aoc05/input.txt")


intervals = []

def get_crates(line, crates):
    ch_idx=0
    crate_idx=1
    while True:
        try:
            if line[ch_idx]=="[":
                crate_idx = int(ch_idx / 4) + 1
                crates[crate_idx].insert(0, line[ch_idx+1])
            ch_idx+=1
        except IndexError:
            break
    return crates

def apply_transition_part1(nums, crates):
    amount = int(nums[0])
    from_id = int(nums[1])
    to_id = int(nums[2])
    for i in range(amount):
        crate = crates[from_id].pop()
        crates[to_id].append(crate)
    return crates

def apply_transition_part2(nums, crates):
    amount = int(nums[0])
    from_id = int(nums[1])
    to_id = int(nums[2])
    ll = []
    for i in range(amount):
        crate = crates[from_id].pop()
        ll.insert(0, crate)
    for crate in ll:
        crates[to_id].append(crate)
    return crates
    
            
        


crates = {i:[]for i in range(1, 10)}
for val in values:
    if val.startswith("move"):
        nums = re.findall("\d+", val)
        crates = apply_transition_part2(nums, crates)
    else:
        crates = get_crates(val, crates)
    
print("".join([crates[idx][-1] for idx in crates]))
    