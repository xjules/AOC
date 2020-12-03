from utils import read_lines_str
import networkx as nx

values = read_lines_str("AOC2020/aoc03/input.txt", ch=None)


dim_x = len(values[0]) - 1
dim_y = len(values)

print(dim_x, dim_y)


def num_hit_trees(tree_map, x_step, y_step):
    x_pos = 0
    y_pos = 0
    num_trees = 0
    while True:
        x_pos = (x_pos + x_step) % dim_x
        y_pos = y_pos + y_step
        if y_pos >= dim_y:
            return num_trees
        if tree_map[y_pos][x_pos] == "#":
            num_trees += 1


# part I.
print(f"Num trees:", num_hit_trees(values, 3, 1))

# part II.
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


# part II.
steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
_tree_mult = 1
for step in steps:
    _tree_mult *= num_hit_trees(tree_map=values, x_step=step[0], y_step=step[1])
print(_tree_mult)
