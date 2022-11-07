#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from my import Zero

f = Zero()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
