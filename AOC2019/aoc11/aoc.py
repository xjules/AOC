import numpy as np
f = open('input.txt').readline()
arr = f.split(',')

# arr = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')
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


class Amp:
    def __init__(self):
        self.rel_base = 0
        self.index = 0
        self.x = 50
        self.y = 50
        self.orient = 1
        self.board = np.zeros((2*self.x, 2*self.y), dtype=np.int32)
        self.mask = np.zeros((2*self.x, 2*self.y), dtype=np.int32)
        self.dict_board = {}
        self.color_type = True
        self.input = 1
        self.first_time = True


    def handle(self, a):
        _pos = (self.x, self.y, )
        if self.color_type:
            self.dict_board[_pos] = a
        elif self.color_type is False:
            if a == 1:
                self.orient += 1
            elif a == 0:
                self.orient -= 1
            self.orient = self.orient % 4 
            _d= {0: (self.x-1, self.y), 
                 1: (self.x, self.y+1),
                 2: (self.x+1, self.y),
                 3: (self.x, self.y-1)}
            self.x, self.y = _d[self.orient]
            # print('turn={} orient={} x={} y={}'.format(a, self.orient, self.x, self.y))
            

    def compute(self, arr, input=None):
        self.index = 0
        output = []
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
                    # a = arr[arr[self.index+1]+self.rel_base]
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
                print('done!!!')
                return (output, arr)
            elif operator == 1:
                store_output(3, a + b)
                self.index += 4
            elif operator == 2:
                store_output(3, a * b)
                self.index += 4
            elif operator == 3:
                if self.first_time and input is not None:
                    self.input = input
                    self.first_time = False
                else:
                    self.input = 0
                if (self.x, self.y, ) in self.dict_board:
                    self.input = self.dict_board[(self.x, self.y, )]
                store_output(1, self.input, mode_a)
                self.index += 2
            elif operator == 4:
                output.append(a)
                self.handle(a)
                self.color_type = not self.color_type
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



if __name__ == "__main__":
    a = Amp()
    output, b = a.compute(arr, input=0)
    num_keys = len(a.dict_board.keys())
    print(num_keys)

    board = np.zeros((200, 200), dtype=np.int32)
    for k in a.dict_board:
        board[k[0], k[1]] = a.dict_board[k]
        if a.dict_board[k] == 1:
            print('painted white')


import matplotlib.pyplot as plt
plt.imshow(np.rot90(board[:,:]))
plt.show()