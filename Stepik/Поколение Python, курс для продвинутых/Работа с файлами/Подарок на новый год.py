with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/class_scores.txt', 'r', encoding='utf') as f:
    scores_dict = {surname: int(result) for surname, result in (line.split() for line in f)}
    with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/new_scores.txt', 'w', encoding='utf') as f2:
        for surname, result in scores_dict.items():
            f2.write(f'{surname} {result + 5 if result <95 else 100}\n')