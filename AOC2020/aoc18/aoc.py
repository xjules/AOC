from utils import read_lines_str
from copy import deepcopy
import regex as re
import networkx as nx

values = read_lines_str("AOC2020/aoc18/input.txt", ch=None)
values = [v.strip() for v in values]


def eval_expression(term, depth=0):
    global_value = {}
    operator = {}

    def apply_value(value, _depth):
        if not depth in global_value:
            global_value[_depth] = value
        elif bool(operator[_depth]):
            if operator[_depth] == "+":
                global_value[_depth] += value
            elif operator[_depth] == "*":
                global_value[_depth] *= value

    for id, item in enumerate(term):
        if item.isnumeric():
            apply_value(int(item), depth)
        elif item in ["+", "*"]:
            operator[depth] = item
        elif item == "(":
            depth += 1
        elif item == ")":
            depth -= 1
            apply_value(global_value[depth + 1], depth)
            del global_value[depth + 1]

    return global_value


# part I
print(sum([eval_expression(v)[0] for v in values]))


# part II.
def eval_expression2(term, depth=0):
    global_value = {}
    operator = {}

    def apply_value(value, _depth):
        if not depth in global_value:
            global_value[_depth] = [value]

        elif bool(operator[_depth]):
            op = operator[_depth][-1]
            if op == "+":
                global_value[_depth][-1] += value
                operator[_depth].pop()
            elif op == "*":
                global_value[_depth].append(value)

    def collect(_depth):
        value = global_value[_depth][0]
        for val in global_value[_depth][1:]:
            value *= val
        return value

    for id, item in enumerate(term):
        if item.isnumeric():
            apply_value(int(item), depth)
        elif item in ["+", "*"]:
            if not depth in operator:
                operator[depth] = [item]
            else:
                operator[depth].append(item)
        elif item == "(":
            depth += 1
        elif item == ")":
            depth -= 1
            val = collect(depth + 1)
            del global_value[depth + 1]
            del operator[depth + 1]
            apply_value(val, depth)
    global_value[0] = collect(depth)
    return global_value


print(sum([eval_expression2(v)[0] for v in values]))