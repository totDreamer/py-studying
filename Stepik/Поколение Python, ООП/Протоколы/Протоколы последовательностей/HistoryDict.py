_sentinel = object()


class HistoryDict:
    def __init__(self, data=_sentinel):
        self.data = dict(data) if data is not _sentinel else dict()
        self._history = {key: [value] for key, value in self.data.items()}

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self._history.setdefault(key, []).append(value)

    def __delitem__(self, key):
        del self.data[key]
        del self._history[key]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __contains__(self, key):
        return key in self.data

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history


historydict = HistoryDict({"ducks": 99, "cats": 1})

print(historydict["ducks"])
print(historydict["cats"])
print(len(historydict))
print()


historydict = HistoryDict({"ducks": 99, "cats": 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())
print()


historydict = HistoryDict({"ducks": 99, "cats": 1})

historydict["ducks"] = 100
print(historydict.history("ducks"))
print(historydict.history("cats"))
print(historydict.history("dogs"))
print()


historydict = HistoryDict({"ducks": 99, "cats": 1})

print(historydict.all_history())
historydict["ducks"] = 100
historydict["ducks"] = 101
historydict["cats"] = 2
print(historydict.all_history())
