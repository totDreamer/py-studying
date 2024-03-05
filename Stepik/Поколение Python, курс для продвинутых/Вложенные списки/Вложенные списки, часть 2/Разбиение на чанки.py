def chunk(*, list : str, n : int):
    list = list.split()
    final_list = []
    while len(list) > 0:
        final_list.append(list[:n])
        list = list[n:]
    return final_list

print(chunk(list = input(), n = int(input())))