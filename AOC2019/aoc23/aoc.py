import numpy as np
import os
# import networkx as nx
from collections import deque
from itertools import count

f = open('input.txt').readline()
arr = f.split(',')

arr = [np.int64(a) for a in arr]
# arr = dict(enumerate(arr))



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
        self.arr = dict(enumerate(arr.copy()))
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
                if len(self.input)==0:
                    self.input.append(-1)
                    store_output(1, self.input.popleft(), mode_a)
                    yield None
                else:
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
class Computer:
    computer = []
    idle_pc = set()
    def __init__(self, addr):
        self.addr = addr
        self.amp = Amp(arr, deque([self.addr]))
        self.packets = []

    def read_packet(self):
        a = next(self.amp)
        if a is not None:
            x = next(self.amp)
            y = next(self.amp)
            Computer.send_packet((a, x, y))
            return a
        else:
            # Computer.idle_pc.add(self.addr)
            return None        

    @classmethod
    def send_packet(cls, packet):
        id, x, y = packet
        print('DBG: ', id, x, y)
        if id==255:
            print('RESULTS: ', y)
        else:
            cls.computer[id].amp.input.append(x)
            cls.computer[id].amp.input.append(y)

    @classmethod
    def create_network(cls):
        cls.computer = [Computer(i) for i in range(50)]



Computer.create_network()
i = 0
while True:
    c = Computer.computer[i]
    if c.addr in Computer.idle_pc:
        # print(Computer.idle_pc)
        i = (i + 1) % 50
        continue
    else:
        print('HERERERERERRERER***********')
        print(c.addr, i)
        next_i = c.read_packet()
        if next_i is not None:
            i = next_i
            print('NEXT is ', i)
        else:
            print('NO NEXT!!!!!!')
            i = (i + 1) % 50

