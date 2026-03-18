from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(iterable)
        self._default = default

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return self._default


defaultlist = DefaultList([1, 2, 3])

print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])
print()


defaultlist = DefaultList([1, 2, 3], 0)

print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])
