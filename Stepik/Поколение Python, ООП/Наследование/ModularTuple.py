class ModularTuple(tuple):
    def __new__(cls, iterable=[], size=100):
        instance = super().__new__(cls, map(lambda x: x % size, iterable))
        return instance


modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))
print()


modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)
print()


modulartuple = ModularTuple()
print(modulartuple)
print()


modulartuple = ModularTuple([1, 2, 3, 4, 5], 1)

print(modulartuple)
print()


data = [1, 2, 3, 4, 5]
modulartuple = ModularTuple(data, -5)

print(modulartuple)

data.extend([6, 7, 8, 9, 10])
print(data)
print(modulartuple)
