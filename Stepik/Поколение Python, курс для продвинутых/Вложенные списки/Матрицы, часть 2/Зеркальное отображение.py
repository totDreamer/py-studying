def mirror_list(*, n: int):
    matrix = [[i for i in input().split()] for _ in range(n)]
    for i in range(n//2):
        matrix[i], matrix[-i-1] = matrix[-i-1], matrix[i]
    return matrix


result = mirror_list(n = int(input()))
for list in result:
    print(*list)