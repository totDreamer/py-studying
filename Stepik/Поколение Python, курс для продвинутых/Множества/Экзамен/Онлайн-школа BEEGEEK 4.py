first_names = set(input().split())
second_names = set(input().split())
all_names = first_names.union(second_names)
print(*sorted(all_names))