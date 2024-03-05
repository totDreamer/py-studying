def num_list(*, num : int):
    first_list = []
    final_list = []
    for i in range(num):
        for n in range(1, num + 1):
            first_list.append(n)
        final_list.append(first_list)
        first_list = []
    for i in range(len(final_list)):
        print(final_list[i])


num_list(num = int(input()))