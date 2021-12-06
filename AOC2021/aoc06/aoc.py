import utils
import numpy as np


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc06/input.txt")

fish = [int(a) for a in lines_raw[0].split(",")]


def fish_days(arr):
    new_fish = np.where([arr == 0])[1]
    dd = max(1, np.min(arr))
    arr = arr - dd
    if len(new_fish) > 0:
        arr[new_fish] = 6
        arr = np.hstack((arr, len(new_fish) * [8]))
    return arr, dd


def part_I(fish):
    arr = np.array(fish)
    days = 0
    while days < 80:
        arr, d = fish_days(arr)
        days += d
    print(len(arr))


def part_II(fish):
    fish_age = [0] * 9
    for f in fish:
        fish_age[f] += 1

    for i in range(256):
        new_fish = fish_age[0]
        fish_age[7] += new_fish
        fish_age = fish_age[1:] + [new_fish]
    print(sum(fish_age))


part_I(fish)
part_II(fish)
