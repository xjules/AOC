import numpy as np
f = open('input.txt').readline()

w = 25
h = 6
p = [int(a) for a in f.strip()]
a = np.array(p).reshape(-1, w*h)

#part-I
idx = np.where(a==0)
vals, counts = np.unique(idx[0], return_counts=True)
id_layer = vals[counts.argmin()]
b = a[id_layer]
print('num len 1 * len 2=',len(b[b==1]) * len(b[b==2]))
#part II
idx=0
image = a[idx].copy()
while True:
    idx +=1
    transparent = np.where(image==2)[0]
    if len(transparent)==0 or idx>=a.shape[0]:
        break
    b = a[idx]
print(image.reshape(h, w))

