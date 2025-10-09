def some_collections(collection):
    data = eval(collection)
    if isinstance(data, list):
        return data[-1]
    elif isinstance(data, tuple):
        return data[0]
    else:
        return len(data)

print(some_collections(input()))