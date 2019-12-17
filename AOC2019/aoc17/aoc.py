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

UP = 94
DOWN = 118
LEFT = 60
RIGHT = 62
SCAFFOLD = 35
SPACE = 46
EOL = 10
X = 88
COMMA = 44
key_L = ord('L')
key_R = ord('R')
key_y = ord('y')
key_n = ord('n')


class Amp:


    def __init__(self):
        self.rel_base = 0
        self.index = 0
        self.output_count = 0
        self.data = [0, 0, 0]
        self.pos = (0, 0)
        self.board = {}
        self.input = 0
        self.oxygen = None
        self.length = 0
        self.arr = {}
        self.map = []
        self._str = ''
        self.width = 0
        self.robot = None

    def get_pos(self, input):

        dir = {
            UP: (0,1),
            DOWN: (0,-1),
            LEFT: (-1,0),
            RIGHT: (1, 0)
        }
        pass

    def read_info(self, val):
        ch = chr(val)
        self._str += ch
        if val == EOL:
            self.pos = (0, self.pos[1] + 1)
        else:
            # print('POS=',self.pos)
            self.pos = (self.pos[0] + 1, self.pos[1])
            self.map.append(val)
        # print('=================================')
        # print(self._str)

    def callibrate(self):
        print(self._str)
        self.width = 59
        print('len(map)={} WIDTH={}'.format(len(self.map),self.width))
        a = np.array(self.map, dtype=np.int32).reshape(-1, self.width)
        ydim = a.shape[0]
        xdim = a.shape[1]
        print(a.shape)
        sum_call = 0
        self.robot = (58, 18)
        print('DBG: ', a[18,:])
        for ix in range(1, xdim-1):
            for iy in range(1, ydim-1):
                if a[iy, ix] == SCAFFOLD and a[iy-1, ix] == SCAFFOLD and a[iy+1, ix] == SCAFFOLD and a[iy, ix-1] == SCAFFOLD and a[iy, ix+1] == SCAFFOLD:
                    sum_call += ix * iy
                if a[iy, ix] in [UP, DOWN, LEFT, RIGHT]:
                    print('DBG robot pos:', self.robot)
                    self.robot = (ix, iy)
        return sum_call

    def get_graph(self):
        self.width = 59
        a = np.array(self.map, dtype=np.int32).reshape(-1, self.width)
        ydim = a.shape[0]
        xdim = a.shape[1]
        print(a.shape)
        self.robot = (58, 18)
        self.G = nx.Graph()
        for ix in range(0, xdim):
            for iy in range(0, ydim):
                if a[iy, ix] == SCAFFOLD:
                    ida = str('{},{}'.format(ix,iy))
                    if iy > 0 and a[iy-1, ix] == SCAFFOLD:
                        idb = str('{},{}'.format(ix,iy-1))
                        self.G.add_edge(ida, idb)

                    if iy < ydim-1 and a[iy+1, ix] == SCAFFOLD:
                        idb = str('{},{}'.format(ix,iy+1))
                        self.G.add_edge(ida, idb)

                    if ix > 0 and a[iy, ix-1] == SCAFFOLD:
                        idb = str('{},{}'.format(ix-1,iy))
                        self.G.add_edge(ida, idb)

                    if ix < xdim-1 and a[iy, ix+1] == SCAFFOLD:
                        idb = str('{},{}'.format(ix+1,iy))
                        self.G.add_edge(ida, idb)
        ida = str('{},{}'.format(self.robot[0],self.robot[1]))
        idb = str('{},{}'.format(self.robot[0]-1,self.robot[1]))
        self.G.add_edge(ida, idb)
        return self.G



    def update_stats(self):
        id = (self.data[0], self.data[1], )



    def draw_board(self):
        print(self._str)

    def compute(self, arr):
        self.index = 0
        output = []
        #Step number, direction, 
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
                self.input = 1
                # print('SENDING INPUT {}'.format(_inputs))
                store_output(1, self.input, mode_a)
                self.index += 2
            elif operator == 4:
                self.read_info(a)
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
print('RES: ',  a.callibrate())

G = a.get_graph()
source = '58,18'
l = list(nx.dfs_edges(G, source=source))
def compile_list(ll):
    nl = []
    for edge in ll:
        ax,ay = (int(x) for x in edge[0].split(','))
        bx,by = (int(x) for x in edge[1].split(','))

        if ax < bx:
            nl.append('R')
        if ax > bx:
            nl.append('L')
        if ay < by:
            nl.append('U')
        if ay > by:
            nl.append('D')
    return nl

nl = compile_list(l)

def compress_list(ll):
    nl = []
    ch = ll[0]
    rep_num = 1
    for a in ll[1:]:
        if a == ch:
            rep_num +=1
        else:
            nl.append([ch, rep_num])
            rep_num = 1
            ch = a
    nl.append([ch, rep_num])
    return nl


print(nl)
print('*************')
nl = compress_list(nl)
print(nl)



