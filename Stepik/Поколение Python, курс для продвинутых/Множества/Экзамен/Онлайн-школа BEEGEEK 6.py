n = int(input())
default_set = set()
for i in range(n):
    if i == 0:
        m = int(input())
        for _ in range(m):
            default_set.add(input())
    else:
        m = int(input())
        new_set = set()
        for _ in range(m):
            new_set.add(input())
        default_set.intersection_update(new_set)
print(*sorted(default_set), sep='\n')