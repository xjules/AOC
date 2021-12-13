import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc13/input.txt")
field = []
fold = []
end_field = False
for line in lines_raw:
    if not end_field and line:
        field.append(list(map(int, line.split(","))))
    elif end_field and line:
        axis, val = line.split("=")
        fold.append((axis[-1], int(val)))
    else:
        end_field = True
        
field = np.array(field)
max_cor = np.max(field, axis=0)+1
doc = np.zeros(max_cor[::-1]).astype(np.int32)
doc[field[:,1], field[:,0]] = 1

def part_I(arr, folds):
    def folde_y(a, val):
        a[val-1::-1, :] += a[val+1:, :] 
        return a[:val, :]
    
    def folde_x(a, val):
        a[:, val-1::-1] += a[:, val+1:] 
        return a[:, :val]
    print(arr)
    for f in folds:
        if f[0] == "y":
            arr = folde_y(arr, f[1])
        elif f[0] == "x":
            arr = folde_x(arr, f[1])
        
        print(arr)
        print(len(arr[arr!=0]))
        break

def part_II(arr, folds):
    def folde_y(a, val):
        a[val-1::-1, :] += a[val+1:, :] 
        return a[:val, :]
    
    def folde_x(a, val):
        a[:, val-1::-1] += a[:, val+1:] 
        return a[:, :val]
    print(arr)
    for f in folds:
        if f[0] == "y":
            arr = folde_y(arr, f[1])
        elif f[0] == "x":
            arr = folde_x(arr, f[1])
        
        print(arr)
        print(len(arr[arr!=0]))
        
    idx = np.where(arr!=0)
    arr[idx]=1
    import matplotlib.pyplot as plt
    plt.imshow(arr)
    plt.show()


part_I(doc, fold)
part_II(doc, fold)
