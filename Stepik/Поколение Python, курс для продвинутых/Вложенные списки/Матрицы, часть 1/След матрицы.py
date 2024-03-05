def matrix_track(*, num : int):
    matrix = [[] for _ in range(num)]
    track = 0
    for i in range(num):
        matrix[i].extend(input().split())
    for i in range(num):
        track += int(matrix[i][i])
    return track


print(matrix_track(num=int(input())))