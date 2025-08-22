def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    else:
        if name.istitle() and name.isalpha():
            return len(names) + 1
        else:
            raise ValueError('Имя не является корректным')


names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'
print(get_id(names, name))

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'
try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']
try:
    print(get_id(names, name))
except TypeError as e:
    print(e)