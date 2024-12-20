from random import choice as ch
with open('first_names.txt', 'r', encoding='UTF') as name, open('last_names.txt', 'r', encoding='utf') as surname:
    names = [x.rstrip() for x in name.readlines()]
    surnames = [y.rstrip() for y in surname.readlines()]
    for _ in range(3):
        print(f'{ch(names)} {ch(surnames)}')