from utils import read_lines_str_stripped
import numpy as np
import uuid


class Board:
    pass


lines_raw = read_lines_str_stripped("AOC2021/aoc04/input.txt")
draw_nums = [int(a) for a in lines_raw[0].split(",")]


class Board:
    def __init__(self, lines):
        self._id = uuid.uuid1()
        self.load_numbers(lines)

    def load_numbers(self, lines):
        self._mask = np.zeros((5, 5)).astype(np.int32)
        self._board = {
            int(a): (col, row)
            for row, line in enumerate(lines)
            for col, a in enumerate(line.split())
        }

    def check(self, num):
        if num in self._board:
            col, row = self._board[num]
            del self._board[num]
            self._mask[col, row] = 1
            if self._mask[col, :].sum() == 5 or self._mask[:, row].sum() == 5:
                print(sum([v for v in self._board]) * num)
                return True
        return False


def load_boards(lines):
    board_lines = []
    boards = []
    for line in lines[1:]:
        if line:
            board_lines.append(line)
        if len(board_lines) == 5:
            boards.append(Board(board_lines))
            board_lines = []
    return boards


def part_I(lines):
    boards = load_boards(lines)
    for num in draw_nums:
        for b in boards:
            if b.check(num):
                return True
    return False


def part_II(lines):
    boards = load_boards(lines)
    board_dict = {b._id: b for b in boards}
    for num in draw_nums:
        for b in boards:
            if b._id in board_dict:
                if b.check(num):
                    if len(board_dict) == 1:
                        print("THIS ONE WINS!")
                        return True
                    del board_dict[b._id]
    return False


part_II(lines_raw)
