import json

in_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data1.json'
in_path_2 = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data2.json'
out_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data_merge.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
    open(in_path_2, 'r', encoding='UTF-8', newline='') as f2, \
        open(out_path, 'w', encoding='UTF-8', newline='') as fo:
    data = json.load(f)| json.load(f2)
    json.dump(data, fo)