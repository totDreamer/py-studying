class Grouper:
    def __init__(self, iterable, key):
        self._groups = dict()
        self.key = key
        for obj in iterable:
            self._groups.setdefault(key(obj), []).append(obj)

    def __len__(self):
        return len(self._groups)

    def __iter__(self):
        yield from self._groups.items()

    def __contains__(self, key):
        return key in self._groups

    def __getitem__(self, key):
        return self._groups[key]

    def add(self, obj):
        self._groups.setdefault(self.key(obj), []).append(obj)

    def group_for(self, obj):
        return self.key(obj)


grouper = Grouper(["bee", "geek", "one", "two", "five", "hi"], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])
print()


grouper = Grouper(["bee", "geek", "one", "two", "five", "hi"], key=len)

print(3 in grouper)
print("bee" in grouper)
print()


grouper = Grouper(["hi"], key=lambda s: s[0])
print(len(grouper))

grouper.add("hello")
grouper.add("bee")
grouper.add("big")

print(len(grouper))

grouper.add("geek")
print(grouper["h"])
print(grouper["b"])
print(grouper["g"])

print(len(grouper))
print()


grouper = Grouper(["hi"], key=lambda s: s[0])

print(grouper.group_for("hello"))
print(grouper.group_for("bee"))
print(grouper["h"])
print("b" in grouper)
