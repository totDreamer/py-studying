from collections import ChainMap

def get_all_values(chainmap, key):
    result = set()

    for d in chainmap.maps:
        try:
            result.add(d[key])
        except:
            continue

    return result


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)