import csv
from collections import namedtuple
from datetime import datetime

path = '/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/meetings.csv'
with open(path, 'r', encoding='UTF-8') as f:
    title = f.readline().strip().split(',')
    data = csv.reader(f)
    Meet = namedtuple('Meet', title)
    meets = sorted([Meet._make(m) for m in data], key=lambda x: datetime.strptime(f'{x.meeting_date} {x.meeting_time}', '%d.%m.%Y %H:%M'))
    
    for meet in meets:
        print(f'{meet.surname} {meet.name}')