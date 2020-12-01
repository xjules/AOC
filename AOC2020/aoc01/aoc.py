from utils import read_lines_int


values = read_lines_int("AOC2020/aoc01/input.txt")
values = sorted(values)


def sum_to(alpha=2020, ind0=0, ind1=1):
    # part I
    while True:
        if (values[ind0] + values[ind1]) == alpha:
            print(f"RESULT: {ind0} {ind1}:", values[ind0] * values[ind1])
            return ind0, ind1
        elif (values[ind0] + values[ind1]) > alpha or ind1 == len(values) - 1:
            ind0 += 1
            ind1 = ind0 + 1
        else:
            ind1 += 1
    return None


# part I
sum_to(2020, 0, 1)

ind0 = 0
ind1 = 1
ind2 = 2
# part II
while True:
    indeces = sum_to(2020 - values[ind0], ind0 + 1, ind0 + 2)
    if bool(indeces):
        print(
            f"RESULT: {ind0} {indeces[0]} {indeces[1]}:",
            values[ind0] * values[indeces[0]] * values[indeces[1]],
        )
        break
    else:
        ind0 += 1
