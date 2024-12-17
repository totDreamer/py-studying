with open('text.txt', 'r', encoding='UTF') as file:
    print(file.readline()[::-1])