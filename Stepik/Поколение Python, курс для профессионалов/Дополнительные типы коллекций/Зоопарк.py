import json
from collections import ChainMap

path = '/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/zoo.json'
with open(path, 'r', encoding='UTF-8') as f:
    data = ChainMap(*json.load(f))
    result = 0
    
    for v in data.values():
        result += v

    print(result)