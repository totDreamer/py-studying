def matrix(*, str_num : int, dig_num : int):
    final_list = [[] for _ in range(str_num)]
    final_list_reverse = [[] for _ in range(dig_num)]
    ghost_list = []
    for i in range(str_num):
        for j in range(dig_num):
            ghost = input()
            ghost_list.append(ghost)
            final_list[i].append(ghost)
    while len(ghost_list) != 0:
        for i in range(dig_num):
            final_list_reverse[i].append(ghost_list[0])
            ghost_list.pop(0)
    return final_list, final_list_reverse


matrix_result = matrix(str_num=int(input()), dig_num=int(input()))
for i in range(len(matrix_result)):
    if i != 0:
        print()
    for j in range(len(matrix_result[i])):
        print(" ".join(matrix_result[i][j]))