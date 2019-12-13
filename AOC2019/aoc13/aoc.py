import numpy as np
f = open('input.txt').readline()
arr = f.split(',')

# arr = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')
# arr = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(',')
# arr = '1102,34915192,34915192,7,4,7,99,0'.split(',')
# arr = '104,1125899906842624,99'.split(',')
# arr = '1102,34915192,34915192,7,4,7,99,0'.split(',')
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




class Amp:
    def __init__(self):
        self.rel_base = 0
        self.index = 0
        self.output_count = 0
        self.data = [0, 0, 0]
        self.padle = None
        self.ball = None
        # self.board = np.zeros((20,44), dtype=np.int32)
        self.blocks = []
        self.score = 0
        self.input = 0

    def read_info(self, val):
        self.data[self.output_count] = val
        self.output_count += 1
        self.output_count = self.output_count % 3
        if self.output_count == 0:
            print('UDPATEING STATS!!!')
            self.update_stats()

    def update_stats(self):
        id = (self.data[0], self.data[1], )
        if self.data[2] == 4:
            self.ball = id
        elif self.data[2] == 3:
            self.padle = id
        elif self.data[2] == 2:
            self.blocks.append(id)
        elif self.data[2] == 0:
            if id in self.blocks:
                self.blocks.remove(id)
        elif self.data[0] == -1:
            self.score = self.data[2]
        if len(self.blocks) == 0 and self.ball is not None and self.padle is not None:
            print('END GAME score ', self.score)

    def update_paddle(self):
        if self.padle is not None and self.ball is not None:
            if self.padle[0] < self.ball[0]:
                self.input = 1
            elif self.padle[0] > self.ball[0]:
                self.input = -1
            else:
                self.input = 0
        




    # def compute(self, arr, input):
    def compute(self, arr):
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
                store_output(1, self.input, mode_a)
                self.index += 2
            elif operator == 4:
                self.read_info(a)
                self.update_paddle()

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
arr[0] = 2
output, b = a.compute(arr)
# print(output)
# partI
# l = output[2::3]
# l = list(filter(lambda x: x==2, l))
# print(len(l))



