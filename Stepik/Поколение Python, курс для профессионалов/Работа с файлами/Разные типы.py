import json

def mod_return(obj):
    if isinstance(i, bool):
        return not i
    elif isinstance(i, int):
        return i+1
    elif isinstance(i, str):
        return f'{i}!'
    elif isinstance(i, list):
        return i+i
    elif isinstance(i, dict):
        return i | {'newkey': None}

with open('/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data.json', 'r', encoding='UTF-8', newline='') as f, \
    open('/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/updated_data.json', 'w', encoding='UTF-8', newline='') as f2:
        data = json.load(f)
        new_data = []
        for i in data:
            if i!=None:
                new_data.append(mod_return(i))
        json.dump(new_data, f2)