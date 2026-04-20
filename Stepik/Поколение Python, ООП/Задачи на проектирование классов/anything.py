import math, re


class AnyTrue:
    def __eq__(self, other):
        return True

    __ne__ = __gt__ = __lt__ = __ge__ = __le__ = __eq__


def anything():
    return AnyTrue()


print(anything() != [])
print(anything() < "World")
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)
