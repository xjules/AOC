from utils import read_lines_str
from copy import deepcopy

values = read_lines_str("AOC2020/aoc11/input.txt", ch=None)
values = [list(v.strip()) for v in values]
_vals = deepcopy(values)
vals_out = deepcopy(values)


def check_adjacent(i, j, vals):
    count_taken = 0
    xmin = max(0, i - 1)
    xmax = min(len(vals[0]) - 1, i + 1)
    ymin = max(0, j - 1)
    ymax = min(len(vals) - 1, j + 1)
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if y == j and i == x:
                continue
            if vals[y][x] == "#":
                count_taken += 1
    return count_taken


def check_seat(i, j, vals):
    global vals_out
    if vals[j][i] == "L":
        if check_adjacent(i, j, vals) == 0:
            vals_out[j][i] = "#"
    elif vals[j][i] == "#":
        if check_adjacent(i, j, vals) >= 4:
            vals_out[j][i] = "L"


def check_taken(vals):
    return sum(["".join(v).count("#") for v in vals])


def print_map(vals):
    print("-------------------------")
    for v in vals:
        print(v)


# part I.
def fill_up_seats(vals):
    global vals_out
    rounds = 0
    while True:
        for i in range(0, len(vals[0])):
            for j in range(0, len(vals)):
                check_seat(i, j, vals)
        _old_taken = check_taken(vals)
        _taken = check_taken(vals_out)
        vals = deepcopy(vals_out)
        rounds += 1
        if _taken == _old_taken:
            print(_taken)
            return


fill_up_seats(_vals)

# part II.
def check_directions(i, j, vals):
    def count_diag(dx, dy):
        cnt = 0
        x = i
        y = j
        while (x < len(vals[0]) and y < len(vals)) and (x >= 0 and y >= 0):
            if i != x or j != y:
                if vals[y][x] == "#":
                    cnt += 1
                    return 1
                elif vals[y][x] == "L":
                    return 0
            x += dx
            y += dy
        return cnt

    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    count_taken = 0
    for dx, dy in dirs:
        count_taken += count_diag(dx, dy)
    return count_taken


def check_seat2(i, j, vals):
    global vals_out
    if vals[j][i] == "L":
        if check_directions(i, j, vals) == 0:
            vals_out[j][i] = "#"
    elif vals[j][i] == "#":
        if check_directions(i, j, vals) >= 5:
            vals_out[j][i] = "L"


vals_out = deepcopy(values)


def fill_up_seats_II(vals):
    global vals_out
    while True:
        for i in range(0, len(vals[0])):
            for j in range(0, len(vals)):
                check_seat2(i, j, vals)
        _old_taken = check_taken(vals)
        _taken = check_taken(vals_out)
        vals = deepcopy(vals_out)
        if _taken == _old_taken:
            print(_taken)
            return


fill_up_seats_II(_vals)
