import numpy as np
import os
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


    def __init__(self):
        self.rel_base = 0
        self.index = 0
        self.output_count = 0
        self.data = [0, 0, 0]
        self.droid = (30, 30)
        self.board = {}
        self.input = 0
        self.oxygen = None
        self.length = 0
        self.arr = {}

    def get_pos(self, input):

        dir = {
            NORTH: (0,1),
            SOUTH: (0,-1),
            WEST: (-1,0),
            EAST: (1, 0)
        }
        return (self.droid[0] + dir[input][0], self.droid[1] + dir[input][1])

    def read_info(self, val):
        idb = self.get_pos(self.input)
        self.board[idb] = val
        if val != WALL:
            self.droid = idb


    def update_stats(self):
        id = (self.data[0], self.data[1], )

    def check_board(self):
        for k in self.board:
            if self.board[k] ==  MOVED_OK:
                return False
            return True

    def compute_oxygen(self, x, y, t):
        id = (x, y)
        if id in self.arr:
            return 10000000
        if id in self.board:
            self.arr[id] = t
            if id == self.oxygen:
                return 10000000
            elif self.board[id] == WALL:
                return 10000000
            else:
                self.board[id] = 10
                if self.check_board():
                    return t

            a = self.compute_length(x + 1, y, t + 1)
            b = self.compute_length(x - 1, y, t + 1)
            c = self.compute_length(x   , y + 1, t + 1)
            d = self.compute_length(x   , y - 1, t + 1)
            return min(a,min(b,min(c,d)))
        else:
            return 10000000000

    def compute_length(self, x, y, l):
        id = (x, y)
        if id in self.arr:
            return 10000000
        if id in self.board:
            self.arr[id] = l
            if id == self.oxygen:
                print('Current l=',l)
                return l
            elif self.board[id] == WALL:
                return 10000000
            a = self.compute_length(x + 1, y, l + 1)
            b = self.compute_length(x - 1, y, l + 1)
            c = self.compute_length(x   , y + 1, l + 1)
            d = self.compute_length(x   , y - 1, l + 1)
            return min(a,min(b,min(c,d)))
        else:
            return 10000000000
        

    def get_distance(self, _input):
        l = 0
        pos = self.start
        while True:
            p = _input[pos]
            if pos == self.oxygen:
                return l 
            dir = {
                NORTH: (0,1),
                SOUTH: (0,-1),
                WEST: (-1,0),
                EAST: (1, 0)
            }
            pos = (pos[0] + dir[p][0],pos[1] + dir[p][1])
            l += 1



    def draw_board(self):
        a = np.ones((2*self.start[0], 2*self.start[1]), dtype=np.int32)
        for id in self.board:
            a[id] = self.board[id]
        a[self.droid] = 3
        a[self.start] = 5
        if self.oxygen is not None:
            a[self.oxygen] = 4
        _d = {
            WALL: '#',
            MOVED_OK: '.',
            3: 'D',
            4: 'O',
            5: 'S'
        }
        os.system('clear')
        for iy in range(a.shape[0]):
            for ix in range(a.shape[1]):
                print(_d[a[(ix, iy)]], end='')
            print('')

    def compute(self, arr):
        self.index = 0
        output = []
        #Step number, direction, 
        self.start = self.droid
        _inputs = {self.droid: NORTH}
        while True:
            operator = arr[self.index]
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
                    a = arr[arr[self.index+1]]
                elif mode_a == Modes.IM_MODE:
                    a = arr[self.index+1]
                elif mode_a == Modes.REL_MODE:
                    a = arr[arr[self.index+1]+self.rel_base]

                if mode_b == Modes.POS_MODE:
                    b = arr[arr[self.index + 2]]
                elif mode_b == Modes.IM_MODE:
                    b = arr[self.index + 2]
                elif mode_b == Modes.REL_MODE:
                    b = arr[arr[self.index + 2]+self.rel_base]
                
            except:
                print('missing parameters for {}'.format(arr[self.index]))

            def store_output(offset, val, mode=mode_c):
                if mode == Modes.POS_MODE:
                    arr[arr[self.index+offset]] = val
                elif mode == Modes.REL_MODE:
                    arr[arr[self.index+offset]+self.rel_base] = val

            if operator == 99:
                return (output, arr)
            elif operator == 1:
                store_output(3, a + b)
                self.index += 4
            elif operator == 2:
                store_output(3, a * b)
                self.index += 4
            elif operator == 3:
                self.input = _inputs[self.droid]
                # print('SENDING INPUT {}'.format(_inputs))
                store_output(1, self.input, mode_a)
                self.index += 2
            elif operator == 4:
                self.read_info(a)
                if a == WALL:
                    _inputs[self.droid] += 1
                    if _inputs[self.droid] == 5:
                        _inputs[self.droid] = NORTH
                elif a == MOVED_OK:
                    if self.droid in _inputs:
                        _inputs[self.droid] += 1
                        if _inputs[self.droid] == 5:
                            _inputs[self.droid] = NORTH
                    else:
                        _inputs[self.droid] = NORTH
                    self.length += 1
                    if self.droid == self.start:
                        self.length = 0
                else:
                    
                    self.oxygen = self.droid
                    self.draw_board()
                    print('YES.... ', self.length)
                    # l = self.get_distance(_inputs)
                    l = self.compute_length(self.start[0], self.start[1], 0)
                    print('start to oxygen=', l)
                    l = self.compute_oxygen(self.oxygen[0], self.oxygen[1], 0)
                    print('time to re-oxygen=', l)
                    return True
                # print('DROID_POS: ', self.droid)
                # self.draw_board()
                # output.append(a)
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
                raise Exception('Something Went wrong {} modes A:{} B:{}'.format(arr[self.index], mode_a, mode_b))

a = Amp()
a.compute(arr)



