def double_puck(*, string : str):
    ghost_list = string.split()
    final_list = [[string[0]]]
    for i in range(1, len(ghost_list)):
        if final_list[-1][-1] == ghost_list[i]:
            final_list[-1].append(ghost_list[i])
        else:
            final_list.append(list(ghost_list[i]))
    return final_list


print(double_puck(string = input()))