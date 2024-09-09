m, n = int(input()), int(input())
names_set = set()
for _ in range(n+m):
    name = input()
    if name in names_set:
        names_set.remove(name)
    else:
        names_set.add(name)
if names_set:
    print(len(names_set))
else:
    print('NO')