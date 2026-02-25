class SequenceZip:
    def __init__(self, *sequences):
        self._sequences = sequences
        self._length = min(len(seq) for seq in sequences) if sequences else 0
        self._cache = {}

    def __len__(self):
        return self._length

    def __iter__(self):
        for i in range(self._length):
            if i not in self._cache:
                self._cache[i] = tuple(seq[i] for seq in self._sequences)
            yield self._cache[i]

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < self._length:
            if index in self._cache:
                return self._cache[index]
            self._cache[index] = tuple(seq[index] for seq in self._sequences)
            return self._cache[index]
        raise IndexError("Индекс должен быть целым числом")


sequencezip = SequenceZip("ABC", ["bee", "geek", "python"], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))
print()


sequencezip = SequenceZip("ABC", ["bee", "geek", "python"], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])
print()


x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])
print()


sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))
print()


data1 = [1, 2, 3, 4, 5]
data2 = "abcde"

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += "fghij"

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))
