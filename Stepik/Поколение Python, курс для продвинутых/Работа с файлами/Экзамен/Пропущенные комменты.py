def a_gde(file):
    with open(file, 'r', encoding='utf') as f:
        lines = [line.strip() for line in f.readlines()]
        propusk = []
    for i in range(len(lines)):
        if lines[i].startswith('def') and i != 0:
            if lines[i-1].startswith('#') == False:
                propusk.append(lines[i][lines[i].index(' ')+1:lines[i].index('(')])
        elif lines[i].startswith('def') and i == 0:
            propusk.append(lines[i][lines[i].index(' ')+1:lines[i].index('(')])
    if len(propusk) == 0:
        return ['Best Programming Team']
    else:
        return propusk

print(*a_gde('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/best_programming_team.txt'), sep='\n')

print(*a_gde('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/not_best.txt'), sep='\n')