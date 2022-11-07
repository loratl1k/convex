from deq import Deq
from r2point import R2Point
from convex import Void


class Quarter:

    def area(self):
        return 0.0

    def rip(self):
        return 0.0
    

class Zero(Quarter):

    def __init__(self):
        self.r = []

    def add(self, t):
        return One(self.r, t)


class One(Quarter):

    def __init__(self, r, t):
        self.t = t
        self.r = r
        if t.quad() == True:
            self.r.append(t)

    def add(self, p):
        return Two(self.r, self.t, p)

    
class Two(Quarter):

    def __init__(self, r, t, p):
        self.t = t
        self.r = r
        self.p = p
        if p.quad() == True:
            self.r.append(p)
        a = R2Point.Ox(p, t)
        if a.is_inside(self.t, self.p):
            if a.quad() == True:
                self.r.append(a)
        b = R2Point.Oy(p, t)
        if b.is_inside(self.t, self.p):
            if b.quad() == True:
                self.r.append(b)

    def add(self, q):
        return Three(self.r, self.t, self.p, q)

class Three(Quarter):

    def __init__(self, r, t, p, q):
        self.q = q
        self.t = t
        self.r = r
        self.p = p
        self.h = Void()
        if q.quad() == True:
            self.r.append(q)
        a = R2Point.Ox(self.q, self.t)
        if a.is_inside(self.q, self.t):
            if a.quad() == True:
                self.r.append(a)
        b = R2Point.Oy(self.q, self.t)
        if b.is_inside(self.q, self.t):
            if b.quad() == True:
                self.r.append(b)
        d = R2Point.Ox(self.q, self.p)
        if d.is_inside(self.q, self.p):
            if d.quad() == True:
                self.r.append(d)
        v = R2Point.Oy(self.q, self.p)
        if v.is_inside(self.q, self.p):
            if v.quad() == True:
                self.r.append(v)
        if R2Point.tri(self.t, self.p, self.q):
            c = R2Point(0, 0)
            self.r.append(c)
        self.points = Deq()
        self.points.push_first(p)
        if b.is_light(t, q):
            self.points.push_first(t)
            self.points.push_last(q)
        else:
            self.points.push_last(t)
            self.points.push_first(q)
        for i in self.r:
            self.h = self.h.add(i)
        self._area = self.h.area()
            
            

    def add(self, t):
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        if t.is_light(self.points.last(), self.points.first()):

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                p = self.points.pop_last()
            self.points.push_last(p)

            self.points.push_first(t)
        
        if t.quad() == True:
            self.h = self.h.add(t)
            self._area = self.h.area()
        
        for n in range(len(self.r)):
            a = R2Point.Ox(t, self.points.first())
            if a.is_inside(t, self.points.first()):
                if a.quad() == True:
                    self.h = self.h.add(a)
                    self._area = self.h.area()
            b = R2Point.Oy(t, self.points.first())
            if b.is_inside(t, self.points.first()):
                if b.quad() == True:
                    self.h = self.h.add(b)
                    self._area = self.h.area()
            if R2Point.tri(self.t, self.points.last(), self.points.first()):
                c = R2Point(0,0)
                self.h = self.h.add(c)
                self._area = self.h.area()
            self.points.push_last(self.points.pop_first())

        return self

    def area(self):
        return self._area
        

if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)        




































    
    
