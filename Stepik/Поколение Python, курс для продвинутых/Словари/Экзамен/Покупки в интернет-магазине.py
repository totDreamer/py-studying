result = {}

for _ in range(int(input())):
    name, item, count = input().split()
    if name not in result:
        result[name] = {item: int(count)}
    else:
        if item not in result[name]:
            result[name][item] = int(count)
        else:
            result[name][item] += int(count)

for key, value in sorted((result).items()):
    print(f'{key}:')
    for k, v in sorted(value.items()):
        print(f'{k} {v}')
 