import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str("AOC2021/aoc08/input.txt")


num_code = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def part_I(arr):
    cnt = 0
    for line in arr:
        _input, _output = line.split("|")
        for sig_output in _output.split():
            if len(sig_output) in [2, 3, 4, 7]:
                cnt += 1
    print(cnt)


def part_II(arr):
    code_c = {c: set() for c in "abcdefg"}
    _len_code_c = {
        2: ["c", "f"],
        3: ["a", "c", "f"],
        4: ["b", "d", "c", "f"],
        7: ["a", "b", "c", "d", "e", "f", "g"],
    }

    def _check(_sz, _sig, code_dict):
        _code_c = deepcopy(code_dict)
        for sig in _sig.split():
            if len(sig) == _sz:
                for c in _len_code_c[_sz]:
                    if _code_c[c]:
                        _code_c[c] = _code_c[c].intersection(set(sig))
                    else:
                        set_sig = set(sig)
                        for _c in code_dict:
                            if c != _c:
                                set_sig = set_sig - code_dict[_c]
                        _code_c[c] = code_dict[c].union(set(set_sig))
        for c in _code_c:
            if len(_code_c[c]) == 1:
                for a in _code_c:
                    if a != c:
                        _code_c[a] = _code_c[a] - _code_c[c]
        return _code_c

    val = 0
    for line in arr:
        _input, _output = line.split("|")
        code_c = {c: set() for c in "abcdefg"}
        code_c = _check(2, _input, code_c)
        code_c = _check(3, _input, code_c)
        code_c = _check(4, _input, code_c)
        code_c = _check(7, _input, code_c)
        num_str = ""
        for i in _output.split():
            num = set()
            for d in code_c:
                if code_c[d].issubset(set(i)):
                    num.add(d)

            for key in num_code:
                if num.issubset(set(key)) and len(i) == len(key):
                    num_str += str(num_code[key])
                    break
        val += int(num_str)
    print(val)


part_II(lines_raw)
