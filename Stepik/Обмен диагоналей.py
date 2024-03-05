def diag_swap(*, n : int):
    matrix = [[k for k in input().split()] for _ in range(n)]
    for i in range(n):
        matrix[i][i], matrix[-i-1][i] = matrix[-i-1][i], matrix[i][i]
    return matrix


final_ans = diag_swap(n = int(input()))
for i in final_ans:
    print(*i, sep=' ')
