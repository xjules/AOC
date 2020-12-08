import regex as re
import numpy as np
from utils import read_lines_str

values = read_lines_str("AOC2020/aoc08/input.txt", ch=None)


class Cmd:
    acc = 0

    def __init__(self, opp, val):
        self._opp = opp
        self._val = val
        self._visited = False

    def execute(self):
        self._visited = True
        # print(f"{self._opp} = {self._val} | {Cmd.acc}")
        if self._opp == "acc":
            Cmd.acc += self._val
        elif self._opp == "jmp":
            return self._val
        return 1

    def copy(self):
        return Cmd(self._opp, self._val)

    def is_swapped(self):
        if self._opp == "nop":
            self._opp = "jmp"
            return True
        if self._opp == "jmp":
            self._opp = "nop"
            return True
        return False

    def __repr__(self) -> str:
        return f"{self._opp} {self._val} | Acc={Cmd.acc}"


prog = []
for id, line in enumerate(values):
    opp, val = line.split()
    if val.startswith("+"):
        val = int(val[1:])
    else:
        val = int(val)
    prog.append(Cmd(opp, val))

# part I
id_cmd = 0
while True:
    cmd = prog[id_cmd]
    if cmd._visited:
        print(Cmd.acc)
        break
    id_cmd += cmd.execute()


# part II
def exec_prog(program):
    id_cmd = 0
    Cmd.acc = 0
    while True:
        if id_cmd >= len(program):
            print(Cmd.acc)
            return True
        cmd = program[id_cmd]
        if cmd._visited:
            return False
        id_cmd += cmd.execute()


id_cmd = 0
while True:
    prog_cp = [p.copy() for p in prog]
    while not prog_cp[id_cmd].is_swapped():
        id_cmd += 1
    if exec_prog(prog_cp):
        break
    id_cmd += 1
