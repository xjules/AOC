from utils import read_lines_str_stripped
import numpy as np

lines = read_lines_str_stripped("AOC2021/aoc03/input.txt")


def part_I(bits):
    num_bits = len(bits[0])
    counter = {idx: {i: 0 for i in range(num_bits)} for idx in range(2)}
    for l in bits:
        for idx, c in enumerate(l):
            counter[int(c)][idx] += 1

    # gamma rate and the epsilon rate
    gamma_rate = [
        "1" if counter[1][i] > counter[0][i] else "0" for i in range(num_bits)
    ]
    gamma_rate = int("".join(gamma_rate), 2)
    epsilon_rate = [
        "0" if counter[1][i] > counter[0][i] else "1" for i in range(num_bits)
    ]
    print(num_bits, epsilon_rate)
    epsilon_rate = int("".join(epsilon_rate), 2)
    print(gamma_rate * epsilon_rate)


def part_II(bits):
    num_bits = len(bits[0])

    def count_bits(num_list, id_bit):
        counter = {idr: [] for idr in ["0", "1"]}
        for num in num_list:
            counter[num[id_bit]].append(num)
        return counter

    def get_last_number(bit_list, pos_ret=True):
        idbit = 0
        while len(bit_list) > 1:
            cnt = count_bits(bit_list, idbit)
            if (len(cnt["1"]) >= len(cnt["0"])) == pos_ret:
                bit_list = cnt["1"]
            else:
                bit_list = cnt["0"]
            idbit += 1
        print(bit_list)
        return int("".join(bit_list[0]), 2)

    gamma_rate = get_last_number(bits, True)
    scrubber_rate = get_last_number(bits, False)
    print(gamma_rate, scrubber_rate, gamma_rate * scrubber_rate)


part_II(lines)
