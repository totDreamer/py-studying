def col_swap(*, n : int, m : int):
    matrix = [input().split() for _ in range(n)]
    swap_list = [int(i) for i in input().split()]
    x = swap_list[0]
    y = swap_list[1]
    for i in range(len(matrix)):
        matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
    return matrix

final_matrix = col_swap(n = int(input()), m = int(input()))
for i in range(len(final_matrix)):
    print(*final_matrix[i])