def filling_matrix(*, n: int, m: int):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = j * n + i + 1
    return matrix


n, m = map(int, input().split())
result = filling_matrix(n=n, m=m)
for i in result:
    print(*i)