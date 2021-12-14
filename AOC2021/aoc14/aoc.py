import utils
import numpy as np
from copy import deepcopy
import re


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc14/input.txt")
polymer = lines_raw[0]

    

 

def part_I(arr):
    rules = [line.split("->")  for line in arr[2:]]
    rules = [(r[0].strip(), r[1].strip()) for r in rules]
    
    counts = {}
    
    def apply(rule_set, pmr):
        res = ""
        for a, b in zip(pmr[:-1], pmr[1:]):
            counts[a] = counts.get(a, 0) + 1
            res += a
            for rule in rule_set:
                if rule[0].startswith(a+b):
                    res += rule[1]
                    counts[rule[1]] = counts.get(rule[1], 0) + 1
        res += b
        counts[b] = counts.get(b, 0) + 1
        return res
    
    pmr = polymer
    for i in range(10):
        counts = {}
        pmr = apply(rules, pmr)
        

    counts = np.array(list(counts.items()))
    counts = counts[:,1].astype(int)
    print(counts.max() - counts.min())
        
    
def part_II(arr):
    rules = [line.split("->")  for line in arr[2:]]
    rules = {r[0].strip(): r[1].strip() for r in rules}
    c_counts = {}
    pair_count = {}
    
    pmr = polymer
    for a, b in zip(pmr[:-1], pmr[1:]):
        pair_count[a+b] = pair_count.get(a+b, 0) + 1
        c_counts[a] = c_counts.get(a, 0) + 1
    c_counts[b] = c_counts.get(b, 0) + 1
    
            
    def apply(rule_set, pairs, counts):
        new_pairs = deepcopy(pairs)
        _todo = []
        for rule_left, rule_right in rule_set.items():
            if rule_left in pairs:
                num_pairs = pairs[rule_left]
                w0 = rule_left[0] + rule_right
                w1 = rule_right + rule_left[1]
                _todo.append((w0, num_pairs))
                _todo.append((w1, num_pairs))
                counts[rule_right] = counts.get(rule_right, 0) + num_pairs
                del pairs[rule_left]
        for pair in _todo:
            pairs[pair[0]] = pairs.get(pair[0], 0) + pair[1]
        return pairs, counts
            
    for i in range(40):
        print(i)
        pair_count, c_counts = apply(rules, pair_count, c_counts)
    c_counts = np.array(list(c_counts.values()))
    print(c_counts.max() - c_counts.min())
    

    

part_I(lines_raw)
part_II(lines_raw)
