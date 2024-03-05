def more_average(*, num: int):
    matrix = [[] for _ in range(num)]
    count = [[] for _ in range(num)]
    for i in range(num):
        matrix[i].extend(int(j) for j in input().split())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > sum(matrix[i]) // len(matrix[i]):
                count[i].append(matrix[i][j])
    return count


count_list = more_average(num=int(input()))
for i in count_list:
    print(len(i))
