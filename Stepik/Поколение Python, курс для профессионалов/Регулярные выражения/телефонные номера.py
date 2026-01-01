from re import search
from sys import stdin

data = [search(r'(?P<country>\d{1,3})(\s|\-)(?P<city>\d{1,3})\2(?P<number>\d{4,10})', line.strip()) for line in stdin]
for number in data:
    num_dict = number.groupdict()
    print(f'Код страны: {num_dict['country']}, Код города: {num_dict['city']}, Номер: {num_dict['number']}')

