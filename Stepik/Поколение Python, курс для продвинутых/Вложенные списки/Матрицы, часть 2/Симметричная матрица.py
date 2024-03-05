def matrix_symetry(*, n : int):
    matrix = [[i for i in input().split()] for i in range(n)]
    flag = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return "NO"
    return "YES"

print(matrix_symetry(n = int(input())))