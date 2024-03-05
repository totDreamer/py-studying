def streak_coin(*, str : str):
    str_list = str.split('О')
    return len(max(str_list))
print(streak_coin(str = input()))