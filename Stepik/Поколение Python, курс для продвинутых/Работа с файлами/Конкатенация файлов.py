n = int(input())
with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/output.txt', 'w', encoding='utf') as f:
    for _ in range(n):
        name = input()
        with open(f'D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/{name}', 'r', encoding='utf') as f2:
            for line in f2:
                f.write(line)