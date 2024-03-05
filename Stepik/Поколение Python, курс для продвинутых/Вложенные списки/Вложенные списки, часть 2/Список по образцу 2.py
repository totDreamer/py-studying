def str_list(*, num : int):
    final_list = []
    for i in range(1, num + 1):
        final_list.append(list(range(1, i + 1)))
    print(*final_list, sep = "\n")

str_list(num = int(input()))