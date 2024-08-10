n = int(input())
matrix = [input().split() for _ in range(n)]
new_matrix = [[]for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_matrix[j].append(matrix[i][j])

if matrix[0] == new_matrix[-1][::-1]:
    print('YES')
else:
    print('NO')