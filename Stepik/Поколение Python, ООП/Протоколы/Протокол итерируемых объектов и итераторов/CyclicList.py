from itertools import cycle


_sentinel = object()


class CyclicList:
    def __init__(self, iterable=_sentinel):
        self.array = list(iterable) if iterable is not _sentinel else []

    def append(self, value):
        self.array.append(value)

    def pop(self, index=-1):
        return self.array.pop(self._correct_index(index))

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return cycle(self.array)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.array[self._correct_index(index)]

    def _correct_index(self, index):
        return index % len(self.array)


cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=" ")

    cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))
