from collections.abc import Set


class BitArray(Set):
    def __init__(self, iterable=None):
        self.iterable = iterable[:] if iterable else []

    def __str__(self):
        return f"[{', '.join(map(str, self.iterable))}]"

    def __iter__(self):
        yield from self.iterable

    def __contains__(self, obj):
        return obj in self.iterable

    def __len__(self):
        return len(self.iterable)

    def __invert__(self):
        return self.__class__([1 - num for num in self.iterable])

    def __getitem__(self, index):
        return self.iterable[index]

    def __and__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if len(self.iterable) != len(other.iterable):
            raise TypeError("Списки должны быть равной длины")
        return self.__class__([f & s for f, s in zip(self.iterable, other.iterable)])

    def __or__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if len(self.iterable) != len(other.iterable):
            raise TypeError("Списки должны быть равной длины")
        return self.__class__([f | s for f, s in zip(self.iterable, other.iterable)])


bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)
print()


bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))
print()


data1 = [0, 1, 1, 0, 0, 1]
data2 = [1, 1, 1, 1, 1]

bitarray1 = BitArray(data1)
bitarray2 = BitArray(data2)

try:
    print(bitarray1 | bitarray2)
except TypeError:
    print("Списки должны быть равной длины")

try:
    print(bitarray1 & bitarray2)
except TypeError:
    print("Списки должны быть равной длины")
