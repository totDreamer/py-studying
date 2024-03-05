def num_reverse(*, list_numbers : list):
    final_list = []
    for j in range(1, len(list_numbers), 2):
        final_list.append(list_numbers[j])
        final_list.append(list_numbers[j-1])
    if len(list_numbers) % 2 != 0:
        final_list.append(list_numbers[-1])
    return ' '.join(final_list)

print(num_reverse(list_numbers = input().split()))