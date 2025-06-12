import pickle

def ctrl_sum(filename, number):
    with open(filename, 'rb') as pf:
        data = pickle.load(pf)
        num_l = [n for n in data if isinstance(n, int)]

        if isinstance(data, list):
            ctrl = max(num_l, default=0) * min(num_l, default=0)
        else:
            ctrl = sum(num_l)
        
        if ctrl == number:
            return 'Контрольные суммы совпадают'
        else:
            return 'Контрольные суммы не совпадают'

name = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/numbers.pkl'
print(ctrl_sum(name, 4))