class SequenceZip:
    def __init__(self, *sequences):
        self._sequnces = tuple(tuple(seq) for seq in sequences)

    def __len__(self):
        return min(len(seq) for seq in self._sequnces)

    def __iter__(self):
        yield from zip(*self._sequnces)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return tuple(item[index] for item in self._sequnces)
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