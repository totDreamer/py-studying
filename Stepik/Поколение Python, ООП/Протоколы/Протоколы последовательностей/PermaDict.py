_sentinel = object()


class PermaDict:
    def __init__(self, data=_sentinel):
        self.data = dict(data) if data is not _sentinel else dict()

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError("Изменение значения по ключу невозможно")
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]


permadict = PermaDict({"name": "Timur", "city": "Moscow"})

print(permadict["name"])
print(len(permadict))


permadict = PermaDict({"name": "Timur", "city": "Moscow", "age": 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())
