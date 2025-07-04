from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if key not in chainmap.keys():
        return None
    else:
        if from_left:
            return chainmap[key]
        else:
            return ChainMap(*chainmap.maps[::-1])[key]

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))