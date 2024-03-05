def shift_index(*, list : list):
    final_list = []
    final_list.append(list[-1])
    final_list.extend(list[0:-1])
    return ' '.join(final_list)
print(shift_index(list = input().split()))