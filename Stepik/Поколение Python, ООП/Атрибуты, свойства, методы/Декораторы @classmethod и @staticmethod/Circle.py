class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


circle = Circle(5)

print(circle.radius)


circle_2 = Circle.from_diameter(10)

print(circle_2.radius)


circle_3 = circle.__class__.from_diameter(10)

print(circle_3.radius)


print(circle == circle_2, circle == circle_3, circle_2 == circle_3)
