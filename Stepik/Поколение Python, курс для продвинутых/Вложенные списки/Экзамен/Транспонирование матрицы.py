n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
new_matrix = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        new_matrix[j].append(matrix[i][j])

for i in new_matrix:
    print(*i)