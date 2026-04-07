class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, "__iter__"):
            return self.__class__(list(self) + list(other))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, "__iter__"):
            return self.__class__(list(other) + list(self))
        return NotImplemented

    def __iadd__(self, other):
        if hasattr(other, "__iter__"):
            return self.__class__(list(self) + list(other))
        return NotImplemented


advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({"a": 1, "b": 2} + advancedtuple)
print()


advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))
