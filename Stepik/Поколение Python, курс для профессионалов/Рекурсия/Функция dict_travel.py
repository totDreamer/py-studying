def dict_travel(data, path=None):
    if path is None:
        path = []
    for key, value in sorted(data.items()):
        if not isinstance(value, dict):
            print(f'{".".join(path + [key])}: {value}')
        else:
            dict_travel(value, path + [key])

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)