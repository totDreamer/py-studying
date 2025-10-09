def hash_as_key(objects):
    result = {}
    for obj in objects:
        result[hash(obj)] = result.get(hash(obj), [])
        result[hash(obj)].append(obj)
    for key, value in result.items():
        if len(value) == 1:
            result[key] = result[key][0]
    return result

data = [1, 2, 3, 4, 5, 5]
print(hash_as_key(data))


data = [5, 5, 5]
print(hash_as_key(data))