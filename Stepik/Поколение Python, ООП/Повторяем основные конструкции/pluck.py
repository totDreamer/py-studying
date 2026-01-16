def pluck(data, path, default=None):
    keys = iter(path.split("."))
    try:
        for key in keys:
            data = data[key]
        return data

    except KeyError:
        return default


d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
print(pluck(d, "x"))

d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
print(pluck(d, "a.b"))

d = {"a": {"b": {"c": {"d": {"e": 4}}}}}
print(pluck(d, "a.b.c"))
