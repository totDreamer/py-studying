first_set = set(list(map(int, input().split())))
second_set = set(list(map(int, input().split())))
third_set = first_set.intersection(second_set)
if third_set:
    print(*sorted(third_set, reverse=True))
else:
    print('BAD DAY')