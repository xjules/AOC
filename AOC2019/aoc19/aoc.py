import numpy as np
import os
import networkx as nx
f = open('input.txt').readline()
arr = f.split(',')

arr = [np.int64(a) for a in arr]
_sz = len(arr)
_arr = np.zeros(10000000, dtype=np.int64)
for i,a in enumerate(arr):
    _arr[i] = a
arr = _arr



def get_oppcode(val):
    return [int(d) for d in str(val)]


class Modes:
    POS_MODE = 0
    IM_MODE  = 1
    REL_MODE = 2

class Moves:
    NEUTRAL = 0
    LEFT = -1
    RIGHT = -1



WALL = 0
MOVED_OK = 1
MOVED_OXYGEN = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

class Amp:


    def __init__(self, arr):
        self.rel_base = 0
        self.index = 0
        self.output_count = 0
        self.data = [0, 0, 0]
        self.input = 0
        self.arr = arr
        self.G = nx.Graph()
        self.iter = self.compute()


    def read_info(self, val):
        idb = self.get_pos(self.input)
        self.board[idb] = val
        if val != WALL:
            self.droid = idb

    def get_pos_from_complex(self, cn):
        return int(cn.real), int(cn.imag)

    def next(self):
        return next(self.iter)

    def compute(self):
        self.index = 0
        output = []
        while True:
            operator = self.arr[self.index]
            mode_a = Modes.POS_MODE
            mode_b = Modes.POS_MODE
            mode_c = Modes.POS_MODE
            if operator>99:
                l = get_oppcode(operator)
                operator = l[-1]
                try:
                    if l[-3] == 1:
                        mode_a = Modes.IM_MODE
                    if l[-3] == 2:
                        mode_a = Modes.REL_MODE
                except:
                    pass
                try:
                    if l[-4] == 1:
                        mode_b = Modes.IM_MODE
                    if l[-4] == 2:
                        mode_b = Modes.REL_MODE
                except:
                    pass

                try:
                    if l[-5] == 2:
                        mode_c = Modes.REL_MODE
                except:
                    pass
            
            a, b = 0, 0
            
            try:
                if mode_a == Modes.POS_MODE:
                    a = self.arr[self.arr[self.index+1]]
                elif mode_a == Modes.IM_MODE:
                    a = self.arr[self.index+1]
                elif mode_a == Modes.REL_MODE:
                    a = self.arr[self.arr[self.index+1]+self.rel_base]

                if mode_b == Modes.POS_MODE:
                    b = self.arr[self.arr[self.index + 2]]
                elif mode_b == Modes.IM_MODE:
                    b = self.arr[self.index + 2]
                elif mode_b == Modes.REL_MODE:
                    b = self.arr[self.arr[self.index + 2]+self.rel_base]
                
            except:
                print('missing parameters for {}'.format(self.arr[self.index]))

            def store_output(offset, val, mode=mode_c):
                if mode == Modes.POS_MODE:
                    self.arr[self.arr[self.index+offset]] = val
                elif mode == Modes.REL_MODE:
                    self.arr[self.arr[self.index+offset]+self.rel_base] = val

            if operator == 99:
                yield (output, self.arr)
            elif operator == 1:
                store_output(3, a + b)
                self.index += 4
            elif operator == 2:
                store_output(3, a * b)
                self.index += 4
            elif operator == 3:
                store_output(1, self.input, mode_a)
                self.index += 2
            elif operator == 4:
                # self.read_info(a)
                yield a
                self.index += 2
            elif operator == 5:
                if a != 0:
                    self.index = b
                else:
                    self.index += 3
            elif operator == 6:
                if a == 0:
                    self.index = b
                else:
                    self.index += 3
            elif operator == 7:
                store_output(3, int(a<b))
                self.index += 4
            elif operator == 8:
                store_output(3, int(a==b))
                self.index += 4
            elif operator == 9:
                self.rel_base += a
                self.index += 2
                
            else:
                raise Exception('Something Went wrong {} modes A:{} B:{}'.format(self.arr[self.index], mode_a, mode_b))

a = Amp(arr)

# a.draw_board()

b = np.zeros((50, 50))
for ix,iy in np.ndindex(b.shape):
    a.input = ix
    c = a.next()
    a.input = iy
    c = a.next()
    if len(c) == 1:
        b[iy, ix] = a.next()
    print(c)
    import pdb; pdb.set_trace()

print(b)




