with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/output.txt', 'w', encoding='utf') as f:
    with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/input.txt', 'r', encoding='utf') as f2:
        for index, line in enumerate(f2):
            f.write(f'{index + 1}) {line}')