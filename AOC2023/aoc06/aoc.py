lines = [l.strip().split() for l in open("AOC2023/aoc06/input.txt").readlines()]
print(lines)

time_a = map(int, lines[0][1:])
dst_a = map(int, lines[1][1:])


def distance_greater_than(mls: int, max_dst: int):
    m = mls
    cnt = 0
    in_range = False
    while m >= 0:
        dst = (mls - m) * m
        if dst > max_dst:
            cnt += 1
            if not in_range:
                in_range = True
        elif in_range:
            return cnt
        m -= 1
    return cnt


mult = 1
for race in zip(time_a, dst_a):
    mult *= distance_greater_than(race[0], race[1])
print(mult)


bmnt = distance_greater_than(45988373, 295173412781210)
print(bmnt)
