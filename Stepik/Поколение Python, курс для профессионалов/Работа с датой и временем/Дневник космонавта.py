from datetime import datetime

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с датой и временем/diary.txt', mode='r', encoding='UTF-8') as f:
    combo_dict = {}
    text = f.readlines()
    text += '\n'

    d = None
    for line in text:
        if not line:
            continue
        try:
            d = datetime.strptime(line, '%d.%m.%Y; %H:%M\n')
            combo_dict[d] = []
            combo_dict[d].append(line.strip())
            continue
        except ValueError:
            if d is not None:
                combo_dict[d].append(line.strip())
 
    sorted_combo_dict = dict(sorted(combo_dict.items()))
    for case in sorted_combo_dict.values():
        for line in case:
            print(line)