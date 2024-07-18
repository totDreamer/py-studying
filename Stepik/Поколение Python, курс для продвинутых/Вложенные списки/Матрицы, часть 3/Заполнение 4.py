n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            matrix[i][j] = 1
        elif i >= j and i >= n - 1 - j:
            matrix[i][j] = 1
for i in matrix:
    print(*i)