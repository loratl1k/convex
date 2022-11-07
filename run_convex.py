#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from my import Zero

h = Zero()
f = Void()
try:
    while True:
        x = int(input("x->"))
        y = int(input("y->"))
        f = f.add(R2Point(x, y))
        h = h.add(R2Point(x, y))
        print(f"S = {f.area()}, P = {f.perimeter()}, Smod = {h.area()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
