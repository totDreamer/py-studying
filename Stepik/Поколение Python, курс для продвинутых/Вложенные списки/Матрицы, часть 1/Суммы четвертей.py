def sum_of_quarters(*, num: int):
    matrix = [[] for _ in range(num)]
    quarters_sum = [[0] for _ in range(4)]
    for i in range(len(matrix)):
        matrix[i].extend([int(i) for i in input().split()])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j and i < num - 1 - j:
                quarters_sum[0][0] += matrix[i][j]
            elif num - 1 - j < i < j:
                quarters_sum[1][0] += matrix[i][j]
            elif j < i and num - 1 - j < i:
                quarters_sum[2][0] += matrix[i][j]
            elif j < i < num - 1 - j:
                quarters_sum[3][0] += matrix[i][j]
    return quarters_sum


final_sum = sum_of_quarters(num=int(input()))
print(f"Верхняя четверть: {sum(final_sum[0])}", f"Правая четверть: {sum(final_sum[1])}", f"Нижняя четверть: {sum(final_sum[2])}", f"Левая четверть: {sum(final_sum[3])}", sep = "\n")