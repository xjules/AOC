from io import open_code
import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc10/input.txt")

close_code = {
    ">": "<",
    "}": "{",
    ")": "(",
    "]": "[",
}
open_code = {
    "<": [],
    "{": [],
    "(": [],
    "[": [],
}
open_code_err = {
    "<": 25137,
    "{": 1197,
    "(": 3,
    "[": 57,
}
close_code_score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def check_line(line):
    last_open = []
    for c in line:
        if c in open_code:
            last_open.append(c)
        elif c in close_code:
            if len(last_open) > 0 and close_code[c] == last_open[-1]:
                last_open.pop()
            else:
                return open_code_err[close_code[c]]
    return 0


def score_line(line):
    last_open = []
    for c in line:
        if c in open_code:
            last_open.append(c)
        elif c in close_code:
            if len(last_open) > 0 and close_code[c] == last_open[-1]:
                last_open.pop()
    total_score = 0
    print(last_open)
    for c in last_open[-1::-1]:
        total_score = total_score * 5 + close_code_score[c]
    return total_score


def part_I(arr):
    print(sum(check_line(line) for line in arr))


def part_II(arr):
    arr = [line for line in arr if check_line(line) == 0]
    print(np.median([score_line(line) for line in arr]))


part_I(lines_raw)
part_II(lines_raw)
