class AdvancedList(list):
    def join(self, separate=" "):
        return f"{separate}".join(map(str, self))

    def map(self, func):
        self[:] = list(map(func, self))
        return self

    def filter(self, func):
        self[:] = list(filter(func, self))
        return self


advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join("-"))
print()


advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
print()


advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)
print()


advancedlist = AdvancedList([0, 1, 2, "", 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)
