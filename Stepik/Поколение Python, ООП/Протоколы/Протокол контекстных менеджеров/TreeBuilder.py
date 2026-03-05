class TreeBuilder:
    def __init__(self):
        self._tree = [[]]

    def __enter__(self):
        self._tree.append([])

    def __exit__(self, *exc_info):
        if self._tree[-1]:
            self._tree[-2].append(self._tree.pop())
        else:
            self._tree.pop()

    def add(self, obj):
        self._tree[-1].append(obj)

    def structure(self):
        return self._tree[0]


tree = TreeBuilder()
print(tree.structure())

tree.add("1st")
print(tree.structure())

with tree:
    tree.add("2nd")
    with tree:
        tree.add("3rd")
    tree.add("4th")
    with tree:
        pass

print(tree.structure())
print()


tree = TreeBuilder()

tree.add("1st")

with tree:
    tree.add("2nd")
    with tree:
        tree.add("3rd")
        with tree:
            tree.add("4th")
            with tree:
                tree.add("5th")
    with tree:
        pass

tree.add("6th")
print(tree.structure())
