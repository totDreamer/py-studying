def chess_board(*, n: int, m: int):
    matrix = [["*" for i in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i % 2 == 1 and j % 2 == 1:
                matrix[i][j] = "."
            elif i % 2 == 0 and j % 2 == 0:
                matrix[i][j] = "."
    return matrix


n, m = map(int, input().split())

board = chess_board(n = n, m = m)
for i in range(n):
    print(*board[i])
