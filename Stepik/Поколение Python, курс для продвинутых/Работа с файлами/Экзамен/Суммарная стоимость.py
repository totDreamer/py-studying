def mounth_profit(file):
    with open(file, 'r') as f:
        data = [int(s.strip('$\n')) for s in f.readlines()]
        return f'${sum(data)}'
    
print(mounth_profit('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/Экзамен/ledger.txt'))