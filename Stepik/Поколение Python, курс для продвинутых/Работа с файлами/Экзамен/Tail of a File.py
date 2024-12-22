def tail_of_a_file(file, n):
    with open(file, 'r', encoding='utf') as f:
        lines = f.readlines()
        if n > len(lines):
            return lines
        else:
            return lines[-n:]


for line in tail_of_a_file('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/tail_of_a_file.txt', 10):
    print(line.strip())