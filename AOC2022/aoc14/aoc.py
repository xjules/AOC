import numpy as np

from utils import read_lines_str

values = read_lines_str("AOC2022/aoc14/test_input.txt")


def get_line(a, b):
    if b > a:
        return list(range(a, b + 1))
    else:
        return list(range(b, a + 1))


def draw_line(a, b, g):
    if a[0] == b[0]:
        for j in get_line(a[1], b[1]):
            g[a[0], j] = 1
    elif a[1] == b[1]:
        for j in get_line(a[0], b[0]):
            g[j, a[1]] = 1
    return g


ll = []


def do_sand(x, y, g, max_y):
    if y >= max_y:
        return False
    if g[x, y + 1] == 0:
        do_sand(x, y + 1, g, max_y)
    elif g[x - 1, y + 1] == 0:
        do_sand(x - 1, y + 1, g, max_y)
    elif g[x + 1, y + 1] == 0:
        do_sand(x + 1, y + 1, g, max_y)
    else:
        g[x, y] = 9
    return True


for line in values:
    rock_line = []
    pts = line.split("->")
    for a in pts:
        x = a.split(",")
        rock_line.append(int(x[0]))
        rock_line.append(int(x[1]))
    rock_l = np.array(rock_line).reshape(len(pts), -1)
    ll.append(rock_l)

min_x = np.min([a.min(0) for a in ll], 0)
max_x = np.max([a.max(0) for a in ll], 0)

grid = np.zeros((510, 10))

# draw lines
for l in ll:
    a = l[0]
    for idx, b in enumerate(l[1:]):
        grid = draw_line(a, b, grid)
        a = b


balls = 0
while True:
    if not do_sand(500, 0, grid, max_x[1]):
        print(f"{balls=}")
        break
    balls += 1
print(grid[490:, :].T)
# get sand
