def uncommon_sorting(string):
    new_lists = {'l_lit': [], 'u_lit': [], 'odd_num': [], 'even_num': []}
    for char in string:
        if char.isalpha():
            if char.islower():
                new_lists['l_lit'].append(char)
            else:
                new_lists['u_lit'].append(char)
        else:
            if int(char) % 2 != 0:
                new_lists['odd_num'].append(char)
            else:
                new_lists['even_num'].append(char)
    for value in new_lists.values():
        print(*sorted(value), sep='', end='')

uncommon_sorting(input())