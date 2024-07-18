n, m = map(int, input().split())
matrix = [[i for i in range(1, m + 1)] for _ in range(n)]
for j in range(1, n):
    move = matrix[j].pop(0)
    matrix[j].append(move)
    if len(matrix) - j > 1:
        matrix[j+1] = list(matrix[j])
for i in matrix:
    print(*i)