from collections import ChainMap

def deep_update(chainmap, key, value):
    if key not in chainmap.keys():
        chainmap.maps[0][key] = value
    else:
        for d in chainmap.maps:
            if key in d:
                d[key] = value

    return None

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)