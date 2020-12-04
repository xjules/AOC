import regex
from utils import read_lines_str

values = read_lines_str("AOC2020/aoc04/input_test_invalid.txt", ch=None)

fields = {
    "byr": None,
    "iyr": None,
    "eyr": None,
    "hgt": None,
    "hcl": None,
    "ecl": None,
    "pid": None,
    # "cid": None,
}
passports = []
passport = fields.copy()
for v in values:
    if ":" in v:
        l = [s.split(":") for s in v.split()]
        for item in l:
            passport[item[0]] = item[1]
    else:
        passports.append(passport.copy())
        passport = fields.copy()
# this's optional
passports.append(passport.copy())

# part I
def count_valid_passports():
    valid = 0
    for passport in passports:
        print(passport)
        if not None in passport.values():
            valid += 1
    return valid


print(count_valid_passports())


# Part II.
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def count_valid_passports_part_II():
    valid = 0
    for passport in passports:
        print(passport)
        if not None in passport.values():
            rule_byr = int(passport["byr"]) in range(1920, 2003)

            rule_iyr = int(passport["iyr"]) in range(2010, 2021)

            rule_eyr = int(passport["eyr"]) in range(2020, 2031)

            rule_hgt = False
            if passport["hgt"].endswith("cm"):
                rule_hgt = int(passport["hgt"][:-2]) in range(150, 194)
            if passport["hgt"].endswith("in"):
                rule_hgt = int(passport["hgt"][:-2]) in range(59, 77)

            reg_str = "(#[0-9a-f]{6})"
            rule_hcl = bool(regex.search(reg_str, passport["hcl"]))

            reg_str = "(amb|blu|brn|gry|grn|hzl|oth)"
            rule_ecl = (
                bool(regex.search(reg_str, passport["ecl"]))
                and len(passport["ecl"]) == 3
            )

            reg_str = "([0-9]{9})"
            rule_pid = bool(regex.search(reg_str, passport["pid"]))
            if (
                rule_byr
                and rule_eyr
                and rule_iyr
                and rule_hgt
                and rule_hcl
                and rule_ecl
                and rule_pid
            ):
                valid += 1

    return valid


print(count_valid_passports_part_II())