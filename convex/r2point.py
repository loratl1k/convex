from math import sqrt
from math import copysign


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):

        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    def quad(self):
        if self.x >= 0.0 and self.y >= 0.0:
            return True
        else:
            return False

    @staticmethod
    def tri(a, b, c):
        if (copysign(1, a.x * (b.y - a.y) - (b.x - a.x) * a.y) ==
                copysign(1, b.x * (c.y - b.y) - (c.x - b.x) * b.y) and
                copysign(1, a.x * (b.y - a.y) - (b.x - a.x) * a.y) ==
                copysign(1, c.x * (a.y - c.y) - (a.x - c.x) * c.y) and
                copysign(1, b.x * (c.y - b.y) - (c.x - b.x) * b.y) ==
                copysign(1, c.x * (a.y - c.y) - (a.x - c.x) * c.y)):
            return True

        else:
            return False

    @staticmethod
    def oy(t, p):
        if p.y == t.y:
            a = R2Point(p.y, 0)
            return a
        else:
            b = R2Point(t.x - (t.y * (p.x - t.x)) / (p.y - t.y), 0)
            return b

    @staticmethod
    def ox(t, p):
        if p.x == t.x:
            a = R2Point(0, p.x)
            return a
        else:
            b = R2Point(0, t.y - (t.x * (p.y - t.y)) / (p.x - t.x))
            return b

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
