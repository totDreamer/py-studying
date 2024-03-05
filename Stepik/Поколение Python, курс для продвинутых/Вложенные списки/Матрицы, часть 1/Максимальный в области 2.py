def max_in_area_2(*, num: int):
    matrix = [[] for i in range(num)]
    max_num = -1000
    for i in range(num):
        matrix[i].extend(int(j) for j in input().split())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j <= i <= num - 1 - j or num - 1 - j <= i <= j:
                if matrix[i][j] > max_num:
                    max_num = matrix[i][j]
    return max_num


print(max_in_area_2(num=int(input())))