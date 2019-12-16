import numpy as np
import numba
from numba.typed import Dict
from numba import types
f = open('input.txt').readline().strip()
arr = [int(c) for c in f]

SIZE = len(arr)

kernel = np.array([0, 1, 0, -1])
# d_k = {}
# d_k = Dict.empty(key_type=types.int32, value_type=types.int32[:])
d_k = [kernel.copy()]

# d_k[0] = kernel

@numba.jit
def get_kernel(pos_kernel, knl, dict_kernel):
    if pos_kernel in dict_kernel:
        return dict_kernel[pos_kernel].flatten()
    a = dict_kernel[pos_kernel-1]
    dict_kernel[pos_kernel] = np.dstack((a, knl)).copy()
    return dict_kernel[pos_kernel].flatten()

@numba.jit
def get_last_digit(a):
    return np.int32(a[-1])

# @numba.njit(['int32[:], int32[:]', parallel=True)
# @numba.njit(nopython = True, parallel = False, nogil = True)
# @numba.jit(nopython=True)
def multiply(a, knl):
    output = np.empty_like(a)
    # kk = np.copy(knl)
    for i in range(SIZE):
        
        # up_knl = get_kernel(i, knl, dict_kernel)
        up_knl = np.repeat(knl, i+1)
        rep_motives = len(a) // len(up_knl) + 1

        b = np.tile(up_knl, rep_motives).flatten()
        d = b[1:len(a)+1]
        c = np.str(np.sum(a[d == 1]) - np.sum(a[d==-1]))[-1]
        output[i] = int(c)
        # c = np.dot(b[1:len(a)+1], a).astype(str)
        # print('****************====', i)
        # print(b[1:len(a)+1])
        # print(a)
        # output[i] = get_last_digit(c)
        # print('=',output[i])
        # print('****************====', i)
        # print(output)
    return output

def multiply_wm(a, PLS, MNS):
    output = np.empty_like(a)
    # kk = np.copy(knl)
    for i in range(SIZE):
        c = np.str(np.sum(a[PLS[i]]) - np.sum(a[MNS[i]]))[-1]
        output[i] = int(c)
    return output

res = np.array(arr)[:]
res = np.tile(res, 10000).flatten()
print(res)

@numba.jit
def precompute(a):
    s = np.sum(a)
    l = [s % 10]
    for i in range(0, len(a)-1):
        s -= a[i]
        l.append(s % 10)
    return np.array(l).copy()

size_2 = len(res) // 2

idx = 5972731 - size_2
# idx = 303673 - size_2
aa = res[size_2:]

for i in range(100):
    aa = precompute(aa)


print('RESULT: ', aa[idx:idx+8])


#part I
# @numba.jit
# def do_all(inarr, knl, dict_knl):
#     for i in range(100):
#         inarr = multiply(inarr, knl.copy())
#         print('STEP=',i)
#     return inarr.copy()
# res = do_all(res, kernel, d_k)
# print(res)





