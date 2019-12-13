import numpy as np
import re
import math
f = open('input.txt').readlines()


class Moon:
    all = []
    def __init__(self, x, y, z, xv=0, yv=0, zv=0):
        self.x = x
        self.y = y
        self.z = z
        self.xv = xv
        self.yv = yv
        self.zv = zv
        self.po_en = 0
        self.ki_en = 0
        self.history = {}
        self.step = 0
        Moon.all.append(self)

    
    def record_step(self):
        id = (self.x, self.y, self.z, self.xv, self.yv, self.zv,)
        if id in self.history:
            self.history[id].append(self.step)
        else:
            self.history[id] = [self.step]


    def get_step(self):
        id = (self.x, self.y, self.z, self.xv, self.yv, self.zv,)
        return self.history.get(id, None)

    @classmethod
    def print_repr(cls):
        for m in cls.all:
            print('pos=<x={}, y={}, z={}> vel=<x={}, y={}, z={}>'.format(m.x, m.y, m.z, m.xv, m.yv, m.zv))
    @classmethod
    def update_vel_all(cls):
        for m in cls.all:
            for n in cls.all:
                if m!=n:
                    m.update_vel(n)
    @classmethod
    def update_pos_all(cls):
        for m in cls.all:
            m.update_pos()
            

    def update_vel(self, m):
        if self.x < m.x:
            self.xv += 1
        elif self.x > m.x:
            self.xv -= 1

        if self.y < m.y:
            self.yv += 1
        elif self.y > m.y:
            self.yv -= 1

        if self.z < m.z:
            self.zv += 1
        elif self.z > m.z:
            self.zv -= 1

    def update_pos(self):
        self.x += self.xv
        self.y += self.yv
        self.z += self.zv
        self.step += 1

    def get_energi(self):
        self.po_en = abs(self.x) + abs(self.y) + abs(self.z)
        self.ki_en = abs(self.xv) + abs(self.yv) + abs(self.zv)
        return self.po_en * self.ki_en


for l in f:
    val = re.findall('(-*\d+)', l)
    Moon(int(val[0]), int(val[1]), int(val[2]))

#partI
# Moon.print_repr()
# for i in range(1000):
#     Moon.update_vel_all()
#     Moon.update_pos_all()
# l = [m.get_energi() for m in Moon.all]
# print(sum(l))

steps = 0

bx = set()
by = set()
bz = set()
foundx = None
foundy = None
foundz = None
while True:
    if foundx and foundy and foundz:
        break

    xk = tuple((m.x, m.xv,) for m in Moon.all)
    if xk in bx and foundx is None:
        foundx = steps
    bx.add(xk)

    yk = tuple((m.y, m.yv,) for m in Moon.all)
    if yk in by and foundy is None: 
        foundy = steps
    by.add(yk)

    zk = tuple((m.z, m.zv,) for m in Moon.all)
    if zk in bz and foundz is None:
        foundz = steps
    bz.add(zk)
    
    Moon.update_vel_all()
    Moon.update_pos_all()
    steps += 1

    if steps > 1000000:
        break
print('*****************HERE*************', foundx, foundy, foundz)
def _tmp(x, y):
    return x // math.gcd(x, y) * y
print(_tmp(_tmp(foundx, foundy), foundz))
