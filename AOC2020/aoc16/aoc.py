from utils import read_lines_str
from copy import deepcopy
import regex as re
from itertools import product
from collections import Counter

values = read_lines_str("AOC2020/aoc16/input.txt", ch=None)
values = [v.strip() for v in values]


def apply_rules(vals):
    rule_reg = "([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
    rules = []
    apply_rule_on = False
    wrong_numbers = []
    for line in vals:
        if not bool(line) or "your ticket" in line:
            continue
        elif "nearby tickets" in line:
            apply_rule_on = True
        elif ":" in line:
            name, rule = line.split(":")
            print(rule)
            bb1mn, bb1mx, bb2mn, bb2mx = re.search(rule_reg, rule).groups()
            rules.append((name, int(bb1mn), int(bb1mx), int(bb2mn), int(bb2mx)))
        elif apply_rule_on:
            numbers = [int(v) for v in line.split(",")]

            for number in numbers:
                valid_rule = False
                for rule in rules:
                    if (number >= rule[1] and number <= rule[2]) or (
                        number >= rule[3] and number <= rule[4]
                    ):
                        valid_rule = True
                        break
                if not valid_rule:
                    wrong_numbers.append(number)
    return wrong_numbers


# part I
# wrong_numbers = apply_rules(values)
# print(wrong_numbers)
# print(sum(n for n in wrong_numbers))

# part II
def apply_rules_II(vals):
    rule_reg = "([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
    rules = []
    apply_rule_on = False
    valid_rules = {}
    valid_tickets = 0
    for line in vals:
        if not bool(line):
            continue
        elif "your ticket" in line:
            continue
        elif "nearby tickets" in line:
            apply_rule_on = True
        elif ":" in line:
            name, rule = line.split(":")
            bb1mn, bb1mx, bb2mn, bb2mx = re.search(rule_reg, rule).groups()
            rules.append((name, int(bb1mn), int(bb1mx), int(bb2mn), int(bb2mx)))
        elif apply_rule_on:
            numbers = [int(v) for v in line.split(",")]
            has_wrong_number = False
            for idx, number in enumerate(numbers):
                is_valid_rule = False
                for rule in rules:
                    if (number >= rule[1] and number <= rule[2]) or (
                        number >= rule[3] and number <= rule[4]
                    ):
                        is_valid_rule = True
                        break
                if not is_valid_rule:
                    has_wrong_number = True
            if not has_wrong_number:
                valid_tickets += 1
                for idx, number in enumerate(numbers):
                    for rule in rules:
                        if (number >= rule[1] and number <= rule[2]) or (
                            number >= rule[3] and number <= rule[4]
                        ):
                            if not idx in valid_rules:
                                valid_rules[idx] = []
                            valid_rules[idx].append(rule[0])

    while valid_rules:
        for col, v_rules in valid_rules.items():
            if len(v_rules) == 1:
                v_rules[0].field = col
                rules_set.append(v_rules[0])
        valid_rules = {
            k: [r for r in v if r not in rules_set]
            for k, v in valid_rules.items()
            if k not in [j.field for j in rules]

    def most_frequent(ll):
        return Counter(ll)

    print(valid_tickets)
    idx_counts = {}
    for idx in valid_rules:
        idx_counts[idx] = most_frequent(valid_rules[idx])

    def check_conf(idx, config, req_len, classes_used, current_conf):
        if idx > 15:
            print(f"current: {idx} classes={classes_used}")
        if not idx in config:
            print("*****************************")
            for c in current_conf:
                print(f"pos={c[0]} class={c[1]}")
            print("*****************************")
            return True
        for ticket_class in config[idx]:
            if (
                not (ticket_class in classes_used)
                and config[idx][ticket_class] == req_len
            ):
                check_conf(
                    idx + 1,
                    config,
                    req_len,
                    classes_used + [ticket_class],
                    current_conf + [(idx, ticket_class)],
                )
        return False

    check_conf(0, idx_counts, valid_tickets, [], [])


apply_rules_II(values)