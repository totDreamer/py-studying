words = input().split()
list_set = [set(i) for i in words]
print('YES') if list_set[0] == list_set[1] and list_set[0] == list_set[2] else print('NO')