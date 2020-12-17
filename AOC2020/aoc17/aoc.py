from utils import read_lines_str
from copy import deepcopy
from collections import Counter
import numpy as np

values = read_lines_str("AOC2020/aoc17/input.txt", ch=None)
values = [v.strip() for v in values]


# part I.
def create_grid(vals, extra_dim=10):
    dim_x = len(vals[0]) + 2 * extra_dim
    dim_y = len(vals) + 2 * extra_dim
    dim_z = 2 * extra_dim

    start = [extra_dim] * 3
    grid = np.zeros((dim_x, dim_y, dim_z))
    for row, line in enumerate(values):
        y = row + start[1]
        for col, value in enumerate(line):
            x = col + start[0]
            if value == "#":
                grid[x, y, start[2]] = 1
    return grid


def do_cycle(input_grid, start, end):
    output_grid = np.zeros_like(input_grid)
    for x in np.arange(start[0], end[0]):
        for y in np.arange(start[1], end[1]):
            for z in np.arange(start[2], end[2]):
                sum = input_grid[x - 1 : x + 2, y - 1 : y + 2, z - 1 : z + 2].sum()
                if input_grid[x, y, z] == 1 and sum in [3, 4]:
                    output_grid[x, y, z] = 1
                elif input_grid[x, y, z] == 0 and sum == 3:
                    output_grid[x, y, z] = 1
    return output_grid


# extra space
extra_dim = 20
grid = create_grid(values, extra_dim=extra_dim)
start = np.array([extra_dim] * 3)
# end = np.array(len(values[0]), len(values), 1)
end = start + np.array([len(values[0]), len(values), 1])
for i in range(6):
    start = start - 1
    end = end + 1
    grid = do_cycle(grid, start, end)

print(len(grid[grid == 1]))


# part II.
def create_grid4d(vals, extra_dim=10):
    dim_x = len(vals[0]) + 2 * extra_dim
    dim_y = len(vals) + 2 * extra_dim
    dim_z = 2 * extra_dim
    dim_w = 2 * extra_dim

    start = [extra_dim] * 4
    grid = np.zeros((dim_x, dim_y, dim_z, dim_w))
    for row, line in enumerate(values):
        y = row + start[1]
        for col, value in enumerate(line):
            x = col + start[0]
            if value == "#":
                grid[x, y, start[2], start[3]] = 1
    return grid


def do_cycle4d(input_grid, start, end):
    output_grid = np.zeros_like(input_grid)
    for x in np.arange(start[0], end[0]):
        for y in np.arange(start[1], end[1]):
            for z in np.arange(start[2], end[2]):
                for w in np.arange(start[3], end[3]):
                    sum = input_grid[
                        x - 1 : x + 2, y - 1 : y + 2, z - 1 : z + 2, w - 1 : w + 2
                    ].sum()
                    if input_grid[x, y, z, w] == 1 and sum in [3, 4]:
                        output_grid[x, y, z, w] = 1
                    elif input_grid[x, y, z, w] == 0 and sum == 3:
                        output_grid[x, y, z, w] = 1
    return output_grid


# extra space
extra_dim = 20
grid = create_grid4d(values, extra_dim=extra_dim)
start = np.array([extra_dim] * 4)
# end = np.array(len(values[0]), len(values), 1)
end = start + np.array([len(values[0]), len(values), 1, 1])
for i in range(6):
    start = start - 1
    end = end + 1
    grid = do_cycle4d(grid, start, end)

print(len(grid[grid == 1]))