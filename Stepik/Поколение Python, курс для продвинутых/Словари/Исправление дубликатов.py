string = input().split()
string_dict = {}
for sym in string:
    if sym not in string_dict:
        string_dict.setdefault(sym, 0)
        print(sym, end=' ')
    else:
        string_dict[sym] += 1
        print(sym+f'_{string_dict[sym]}', end=' ')