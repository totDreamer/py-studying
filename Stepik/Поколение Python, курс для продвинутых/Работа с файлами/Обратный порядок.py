with open('data.txt', 'r', encoding='UTF') as file:
    print(*file.readlines()[::-1], sep='')