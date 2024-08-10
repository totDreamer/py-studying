s, n = input().split(), int(input())
final_list = []
for i in range(n):
    new_list = []
    for j in s[i::n]:
        new_list.append(j)
    final_list.append(new_list)

print(final_list)