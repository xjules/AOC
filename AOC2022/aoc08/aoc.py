import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc08/input.txt")


grid = [[int(val) for val in line.strip()] for line in values]
grid = np.array(grid).astype(np.int32)

visible = np.zeros((len(grid), len(grid[0]))).astype(np.int32)
score = np.zeros((len(grid), len(grid[0]))).astype(np.int32)

visible[:, [0, -1]] = 1
visible[[0, -1], :] = 1


def is_visible(i, j, g):
    all_smaller_0 = g[:j, i] < g[j, i]
    if np.all(all_smaller_0):
        return 1
    all_smaller_1 = g[j + 1 :, i] < g[j, i]
    if np.all(all_smaller_1):
        return 1
    all_smaller_2 = g[j, :i] < g[j, i]
    if np.all(all_smaller_2):
        return 1
    all_smaller_3 = g[j, i + 1 :] < g[j, i]
    if np.all(all_smaller_3):
        return 1
    return 0


def get_score(i, j, g):
    def count_smaller(l):
        if i == 1 and j == 1:
            print(l)
        cnt = 0
        for smaller in l:
            cnt += 1
            if not smaller:
                break
        return cnt

    all_smaller_0 = [g[:j, i] < g[j, i]][0][::-1]
    all_smaller_1 = g[j + 1 :, i] < g[j, i]
    all_smaller_2 = [g[j, :i] < g[j, i]][0][::-1]
    all_smaller_3 = g[j, i + 1 :] < g[j, i]
    return (
        count_smaller(all_smaller_0)
        * count_smaller(all_smaller_1)
        * count_smaller(all_smaller_2)
        * count_smaller(all_smaller_3)
    )


for y in range(1, grid.shape[0] - 1):
    for x in range(1, grid.shape[1] - 1):
        visible[y, x] = is_visible(y, x, grid)

print(f"SUM visible={np.sum(visible)}")


for y in range(1, grid.shape[0] - 1):
    for x in range(1, grid.shape[1] - 1):
        score[y, x] = get_score(y, x, grid)

print(score)
print(f"SUM max size={np.max(score)}")
