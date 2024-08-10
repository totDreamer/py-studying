n = int(input())
matrix = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j or i == n // 2 or j == n // 2:
            matrix[i][j] = '*'

for i in matrix:
    print(*i)