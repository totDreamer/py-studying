def rev(*, num : int):
    matrix = [input().split() for _ in range(num)]
    new_matrix = [["" for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            new_matrix[i][j] = matrix[j][i]
    for i in range(num):
        new_matrix[i].reverse()
    return new_matrix


final = rev(num=int(input()))
for ans in final:
    print(*ans)