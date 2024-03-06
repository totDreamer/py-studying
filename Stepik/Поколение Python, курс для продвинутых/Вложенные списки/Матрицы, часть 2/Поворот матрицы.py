def reverse(*, num : int):
    matrix = [input().split() for n in range(num)]
    for i in range(num):
        for j in range(num):
            matrix[i][j], matrix[num - j - 1][i] = matrix[num - j - 1][i], matrix[i][j]
    return matrix


print(reverse(num=int(input())))