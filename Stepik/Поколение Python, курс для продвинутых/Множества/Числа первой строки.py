first_set, second_set = set(map(int, input().split())), set(map(int, input().split()))
print(*sorted(first_set - second_set))