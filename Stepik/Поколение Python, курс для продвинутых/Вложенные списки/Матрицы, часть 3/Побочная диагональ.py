def side_diag(*, num : int):
    matrix = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        flag = False
        for j in range(num):
            if flag:
                matrix[i][j] = 2
            if j == num - i - 1:
                matrix[i][j] = 1
                flag = True
    return matrix

side_matrix = side_diag(num = int(input()))
for i in side_matrix:
    print(*i)