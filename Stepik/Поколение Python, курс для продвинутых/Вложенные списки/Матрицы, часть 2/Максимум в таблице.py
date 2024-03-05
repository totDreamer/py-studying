def max_index(*, n : int, m : int):
    max_num = -1000
    first_entrance = []
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]
                first_entrance = [str(i), str(j)]
    return " ".join(first_entrance)


print(max_index(n = int(input()), m = int(input())))