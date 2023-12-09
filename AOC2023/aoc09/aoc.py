import numpy as np

# lines = [l.strip().split() for l in open("AOC2023/aoc09/test_input.txt").readlines()]
lines = [l.strip().split() for l in open("AOC2023/aoc09/input.txt").readlines()]


def predict_history(l):
    a = np.array([int(i) for i in l])

    b = a
    ll = [a]
    while True:
        b = np.diff(b)
        ll.append(b)
        if np.abs(b).sum() == 0:
            break
    ll = ll[::-1]

    # part II
    s = 0
    for a in ll:
        s = a[0] - s
    return s

    # part I
    # s = 0
    # for a in ll:
    #     s += a[-1]
    # return s


s = 0
for l in lines:
    s += predict_history(l)
print(s)
