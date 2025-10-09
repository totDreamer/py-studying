def print_operation_table(operation, rows, cols):
    matrix = [[operation(n, m) for m in range(1, cols + 1)] for n in range(1, rows + 1)]
    for row in matrix:
        print(*row)

print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)