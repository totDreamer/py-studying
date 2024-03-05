def pod_list(*, string : str):
    first_list = string.split()
    final_list = [[]]
    for i in range(len(first_list)):
        for j in range(i, len(first_list)):
            final_list.append(first_list[i:j+1])
    return sorted(final_list, key=len)

print(pod_list(string = input()))