n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max = 0

for i in range(n):
    for j in range(n):
        if i >= j and i >= n - 1 - j or i <= j and i >= n - 1 - j:
            if max < matrix[i][j]:
                max = matrix[i][j]
print(max)