import math
import pickle
import numpy as np
f = open('input.txt').readlines()



class Asteroid:

    all = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = {}
        self.id = len(Asteroid.all)
        self.ag = {}
        self._visible_sorted = None


    def distance_to(self, a):
        return math.sqrt((self.x - a.x)**2 + (self.y - a.y)**2)

    def is_between(self, b, c):
        eps = 0.00001
        return abs(self.distance_to(c) + b.distance_to(c) - self.distance_to(b)) < eps

    @classmethod
    def extract_asteroids(cls, grid):
        cls.all = []
        for i, g in enumerate(grid):
            for j, c in enumerate(g):
                if c == '#':
                    cls.all.append(Asteroid(j, i))
        dim = len(cls.all)
        cls.angle = np.zeros((dim, dim)) - 1

    def is_visible(self, a):
        if self.id in a.visible:
            return a.visible[self.id]
        if a.id in self.visible:
            return self.visible[a.id]
        for c in Asteroid.all:
            if c!=self and c!=a:
                if self.is_between(a, c):
                    return False
        return True

    def get_visible(self):
        for a in Asteroid.all:
            if a != self:
                if self.is_visible(a):
                    self.visible[a] = True
                    a.visible[self] = True
                else:
                    self.visible[a] = False
                    a.visible[self] = False

        return len([a for a in self.visible if self.visible[a]])

    def get_angle(self, a):
        if self in a.ag:
            return a.ag[self]
        if a in self.ag:
            return self.ag[a]
        vy = a.y - self.y
        vx = a.x - self.x
        sz = math.sqrt(vy*vy + vx*vx)
        vy /= sz
        vx /= sz
        wy = -1
        wx = 0
        _aa = -1 * (math.atan2(wy, wx) - math.atan2(vy, vx))
        aa =  _aa * 180 / np.pi
        if _aa < 0:
            aa += 360
        self.ag[a] = aa
        a.ag[self] = aa

        return aa

    def sort_visible(self):
        aa = []
        l = []
        for a in self.visible:
            if self.visible[a]:
                aa.append(self.get_angle(a))
                l.append(a)
        self._visible_sorted = np.array(aa).argsort()
        for j, i in enumerate(self._visible_sorted):
            if j==199:
                print(100 * l[i].x + l[i].y)

        
       
    @classmethod
    def compute_visible(cls):
        l=[]
        for a in cls.all:
            nvis = a.get_visible()
            l.append(nvis)
        cls.vis_num = np.array(l)
        id = np.argmax(cls.vis_num)
        cls.station = cls.all[id]

if __name__ == "__main__":
    Asteroid.extract_asteroids(f)
    Asteroid.compute_visible()
    a = Asteroid.station
    print('STATION POS: ', a.x, a.y)
    Asteroid.station.sort_visible()


