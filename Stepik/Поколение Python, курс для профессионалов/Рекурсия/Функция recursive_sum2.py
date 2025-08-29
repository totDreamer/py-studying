def recursive_sum(nested_lists):
    if not nested_lists:
        return 0
    
    if isinstance(nested_lists[0], list):
        return recursive_sum(nested_lists[0]) + recursive_sum(nested_lists[1:])
    return nested_lists[0] + recursive_sum(nested_lists[1:])

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))