def union_of_sets(n):
    sets = [set(input().split(', ')) for _ in range(n)]
    common_elements = list(set.intersection(*sets))
    if common_elements:
        return sorted(common_elements)
    else:
        return ['Сериал снять не удастся']

print(*union_of_sets(int(input())), sep=', ')