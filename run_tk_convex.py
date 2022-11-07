#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from my import Zero


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
h = Zero()

tk.clean()

try:
    while True:
        x = int(input("x->"))
        y = int(input("y->"))
        f = f.add(R2Point(x, y))
        h = h.add(R2Point(x, y))
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, Smod = {h.area()}")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()