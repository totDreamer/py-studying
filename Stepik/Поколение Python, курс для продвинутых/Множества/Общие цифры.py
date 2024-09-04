n = int(input())
final_intersection = set()
for i in range(n):
    if i == 0:
        final_intersection = set((input()))
    else:
        final_intersection.intersection_update(set(input()))
print(*sorted(final_intersection))