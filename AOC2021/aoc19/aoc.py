import utils
import numpy as np
from copy import deepcopy
import mayavi.mlab as mlab


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc19/test_input_2.txt")
scanners = {}
current_scanner = -1
for line in lines_raw:
    if line.startswith("--- scanner"):
        current_scanner += 1
        scanners[current_scanner] = []
    elif line:
        posX, posY, posZ = [int(a) for a in line.split(",")]
        scanners[current_scanner].append([posX, posY, posZ])
scanners = {scanner_id: np.array(scanners[scanner_id]) for scanner_id in scanners}

print(scanners[0])


def compute_dst(id):
    return np.array([np.sqrt(np.sum(beacone ** 2)) for beacone in scanners[id]])


def rotate_x(pts, dir):
    return np.array([pts[:, 0], pts[:, 2], dir * pts[:, 1]])


def rotate_z(pts, dir):
    return np.array([pts[:, 1], dir * pts[:, 0], pts[:, 2]])


def rotate_y(pts, dir):
    return np.array([dir * pts[:, 2], pts[:, 1], pts[:, 0]])


# print(scanners)


def part_I(arr):
    pass


def part_II(arr):
    pass


mlab.points3d(
    scanners[0][:, 0],
    scanners[0][:, 1],
    scanners[0][:, 2],
    np.ones(len(scanners[0][:, 0])),
    scale_factor=100,
)
mlab.show()
part_I(lines_raw)
# part_II(line)
