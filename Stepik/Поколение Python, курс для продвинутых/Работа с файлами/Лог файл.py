def minutes(x):
    res=[int(i) for i in x.split(':')]
    return res[0]*60+res[1]

with open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/logfile.txt', 'r', encoding='utf') as f,\
open('D:/Python-Studying/Stepik/Поколение Python, курс для продвинутых/Работа с файлами/logfile_output.txt', 'w', encoding='utf') as f2:
    lines = [line.rstrip().split(', ') for line in f.readlines()]
    online_time = {value[0] : minutes(value[2]) - minutes(value[1]) for value in lines}
    for key, value in online_time.items():
        if value >= 60:
            f2.write(f'{key}\n')