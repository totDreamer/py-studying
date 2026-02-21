class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, attr, value):
        if isinstance(value, (int, float)):
            self.__dict__[attr] = abs(value)
        else:
            self.__dict__[attr] = value


point = NonNegativeObject(x=1, y=-2, z=0, color="black")

print(point.x)
print(point.y)
print(point.z)
print(point.color)


point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color="yellow")

print(point.x)
print(point.y)
print(point.z)
print(point.color)
