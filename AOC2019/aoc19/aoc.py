import numpy as np
import os
import networkx as nx
from collections import deque
from itertools import count

f = open('input.txt').readline()
arr = f.split(',')

arr = [np.int64(a) for a in arr]
arr = dict(enumerate(arr))



def get_oppcode(val):
    return [int(d) for d in str(val)]


class Modes:
    POS_MODE = 0
    IM_MODE  = 1
    REL_MODE = 2
class Amp:

    def __init__(self, arr, input = None):
        self.rel_base = 0
        self.index = 0
        self.input = input
        self.arr = arr.copy()
        self.iter = self.compute()

    def __next__(self):
        return next(self.iter)

    def __iter__(self):
        return self.iter

    def __getitem__(self, index):
        if index < 0:
            raise Exception('Negative access {}'.format(index))
        return self.arr[index]

    def __setitem__(self, index, val):
        self.arr[index] = val

    def compute(self):
        while True:
            operator = self[self.index]
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
                    a = self[self[self.index+1]]
                elif mode_a == Modes.IM_MODE:
                    a = self[self.index+1]
                elif mode_a == Modes.REL_MODE:
                    a = self[self[self.index+1]+self.rel_base]

                if mode_b == Modes.POS_MODE:
                    b = self[self[self.index + 2]]
                elif mode_b == Modes.IM_MODE:
                    b = self[self.index + 2]
                elif mode_b == Modes.REL_MODE:
                    b = self[self[self.index + 2]+self.rel_base]
                
            except:
                # print('missing parameters for {}'.format(self[self.index]))
                pass

            def store_output(offset, val, mode=mode_c):
                if mode == Modes.POS_MODE:
                    self[self[self.index+offset]] = val
                elif mode == Modes.REL_MODE:
                    self[self[self.index+offset]+self.rel_base] = val

            if operator == 99:
                return
            elif operator == 1:
                store_output(3, a + b)
                self.index += 4
            elif operator == 2:
                store_output(3, a * b)
                self.index += 4
            elif operator == 3:
                store_output(1, self.input.popleft(), mode_a)
                self.index += 2
            elif operator == 4:
                self.index += 2
                yield a
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
                raise Exception('Something Went wrong {} modes A:{} B:{}'.format(self[self.index], mode_a, mode_b))

# part I
b = np.zeros((50, 50))
sum_flags = 0
for ix, iy in np.ndindex(b.shape):
    amp = Amp(arr, deque([ix, iy]))
    beam = next(amp)
    sum_flags += beam
    if iy == 0:
        print('x={} y={} beam={} | sum={}'.format(ix, iy, beam, sum_flags))
print('res:', sum_flags)


#6191165
prev_first_x = 0
rows = []
for y in count(500):
    first_x = None
    if prev_first_x == None:
        prev_first_x = 0
    x = prev_first_x
    while True:
        input = deque([x, y])
        amp = Amp(arr, input)
        output = next(amp)
        if output:
            if first_x == None:
                first_x = x
                if rows:
                    x = rows[-1][1] - 1
        else:
            if first_x != None:
                rows.append((first_x, x))
                if len(rows) > 100:
                    smallest_x = rows[-1][0]
                    biggest_x = rows[-100][1]
                    if biggest_x-smallest_x >= 100:
                        print('res: ',smallest_x*10000+y-100+1)
                break
        x += 1
    prev_first_x = first_x




