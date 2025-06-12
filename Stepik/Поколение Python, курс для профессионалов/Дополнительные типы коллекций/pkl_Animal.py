import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

path = '/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/data.pkl'
with open(path, 'rb') as f:
    data = pickle.load(f)
    for animal in data:
        for field, value in zip(Animal._fields, animal):
            print(f'{field}: {value}')
        print()
