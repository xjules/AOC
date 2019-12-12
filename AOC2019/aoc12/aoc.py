import numpy as np
import re
f = open('input1.txt').readlines()


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
        Moon.all.append(self)

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

    def get_energi(self):
        self.po_en = abs(self.x) + abs(self.y) + abs(self.z)
        self.ki_en = abs(self.xv) + abs(self.yv) + abs(self.zv)
        return self.po_en * self.ki_en


for l in f:
    val = re.findall('\d+', l)
    print(val)
    Moon(int(val[0]), int(val[1]), int(val[2]))

for i in range(10):
    Moon.update_vel_all()
    Moon.update_pos_all()


for m in Moon.all:
     print('x={} y={} z={}'.format(m.x, m.y, m.z))

l = [m.get_energi() for m in Moon.all]
print(sum(l))
