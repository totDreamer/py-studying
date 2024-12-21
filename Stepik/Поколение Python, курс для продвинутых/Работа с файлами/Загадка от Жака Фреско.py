from decimal import Decimal

with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/goats.txt', 'r', encoding='utf') as f, \
open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/answer.txt', 'w', encoding='utf') as f2:
    lines = sorted([line.rstrip() for line in f.readlines() if line != 'GOATS\n' and line != 'COLOURS\n'])
    colours_dict = {}
    all_sum = 0
    for line in lines:
        colours_dict[line] = colours_dict.get(line, -1) + 1
        all_sum += 1
    for key, value in colours_dict.items():
        if value > all_sum * Decimal(0.07):
            f2.write(key +'\n')