def magic_square(*, n: int):
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    element_matrix = [int(i) for i in range(1, n * n + 1)]
    flag = True
    sum_flag = sum(matrix[0])
    unique_elements = []
    column_sum = [0 for _ in range(n)]
    main_diagonal_sum = 0
    side_diagonal_sum = 0

    for i in range(n):
        unique_elements.extend(matrix[i])
    unique_elements = list(set(unique_elements))
    if unique_elements != element_matrix:
        flag = False
        return "NO"

    for i in range(n):
        if sum(matrix[i]) != sum_flag:
            flag = False
            return "NO"

    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        for j in range(n):
            column_sum[i] += matrix[j][i]
            if j == n - i - 1:
                side_diagonal_sum += matrix[i][j]

    for i in column_sum:
        if i != sum_flag:
            flag = False
            return "NO"

    if main_diagonal_sum != sum_flag:
        flag = False
        return "NO"

    if side_diagonal_sum != sum_flag:
        flag = False
        return "NO"

    if flag:
        return "YES"
    else:
        return "NO"


print(magic_square(n=int(input())))
