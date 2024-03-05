def max_in_area(*, num: int):
    matrix = [[] for i in range(num)]
    max_num = -1000
    for i in range(num):
        matrix[i].extend(int(j) for j in input().split())
    for i in range(len(matrix)):
        for j in range(len(matrix[:i+1])):
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]
    return max_num


print(max_in_area(num=int(input())))