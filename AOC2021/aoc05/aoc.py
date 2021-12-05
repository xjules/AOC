import utils
import numpy as np


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc05/input.txt")

points = (line.split("->") for line in lines_raw)


class Board:
    def __init__(self, pts):
        self._points = self.process_pts(pts)

    def process_pts(self, pts):
        points = []
        for pt0, pt1 in pts:
            x = [int(v) for v in pt0.split(",")]
            y = [int(v) for v in pt1.split(",")]
            points.append((x, y))
        return np.array(points).astype(np.int32)

    def _line(self, ax, ay, bx, by):
        mnx = min(ax, bx)
        mny = min(ay, by)
        mxx = max(ax, bx)
        mxy = max(ay, by)
        for x in range(mnx, mxx + 1):
            for y in range(mny, mxy + 1):
                self._canvas[x, y] += 1

    def _line_diag(self, ax, ay, bx, by):
        sx = -1 if ax > bx else 1
        sy = -1 if ay > by else 1
        for x, y in zip(range(ax, bx + sx * 1, sx), range(ay, by + sy * 1, sy)):
            self._canvas[x, y] += 1

    def draw_lines(self, part_2=False):
        maxy = np.max(self._points[:, :, 1])
        maxx = np.max(self._points[:, :, 0])
        self._canvas = np.zeros((maxx + 1, maxy + 1)).astype(np.int32)
        delta_pts = np.diff(self._points, axis=1)
        for idx, dp in enumerate(delta_pts):
            if 0 in dp[0]:
                self._line(
                    self._points[idx][0][0],
                    self._points[idx][0][1],
                    self._points[idx][1][0],
                    self._points[idx][1][1],
                )
            elif part_2:
                self._line_diag(
                    self._points[idx][0][0],
                    self._points[idx][0][1],
                    self._points[idx][1][0],
                    self._points[idx][1][1],
                )


def part_I(pts):
    board = Board(pts)
    board.draw_lines(part_2=False)
    print(len(board._canvas[board._canvas >= 2]))


def part_II(pts):
    board = Board(pts)
    board.draw_lines(part_2=True)
    print(len(board._canvas[board._canvas >= 2]))


part_II(points)
