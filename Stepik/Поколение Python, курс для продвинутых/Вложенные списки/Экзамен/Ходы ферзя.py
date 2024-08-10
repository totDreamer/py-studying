key = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
n = input()
m, n = key[n[0]], 8 - int(n[1])  # Обратный порядок строк
matrix = [['.' for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i + j == n + m or i - j == n - m or i == n or j == m:
            matrix[i][j] = '*'
matrix[n][m] = 'Q'

for row in matrix:
    print(*row)
