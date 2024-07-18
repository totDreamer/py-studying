n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
count = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1
for j in range(1, n, 2):
    matrix[j] = reversed(list(matrix[j]))
for i in matrix:
    print(*i)