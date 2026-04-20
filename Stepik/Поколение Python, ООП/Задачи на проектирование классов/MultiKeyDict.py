from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, original_key, alias_key):
        if original_key not in self.data:
            raise KeyError(original_key)
        self.aliases[alias_key] = original_key

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if key in self.aliases:
            original_key = self.aliases[key]
            if original_key in self.data:
                return self.data[original_key]
            if original_key in self.aliases:
                return self[original_key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key] = value
        elif key in self.aliases:
            original_key = self.aliases[key]
            if original_key in self.data:
                self.data[original_key] = value
            else:
                self.data[key] = value
                del self.aliases[key]
        else:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            value = self.data[key]
            aliases_list = [k for k, v in self.aliases.items() if v == key]
            del self.data[key]
            if aliases_list:
                new_key = aliases_list[0]
                self.data[new_key] = value
                for alias in aliases_list[1:]:
                    self.aliases[alias] = new_key
        elif key in self.aliases:
            original_key = self.aliases[key]
            if original_key in self.data:
                value = self.data[original_key]
                aliases_list = [k for k, v in self.aliases.items() if v == original_key]
                del self.data[original_key]
                if aliases_list:
                    new_key = aliases_list[0]
                    self.data[new_key] = value
                    for alias in aliases_list[1:]:
                        self.aliases[alias] = new_key
            del self.aliases[key]
        else:
            raise KeyError(key)

    def __contains__(self, key):
        if key in self.data:
            return True
        if key in self.aliases:
            original_key = self.aliases[key]
            return original_key in self.data or original_key in self.aliases
        return False

    def __len__(self):
        return len(self.data)

    def clear(self):
        self.data.clear()
        self.aliases.clear()

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError(f"update expected at most 1 argument, got {len(args)}")
            other = args[0]
            if hasattr(other, "items"):
                for key, value in other.items():
                    self[key] = value
            else:
                for key, value in other:
                    self[key] = value
        for key, value in kwargs.items():
            self[key] = value


# TEST_11:
multikeydict = MultiKeyDict(x=100, y=200, z=300)

multikeydict.alias("x", "t")
multikeydict.alias("y", "q")

print(len(multikeydict))

del multikeydict["y"]

print(len(multikeydict))

multikeydict.clear()

print(len(multikeydict))
print()


# TEST_12:
multikeydict = MultiKeyDict(x=100, y=200, z=300)

multikeydict.alias("x", "t")
multikeydict.alias("y", "q")

multikeydict.update({"t": 400, "q": 500})

print(multikeydict["x"], multikeydict["t"])
print(multikeydict["y"], multikeydict["q"])
print(len(multikeydict))

multikeydict.update({"a": 600, "b": 700})
print(len(multikeydict))
