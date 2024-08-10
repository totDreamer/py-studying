n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
new_matrix = [[] for _ in range(n)]
flag = True
latin_list = [i for i in range(1, n + 1)]
for i in range(n):
    for j in range(n):
        new_matrix[j].append(matrix[i][j])

for i in range(n):
    if latin_list != sorted(matrix[i]) or latin_list != sorted(new_matrix[i]):
        flag = False
        break

if flag == True:
    print('YES')
else:
    print('NO')