import regex
import numpy as np
from utils import read_lines_str

values = read_lines_str("AOC2020/aoc05/input.txt", ch=None)


def get_seat(min_val, max_val, code, pos, LH="F", UH="B"):
    if min_val == max_val - 1:
        return min_val
    mid_val = min_val + int((max_val - min_val) / 2)
    if code[pos] == LH:
        return get_seat(min_val, mid_val, code, pos + 1, LH, UH)
    elif code[pos] == UH:
        return get_seat(mid_val, max_val, code, pos + 1, LH, UH)
    raise ValueError("Out of characters. Something went wrong!")


def test_seat_id():
    row = get_seat(0, 128, "BFFFBBF", 0, "F", "B")
    column = get_seat(0, 8, "RRR", 0, "L", "R")
    assert row * 8 + column == 567


l = []
for line in values:
    row_code = line[:7]
    col_code = line[7:]
    row = get_seat(0, 128, row_code, 0, "F", "B")
    column = get_seat(0, 8, col_code, 0, "L", "R")
    l.append(row * 8 + column)

# part I
print(max(l))

# part II
seats = np.sort(np.array(l))
ids = np.diff(seats) > 1
print(seats[:-1][ids] + 1)
