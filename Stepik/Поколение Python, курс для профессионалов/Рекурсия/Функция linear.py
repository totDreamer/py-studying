def linear(my_list):
    linear_list = []
    if not my_list:
        return []

    for obj in my_list:
        if isinstance(obj, int):
            linear_list.append(obj)
        if isinstance(obj, list):
            linear_list.extend(linear(obj))

    return linear_list

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))