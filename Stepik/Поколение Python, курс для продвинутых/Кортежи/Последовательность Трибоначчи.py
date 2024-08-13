n = int(input())
final_list = []
f1, f2, f3 = 1, 1, 1
for i in range(n):
    final_list.append(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3
print(*final_list)