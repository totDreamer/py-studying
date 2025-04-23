import csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/deniro.csv', 'r', encoding='UTF-8', newline='') as f:
    data = list(csv.reader(f))
    n = int(input()) - 1
    sort_data = sorted(data, key=lambda x: int(x[n]) if x[n].isdigit() else x[n])

    for row in sort_data:
        print(*row, sep=',')