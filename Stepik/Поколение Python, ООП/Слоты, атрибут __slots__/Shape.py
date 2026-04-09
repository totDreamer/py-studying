from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ("name", "color", "area")

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f"{self.color} {self.name} ({self.area})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area == other.area

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area > other.area


shape = Shape("triangle", "red", 12)

print(shape.name)
print(shape.color)
print(shape.area)
print()


print(Shape('Square', 'Red', 4))
print()


print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
print()


shape = Shape('triangle', 'red', 12)

try:
    shape.perimeter = 9
except AttributeError:
    print('Error')