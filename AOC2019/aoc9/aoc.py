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


class Amp:
    def __init__(self):
        self.rel_base = 0
        self.index = 0

    def compute(self, arr, input):
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
                return (output, arr)
            elif operator == 1:
                store_output(3, a + b)
                self.index += 4
            elif operator == 2:
                store_output(3, a * b)
                self.index += 4
            elif operator == 3:
                store_output(1, input, mode_a)
                self.index += 2
            elif operator == 4:
                output.append(a)
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
output, b = a.compute(arr, 2)
print("SOLUTION:", output)