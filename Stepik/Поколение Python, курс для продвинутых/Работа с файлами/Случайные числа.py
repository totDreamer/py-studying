from random import randrange
with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/random.txt', 'w', encoding='utf') as f:
    for _ in range(25):
        f.write(str(randrange(111, 777)) + '\n')