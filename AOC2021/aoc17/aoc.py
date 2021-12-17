import utils
import numpy as np
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc17/input.txt")
line = "target area: x=20..30, y=-10..-5"
xbox = [20, 30]
ybox = [-10, -5]

# x=169..206, y=-108..-68
xbox = [169, 206]
ybox = [-108, -68]

total_count = 0


class Probe:
    def __init__(self, vx, vy):
        self.vx = vx
        self.vy = vy
        self.x = 0
        self.y = 0
        self._xa = [self.x]
        self._ya = [self.y]
        self.inside = False

    def step(self):
        global total_count
        self.x += self.vx
        self.y += self.vy
        self._xa.append(self.x)
        self._ya.append(self.y)
        self.vx -= np.sign(self.vx)
        self.vy -= 1
        if (self.x >= xbox[0] and self.x <= xbox[1]) and (
            self.y >= ybox[0] and self.y <= ybox[1]
        ):
            if not self.inside:
                self.inside = True
                # print(f"Inside: POSX: {self.x} POSY: {self.y}")
                total_count += 1

    def velocity_unroll(self):
        max_steps = np.min(ybox)
        while self.y > ybox[0]:
            self.step()


x_start = 7
y_start = 2


def part_I(arr):

    probe = Probe(x_start, y_start)
    probe.velocity_unroll()

    def on_press(event):
        global x_start, y_start
        if event.key == "left":
            x_start -= 1
        elif event.key == "right":
            x_start += 1
        elif event.key == "up":
            y_start -= 1
        elif event.key == "down":
            y_start += 1

        ax.clear()
        probe = Probe(x_start, y_start)
        probe.velocity_unroll()
        ax.plot(probe._xa, probe._ya, "o--")
        print(np.max(probe._ya))
        rect = mpatches.Rectangle(
            (xbox[0], ybox[0]),
            width=(xbox[1] - xbox[0]),
            height=(ybox[1] - ybox[0]),
            fill=False,
            color="purple",
            linewidth=2,
        )
        plt.gca().add_patch(rect)
        plt.show()

    fig, ax = plt.subplots()
    rect = mpatches.Rectangle(
        (xbox[0], ybox[0]),
        width=(xbox[1] - xbox[0]),
        height=(ybox[1] - ybox[0]),
        fill=False,
        color="purple",
        linewidth=2,
    )
    fig.canvas.mpl_connect("key_press_event", on_press)
    plt.gca().add_patch(rect)
    plt.show()


def part_II(arr):
    for x in range(18, 365):
        for y in range(-110, 109):
            probe = Probe(x, y)
            probe.velocity_unroll()

    print(total_count)


# part_I(line)
part_II(line)
