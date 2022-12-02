import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc02/input.txt")

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.


def get_points(h1, h2):
    pts_win = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }
    pts_sign = {"X": 1, "Y": 2, "Z": 3}
    return pts_win[h1][h2] + pts_sign[h2]


sum_pts = 0
for val in values:
    H1, H2 = val.split()
    sum_pts += get_points(H1, H2)

print(f"SUM points={sum_pts}")

# X means you need to lose,
# Y means you need to end the round in a draw, and
# Z means you need to win.


def get_points_pt2(h1, h2):
    tf_sign = {
        "A": {"X": "Z", "Y": "X", "Z": "Y"},
        "B": {"X": "X", "Y": "Y", "Z": "Z"},
        "C": {"X": "Y", "Y": "Z", "Z": "X"},
    }
    pts_win = {"X": 0, "Y": 3, "Z": 6}
    pts_sign = {"X": 1, "Y": 2, "Z": 3}
    return pts_sign[tf_sign[h1][h2]] + pts_win[h2]


sum_pts = 0
for val in values:
    H1, H2 = val.split()
    sum_pts += get_points_pt2(H1, H2)

print(f"SUM points={sum_pts}")
