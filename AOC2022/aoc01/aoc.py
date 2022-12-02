from utils import read_lines_str
import numpy as np

values = read_lines_str("AOC2022/aoc01/input.txt")

elf = []
cal = 0
for val in values:
    try:
        cal += int(val)
    except ValueError:
        elf.append(cal)
        cal = 0
if cal>0:
    elf.append(cal)
print(f"MAX CAL={max(elf)}")


np_elf = np.array(elf)
max_tree = np.sum(np.sort(np_elf)[::-1][:3])
print(f"MAX 3 CAL sum={max_tree}")

