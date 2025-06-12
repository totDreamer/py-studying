import pickle

def filter_dump(filename, objects, type):
    objects_type = [o for o in objects if isinstance(o, type)]
    with open(filename, 'wb') as pf:
        pickle.dump(objects_type, pf)

name = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/numbers.pkl'
l = [1, '2', 3, 4, '5']
filter_dump(name, l, int)