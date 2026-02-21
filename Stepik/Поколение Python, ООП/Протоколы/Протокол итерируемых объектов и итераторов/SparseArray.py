class SparseArray:
    def __init__(self, default=0):
        self.array = dict()
        self.default = default

    def __getitem__(self, key):
        if key not in self.array:
            return self.default
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])


array = SparseArray(None)

array[0] = "Timur"
array[1] = "Arthur"

print(array[0])
print(array[1])
print(array[2])
