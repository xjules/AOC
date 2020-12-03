from utils import read_lines_str
import regex as re

values = read_lines_str("AOC2020/aoc02/input.txt", ch=None)

reg_str = "(\d+)-(\d+) (\w): (\w*)"


def num_valid_passwords(passwords):
    valid_num = 0
    for password in passwords:
        low, high, char, passwd = re.search(reg_str, password).groups()
        if passwd.count(char) >= int(low) and passwd.count(char) <= int(high):
            valid_num += 1
    return valid_num


# part I
print(num_valid_passwords(values))


def num_valid_passwords_II(passwords):
    valid_num = 0
    for password in passwords:
        low, high, char, passwd = re.search(reg_str, password).groups()
        if ((passwd[int(low) - 1] == char) + (passwd[int(high) - 1] == char)) == 1:
            valid_num += 1
    return valid_num


# part II
print(num_valid_passwords_II(values))
