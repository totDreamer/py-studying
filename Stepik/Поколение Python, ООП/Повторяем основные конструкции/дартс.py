def darts(n):
    n = int(n)
    matrix = [
        [min(row + 1, column + 1, n - row, n - column) for column in range(n)]
        for row in range(n)
    ]
    return matrix


for row in darts(input()):
    print(*row)
