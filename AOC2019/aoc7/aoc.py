import itertools
import traceback
f = open('input.txt').readline()
arr = f.split(',')

# arr = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')
arr = [int(a) for a in arr]

def get_oppcode(val):
    return [int(d) for d in str(val)]

class Amp:
    def __init__(self, id, phase, code):
        self.arr = code
        self.index = 0
        self.id = id
        self.input = None

    def compute(self, signal, init=False):
        self.input = signal
        if self.input is None:
            raise Exception('No input given')
        while True:
            operator = self.arr[self.index]
            im_mode_a = False
            im_mode_b = False
            if operator>99:
                l = get_oppcode(operator)
                operator = l[-1]
                try:
                    im_mode_a = l[-3] == 1
                except:
                    pass
                try:
                    im_mode_b = l[-4] == 1
                except:
                    pass
            a, b = 0, 0
            try:
                a = self.arr[self.index + 1] if im_mode_a else self.arr[self.arr[self.index + 1]]
                b = self.arr[self.index + 2] if im_mode_b else self.arr[self.arr[self.index + 2]]
            except:
                pass
            if operator == 99:
                print('exiting {} with index {} on input {}'.format(self.id, self.index, self.input))
                return
            elif operator == 1:
                self.arr[self.arr[self.index + 3]] = a + b
                self.index += 4
            elif operator == 2:
                self.arr[self.arr[self.index + 3]] = a * b
                self.index += 4
            elif operator == 3:
                if self.input is None:
                    raise Exception('No input')
                self.arr[self.arr[self.index+1]] = self.input
                self.index += 2
                self.input = None
                if init:
                    return
            elif operator == 4:
                self.index += 2
                return a
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
                self.arr[self.arr[self.index + 3]] = int(a < b)
                self.index += 4
            elif operator == 8:
                self.arr[self.arr[self.index + 3]] = int(a == b)
                self.index += 4
            else:
                raise Exception('Something Went wrong {} modes A:{} B:{}'.format(self.arr[self.index], im_mode_a, im_mode_b))

def get_thruster_output(code, phase):
        amps= []
        for i, s in enumerate(phase):
            a = Amp(i, s, code.copy())
            amps.append(a)
            a.compute(s, init=True)
        signal = 0
        init = False
        while True:
            try:
                for a in amps:
                    signal = a.compute(signal, init=init)
                output = signal
            except:
                return output
        return output
            

phase_init = [5, 6, 7, 8, 9]
l = list(itertools.permutations(phase_init))
max_phase = -1
max_output = -1
for p in l:
    output = get_thruster_output(arr, phase=p)
    if output > max_output:
        max_phase = p
        max_output = output

print(max_output, max_phase)
