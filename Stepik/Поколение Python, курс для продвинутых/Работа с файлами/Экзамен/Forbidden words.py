import re
def forb_replace(file):
    with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/forbidden_words.txt', 'r', encoding='utf-8') as f,\
    open(file, 'r', encoding='utf-8') as f2:
        forb_words = f.read().split()
        replaced_text = []
        for line in f2:
            for word in forb_words:
                line = re.sub(word, '*' * len(word), line, flags=re.IGNORECASE)
            replaced_text.append(line)
    return replaced_text
            

for line in forb_replace('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/stepik.txt'):
    print(line, end='')