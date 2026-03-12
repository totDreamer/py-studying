from random import randint


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._last_one = 0

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if not self._last_one:
            self._last_one = randint(self._start, self._end)
            return self._last_one
        if self._cache:
            return self._last_one
        return randint(self._start, self._end)

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])
print()


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])
print()


class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)
print()


class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
