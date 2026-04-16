from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, default=0)

    def __post_init__(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        else:
            self.quadrant = 0

    def symmetric_x(self):
        return self.__class__(self.x, -self.y)

    def symmetric_y(self):
        return self.__class__(-self.x, self.y)


point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)
print()


point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
print()


point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)
