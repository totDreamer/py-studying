def matrix(*, str_num : int, dig_num : int):
    final_list = [[] for i in range(str_num)]
    for i in range(str_num):
        for j in range(dig_num):
            final_list[i].append(input())
    return final_list
matrix_result = matrix(str_num=int(input()), dig_num=int(input()))

for i in matrix_result:
    print(" ".join(i))