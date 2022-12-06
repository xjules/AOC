import numpy as np
from collections import deque
from utils import read_lines_str

values = read_lines_str("AOC2022/aoc06/input.txt")


def get_starter_pack(line):
    
    d = deque(maxlen=4)
    for ch_idx, ch in enumerate(line):
        d.append(ch)
        if len(d) == 4:
            s = set(d)
            if len(s) == 4:
                print(d)
                return ch_idx + 1
    return -1


def get_starter_msg(line):
    
    d = deque(maxlen=14)
    for ch_idx, ch in enumerate(line):
        d.append(ch)
        if len(d) == 14:
            s = set(d)
            if len(s) == 14:
                print(d)
                return ch_idx + 1
    return -1
        
        
        

for v in values:
    idx = get_starter_pack(v)
    idx = get_starter_msg(v)
    print(f"FOUND = {idx}")