import numpy as np
from collections import deque
from utils import read_lines_str
from pathlib import PurePath

values = read_lines_str("AOC2022/aoc07/input.txt")


key_path = PurePath("/")
root = {key_path:None}
children = 1
for v in values:
    cmds = v.split()
    if cmds[0]=="$":
        if cmds[1]=="ls":
            root[key_path] = []
        elif cmds[1] == "cd":
            if cmds[2] == "..":
                key_path = key_path.parent
            elif cmds[2] == "/":
                key_path = PurePath("/")
            else:
                key_path = key_path / cmds[2]
    elif cmds[0] == "dir":
        root[key_path].append(("dir", cmds[1]))
    else:
        root[key_path].append((int(cmds[0]), cmds[1]))
        


sz_dict = {}

def get_size(cp, file_dict):
    sz = 0
    for node_type, node_name in file_dict[cp]:
        if isinstance(node_type, int):
            sz += node_type
        else:
            key = cp / node_name
            if key in sz_dict:
                sz += sz_dict[key]
            else:
                sz_dir = get_size(cp / node_name, file_dict)
                sz_dict[key] = sz_dir
                sz += sz_dir
    return sz
        

total_size = get_size(PurePath("/"), root)
print(total_size)
    
sz = 0
for key in sz_dict:
    if sz_dict[key] <= 100000:
        sz += sz_dict[key]
print(f"SUM = {sz}")


avail_space = 70000000 - total_size
freeup = 30000000-avail_space
print(f"AVAIL SPACE {avail_space} freeup {freeup}")
sz = 0
sizes = [(freeup - sz_dict[key], sz_dict[key]) for key in sz_dict]
sz = sorted(sizes)
for idx, (diff, full_size) in enumerate(sz):
    if diff > 0:
        print(f"SIZE to rem {sz[idx-1][1]}")
        break
    
        
    
        
                    