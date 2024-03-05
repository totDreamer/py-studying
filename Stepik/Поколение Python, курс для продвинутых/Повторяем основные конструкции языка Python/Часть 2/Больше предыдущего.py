def more_then_last(*, list_numbers : list):
    count_num = 0
    for j in range(1, len(list_numbers)):
        if int(list_numbers[j]) > int(list_numbers[j - 1]):
            count_num += 1
    return count_num

print(more_then_last(list_numbers = input().split()))