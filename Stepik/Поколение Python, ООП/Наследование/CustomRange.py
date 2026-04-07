from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *sequences):
        self.sequence = []
        for seq in sequences:
            if isinstance(seq, str):
                start, end = int(seq.split("-")[0]), int(seq.split("-")[1]) + 1
                self.sequence.extend(range(start, end))
            elif isinstance(seq, int):
                self.sequence.append(seq)
            else:
                raise NotImplementedError

    def __getitem__(self, index):
        return self.sequence[index]

    def __len__(self):
        return len(self.sequence)


customrange = CustomRange(1, "2-5", 5, "6-8")

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])
print()


customrange = CustomRange(1, "2-5", 3, "1-4")

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)
print()


customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))
