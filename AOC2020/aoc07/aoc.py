import regex as re
import numpy as np
from utils import read_lines_str

root_bag = "(\w+\s\w+) bags contain (.*)"
no_bag = "no other bags"
id_bags = "(\d+) (\w+\s\w+)"


values = read_lines_str("AOC2020/aoc07/input.txt", ch=None)


class Bag:
    bags = {}

    def __init__(self, name):
        self._name = name
        self._bags = {}

    def add_bags(self, num, name):
        if not name in Bag.bags:
            Bag.bags[name] = Bag(name)
        bag = Bag.bags[name]
        self._bags[name] = (bag, num)

    def contains(self, bg_name):
        return bg_name in self._bags

    def count_bags(self):
        all_num = 0
        for bg_name in self._bags:
            bg, num = self._bags[bg_name]
            all_num += num + num * bg.count_bags()
            print(f"main bag={self._name} contains {num} of {bg_name}")
        return all_num


def extract_bags(lines):
    for line in lines:
        main_bag, content = re.search(root_bag, line).groups()
        if not main_bag in Bag.bags:
            Bag.bags[main_bag] = Bag(main_bag)
        bg = Bag.bags[main_bag]
        if no_bag in content:
            continue
        items = content.split(",")
        for item in items:
            num, bag = re.search(id_bags, item).groups()
            # print(f"num={int(num)}, for {bag}")
            bg.add_bags(int(num), bag)


extract_bags(values)


bg_to_find = Bag.bags["shiny gold"]


def find_in_content(bag):
    d = {}
    for bag_name in Bag.bags:
        bg = Bag.bags[bag_name]
        if bg.contains(bag._name):
            d[bag_name] = bg
    return d


# part I
bags = find_in_content(bg_to_find)
num_bags = len(bags)

while True:
    lbags = len(bags)
    bags_cp = bags.copy()
    for bag_name in bags_cp:
        dict_bag = find_in_content(bags_cp[bag_name])
        bags.update(dict_bag)
    if lbags == len(bags):
        print(len(bags))
        break

# part II
print(bg_to_find.count_bags())